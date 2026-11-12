"""本站查核機制的在地設定（HkTxGNN，繁體中文（香港用語）；2026-11-12 建）。

程式（page_format、licenses、withdrawn、scripts/apply_drug_reviews.py、build_license_snapshot.py、reviews_from_edits.py、
check_original_indications.py）的核心流程比照 TwTxGNN／UsTxGNN，本站的字樣、規則細節、提交清單集中在這裡。
本站的許可證資料是衞生署藥物辦公室的 DrugList.xml（只收現行在列的藥劑製品，不含已註銷的），事實層只涵蓋這部分
（checker X_SCOPE）；「沒有已註銷」之類的寫法資料無法證實，不當作錯誤，也不據以更正。
"""
import re

SITE = "HkTxGNN"
CODE = "hk"

# ---- 頁首等級（page_format）----
OVERVIEW_LEVEL_LABELS = ["證據等級"]
HEADER_LABEL = "證據等級"
# 2026-11-12 實測：876 頁有總覽等級，頁首全部＝總覽格第一個等級（主預測），0 頁例外 → first（不照 Tw 整格取最高）
HEADER_RULE = "first"
HEADER_KEEP_NA = True
HEADER_EXCEPTIONS: dict = {}
WITHDRAWN_RE = re.compile(r"^\s*(\*\*)?撤回")
DESC_LEVEL_WORD = r"證據等級"
DESC_LEVEL_DEFAULT = "證據等級"
NA_DESC = "僅已知用途"

# ---- 許可證（licenses）----
MARKET_SECTIONS = ["香港上市資訊"]

# ---- 查核框與查核紀錄表（apply_drug_reviews）----
DISCLAIMER_RE = re.compile(r"^## 免責聲明", re.M)
LOG_HEAD = "## 查核紀錄"
LOG_COLS = "| 查核日期 | 項目 | 處理 | 依據 |"
LABEL = {"correct": "查核更正", "annotate": "查核加註", "rereview": "待重審", "rereview_result": "重審結果"}
ACTION = {"correct": "更正", "annotate": "加註", "rereview": "標記待重審", "section": "新增附來源段落",
          "rereview_result": "重審完成", "header_level": "頁首等級依快速總覽重算",
          "description_level": "頁面描述的證據等級改為頁首等級"}
VERDICT = {"maintain": "維持", "downgrade": "降級", "upgrade": "升級", "withdraw": "撤回"}
BOX_HEAD = "> **{label}（{date}）**："
ORIG_STATED = "原文為「{claim}」。"
SPACE, FULL_STOP, SENT_END = "", "。", "。！？）」"
PAREN = "（{}）"
JOIN, LIST_SEP, ITEM_SEP = "／", "；", "、"
SOURCE_WORD = "依據："
DECISION = "決策建議另議："
TABLE_UPDATED = "本頁{labels}已依重審結果更新，原值列於下方查核紀錄。"
LEVEL_SAME = "證據等級 {o} 不變"
LEVEL_CHANGE = "證據等級 {o}→{n}"
ACT_REREVIEWED = "標記待重審 → 已重審（見下列重審結果）"
ACT_HEADER = "頁首等級依快速總覽重算（原 {o}→{n}）"
ACT_HEADER_WD = "主預測經重審撤回，頁首等級重算（原 {o}→{n}）"
ACT_NA_LIST = "，改列入「{title}」"
ACT_RESULT = "重審：{verdict}，{change}"
ACT_TABLE = "；{label}：原「{a}」→「{b}」"
ACT_DESC = "頁面描述（description）的「證據等級 {o}」改為「{n}」（依頁首等級；其他文字未有改動，原文保留於紀錄）"
ACT_REVISED = "（{d} 修訂，前版保留於紀錄）"
ST_SUPERSEDED = "已由程式產生的許可證表取代（原為{act}）"
ST_REGEN = "報告重新產生後已無此錯誤（{d}：{note}；原為{act}）"
ST_PROGRAM = "程式修正後已無此錯誤（{d}：{note}；原為{act}）"
ST_WITHDRAWN = "查核撤回（{d}：{note}；原為{act}）"
INTRO = ("以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。"
         "更正只限基本事實，模型預測、證據等級與結論未有改寫。")
INTRO_HEADER = "以下是本頁的查核紀錄；頁首證據等級依本頁「快速總覽」重算，模型預測、總覽表與結論未有改寫。"
INTRO_RERE = ("以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測原文未有改寫；"
              "證據等級與決策只依重審結果（降級、升級或撤回）更新，原值列於下表。")

# ---- 刪改轉紀錄（reviews_from_edits）----
# 2026-10-31～11-06：本站第二批許可證掃描沒有要刪的句子（11-06 掃描 0 句）；只有 8b5fd5613 regorafenib 刪掉把已移除的預測
# 「腎細胞癌」當作預測舉例的括號（checker P3），同屬事實更正，一併轉成紀錄（COMMIT_KIND＝pred）。
COMMITS = ["8b5fd5613"]
COMMIT_KIND = {"8b5fd5613": "pred"}
REGEN_COMMITS = ["6ee0c4967", "faab5d54a", "a1e1c9568", "994e31d25", "931a627f7", "c1a22be61", "8364126fc", "d153b52c7", "825d97671"]
SOURCES = [{"title": "衞生署藥物辦公室 – 藥劑製品資料（DrugList.xml）", "url": "https://www.drugoffice.gov.hk/eps/psi/DrugList.xml"},
           {"title": "衞生署藥物辦公室", "url": "https://www.drugoffice.gov.hk/"}]
SENT = re.compile(r"(?<=[。！？；])|\n")
CLASS_EXTRA: dict = {}
NOTES = {
    "tw": "已刪除：從台灣站範本殘留的台灣食藥署（TFDA）內容，與本香港頁面無關。",
    "cancel": "已刪除：這段指許可證已註銷或沒有有效許可證，與衞生署藥物辦公室的註冊資料不符（{date}）。",
    "count": "已刪除：這段寫的許可證數目或狀態，與衞生署藥物辦公室的註冊資料不符（{date}）。",
    "generic": "已刪除：這段內容與衞生署藥物辦公室的註冊資料不符（{date}）。",
    "pred": "已刪除：這段把已從本頁移除的預測適應症當作預測舉例，與本頁保留的預測不符（{date}）。",
}
FIGURES = "資料中的許可證共 {total} 張，有效 {valid} 張；最新數字見快速總覽及香港上市資訊。"
SUMMARY = "刪除「{text}」"
STRIP_CHARS = " ，、；。,;.\n-（）()"
REGEN_NOTE = "報告於 2026 年 11 月重新產生，已不含此內容"

# ---- 原適應症交叉驗證（check_original_indications）----
ORIGINAL_LABELS = ["原適應症"]
ORIGINAL_NONE_RE = re.compile(r"^\s*(本地許可證資料未記載|未記載|未載明|沒有|無|不詳)")
PHRASE_SPLIT = re.compile(r"[；;、，,/（）()]+|及|與|和|或")
PHRASE_MIN = 2
