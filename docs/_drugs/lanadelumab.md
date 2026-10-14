---
layout: default
title: Lanadelumab
parent: 高證據等級 (L1-L2)
nav_order: 507
evidence_level: L1
indication_count: 10
---

# Lanadelumab
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Lanadelumab：從遺傳性血管性水腫到 C1 抑制劑缺乏症

## 一句話總結

Lanadelumab 是一種抑制血漿激肽釋放酶（plasma kallikrein）的單株抗體，原本用於預防遺傳性血管性水腫（HAE）發作。
TxGNN 模型預測它對 **C1 抑制劑缺乏症 (C1 inhibitor deficiency)** 有效，目前有 **5 個臨床試驗**和 **20 篇文獻**支持。
需注意：C1 抑制劑缺乏症即 I/II 型 HAE 的病因，與藥物既有適應症高度重疊，嚴格來說並非全新的再利用方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 遺傳性血管性水腫 (Hereditary Angioedema)、合併 C1 抑制劑缺乏的遺傳性血管性水腫（來自知識圖譜；香港許可證未載明核准適應症文字） |
| 預測新適應症 | C1 抑制劑缺乏症 (C1 inhibitor deficiency) |
| TxGNN 預測分數 | 99.996% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料，但文獻中的機轉已相當明確。Lanadelumab 是完全人源化的單株抗體，專一抑制血漿激肽釋放酶（KLKB1）。

在 C1 抑制劑缺乏症中，SERPING1 基因突變使 C1-INH 不足或功能異常，血漿激肽釋放酶活性失控，產生過量的緩激肽（bradykinin）。緩激肽是造成血管擴張與水腫發作的主要因子。直接抑制激肽釋放酶即可針對這條路徑介入。

此預測與原適應症本質上是同一疾病譜系，所以預測合理，但**並不代表發現了新用途**。排名第 2 至第 10 的預測（如 serpinopathy、胰臟炎、血小板疾病、肌炎等）僅有模型分數，無臨床試驗或文獻，且多數缺乏機轉關聯，應視為模型推測。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | 完成 | 20 | 中國 HAE 受試者開放標籤試驗，治療 26 週，評估安全性、PK 與療效 |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | 完成 | 21 | SPRING 研究：2 至 <12 歲兒童 HAE 的安全性、PK 與預防發作 |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | 完成 | 12 | 日本 I/II 型 HAE 受試者的療效與安全性 |
| [NCT05397431](https://clinicaltrials.gov/study/NCT05397431) | 不適用 | 進行中（不招募） | 155 | 日本長期使用的上市後調查，監測副作用與症狀改善 |
| [NCT04583007](https://clinicaltrials.gov/study/NCT04583007) | 不適用 | 已不提供 | 無資料 | 擴大使用計畫，供兒童 HAE 及正常 C1-INH 非組織胺性血管性水腫患者使用，療效證據有限 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab 與安慰劑比較，預防 HAE 發作的隨機臨床試驗（HELP） |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | 開放標籤延伸 | Allergy | HELP OLE：≥12 歲 HAE 1/2 型患者的長期療效與安全性 |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | RCT 次族群分析 | BioDrugs | 針對 C1-INH 缺乏型 HAE 的前臨床與 Phase I 研究回顧 |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | 網絡統合分析 | Drugs in R&D | 比較 garadacimab、lanadelumab、皮下 C1-INH、berotralstat 等長期預防療法 |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | 系統性回顧 | Clin Rev Allergy Immunol | 評估接受長期預防的 I/II 型 HAE 患者仍發生發作的比例與特徵 |
| [40504359](https://pubmed.ncbi.nlm.nih.gov/40504359/) | 2025 | 真實世界研究 | Adv Ther | EMPOWER 第 4 期研究，最長 36 個月的療效與安全性 |
| [40769455](https://pubmed.ncbi.nlm.nih.gov/40769455/) | 2025 | 真實世界研究 | Ann Allergy Asthma Immunol | 不同疾病活動度族群的 HAE 控制與生活品質 |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Review | Drugs | Lanadelumab 首次全球核准概述 |
| [31560114](https://pubmed.ncbi.nlm.nih.gov/31560114/) | 2019 | Review | Drugs | Lanadelumab 在 HAE 的綜述，HELP 試驗顯著降低發作率 |
| [31234673](https://pubmed.ncbi.nlm.nih.gov/31234673/) | 2019 | Review | Immunotherapy | 激肽釋放酶抑制劑 lanadelumab 綜述，半衰期約 14 天 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67123 | TAKHZYRO SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 300MG/2ML（持證商：武田藥品香港） | 注射液（預填充針筒） | 許可證資料未載明 |

---

## 安全性考量

- **藥物交互作用**：資料庫僅記錄 lanadelumab 與其作用標的 kallikrein B1 (KLKB1) 的藥理交互作用，屬於作用機轉本身，並非臨床上的藥物間交互作用。
- **其他**：目前未取得香港仿單的警語與禁忌資料。一項預測（pseudo-von Willebrand disease）的分析提到，lanadelumab 可能干擾 aPTT 檢驗，此為理論性疑慮，需對照仿單確認。

其餘安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 3 個已完成的 Phase 3 試驗、HELP 隨機對照試驗及多項長期與真實世界研究，證據等級為 L1，且藥物已在香港上市。
- 但此預測對應的是藥物既有適應症，而非真正的新用途，且香港許可證未載明核准適應症文字，仿單安全性資料也尚缺。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌
- 補充 DrugBank 的作用機轉資料
- 若要探索真正的新適應症（排名 2 至 10），需先建立機轉假設並取得初步臨床或前臨床證據，目前這些預測均建議 Hold
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

