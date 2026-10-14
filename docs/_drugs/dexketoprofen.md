---
layout: default
title: Dexketoprofen
parent: 高證據等級 (L1-L2)
nav_order: 266
evidence_level: L1
indication_count: 10
---

# Dexketoprofen
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

# Dexketoprofen：從（原適應症未載明）到偏頭痛

## 一句話總結

Dexketoprofen 是一種非類固醇消炎止痛藥（NSAID），香港已有 1 張許可證，但本次彙整的資料中未載明核准適應症。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，目前有 **5 個臨床試驗**和 **20 篇文獻**支持這個方向。
在 TxGNN 預測分數最高的前幾名適應症中（如肌腱炎），證據都很薄弱，偏頭痛是目前證據最完整的一項，因此以下報告以偏頭痛為主軸。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未載明 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

> 說明：TxGNN 排名第 1 的預測為肌腱炎（分數 99.90%），但僅有 1 篇間接文獻（L4，建議 Hold）。偏頭痛排名第 6，但證據最充分，故作為本報告的主要評估對象。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位未收錄）。依一般藥理知識，Dexketoprofen 屬於 NSAID，透過抑制環氧合酶（COX-1/COX-2）減少前列腺素生成，進而降低發炎與疼痛。

偏頭痛發作時，前列腺素參與神經性發炎與痛覺訊號傳遞，因此 COX 抑制劑理論上可以緩解疼痛。這個機轉推論也得到臨床證據支持：一項隨機對照試驗的統合分析（PMID 31725614）、急診室靜脈注射 Dexketoprofen 對照安慰劑的 RCT（PMID 25944813），以及口服 Dexketoprofen trometamol 的第二期 RCT（PMID 24412801）。

需要注意的是，目前的證據多數來自急診室的靜脈注射用藥，而香港已登記的製劑為口服錠劑（SKUDEXA 75MG/25MG），給藥途徑的對應性尚待確認。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02159547](https://clinicaltrials.gov/study/NCT02159547) | Phase 4 | 完成 | 224 | 急診室靜脈注射 Dexketoprofen vs 安慰劑，用於終止偏頭痛發作 |
| [NCT04252521](https://clinicaltrials.gov/study/NCT04252521) | NA | 完成 | 150 | 靜脈注射 Metoclopramide vs Dexketoprofen vs 兩者合併，用於急性偏頭痛 |
| [NCT01730326](https://clinicaltrials.gov/study/NCT01730326) | Phase 4 | 完成 | 200 | 靜脈注射 Dexketoprofen vs Paracetamol，用於急性偏頭痛頭痛 |
| [NCT04533568](https://clinicaltrials.gov/study/NCT04533568) | Phase 4 | 完成 | 160 | 靜脈注射 Ibuprofen vs Dexketoprofen，用於無預兆偏頭痛 |
| [NCT04372264](https://clinicaltrials.gov/study/NCT04372264) | Phase 4 | 未知 | 210 | 靜脈注射 Paracetamol、Dexketoprofen、Ibuprofen 的疼痛視覺類比量表比較 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31725614](https://pubmed.ncbi.nlm.nih.gov/31725614/) | 2019 | 統合分析 | Medicine | RCT 統合分析，評估 Dexketoprofen 相較安慰劑對偏頭痛疼痛控制的效果 |
| [25944813](https://pubmed.ncbi.nlm.nih.gov/25944813/) | 2016 | RCT | Cephalalgia | 急診室靜脈注射 Dexketoprofen vs 安慰劑，評估終止偏頭痛的效果 |
| [32359776](https://pubmed.ncbi.nlm.nih.gov/32359776/) | 2020 | RCT | Am J Emerg Med | Metoclopramide、Dexketoprofen 與合併療法於急性偏頭痛的止痛效果與安全性 |
| [24412801](https://pubmed.ncbi.nlm.nih.gov/24412801/) | 2014 | RCT（第二期） | J Pain | 93 位患者，比較 25 mg、50 mg Dexketoprofen 與安慰劑的劑量優化交叉試驗 |
| [24394884](https://pubmed.ncbi.nlm.nih.gov/24394884/) | 2014 | RCT | Emerg Med J | 靜脈注射 Dexketoprofen vs Paracetamol 於急性偏頭痛 |
| [25056381](https://pubmed.ncbi.nlm.nih.gov/25056381/) | 2014 | RCT | Expert Rev Neurother | Frovatriptan 與 Dexketoprofen 治療急性偏頭痛的療效與耐受性 |
| [34085549](https://pubmed.ncbi.nlm.nih.gov/34085549/) | 2021 | RCT | Ann Saudi Med | 皮內美容療法 vs 靜脈注射 Dexketoprofen 於無預兆偏頭痛 |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | 指引 | Headache | 美國頭痛學會 2025 年急診室偏頭痛注射藥物治療指引更新 |
| [37291500](https://pubmed.ncbi.nlm.nih.gov/37291500/) | 2023 | 統合分析 | BMC Neurol | Metoclopramide 與其他偏頭痛藥物的系統性回顧與網絡統合分析 |
| [11155464](https://pubmed.ncbi.nlm.nih.gov/11155464/) | 2000 | 臨床研究 | Minerva Med | Dexketoprofen trometamol 治療急性偏頭痛的療效與安全性 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65491 | SKUDEXA TABLETS 75MG/25MG | 未載明 | 未載明 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

另依文獻與一般 NSAID 類別特性，推進時應留意胃腸道、腎臟與心血管風險，以及藥物過度使用性頭痛。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 偏頭痛有多個已完成的 Phase 4 試驗（含安慰劑對照）、多項 RCT 及一篇統合分析，達到 L1 證據等級。
- 但香港許可證的核准適應症與劑型未載明，安全性資料亦缺漏，且多數證據來自靜脈注射劑型，需先確認與本地口服製劑的相容性。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、劑型、警語與禁忌症
- 確認口服製劑（SKUDEXA）與研究所用劑型、劑量的對應性
- 補充 Dexketoprofen 的作用機轉資料（DrugBank）
- 確認香港對偏頭痛適應症的法規標示
- 建立 NSAID 標準風險（胃腸、腎臟、心血管）及藥物過度使用性頭痛的監測計畫

**其他預測適應症簡述：** 頭痛疾患（證據多由偏頭痛外推，建議 Proceed with Guardrails）；肌腱炎僅有間接證據（Hold）；纖維肌痛、類風濕性關節炎等僅有模型預測，無直接證據（Hold）；腦幹預兆偏頭痛缺乏亞型專屬證據（Research Question）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

