---
layout: default
title: Vortioxetine
parent: 僅模型預測 (L5)
nav_order: 942
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "VORTIOXETINE"
predicted_indications: ["neurotic disorder", "benign paroxysmal torticollis of infancy"]
description: "Vortioxetine：預測新適應症為神經症 (neurotic disorder)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Vortioxetine
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

## Vortioxetine: 神經症 (neurotic disorder)
{: .text-alpha }

> 說明：本報告依規定以 `predicted_indications[0]`（排名第 1，neurotic disorder）作為主要分析對象，並在最後補充其他預測適應症的比較。

---

## 一句話總結

Vortioxetine 是一種多重作用機轉的抗憂鬱藥，原本用於單極性憂鬱症、重度憂鬱症與焦慮症。
TxGNN 模型預測它可能對 **神經症 (Neurotic Disorder)** 有效，但目前**沒有相關臨床試驗**，只有 **1 篇**屬個案報告性質的文獻，證據僅停留在模型預測層級。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 神經症 (neurotic disorder) |
| TxGNN 預測分數 | 0.9924 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據文獻中的一般描述，vortioxetine 具多重血清素作用：抑制血清素轉運體 (SERT)，並調節 5-HT1A、5-HT1B、5-HT3、5-HT7 等受體。這些作用在重度憂鬱症中已有充分證據。

「神經症」是一個過時且範圍很廣的診斷類別，與憂鬱症、焦慮症高度重疊，而這兩者已在 vortioxetine 的原適應症內。TxGNN 的高分很可能反映的是疾病分類上的語意接近，而非獨立的療效證據。

因此，這項預測的合理性主要來自與既有適應症的重疊。針對「神經症」本身，目前沒有機轉或臨床上的直接證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31006795](https://pubmed.ncbi.nlm.nih.gov/31006795/) | 2019 | Review（內容為個案報告） | Zhurnal nevrologii i psikhiatrii imeni S.S. Korsakova | 神經症性憂鬱病例；建議以抗憂鬱藥結合心理治療（認知行為治療）的整合方式治療，並未專門評估 vortioxetine |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63599 | BRINTELLIX TABLETS 20MG | — | 未提供 |
| HK-63600 | BRINTELLIX TABLETS 10MG | — | 未提供 |
| HK-63601 | BRINTELLIX TABLETS 5MG | — | 未提供 |

三張許可證皆為單一成分、有效狀態，持證商為 Lundbeck HK Limited。

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為其中的主要項目（資料顯示前 20 筆）：
  - **嚴重 (Major)**：Bupropion、Lorcaserin、Diethylpropion、Dolasetron、Palonosetron、Phentermine
  - **中度 (Moderate)**：Morphine、Acetylsalicylic acid（阿斯匹靈）、Dexamethasone、Chlorpropamide、Glimepiride、多種胰島素（aspart、degludec、detemir、glargine、glulisine）、Picosulfuric acid、Sodium sulfate、Polyethylene glycol、Eliglustat
- 另依預測資料所述，vortioxetine 在年輕族群有自殺意念相關的黑框警語，且未確立兒童使用的安全性。

其餘警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 神經症是過時的寬泛診斷類別，TxGNN 高分很可能來自與憂鬱症、焦慮症的本體論重疊，並非獨立證據。目前無臨床試驗，僅 1 篇個案性質文獻，證據等級為 L5。

**若要推進需要：**
- 釐清「神經症」在現行診斷標準（如 DSM-5 / ICD-11）中對應的具體疾病，改以明確的焦慮或憂鬱亞型作為研究目標
- 取得香港仿單的警語、禁忌症與核准適應症文字
- 補齊作用機轉資料
- 針對目標族群設計對照試驗

---

## 附錄：其他預測適應症比較

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 說明 |
|------|-----------|-----------|---------|------|------|
| 4 | 嬰兒良性陣發性斜頸 | 0.9907 | L5 | Hold | 無可辨識的機轉連結，無試驗與文獻，此分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病學到的相似性，而非生物學證據，且嬰兒族群有安全疑慮 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

