---
layout: default
title: Docetaxel
parent: 高證據等級 (L1-L2)
nav_order: 283
evidence_level: L1
indication_count: 10
---

# Docetaxel
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

# Docetaxel：預測新適應症為女性乳癌

## 一句話總結

Docetaxel（多西他賽）是 Taxane 類細胞毒性化療藥物，香港已有 20 張許可證。
TxGNN 模型預測它對**女性乳癌 (Female Breast Carcinoma)** 有效，目前有 **40 個臨床試驗**和 **20 篇文獻**支持，其中包含多個已完成的 Phase 3 試驗。
乳癌其實是 docetaxel 早已確立的用途，因此本預測較接近既有用途的確認，而非真正的老藥新用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前 DrugBank 缺乏詳細的作用機轉（MOA）資料。不過 docetaxel 的藥理機轉已相當明確：它穩定微管，使快速分裂的腫瘤細胞停滯在 G2/M 期並走向凋亡。

乳癌細胞增殖活躍，對微管標靶的細胞毒性藥物敏感，這個機轉在乳癌中已有長期臨床實證。因此 TxGNN 給出高分並不意外。

需要留意的是，資料庫中沒有記錄原適應症，香港許可證的核准適應症欄位也是空白。我們無法從本次資料直接確認香港仿單是否載明乳癌適應症。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | 完成 | 2411 | 比較術前 AC 加或不加 docetaxel（術前或術後）用於可手術乳癌 |
| [NCT00054587](https://clinicaltrials.gov/study/NCT00054587) | Phase 3 | 完成 | 3010 | Docetaxel + epirubicin 對比 FEC100，用於淋巴結陽性乳癌，HER2 陽性者序貫加 trastuzumab |
| [NCT00615602](https://clinicaltrials.gov/study/NCT00615602) | Phase 3 | 完成 | 489 | FE75C 後接劑量密集 docetaxel，比較 trastuzumab 6 個月與 12 個月 |
| [NCT00129935](https://clinicaltrials.gov/study/NCT00129935) | Phase 3 | 完成 | 1384 | EC→T 對比 ET→X，用於淋巴結陽性、HER2 陰性乳癌的輔助治療 |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | 完成 | 478 | 劑量密集 FE75C 後接 docetaxel 或 paclitaxel，用於淋巴結陽性乳癌 |
| [NCT01547741](https://clinicaltrials.gov/study/NCT01547741) | Phase 3 | 狀態未知 | 1871 | Docetaxel + cyclophosphamide 對比含 anthracycline 方案，用於 HER2 陰性乳癌 |
| [NCT00015938](https://clinicaltrials.gov/study/NCT00015938) | Phase 2 | 完成 | 95 | Docetaxel + vinorelbine + filgrastim，用於 HER2 陰性第四期乳癌 |
| [NCT01208480](https://clinicaltrials.gov/study/NCT01208480) | Phase 2 | 完成 | 45 | Bevacizumab + docetaxel + carboplatin 術前治療三陰性乳癌 |
| [NCT01352494](https://clinicaltrials.gov/study/NCT01352494) | Phase 2 | 狀態未知 | 99 | Docetaxel + gemcitabine 用於局部晚期乳癌的術前治療 |
| [NCT02897050](https://clinicaltrials.gov/study/NCT02897050) | Phase 2 | 暫停 | 170 | 術前 docetaxel ± 節拍式 capecitabine/cyclophosphamide，後接 FEC，用於三陰性乳癌 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | ABC 系列試驗：比較 TC（docetaxel + cyclophosphamide）6 週期與含 taxane 的 AC 方案，用於早期乳癌輔助治療 |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | 隨機 Phase IIb | J Clin Oncol | 術前劑量密集 doxorubicin + docetaxel，比較加不加 tamoxifen 對病理反應的影響 |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Phase 2 | Breast Cancer | Docetaxel + cyclophosphamide + trastuzumab 用於 HER2 陽性乳癌的術前治療 |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 2 | Cancer | Capecitabine 併用 docetaxel 與 epirubicin，用於未治療的晚期乳癌 |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase 2 | Oncology | 每週 docetaxel + gemcitabine 用於轉移性乳癌第一線治療 |
| [15585076](https://pubmed.ncbi.nlm.nih.gov/15585076/) | 2004 | Phase 2 | Clin Breast Cancer | Docetaxel + cisplatin 用於局部晚期乳癌的術前治療 |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase 1/2 劑量探索 | Tumori | Docetaxel + gemcitabine 用於曾接受 anthracycline 治療的轉移性乳癌 |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | 世代研究 | Anti-Cancer Drugs | 回溯性分析輔助 docetaxel 化療與乳癌相關淋巴水腫的關聯 |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review | J Clin Oncol | Docetaxel 的臨床前與臨床特性回顧 |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | 回顧 paclitaxel 與 docetaxel 在乳癌與卵巢癌的角色 |

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-41354 | TAXOTERE CONC FOR INF. 80MG/2ML (VIAL) | SANOFI HONG KONG LIMITED |
| HK-64612 | ACCORD DOCETAXEL CONCENTRATE FOR SOLUTION FOR INFUSION 80MG/4ML | I & C (HONG KONG) LIMITED |
| HK-64613 | ACCORD DOCETAXEL CONCENTRATE FOR SOLUTION FOR INFUSION 20MG/1ML | I & C (HONG KONG) LIMITED |
| HK-65779 | DOCETAXEL CONCENTRATE FOR SOLUTION FOR INFUSION 20MG/1ML | SINO PACIFIC PHARMA COMPANY LIMITED |
| HK-65780 | DOCETAXEL CONCENTRATE FOR SOLUTION FOR INFUSION 80MG/4ML | SINO PACIFIC PHARMA COMPANY LIMITED |

## 細胞毒性

以下內容依藥物類別（Taxane 類）判斷，並非來自本次 Evidence Pack 的 toxicity 資料，實際請以原廠仿單為準。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Taxane 類、微管穩定劑） |
| 骨髓抑制風險 | 高（嗜中性白血球減少為常見劑量限制毒性） |
| 致吐性分級 | 低 |
| 監測項目 | CBC（含分類）、肝功能、體液滯留與周邊水腫 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。

香港衛生署仿單的警語與禁忌尚未取得，藥物交互作用查詢也無結果。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個完成的 Phase 3 試驗（總人數逾數千人）直接以 docetaxel 方案治療乳癌，證據等級為 L1。
- 這是既有用途的確認，而非新發現。安全性資料（DG001，阻斷級缺口）尚未補齊，因此需附帶防護條件。

**若要推進需要：**
- 取得香港衛生署仿單，確認乳癌適應症、警語與禁忌
- 補充 DrugBank 作用機轉資料（DG002）
- 確認各許可證的核准適應症與劑型
- 建立血液學毒性與體液滯留的監測計畫

**其他預測適應症：**
Ewing 肉瘤（L2）與橫紋肌肉瘤（L3）僅有研究層級的證據，其餘預測多為 L4-L5，建議暫緩（Hold）。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

