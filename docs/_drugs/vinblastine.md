---
layout: default
title: Vinblastine
parent: 僅模型預測 (L5)
nav_order: 921
evidence_level: L5
indication_count: 10
---

# Vinblastine
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

# Vinblastine：從抗腫瘤化療藥到橫紋肌肉瘤

## 一句話總結

Vinblastine 是長春花生物鹼（vinca alkaloid）類的抗腫瘤注射藥，在香港已上市。
TxGNN 模型預測它可能對**橫紋肌肉瘤 (Rhabdomyosarcoma)** 有效。
目前**無臨床試驗**登記，僅有少量病例報告、前臨床與同類藥物（vincristine、vinorelbine）的間接文獻支持，屬於「研究假說」階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 橫紋肌肉瘤 (Rhabdomyosarcoma) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L4（僅有病例報告與前臨床／機轉研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的原廠作用機轉資料。就藥物類別而言，Vinblastine 是長春花生物鹼，會抑制微管聚合、使細胞停滯在有絲分裂期，對快速增生的腫瘤細胞有毒性。

橫紋肌肉瘤是增生快速的兒童與青少年軟組織肉瘤。同類藥物 vincristine 是標準橫紋肌肉瘤化療方案的骨幹，vinorelbine 在兒童肉瘤也有 Phase 2 與前導試驗的活性訊號。因此在機轉上，Vinblastine 可能適用。

但要注意，這個連結是**間接**的。針對 Vinblastine 本身的證據只有前臨床資料和少數合併療法的病例報告，無法分離出它單獨的貢獻。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22633624](https://pubmed.ncbi.nlm.nih.gov/22633624/) | 2012 | Phase 2 單臂試驗 | Eur J Cancer | 針對的是 vinorelbine（非 vinblastine）加低劑量 cyclophosphamide，用於復發或難治性兒童與年輕成人實體瘤。耐受性良好，在橫紋肌肉瘤顯示療效 |
| [41216926](https://pubmed.ncbi.nlm.nih.gov/41216926/) | 2026 | 世代研究 | Pediatr Blood Cancer | CWS-96 與 CWS-2002P 前瞻試驗，對象為局部性**非橫紋肌肉瘤**軟組織肉瘤，與本適應症僅間接相關 |
| [38050209](https://pubmed.ncbi.nlm.nih.gov/38050209/) | 2023 | 病例報告／回顧 | Medicine | 成人會陰橫紋肌肉瘤，使用 nivolumab、dacarbazine、cisplatin、vinblastine 後部分緩解 |
| [2451411](https://pubmed.ncbi.nlm.nih.gov/2451411/) | 1987 | 病例報告 | Hinyokika Kiyo | 兒童前列腺橫紋肌肉瘤，難治後改用 cisplatin、vinblastine、peplomycin 合併療法，骨盆腫塊快速縮小 |
| [15378498](https://pubmed.ncbi.nlm.nih.gov/15378498/) | 2004 | 前導試驗 | Cancer | 針對的是 vinorelbine（非 vinblastine）加低劑量 cyclophosphamide，用於歐洲橫紋肌肉瘤維持治療方案的劑量探索 |
| [12115359](https://pubmed.ncbi.nlm.nih.gov/12115359/) | 2002 | 臨床研究 | Cancer | 針對的是 vinorelbine，用於曾接受治療的晚期兒童肉瘤，在橫紋肌肉瘤顯示活性 |
| [3329524](https://pubmed.ncbi.nlm.nih.gov/3329524/) | 1987 | 前臨床 | Anticancer Drug Des | 以人類橫紋肌肉瘤異種移植小鼠模型，探討 vinca 生物鹼的治療選擇性 |
| [26024389](https://pubmed.ncbi.nlm.nih.gov/26024389/) | 2015 | 前臨床 | Cell Death Differ | PLK1 抑制劑與微管去穩定藥物在橫紋肌肉瘤模型中有合成致死協同作用 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51030 | VELBASTINE FOR INJ 10MG（HEALTHCARE PHARMASCIENCE LIMITED） | 未提供（注射劑） | 未提供 |
| HK-36337 | VINBLASTINE SULPHATE INJ 10MG IN 10ML（PFIZER CORPORATION HONG KONG LIMITED） | 未提供（注射劑） | 未提供 |

## 細胞毒性

以下依藥物類別（長春花生物鹼，傳統細胞毒性藥物）判斷，並非來自本次資料包的 toxicity 欄位，細節請以原廠仿單為準。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（抗微管藥物，Vinca alkaloid 類） |
| 骨髓抑制風險 | 高（白血球減少是常見的劑量限制毒性） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類）、肝功能、神經學症狀與腸胃道症狀（如便秘、腸阻塞） |
| 處置防護 | 需依細胞毒性藥物處置規範操作。僅限靜脈注射，注意外滲風險 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 橫紋肌肉瘤這個預測目前沒有臨床試驗。文獻多為病例報告、前臨床研究，或針對 vinorelbine 的間接證據，無法區分 Vinblastine 在合併療法中的貢獻。
- 香港仿單的警語與禁忌資料尚未取得（資料缺口 DG001，屬阻擋性），無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌與適應症文字。
- 補齊 Vinblastine 的作用機轉資料（可查詢 DrugBank）。
- 與 vincristine 或 vinorelbine 做系統性比較，確認 Vinblastine 的增益。
- 若要優先挑選方向，**神經母細胞瘤 (Neuroblastoma)** 是同批預測中證據最強的（L2）。它有 1 個已完成的 Phase 2 metronomic 試驗（NCT02641314，n=18）、1 個 Phase 1 vinblastine + sirolimus 兒童研究，以及前臨床協同資料，但仍無隨機對照，建議另行評估。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

