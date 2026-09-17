---
layout: default
title: Uracil
parent: 僅模型預測 (L5)
nav_order: 781
evidence_level: L5
indication_count: 10
---

# Uracil
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

# Uracil：從代謝佐劑（UFT 複方成分）到大腸腫瘤（研究性預測）

## 一句話總結

Uracil（DrugBank DB03419）目前在香港**未上市**，也沒有獨立的核准適應症。TxGNN 模型預測它可能對**大腸腫瘤（Colonic Neoplasm）**有效，評分達 **99.50%**，並有 8 個臨床試驗與 20 篇文獻作為背景證據。但需特別注意：現有證據幾乎全部來自 **UFT 複方（tegafur + uracil）**，而非 uracil 這個分子獨立產生的抗腫瘤效果。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無（Uracil 未單獨上市，無核准適應症） |
| 預測新適應症 | 大腸腫瘤 (Colonic Neoplasm) |
| TxGNN 預測分數 | 99.50% |
| 證據等級 | L1（見下方「證據歸因警示」） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

**⚠️ 證據歸因警示**：Uracil 本身缺乏獨立的作用機轉（MOA）記錄，也從未以單方藥物形式上市。所有支持本項預測的臨床試驗與文獻，實際上研究的是 **UFT 複方（tegafur-uracil）**——uracil 在其中扮演的角色是競爭性抑制 dihydropyrimidine dehydrogenase（DPD），減緩 tegafur 代謝生成的 5-FU 被分解，藉此提高血中 5-FU 濃度與生體可用率。這是「代謝增效佐劑」機轉，而非 uracil 自身具有獨立抗腫瘤活性。

換言之，本評估報告呈現的證據強度（L1）反映的是 **UFT 複方 vs. 5-FU/LV 單方**在大腸癌輔助化療領域的紮實 RCT 證據基礎，而非「uracil 這個分子」的老藥新用訊號。這是知識圖譜方法在拆解複方成分時常見的歸因難題：TxGNN 學習到的是 uracil 節點與 fluoropyrimidine 代謝路徑的關聯，但無法區分「主成分」與「增效佐劑」的角色差異。

若要以此訊號推進，正確的臨床標的應是 **UFT (tegafur-uracil) 複方**，而非 uracil 單一成分。

## 臨床試驗證據

以下為與大腸腫瘤相關度較高的試驗（含直接使用 UFT 者優先列出）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01225744](https://clinicaltrials.gov/study/NCT01225744) | Phase 2 | 完成 | 47 | Cetuximab+Irinotecan+Oxaliplatin+**UFT** 併用治療轉移性大腸癌一線治療（明確使用 UFT） |
| [NCT00217737](https://clinicaltrials.gov/study/NCT00217737) | Phase 3 | 進行中未招募 | 2431 | FOLFOX ± Bevacizumab 用於高復發風險 stage II 大腸癌（5-FU 骨幹，非 UFT 特異） |
| [NCT02893540](https://clinicaltrials.gov/study/NCT02893540) | Phase 2/3 | 未知 | 250 | Capecitabine 節律性化療 vs. 傳統化療維持治療轉移性大腸癌 |
| [NCT00425152](https://clinicaltrials.gov/study/NCT00425152) | Phase 3 | 完成 | 2151 | 5-FU+Leucovorin+Levamisole 三種組合比較，Dukes B/C 大腸癌術後輔助治療 |
| [NCT05236972](https://clinicaltrials.gov/study/NCT05236972) | Phase 3 | 招募中 | 323 | Sintilimab (PD-1) vs. XELOX 標準治療，dMMR/MSI-H stage III 大腸癌 |
| [NCT00182715](https://clinicaltrials.gov/study/NCT00182715) | Phase 3 | 未知 | 2421 | Cetuximab 三臂試驗比較連續/間歇化療於轉移性大腸癌一線治療 |
| [NCT06997497](https://clinicaltrials.gov/study/NCT06997497) | Phase 3 | 招募中 | 477 | MK-1084+Cetuximab+mFOLFOX6 vs. mFOLFOX6±Bev，KRAS G12C 突變轉移性大腸癌 |
| [NCT05239741](https://clinicaltrials.gov/study/NCT05239741) | Phase 3 | 招募中 | 100 | Pembrolizumab vs. 標準化療，中國 MSI-H/dMMR stage IV 大腸癌患者 |
| [NCT04034459](https://clinicaltrials.gov/study/NCT04034459) | Phase 2 | 未知 | 109 | FOLFOXIRI+Cetuximab vs. FOLFOXIRI+Bevacizumab，BRAF 突變轉移性大腸癌一線治療 |
| [NCT00646607](https://clinicaltrials.gov/study/NCT00646607) | Phase 3 | 完成 | 3756 | FOLFOX-4 療程長度（3 vs 6 個月）+ Bevacizumab 輔助治療 stage II/III 大腸癌 |

**注意**：上列僅 NCT01225744 明確以 UFT 作為介入藥物，其餘試驗骨幹多為 5-FU、Capecitabine 或 Oxaliplatin 方案，uracil/UFT 並非核心介入成分。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | RCT | J Clin Oncol | NSABP C-06：口服 UFT+LV 與靜脈 5-FU+LV 在 stage II/III 大腸癌療效相當 |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT | ESMO Open | ACTS-CC 02 五年追蹤：S-1+Oxaliplatin 未優於 UFT/LV 輔助化療（高風險 stage III） |
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02 原始 Phase 3：SOX vs. UFT/LV 術後輔助化療優越性試驗 |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | RCT | Medicine | 台灣全國健保資料庫世代研究：UFT vs. 5-FU 術後輔助化療於 stage II/III 大腸癌 |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | 前瞻性對照試驗 | Int J Clin Oncol | JFMC46-1201 最終分析：UFT/LV 輔助治療高復發風險 stage II 大腸癌 |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | 前瞻性觀察研究 | BMC Cancer | JFMC46-1201 初步報告：UFT/LV 用於高風險 stage II 大腸癌之效果評估 |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surgery Today | UFT（tegafur+uracil）輔助化療於肺、胃、大腸直腸、乳癌的臨床證據與機轉綜述 |
| [26722024](https://pubmed.ncbi.nlm.nih.gov/26722024/) | 2016 | Review | Anticancer Res | 口服氟嘧啶類藥物綜述，涵蓋 UFT 抑制 DPD 增強 5-FU 療效的機轉 |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | OK-432 免疫化療 + HCFU/UFT 組合輔助治療大腸直腸癌隨機對照試驗 |
| [11320674](https://pubmed.ncbi.nlm.nih.gov/11320674/) | 2001 | 個案報告 | Cancer Chemother Pharmacol | UFT 誘發溶血性貧血個案報告（轉移性大腸癌患者） |

## 香港上市資訊

Uracil 目前在香港**未上市**，無任何許可證登記（`total_licenses = 0`）。若欲評估相關藥物的香港上市狀態，應改查詢 **UFT (tegafur-uracil) 複方製劑**或其品牌名稱（如愛斯萬類產品）的登記資訊。

## 安全性考量

Uracil 單一成分無仿單可查（未上市），且原始 Evidence Pack 中主要警語、禁忌症、DDI 查詢均為 `[Data Gap]` / `not_found`。

> 安全性資訊請參考 **UFT (tegafur-uracil) 複方產品**之原廠仿單。文獻中曾有 UFT 相關溶血性貧血個案報告（PMID 11320674），提示併用化療時需留意血液學毒性。

## 結論與下一步

**決策：Hold**

**理由：**
- 現有 L1 等級證據實質上是 **UFT 複方**（tegafur-uracil）vs. 5-FU/LV 骨幹方案的 Phase 3 RCT 證據，並非 uracil 分子本身獨立產生的抗腫瘤訊號，存在複方成分歸因混淆問題。
- Uracil 無獨立 MOA 記錄（DG002，High severity）、無 TFDA/香港仿單警語與禁忌資料（DG001，**Blocking severity**），無法通過 S1 安全性初評。
- Uracil 在香港未上市，無許可證可供銜接既有法規路徑。

**若要推進需要：**
- **釐清評估標的**：建議將老藥新用評估對象由「Uracil 單一成分」改為「**UFT (tegafur-uracil) 複方**」，因為所有實質療效證據均針對複方而非 uracil 單獨使用。
- 補充 DrugBank API 查詢結果，取得 uracil 完整 MOA 資料（DG002 remediation）。
- 若確定推進複方評估，需下載並解析 TFDA/香港仿單 PDF，取得警語與禁忌症資料以解除 S1 安全性初評的 Blocking 缺口（DG001 remediation）。
- 針對 NCT01225744（唯一明確使用 UFT 的試驗）與 UFT 相關文獻（PMID 16648506、31917122、33714860 等）進行更深入的複方層級證據整合。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

