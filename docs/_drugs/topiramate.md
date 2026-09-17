---
layout: default
title: Topiramate
parent: 僅模型預測 (L5)
nav_order: 758
evidence_level: L5
indication_count: 5
---

# Topiramate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Topiramate：從癲癇治療到反射性癲癇亞型的老藥新用評估

> 本評估包含 TxGNN 對 topiramate 預測的 **5 個候選適應症**，證據強度差異極大，故以總覽表統整全部候選，再針對有實質證據支持的項目展開細節。

## 一句話總結

Topiramate 是廣效型抗癲癇藥物（依文獻脈絡為癲癇／偏頭痛預防用藥，正式登記適應症資料缺失，香港目前**未上市**）。TxGNN 模型針對 5 個候選適應症評分皆逾 99%，但證據強度落差極大：**視覺型癲癇 (Visual Epilepsy)** 有 4 個臨床試驗與 20 篇文獻支持，是唯一達到 L2 證據等級的候選；其餘 4 項（三叉神經腫瘤、排尿誘發癲癇、聽覺誘發癲癇、驚愕型癲癇）證據薄弱，多屬動物模型推論或純模型預測。

## 快速總覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議決策 |
|------|-----------|-----------|---------|---------|---------|
| 1 | 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) | 99.70% | L5 | S0 | Hold |
| 2 | 視覺型癲癇 (Visual Epilepsy) | 99.28% | L2 | S2 | Proceed with Guardrails |
| 3 | 排尿誘發癲癇 (Micturition-induced Seizures) | 99.21% | L4 | S1 | Research Question |
| 4 | 聽覺誘發癲癇 (Audiogenic Seizures) | 99.21% | L4 | S1 | Research Question |
| 5 | 驚愕型癲癇 (Startle Epilepsy) | 99.21% | L5 | S0 | Hold |

| 項目 | 內容 |
|------|------|
| 原適應症 | 癲癇（依大量文獻脈絡推斷；正式登記適應症文字缺失） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 整體建議 | 僅視覺型癲癇候選可 Proceed with Guardrails，其餘 Hold 或列為 Research Question |

---

## 為什麼這個預測合理？

Topiramate 是結構特殊的胺磺酸取代單醣衍生物，機轉上具多重作用：鈉／鈣離子通道調節、GABA-A 受體增強，以及 AMPA/kainate 受體拮抗。這些機轉使其成為廣效型抗癲癇藥，已廣泛用於局部型、全身型癲癇及 Lennox-Gastaut 症候群。

排名 2-4 的候選（視覺型癲癇、排尿誘發癲癇、聽覺誘發癲癇）皆屬於**反射性癲癇 (reflex epilepsy)** 亞型——由特定刺激（光敏感、排尿、聲音）誘發的癲癇發作。Topiramate 的廣效抗癲癇機轉在理論上可延伸至此類亞型，其中聽覺誘發癲癇已有動物模型（GAERS、DBA/2 小鼠）直接驗證抗痙攣效果，機轉關聯性相對明確；視覺型癲癇與排尿誘發癲癇則缺乏亞型專一試驗，證據多為從廣泛性癲癇族群外推。

排名 1（三叉神經腫瘤）與排名 5（驚愕型癲癇）則**缺乏可辨識的機轉關聯**：前者與抗癲癇藥物的已知病理生理機轉無連結，後者雖同屬反射性癲癇但完全沒有支持文獻，兩者皆疑似 TxGNN 模型的高分偽陽性，僅供研究假設參考，不建議進一步投入資源。

---

## 臨床試驗證據

**僅視覺型癲癇候選有相關臨床試驗登記；其餘 4 項候選目前無相關臨床試驗登記。**

### 視覺型癲癇 (Visual Epilepsy)

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00231556](https://clinicaltrials.gov/study/NCT00231556) | Phase 3 | 完成 | 750 | Topiramate 兩種劑量單一療法治療新診斷/復發癲癇之安全性與療效比較，直接 RCT 證據，惟非視覺型癲癇專一設計 |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | 完成 | 111 | LICEO 前瞻觀察性研究，評估新型 AED（含 topiramate）作為一線雙藥合併治療之真實世界療效 |
| [NCT00231556](https://clinicaltrials.gov/study/NCT00231556) 之外，另有 [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | 未知 | 40 | 評估 levetiracetam（非 topiramate）於新生兒癲癇療效，僅間接佐證治療框架 |
| [NCT03803046](https://clinicaltrials.gov/study/NCT03803046) | N/A | 終止 | 1 | 兒童局部型癲癇術後 benzodiazepine 停藥認知影響，非 topiramate 專一，證據力極低 |

---

## 文獻證據

### 視覺型癲癇 (Visual Epilepsy) — L2

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17382828](https://pubmed.ncbi.nlm.nih.gov/17382828/) | 2007 | RCT (Tier 1) | Lancet | SANAD 研究：topiramate 於全身性/未分類癲癇之長期療效比較 |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | SR/網絡統合分析 (Tier 1) | J Neurol | 特發性全身性癲癇抗癲癇藥物療效與安全性比較 |
| [35421622](https://pubmed.ncbi.nlm.nih.gov/35421622/) | 2022 | Review (Tier 2) | Seizure | Topiramate 分子機轉與臨床應用價值綜述 |
| [30687937](https://pubmed.ncbi.nlm.nih.gov/30687937/) | 2019 | Cochrane Review (Tier 2) | Cochrane DB Syst Rev | Topiramate 治療青少年肌陣攣型癲癇之系統性回顧 |
| [17641254](https://pubmed.ncbi.nlm.nih.gov/17641254/) | 2007 | RCT | J Child Neurol | Topiramate 單一療法治療兒童青少年新診斷癲癇，470 人雙盲研究 |
| [33350762](https://pubmed.ncbi.nlm.nih.gov/33350762/) | 2020 | Prospective | Medicine | 劑量遞增 topiramate 用於神經外科相關癲癇之前瞻性研究 |
| [22576069](https://pubmed.ncbi.nlm.nih.gov/22576069/) | 2012 | Open-label | Epileptic Disord | Topiramate 治療顳葉癲癇之開放性研究 |
| [29424067](https://pubmed.ncbi.nlm.nih.gov/29424067/) | 2018 | Cohort (Tier 3) | Clin Exp Pharmacol Physiol | Topiramate 血中濃度與抗藥性癲癇發作頻率相關性 |
| [15811478](https://pubmed.ncbi.nlm.nih.gov/15811478/) | 2005 | Review | Clin Ther | Topiramate 單一療法用於癲癇及偏頭痛預防之療效評估 |
| [18193927](https://pubmed.ncbi.nlm.nih.gov/18193927/) | 2008 | Review | CNS Drugs | Topiramate 於癲癇治療之定位綜述 |

> 註：以上文獻均為一般癲癇族群研究，**無任何一篇針對「視覺型癲癇」此反射性亞型直接設計**，證據為從廣泛性癲癇族群外推。

### 排尿誘發癲癇 (Micturition-induced Seizures) — L4

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37368102](https://pubmed.ncbi.nlm.nih.gov/37368102/) | 2023 | Review (Tier 2) | Adv Ther | Topiramate 臨床用途與藥理考量之敘述性回顧（含非癲癇適應症擴展） |
| [40742426](https://pubmed.ncbi.nlm.nih.gov/40742426/) | 2025 | Review (Tier 2) | Epilepsia | Topiramate 用於新生兒癲癇及其他適應症之擴展應用 |
| [11384919](https://pubmed.ncbi.nlm.nih.gov/11384919/) | 2001 | Case Report (Tier 3) | Am J Psychiatry | Topiramate 用於 clozapine 誘發癲癇之個案 |
| [31029222](https://pubmed.ncbi.nlm.nih.gov/31029222/) | 2019 | Profile | Profiles Drug Subst | Topiramate 藥理全面剖析 |
| [15833090](https://pubmed.ncbi.nlm.nih.gov/15833090/) | 2005 | Review | Headache | Topiramate 分子藥理：癲癇控制與偏頭痛預防 |

> **無任何文獻直接研究「排尿誘發癲癇」**，全部為一般 topiramate 藥理/安全性資料，證據為間接推論（如評估報告 rationale 所述）。

### 聽覺誘發癲癇 (Audiogenic Seizures) — L4

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12581224](https://pubmed.ncbi.nlm.nih.gov/12581224/) | 2003 | Preclinical (Tier 3) | Epilepsia | Topiramate 於 GAERS 與 Audiogenic Wistar AS 大鼠模型之抗癲癇效果**（直接動物模型）** |
| [10666508](https://pubmed.ncbi.nlm.nih.gov/10666508/) | 2000 | Preclinical | Eur J Pharmacol | Topiramate 增強其他抗癲癇藥於 DBA/2 小鼠聲音誘發癲癇之效果**（直接動物模型）** |
| [15033346](https://pubmed.ncbi.nlm.nih.gov/15033346/) | 2004 | Preclinical | Neuropharmacology | Nifedipine 對 topiramate 抗聲音誘發癲癇活性之影響 |
| [8761322](https://pubmed.ncbi.nlm.nih.gov/8761322/) | 1996 | Preclinical (Tier 3) | Life Sci | Topiramate 於缺血誘發癲癇大鼠模型（含聽覺誘發型）之抗痙攣活性 |
| [16302877](https://pubmed.ncbi.nlm.nih.gov/16302877/) | 2005 | Review (Tier 2) | Epilepsia | 特發性全身性癲癇之光敏感性綜述 |
| [17553669](https://pubmed.ncbi.nlm.nih.gov/17553669/) | 2007 | Preclinical | Epilepsy Res | Levetiracetam 對聲音誘發癲癇抗癲癇藥效力之影響（含合併用藥比較） |

> 此候選為唯一具備**直接動物模型證據**支持機轉關聯的項目，但完全**無人體臨床試驗或個案報告**。

### 三叉神經腫瘤、驚愕型癲癇 — L5

目前無相關臨床試驗登記，亦無相關文獻。

---

## 香港上市資訊

Topiramate 目前**未於香港取得任何許可證登記**（`total_licenses = 0`），無可供分析之上市劑型或核准適應症資料。

---

## 安全性考量

安全性資訊完全缺失：警語、禁忌症、藥物交互作用查詢均為空值（`ddi.query_status = not_found`），且因香港未上市，無本地仿單可查。**安全性資訊請參考原廠（如美國 FDA 或 EMA）仿單。**

---

## 結論與下一步

**決策：分候選處理，無單一「Go」建議**

| 候選 | 決策 | 理由 |
|------|------|------|
| 視覺型癲癇 | Proceed with Guardrails | 唯一具 Phase 3/4 人體試驗與充分文獻的候選，但缺乏亞型專一設計 |
| 排尿誘發癲癇、聽覺誘發癲癇 | Research Question | 機轉理論可能成立（聽覺型有動物模型佐證），但無人體證據，需先設計探索性研究 |
| 三叉神經腫瘤、驚愕型癲癇 | Hold | 無機轉關聯或無任何證據支持，疑似模型偽陽性，不建議投入資源 |

**若要推進需要：**
- 補齊 topiramate 正式作用機轉（MOA）與原廠仿單警語/禁忌症資料（目前為 Blocking 缺口，阻擋 S1 安全性初評）
- 若考慮香港上市，需先完成藥證申請與在地安全性資料建置
- 針對視覺型癲癇，建議設計亞型專一之前瞻性研究以驗證現有廣泛性癲癇族群外推證據
- 聽覺誘發癲癇候選可優先進行轉譯研究（動物模型已具基礎），驗證是否值得推進至人體研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

