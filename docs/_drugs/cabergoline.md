---
layout: default
title: Cabergoline
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 5
---

# Cabergoline
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

# Cabergoline：從高泌乳素血症到垂體腺癌（垂體腫瘤）

## 一句話總結

Cabergoline 是一種多巴胺 D2 受體促效劑，原本用於高泌乳素血症與泌乳素分泌型垂體腫瘤。
TxGNN 模型預測它可能對**垂體腺癌 (Pituitary Adenocarcinoma)** 有效，但此預測的直接證據很薄弱：僅有 3 篇個案或不相關文獻，且沒有臨床試驗。
相關的**垂體癌 (Pituitary Cancer)** 項目有 **14 個臨床試驗**和 **20 篇文獻**，不過這些證據大多針對垂體腺瘤，而非真正的垂體癌。

> 說明：排名第 1 的預測為垂體腺癌，但證據最完整的是排名第 3 的「垂體癌」。以下表格與評估以排名第 3 的資料呈現，並在相關處註明差異。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高泌乳素血症、泌乳素分泌型垂體腫瘤（香港許可證未提供核准適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 垂體腺癌 (Pituitary Adenocarcinoma)；證據最完整的相關項目為垂體癌 (Pituitary Cancer) |
| TxGNN 預測分數 | 垂體腺癌 99.06%；垂體癌 99.04% |
| 證據等級 | 垂體腺癌 L4；垂體癌 L1（僅適用於腺瘤概念，需保留解讀） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold（垂體腺癌）；Proceed with Guardrails（限腺瘤相關研究方向） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Cabergoline 是 D2 多巴胺受體促效劑，能抑制泌乳素分泌，並可使表現 D2 受體的垂體腫瘤縮小。

垂體腺瘤與垂體癌的腫瘤細胞可能表現 D2 受體，這是預測合理的基礎。試驗 NCT00889525 的背景說明提到，體外研究顯示促腎上腺皮質素 (ACTH) 分泌型腺瘤具有 D2 受體；另一項試驗 NCT01620138 也在研究 D2 受體的表現。

但需要注意：
- 目前資料中的「垂體癌」證據主要來自垂體**腺瘤**（泌乳素瘤、無功能腺瘤、庫欣氏病相關腫瘤），並非轉移性垂體癌。
- 泌乳素瘤本來就是核准適應症，這部分不算真正的藥物再利用。真正的新方向是無功能垂體腺瘤 (NFPA) 的生長控制、手術後殘留腫瘤，以及庫欣氏病相關的 ACTH 分泌型腫瘤。
- 對真正的垂體癌，目前沒有直接證據，且所列試驗的療效結果在資料中均未提供，效果方向尚未確認。

---

## 臨床試驗證據

以下為「垂體癌」項目的臨床試驗（垂體腺癌項目沒有臨床試驗）。依相關性挑選 10 項：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00889525](https://clinicaltrials.gov/study/NCT00889525) | Phase 3 | 完成 | 未提供 | 評估 Cabergoline 治療 ACTH 分泌型垂體腫瘤（庫欣氏病）；結果未提供 |
| [NCT03271918](https://clinicaltrials.gov/study/NCT03271918) | Phase 3 | 完成 | 140 | 隨機、開放性試驗，評估 Cabergoline 用於經蝶竇手術後殘留的無功能垂體腺瘤；結果未提供 |
| [NCT02288962](https://clinicaltrials.gov/study/NCT02288962) | Phase 3 | 進行中（不再招募） | 60 | 隨機對照試驗，多巴胺促效劑治療無功能垂體腺瘤 |
| [NCT01620138](https://clinicaltrials.gov/study/NCT01620138) | Phase 2/3 | 完成 | 21 | 無功能腺瘤與抗藥性泌乳素瘤中體生長抑素與多巴胺受體的表現及體內外反應，支持 D2 表現的機轉依據 |
| [NCT07034859](https://clinicaltrials.gov/study/NCT07034859) | Phase 4 | 邀請登記中 | 30 | 隨機分為 Cabergoline 組與未治療組，共 48 週，評估原發治療是否縮小無功能腺瘤 |
| [NCT00376064](https://clinicaltrials.gov/study/NCT00376064) | Phase 4 | 完成 | 20 | 單臂概念驗證，Octreotide 合併 Cabergoline 用於對體抑素類似物反應不佳的肢端肥大症 |
| [NCT01915303](https://clinicaltrials.gov/study/NCT01915303) | Phase 2 | 提前終止 | 68 | Pasireotide 單用或合併 Cabergoline 治療庫欣氏病 |
| [NCT07463235](https://clinicaltrials.gov/study/NCT07463235) | Phase 3 | 招募中 | 70 | 高劑量 Cabergoline 用於微小泌乳素瘤（原適應症，主要提供劑量與安全性資訊） |
| [NCT07045935](https://clinicaltrials.gov/study/NCT07045935) | Phase 4 | 招募中 | 60 | 泌乳素瘤患者使用多巴胺促效劑後的葡萄糖代謝結果（原適應症族群） |
| [NCT00460616](https://clinicaltrials.gov/study/NCT00460616) | 不適用 | 完成 | 50 | 觀察性研究，長期使用 Cabergoline 之泌乳素瘤患者的心臟異常與瓣膜逆流盛行率 |

---

## 文獻證據

優先列出綜述與機轉研究；垂體腺癌項目的文獻多為個案報告，此處一併標註。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37097352](https://pubmed.ncbi.nlm.nih.gov/37097352/) | 2023 | Review | JAMA | 垂體腺瘤的診斷與處置綜述 |
| [31597135](https://pubmed.ncbi.nlm.nih.gov/31597135/) | 2020 | Review | Neuroendocrinology | Cabergoline 治療垂體及其他腫瘤的新機轉與潛在更廣泛應用 |
| [36013562](https://pubmed.ncbi.nlm.nih.gov/36013562/) | 2022 | Review | Medicina (Kaunas) | 泌乳素瘤治療，包括侵襲性泌乳素瘤的多模式治療 |
| [40876473](https://pubmed.ncbi.nlm.nih.gov/40876473/) | 2025 | Review | Lancet Diabetes Endocrinol | 泌乳素分泌型腺瘤的致病機轉、診斷與處置 |
| [25732645](https://pubmed.ncbi.nlm.nih.gov/25732645/) | 2015 | 綜述 | Endocrinol Metab Clin North Am | 多數研究顯示 Cabergoline 與顯著瓣膜病變風險增加無關，但仍有爭議 |
| [28025719](https://pubmed.ncbi.nlm.nih.gov/28025719/) | 2017 | Review | Pituitary | Cabergoline 用於肢端肥大症 |
| [38989697](https://pubmed.ncbi.nlm.nih.gov/38989697/) | 2024 | 前臨床 | Neuro-oncology | 抑制 HTR2B 可抑制無功能垂體腺瘤生長，並增強 Cabergoline 的敏感性 |
| [34034260](https://pubmed.ncbi.nlm.nih.gov/34034260/) | 2022 | Review | Neuroendocrinology | 微小 RNA 與多巴胺促效劑抗藥性泌乳素瘤；約 10% 使用 Cabergoline 者出現抗藥性 |
| [20497940](https://pubmed.ncbi.nlm.nih.gov/20497940/) | 2010 | 個案報告 | Endocr Pract | 異位 ACTH 分泌患者長期使用 Octreotide 或 Cabergoline 的反應（垂體腺癌項目） |
| [41760078](https://pubmed.ncbi.nlm.nih.gov/41760078/) | 2026 | 個案報告 | Medicine | MEN1 基因意義未明變異的非典型病程（與療效關聯有限，垂體腺癌項目） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-41290 | DOSTINEX TAB 0.5MG（輝瑞） | 片劑 | 資料未提供 |
| HK-67878 | CABENEX TABLETS 0.5MG（SB Pharma） | 片劑 | 資料未提供 |

---

## 細胞毒性

Cabergoline 為多巴胺促效劑，並非傳統細胞毒性化療藥物，原適應症也非惡性腫瘤，因此不適用細胞毒性評估。

---

## 安全性考量

- **知識圖譜中的禁忌疾病**（來自知識圖譜關聯，非仿單內容）：肝病、膽囊疾病、心臟瓣膜疾病、肺纖維化（含發炎後肺纖維化）、IgG4 相關後腹膜纖維化、子癇前症（含重度）。
- **藥物交互作用**：共查得 60 筆，以下為主要項目：
  - 嚴重 (Major)：Lorcaserin、Clarithromycin
  - 中度 (Moderate)：Metoclopramide
  - 其餘多為等級未明，如 Pantoprazole、Omeprazole、Metformin、Simvastatin、Prednisone 等
- **瓣膜病變**：高劑量 Cabergoline（如帕金森氏症用量）曾有心臟瓣膜病變的報導，用於垂體腫瘤時是否增加風險仍有爭議。
- **青光眼**：有個案報告指出，使用 Cabergoline 後出現雙側閉角型青光眼，因此預測「青光眼」適應症反而帶有潛在傷害訊號。

其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（垂體腺癌）／Proceed with Guardrails（限腺瘤相關研究問題）**

**理由：**
- 預測的「垂體腺癌」僅有個案或不相關文獻（L4），沒有臨床試驗，直接證據不足，建議暫緩。
- 「垂體癌」項目有多個 Phase 3 試驗（如 NCT03271918、NCT02288962、NCT00889525），但針對的是腺瘤；泌乳素瘤本身是原適應症。真正的新方向是無功能腺瘤與庫欣氏病相關腫瘤，可作為研究問題，但必須先釐清療效。
- 其他預測（進行性老化症候群相關、痙攣性四肢麻痺型腦性麻痺）僅有模型分數，無證據；青光眼則有安全疑慮，均不建議推進。

**若要推進需要：**
- 取得 NCT03271918、NCT02288962、NCT00889525 的實際療效結果
- 釐清真正垂體癌（轉移性）與腺瘤的證據差異，並尋找垂體癌的直接研究
- 補充詳細作用機轉資料（MOA）
- 取得香港仿單的警語與禁忌，並完成安全性篩選
- 制定心臟瓣膜（心臟超音波）及眼壓的監測計畫，並審視肝病、膽囊疾病、肺纖維化等禁忌族群
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

