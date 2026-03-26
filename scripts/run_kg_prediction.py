#!/usr/bin/env python3
"""執行知識圖譜方法預測 - 香港版本

使用 TxGNN 知識圖譜進行老藥新用預測。

使用方法:
    uv run python scripts/run_kg_prediction.py

前置條件:
    1. 已下載香港藥品資料 (data/raw/DrugList.xml)
    2. 已執行 prepare_external_data.py

產生檔案:
    data/processed/drug_mapping.csv
    data/processed/repurposing_candidates.csv
"""

from pathlib import Path

import pandas as pd

from hktxgnn.data.loader import load_fda_drugs, filter_active_drugs, get_drug_summary
from hktxgnn.mapping.drugbank_mapper import map_fda_drugs_to_drugbank
from hktxgnn.predict.repurposing import find_repurposing_candidates


def main():
    print("=" * 60)
    print("HkTxGNN - 執行知識圖譜方法預測")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent

    # 1. 載入藥品資料
    print("1. 載入香港藥品資料...")
    fda_df = load_fda_drugs()
    active_df = filter_active_drugs(fda_df)
    summary = get_drug_summary(active_df)
    print(f"   總藥品數: {summary['total_count']}")
    print(f"   有成分藥品: {summary['with_ingredient']}")
    print(f"   唯一成分數: {summary['unique_ingredients']}")

    # 2. DrugBank 映射
    print()
    print("2. 執行 DrugBank 映射...")
    # 準備符合 mapper 欄位名稱的 DataFrame
    mapper_df = active_df.rename(columns={
        'license_id': '許可證字號',
        'brand_name': '中文品名',
        'ingredients': '主成分略述'
    })
    drug_mapping = map_fda_drugs_to_drugbank(mapper_df)
    mapped_count = drug_mapping['drugbank_id'].notna().sum()
    total_count = len(drug_mapping)
    print(f"   映射成功: {mapped_count}/{total_count} ({mapped_count/total_count*100:.1f}%)")

    # 儲存藥品映射
    output_dir = base_dir / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)
    drug_mapping.to_csv(output_dir / "drug_mapping.csv", index=False)
    print(f"   已儲存藥品映射: {output_dir / 'drug_mapping.csv'}")

    # 3. 尋找老藥新用候選
    # 香港資料沒有適應症欄位，所以使用簡化方法：
    # 直接生成所有 (藥物, 疾病) 配對
    print()
    print("3. 尋找老藥新用候選...")
    print("   （香港資料無適應症欄位，將生成所有可能配對）")

    # 載入藥物-疾病關係 (columns: relation, x_id, x_name, y_id, y_name)
    from hktxgnn.predict.repurposing import load_drug_disease_relations
    relations_df = load_drug_disease_relations()

    # 取得成功映射的唯一藥物
    mapped_drugs = drug_mapping[drug_mapping['drugbank_id'].notna()]['drugbank_id'].unique()
    print(f"   映射成功的唯一藥物: {len(mapped_drugs)}")

    # 載入疾病詞彙表
    diseases_df = pd.read_csv(base_dir / "data" / "external" / "disease_vocab.csv")
    diseases = diseases_df['disease_id'].unique()
    print(f"   TxGNN 中的疾病數: {len(diseases)}")

    # 取得已知的藥物-疾病關係 (x_id = drug, y_id = disease)
    known_relations = set(zip(relations_df['x_id'], relations_df['y_id']))

    # 建立 drugbank_id -> 藥品資訊映射
    drug_info = drug_mapping[drug_mapping['drugbank_id'].notna()].drop_duplicates(subset=['drugbank_id'])
    drug_info_map = {}
    for _, row in drug_info.iterrows():
        drug_info_map[row['drugbank_id']] = {
            'license_id': row.get('license_id', row.get('許可證字號', '')),
            'brand_name': row.get('brand_name', row.get('中文品名', '')),
            'drug_ingredient': row.get('normalized_ingredient', row.get('標準化成分', '')),
        }

    # 生成候選配對（排除已知關係）
    disease_name_map = dict(zip(diseases_df['disease_id'], diseases_df['disease_name']))
    candidates_list = []
    for drug in mapped_drugs:
        info = drug_info_map.get(drug, {})
        for disease in diseases:
            if (drug, disease) not in known_relations:
                candidates_list.append({
                    'license_id': info.get('license_id', ''),
                    'brand_name': info.get('brand_name', ''),
                    'drug_ingredient': info.get('drug_ingredient', ''),
                    'drugbank_id': drug,
                    'potential_indication': disease_name_map.get(disease, disease),
                    'source': 'TxGNN Knowledge Graph',
                })

    candidates = pd.DataFrame(candidates_list)
    print(f"   候選數: {len(candidates)}")
    print(f"   涉及藥物數: {candidates['drugbank_id'].nunique()}")
    print(f"   潛在新適應症數: {candidates['potential_indication'].nunique()}")

    # 4. 儲存結果
    print()
    print("4. 儲存結果...")
    candidates.to_csv(output_dir / "repurposing_candidates.csv.gz", index=False)
    print(f"   已儲存至: {output_dir / 'repurposing_candidates.csv.gz'}")

    print()
    print("=" * 60)
    print("完成！")
    print("=" * 60)
    print()
    print("統計摘要:")
    print(f"  - 香港註冊藥品: {summary['total_count']}")
    print(f"  - DrugBank 映射成功: {mapped_count}")
    print(f"  - 老藥新用候選: {len(candidates)}")
    print()
    print("下一步: 執行深度學習預測")
    print("  source ~/miniforge3/bin/activate txgnn")
    print("  PYTHONPATH=src python -m hktxgnn.predict.txgnn_model")


if __name__ == "__main__":
    main()
