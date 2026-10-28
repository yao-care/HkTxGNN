---
layout: default
title: Ocrelizumab
parent: 僅模型預測 (L5)
nav_order: 635
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
monitor_inn: "OCRELIZUMAB"
predicted_indications: ["HER2 positive breast carcinoma", "normal breast-like subtype of breast carcinoma", "progesterone-receptor positive breast cancer", "breast tumor luminal A or B", "progesterone-receptor negative breast cancer"]
description: "Ocrelizumab：預測新適應症為HER2 陽性乳癌 (HER2 positive breast carcinoma)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Ocrelizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Ocrelizumab: HER2 陽性乳癌 (HER2 positive breast carcinoma)
{: .text-alpha }

## 一句話總結

Ocrelizumab 是一種靶向 CD20 的人源化單株抗體，原本用於進行性多發性硬化症。
TxGNN 模型預測它可能對 **HER2 陽性乳癌 (HER2 positive breast carcinoma)** 有效，但目前**沒有任何臨床試驗或直接相關文獻**支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | HER2 陽性乳癌 (HER2 positive breast carcinoma) |
| TxGNN 預測分數 | 0.9989 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 ocrelizumab 是一種人源化抗 CD20 單株抗體，可選擇性清除表現 CD20 的 B 細胞，在多發性硬化症（包含復發型與原發進行型）的療效已有大型試驗證實。

然而，就現有資料而言，**無法建立合理的機轉連結**。HER2 陽性乳癌的病理主要由 HER2 訊號驅動，編譯資料中沒有任何以 CD20 或 B 細胞清除為基礎的乳癌治療依據。0.9989 的高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，不等同於生物學證據。

同時，預測清單中的其他乳癌亞型（PR 陽性、PR 陰性、類正常乳房型、Luminal A/B）分數幾乎相同（0.9980 至 0.9981），顯示這較可能反映 TxGNN 模型（深度學習）從相關疾病之間學到的相似性，而非各亞型特有的生物學。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對 HER2 陽性乳癌，目前無相關文獻。

另外說明：在排名第 4 的預測（Luminal A/B 乳房腫瘤）下雖檢索到 18 篇文獻（以下列出部分代表），但內容全部是 ocrelizumab 用於多發性硬化症、抗 CD20 免疫學或其他自體免疫疾病，**沒有任何一篇探討乳癌**，應視為以藥名檢索的偶然結果，不能作為乳癌證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28002688](https://pubmed.ncbi.nlm.nih.gov/28002688/) | 2017 | RCT | N Engl J Med | Ocrelizumab 對原發進行型多發性硬化症優於安慰劑（僅支持原適應症） |
| [28002679](https://pubmed.ncbi.nlm.nih.gov/28002679/) | 2017 | RCT | N Engl J Med | 復發型多發性硬化症中 ocrelizumab 對比干擾素 β-1a（僅支持原適應症） |
| [40245351](https://pubmed.ncbi.nlm.nih.gov/40245351/) | 2025 | RCT | Neurology | 第 3 期 OCARINA II：皮下注射與靜脈注射的藥物暴露非劣性 |
| [37307006](https://pubmed.ncbi.nlm.nih.gov/37307006/) | 2023 | Cohort | JAMA Neurol | 復發緩解型多發性硬化症中 rituximab 與 ocrelizumab 比較 |
| [37033984](https://pubmed.ncbi.nlm.nih.gov/37033984/) | 2023 | Review | Front Immunol | 抗 CD20 療法在多發性硬化症的應用 |
| [35192158](https://pubmed.ncbi.nlm.nih.gov/35192158/) | 2022 | Review | Drugs | Ocrelizumab 在多發性硬化症的綜述 |
| [35176351](https://pubmed.ncbi.nlm.nih.gov/35176351/) | 2022 | Review | J Allergy Clin Immunol | 次發性低γ球蛋白血症的診斷與處置指引 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67765 | OCREVUS CONCENTRATE FOR SOLUTION FOR INFUSION 300MG/10ML（廠商：ROCHE HONG KONG LIMITED） | 輸注用濃縮液（依品名） | 未載明 |

## 安全性考量

- **藥物交互作用**：共查得 100 筆交互作用，以下為部分範例：
  - 中度：皮質類固醇類，包括 hydrocortisone、prednisolone、prednisone、dexamethasone、betamethasone、budesonide、triamcinolone
  - 中度：放射性藥物，如 iobenguane (I-131)、ibritumomab tiuxetan、tositumomab、samarium (153Sm) lexidronam
  - 中度：albendazole、pentamidine、levamisole
  - 輕度：鋅鹽類（硫酸鋅、醋酸鋅、葡萄糖酸鋅、氯化鋅）

主要警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測僅來自 TxGNN 模型分數，沒有任何臨床試驗或乳癌相關文獻，也沒有可成立的機轉連結，證據等級為 L5。
- 檢索到的 Phase 3 RCT 屬於多發性硬化症的證據，無法提升乳癌適應症的證據等級。

**若要推進需要：**
- 取得完整作用機轉資料，並評估 CD20/B 細胞與 HER2 陽性乳癌之間是否存在合理的生物學連結
- 進行乳癌相關的前臨床或機轉研究，並針對乳癌重新做文獻與試驗檢索
- 取得香港衛生署核准的仿單，補齊警語與禁忌症，以進行安全性篩選
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

