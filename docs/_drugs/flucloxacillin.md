---
layout: default
title: Flucloxacillin
parent: 僅模型預測 (L5)
nav_order: 320
evidence_level: L5
indication_count: 10
---

# Flucloxacillin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Flucloxacillin：從 葡萄球菌感染症 到 結膜炎

## 一句話總結

Flucloxacillin 是一種抗青黴素酶盤尼西林類窄效抗生素，主要用於治療 Methicillin 敏感性金黃葡萄球菌（MSSA）引起的皮膚軟組織感染、骨髓炎及心內膜炎。
TxGNN 模型預測它可能對**結膜炎 (Conjunctivitis)** 有效，
目前有 **0 個臨床試驗**和 **2 篇間接相關文獻**，整體直接證據不足。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（香港未上市，無許可證） |
| 預測新適應症 | 結膜炎 (Conjunctivitis) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知藥理資訊，Flucloxacillin 是 Isoxazolyl penicillin 類抗生素，透過與細菌青黴素結合蛋白（PBP）共價結合、抑制細胞壁肽聚糖合成來殺菌。其最大特點是對 β-lactamase（青黴素酶）具有抵抗性，因此對 MSSA 具有強效覆蓋，但對 MRSA 無效。

細菌性結膜炎的常見致病菌包含金黃葡萄球菌（*S. aureus*），此為 Flucloxacillin 最強覆蓋的目標菌種。就機轉而言，若結膜炎由 MSSA 引起，Flucloxacillin 的抗菌活性在理論上可能有效——這是 TxGNN 預測的主要生物合理性來源。

然而，臨床轉化存在明顯障礙：結膜炎的標準治療為**局部眼科劑型**（眼藥水或眼藥膏），Flucloxacillin 目前無此劑型；現有文獻中對「結膜炎」的提及，也僅出現在 Staphylococcal Scalded Skin Syndrome（SSSS）的前驅症狀描述中，而非針對 Flucloxacillin 治療結膜炎的療效研究。整體評估，預測的機轉邏輯具備合理出發點，但缺乏實際臨床研究支撐。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [12627992](https://pubmed.ncbi.nlm.nih.gov/12627992/) | 2003 | Review | Am J Clin Dermatol | 葡萄球菌燙傷樣皮膚症候群（SSSS）診斷與處置回顧；結膜炎為 SSSS 前驅症狀之一，間接說明 flucloxacillin 治療 MSSA 相關感染的脈絡 |
| [1286123](https://pubmed.ncbi.nlm.nih.gov/1286123/) | 1992 | Case Report | Int J STD & AIDS | 疱疹病毒非典型表現個案報告；無摘要，與 Flucloxacillin 之關聯性不明，參考價值有限 |

---

## 香港上市資訊

Flucloxacillin 目前在香港**未上市**，無任何藥品許可證登記紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數雖高（99.84%），但目前缺乏任何臨床試驗或直接文獻支持 Flucloxacillin 用於結膜炎治療；現有 2 篇文獻均屬間接引用，且該藥在香港未上市、無局部眼科劑型，臨床轉化路徑尚未確立，現階段不具推進條件。

**若要推進需要：**
- 補齊作用機轉資料（DrugBank MOA API 查詢）
- 搜尋葡萄球菌性細菌性結膜炎的抗生素治療直接文獻，確認 flucloxacillin 同類藥物（如 oxacillin、nafcillin）的眼科應用案例
- 評估眼科局部劑型（滴眼液）的開發可行性
- 確認香港或其他市場的上市路徑與法規要求
- 取得安全性完整資料：仿單警語、禁忌症及藥物交互作用
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

