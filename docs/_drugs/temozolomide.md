---
layout: default
title: Temozolomide
parent: 高證據等級 (L1-L2)
nav_order: 840
evidence_level: L1
indication_count: 2
---

# Temozolomide
{: .fs-9 }

證據等級: **L1** | 預測適應症: **2** 個
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

# Temozolomide：從香港許可證未登載適應症到成人星狀細胞瘤

## 一句話總結

Temozolomide 是口服烷化劑化療藥，香港共有 17 張許可證，但資料中未登載原核准適應症。
TxGNN 模型預測它可能對**成人星狀細胞瘤 (Adult Astrocytic Tumour)** 有效，
目前有 **2 個臨床試驗**和 **20 篇文獻**支持，其中包含多項 Phase 3 RCT。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 成人星狀細胞瘤 (Adult Astrocytic Tumour) |
| TxGNN 預測分數 | 99.36% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 17 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前資料庫缺乏詳細的作用機轉欄位，但從預測推論可知：Temozolomide 是口服烷化劑，會使 DNA 甲基化（主要在 O6-鳥嘌呤），造成細胞毒性病灶並誘導腫瘤細胞凋亡。其療效會受 MGMT 啟動子甲基化狀態影響。

星狀細胞瘤包含膠質母細胞瘤（WHO 第 4 級星狀細胞瘤）與間變性星狀細胞瘤，都是 Temozolomide 的核心治療對象。這與 99.36% 的高預測分數一致，也有隨機對照試驗（RCT）支持。

需要注意：許可證資料中沒有原適應症，因此這個適應症可能是已核准的標準用途，而不是真正的「老藥新用」。實際在香港是否屬於標示內使用，需要另行確認。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | 完成 | 500 | Temozolomide 與 PCV（procarbazine、lomustine、vincristine）直接比較，用於復發性 WHO 3/4 級星狀細胞瘤 |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | 完成 | 26 | XL184 (cabozantinib) 合併 Temozolomide 與放射治療，用於初診膠質母細胞瘤的劑量探索與藥動學；Temozolomide 為背景治療，僅提供合併用藥的安全性參考 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | 比較單純放療與放療合併同步及輔助 Temozolomide 治療膠質母細胞瘤的療效與安全性 |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT | Lancet Oncol | EORTC-NCIC Phase 3 試驗的 5 年以上長期追蹤與最終存活分析 |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncol | NOA-08 Phase 3：高齡間變性星狀細胞瘤或膠質母細胞瘤患者，劑量密集 Temozolomide 單用對比單純放療 |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | 在標準 Temozolomide 加放療的基礎上，評估加入 bevacizumab 是否改善初診膠質母細胞瘤存活 |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | 維持治療階段，腫瘤治療電場 (TTFields) 合併 Temozolomide 對比單用 Temozolomide |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | CeTeG/NOA-09 Phase 3：MGMT 甲基化膠質母細胞瘤，lomustine 加 Temozolomide 對比標準 Temozolomide |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT | J Clin Oncol | NRG BN007 Phase II/III：MGMT 未甲基化初診膠質母細胞瘤的雙重免疫檢查點阻斷 |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | 成人膠質母細胞瘤與其他原發性惡性腦腫瘤的綜述 |
| [25920709](https://pubmed.ncbi.nlm.nih.gov/25920709/) | 2015 | Review | J Neurooncol | 放療合併 Temozolomide 用於間變性星狀細胞瘤與間變性寡星狀細胞瘤的探索性世代 |
| [41345097](https://pubmed.ncbi.nlm.nih.gov/41345097/) | 2025 | Phase Ib/II | Nat Commun | Glasdegib 合併 Temozolomide 與放療用於初診膠質母細胞瘤的安全性與療效（GEINO 1602） |

## 香港上市資訊

香港共有 17 張含 Temozolomide 的許可證，以下列出 5 張。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53861 | TEMODAL CAP 5MG | — | 資料未登載 |
| HK-65593 | TEMOL CAPSULES 100MG | — | 資料未登載 |
| HK-65823 | ZOLOTEM-5 CAPSULES 5MG | — | 資料未登載 |
| HK-62467 | TEMOZOLOMIDE CAPSULES 100MG | — | 資料未登載 |
| HK-68590 | JECETEMOZ CAPSULES 100MG | — | 資料未登載 |

## 細胞毒性

以下依藥物類別判斷，資料庫本身沒有 toxicity 欄位，詳細內容請以原廠仿單為準。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（烷化劑，imidazotetrazine 類） |
| 骨髓抑制風險 | 中至高（可能出現嗜中性白血球減少與血小板減少） |
| 致吐性分級 | 中度 |
| 監測項目 | CBC（含分類與血小板）、肝功能、腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有已完成的 Phase 3 試驗，以及多項 Phase 3 RCT 文獻（如 EORTC-NCIC、NOA-08、CeTeG/NOA-09）支持 Temozolomide 用於星狀細胞瘤，證據等級為 L1。
但原適應症與作用機轉資料缺漏，安全性資料也未取得，需先確認這是否已是標示內用途。

**若要推進需要：**
- 取得香港衛生署的仿單，確認核准適應症、警語與禁忌
- 確認該適應症在香港是否屬標示內使用，而非真正的新適應症
- 補充 DrugBank 的作用機轉資料
- 納入 MGMT 狀態檢測，作為使用建議的前提
- 膠質母細胞瘤證據較多，推及低級別星狀細胞瘤時，應以復發性或間變性星狀細胞瘤的分級別試驗為依據

**附註：** 第二個預測適應症「馬尾神經腫瘤 (Cauda Equina Neoplasm)」分數為 99.30%，但證據僅有 1 篇脊髓黏液乳突型室管膜瘤的個案報告，另一篇檢索文獻與此適應症無關。目前僅屬研究問題（L4），不建議據此推進。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

