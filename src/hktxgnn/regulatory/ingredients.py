"""衞生署藥劑製品註冊名單 activeIng（證據包 ingredients）的成分切分與單一成分／複方判定（2026-11-24）。

原本 reviewer/drug_evidence_pack.py 用「;;」切成分，但本站成分欄以「; 」分隔（例「naloxone hydrochloride; oxycodone hydrochloride」），
每張都被判成單一成分（事實層 single_total＝total）。用戶 2026-11-24 決定：事實層依本站成分欄正確切分。
規則同 scripts/sync_license_tables.py 的程式表（2026-11-17 起的查核紀錄也照這個算法）：以「;」分隔，
只有「-」之類沒有字母數字的項不算成分（例 ELOCTATE「-; efmoroctocog alfa」是粉末＋溶劑包裝）。
"""


def split_ingredients(s):
    return [x.strip() for x in str(s or "").split(";") if any(c.isalnum() for c in x)]


def kind(s):
    """單一成分 single／複方 combo；成分欄空白時照舊算 single（跟原本「;;」切法空白時的結果相同）"""
    return "combo" if len(split_ingredients(s)) > 1 else "single"
