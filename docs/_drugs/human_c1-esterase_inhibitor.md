---
layout: default
title: Human C1-Esterase Inhibitor
parent: 僅模型預測 (L5)
nav_order: 373
evidence_level: L5
indication_count: 4
---

# Human C1-Esterase Inhibitor
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

# Human C1-Esterase Inhibitor：從遺傳性血管水腫到嚴重非增生性糖尿病視網膜病變

## 一句話總結

Human C1-Esterase Inhibitor（C1-INH）是補體系統的天然絲胺酸蛋白酶抑制劑，原本用於遺傳性血管水腫（Hereditary Angioedema, HAE）的預防與急性發作治療。TxGNN 模型預測它可能對**嚴重非增生性糖尿病視網膜病變（Severe Nonproliferative Diabetic Retinopathy）**有效，但目前此特定適應症尚**無任何臨床試驗或文獻**直接支持，建議暫緩推進。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 遺傳性血管水腫（Hereditary Angioedema）（香港無上市許可紀錄） |
| 預測新適應症 | 嚴重非增生性糖尿病視網膜病變（Severe Nonproliferative Diabetic Retinopathy） |
| TxGNN 預測分數 | 99.61% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

C1-Esterase Inhibitor 是人體補體系統的多靶點調節蛋白，透過抑制 C1r、C1s（古典途徑）、MASP-1/2（Lectin 途徑）以及 Factor XIIa、Kallikrein（接觸活化途徑）等多個絲胺酸蛋白酶，防止補體過度活化。值得注意的是，C1-INH 同時抑制緩激肽（bradykinin）的生成，從而降低血管通透性——這正是其用於遺傳性血管水腫的核心機轉。

在糖尿病視網膜病變的病生理研究中，補體古典途徑活化物 C1q 的沉積已在糖尿病患者的視網膜微血管中被觀察到，且補體調節基因（SERPING1 即編碼 C1-INH 的基因、C5）的遺傳多型性與第 2 型糖尿病視網膜病變易感性呈現相關性（見文獻 PMID 26989329）。理論上，C1-INH 可抑制 C1 複合體介導的視網膜血管炎症，減少膜攻擊複合物（MAC）對視網膜微血管的慢性損傷，提供神經血管保護。

然而，**嚴重非增生性糖尿病視網膜病變（Severe NPDR）**為糖尿病視網膜病變的分期次分類，TxGNN 高預測分數可能部分來自其與父疾病節點（diabetic retinopathy）在知識圖譜中的鄰近性，而非對此特定嚴重度的獨立預測依據。目前缺乏 C1-INH 用於任何 DR 分期的干預性臨床數據，機轉合理性仍屬理論層次。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無針對嚴重非增生性糖尿病視網膜病變的直接相關文獻。

> **補充參考**：在較廣泛的**糖尿病視網膜病變（Diabetic Retinopathy）**研究領域，有以下間接支持補體機轉的文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [26989329](https://pubmed.ncbi.nlm.nih.gov/26989329/) | 2016 | 遺傳關聯研究 | Mediators of Inflammation | SERPING1 與 C5 基因 SNP 與第 2 型糖尿病視網膜病變（NPDR 及 PDR）易感性相關；C5 rs17611 在 DR 患者中達邊緣顯著（P = 0.009），支持補體途徑參與 DR 炎症病生理 |

## 香港上市資訊

Human C1-Esterase Inhibitor 目前**未在香港取得上市許可**，無任何許可證記錄。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
針對嚴重非增生性糖尿病視網膜病變，目前完全缺乏干預性臨床試驗與直接文獻支持，證據等級僅達 L5（純模型預測）。補體途徑參與 DR 病生理的遺傳學線索雖存在，但從機轉推論到臨床干預仍有大幅跨越，且藥物尚未在香港上市，整體風險過高，不宜在現階段推進再利用評估。

**若要推進需要：**
- 補全作用機轉（MOA）資料：查詢 DrugBank DB06404 API，取得完整藥理分類與靶點資訊
- 取得原廠仿單：確認警語、禁忌症及毒性資料（目前為 Blocking Data Gap）
- 擴大文獻搜尋範圍：以 MeSH 詞彙「C1 Inhibitor Protein」+「Diabetic Retinopathy」進行系統性搜尋，納入動物實驗及體外研究
- 評估概念驗證可行性：確認是否有其他補體抑制劑（如 Eculizumab、Compstatin）已有 DR 相關臨床數據，可作為機轉可行性的間接參照
- 評估給藥途徑：C1-INH 目前僅為靜脈注射製劑，需評估能否應用於眼科（玻璃體內注射之穩定性、劑量及安全性完全未知）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

