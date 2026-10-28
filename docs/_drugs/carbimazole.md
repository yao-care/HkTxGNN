---
layout: default
title: Carbimazole
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 2
monitor_inn: "CARBIMAZOLE"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia"]
last_modified_at: 2026-10-28
description: "Carbimazole：預測新適應症為甲狀腺素抵抗症（resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta）（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Carbimazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Carbimazole：抗甲狀腺藥物（甲巴唑前驅藥，抑制甲狀腺過氧化酶） → 甲狀腺素抵抗症（resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta）
{: .text-alpha }

## 一句話總結

Carbimazole 是一種抗甲狀腺藥物，在體內轉換為甲巴唑（methimazole）而發揮作用。
TxGNN 模型預測它可能對**甲狀腺素抵抗症（resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta）**有效，
但目前**無臨床試驗**，僅有 **1 篇**與診斷鑑別相關的病例文獻，證據非常薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 甲狀腺素抵抗症（resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta） |
| TxGNN 預測分數 | 0.9971 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 許可證數 | 6 張（有效 6 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知藥理而言，Carbimazole 為甲巴唑的前驅藥，可抑制甲狀腺過氧化酶，減少甲狀腺素合成。

甲狀腺素抵抗症（RTH-β）的特徵是周邊組織對 T3/T4 部分不敏感，同時 TSH 無法被抑制。若以抗甲狀腺藥物降低甲狀腺素濃度，可能使 TSH 進一步升高，造成甲狀腺腫大與甲狀腺刺激增加，也可能在已抵抗的組織中誘發甲狀腺功能低下症狀。因此，機轉上的合理性偏弱，甚至可能有害。

高分數較可能反映模型網路中與高甲狀腺素血症相關疾病的鄰近性，而非真正的治療訊號，解讀時需特別謹慎。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | 病例報告／回顧 | BMJ Case Reports | 一名年輕男性游離 T4 升高但 TSH 未被抑制，曾間歇使用 carbimazole 治療；內容著重於此種檢驗結果的鑑別診斷，並非治療效果的證據 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52760 | CARBIMAZOLE 5 TAB 5MG (REMEDICA) | 未記載 | 未記載 |
| HK-60955 | SYN-CARBIMAZOLE TAB 5MG | 未記載 | 未記載 |
| HK-35972 | CARBIROID TAB 5MG | 未記載 | 未記載 |
| HK-26101 | CARBIMAZOLE TAB 5MG | 未記載 | 未記載 |
| HK-65516 | CAMAZOL TABLETS 5MG | 未記載 | 未記載 |

目前 6 張許可證均為有效的單一成分製劑，此處僅列出 5 張。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或直接研究此疾病的文獻，證據等級為 L5。
- 機轉上，降低甲狀腺素可能加重 TSH 刺激與甲狀腺腫大，並可能在抵抗組織中誘發甲狀腺功能低下，潛在風險高於預期效益。

**若要推進需要：**
- 補充 Carbimazole 的作用機轉資料，並進行與 RTH-β 病理生理的機轉對照分析。
- 取得直接針對 RTH-β 患者使用抗甲狀腺藥物的臨床或文獻證據，並評估安全性。
- 取得香港仿單的警語、禁忌與交互作用資料，完成安全性評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

