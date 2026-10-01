---
layout: default
title: Dacarbazine
parent: 僅模型預測 (L5)
nav_order: 237
evidence_level: L5
indication_count: 1
---

# Dacarbazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Dacarbazine：從烷化劑類抗腫瘤藥到上呼吸消化道腫瘤

## 一句話總結

Dacarbazine（DTIC）是一種甲基化烷化劑類抗腫瘤藥，在香港已有 3 張上市許可證。
TxGNN 模型預測它可能對**上呼吸消化道腫瘤 (Upper Aerodigestive Tract Neoplasm)** 有效。
目前僅有 **1 個間接的臨床試驗**（研究藥物為 temozolomide，並非 dacarbazine）。文獻中沒有直接證明 dacarbazine 對此適應症有效的研究，證據以模型預測為主。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 上呼吸消化道腫瘤 (Upper Aerodigestive Tract Neoplasm) |
| TxGNN 預測分數 | 99.26% |
| 證據等級 | L4（僅有同類藥物的間接研究與機轉推論） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，dacarbazine 是甲基化烷化劑，其活性代謝物 MTIC 與 temozolomide 釋出的活性物質相同。因此在 MGMT 修復能力低的腫瘤中，兩者機轉上可能有類似的抗腫瘤活性。

這是同類藥物層級的推論。本次收集到唯一的臨床訊號來自 temozolomide，並非 dacarbazine。我們沒有找到 dacarbazine 在上呼吸消化道腫瘤的專屬試驗或研究。

TxGNN 分數 (99.26%) 是知識圖譜的預測結果，不是臨床證據。此外，輸入資料中缺少原適應症與作用機轉，以上機轉說明是根據一般藥理知識推論的。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00423150](https://clinicaltrials.gov/study/NCT00423150) | Phase 2 | 提前終止 | 86 | 以 MGMT 啟動子甲基化篩選病人，評估 temozolomide 用於晚期上呼吸消化道癌（含大腸直腸癌、非小細胞肺癌、頭頸癌、食道癌）的療效與安全性。藥物為 temozolomide 而非 dacarbazine，屬間接證據，且提前終止限制了結果的可解讀性 |

## 文獻證據

以下文獻多數與 dacarbazine 用於此適應症無直接關係，僅供背景參考。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41481311](https://pubmed.ncbi.nlm.nih.gov/41481311/) | 2026 | RCT (Phase 3) | JAMA Oncology | 在肢端型晚期黑色素瘤中，比較 toripalimab 與 dacarbazine 作為第一線治療（dacarbazine 為對照組，適應症不同） |
| [23443801](https://pubmed.ncbi.nlm.nih.gov/23443801/) | 2013 | Phase 2 試驗 | Molecular Cancer Therapeutics | 即 NCT00423150 的發表文獻，探討 MGMT 啟動子甲基化能否預測晚期上呼吸消化道癌與大腸直腸癌病人對 temozolomide 的反應 |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | 臨床研究 | Annals of Oncology | 以 dacarbazine 合併 5-FU 治療晚期甲狀腺髓質癌（適應症不同） |
| [8346929](https://pubmed.ncbi.nlm.nih.gov/8346929/) | 1993 | Review | Gan to Kagaku Ryoho | 血管肉瘤的化療回顧，提到 CYVADIC 方案（含 DTIC）用於頭頸部血管肉瘤 |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Review | Clinical Oncology | 甲狀腺髓質癌的綜述（適應症不同） |
| [25772801](https://pubmed.ncbi.nlm.nih.gov/25772801/) | 2015 | Review | J Clin Neurosci | temozolomide 用於侵襲性腦下垂體腫瘤（適應症不同） |
| [12113649](https://pubmed.ncbi.nlm.nih.gov/12113649/) | 2002 | Review | Am J Clin Dermatol | 黑色素瘤的處置概念綜述 |
| [11163509](https://pubmed.ncbi.nlm.nih.gov/11163509/) | 2001 | Review | Int J Radiat Oncol Biol Phys | 嗅神經母細胞瘤的放射治療（非藥物研究） |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | 回溯性病例系列 | Ear Nose Throat J | 6 例頭頸部惡性副神經節瘤的臨床病理與治療選擇 |
| [20564093](https://pubmed.ncbi.nlm.nih.gov/20564093/) | 2010 | 回溯性研究 | Cancer | 頭頸部霍奇金淋巴瘤的特徵與預後（適應症不同） |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-44067 | DACARBAZINE FOR INJ 200MG | PFIZER CORPORATION HONG KONG LIMITED |
| HK-52120 | D.T.I FOR INJ 100MG | HEALTHCARE PHARMASCIENCE LIMITED |
| HK-52119 | D.T.I FOR INJ 200MG | HEALTHCARE PHARMASCIENCE LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（甲基化烷化劑） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

骨髓抑制風險、致吐性分級與監測項目，請參考原廠仿單的警語與注意事項。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有 TxGNN 預測分數和 temozolomide 的間接試驗（Phase 2、提前終止），沒有 dacarbazine 用於上呼吸消化道腫瘤的直接證據。
- 香港仿單的警語、禁忌與作用機轉資料也尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 從香港衛生署下載並解析仿單，補齊警語、禁忌症與核准適應症。
- 從 DrugBank 補齊 dacarbazine 的作用機轉（MOA）。
- 搜尋 dacarbazine 本身用於頭頸部、食道等上呼吸消化道腫瘤的臨床研究。
- 評估 MGMT 啟動子甲基化作為病人選擇生物標記的可行性，並釐清 temozolomide 的證據能否合理外推到 dacarbazine。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

