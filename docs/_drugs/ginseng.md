---
layout: default
title: Ginseng
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ginseng：預測新適應症為藥物性骨質疏鬆症 (Drug-induced Osteoporosis)（證據等級 L5）。原適應症：未載明"
monitor_inn: "GINSENG"
predicted_indications: ["drug-induced osteoporosis", "acne (disease)", "severe nonproliferative diabetic retinopathy", "hemorrhagic disease of newborn", "nuclear senile cataract"]
---

# Ginseng
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# 人參 (Ginseng)：從（原適應症未載明）到藥物性骨質疏鬆症

## 一句話總結

人參 (GINSENG) 在香港已有 2 張單方製劑許可證，但本次彙整的資料中未載明其核准適應症。
TxGNN 模型預測它可能對**藥物性骨質疏鬆症 (Drug-induced Osteoporosis)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持此預測，僅屬於模型運算結果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未載明（香港許可證資料中無核准適應症文字） |
| 預測新適應症 | 藥物性骨質疏鬆症 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，人參是含人參皂苷 (ginsenosides) 的植物性藥材，原適應症在本次資料中未載明，因此無法就原適應症與新適應症的關聯性做具體分析。

前臨床研究曾提出，人參皂苷可能影響骨代謝（成骨細胞與蝕骨細胞的平衡），這是支持此預測的可能方向。但此說法並未獲得本次彙整資料中任何研究的支持，目前只能視為電腦模型的預測。

TxGNN 分數雖然很高（0.9995），但分數高不等於有臨床證據。在取得實際研究資料前，應謹慎解讀。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 其他預測適應症（供參考）

模型同時預測了下列適應症，以下是各自的證據概況：

| 預測適應症 | TxGNN 分數 | 證據等級 | 證據概況 | 建議 |
|-----------|-----------|---------|---------|------|
| 痤瘡 (Acne) | 99.87% | L4 | 1 篇 2019 年前臨床研究（[PMID 30506753](https://pubmed.ncbi.nlm.nih.gov/30506753/)），顯示紅蔘疏水性萃取物具抗菌特性；尚無人體試驗 | Hold |
| 重度非增殖性糖尿病視網膜病變 | 99.71% | L4 | 1 篇 2026 年前瞻性研究（[PMID 42395017](https://pubmed.ncbi.nlm.nih.gov/42395017/)），探討韓國紅蔘對視網膜深層微血管叢參數的影響；設計、樣本數與是否納入重度 NPDR 族群待確認，且為影像參數而非臨床結果 | Research Question |
| 新生兒出血症 | 99.70% | L4 | 唯一關聯試驗 [NCT00719563](https://clinicaltrials.gov/study/NCT00719563) 為美國人參用於癌症相關疲勞的 Phase 3 試驗（n=364，已完成），與此適應症無關，可能是假性關聯 | Hold |
| 核性老年性白內障 | 99.56% | L5 | 無臨床試驗與文獻 | Hold |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-45214 | HIYA KIOGAN SILVER PILLS | 未載明 | 未載明 |
| HK-45213 | HIYA KIOGAN GOLD PILLS | 未載明 | 未載明 |

兩張許可證皆為單方製劑、狀態有效，製造商為 MAN HING MEDICINE TRADERS。

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 83 筆交互作用，以下為部分中度 (Moderate) 交互作用，主要集中在降血糖藥物：
  - 口服降血糖藥：Acarbose、Metformin、Pioglitazone、Glimepiride、Chlorpropamide
  - DPP-4 / SGLT2 抑制劑：Alogliptin、Linagliptin、Canagliflozin、Dapagliflozin、Empagliflozin
  - GLP-1 類藥物：Albiglutide、Dulaglutide、Semaglutide、Lixisenatide
  - 胰島素類：Insulin aspart、degludec、detemir、glargine、glulisine
  - 其他：Acetylsalicylic acid（阿斯匹靈）
- **其他提醒**：人參有報告指出可能影響凝血功能，並與抗凝血藥（如 warfarin）有交互作用，在出血性疾病的情境下需特別留意；新生兒使用亦無證據支持。

其餘警語與禁忌症資料缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（藥物性骨質疏鬆症）僅有模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。
- 香港許可證缺少適應症、劑型與仿單的安全性資訊，目前無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊核准適應症、警語與禁忌症
- 補充作用機轉資料（如人參皂苷對骨代謝的機轉）
- 針對骨質疏鬆症進行文獻與前臨床證據回顧，確認是否有人體研究
- 若優先考慮其他預測，可先查證糖尿病視網膜病變研究（PMID 42395017）的設計與族群，作為較有潛力的研究方向
- 針對與降血糖藥物及抗凝血藥的交互作用，制定監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

