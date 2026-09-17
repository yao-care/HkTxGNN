---
layout: default
title: Temozolomide
parent: 僅模型預測 (L5)
nav_order: 726
evidence_level: L5
indication_count: 2
---

# Temozolomide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Temozolomide：原適應症資料缺口 → 成人星形細胞瘤 (Adult Astrocytic Tumour)

## 一句話總結

> Temozolomide 目前在香港未上市，原適應症登記資料與作用機轉（MOA）皆為資料缺口。
> TxGNN 模型預測它對**成人星形細胞瘤 (Adult Astrocytic Tumour)** 有效，
> 文獻中已有多個完成的 **Phase 3 RCT**（如確立標準治療地位的 Stupp 2005 試驗）及共 **20 篇文獻**支持，證據強度高，但安全性資料仍待補齊。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（未提供，`original_indications` 為空） |
| 預測新適應症 | 成人星形細胞瘤 (Adult Astrocytic Tumour) |
| TxGNN 預測分數 | 99.36% |
| 證據等級 | L1（文獻含 ≥2 個已完成 Phase 3 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Temozolomide 詳細的作用機轉資料（DrugBank MOA 為資料缺口），香港本地也無許可證登記，因此無法從本地法規資料取得原適應症文字。

不過，從文獻證據可清楚看到：Temozolomide 已在國際間廣泛用於惡性膠質瘤（glioblastoma）與星形細胞瘤（astrocytoma）的治療，其中 Stupp 等人 2005 年發表於 *NEJM* 的 EORTC-NCIC 隨機三期試驗確立了「放療併用 Temozolomide」為新診斷膠質母細胞瘤的標準治療，後續 5 年追蹤（2009, *Lancet Oncology*）及多個三期試驗（CeTeG/NOA-09、NOA-08、EF-14 等）持續強化此地位。

這代表 TxGNN 預測的「成人星形細胞瘤」適應症，實質上與全球臨床實務高度一致，機轉上的合理性主要來自大量已完成的隨機對照試驗證據，而非單純理論推導。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00052455](https://clinicaltrials.gov/study/NCT00052455) | Phase 3 | 完成 | 500 | 比較 Temozolomide 單藥 vs. PCV 療法用於復發性 WHO Grade III/IV 星形細胞瘤 |
| [NCT00960492](https://clinicaltrials.gov/study/NCT00960492) | Phase 1 | 完成 | 26 | XL184 併用 Temozolomide 與放療於新診斷膠質母細胞瘤之劑量探索試驗 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15758009](https://pubmed.ncbi.nlm.nih.gov/15758009/) | 2005 | RCT (Phase 3) | N Engl J Med | 放療併用 Temozolomide 確立為新診斷膠質母細胞瘤標準治療（EORTC-NCIC 試驗） |
| [19269895](https://pubmed.ncbi.nlm.nih.gov/19269895/) | 2009 | RCT 追蹤 | Lancet Oncol | 同一 EORTC-NCIC 試驗 5 年存活率追蹤分析，確認長期效益 |
| [30782343](https://pubmed.ncbi.nlm.nih.gov/30782343/) | 2019 | RCT (Phase 3) | Lancet | CeTeG/NOA-09 試驗：Lomustine-Temozolomide 併用於 MGMT 甲基化膠質母細胞瘤 |
| [26670971](https://pubmed.ncbi.nlm.nih.gov/26670971/) | 2015 | RCT | JAMA | Tumor-Treating Fields 併用 Temozolomide vs. Temozolomide 單藥維持治療 |
| [24552317](https://pubmed.ncbi.nlm.nih.gov/24552317/) | 2014 | RCT | N Engl J Med | Bevacizumab 併用標準 Temozolomide 化療於新診斷膠質母細胞瘤 |
| [22578793](https://pubmed.ncbi.nlm.nih.gov/22578793/) | 2012 | RCT (Phase 3) | Lancet Oncol | NOA-08 試驗：老年惡性星形細胞瘤患者 Temozolomide 單藥 vs. 放療單獨治療 |
| [40779733](https://pubmed.ncbi.nlm.nih.gov/40779733/) | 2025 | RCT (Phase II/III) | J Clin Oncol | NRG BN007 試驗：MGMT 未甲基化膠質母細胞瘤雙重免疫檢查點阻斷合併治療 |
| [41345097](https://pubmed.ncbi.nlm.nih.gov/41345097/) | 2025 | RCT (Phase Ib/II) | Nat Commun | GEINO 1602 試驗：Glasdegib 併用 Temozolomide 與放療 |
| [36809318](https://pubmed.ncbi.nlm.nih.gov/36809318/) | 2023 | Review | JAMA | 成人原發性腦惡性腫瘤總論，涵蓋膠質母細胞瘤流行病學與治療現況 |
| [29075865](https://pubmed.ncbi.nlm.nih.gov/29075865/) | 2017 | Review | Curr Oncol Rep | 老年膠質母細胞瘤患者治療現況回顧 |

---

## 香港上市資訊

目前 Temozolomide 在香港**未上市**，無許可證登記資料（`total_licenses: 0`）。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Imidazotetrazine 類烷化劑） |
| 骨髓抑制風險 | 高（文獻廣泛記載嗜中性白血球減少、血小板減少，尤其延長給藥期間） |
| 致吐性分級 | 中度 |
| 監測項目 | 每週 CBC（含分類計數）、肝功能、腎功能 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

---

## 安全性考量

> 安全性資訊請參考原廠仿單。目前主要警語、禁忌症與藥物交互作用資料均為資料缺口（DG001，Blocking 等級），已阻擋進入 S1 安全性初評階段。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 文獻證據強度高（多個已完成 Phase 3 RCT，已是國際標準治療），機轉合理性充分。
- 但香港未上市、原適應症與 MOA 資料缺口，且安全性資料（仿單警語/禁忌症）為 **Blocking** 級缺口，無法完成 S1 安全性初評，故暫列 Hold。

**若要推進需要：**
- 取得原廠仿單 PDF 並解析警語與禁忌症（DG001）
- 查詢 DrugBank API 補齊完整 MOA 資料（DG002）
- 評估香港上市/許可證申請途徑
- 補充 DDI 資料庫查詢結果
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

