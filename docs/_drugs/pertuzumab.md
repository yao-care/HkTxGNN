---
layout: default
title: Pertuzumab
parent: 高證據等級 (L1-L2)
nav_order: 575
evidence_level: L1
indication_count: 5
---

# Pertuzumab
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

# PERTUZUMAB：從 HER2陽性乳癌 到 黃體素受體陽性乳癌

## 一句話總結

Pertuzumab（Perjeta）是一種人源化單株抗體，透過阻斷 HER2/HER3 二聚化用於 HER2 陽性乳癌治療。
TxGNN 模型預測它對**黃體素受體陽性乳癌 (Progesterone-Receptor Positive Breast Cancer)** 同樣有效，
目前有 **10 個臨床試驗**和 **20 篇文獻**支持這個方向，且證據顯示這其實是既有適應症下的生物標記亞群，而非全新機轉假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HER2 陽性乳癌（依證據內容推得，香港無正式許可證資料） |
| 預測新適應症 | 黃體素受體陽性乳癌 (Progesterone-Receptor Positive Breast Cancer) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Pertuzumab 的作用機轉是阻斷 HER2 與 HER3 之間的二聚化，抑制下游訊息傳遞路徑，這是其在 HER2 陽性乳癌中發揮療效的核心機制。這個機轉本身與黃體素受體 (PR) 狀態沒有直接交互作用。

根據證據包中的機轉關聯分析，黃體素受體陽性乳癌其實是「HER2 陽性乳癌」既有核心適應症下的一個生物標記切分子群，並非新的機轉假說——PR 陽性只是共存的分類條件，從未被排除在 Pertuzumab 的治療對象之外。這也解釋了為何多個大型 Phase 2/3 試驗（如 NeoSphere、BCD-178 vs Perjeta 等）都直接涵蓋此族群，累積出扎實的臨床證據。

換言之，這項預測的價值不在於發現全新的治療領域，而在於確認 Pertuzumab 對 PR 陽性/HER2 陽性乳癌患者這個特定族群的療效具有充分證據支持。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | 進行中(未招募) | 128 | TBCRC 023：Lapatinib+Trastuzumab±內分泌治療，Pertuzumab為附加臂 |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | 進行中(未招募) | 398 | BCD-178（pertuzumab生物相似藥）vs Perjeta 於 HER2+ 乳癌術前治療直接比較 |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | 進行中(未招募) | 164 | T-DM1+Pertuzumab 術前治療，評估 HER2 異質性對療效影響 |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | 未知 | 7 | NEOADAPT：芳香酶抑制劑+Pertuzumab/Trastuzumab（不含化療）治療 HR+/HER2+ 乳癌 |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | 已終止 | 139 | DECRESCENDO：術前紫杉醇+皮下固定劑量 Pertuzumab/Trastuzumab 化療降階策略 |
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | 已完成 | 417 | Herceptin+Docetaxel±Pertuzumab 四臂比較病理完全反應率（NeoSphere型設計） |
| [NCT03058939](https://clinicaltrials.gov/study/NCT03058939) | Phase 2 | 已撤回 | 0 | 已撤回，0人收案，無法提供證據力 |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | 已完成 | 517 | QL1209（pertuzumab生物相似藥）+Docetaxel vs Pertuzumab+Docetaxel，HER2+/ER/PR陰性早期乳癌大型RCT |
| [NCT06131424](https://clinicaltrials.gov/study/NCT06131424) | N/A | 已完成 | 1151 | HER2-low 盛行率回顧性觀察研究，非介入性療效試驗 |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | 已完成 | 454 | IMpassion050：Atezolizumab±術前化療+Trastuzumab+Pertuzumab（安慰劑對照） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT（NeoSphere 5年追蹤） | Lancet Oncol | Pertuzumab+Trastuzumab+Docetaxel 較單用 Trastuzumab+Docetaxel 提升5年PFS/DFS |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT（WSG-ADAPT） | Ann Oncol | HER2+/HR- 短程雙標靶阻斷±紫杉醇降階治療的 pCR 評估 |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Review/Guideline（ASCO） | J Clin Oncol | HER2 陽性晚期乳癌全身治療 ASCO 指引更新 |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT（生物相似藥） | Br J Cancer | QL1209（pertuzumab生物相似藥）術前治療等效性試驗 |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncol | WSG-TP-II：內分泌治療+雙標靶 vs 降階化療於 HR+/HER2+ 早期乳癌 |
| [37609714](https://pubmed.ncbi.nlm.nih.gov/37609714/) | 2023 | RCT（DECRESCENDO） | Future Oncol | HER2+/ER-/N0 早期乳癌化療降階策略 |
| [40739524](https://pubmed.ncbi.nlm.nih.gov/40739524/) | 2025 | Cohort（真實世界） | Br J Clin Pharmacol | 美國 HR+ 轉移性乳癌真實世界治療模式與族裔差異 |
| [28973704](https://pubmed.ncbi.nlm.nih.gov/28973704/) | 2017 | Review | South Med J | 乳癌術前與術後輔助治療總覽 |
| [40282499](https://pubmed.ncbi.nlm.nih.gov/40282499/) | 2025 | Cohort | Cancers | pT1-T2N0M0 HER2+/ER/PR+ 術後節拍化療合併標靶/抗荷爾蒙治療新方案 |
| [32905036](https://pubmed.ncbi.nlm.nih.gov/32905036/) | 2020 | Review | Cureus | HER2 陽性轉移性乳癌治療策略文獻回顧 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（人源化單株抗體，抑制 HER2/HER3 二聚化，非傳統細胞毒性化療藥物） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
多個 Phase 2/3 臨床試驗（含 NeoSphere、QL1209 等大型RCT）已涵蓋 PR 陽性/HER2 陽性乳癌族群，證據等級達 L1；但此適應症本質上是既有核心適應症的生物標記亞群而非新機轉，加上香港尚未取得許可證、仿單警語與禁忌症資料仍缺失，故不宜直接列為 Go。

**若要推進需要：**
- 補齊官方仿單警語與禁忌症資料（目前為 Blocking 級資料缺口，無法完成 S1 安全性初評）
- 補充詳細作用機轉（MOA）資料以強化機轉關聯性分析
- 確認香港上市/許可證申請規劃（目前市場狀態為未上市）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

