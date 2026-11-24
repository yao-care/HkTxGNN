"""正文許可證張數的程式改寫（2026-11-24 建，用戶決定；做法移植 KrTxGNN／MyTxGNN 的 count_prose，規則是本站中文（香港用語）句型）。

用戶 2026-11-24 決定：正文裡「N 張許可證」這類許可證張數敘述，由程式依許可證快照（snapshots/hk_licenses.json.gz 的 facts，
單一成分／複方張數用快照的 mix）改寫，每週資料更新後跟著改，不逐筆寫查核紀錄（同 Tw／Kr／My：程式改寫的張數敘述是程式產生的正文）。

只改「句型明確、數字確定是本藥許可證張數」的地方，其餘一律不動：
  - 數字是阿拉伯數字＋「張」（「兩張」「三張」這類中文數字不改，只列出跟事實與程式表列數都不符的；這類句子多半是講上表那幾張）；句子要有「許可證／註冊／藥證／登記」
    （在市場段落「香港上市資訊」裡可不寫），且沒有試驗／文獻／研究／病例／交互作用等字樣（那些「N 張」不是許可證）。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、front matter；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上；2026-11-17 的「香港共有 N 張含本藥成分的許可證（…）」
    都在紀錄裡，照紀錄的日期與內容保留）。
  - 整句不動（hedged/subset）：有保留（至少、部分、可能不完整）、相對數（另有、其餘、其他、此外、尚有、以外）、
    講資料或查詢（資料只有／收錄／查詢到／證據包）、劑型或廠商子集（錠劑、注射、乳膏…、持有、廠商、公司；只看數字所在的子句）、
    子句裡點名許可證號（HK-xxxxx）；事實層 partial（證據包只收部分許可證）的頁整頁不動。
  - 數字不動（display）：顯示筆數（列出、以下、以上、上表、下表、其中、前、此處、僅列；「N 張主要／代表」）。
角色（看數字左右幾個字）：「已註銷 N 張」「N 張已註銷」→註銷；「有效 N 張」「N 張有效」→有效；「單一成分／單方」→單方（同時有效
→有效單方）；「複方」→複方（同時有效→有效複方）；其餘→總數。
同一行只要有一句含許可證數字而被略過，整行都不動（免得前後句數字對不上）。
同一句另有明確的有效／註銷數字時，沒有限定詞的總數、單方、複方數字就是全部張數。
單一成分／複方的數字只驗、不改（列為 single-combo）：2026-11-17 以前的報告依舊證據包（成分用「;;」切，每張都算單方）寫「N 張
有效單方許可證」，其實多半指全部張數；只換數字會留下錯的「單方」字樣，要改整句請寫查核紀錄。
數字左邊緊接英文（廠商、品牌名，例「Sandoz 4 張」）的句子整句不動。
數字已等於該角色的任一合理讀法（沒有限定詞的「N 張」＝總數或有效數）就不動；不等於時，兩種讀法相同才改，不同就列為 ambiguous。
原數字是 0 的句子不改、列為 zero-premise；要改成 0 的也不改、列為 to-zero（前提變了，「香港已有 0 張有效許可證」不通）。
前提檢查（premise）：句子說「全部有效／皆有效／無已註銷」而有效≠總數（只講單方的句子比單方）、「皆為單一成分／無複方」而單方≠總數、
「皆為複方」而複方≠總數時整句不動、列出（要改請寫查核紀錄）。
"""
from __future__ import annotations

import re

from . import site as C

SENT_SPLIT = re.compile(r"(?<=[。！？])")
NUM = re.compile(r"(?<![\d.,A-Za-z-])(\d[\d,]*)(\s*)張(?!力)")
WNUM = re.compile(r"(?<![一-鿿])([一兩二三四五六七八九十]{1,2})張(?!力)|(?<=[有共為])([一兩二三四五六七八九十]{1,2})張(?!力)")
LICENSE = re.compile(r"許可證|註冊|藥證|登記")
NOT_LICENSE = re.compile(r"試驗|文獻|研究|論文|PMID|NCT|病例|個案|患者|病人|交互作用|不良反應|候選|預測|圖|照片|處方箋")
HEDGED = re.compile(r"至少|部分|可能不完整|不完整|另有|其餘|其他|此外|另外|還有|尚有|以外|之外|除了|除此|過去|曾經|先前|約\s*\d|逾|超過|多於|不少於|"
                    r"資料(中)?(只|僅|顯示|收錄|列出|共有|有)|收錄|查詢|查到|查得|證據包|本報告所用|所整理的資料(中)?(只|僅|顯示|共)")
SUBSET = re.compile(r"錠|膠囊|注射|針劑|乳膏|軟膏|眼藥|滴劑|滴眼|滴鼻|糖漿|吸入|噴劑|噴霧|口服|外用|獸用|輸注|輸液|貼片|貼劑|栓劑|散劑|顆粒|"
                    r"溶液|懸液|懸浮|凝膠|洗劑|洗髮|含片|毫克|\d\s*(mg|MG|ml|ML|%)|持有|持證|廠商|製造|公司|Ltd|LTD|Limited|LIMITED|"
                    r"HK-\d|學名藥|原廠|品牌")
DISPLAY_LEFT = re.compile(r"(列出|列|顯示|其中|前|上表|下表|表中|表列|此處|僅|以下|以上|下列|上列|共列)\s*(為)?\s*(其中)?\s*(主要|代表性?|部分)?(的)?\s*$")
DISPLAY_RIGHT = re.compile(r"^\s*(主要|代表|作為|為例|示例)")
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)
CANC_L = re.compile(r"(已註銷|註銷|撤銷|取消|失效|過期)(的|者)?\s*$")
CANC_R = re.compile(r"^\s*(的)?(已|均已|皆已|被)?(註銷|撤銷|取消|失效)")
VALID_L = re.compile(r"有效(的)?\s*$")
VALID_R = re.compile(r"^\s*(的)?(為|是|均為|皆為|狀態為)?(有效|現行)(?!期)")
SINGLE_L = re.compile(r"(單一成分|單方)(的|製劑)?\s*$")
SINGLE_R = re.compile(r"^\s*(的)?(有效)?(的)?(單一成分|單方)")
COMBO_L = re.compile(r"複方(的|製劑)?\s*$")
COMBO_R = re.compile(r"^\s*(的)?(有效)?(的)?複方")
ALL_VALID = re.compile(r"(全部|皆|均|都|全數|一律)(為|是|屬)?(有效|現行)(?!期)|(無|沒有|未有|並無|未見)(任何)?(已)?(註銷|撤銷)")
ALL_SINGLE = re.compile(r"(全部|皆|均|都|全數)(為|是|屬)?(單一成分|單方)|(無|沒有|並無)複方")
ALL_COMBO = re.compile(r"(全部|皆|均|都|全數)(為|是|屬)?複方")
_WN = {"一": 1, "兩": 2, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10}


CLAUSE_SEP = "，,、；;：:（）()"


def _clause(s, a, b):
    """數字所在的子句（逗號、頓號、分號、冒號、括號之間）：劑型、廠商等子集字樣只看這一段，
    「是一種外用皮質類固醇，在香港已有 3 張有效許可證」的「外用」是講藥、不是講許可證子集"""
    i = max(s.rfind(c, 0, a) for c in CLAUSE_SEP)
    j = min([k for k in (s.find(c, b) for c in CLAUSE_SEP) if k >= 0] or [len(s)])
    return s[i + 1:j]


def _wnum(w):
    if len(w) == 1:
        return _WN.get(w)
    if w[0] == "十":
        return 10 + _WN.get(w[1], 0)
    if w[1] == "十":
        return _WN.get(w[0], 0) * 10
    return None


def _role(s, a, b):
    left, right = s[max(0, a - 10):a], s[b:b + 8]
    if re.search(r"[A-Za-z][A-Za-z.&）)]*\s*$", left):
        return "named"  # 「Sandoz 4 張」「Bristol-Myers Squibb 4 張」：廠商或品牌的子集
    if DISPLAY_LEFT.search(left) or DISPLAY_RIGHT.match(right):
        return "display"
    if CANC_L.search(left) or CANC_R.match(right):
        return "cancelled"
    valid = bool(VALID_L.search(left) or VALID_R.match(right))
    if SINGLE_L.search(left) or SINGLE_R.match(right):
        return "valid_single" if valid or re.match(r"^\s*(的)?有效", right) else "single"
    if COMBO_L.search(left) or COMBO_R.match(right):
        return "valid_combo" if valid or re.match(r"^\s*(的)?有效", right) else "combo"
    return "valid" if valid else "total"


def _readings(role, f, explicit):
    """(可接受的值, 改寫用的值)。改寫用的值是 None：兩種讀法不同、又沒有限定詞，判斷不了。"""
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    st, sc, vs, vc = f.get("single_total"), f.get("combo_total"), f.get("valid_single"), f.get("valid_combo")
    if role == "cancelled":
        return {c}, c
    if role == "valid":
        return {v}, v
    if role == "valid_single":
        return {vs}, vs
    if role == "valid_combo":
        return {vc}, vc
    if role == "single":
        return ({st}, st) if explicit else ({st, vs}, st if st == vs else None)
    if role == "combo":
        return ({sc}, sc) if explicit else ({sc, vc}, sc if sc == vc else None)
    return ({t}, t) if explicit else ({t, v}, t if t == v else None)


def _premise_ok(sent, f, roles):
    scope_single = any(r in ("single", "valid_single") for r in roles) and not any(r in ("total", "valid") for r in roles)
    scope_combo = any(r in ("combo", "valid_combo") for r in roles) and not any(r in ("total", "valid") for r in roles)
    if ALL_VALID.search(sent):
        if scope_single and f.get("valid_single") != f.get("single_total"):
            return False
        if scope_combo and f.get("valid_combo") != f.get("combo_total"):
            return False
        if not (scope_single or scope_combo) and f.get("valid") != f.get("total"):
            return False
    if ALL_SINGLE.search(sent) and not scope_single and f.get("single_total") != f.get("total"):
        return False
    if ALL_COMBO.search(sent) and not scope_combo and f.get("combo_total") != f.get("total"):
        return False
    return True


def rewrite_sentence(sent, f, market=False):
    """回傳 (新句子, 跳過理由或 None)。market：句子在市場段落「香港上市資訊」裡，「N 張」不寫「許可證」也算許可證。"""
    licish = (LICENSE.search(sent) or market) and not NOT_LICENSE.search(sent)
    if not licish:
        return sent, None
    nums = list(NUM.finditer(sent))
    if not nums:
        for m in WNUM.finditer(sent):  # 中文數字：不改，只在跟事實不符時列出
            w = m.group(1) or m.group(2)
            role = _role(sent, m.start(), m.end())
            if role == "display" or HEDGED.search(sent) or SUBSET.search(_clause(sent, m.start(), m.end())):
                continue
            ok, _ = _readings(role, f, False)
            if _wnum(w) is not None and _wnum(w) not in ok and _wnum(w) != f.get("_shown"):
                return sent, "numeral-word"
        return sent, None
    if HEDGED.search(sent) or any(SUBSET.search(_clause(sent, m.start(), m.end())) for m in nums):
        return sent, "hedged/subset"
    found = []
    if any(_role(sent, m.start(), m.end()) == "named" for m in nums):
        return sent, "hedged/subset"
    for i, m in enumerate(nums):
        if i and re.search(r"(中|之中|當中)(的)?\s*$", sent[nums[i - 1].end():m.start()]):
            continue  # 「M 張中 N 張」：N 是顯示筆數
        found.append((m, _role(sent, m.start(), m.end())))
    roles = [r for _, r in found if r != "display"]
    explicit = any(r in ("valid", "cancelled") for r in roles)
    subs = []
    for m, role in found:
        if role == "display":
            continue
        old = int(m.group(1).replace(",", ""))
        ok, v = _readings(role, f, explicit)
        if None in ok and len(ok) == 1:
            return sent, "no-fact"
        if old in ok:
            continue
        if role in ("single", "combo", "valid_single", "valid_combo"):
            return sent, "single-combo"
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        if v == 0:
            return sent, "to-zero"  # 改成 0 張＝本藥在香港已沒有有效／任何許可證，句子的前提變了，要人改整句
        subs.append((m, v))
    if not subs:
        return sent, None
    if not _premise_ok(sent, f, roles):
        return sent, "premise"
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(f"{v:,}" if "," in m.group(1) else str(v))
        pos = m.end(1)
    out.append(sent[pos:])
    return "".join(out), None


def _line(ln, f, protect, skipped, market=False):
    if ln.startswith(("|", "#", ">", "<!--")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect if s.strip()):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f, market)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動，免得改了一句、旁邊的句子對不上
        return ln
    return "".join(new)


def merged(facts, mix):
    f = dict(facts or {})
    if mix:
        f.update(mix)
    return f


def rewrite(text, facts, mix=None, protect=()):
    """text：整頁 markdown。facts：快照的 facts；mix：快照的單一成分／複方張數。回傳 (新內容, skipped)。
    front matter、查核框、程式區塊、表格、標題不動。"""
    skipped = []
    if not facts or facts.get("partial") or facts.get("total") is None:
        return text, skipped
    f = merged(facts, mix)
    pb = re.search(r"<!-- licenses:begin -->(.*?)<!-- licenses:end -->", text, re.S)
    f["_shown"] = len(re.findall(r"^\| (?!許可證號)[^-|][^|]*\|", pb.group(1), re.M)) if pb else None  # 程式表列出的張數
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines, market, mlv = [], False, 0
    for ln in body.split("\n"):
        h = re.match(r"^(#{1,6}) (.+?)\s*$", ln)
        if h:
            lv = len(h.group(1))
            if h.group(2) in C.MARKET_SECTIONS:
                market, mlv = True, lv
            elif market and lv <= mlv:
                market = False
        lines.append(ln if "\x00" in ln else _line(ln, f, protect, skipped, market))
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
