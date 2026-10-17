---
layout: default
title: Temozolomide
parent: 高證據等級 (L1-L2)
nav_order: 855
evidence_level: L1
indication_count: 2
last_modified_at: 2026-10-14
description: "Temozolomide：預測新適應症為成人星狀細胞腫瘤 (Adult Astrocytic Tumour)（證據等級 L1）。原適應症：退行性星狀細胞瘤、星狀細胞瘤（不含膠質母細胞瘤）、腦膠質母細胞瘤"
monitor_inn: "TEMOZOLOMIDE"
predicted_indications: ["adult astrocytic tumour", "cauda equina neoplasm"]
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Temozolomide：從惡性星狀細胞瘤到成人星狀細胞腫瘤

## 一句話總結

Temozolomide 是口服烷化劑，原本用於退行性星狀細胞瘤、星狀細胞瘤（不含膠質母細胞瘤）及腦膠質母細胞瘤的治療。
TxGNN 模型預測它可能對**成人星狀細胞腫瘤 (Adult Astrocytic Tumour)** 有效，目前有 **2 個臨床試驗**和 **20 篇文獻**支持這個方向。
需注意：此預測與原適應症高度重疊，屬於既有用途的再確認，並非真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 退行性星狀細胞瘤、星狀細胞瘤（不含膠質母細胞瘤）、腦膠質母細胞瘤（來自知識圖譜；香港許可證未列核准適應症文字） |
| 預測新適應症 | 成人星狀細胞腫瘤 (Adult Astrocytic Tumour) |
| TxGNN 預測分數 | 99.36% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 17 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏經正式資料庫確認的作用機轉資料。根據文獻整理，Temozolomide 是口服烷化劑，會使 DNA 甲基化（鳥嘌呤 O6 與 N7 位置、腺嘌呤 N3 位置），造成細胞毒性病變並誘發腫瘤細胞凋亡。藥效受 MGMT 啟動子甲基化狀態影響，該狀態是重要的預測生物標記。

成人星狀細胞腫瘤（含退行性星狀細胞瘤與膠質母細胞瘤）本來就是 Temozolomide 的核心適應症，因此機轉上直接適用。多項文獻也顯示，Temozolomide 合併放射治療是新診斷膠質母細胞瘤的標準治療。

換言之，這項預測是對既有用途的驗證，而非跨疾病的藥物再利用發現。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | 完成 | 500 | 比較 Temozolomide 與 PCV 方案用於復發性 WHO III–IV 級星狀細胞腫瘤，與適應症直接相關 |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | 完成 | 26 | XL184 (cabozantinib) 合併 Temozolomide 與放療用於膠質母細胞瘤的劑量探索，僅提供有限的安全性參考 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT | N Engl J Med | 放療合併同步及輔助 Temozolomide 用於膠質母細胞瘤，確立標準治療 |
| [29260225](https://pubmed.ncbi.nlm.nih.gov/29260225/) | 2017 | RCT | JAMA | 腫瘤電場治療加維持性 Temozolomide，對照單用 Temozolomide 的存活比較 |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | 維持期腫瘤電場治療加 Temozolomide 與單用 Temozolomide 比較 |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT | Lancet | Lomustine 加 Temozolomide 與標準 Temozolomide 用於 MGMT 甲基化的新診斷膠質母細胞瘤（Phase 3） |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | 在標準 Temozolomide 合併放療基礎上加 Bevacizumab，用於新診斷膠質母細胞瘤 |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT | Lancet Oncol | NOA-08：高齡惡性星狀細胞瘤患者，單用 Temozolomide 對比單用放療（Phase 3） |
| [39480453](https://pubmed.ncbi.nlm.nih.gov/39480453/) | 2024 | RCT | JAMA Oncol | Temozolomide 加 Veliparib 用於 MGMT 甲基化膠質母細胞瘤 |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | Meta-analysis | Lancet Oncol | EORTC-NCIC 試驗 5 年分析，確認 Temozolomide 合併放療的長期存活益處 |
| [34898238](https://pubmed.ncbi.nlm.nih.gov/34898238/) | 2022 | Guideline | J Clin Oncol | ASCO-SNO 成人瀰漫性星狀細胞及寡樹突膠質細胞腫瘤治療指引 |
| [17478095](https://pubmed.ncbi.nlm.nih.gov/17478095/) | 2007 | Review | Crit Rev Oncol Hematol | 成人退行性星狀細胞瘤綜述，指出化療對其預後改善有限 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53861 | TEMODAL CAP 5MG（默沙東） | 膠囊 | 資料未提供 |
| HK-53858 | TEMODAL CAP 20MG（默沙東） | 膠囊 | 資料未提供 |
| HK-53859 | TEMODAL CAP 100MG（默沙東） | 膠囊 | 資料未提供 |
| HK-53860 | TEMODAL CAP 250MG（默沙東） | 膠囊 | 資料未提供 |
| HK-65593 | TEMOL CAPSULES 100MG（Lotus） | 膠囊 | 資料未提供 |

香港共有 17 張有效的單方許可證，無已註銷者，此處僅列出 5 張主要許可證。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（烷化劑） |
| 骨髓抑制風險 | 中至高（知識圖譜列有嗜中性白血球減少、血小板減少、全血球減少、再生不良性貧血等禁忌關聯） |
| 致吐性分級 | 中度 |
| 監測項目 | CBC（含分類與血小板）、肝功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

更詳細的警語與注意事項請參考原廠仿單。

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**：肝衰竭、血小板低下、嗜中性白血球低下、顆粒球缺乏症、貧血（含大球性貧血）、肺囊蟲病、全血球低下、淋巴球低下、骨髓增生異常症候群、再生不良性貧血。這些來自知識圖譜的關聯，並非仿單原文。
- **藥物交互作用**：資料庫共記錄 100 筆。已列出者中，Naltrexone 為中度、Levofloxacin 為輕度，其餘（如 Pantoprazole、Omeprazole、Morphine、Metformin、Prednisone 等）嚴重度未知。

仿單的警語與禁忌症資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有已完成的 Phase 3 RCT（NCT00052455）以及多項高品質 RCT 與臨床指引支持其在成人星狀細胞腫瘤的療效，證據等級為 L1。
- 此適應症與原核准用途重疊，並非新發現；加上骨髓抑制風險明確，需在監測下使用。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 補充 DrugBank 的作用機轉資料
- 建立血液學監測計畫（CBC、肝功能）
- 若目標是真正的再利用，應轉向評估其他預測適應症，例如馬尾神經腫瘤（目前僅有 1 篇病例報告，屬 L4，為研究性問題，尚無臨床試驗支持）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

