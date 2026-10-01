---
layout: default
title: Dexketoprofen
parent: 僅模型預測 (L5)
nav_order: 261
evidence_level: L5
indication_count: 10
---

# Dexketoprofen
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

# Dexketoprofen：從 NSAID 止痛藥到偏頭痛

## 一句話總結

Dexketoprofen 是 ketoprofen 的活性 S-鏡像異構物，屬於 COX 抑制型非類固醇消炎止痛藥（NSAID）。
TxGNN 模型預測它可能對多種疾病有效，其中證據最完整的是**偏頭痛 (Migraine Disorder)**，目前有 **7 個臨床試驗**和 **20 篇文獻**支持。
排名第 1 的**肌腱炎 (Tendinitis)** 目前只有 1 篇間接文獻。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症（排名第 1） | 肌腱炎 (Tendinitis) |
| 預測新適應症（證據最強） | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 肌腱炎 99.90%；偏頭痛 99.87% |
| 證據等級 | 肌腱炎 L4；偏頭痛 L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | 偏頭痛：Proceed with Guardrails；肌腱炎：Research Question |

> 證據等級說明：偏頭痛的 L1 是依證據包評分。有多個已完成的 Phase 4 RCT、多篇 RCT 和 1 篇統合分析，但這些試驗都不是 Phase 3，與本報告的 L1 條件（≥2 個已完成的 Phase 3 RCT）並不完全吻合。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位空白）。根據已知資訊，Dexketoprofen 是 ketoprofen 的 S-鏡像異構物，屬於 COX-1/COX-2 抑制劑。它透過阻斷前列腺素合成，減少發炎與疼痛訊號。

偏頭痛發作時有前列腺素參與的周邊與中樞敏感化及神經性發炎，因此與其他 NSAID 一樣，Dexketoprofen 在機轉上適用於急性偏頭痛。這個預測有臨床證據支持，包括安慰劑對照 RCT 和統合分析。

肌腱炎的推論同樣是 COX 抑制的類別效應（NSAID 在肌腱病變中用於緩解症狀）。但目前唯一的文獻研究的是急診非外傷性肌肉骨骼疼痛，並非肌腱炎專屬，屬間接證據。

## 臨床試驗證據

以下為偏頭痛與頭痛相關試驗（已依相關性挑選）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02159547](https://clinicaltrials.gov/study/NCT02159547) | Phase 4 | 完成 | 224 | 靜脈注射 Dexketoprofen 對比安慰劑，用於急診偏頭痛發作（尚無結果摘要） |
| [NCT01730326](https://clinicaltrials.gov/study/NCT01730326) | Phase 4 | 完成 | 200 | 靜脈注射 Dexketoprofen 對比 Paracetamol，用於急診急性偏頭痛頭痛 |
| [NCT04372264](https://clinicaltrials.gov/study/NCT04372264) | Phase 4 | 未知 | 210 | 靜脈注射 Paracetamol、Dexketoprofen、Ibuprofen 的 VAS 疼痛評分比較 |
| [NCT04252521](https://clinicaltrials.gov/study/NCT04252521) | N/A | 完成 | 150 | Metoclopramide、Dexketoprofen 及兩者合併於急性偏頭痛的雙盲比較 |
| [NCT04533568](https://clinicaltrials.gov/study/NCT04533568) | Phase 4 | 完成 | 160 | 靜脈注射 Ibuprofen 對比 Dexketoprofen，用於偏頭痛相關頭痛 |
| [NCT04519346](https://clinicaltrials.gov/study/NCT04519346) | N/A | 完成 | 150 | 皮內中胚層療法對比全身性療法（推測 Dexketoprofen 為對照，尚未確認） |
| [NCT03830398](https://clinicaltrials.gov/study/NCT03830398) | Phase 4 | 未知 | 225 | Paracetamol 對比 Dexketoprofen，用於電痙攣治療後頭痛（非偏頭痛） |
| [NCT05780671](https://clinicaltrials.gov/study/NCT05780671) | N/A | 完成 | 160 | 補充氧氣的效果；標準治療含 Dexketoprofen 50 mg（間接相關） |

肌腱炎、纖維肌痛等其他預測適應症目前無相關臨床試驗登記。

## 文獻證據

以下為偏頭痛相關文獻。證據包中多數摘要被截斷，因此「主要發現」只列出研究比較的內容，不含結果數據。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31725614](https://pubmed.ncbi.nlm.nih.gov/31725614/) | 2019 | Meta-analysis | Medicine | 統合分析 Dexketoprofen 對比安慰劑於偏頭痛發作的止痛效果 |
| [25944813](https://pubmed.ncbi.nlm.nih.gov/25944813/) | 2016 | RCT | Cephalalgia | 靜脈注射 Dexketoprofen 對比安慰劑，用於急診偏頭痛 |
| [24394884](https://pubmed.ncbi.nlm.nih.gov/24394884/) | 2014 | RCT | Emerg Med J | 靜脈注射 Paracetamol 對比 Dexketoprofen，用於急診急性偏頭痛 |
| [32359776](https://pubmed.ncbi.nlm.nih.gov/32359776/) | 2020 | RCT | Am J Emerg Med | Metoclopramide、Dexketoprofen 及合併使用的止痛效果與安全性 |
| [24412801](https://pubmed.ncbi.nlm.nih.gov/24412801/) | 2014 | Phase II RCT | J Pain | 25 mg 與 50 mg Dexketoprofen 對比安慰劑的劑量優化研究（93 位病人） |
| [24363238](https://pubmed.ncbi.nlm.nih.gov/24363238/) | 2014 | RCT | Cephalalgia | Frovatriptan 加 Dexketoprofen 對比單用 Frovatriptan |
| [34085549](https://pubmed.ncbi.nlm.nih.gov/34085549/) | 2021 | RCT | Ann Saudi Med | 皮內中胚層療法對比靜脈注射 Dexketoprofen，用於無預兆偏頭痛 |
| [25056381](https://pubmed.ncbi.nlm.nih.gov/25056381/) | 2014 | RCT | Expert Rev Neurother | Frovatriptan 與 Dexketoprofen 的療效與耐受性 |
| [37291500](https://pubmed.ncbi.nlm.nih.gov/37291500/) | 2023 | Meta-analysis | BMC Neurol | Metoclopramide 與其他偏頭痛藥物的網絡統合分析 |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | 美國頭痛學會 2025 年急診偏頭痛注射藥物治療指引更新 |

其他預測適應症：
- 肌腱炎僅有 [30744914](https://pubmed.ncbi.nlm.nih.gov/30744914/)（2019，RCT，Am J Emerg Med），比較靜脈注射 Dexketoprofen 與 Paracetamol 治療急診非外傷性肌肉骨骼疼痛，非肌腱炎專屬。
- 纖維肌痛、類風濕性關節炎等目前無文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65491 | SKUDEXA TABLETS 75MG/25MG（A. MENARINI HONG KONG LIMITED） | — | — |

證據包未提供劑型與核准適應症。品名規格為 75mg/25mg，可能是複方，實際成分與適應症請以仿單確認。

## 其他預測適應症

| 排名 | 適應症 | 預測分數 | 證據等級 | 建議 |
|-----|--------|---------|---------|------|
| 1 | 肌腱炎 (Tendinitis) | 99.90% | L4 | Research Question |
| 2 | 纖維肌痛 (Fibromyalgia) | 99.88% | L5 | Hold |
| 3 | 纖維性肌炎 (Myositis Fibrosa) | 99.88% | L5 | Hold |
| 4 | 特發性肉芽腫性肌炎 | 99.88% | L5 | Hold |
| 5 | 類風濕性關節炎 | 99.88% | L5 | Hold |
| 7 | 頭痛疾患 (Headache Disorder) | 99.86% | L2 | Research Question |
| 8 | 腦幹先兆偏頭痛 | 99.86% | L2 | Research Question |
| 9 | 外生骨疣 (Exostosis) | 99.85% | L5 | Hold |
| 10 | 先天性少毛症伴粟丘疹 | 99.83% | L5 | Hold |

- **纖維肌痛**：屬中樞敏感化疾病，NSAID 一般效果有限。
- **類風濕性關節炎**：NSAID 只能緩解症狀，無法改變疾病進程。
- **頭痛疾患**：直接證據幾乎都來自偏頭痛。唯一的非偏頭痛藥物試驗 NCT03830398 狀態未知，也無結果。
- **腦幹先兆偏頭痛**：現有 RCT 針對一般偏頭痛族群，沒有此亞型的專屬分析，NSAID 也不處理先兆症狀。
- **外生骨疣、先天性少毛症伴粟丘疹**：找不到合理機轉，很可能是知識圖譜的假象。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails（僅限偏頭痛急性治療）**

**理由：**
- 偏頭痛有多個已完成的 Phase 4 RCT、安慰劑對照研究與統合分析，急性發作期的證據最充分。
- 這些證據只涵蓋急性治療，不含預防，且各地區核准標示不一。
- 其餘適應症多為純模型預測或間接證據，建議暫緩（Hold）或列為研究問題。

**若要推進需要：**
- 取得香港衛生署（Department of Health）仿單，確認警語、禁忌與核准適應症。這是目前的阻斷性資料缺口，未補齊前無法進入安全性篩選。
- 確認 SKUDEXA 的實際成分（是否為複方）與劑型，並釐清與研究所用劑型（靜脈注射與口服）的差異。
- 補充 DrugBank 作用機轉資料。
- 建立 NSAID 風險控管：胃腸道、腎臟與心血管風險，避免用於 NSAID 過敏或高出血風險病人。
- 肌腱炎需要專屬臨床試驗才能評估。

本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

