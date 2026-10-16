---
layout: default
title: Dorzolamide
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dorzolamide：預測新適應症為原發性遺傳性青光眼 (primary hereditary glaucoma)（證據等級 L5）。原適應症：開角型青光眼、高眼壓症"
---

# Dorzolamide
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

# Dorzolamide：從開角型青光眼到原發性遺傳性青光眼（及其他預測適應症）

## 一句話總結

Dorzolamide 是局部用碳酸酐酶抑制劑，原本用於開角型青光眼與高眼壓症。
TxGNN 模型的首位預測為**原發性遺傳性青光眼 (primary hereditary glaucoma)**，但目前**沒有任何臨床試驗或文獻**直接支持。
證據最充分的預測是「開角型青光眼」，有 **34 個臨床試驗**與多篇系統性回顧，不過這屬於原有適應症的再確認，並非真正的新用途。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 開角型青光眼、高眼壓症（許可證資料未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 原發性遺傳性青光眼 (primary hereditary glaucoma) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（僅模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

> 補充：排名第 6、7 的「glaucoma 1, open angle」與「open angle glaucoma」證據等級為 L1，建議為 Proceed with Guardrails，但這屬於原適應症的再確認。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫記錄。根據藥理學資料，Dorzolamide 抑制睫狀突中的碳酸酐酶 II，減少碳酸氫根與房水生成，進而降低眼壓。資料中也顯示它作用於多種碳酸酐酶亞型（CA1、CA7、CA12、CA14）。

原發性遺傳性青光眼同樣以眼壓升高為核心病理，因此降眼壓機轉上有合理性。不過這個高分更可能反映與已核准青光眼適應症的重疊，並不代表有獨立證據。

其他預測適應症（如禿髮類疾病、心衰竭、急性肺心症、呼吸衰竭）在機轉上缺乏可信連結：
- **毛髮疾患**（hypotrichosis、alopecia、alopecia areata）：碳酸酐酶抑制與毛囊發育或自體免疫機轉無明確關聯，很可能是知識圖譜的假象。
- **心肺疾病**：全身性碳酸酐酶抑制劑（如 acetazolamide）理論上有利尿或呼吸刺激作用，但局部用 dorzolamide 全身暴露量極低，療效不太可能。相關文獻僅涉及安全性與處方情境（如對 beta 阻斷劑禁忌的病人選用），並非療效證據。

---

## 臨床試驗證據

首位預測（原發性遺傳性青光眼）目前無相關臨床試驗登記。

以下為證據最充分的相關預測「開角型青光眼」的代表性試驗（原適應症，非新適應症）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00878917](https://clinicaltrials.gov/study/NCT00878917) | Phase 3 | 完成 | 32 | Dorzolamide 2% 隨機雙盲交叉等效性試驗，用於開角型青光眼/高眼壓症 |
| [NCT00314171](https://clinicaltrials.gov/study/NCT00314171) | Phase 3 | 完成 | 437 | 青光眼療法於開角型青光眼/高眼壓症的安全性與有效性 |
| [NCT00108017](https://clinicaltrials.gov/study/NCT00108017) | Phase 3 | 完成 | 330 | Dorzolamide/timolol 複方 24 小時眼壓控制 |
| [NCT00546286](https://clinicaltrials.gov/study/NCT00546286) | Phase 3 | 完成 | 170 | Dorzolamide-timolol 作為未治療病人第一線療法的 12 週開放試驗 |
| [NCT03257813](https://clinicaltrials.gov/study/NCT03257813) | Phase 3 | 完成 | 60 | PRO-122 眼用溶液非劣性試驗 |
| [NCT00991822](https://clinicaltrials.gov/study/NCT00991822) | Phase 2/3 | 完成 | 160 | Dorzolamide 與 timolol 對視神經盤血流的影響 |
| [NCT00675207](https://clinicaltrials.gov/study/NCT00675207) | Phase 4 | 完成 | 120 | Brimonidine、dorzolamide、brinzolamide 作為前列腺素類似物的輔助治療比較 |
| [NCT00822081](https://clinicaltrials.gov/study/NCT00822081) | Phase 4 | 完成 | 140 | Brimonidine/timolol 與 dorzolamide/timolol 複方比較 |
| [NCT02325518](https://clinicaltrials.gov/study/NCT02325518) | Phase 4 | 完成 | 218 | Brinzolamide/timolol 與 dorzolamide/timolol 複方比較 |
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | 完成 | 37 | Latanoprost 與 dorzolamide 用於兒童青光眼 |

> 另有一項已撤回試驗（NCT00815373，n=0），無數據可用。

---

## 文獻證據

首位預測（原發性遺傳性青光眼）目前無相關文獻。以下為開角型青光眼相關文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26526633](https://pubmed.ncbi.nlm.nih.gov/26526633/) | 2016 | 系統性回顧/網絡統合分析 | Ophthalmology | 比較原發性開角型青光眼第一線藥物的相對療效 |
| [17943780](https://pubmed.ncbi.nlm.nih.gov/17943780/) | 2007 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 原發性開角型青光眼與高眼壓症的藥物介入 |
| [39677168](https://pubmed.ncbi.nlm.nih.gov/39677168/) | 2024 | RCT | Cureus | Brinzolamide/timolol 與 dorzolamide/timolol 複方在印度病人的 Phase 3 比較 |
| [19365194](https://pubmed.ncbi.nlm.nih.gov/19365194/) | 2009 | RCT | J Glaucoma | Brinzolamide/timolol 與 dorzolamide/timolol 複方的安全性與療效比較 |
| [11200308](https://pubmed.ncbi.nlm.nih.gov/11200308/) | 2000 | Review | Drugs & Aging | 局部 dorzolamide 2%/timolol 0.5% 用於開角型青光眼的回顧 |
| [9143858](https://pubmed.ncbi.nlm.nih.gov/9143858/) | 1997 | Review | Drugs & Aging | Dorzolamide 藥理與治療潛力，尖峰時眼壓降低約 4–6 mmHg |
| [40719703](https://pubmed.ncbi.nlm.nih.gov/40719703/) | 2025 | RCT | J Glaucoma | Dorzolamide 與 netarsudil 對早期青光眼眼壓與眼灌流的比較 |
| [32106236](https://pubmed.ncbi.nlm.nih.gov/32106236/) | 2020 | 統合分析 | PLoS One | Latanoprost/timolol 複方與其他複方的眼壓降低效果比較 |
| [39569785](https://pubmed.ncbi.nlm.nih.gov/39569785/) | 2024 | 臨床研究 | Vestn Oftalmol | Dorzolamide/timolol 複方在原發性開角型青光眼的療效與安全性 |
| [37425383](https://pubmed.ncbi.nlm.nih.gov/37425383/) | 2023 | 回溯性世代研究 | Malays J Med Sci | 固定與非固定 dorzolamide/timolol 複方的療效與依從性比較 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-40713 | TRUSOPT EYE SOLUTION 2% | 眼用溶液 | — |
| HK-66812 | REZLOD EYE DROPS SOLUTION 20MG/ML | 眼藥水 | — |
| HK-64039 | DORZO EYE DROPS 2%W/V | 眼藥水 | — |
| HK-46578 | COSOPT OPHTHALMIC SOLUTION | 眼用溶液 | — |
| HK-61930 | DORZOLAMIDE AND TIMOLOL STADA EYE DROPS | 眼藥水 | — |

> 共 10 張有效許可證（均為有效單方登記）。許可證資料未載明劑型與核准適應症文字。

---

## 安全性考量

- **知識圖譜標示的相關禁忌疾病**（來自藥物－疾病關聯資料，非仿單文字）：糖尿病、糖尿病酮酸中毒、重症肌無力、神經肌肉接合處疾病、甲狀腺機能亢進（含 Graves 病、甲狀腺毒症）、低血糖、房室傳導阻滯、肺氣腫、支氣管疾病、過敏性休克。其中部分可能與複方中的 timolol 成分相關，需對照仿單確認。
- **藥理交互作用**：藥物交互作用查詢已完成，未發現具分級的藥物間交互作用，僅有與碳酸酐酶 1、7、12、14 的標靶結合資料。

仿單的警語與禁忌資料尚未取得，詳細安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**（針對首位預測「原發性遺傳性青光眼」）

**理由：**
- 首位預測僅有模型分數，無任何臨床試驗或文獻支持（L5）。其餘新適應症（禿髮類、心肺疾病）機轉上缺乏可信連結，很可能是知識圖譜假象。
- 「開角型青光眼」雖有 L1 等級證據（建議 Proceed with Guardrails），但屬原有適應症，並非新用途。注意事項：多為 Phase 4 主動對照試驗，多項樣本偏小（n=32–60），許多比較的是複方，難以單獨評估 dorzolamide 的貢獻，另有一項試驗已撤回。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料（目前為阻斷性資料缺口）
- 補充作用機轉資料（可由 DrugBank 取得）
- 針對遺傳性青光眼（如先天性或兒童青光眼）搜尋專屬證據；現有的兒童青光眼 Phase 2 試驗（NCT01527682）可作為起點
- 確認許可證的核准適應症與劑型，以釐清原適應症範圍
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

