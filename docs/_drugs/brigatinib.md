---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 9
monitor_inn: "BRIGATINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
last_modified_at: 2026-11-20
description: "Brigatinib：預測新適應症為牙齦纖維瘤病 (fibromatosis, gingival)（證據等級 L5）。香港藥劑製品註冊：3 張（有效 3 張）"
---

# Brigatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Brigatinib：ALK/EGFR/FAK 多重激酶抑制劑 → 牙齦纖維瘤病 (fibromatosis, gingival)
{: .text-alpha }

## 一句話總結

Brigatinib 是一種口服的多重酪胺酸激酶抑制劑（以 ALK 為主要標靶）。
TxGNN 模型預測它可能對**牙齦纖維瘤病 (fibromatosis, gingival)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 牙齦纖維瘤病 (fibromatosis, gingival) |
| TxGNN 預測分數 | 0.9989 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Brigatinib 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Brigatinib是一種酪胺酸激酶抑制劑（TKI），於臨床可達到的濃度下，在體外對多種激酶具有活性，包括ALK、ROS1、類胰島素生長因子-1受體（IGF-1R）及FLT-3，以及EGFR缺失及點突變。在體外及體內分析中，brigatinib可抑制ALK的自體磷酸化，以及ALK所媒介的下游訊息傳遞蛋白STAT3、AKT、ERK1/2及S6的磷酸化。」英文原文："Brigatinib is a tyrosine kinase inhibitor (TKI) with in vitro activity at clinically achievable concentrations against multiple kinases including ALK, ROS1, insulin-like growth factor-1 receptor (IGF-1R), and FLT-3 as well as EGFR deletion and point mutations. Brigatinib inhibited autophosphorylation of ALK and ALK-mediated phosphorylation of the downstream signaling proteins STAT3, AKT, ERK1/2, and S6 in in vitro and in vivo assays."（[DailyMed: Alunbrig (brigatinib) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fe9ff20-d402-41f3-bc1e-7002ea7007db)，版本日期 2026-01-12；查閱日期 2026-11-19）。已知 brigatinib 是以 ALK 為主要標靶的激酶抑制劑，同時也抑制 EGFR、FAK 等激酶。

就目前整理的資料而言，ALK、EGFR、FAK 等激酶的抑制作用與牙齦纖維瘤病之間，並沒有已確認的機轉關聯。這個預測分數很高（0.9989），但屬於模型輸出，不能視為藥理上的合理性證明。

因此，這項預測目前只能視為待驗證的假說。若要推進，需要先建立牙齦纖維組織增生與相關激酶訊號路徑之間的生物學連結。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66121 | ALUNBRIG TABLETS 90MG | 未記載 | 本地資料未記載 |
| HK-66119 | ALUNBRIG TABLETS 180MG | 未記載 | 本地資料未記載 |
| HK-66120 | ALUNBRIG TABLETS 30MG | 未記載 | 本地資料未記載 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：本次彙整的資料共記錄 100 筆交互作用，以下為其中部分。
  - **重大 (Major)**：Aprepitant、Dexamethasone、Clarithromycin
  - **中度 (Moderate)**：Famotidine、Ranitidine、Rabeprazole、Cimetidine、Metformin、Pioglitazone、Loperamide、Morphine 等

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這項預測僅來自模型分數，沒有臨床試驗或文獻直接研究牙齦纖維瘤病，證據等級為 L5。
- ALK/EGFR/FAK 抑制與牙齦纖維瘤病之間沒有已知的機轉關聯。

**若要推進需要：**
- 補充 brigatinib 的作用機轉資料，並探討其與牙齦纖維組織增生的生物學關聯
- 進行前臨床研究（如細胞或動物模型）驗證可行性
- 取得香港原廠仿單，確認警語、禁忌症與核准適應症內容
- 評估全身性激酶抑制劑用於良性局部病變的風險效益

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Alunbrig (brigatinib) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=0fe9ff20-d402-41f3-bc1e-7002ea7007db) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

