---
layout: default
title: Tizanidine
parent: 高證據等級 (L1-L2)
nav_order: 753
evidence_level: L2
indication_count: 5
---

# Tizanidine
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

# Tizanidine：從原適應症資料缺失到偏頭痛預防

## 一句話總結

> Tizanidine 是一種中樞性 alpha-2 腎上腺素受體致效劑，其原始核准適應症資料在本次 Evidence Pack 中缺失，香港目前也尚未上市。
> TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
> 目前有 **2 個臨床試驗**（含 1 個進行中的 Phase 3 RCT）和相關文獻支持這個方向，其中包含一篇已完成的小型雙盲安慰劑對照試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（Evidence Pack 未提供 `original_indications`，見 DG002） |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏正式的 MOA 資料庫欄位（`original_moa` 標記為缺口，DG002），但 Evidence Pack 的機轉關聯分析提供了關鍵線索：

Tizanidine 為中樞性 alpha-2 腎上腺素受體致效劑，與 clonidine 同屬一類。alpha-2 促效可抑制突觸前正腎上腺素釋放、降低交感輸出，並調節三叉神經血管系統的痛覺傳導——這正是 alpha-2 agonist 類藥物用於偏頭痛預防的既有理論基礎。

此外，Tizanidine 具有肌肉鬆弛作用，對於肌肉緊張相關的慢性每日頭痛（chronic daily headache）亦有理論加成效果。事實上，文獻中已有數篇針對 tizanidine 用於慢性每日頭痛預防的臨床研究（見下方文獻證據），顯示此藥理機轉在頭痛預防領域並非全新假說，而是有一定歷史基礎的研究方向。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05484349](https://clinicaltrials.gov/study/NCT05484349) | Phase 3 | 招募中 | 189 | 針對 18-65 歲成人偏頭痛患者（含有無先兆型），評估口服 Tizanidine 預防偏頭痛發作的療效、安全性與耐受性；多中心、隨機、雙盲、安慰劑對照。尚無結果數據。 |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | N/A | 已完成 | 300 | 24 週前瞻性觀察型研究，評估外用非類固醇消炎藥止痛效果的廣泛性鎮痛化合物研究，非專為 tizanidine-migraine 設計，相關性中等，需另行確認 tizanidine 是否為研究臂之一。 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12167135](https://pubmed.ncbi.nlm.nih.gov/12167135/) | 2002 | RCT | Headache | 雙盲、安慰劑對照、多中心研究，評估 tizanidine 作為慢性每日頭痛（含慢性偏頭痛、類偏頭痛、緊張型頭痛）輔助預防治療的療效。 |
| [11318882](https://pubmed.ncbi.nlm.nih.gov/11318882/) | 2001 | 開放性劑量滴定研究 | Headache | 評估 tizanidine 錠劑用於慢性每日頭痛預防的效果與安全性之開放性劑量滴定研究。 |
| [40983294](https://pubmed.ncbi.nlm.nih.gov/40983294/) | 2025 | 前臨床/劑型研究 | J Control Release | 透過超分子自組裝技術將 tizanidine 與 meloxicam 共結晶，設計出具協同抗偏頭痛效果的複合藥物。 |
| [11903539](https://pubmed.ncbi.nlm.nih.gov/11903539/) | 2002 | 臨床實務描述 | Headache | 描述以低劑量 tizanidine 併用 NSAID 進行止痛藥過度使用反彈性頭痛的門診戒斷治療方案。 |
| [12696998](https://pubmed.ncbi.nlm.nih.gov/12696998/) | 2003 | Review | CNS Drugs | 回顧 baclofen、tizanidine、botulinum toxin A 等作用於肌肉張力的藥物在偏頭痛與緊張型頭痛預防中的角色。 |
| [15115635](https://pubmed.ncbi.nlm.nih.gov/15115635/) | 2004 | Review | Curr Pain Headache Rep | 回顧偏頭痛預防新興治療選項，含 topiramate、tizanidine 等藥物。 |
| [17115988](https://pubmed.ncbi.nlm.nih.gov/17115988/) | 2006 | Review | Headache | 回顧慢性每日頭痛的預防性治療，提及 topiramate、gabapentin、tizanidine 等已研究藥物。 |
| [21770931](https://pubmed.ncbi.nlm.nih.gov/21770931/) | 2011 | Review | Headache | 探討聚焦於藥物過度使用與治療性預防的臨床試驗意涵，涵蓋 tizanidine 等預防性藥物。 |
| [23293866](https://pubmed.ncbi.nlm.nih.gov/23293866/) | 2013 | Review | Headache | 慢性偏頭痛管理之理性治療方法，提及 sodium valproate、gabapentin、tizanidine 等藥物。 |
| [20464578](https://pubmed.ncbi.nlm.nih.gov/20464578/) | 2010 | Review | Neurol Sci | 回顧雙盲安慰劑對照試驗中慢性偏頭痛的藥理預防性治療證據。 |

---

## 香港上市資訊

目前無許可證登記資料（`total_licenses = 0`，市場狀態：未上市）。

---

## 安全性考量

安全性資訊請參考原廠仿單。（`key_warnings`、`contraindications`、DDI 查詢結果目前皆為缺口，見 DG001，屬 Blocking 等級）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 個正在招募中的 Phase 3 RCT（NCT05484349）直接針對「口服 tizanidine 預防成人偏頭痛發作」設計，題目與適應症完全對應；
- 機轉理論基礎充分（alpha-2 agonist，與已核准用於相關領域的 clonidine 同類）；
- 已有一篇完成的小型雙盲安慰劑對照研究（PMID 12167135）顯示 tizanidine 用於慢性每日頭痛預防的正面訊號，加上多篇 Review 級文獻支持此藥物類別的預防性頭痛治療角色；
- 但目前尚無確認性大型試驗結果，且香港未上市、無許可證資料，安全性仿單資訊（DG001，Blocking）也仍缺失，須先補齊才能進入 S1 安全性初評。

**若要推進需要：**
- 補齊 TFDA/香港藥品仿單警語與禁忌症資料（DG001，Blocking，優先處理）
- 補齊完整作用機轉（MOA）正式資料（DG002）
- 追蹤 NCT05484349（預計 2025-12-25 完成）之三期試驗結果
- 若證據持續正向，規劃香港上市/許可證申請路徑
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

