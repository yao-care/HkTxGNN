"""HK（衛生署藥物辦公室 DrugList.xml）下載與狀態對應，給 license_refresh_20261029.py 用（2026-10-30）。

來源：https://www.drugoffice.gov.hk/eps/psi/DrugList.xml（免金鑰，有 lastUpdate）。只列現行註冊的藥劑製品、沒有狀態欄：
在列＝status 維持原值（證據包原本是空白，reviewer 視為有效），新清單查不到的註冊號保留原狀態、列在 summary（不推定為撤銷）。
證據包 license_id＝permitNo（HK-xxxxx）。
"""
import time
import xml.etree.ElementTree as ET

import requests

RAW_FILE = "raw/hk_druglist_permits.json"
URL = "https://www.drugoffice.gov.hk/eps/psi/DrugList.xml"


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
    return [x for x in out if x["permit"]]


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
