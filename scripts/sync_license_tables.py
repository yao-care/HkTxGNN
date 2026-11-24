#!/usr/bin/env python3
"""「## 香港上市資訊」段落的許可證表改由程式依證據包產生（2026-11-24，用戶決定；全程不用 AI）。

為什麼：以前這張表是報告（AI）寫的自由格式表（多數是「| 許可證號 | 品名 | 劑型 | 核准適應症 |」，劑型、適應症欄全是「未記錄」），
每週許可證排程只改得到概覽表的狀態列與張數列，表裡寫死的狀態與選列跟著主管機關資料變動就過期，checker 擋整頁、開 issue。
改成程式表後，每週排程（scripts/license_adapter.py 的 sync_tables 掛鉤）依同一套規則重排，gate 依快照驗內容。

表格（比照 SgTxGNN／UkTxGNN／NZTxGNN／UsTxGNN 的程式表）：
- 段落裡原有的第一張表（不論原欄位）換成「| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |」；資料是證據包 tfda.records
  （衞生署藥物辦公室註冊名單 DrugList.xml；scripts/add_current_registrations.py 已補齊本藥全部註冊）。
- 選列與順序：換表當時報告原表列出的許可證號（config/license_table_pins.json，依原表順序）在前——正文常寫「以上 5 張…」
  「另有 HK-xxxxx…」「其餘包括 …」，換成別的列會對不上；其餘（以及原本沒有表的頁）依程式排序：單一成分在前、複方在後；
  同類中有效在前、已註銷在後；再依許可證號。單一成分／複方照註冊名單成分欄（activeIng，
  證據包 ingredients 以「;」分隔；只寫「-」的項不算成分）的個數判斷（事實層 single_total 用「;;」切，本站每張都會算成單方，不能用；見本站 CLAUDE.md）。
- 品名照註冊名單原文，只把重量單位「KG」寫成小寫「kg」（checker P5 會把大寫 KG 當成知識圖譜字樣）。
- 狀態欄：有效／已註銷（license_status＝cancelled，即現行名單已不列，scripts/license_adapter.py 的 preprocess）。
- 列數＝原表列數（最多 20 列；不比照 Sg 補到 5 列：本站正文常照原表列數寫「以下列出 3 張」「三張皆為單方…」），
  所以正文「以下列出 5 張主要許可證」之類的說法照樣成立；
  總數多於列數時，表下加一句「上表列出其中 N 張（共 M 張）。」
- 段落裡沒有表的頁：在標題下補程式表（min(5, 總數) 列）；證據包沒有任何紀錄時補 NONE_LINE。
- 表以外的文字不動（正文張數由 scripts/rewrite_license_counts.py 依快照事實層改寫）。
程式區塊標記：程式表（連同表下說明句，或 NONE_LINE）前後各一行「<!-- licenses:begin -->」「<!-- licenses:end -->」（前後空行），
讓查核紀錄、正文張數改寫與 gate 分得出哪些字是程式寫的。
program_rows 給 scripts/build_license_snapshot.py（快照存最多 20 列可列的列，gate 比頁面上的前 N 列，狀態欄由 checker 另驗）；
carry_block 給 scripts/sync_notes_to_docs.py 重寫整頁時移植舊頁的程式區塊；run 給 scripts/license_adapter.py 的 sync_tables。
用法（repo 根目錄，先還原 data/）：python3 scripts/sync_license_tables.py [--dry-run] [頁 ...]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SECS = ("香港上市資訊",)
HEAD = ["| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |", "|------|------|------|------|------|"]
NONE_LINE = "衞生署藥物辦公室的註冊名單（本報告所用資料）中沒有含本藥成分的許可證。"
SHOW = "上表列出其中 {n} 張（共 {m} 張）。"
SHOW_RX = re.compile(r"^上表列出其中 \d+ 張（共 \d+ 張）。$")
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
MAX_ROWS = 20
ST_VALID, ST_CANC = "有效", "已註銷"
SINGLE, COMBO = "單一成分", "複方"


def cell(x, cap=None):
    s = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    # 品名裡的重量單位「200G/KG」「(1.2-2.8 KG)」寫成小寫 kg：checker P5 會把大寫 KG 當成「知識圖譜（KG）」字樣（只改單位大小寫）
    s = re.sub(r"(\d\s*|/)KG\b", r"\1kg", s)
    return s[:cap].rstrip() + "…" if cap and len(s) > cap else s


def ingredients_of(r):
    """註冊名單 activeIng（證據包 ingredients，「;」分隔）的有效成分；只有「-」之類沒有字母數字的項不算成分
    （例 ELOCTATE「-; efmoroctocog alfa」是粉末＋溶劑包裝，溶劑那格寫「-」；2026-11-24 用戶決定「-」不算一個成分）"""
    return [x.strip() for x in str(r.get("ingredients") or "").split(";") if any(c.isalnum() for c in x)]


def is_combo(r):
    # 照註冊名單 activeIng 的有效成分個數（本站 CLAUDE.md 同一規則；2026-11-17 起的查核紀錄也照這個算法，「-」不算）
    return len(ingredients_of(r)) > 1


def is_cancelled(r):
    return str(r.get("license_status") or "").lower() == "cancelled"


def uniq(recs):
    seen = {}
    for r in recs or []:
        k = str(r.get("license_id") or "").strip()
        if k and k not in seen:
            seen[k] = r
    return list(seen.values())


def mix(recs):
    """單一成分／複方張數（含有效張數），給快照與正文張數改寫用"""
    u = uniq(recs)
    s = [r for r in u if not is_combo(r)]
    c = [r for r in u if is_combo(r)]
    return {"single_total": len(s), "combo_total": len(c),
            "valid_single": sum(1 for r in s if not is_cancelled(r)), "valid_combo": sum(1 for r in c if not is_cancelled(r))}


PINS_FILE = ROOT / "config" / "license_table_pins.json"
_PINS = None


def pins_for(stem):
    """換表當時報告原表依序列出的許可證號（config/license_table_pins.json）；沒有就是 []"""
    global _PINS
    if _PINS is None:
        _PINS = json.loads(PINS_FILE.read_text(encoding="utf-8")).get("pins", {}) if PINS_FILE.exists() else {}
    return _PINS.get(stem) or _PINS.get(stem.replace("-", "_")) or _PINS.get(stem.replace("_", "-")) or []


def table_rows(recs, pins=()):
    """全部可列的列：pins（原表選列）依序在前，其餘依程式排序"""
    rows = []
    u = sorted(uniq(recs), key=lambda r: (is_combo(r), is_cancelled(r), str(r.get("license_id")).strip()))
    rank = {k: i for i, k in enumerate(pins or [])}
    u.sort(key=lambda r: rank.get(str(r.get("license_id")).strip(), len(rank)))  # sort 是穩定的：沒選的保持程式排序
    for r in u:
        name = cell(r.get("brand_name_zh") or r.get("brand_name_en"), 80) or "未記錄"
        holder = cell(r.get("license_holder") or r.get("manufacturer"), 70) or "未記錄"
        rows.append(f"| {str(r['license_id']).strip()} | {name} | {COMBO if is_combo(r) else SINGLE} | {holder} | "
                    f"{ST_CANC if is_cancelled(r) else ST_VALID} |")
    return rows


def block_for(recs, n=None, pins=()):
    """程式區塊的內容（不含標記）：n 列的表＋（總數較多時）SHOW 句；n 預設 min(5, 總數)；沒有任何紀錄時是 NONE_LINE 一句"""
    rows = table_rows(recs, pins)
    if not rows:
        return [NONE_LINE]
    n = min(5, len(rows)) if n is None else min(n, len(rows))
    return HEAD + rows[:n] + (["", SHOW.format(n=n, m=len(rows))] if len(rows) > n else [])


def program_rows(tf, fc=None, pins=()):
    """快照用：(程式表最多可列的列, None)；頁面的列數依原表列數（5～20），gate 比前 N 列；SHOW 句的 N 隨頁不同，不比"""
    return table_rows(tf.get("records") or [], pins)[:MAX_ROWS], None


def strip_marks(lines):
    return [l for l in lines if l.strip() not in (BEGIN, END)]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def bounds(lines):
    """第一個市場段落（## 或 ### 香港上市資訊）的 (標題下一行, 段落結尾)；沒有回 (None, None)"""
    for i, ln in enumerate(lines):
        m = re.match(r"^(#{2,3}) (.+?)\s*$", ln)
        if m and m.group(2) in SECS:
            lv = len(m.group(1))
            j = next((k for k in range(i + 1, len(lines)) if re.match(rf"^#{{1,{lv}}} ", lines[k])), len(lines))
            return i + 1, j
    return None, None


def _first_table(lines, a, b):
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        return None, None
    x = y = tb[0]
    while y + 1 < b and lines[y + 1].startswith("|"):
        y += 1
    return x, y


def process(text, recs, pins=()):
    """回傳新內容（沒變回 None）"""
    lines = strip_marks(text.split("\n"))
    a, b = bounds(lines)
    if a is None:
        t2 = add_section(text, recs, pins)
        return t2 if t2 and t2 != text else None
    x, y = _first_table(lines, a, b)
    rows = table_rows(recs, pins)
    if x is None:
        lines = lines[:a] + [""] + wrap(block_for(recs, None, pins)) + [""] + [l for l in lines[a:] if l.strip() != NONE_LINE]
    else:
        n = min(MAX_ROWS, max(1, y - x - 1))
        rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip()) and l.strip() != NONE_LINE]
        lines = lines[:x] + ([""] if lines[x - 1].strip() else []) + wrap(block_for(recs, n, pins)) + [""] + rest + lines[b:]
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
    return t2 if t2 != text else None


# 2026-11-24 第三輪（用戶決定，比照 JpTxGNN 第二輪）：公開頁沒有「## 香港上市資訊」段落、但證據包有紀錄的，補一個段落放程式表。
# 位置：「## 安全性考量」之前（預測頁的固定順序）；沒有就「## 結論與下一步」之前；再沒有就「## 免責聲明」之前。
# noindex 頁與證據包沒有紀錄的頁不補。
ADD_BEFORE = ("安全性考量", "結論與下一步", "免責聲明")


def add_section(text, recs, pins=()):
    fm = text.split("---", 2)[1] if text.startswith("---") else ""
    if re.search(r"^noindex:\s*true", fm, re.M) or not uniq(recs):
        return None
    lines = text.split("\n")
    heads = {m.group(1): i for i, l in enumerate(lines) for m in [re.match(r"^## (.+?)\s*$", l)] if m}
    at = next((heads[h] for h in ADD_BEFORE if h in heads), None)
    if at is None:
        return None
    sec = ["## " + SECS[0], ""] + wrap(block_for(recs, None, pins)) + [""]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines[:at] + sec + lines[at:]))


def carry_block(old_text, new_text):
    """sync_notes_to_docs.py 重寫整頁時用：舊頁的程式區塊移植到新頁的市場段落，取代新頁模型寫的第一張表（連同表下程式文字）；
    新頁段落沒有表時接在標題下。舊頁沒有程式區塊就原樣回傳新頁。"""
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    blk = old[old.index(BEGIN):old.index(END) + 1]
    lines = strip_marks(new_text.split("\n"))
    a, b = bounds(lines)
    if a is None:
        return new_text
    x, y = _first_table(lines, a, b)
    if x is None:
        out = lines[:a] + [""] + blk + [""] + lines[a:]
    else:
        rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip())]
        out = lines[:x] + [""] + blk + [""] + rest + lines[b:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def bundle_file(stem):
    for key in dict.fromkeys((stem, stem.replace("-", "_"), stem.replace("_", "-"))):
        f = ROOT / "data/bundles" / key / "drug_bundle.json"
        if f.exists():
            return f
    return None


def run(only=None, dry=False):
    """全站（或 only 指定的頁）重排程式表。回傳改到的頁（檔名去 .md）。沒有 data/bundles 就什麼都不做。"""
    changed = []
    if not (ROOT / "data/bundles").is_dir():
        return changed
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only:
            continue
        bf = bundle_file(page.stem)
        if bf is None:
            continue
        raw = page.read_bytes().decode("utf-8")
        if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
            continue
        crlf = "\r\n" in raw[:500]
        recs = (json.loads(bf.read_text(encoding="utf-8")).get("tfda") or {}).get("records") or []
        new = process(raw.replace("\r\n", "\n"), recs, pins_for(page.stem))
        if new is None:
            continue
        changed.append(page.stem)
        if not dry:
            page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    return changed


if __name__ == "__main__":
    a = sys.argv[1:]
    ch = run({x for x in a if not x.startswith("--")} or None, "--dry-run" in a)
    print(f"許可證表{'（試跑）' if '--dry-run' in a else ''}改 {len(ch)} 頁")
