---
layout: default
title: Doxorubicin
parent: 高證據等級 (L1-L2)
nav_order: 293
evidence_level: L1
indication_count: 10
---

# Doxorubicin
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

# Doxorubicin：從（原適應症資料缺漏）到 Ewing 肉瘤

## 一句話總結

Doxorubicin（多柔比星）是一種蔥環類（anthracycline）抗腫瘤藥物，輸入資料中未列出其原適應症。
TxGNN 模型預測它可能對 **Ewing 肉瘤 (Ewing sarcoma)** 有效，
目前有 **40 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含多個已完成的 Phase 3 隨機對照試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未提供適應症文字 |
| 預測新適應症 | Ewing 肉瘤 (Ewing sarcoma) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據已知資訊，Doxorubicin 是 topoisomerase II 毒物與 DNA 嵌入劑，屬於蔥環類藥物，其抗腫瘤療效已在多種癌症中被證實。

Doxorubicin 是 Ewing 肉瘤多藥化療（如 VDC/IE 方案：vincristine、doxorubicin、cyclophosphamide 交替 ifosfamide、etoposide）的骨幹成分，共識指引與多個隨機試驗都支持這個用法。因此這比較像是**確認既有標準方案的成分**，而不是全新的老藥新用訊號。

**其他預測適應症的整體狀況**（僅供參考，證據強度皆低於 Ewing 肉瘤）：

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----------|-----------|---------|------|
| 橫紋肌肉瘤 | 99.70% | L2 | Research Question |
| 肺母細胞瘤 | 99.85% | L3 | Research Question |
| 原發性肺淋巴瘤 | 99.85% | L4 | Research Question |
| 神經節母細胞瘤 | 99.70% | L4 | Research Question |
| 慢性骨髓性白血病 (BCR-ABL1 陽性) | 99.77% | L4 | Hold |
| 單核球性白血病 | 99.74% | L4 | Hold |
| 副腦膜胚胎型橫紋肌肉瘤 | 99.71% | L4 | Hold |
| 陰道葡萄狀胚胎型橫紋肌肉瘤 | 99.72% | L4 | Hold |
| 高分化胎兒型肺腺癌 | 99.86% | L5 | Hold |

## 臨床試驗證據

以下列出與 Ewing 肉瘤最相關的 10 個試驗（共檢索到 40 個）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | 完成 | 278 | 非轉移性 Ewing 肉瘤化療劑量強化的隨機對照試驗（疾病專一、高度相關） |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | 完成 | 642 | 標準五藥方案（含 doxorubicin）加 vincristine-topotecan-cyclophosphamide，用於非轉移性 Ewing 肉瘤 |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | 完成 | 587 | 以間隔壓縮方式強化化療，用於 Ewing 肉瘤及相關腫瘤 |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | 進行中（不再招募） | 312 | 多藥化療（含 doxorubicin）加 ganitumab，用於新診斷轉移性 Ewing 肉瘤 |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | 未知 | 1200 | EURO-E.W.I.N.G.99，歐洲 Ewing 肉瘤多國隨機試驗 |
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | 未知 | 未提供 | EICESS 92，比較不同組合化療方案 |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | 進行中（不再招募） | 2 | VIrR 加 VDC/IE 對比標準 VDC/IE，用於新診斷轉移性 Ewing 肉瘤 |
| [NCT01946529](https://clinicaltrials.gov/study/NCT01946529) | Phase 2 | 完成 | 24 | Ewing 肉瘤家族腫瘤與促結締組織增生性小圓細胞腫瘤的治療方案 |
| [NCT00061893](https://clinicaltrials.gov/study/NCT00061893) | Phase 2 | 完成 | 38 | 標準多藥化療加低劑量抗血管新生治療，用於轉移性 Ewing 肉瘤家族腫瘤 |
| [NCT01313884](https://clinicaltrials.gov/study/NCT01313884) | Phase 2 | 提前終止 | 3 | 含 doxorubicin 方案交替 irinotecan/temozolomide；僅收 3 人，證據貢獻極小 |

**說明：** 上述 Phase 3 試驗多數在標準方案中使用 doxorubicin，但試驗設計比較的是整體方案或新增藥物，並非單獨檢驗 doxorubicin 的貢獻。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | 在標準化療上加入 ifosfamide 與 etoposide，用於新診斷 Ewing 肉瘤與骨原始神經外胚層腫瘤 |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (Phase 3) | Lancet | EE2012：比較歐洲與美國兩種標準化療策略 |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT (Phase 3) | J Clin Oncol | 間隔壓縮化療加 ganitumab，用於新診斷轉移性 Ewing 肉瘤（COG AEWS1221） |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | 局部性 Ewing 肉瘤以間隔壓縮強化化療（COG） |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT 試驗方案 | Trials | EURO EWING 2012 國際隨機試驗方案 |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | 共識指引 | Cancer | 美國國家 Ewing 肉瘤腫瘤委員會的治療共識建議 |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Ewing 肉瘤目前治療與國際合作的未來方向 |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | 局部性 Ewing 肉瘤存活率由約 10% 提升至約 75%，轉移性仍預後不佳 |
| [28710342](https://pubmed.ncbi.nlm.nih.gov/28710342/) | 2017 | 回顧性研究 | Oncologist | 成人 Ewing 肉瘤使用 vincristine、ifosfamide、doxorubicin（VID）的經驗 |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | 臨床研究（間接） | J Natl Cancer Inst | doxorubicin 劑量強度分析，涵蓋骨肉瘤與 Ewing 肉瘤 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52946 | DOXORUBICIN-TEVA INJ 2MG/ML | 未提供 | 未提供 |
| HK-68965 | DOXOCCORD LP CONCENTRATE FOR DISPERSION FOR INFUSION 50MG/25ML | 未提供 | 未提供 |
| HK-40874 | DOXORUBICIN-EBEWE INJ 10MG/5ML VIAL | 未提供 | 未提供 |
| HK-67505 | DOXORUBICIN HYDROCHLORIDE LIPOSOME CONCENTRATE FOR SOLUTION FOR INFUSION 20MG/10ML | 未提供 | 未提供 |
| HK-66647 | CAELYX CONCENTRATE FOR SOLUTION FOR INFUSION 20MG/10ML | 未提供 | 未提供 |

其中包含傳統劑型與微脂體（liposomal）劑型，共 7 張許可證，此處列出 5 張。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（蔥環類，topoisomerase II 抑制劑／DNA 嵌入劑） |
| 骨髓抑制風險 | 高（蔥環類的常見劑量限制毒性） |
| 致吐性分級 | 中至高（依劑量與併用藥物而異） |
| 監測項目 | CBC（含分類）、肝腎功能、心功能（累積劑量相關心毒性，如 LVEF、心肌旋轉蛋白） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

以上為依藥物類別的一般判斷，具體內容請以原廠仿單為準。本次資料中相關試驗（如 NCT01112800、NCT01095926）也顯示蔥環類心毒性是重要議題。

## 安全性考量

安全性資訊請參考原廠仿單。

（香港衛生署仿單的警語與禁忌資料在本次輸入中缺漏，藥物交互作用查詢也無結果。）

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Ewing 肉瘤已有多個已完成的 Phase 3 隨機試驗與國際共識指引，doxorubicin 是標準多藥方案的骨幹成分，證據等級為 L1。但這是對既有標準方案的確認，而非新發現；且試驗多是比較整體方案，無法單獨歸因 doxorubicin 的貢獻。另外，香港許可證的適應症文字與仿單警語資料皆缺漏，因此需要設置防護條件。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌症），補齊安全性資料，此為阻斷性缺口，未完成前無法進入安全性篩選
- 補齊香港許可證的核准適應症與劑型，確認是否已涵蓋 Ewing 肉瘤
- 取得 DrugBank 作用機轉資料
- 明確累積劑量與心毒性監測計畫
- 其他 9 個預測適應症：橫紋肌肉瘤（L2）可持續追蹤 NCT05457829 的結果；其餘證據薄弱，暫不建議推進

---
*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

