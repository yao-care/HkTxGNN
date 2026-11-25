"""HK 證據包補收現行註冊名單上、依本站原本的比對規則屬於本藥、卻不在證據包的註冊號（2026-11-17，用戶要求；全程不用 AI）。

證據包的許可證紀錄（tfda 區塊）是 collectors/hkfda.py 依 data/raw/DrugList.xml（2026-03 版）＋ data/processed/drug_mapping.csv 收的：
藥名 → DrugBank ID → drug_mapping 裡對到同一個 DrugBank ID 的註冊號（單方、複方都收），最多存 20 筆、total_matches 記總數。
之後新註冊的產品不在 drug_mapping，所以永遠收不進來（例：ezetimibe HK-69166 EZETIMIBE TABLETS 10MG，2026-03 版名單還沒有）。
這支照同一套規則補收（不放寬）：
A. 現行名單（DrugList.xml 最新版）有、2026-03 版沒有的註冊號，用本站同一支 mapping（hktxgnn.mapping.drugbank_mapper.map_fda_drugs_to_drugbank）
   對 DrugBank ID；跟證據包的 drugbank_ids 有交集就補一筆（欄位照 hkfda.LocalFDACollector._format），total_matches 同步加
   （這些號不在原本的 total_matches 裡）。
B. 證據包裡已標 drugoffice_not_listed（名單已不列）的紀錄，現行名單上有產品名與成分完全相同、依規則也屬於本藥的另一個註冊號，
   而證據包只收了部分（20 筆上限）沒收到它時，補一筆（例：metformin HK-54377 → HK-56689 METFORMIN TAB 500MG）；
   這種號原本就算在 total_matches 裡，total_matches 不變。
C. 2026-11-17（用戶決定拿掉 20 筆上限）：照原收錄規則把本藥的全部註冊號補齊，證據包不再是部分收錄——
   2026-03 版名單上的號照原規則（data/processed/drug_mapping.csv 的 DrugBank ID）判斷是否屬於本藥，之後新增的號照 A 的規則；
   現行名單上有的補成現行紀錄，2026-03 版有、現行名單已不列的補成已註銷紀錄（license_status＝cancelled、drugoffice_not_listed，
   欄位同 scripts/license_adapter.py 的 preprocess；表示原本算在 total_matches 裡、因上限沒收的舊號）。
   補完 total_matches＝紀錄數（不重複註冊號），t["complete"]＝名單 lastUpdate（給 drug_evidence_pack 的 partial 判定：total_matches 不大於紀錄數＝完整）。
   預設就做 C（每週排程同一支）；--no-complete 只做 A、B（舊行為）。
補的紀錄加 source（名單版本日期）與 added（補收日）。可重複執行、只加不刪（已在證據包的號不重補，已註銷的舊號照舊保留）。
2026-11-25（第五輪，用戶決定）：config/bundle_record_exclusions.json 列的收錯品項（例 sodium_acetate 證據包收到的乳酸林格液）不補、
已移到 tfda.excluded_records 的號也不再補回（規則見 hktxgnn.regulatory.record_exclusions）。
用法（repo 根目錄）：python3 scripts/add_current_registrations.py --xml <現行 DrugList.xml> [--dry-run] [--report out.tsv]
"""
import argparse
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))


def _norm(s):
    return re.sub(r"\s+", " ", str(s or "")).strip().lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--xml", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report")
    ap.add_argument("--no-complete", action="store_true", help="只做 A、B（不依原規則補齊全部註冊號）")
    a = ap.parse_args()
    from hktxgnn.collectors.hkfda import LocalFDACollector
    from hktxgnn.data.loader import filter_active_drugs, load_fda_drugs
    from hktxgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank
    from hktxgnn.regulatory import record_exclusions as RX

    xml = Path(a.xml)
    last = ET.parse(xml).getroot().findtext("lastUpdate") or ""
    cur = load_fda_drugs(xml)
    old = load_fda_drugs(ROOT / "data/raw/DrugList.xml")
    old_ids = set(old["license_id"].astype(str))
    old_rows = {str(r["license_id"]): r for r in old.to_dict("records")}
    if len(cur) < 10000:
        sys.exit(f"現行名單只有 {len(cur)} 筆，疑似下載或格式有問題")
    mp = map_fda_drugs_to_drugbank(filter_active_drugs(cur).rename(
        columns={"license_id": "許可證字號", "brand_name": "中文品名", "ingredients": "主成分略述"}))
    lic_db = {}
    for _, r in mp.iterrows():
        if r["映射成功"]:
            lic_db.setdefault(str(r["許可證字號"]), set()).add(str(r["drugbank_id"]).upper())
    col = LocalFDACollector()
    col._prepare()
    rows = {str(r["license_id"]): r for r in cur.to_dict("records")}
    # C 用的原規則：2026-03 版名單上的號 → drug_mapping.csv 的 DrugBank ID（collectors/hkfda.py 原收錄就是這樣對的）
    dm = {}
    for db, lics in col.db_to_lic.items():
        for lic in lics:
            dm.setdefault(lic, set()).add(db)
    key = {k: (_norm(r.get("brand_name")), tuple(sorted(_norm(x) for x in (r.get("ingredient_list") or [])))) for k, r in rows.items()}
    by_key = {}
    for k, v in key.items():
        by_key.setdefault(v, set()).add(k)
    today = time.strftime("%Y-%m-%d")
    out, n_b = [], 0
    for f in sorted((ROOT / "data/bundles").glob("*/drug_bundle.json")):
        b = json.loads(f.read_text(encoding="utf-8"))
        t = b.get("tfda") or {}
        recs = t.get("records") or []
        dbs = {str(x).upper() for x in (t.get("drugbank_ids") or [])}
        if not dbs or not recs:
            continue
        have = {str(r.get("license_id") or "").strip() for r in recs}
        have |= {str(r.get("license_id") or "").strip() for r in t.get("excluded_records") or []}
        bname = f.parent.name

        def _excl(k):  # 排除表列的收錯品項不補
            row = rows.get(k) or old_rows.get(k) or {}
            return RX.match_ingredients(bname, row.get("ingredients")) is not None
        new_a = sorted(k for k, d in lic_db.items() if k not in have and k not in old_ids and d & dbs)
        partial = int(t.get("total_matches") or 0) > len(recs)
        new_b = set()
        if partial:
            for r in recs:
                if r.get("drugoffice_not_listed"):
                    ok = (_norm(r.get("brand_name_en")), tuple(sorted(_norm(x) for x in re.split(r";\s*", r.get("ingredients") or "") if x)))
                    new_b |= {k for k in by_key.get(ok, ()) if k not in have and k in old_ids and lic_db.get(k, set()) & dbs}
        new_a = [k for k in new_a if not _excl(k)]
        new_b = {k for k in new_b if not _excl(k)}
        add = new_a + sorted(new_b)
        new_c, new_x = [], []
        if not a.no_complete:
            taken = have | set(add)
            new_c = sorted(k for k in rows if k not in taken
                           and ((k in old_ids and dm.get(k, set()) & dbs) or (k not in old_ids and lic_db.get(k, set()) & dbs)))
            new_x = sorted(k for k in old_rows if k not in taken and k not in rows and dm.get(k, set()) & dbs)
            new_c = [k for k in new_c if not _excl(k)]
            new_x = [k for k in new_x if not _excl(k)]
        if not (add or new_c or new_x):
            if not a.no_complete and len({str(r.get("license_id") or "").strip() for r in recs}) >= int(t.get("total_matches") or 0) \
                    and t.get("complete") != last:
                t["total_matches"], t["complete"] = len(recs), last
                b["tfda"] = t
                if not a.dry_run:
                    f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
            continue
        for k in add + new_c + new_x:
            rec = col._format([rows[k] if k in rows else old_rows[k]], set())["records"][0]
            if k in new_x:
                rec["source"] = "衞生署藥物辦公室註冊名單 DrugList.xml（2026-03 版；現行名單 lastUpdate " + last + " 已不列）"
                rec["drugoffice_not_listed"] = today
                rec["license_status"] = "cancelled"
            else:
                rec["source"] = f"衞生署藥物辦公室註冊名單 DrugList.xml（lastUpdate {last}）"
            rec["added"] = today
            if k in new_b:
                rec["same_product_as"] = sorted(r["license_id"] for r in recs if r.get("drugoffice_not_listed")
                                                and _norm(r.get("brand_name_en")) == key[k][0])
            recs.append(rec)
            tag = "A" if k in new_a else "B" if k in new_b else "C" if k in new_c else "X"
            out.append(f"{f.parent.name}\t{tag}\t{k}\t{rec['brand_name_en']}\t{rec['ingredients']}")
        tm = int(t.get("total_matches") or 0)
        if a.no_complete:
            t["total_matches"] = max(tm + len(new_a), len(recs))
        elif len(recs) >= tm:
            t["total_matches"], t["complete"] = len(recs), last
        else:  # 原規則找到的比原本 total_matches 少：不能斷定完整，照舊算部分收錄
            t["total_matches"] = tm + len(new_a)
        t["records"], t["found"] = recs, True
        b["tfda"] = t
        n_b += 1
        if not a.dry_run:
            f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"補收 {len(out)} 筆、{n_b} 個證據包（名單 lastUpdate {last}）{'（試跑，未寫回）' if a.dry_run else ''}")
    if a.report:
        Path(a.report).write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
