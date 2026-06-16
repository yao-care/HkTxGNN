---
layout: default
title: Glutamic Acid
parent: 僅模型預測 (L5)
nav_order: 352
evidence_level: L5
indication_count: 4
---

# Glutamic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# GLUTAMIC ACID（麩胺酸）：從天然胺基酸到多項新適應症預測

## 一句話總結

GLUTAMIC ACID（麩胺酸）是人體最豐富的興奮性神經傳導物質之一，目前無核准藥物適應症。TxGNN 模型預測它可能對**停經後骨質疏鬆症、妊娠相關骨質疏鬆症、原發性遺傳性青光眼及胃輕癱**等四項疾病有潛在療效。其中胃輕癱方向有 **1 個臨床試驗登記**（已撤回）和 **3 篇文獻**，是目前證據相對最充分、但仍十分有限的候選方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無核准藥物適應症（天然非必需胺基酸） |
| 最高分預測新適應症 | 停經後骨質疏鬆症 (Postmenopausal Osteoporosis) |
| TxGNN 預測分數（最高） | 99.34% |
| 最佳證據等級 | L4（胃輕癱）；其餘三項 L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，GLUTAMIC ACID 是中樞及周邊神經系統中最主要的興奮性神經傳導物質，透過 NMDA、AMPA 及代謝型麩胺酸受體（mGluR）家族發揮廣泛的生理調節作用。以下針對四個預測適應症分別說明機轉關聯性：

**骨質疏鬆症（停經後及妊娠相關）**
骨細胞（成骨細胞、蝕骨細胞）表達 NMDA/AMPA 型麩胺酸受體，理論上可調節骨重塑訊號。然而，此推論目前僅停留在基礎科學層面，尚無臨床轉化數據支持麩胺酸補充對停經後或妊娠相關骨質疏鬆的療效。妊娠期骨代謝改變（鈣需求上升、激素波動）雖可能與麩胺酸訊號交互作用，但機轉鏈條高度間接且推測性強。

**原發性遺傳性青光眼**
麩胺酸興奮毒性（glutamate excitotoxicity）被認為是青光眼視網膜神經節細胞（RGC）死亡的重要機轉之一——玻璃體麩胺酸濃度升高與 RGC 損傷相關。**值得特別注意的是，此機轉提示外源性麩胺酸補充可能加重而非改善眼部損傷，與 TxGNN 預測的治療方向相悖**，此適應症需特別謹慎解讀。

**胃輕癱（Gastroparesis）**
腸道肌間神經叢及黏膜下神經叢表達代謝型麩胺酸受體（mGluR1/5），可調節腸蠕動與胃排空速率。味精（MSG/monosodium glutamate）可刺激迷走神經傳入纖維，理論上可促進胃腸運動。NCT02745028 的臨床試驗設計（單劑 MSG 改善兒童胃排空延遲）正是基於此機轉假說，顯示此方向具一定科學社群認可度，儘管試驗最終未完成。

---

## 預測適應症總覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|--------|-----------|---------|------|
| 1 | 停經後骨質疏鬆症 (Postmenopausal Osteoporosis) | 99.34% | L5 | Hold |
| 2 | 妊娠相關骨質疏鬆症 (Pregnancy Associated Osteoporosis) | 99.18% | L5 | Hold |
| 3 | 原發性遺傳性青光眼 (Primary Hereditary Glaucoma) | 99.13% | L5 | Hold ⚠️ |
| 4 | 胃輕癱 (Gastroparesis) | 99.11% | L4 | Research Question |

---

## 臨床試驗證據

### 胃輕癱（Gastroparesis）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02745028](https://clinicaltrials.gov/study/NCT02745028) | NA | 已撤回 (WITHDRAWN) | 0 | 探索單劑 MSG 是否能縮短兒童胃排空時間；試驗已撤回，無任何數據 |

> ⚠️ 此試驗狀態為 **WITHDRAWN**、招募數為 **0**，代表試驗從未執行，無療效或安全性數據可參考。試驗設計本身印證了科學假說的可行性，但撤回原因不明，可能涉及安全性顧慮或可行性問題，建議進一步追查。

其他三個適應症（停經後骨質疏鬆、妊娠相關骨質疏鬆、原發性遺傳性青光眼）目前無相關臨床試驗登記。

---

## 文獻證據

### 妊娠相關骨質疏鬆症（Pregnancy Associated Osteoporosis）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11369436](https://pubmed.ncbi.nlm.nih.gov/11369436/) | 2001 | Review | Progress in Neurobiology | 回顧腦部麩胺酸轉運蛋白（神經膠質細胞/神經元）的清除機轉；與妊娠骨質疏鬆的直接關聯性尚不明確 |

### 胃輕癱（Gastroparesis）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41071175](https://pubmed.ncbi.nlm.nih.gov/41071175/) | 2025 | Retrospective Cohort | Journal of Clinical Gastroenterology | 評估 IVIG 對自體免疫性胃輕癱（AGID）症狀嚴重程度的影響；涉及 GAD 抗體但非麩胺酸直接補充療效 |
| [29487566](https://pubmed.ncbi.nlm.nih.gov/29487566/) | 2018 | Cohort/Observational | Frontiers in Endocrinology | 探討糖尿病合併胃輕癱患者的 GADA 抗體與 C-Peptide 水準；核心機轉為抗體介導，非麩胺酸再利用 |
| [27014566](https://pubmed.ncbi.nlm.nih.gov/27014566/) | 2016 | Case Series/Review | Results in Immunology | GAD65 抗體陽性自體免疫胃輕癱患者以免疫療法（IVIG）治療的案例系列 |

> **⚠️ 重要提示**：胃輕癱相關文獻的核心主題是**麩胺酸去羧酶（GAD）抗體**作為自體免疫胃輕癱的生物標記，而非麩胺酸（Glutamic Acid）本身的治療效果。文獻與本預測的直接相關性有限，需謹慎評估。

停經後骨質疏鬆症及原發性遺傳性青光眼目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
四個預測適應症中，三項（骨質疏鬆相關及青光眼）完全缺乏臨床或文獻直接支持（L5）；青光眼方向的機轉邏輯更顯示外源性麩胺酸補充可能具有反效果。胃輕癱方向雖有機轉假說支持，但唯一相關臨床試驗已撤回且從未執行，現有文獻亦主要聚焦 GAD 抗體而非麩胺酸本身，整體證據基礎不足以支持推進。

**若要推進需要：**
- 調查 NCT02745028 撤回具體原因（是否涉及安全性疑慮）
- 取得麩胺酸詳細作用機轉資料（MOA）及已知毒理/安全性資料
- 針對胃輕癱方向補充前臨床研究（動物模型、體外胃腸運動實驗）
- 釐清麩胺酸在香港的藥事法規地位（食品添加物 vs. 藥物）
- **青光眼適應症建議不推進**，除非有明確以麩胺酸受體拮抗（而非補充）為方向的新設計
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

