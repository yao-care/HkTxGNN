---
layout: default
title: Clobazam
parent: 中證據等級 (L3-L4)
nav_order: 211
evidence_level: L4
indication_count: 10
---

# Clobazam
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

# Clobazam：從 Lennox-Gastaut 症候群到熱性感染相關癲癇症候群 (FIRES)

## 一句話總結

Clobazam 是一種苯二氮平類（1,5-benzodiazepine）抗癲癇藥，原本用於 Lennox-Gastaut 症候群與腦回狀頭皮（cutis verticis gyrata）。
TxGNN 模型預測它可能對**熱性感染相關癲癇症候群（FIRES）**有效，
但目前**沒有臨床試驗**，僅有 **2 篇**間接相關文獻（病例系列與個案報告，且均未直接測試 clobazam）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | Lennox-Gastaut 症候群、腦回狀頭皮（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 熱性感染相關癲癇症候群 (Febrile Infection-Related Epilepsy Syndrome, FIRES) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold（列為研究問題，暫不推進） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Clobazam 是 GABA-A 受體的正向異位調節劑。FIRES 是一種難治性癲癇性腦病變，臨床上常使用 midazolam、lorazepam、巴比妥類等 GABA 能藥物，因此機轉上有合理性。

不過，目前提供的文獻談的是其他藥物（腸道給予 lorazepam、perampanel），並未直接測試 clobazam。此預測目前主要建立在藥物類別層級的推論，屬於間接支持。

此外，排名較後的預測（如 perioral myoclonia with absences、restless legs syndrome 等）幾乎只有模型分數支持，證據更為薄弱，因此本報告以排名第一的 FIRES 為主軸。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | 世代研究／病例系列 | Epileptic Disord | 腸道給予 lorazepam 可作為 midazolam 依賴型 FIRES 患者的撤藥替代策略（未涉及 clobazam） |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | 個案報告 | Cureus | 一名 13 歲男童使用 perampanel，可能有助於降低巴比妥類依賴（未涉及 clobazam） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67412 | TAPCLOB ORAL SUSPENSION 5MG/5ML | 口服懸液 | 未提供 |
| HK-05574 | FRISIUM 10 TAB 10MG | 錠劑 | 未提供 |
| HK-67411 | TAPCLOB ORAL SUSPENSION 10MG/5ML | 口服懸液 | 未提供 |

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用，以下列出較重要者：
  - **嚴重（Major）**：Morphine（含脂質體劑型）、Eliglustat
  - **中度（Moderate）**：Bupropion、Aprepitant、Omeprazole、Esomeprazole、Lansoprazole、Cimetidine、Clarithromycin、Fenfluramine、Metoclopramide 等
  - **輕微（Minor）**：多種制酸劑（氫氧化鎂、氫氧化鋁、碳酸鈣等）

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 模型分數雖高（99.82%），但目前沒有任何臨床試驗，文獻也未直接評估 clobazam 對 FIRES 的效果，證據停留在 L4（僅有機轉推論與間接文獻）。
- 作用機轉資料與仿單安全性資料（警語、禁忌症）仍有缺口，尚無法進入安全性篩選。

**若要推進需要：**
- 取得 Clobazam 的作用機轉資料（如透過 DrugBank）
- 下載並解析香港衛生署的仿單，補齊警語、禁忌症與核准適應症
- 檢索 clobazam 用於 FIRES 或 NORSE 的直接病例報告／回溯性研究
- 評估 FIRES 患者（多為兒童、常需重症照護）是否適合口服劑型（懸液劑 TAPCLOB 可能較合適），並釐清與常用 GABA 能藥物合併使用時的交互作用風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

