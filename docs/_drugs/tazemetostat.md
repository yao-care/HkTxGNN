---
layout: default
title: Tazemetostat
parent: 中證據等級 (L3-L4)
nav_order: 850
evidence_level: L4
indication_count: 10
---

# Tazemetostat
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Tazemetostat：從上皮樣肉瘤到腎透明細胞癌

## 一句話總結

Tazemetostat 是一種 EZH2 抑制劑，原本用於上皮樣肉瘤（epithelioid sarcoma）等肉瘤的治療。
TxGNN 模型預測它可能對**腎透明細胞癌 (Clear Cell Renal Carcinoma)** 有效，
目前**沒有相關臨床試驗登記**，僅有 **5 篇文獻**（以前臨床與機轉研究為主）提供間接支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 上皮樣肉瘤、肉瘤（香港許可證未載明核准適應症文字，此處依藥物知識圖譜） |
| 預測新適應症 | 腎透明細胞癌 (Clear Cell Renal Carcinoma) |
| TxGNN 預測分數 | 98.98% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原廠資料未收錄）。不過已知 Tazemetostat 屬於 EZH2 抑制劑，EZH2 是 Polycomb repressive complex 2 (PRC2) 的催化次單元，負責 H3K27me3 的沉積並參與基因沉默。

在腎細胞癌方面，前臨床研究（PMID 36808829）顯示抑制 EZH2 可透過 LATS1 發揮抗腫瘤作用。另一篇綜述（PMID 40526876）指出 BAP1 與 EZH2 路徑存在交互作用，而 BAP1 功能缺失在腎透明細胞癌相當常見，提示可能存在對 EZH2 抑制的合成致死弱點。

此外，NCI-COG 兒童 MATCH 研究（PMID 37228094）納入帶有 SMARCB1/SMARCA4 缺失或 EZH2 變異的腫瘤，這類族群與腎髓質癌、類橫紋肌樣腎腫瘤相關，但**並未直接證明對腎透明細胞癌有效**。整體而言，這些是機轉層面的間接線索，尚未有臨床療效證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37228094](https://pubmed.ncbi.nlm.nih.gov/37228094/) | 2023 | 第 2 期籃式臨床試驗（兒童） | J Natl Cancer Inst | 針對帶有 EZH2 突變或 SMARCB1/SMARCA4 缺失的難治性實體瘤，以 tazemetostat 治療 |
| [40526876](https://pubmed.ncbi.nlm.nih.gov/40526876/) | 2025 | Review | JCO Precis Oncol | 探討 BAP1 與 EZH2 路徑交互作用，及其在乳癌、間皮瘤、淋巴瘤的治療介入 |
| [36808829](https://pubmed.ncbi.nlm.nih.gov/36808829/) | 2023 | 前臨床 | FEBS Open Bio | 抑制 EZH2 可經由 LATS1 在腎細胞癌發揮抗腫瘤作用 |
| [39988317](https://pubmed.ncbi.nlm.nih.gov/39988317/) | 2025 | 前臨床／機轉 | Nucleic Acids Res | NEXT 複合體調控 H3K27me3 水準，影響癌症進展 |
| [39833894](https://pubmed.ncbi.nlm.nih.gov/39833894/) | 2025 | 病例報告 | Acta Neuropathol Commun | 腎髓質癌病人接受含 tazemetostat 的治療後出現腦轉移與膠質細胞轉分化 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68216 | TAZVERIK TABLETS 200MG | 未載明 | 未載明（製造商：HUTCHMED (HONG KONG) LIMITED） |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（EZH2 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下列出部分主要項目：
  - **嚴重 (Major)**：Aprepitant、Dexamethasone、Clarithromycin
  - **中度 (Moderate)**：Hydrocortisone、Triamcinolone、Betamethasone、Prednisone、Cimetidine、Saxagliptin、Linagliptin、Repaglinide、Granisetron 等

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 腎透明細胞癌的預測分數雖高（98.98%），但沒有任何臨床試驗，文獻也以前臨床與機轉研究為主，證據等級僅 L4，屬於「研究問題」階段。
- 香港仿單的警語與禁忌症資料尚缺，無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌症、核准適應症）並完成安全性篩選
- 補齊 DrugBank 的作用機轉資料
- 驗證 BAP1 缺失或 SMARCB1 缺失的腎癌亞群是否對 EZH2 抑制敏感（細胞株／動物模型）
- 若前臨床結果支持，設計生物標記篩選的小型 Phase 2 試驗
- 評估與嚴重交互作用藥物（如 Clarithromycin、Aprepitant、Dexamethasone）併用時的管理方案
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

