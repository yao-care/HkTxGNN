"""HK（衛生署藥物辦公室 DrugList.xml）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：https://www.drugoffice.gov.hk/eps/psi/DrugList.xml（免金鑰，有 lastUpdate）。只列現行註冊的藥劑製品、沒有狀態欄：
在列＝status 維持原值（證據包原本是空白，reviewer 視為有效），新清單查不到的註冊號保留原狀態、列在 summary（不推定為撤銷）。
證據包 license_id＝permitNo（HK-xxxxx）。
2026-11-17（用戶要求確認查不到的註冊號）：DrugList.xml 是藥物辦公室唯一的公開註冊名單（DrugList-v1.1.xml 內容相同，
網上「搜尋藥物資料庫」也只查得到現行註冊），沒有另一份現行或已取消清單。11-16 查不到的 146 張全部在 data.gov.hk 歷史存檔
（2025-08～2026-11-02 的每週 DrugList.xml）裡出現過、之後不再列，網上資料庫也查不到＝已不是現行註冊（取消或沒有續期，名單不分原因）。
所以名單有成功下載、而且至少 MIN_CURRENT 張時，preprocess 對名單沒有的 HK-xxxxx 標 license_status＝cancelled 與
drugoffice_not_listed（第一次發現日）；之後又出現在名單就取消標記。下載失敗或筆數過少時不判定（維持原狀態）。
"""
import re
import time
import xml.etree.ElementTree as ET

import requests

RAW_FILE = "raw/hk_druglist_permits.json"
URL = "https://www.drugoffice.gov.hk/eps/psi/DrugList.xml"
CURRENT: set = set()   # fetch() 填：DrugList.xml 的現行註冊號；空的就不做「不在名單」判定
MIN_CURRENT = 10000    # 少於這個數＝下載或格式有問題，不判定
ID_RE = re.compile(r"HK-\d{5}")


def fetch():
    for attempt in range(4):
        try:
            r = requests.get(URL, timeout=300)
            r.raise_for_status()
            break
        except Exception:
            if attempt == 3:
                raise
            time.sleep(15 * (attempt + 1))
    root = ET.fromstring(r.content)
    out = [{"permit": (d.findtext("permitNo") or "").strip()} for d in root.iter("drug")]
    out = [x for x in out if x["permit"]]
    CURRENT.clear()
    ids = {x["permit"] for x in out}
    if len(ids) >= MIN_CURRENT:
        CURRENT.update(ids)
    return out


def confirmed_absent(lid):
    """給 license_refresh：名單有成功下載、這張 HK-xxxxx 不在名單＝確認已不是現行註冊"""
    k = str(lid or "").strip()
    return bool(CURRENT) and bool(ID_RE.fullmatch(k)) and k not in CURRENT


def preprocess(bundle):
    """名單沒有的註冊號標 cancelled（drugoffice_not_listed＝第一次發現日）；又出現的取消標記。有改回 True"""
    if not CURRENT:
        return False
    today = time.strftime("%Y-%m-%d")
    ch = False
    for r in (bundle.get("tfda") or {}).get("records") or []:
        k = str(r.get("license_id") or "").strip()
        if not ID_RE.fullmatch(k):
            continue
        if k in CURRENT:
            if r.get("drugoffice_not_listed"):
                r.pop("drugoffice_not_listed", None)
                r.pop("license_status", None)
                ch = True
        elif not r.get("drugoffice_not_listed"):
            r["drugoffice_not_listed"] = today
            r["license_status"] = "cancelled"
            ch = True
    return ch


def validate(new, old):
    p = []
    if len(new) < 10000:
        p.append(f"只解析出 {len(new)} 筆，疑似格式改變")
    if old and len(new) < 0.9 * len(old):
        p.append(f"筆數 {len(new)} 比上次 {len(old)} 少超過 10%")
    return p


def status_index(new):
    return {r["permit"]: "listed" for r in new}


def record_id(rec):
    return str(rec.get("license_id") or "").strip()


def update(rec, new):
    return False  # 在列不改紀錄；只用來確認仍在列，查不到的列在 summary


# 2026-11-24（用戶決定）：「香港上市資訊」的許可證表改由 scripts/sync_license_tables.py 依證據包產生（程式區塊 <!-- licenses:begin/end -->）。
# 每週排程（license_refresh_20261029.py 的 sync_tables 掛鉤）全站重排：狀態變了、或 add_current_registrations.py 補收了新註冊，
# 排序與「上表列出其中 N 張（共 M 張…）」都跟著變；只重排表格內容，表以外的正文不動（正文張數由 4b 的 apply_drug_reviews.py
# 結尾的 rewrite_license_counts.py 依快照改寫）。PAGE_NOTE：表格列以外、程式寫的行（說明句、區塊標記、沒有任何註冊時的一句）。
PAGE_NOTE = (r"^(上表列出其中 \d+ 張（共 \d+ 張）。|<!-- licenses:(begin|end) -->|"
             r"衞生署藥物辦公室的註冊名單（本報告所用資料）中沒有含本藥成分的許可證。)$")


def sync_tables(site_dir, bundles):
    import importlib.util
    s = importlib.util.spec_from_file_location("hk_slt", site_dir / "scripts/sync_license_tables.py")
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return [(pg, "許可證表", "", "依證據包重排") for pg in m.run()]
