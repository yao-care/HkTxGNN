---
layout: default
title: Clofarabine
parent: 僅模型預測 (L5)
nav_order: 211
evidence_level: L5
indication_count: 10
---

# Clofarabine
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

# Clofarabine：從兒童復發／難治性急性淋巴母細胞白血病到骨髓性白血病

## 一句話總結

Clofarabine 是嘌呤核苷類似物的抗代謝化療藥。根據試驗與文獻的描述，它原本用於兒童復發或難治性急性淋巴母細胞白血病（ALL）。
TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效，目前有 **50 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含 **3 個已完成的 Phase 3 試驗**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症；試驗與文獻描述其核准用於兒童復發／難治性 ALL |
| 預測新適應症 | 骨髓性白血病 (Myeloid Leukemia) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L1（依判定規則：≥2 個已完成 Phase 3；資料包內建標示 L2，因相關性評級尚未完成） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據文獻摘要，clofarabine 是第二代嘌呤核苷類似物。它抑制核糖核苷酸還原酶與 DNA 聚合酶，耗竭 DNA 複製所需的去氧核苷三磷酸，也會破壞粒線體膜完整性而誘發細胞凋亡。設計上結合了 fludarabine 與 cladribine 的優點，並更耐去胺作用。

ALL 與急性骨髓性白血病（AML）同屬快速增殖的造血系惡性腫瘤，這類藥物對快速分裂的母細胞都有活性。文獻與試驗顯示，clofarabine 已被用於成人與兒童 AML 的誘導、挽救治療及移植前預處理，這使 TxGNN 的高分預測在機轉與臨床上都合理。

需注意，Phase 3 試驗的療效結果不在本資料包內，無法據此判斷 clofarabine 是否優於標準治療。CoALL 08-09（兒童 ALL）的文獻指出 clofarabine 提高了微量殘存病灶清除率，但預後未改善。成人 ALL 的 HOVON-100 也未見無事件存活期（EFS）改善。這些結果提示，能否清除腫瘤細胞不等於病人存活獲益。

## 臨床試驗證據

本預測共有 50 個相關試驗，以下列出 10 個最相關者（Phase 3 優先，其次為完成的 Phase 2）。「主要發現」僅摘自試驗登記說明，資料包未提供結果數據。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00317642](https://clinicaltrials.gov/study/NCT00317642) | Phase 3 | 完成 | 326 | 雙盲：clofarabine + cytarabine vs cytarabine，用於 ≥55 歲復發／難治 AML |
| [NCT02085408](https://clinicaltrials.gov/study/NCT02085408) | Phase 3 | 完成 | 727 | 隨機：clofarabine 誘導與緩解後治療 vs 標準 daunorubicin + cytarabine，之後 decitabine 維持 vs 觀察，用於 ≥60 歲新診斷 AML |
| [NCT00703820](https://clinicaltrials.gov/study/NCT00703820) | Phase 3 | 完成 | 324 | AML08：clofarabine + cytarabine vs 傳統誘導治療，並評估 NK 細胞移植 |
| [NCT01101880](https://clinicaltrials.gov/study/NCT01101880) | Phase 2 | 完成 | 50 | Clofarabine + 高劑量 cytarabine + G-CSF 引導，用於 65 歲以下新診斷 AML |
| [NCT00778375](https://clinicaltrials.gov/study/NCT00778375) | Phase 2 | 完成 | 122 | Clofarabine + 低劑量 cytarabine，與 decitabine 交替鞏固，用於 ≥60 歲 AML／高風險 MDS |
| [NCT00088218](https://clinicaltrials.gov/study/NCT00088218) | Phase 2 | 完成 | 95 | 隨機：clofarabine 單用 vs 合併低劑量 cytarabine，用於 ≥60 歲未治療 AML／高風險 MDS |
| [NCT01295307](https://clinicaltrials.gov/study/NCT01295307) | Phase 2 | 完成 | 86 | Clofarabine 挽救治療復發／難治 AML |
| [NCT01457885](https://clinicaltrials.gov/study/NCT01457885) | Phase 2 | 完成 | 75 | Clofarabine + busulfan 清髓性移植，用於未緩解 AML |
| [NCT00469014](https://clinicaltrials.gov/study/NCT00469014) | Phase 2 | 完成 | 72 | 隨機：busulfan-fludarabine-clofarabine 移植，用於難治 AML／MDS／CML |
| [NCT00065143](https://clinicaltrials.gov/study/NCT00065143) | Phase 2 | 完成 | 60 | Clofarabine + cytarabine，用於 ≥50 歲新診斷 AML／高風險 MDS |

## 文獻證據

本預測共有 20 篇相關文獻，以下列出 10 篇（隨機試驗優先）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31246522](https://pubmed.ncbi.nlm.nih.gov/31246522/) | 2019 | RCT (Phase 3) | J Clin Oncol | AML08：兒童 AML 誘導治療中，clofarabine 可取代部分 daunorubicin 與 etoposide |
| [31905904](https://pubmed.ncbi.nlm.nih.gov/31905904/) | 2019 | 分析 | Cancers | Clofarabine 鞏固方案（CLARA）在微複雜核型的年輕 AML 病人改善無復發存活 |
| [32187883](https://pubmed.ncbi.nlm.nih.gov/32187883/) | 2020 | Cohort (Phase 2) | Cancer Med | Clofarabine + cytarabine + mitoxantrone 用於難治／復發 AML，反應率高，可有效銜接異體移植（香港團隊） |
| [36336258](https://pubmed.ncbi.nlm.nih.gov/36336258/) | 2023 | Cohort | Transplant Cell Ther | Clofarabine + busulfan 清髓性預處理，用於活動性骨髓性惡性腫瘤的異體移植 |
| [31637757](https://pubmed.ncbi.nlm.nih.gov/31637757/) | 2020 | Phase I/II | Am J Hematol | Clofarabine + 低劑量全身照射的非清髓性預處理，用於不適合強烈方案的 AML |
| [29773602](https://pubmed.ncbi.nlm.nih.gov/29773602/) | 2018 | Phase Ib | Haematologica | 以 clofarabine 取代 fludarabine，用於兒童復發／難治 AML，尋找建議 Phase 2 劑量 |
| [25457773](https://pubmed.ncbi.nlm.nih.gov/25457773/) | 2015 | Review | Crit Rev Oncol Hematol | 回顧 clofarabine 用於成人 AML 的單藥與各種合併策略 |
| [22957815](https://pubmed.ncbi.nlm.nih.gov/22957815/) | 2013 | Review | Leuk Lymphoma | 回顧 clofarabine 在 AML 的角色與作用機轉 |
| [18756533](https://pubmed.ncbi.nlm.nih.gov/18756533/) | 2008 | 臨床研究 | Cancer | Clofarabine 合併方案用於 AML 挽救治療，合併 cytarabine 可行且有效 |
| [31281098](https://pubmed.ncbi.nlm.nih.gov/31281098/) | 2019 | Review | Lancet Oncol | Clofarabine 與 cytarabine 用於 AML 的評論 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67620 | CLOFARABINE CONCENTRATE FOR SOLUTION FOR INFUSION 20MG/20ML（Chemill Pharma） | 未載明（輸注用濃縮液） | 許可證資料未載明 |
| HK-68623 | CLOFACORD CONCENTRATE FOR SOLUTION FOR INFUSION 20MG/20ML（Jacobson Marketing） | 未載明（輸注用濃縮液） | 許可證資料未載明 |
| HK-61183 | EVOLTRA CONCENTRATE FOR SOLUTION FOR INFUSION 1MG/ML（Sanofi Hong Kong） | 未載明（輸注用濃縮液） | 許可證資料未載明 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（嘌呤核苷類似物、抗代謝藥） |
| 骨髓抑制風險 | 高（用於白血病誘導與清髓性預處理，預期會有顯著血球低下與感染風險） |
| 致吐性分級 | 低至中度（依藥物類別判斷） |
| 監測項目 | CBC（含分類）、肝腎功能、電解質 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

以上為依藥物類別的判斷，資料包無 DrugBank 毒性資料，請以原廠仿單的警語與注意事項為準。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有 3 個已完成的 Phase 3 試驗（NCT00317642、NCT02085408、NCT00703820）和多個 Phase 2 研究支持用於骨髓性白血病，證據量充分。但資料包沒有這些試驗的療效結果，且相關 ALL 隨機試驗（CoALL 08-09、HOVON-100）未顯示存活改善。同時香港仿單的警語與禁忌資料缺漏，屬阻擋性缺口。

**若要推進需要：**
- 取得香港衛生署三張許可證的仿單，補齊核准適應症、警語與禁忌症（阻擋性缺口）
- 查證三個 Phase 3 試驗的主要終點與存活結果，確認 clofarabine 相對標準治療的實際獲益
- 補充 DrugBank 的作用機轉資料
- 建立骨髓抑制、感染與肝腎功能的監測計畫，並確認細胞毒性藥物的調配與處置流程
- 完成試驗與文獻的相關性評級（目前多數為待評），以確認證據等級

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

