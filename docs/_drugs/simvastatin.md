---
layout: default
title: Simvastatin
parent: 高證據等級 (L1-L2)
nav_order: 688
evidence_level: L1
indication_count: 5
---

# Simvastatin
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# SIMVASTATIN：原適應症資料缺失 → 預測新適應症為家族性高膽固醇血症

## 一句話總結

> SIMVASTATIN（辛伐他汀）是 HMG-CoA reductase 抑制劑類的他汀藥物，但本 Evidence Pack 未提供其原始核准適應症資料（資料缺口）。
> TxGNN 模型預測它對**家族性高膽固醇血症 (Familial Hypercholesterolemia)** 有效，
> 目前有 **19 個臨床試驗**和 **18 篇文獻**支持這個方向，證據等級達 L1。
> ⚠️ 需特別注意：模型自身的機轉推論註記指出，家族性高膽固醇血症可能本來就是 simvastatin 的既有核准適應症，而非典型的「老藥新用」案例——詳見下方說明。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | ⚠️ 資料缺失（Evidence Pack 中 `original_indications` 與香港許可證皆為空） |
| 預測新適應症 | 家族性高膽固醇血症 (Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.63%（rank 7382） |
| 證據等級 | L1 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 SIMVASTATIN 的正式作用機轉資料（Evidence Pack 中 `original_moa` 標記為資料缺口）。不過模型針對此適應症提供了機轉推論：

Simvastatin 抑制 HMG-CoA reductase，降低肝臟膽固醇合成並上調 LDL 受體表現；家族性高膽固醇血症（FH）主要由 LDL 受體基因缺陷（LDLR/APOB/PCSK9）導致 LDL-C 顯著升高，機轉上與 simvastatin 的作用路徑直接相關。

**重要警示**：模型註記明確指出——這很可能**不是典型的老藥新用案例**，而是 simvastatin 本身既有的核准適應症之一，只是此份 Evidence Pack 的 `original_indications` 欄位剛好是空的（資料缺口所致）。因此本報告的「新適應症」標籤應審慎解讀，建議在推進前先確認 SIMVASTATIN 是否已在其他地區核准用於 FH 治療。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | 完成 | 486 | 雙盲安慰劑對照，評估 alirocumab 於 heFH 族群療效安全性（simvastatin 為背景治療） |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3b | 完成 | 442 | 多中心研究比較 rosuvastatin 與 simvastatin 對腎功能之影響，涵蓋 heFH 族群 |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | 完成 | 720 | ENHANCE 試驗：simvastatin 單用 vs 併用 ezetimibe，於 heFH 患者評估動脈硬化進展 |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | 完成 | 18 | 兒童/青少年同型合子 FH 評估 alirocumab 療效（simvastatin 為背景治療） |
| [NCT00145574](https://clinicaltrials.gov/study/NCT00145574) | Phase 4 | 完成 | 194 | 評估 colesevelam 於穩定劑量他汀（含 simvastatin）治療中的異型合子 FH 兒童患者 |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | 完成 | 248 | 青少年異型合子 FH 併用 ezetimibe 與 simvastatin 療效安全性 |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | 完成 | 44 | 同型合子 FH 長期併用 ezetimibe 與 atorvastatin/simvastatin 之安全性 |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | 完成 | 50 | 同型合子 FH 評估 ezetimibe 併用 atorvastatin 或 simvastatin 之療效安全性 |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | 完成 | 249 | 異型合子 FH 患者評估 alirocumab（simvastatin 為背景治療之一） |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | 完成 | 216 | 異型合子 FH 或高心血管風險族群評估 alirocumab（併用穩定他汀療法） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | RCT | NEJM | Simvastatin 併用/不併用 ezetimibe 於 FH 患者，評估動脈粥樣硬化進展（ENHANCE 試驗） |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opin Drug Saf | Simvastatin 於 FH 治療之效益與風險評估，強調長期安全性重要性 |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Safety | Simvastatin 於 FH 患者之效益與風險，FH 未治療者預期壽命減少 15-30 年 |
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guideline | Circulation | 2026 ACC/AHA 血脂異常管理指引，取代 2018 版膽固醇管理指引 |
| [35629051](https://pubmed.ncbi.nlm.nih.gov/35629051/) | 2022 | Cohort | J Clin Med | 評估 simvastatin 治療兒童 FH 對細胞免疫參數之影響 |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Review | Cochrane DB Syst Rev | 兒童 FH 使用他汀類藥物之系統性回顧 |
| [27417002](https://pubmed.ncbi.nlm.nih.gov/27417002/) | 2016 | 觀察性研究 | JACC | 他汀治療對異型合子 FH 患者冠心病與全因死亡率之影響 |
| [30270066](https://pubmed.ncbi.nlm.nih.gov/30270066/) | 2018 | 回溯性研究 | Atherosclerosis | 斯洛伐克 FH 治療模式：治療目標、實務與障礙 |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | 比較研究 | Nutr Metab Cardiovasc Dis | 異型合子 FH 治療：atorvastatin vs simvastatin 降膽固醇效果比較 |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | Rosuvastatin 綜述，與 simvastatin 等他汀類比較療效資料 |

---

## 香港上市資訊

目前香港無 SIMVASTATIN 許可證登記（`total_licenses: 0`，`market_status: 未上市`）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充：本次資料收集中，TFDA/HK 仿單警語與禁忌症項目（DG001）被標記為 **Blocking** 等級的資料缺口，代表在補齊此資料前，無法完成 S1 安全性初評。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個 Phase 3 RCT（含 ENHANCE 試驗、alirocumab 對照試驗）及 2026 年最新 ACC/AHA 指引直接支持 simvastatin 於 FH 族群的療效與安全性，證據等級達 L1。
- 但需注意：模型機轉推論本身提示此可能非典型「老藥新用」——FH 極可能已是 simvastatin 的既有適應症，只是本 Evidence Pack 的原適應症欄位剛好缺失，需人工確認釐清。

**若要推進需要：**
- 確認 SIMVASTATIN 在其他地區（如美國 FDA、EMA）是否已核准用於家族性高膽固醇血症，釐清此候選是否屬於真正的「再利用」而非資料缺口造成的誤判。
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，Blocking），以完成 S1 安全性初評。
- 補齊作用機轉正式來源資料（DG002，DrugBank API 查詢），取代目前僅存於單一適應症 rationale 的機轉描述。
- 確認香港上市狀態與許可證規劃，目前 `market_status: 未上市` 意味著若要推進在地應用，需先處理藥證申請流程。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

