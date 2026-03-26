"""香港衛生署藥品資料載入與過濾"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Optional

import pandas as pd
import yaml


def load_field_config() -> dict:
    """載入欄位映射設定"""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入香港衛生署藥品資料 (XML 格式)

    Args:
        filepath: XML 檔案路徑，預設為 data/raw/DrugList.xml

    Returns:
        包含所有藥品的 DataFrame

    Raises:
        FileNotFoundError: 找不到資料檔案時，提供下載指引
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "raw" / "DrugList.xml"

    if not filepath.exists():
        raise FileNotFoundError(
            f"找不到藥品資料: {filepath}\n"
            f"請先執行以下步驟：\n"
            f"1. 從香港藥物辦公室網站下載資料\n"
            f"   URL: https://www.drugoffice.gov.hk/eps/psi/DrugList.xml\n"
            f"2. 放到 data/raw/ 目錄\n"
        )

    # 解析 XML
    tree = ET.parse(filepath)
    root = tree.getroot()

    drugs = []
    for drug in root.findall('drug'):
        # 提取基本資訊
        product_name = drug.find('productName')
        holder_name = drug.find('regCertHolderName')
        permit_no = drug.find('permitNo')

        # 提取成分列表
        active_ings = drug.find('activeIngs')
        ingredients = []
        if active_ings is not None:
            for ing in active_ings.findall('activeIng'):
                if ing.text:
                    ingredients.append(ing.text.strip())

        drugs.append({
            'license_id': permit_no.text if permit_no is not None else None,
            'brand_name': product_name.text if product_name is not None else None,
            'holder_name': holder_name.text if holder_name is not None else None,
            'ingredients': '; '.join(ingredients) if ingredients else None,
            'ingredient_list': ingredients,
        })

    df = pd.DataFrame(drugs)
    return df


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """過濾有效藥品

    Args:
        df: 原始藥品 DataFrame

    Returns:
        僅包含有效藥品的 DataFrame（香港清單只包含有效註冊藥品）
    """
    # 香港清單只包含有效註冊藥品，所以主要過濾有成分的
    active = df[df['ingredients'].notna() & (df['ingredients'] != '')].copy()

    # 重設索引
    active = active.reset_index(drop=True)

    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """取得藥品資料摘要統計

    Args:
        df: 藥品 DataFrame

    Returns:
        摘要統計字典
    """
    summary = {
        "total_count": len(df),
        "with_ingredient": df['ingredients'].notna().sum(),
        "unique_products": df['brand_name'].nunique() if 'brand_name' in df.columns else 0,
        "unique_holders": df['holder_name'].nunique() if 'holder_name' in df.columns else 0,
    }

    # 統計唯一成分數
    all_ingredients = set()
    for ing_list in df['ingredient_list'].dropna():
        all_ingredients.update(ing_list)
    summary["unique_ingredients"] = len(all_ingredients)

    return summary


if __name__ == "__main__":
    # 測試載入
    df = load_fda_drugs()
    print(f"載入 {len(df)} 筆藥品資料")

    df_active = filter_active_drugs(df)
    print(f"有效藥品: {len(df_active)} 筆")

    summary = get_drug_summary(df_active)
    print(f"摘要: {summary}")
