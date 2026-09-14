---
layout: default
title: Salicylamide
parent: 中證據等級 (L3-L4)
nav_order: 673
evidence_level: L3
indication_count: 5
---

# Salicylamide
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Salicylamide：候選藥物於咽炎（Pharyngitis）之老藥新用評估

## 一句話總結

Salicylamide（水楊醯胺）是水楊酸類似物，具解熱、鎮痛、消炎作用，歷史上作為複方感冒藥與喉嚨痛製劑成分使用，目前在香港未取得藥品許可證、尚未上市。
TxGNN 模型預測它可能對**咽炎 (Pharyngitis)** 有效，
目前有 **3 篇 1950–60 年代文獻**支持，但**無任何臨床試驗登記**，且關鍵安全性資料（仿單警語、禁忌症）仍缺乏。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無正式核准適應症資料（DrugBank 未列出，香港未上市） |
| 預測新適應症 | 咽炎 (Pharyngitis) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Salicylamide 是水楊酸的類似物（並非經代謝轉化為水楊酸），具有非選擇性 COX 抑制相關的解熱、鎮痛、消炎特性。

Salicylamide 長期作為複方感冒藥與退熱鎮痛製劑成分使用（如 Dilacol、Donaran、PL 感冒藥等），主要用於緩解發燒、頭痛、全身痠痛及喉嚨痛等上呼吸道症狀。這類症狀與咽炎（喉嚨發炎與疼痛）高度重疊，因此 TxGNN 預測具一定的生物學合理性。

機轉上，其鎮痛消炎作用理論上可緩解咽炎相關的局部發炎與疼痛症狀，但目前並無明確受體或分子通路層級的機轉資料，此為評估此適應症合理性時的主要限制。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [5354503](https://pubmed.ncbi.nlm.nih.gov/5354503/) | 1969 | RCT（雙盲、活性對照） | Minerva medica | 比較兩種鉍劑製劑用於咽扁桃腺炎之雙盲研究（原文摘要未提供，無法擷取具體療效數據） |
| [14126993](https://pubmed.ncbi.nlm.nih.gov/14126993/) | 1963 | 病例系列 | Kinderarztliche Praxis | 新型直腸栓劑劑型退熱鎮痛藥之臨床應用經驗（原文摘要未提供） |
| [13060598](https://pubmed.ncbi.nlm.nih.gov/13060598/) | 1953 | 病例系列 | Gazzetta medica italiana | Salicylamide 併用對胺基苯甲酸鈉治療嬰幼兒卡他性扁桃腺炎（原文摘要未提供） |

> 註：上述文獻均為 1950–60 年代發表，缺乏摘要內容，且多屬病例系列（tier 3），證據強度有限。

---

## 香港上市資訊

本藥物於香港未取得任何藥品許可證，目前未上市，無註冊產品資訊可供列出。

---

## 安全性考量

- **正式安全性資料缺口**：TFDA/香港衛生署仿單警語與禁忌症資料目前缺乏，此為 **Blocking** 等級的資料缺口，依評估規則**無法進入 S1 安全性初評**，需優先補齊。
- **已知毒性文獻**（來自其他候選適應症之證據檢索，屬藥物本身安全性資訊）：
  - 過量中毒風險（[PMID 8864802](https://pubmed.ncbi.nlm.nih.gov/8864802/)，Salicylamide toxicity in overdose）
  - 含 salicylamide 之複方感冒藥（PL）曾有藥物誘發溶血性貧血併顆粒球缺乏症案例報告（[PMID 8952318](https://pubmed.ncbi.nlm.nih.gov/8952318/)）
- 藥物交互作用查詢無資料（query_status: not_found）。

---

## 結論與下一步

**決策：Hold**

**理由：**
咽炎與普通感冒兩項候選適應症雖有歷史文獻支持（L3），但均為 1950–60 年代小型病例系列或雙盲研究，證據陳舊且強度有限；更關鍵的是，TFDA 仿單警語與禁忌症資料為 **Blocking** 缺口，依規則無法進入 S1 安全性初評。此外本藥物在香港未上市，無許可證資訊可佐證其法規地位，且已有文獻報告過量中毒與溶血性貧血風險，須先完成安全性評估才可能進一步推進。

**若要推進需要：**
- 取得 TFDA（或香港衛生署）正式仿單警語與禁忌症資料（Blocking，優先補齊）
- 補齊作用機轉 (MOA) 詳細資料
- 尋找 2000 年後之現代臨床證據，取代目前陳舊之 1950–60 年代文獻
- 評估過量中毒、溶血性貧血等已知安全性風險對候選適應症的影響

---

### 附註：其他預測適應症（證據不足，暫不建議推進）

| 適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|--------|-----------|---------|---------|------|
| Nasal cavity disease | 99.97% | L5 | S0 | Hold（唯一文獻為羊隻寄生蟲研究，判定為偽陽性關聯） |
| Acute laryngopharyngitis | 99.97% | L5 | S0 | Hold（無任何臨床試驗或文獻佐證） |
| Trigeminal autonomic cephalalgia | 99.94% | L5 | S0 | Hold（機轉不合理，無證據支持） |
| Common cold | 99.93% | L3 | S1 | Research Question（與咽炎證據性質相近，可併案評估，但同樣受限於 Blocking 安全性缺口） |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

