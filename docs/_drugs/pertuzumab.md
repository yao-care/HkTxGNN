---
layout: default
title: Pertuzumab
parent: 高證據等級 (L1-L2)
nav_order: 670
evidence_level: L2
indication_count: 5
---

# Pertuzumab
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Pertuzumab：從 HER2 陽性乳癌到 PR 陽性乳癌

## 一句話總結

Pertuzumab 是抗 HER2 的單株抗體，已有上市用途為 HER2 陽性乳癌（原適應症欄位缺資料，此為依機轉推論，需與藥證核對）。
TxGNN 模型預測它可能對**黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer)** 有效，
目前有 **9 個臨床試驗**和 **20 篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉欄位，以下依本次分析的機轉推論說明。Pertuzumab 結合 HER2 的 subdomain II，阻斷 HER2-HER3 異二聚體形成，進而抑制 PI3K/AKT 與 MAPK 訊號，並可促進抗體依賴性細胞毒殺作用 (ADCC)。

PR 陽性乳癌是 HER2 陽性乳癌中的荷爾蒙受體陽性亞群，約一半的 HER2 過度表現乳癌同時帶有 ER 和/或 PR。Pertuzumab 的療效取決於 HER2 狀態，而不是 PR 狀態，所以這個預測在機轉上合理，本質上是已上市用途中的一個亞群。

證據等級定為 L2 的原因是：Phase 2 隨機試驗（NeoSphere、WSG-TP-II、PERTAIN、NEOADAPT）直接涵蓋 HR+/HER2+ 族群。Phase 3 試驗多為生物相似藥的等效性研究，針對一般 HER2 陽性族群，沒有單獨分析 PR 陽性族群。

## 臨床試驗證據

此預測共有 9 個臨床試驗，下表列出 7 個最相關者（略過撤回且 0 人收案、以及僅做 HER2-low 盛行率回溯的研究）。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00545688](https://clinicaltrials.gov/study/NCT00545688) | Phase 2 | 完成 | 417 | 四種 trastuzumab、docetaxel、pertuzumab 組合的術前療法比較（HER2 陽性乳癌，含 HR+ 與 HR- 分層） |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | 未知 | 7 | 芳香環轉化酶抑制劑 + pertuzumab/trastuzumab 術前免化療方案，針對 HR+/HER2+ 乳癌；收案數很少，權重低 |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | 進行中（不再招募） | 398 | 生物相似藥 BCD-178 對比 Perjeta 的術前雙盲 RCT；收案族群為 ER/PR 皆陰性，並非 PR 陽性 |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | 完成 | 517 | 生物相似藥 QL1209 對比 pertuzumab（併用 trastuzumab + docetaxel）的等效性試驗；族群為 HER2 陽性且 ER/PR 陰性 |
| [NCT02326974](https://clinicaltrials.gov/study/NCT02326974) | Phase 2 | 進行中（不再招募） | 164 | T-DM1 併用 pertuzumab 術前治療，探討 HER2 異質性對早期 HER2 陽性乳癌的影響 |
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | 進行中（不再招募） | 128 | TBCRC 023：lapatinib + trastuzumab 術前治療，比較加或不加內分泌治療；主要藥物非 pertuzumab |
| [NCT04675827](https://clinicaltrials.gov/study/NCT04675827) | Phase 2 | 提前終止 | 139 | DECRESCENDO：ER 陰性、淋巴結陰性族群，達 pCR 後降階輔助化療；荷爾蒙受體情境相反 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncology | WSG-TP-II：在 HR 陽性/HER2 陽性早期乳癌中，比較內分泌治療 + trastuzumab + pertuzumab 與降階化療 |
| [30106636](https://pubmed.ncbi.nlm.nih.gov/30106636/) | 2018 | 隨機 Phase 2 | J Clin Oncol | PERTAIN：HER2 陽性且 HR 陽性的轉移性/局部晚期乳癌，一線 trastuzumab + 芳香環轉化酶抑制劑，加或不加 pertuzumab |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT | Lancet Oncology | NeoSphere 5 年分析：術前 pertuzumab + trastuzumab 的無惡化存活、無病存活與安全性 |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Annals of Oncology | WSG-ADAPT HER2+/HR-：12 週 trastuzumab + pertuzumab 雙重阻斷，加或不加每週 paclitaxel 的降階策略 |
| [38906970](https://pubmed.ncbi.nlm.nih.gov/38906970/) | 2024 | RCT | British Journal of Cancer | QL1209（pertuzumab 生物相似藥）對比原廠藥的 Phase 3 等效性試驗，族群為 HER2 陽性、ER/PR 陰性 |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | 指引 | J Clin Oncol | ASCO 晚期 HER2 陽性乳癌全身性治療指引更新 |
| [40076535](https://pubmed.ncbi.nlm.nih.gov/40076535/) | 2025 | 系統性回顧 | Int J Mol Sci | Pertuzumab + trastuzumab + docetaxel 作為 HER2 陽性乳癌輔助雙藥療法的系統性回顧 |
| [27057657](https://pubmed.ncbi.nlm.nih.gov/27057657/) | 2016 | Review | Cancer Treat Rev | HR+/HER2+ 乳癌的現況與未來；ER/PR 與 HER2 下游訊號存在交互作用 |
| [40983817](https://pubmed.ncbi.nlm.nih.gov/40983817/) | 2025 | Review | Breast Cancer (Tokyo) | HR+/HER2+ 乳癌的內在訊號通路交互作用與臨床轉譯進展 |
| [40246081](https://pubmed.ncbi.nlm.nih.gov/40246081/) | 2025 | 回溯性研究 | Modern Pathology | 多中心回溯研究：荷爾蒙受體狀態與 HER2 表現對 HER2 陽性乳癌術前標靶治療反應的影響 |

## 香港上市資訊

香港共有 3 張許可證，劑型與核准適應症欄位目前無資料。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-62758 | PERJETA CONCENTRATE FOR SOLUTION FOR INFUSION 420MG | ROCHE HONG KONG LIMITED |
| HK-67118 | PHESGO SOLUTION FOR SUBCUTANEOUS INJECTION 1200MG/600MG IN 15ML | ROCHE HONG KONG LIMITED |
| HK-67119 | PHESGO SOLUTION FOR SUBCUTANEOUS INJECTION 600MG/600MG IN 10ML | ROCHE HONG KONG LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（HER2 單株抗體） |
| 骨髓抑制風險、致吐性分級、監測項目、處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
多個 Phase 2 隨機試驗（NeoSphere、WSG-TP-II、PERTAIN）直接涵蓋 HR+/HER2+ 族群，且 pertuzumab 已在香港上市。不過療效取決於 HER2 狀態而非 PR 狀態，Phase 3 試驗也未單獨分析 PR 陽性族群，因此只能有條件推進。

**若要推進需要：**
- 確認 HER2 陽性，這是使用的前提
- 內分泌治療合併或化療降階，僅限在試驗或指引範圍內使用
- 取得香港衛生署仿單的警語與禁忌症資料（目前為阻擋性缺口，無法進入安全性篩檢）
- 補齊作用機轉（DrugBank）與原適應症資料，並核對香港藥證的核准適應症
- 有一篇回溯性研究（PMID 37723497）提示 PR 狀態可能影響加入 pertuzumab 的效益，僅能視為假說，需前瞻性驗證

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

