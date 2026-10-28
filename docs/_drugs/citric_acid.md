---
layout: default
title: Citric Acid
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 8
monitor_inn: "CITRIC ACID"
predicted_indications: ["stomach disease", "pharyngitis", "acute laryngopharyngitis", "postgastrectomy syndrome", "nasal cavity disease", "papillary conjunctivitis", "blepharoconjunctivitis", "rhinitis"]
last_modified_at: 2026-10-28
description: "Citric Acid：預測新適應症為胃部疾病 (stomach disease)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Citric Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Citric Acid：有機酸類藥物 → 胃部疾病 (stomach disease)
{: .text-alpha }

## 一句話總結

Citric Acid（檸檬酸）是一種有機酸類成分，已有多款含此成分的產品在香港上市。
TxGNN 模型預測它可能對**胃部疾病 (stomach disease)** 有效，
但目前**沒有臨床試驗**，文獻多為間接證據（例如作為 13C-尿素呼氣試驗的輔助用餐），尚無直接顯示其可治療胃部疾病的研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 胃部疾病 (stomach disease) |
| TxGNN 預測分數 | 0.9974 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 許可證數 | 6 張（有效 6 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。檸檬酸是一種常見的有機酸，常用於口服製劑與泡騰劑，與腸胃道用藥場景相鄰，因此模型預測它與胃部疾病有關聯。

不過，現有文獻中與胃部最直接相關的，是用檸檬酸作為測試餐來提高 13C-尿素呼氣試驗（幽門螺旋桿菌檢測）的準確度。這屬於診斷輔助用途，並非治療效果。其餘文獻涉及一般飲食與營養、幽門螺旋桿菌生理學、胃癌代謝體學、獸醫與動物研究，皆屬間接證據，無法證明檸檬酸能治療胃部疾病。

0.9974 的高分只是計算模型的預測結果，尚無臨床證據佐證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下為與主題較相關的文獻（均無直接評估檸檬酸治療胃部疾病）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31505905](https://pubmed.ncbi.nlm.nih.gov/31505905/) | 2019 | 診斷研究 | Gut and liver | 討論檸檬酸測試餐是否有助提高亞洲人群 13C-尿素呼氣試驗的準確度 |
| [30970440](https://pubmed.ncbi.nlm.nih.gov/30970440/) | 2019 | 診斷研究 | Gut and liver | 評估檸檬酸對幽門螺旋桿菌根除後呼氣試驗準確度的影響（萎縮性胃炎高盛行地區） |
| [15854177](https://pubmed.ncbi.nlm.nih.gov/15854177/) | 2005 | 機轉研究 | Aliment Pharmacol Ther | 比較不同有機酸（檸檬酸、蘋果酸、抗壞血酸）對胃內尿素酶活性的影響 |
| [2072799](https://pubmed.ncbi.nlm.nih.gov/2072799/) | 1991 | Review | Med Clin North Am | 消化性潰瘍的飲食與營養；不建議嚴格限制飲食 |
| [9889978](https://pubmed.ncbi.nlm.nih.gov/9889978/) | 1998 | Review | Adv Microb Physiol | 幽門螺旋桿菌的生理與代謝 |
| [35900644](https://pubmed.ncbi.nlm.nih.gov/35900644/) | 2022 | 觀察性研究 | Metabolomics | 韓國人胃癌發病前血清檸檬酸與肉鹼偏高，與鹼性磷酸酶呈負相關 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-09759 | BABY COUGH MIXTURE (PAED SIMPLE LINCT) | 未記載 | 未記載 |
| HK-63415 | CITRAFLEET POWDER FOR ORAL SOLUTION | 未記載 | 未記載 |
| HK-60968 | PICOPREP POWDER FOR ORAL SOLUTION | 未記載 | 未記載 |
| HK-20004 | LEMON FLAVOURED ENO FRUIT SALT | 未記載 | 未記載 |
| HK-06461 | BABY COUGH SYRUP WITH ANTIHISTAMINE | 未記載 | 未記載 |

## 安全性考量

- **藥物交互作用**：共查得 15 項交互作用。
  - 重大（Major）：Aluminum hydroxide。
  - 中度（Moderate）：多種氟喹諾酮類及相關抗菌藥，包括 Ciprofloxacin、Levofloxacin、Moxifloxacin、Ofloxacin、Norfloxacin 等，以及 Cinoxacin、Nalidixic acid。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有臨床試驗，文獻僅提供間接證據（診斷輔助、機轉、飲食與營養），沒有直接研究顯示檸檬酸可治療胃部疾病，因此證據等級為 L5，僅有模型預測支持。

**若要推進需要：**
- 取得詳細的作用機轉資料
- 設計並執行直接評估檸檬酸於胃部疾病的臨床前或早期臨床研究
- 取得香港原廠仿單，確認警語、禁忌與適應症文字
- 評估與氟喹諾酮類及含鋁制酸劑併用時的交互作用風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

