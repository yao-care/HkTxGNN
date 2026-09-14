---
layout: default
title: Tazemetostat
parent: 中證據等級 (L3-L4)
nav_order: 721
evidence_level: L3
indication_count: 10
---

# Tazemetostat
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Tazemetostat：原適應症資料缺失，聚焦腎透明細胞癌新適應症

## 一句話總結

Tazemetostat 在本 Evidence Pack 中原適應症與作用機轉資料均列為缺口（DG001 Blocking、DG002 High）。
TxGNN 模型預測它可能對**腎透明細胞癌 (Clear Cell Renal Carcinoma)** 有效，
目前**無臨床試驗登記**，但有 **5 篇文獻**支持，其中 1 篇為腎細胞癌特異性機轉研究。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（Evidence Pack 未提供） |
| 預測新適應症 | 腎透明細胞癌 (Clear Cell Renal Carcinoma) |
| TxGNN 預測分數 | 98.98% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，原適應症與 MOA 在 Evidence Pack 中皆列為資料缺口（DG001、DG002）。根據 predicted_indications 提供的機轉推論：Tazemetostat 是 EZH2（enhancer of zeste homolog 2）甲基轉移酶抑制劑，可降低 H3K27me3 甲基化水平。

腎透明細胞癌 (ccRCC) 常見 PBRM1、BAP1、SETD2 等染色質修飾基因突變，與 EZH2 過度活化及腫瘤進展相關。文獻 PMID 36808829 直接顯示 EZH2 抑制經 LATS1 路徑在腎細胞癌（涵蓋 ccRCC、pRCC、chRCC）中產生抗腫瘤效果，為此預測提供機轉層面的支持證據。此外 PMID 37228094（NCI-COG 兒童 basket trial）證實 tazemetostat 對 EZH2 突變/SMARCB1 缺失腫瘤具臨床活性，顯示藥物在此分子路徑上確有實際療效訊號，但仍需針對 ccRCC 成人病人族群設計專屬試驗驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37228094](https://pubmed.ncbi.nlm.nih.gov/37228094/) | 2023 | Phase 1/2 basket trial | J Natl Cancer Inst | NCI-COG MATCH：EZH2 突變或 SMARCB1/SMARCA4 缺失實體瘤病人接受 tazemetostat 治療結果 |
| [36808829](https://pubmed.ncbi.nlm.nih.gov/36808829/) | 2023 | Preclinical mechanistic (RCC-specific) | FEBS Open Bio | EZH2 抑制經 LATS1 路徑對腎細胞癌（含 ccRCC）產生抗腫瘤效果 |
| [40526876](https://pubmed.ncbi.nlm.nih.gov/40526876/) | 2025 | Review | JCO Precision Oncology | BAP1 與 EZH2 路徑交互作用，與腎細胞癌、間皮瘤、淋巴瘤等腫瘤發生相關 |
| [39833894](https://pubmed.ncbi.nlm.nih.gov/39833894/) | 2025 | Case report | Acta Neuropathol Commun | SMARCB1 缺失腎髓質癌病人經 tazemetostat 治療後腦轉移個案 |
| [39988317](https://pubmed.ncbi.nlm.nih.gov/39988317/) | 2025 | Basic science | Nucleic Acids Research | NEXT 複合體調控 H3K27me3 水平影響癌症進展機轉（非腎癌特異性基礎研究） |

---

## 香港上市資訊

Tazemetostat 目前**未於香港上市**，無有效許可證。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（EZH2 甲基轉移酶抑制劑，非傳統細胞毒性藥物） |
| 骨髓抑制風險 | 資料缺失，請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 資料缺失，請參考原廠仿單的警語與注意事項 |
| 監測項目 | 資料缺失，請參考原廠仿單的警語與注意事項 |
| 處置防護 | 資料缺失，請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。（本 Evidence Pack 中「仿單警語/禁忌」列為 **Blocking** 等級資料缺口，尚未完成 S1 安全性初評）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一候選（腎透明細胞癌）已有機轉層面支持（L3 證據等級，含腎癌特異性 preclinical 研究），但無任何臨床試驗登記；其餘 9 個預測適應症證據等級皆為 L4-L5，僅為知識圖譜推論。
- 藥物在香港未上市，且仿單警語/禁忌（DG001, Blocking）尚未取得，無法進入 S1 安全性初評。

**若要推進需要：**
- 補齊仿單警語與禁忌資料（DG001, Blocking）
- 補齊作用機轉 (MOA) 完整資料（DG002, High）
- 確認香港上市與許可證狀態
- 針對 ccRCC 設計早期臨床試驗（目前無 disease-specific 試驗登記）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

