---
layout: default
title: Levetiracetam
parent: 高證據等級 (L1-L2)
nav_order: 448
evidence_level: L2
indication_count: 5
---

# Levetiracetam
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

# Levetiracetam：從癲癇治療到視覺誘發癲癇（Visual Epilepsy）

## 一句話總結

Levetiracetam（LEV）是國際上廣泛使用的廣效型抗癲癇藥，原用於癲癇（部分發作性癲癇等）的治療。
TxGNN 模型預測它可能對**視覺誘發癲癇 (Visual Epilepsy)** 有效，
目前有 **9 個臨床試驗**和 **20 篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 癲癇（廣效型抗癲癇藥，國際已上市；香港未查得許可證資料） |
| 預測新適應症 | 視覺誘發癲癇 (Visual Epilepsy) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 結構化的作用機轉資料（MOA 欄位為 Data Gap）。不過根據證據包中的機轉分析，Levetiracetam 透過結合突觸囊泡蛋白 SV2A，調節神經傳導物質釋放並降低皮質過度同步化放電，是一種廣效型抗癲癇藥，已知適應症涵蓋部分發作性癲癇及肌陣攣性癲癇等。

視覺誘發（光敏感型）癲癇屬於反射性癲癇的一個亞型，常合併於特發性全面型癲癇（IGE），其病生理核心是枕葉—皮質過度興奮性。這與 LEV 已證實可降低肌陣攣發作及光陣發反應（photoparoxysmal response）的機轉直接相關，因此機轉上具有合理的外推基礎。

但需注意，目前多數臨床試驗與文獻是以「癲癇大類」（創傷後癲癇預防、新生兒癲癇、全面型癲癇等）為對象，直接針對「視覺誘發癲癇」這一特定亞型的獨立確效試驗仍有限，屬同一疾病光譜內的間接證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | 已完成 | 87 | 隨機雙盲安慰劑對照，評估 LEV 於 4-16 歲難治性局部癲癇兒童之認知神經心理影響；設計與光敏感型癲癇確效研究高度相關 |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | 尚未招募 | 1649 | 探討創傷性腦損傷後癲癇之抗癲癇藥物（含 LEV）最佳使用療程 |
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | 尚未招募 | 580 | 隨機雙盲安慰劑對照試驗，評估預防性 LEV 用於腦出血急性期改善功能預後 |
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | 已完成 | 111 | 前瞻觀察性研究，評估新型 AED（含 LEV）作為局部癲癇一線併用治療之療效 |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | NA | 已完成 | 31 | 單中心開放性試驗，評估 LEV 預防偏頭痛（含有無視覺先兆）之安全性與有效性 |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | 狀態不明 | 40 | 評估 LEV 控制新生兒癲癇之療效 |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | 已完成 | 62 | 探討 LEV 調節精神病患者海馬過度活性，使用含視覺場景處理作業之功能性 MRI |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | 已終止（僅收案 1 人） | 1 | 同上主題之終止試驗，證據價值有限 |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | 邀請招募中 | 24 | Canavan disease 基因治療試驗，與 LEV 機轉無直接關聯，僅同屬癲癇治療領域 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Review/Network Meta-analysis | Journal of Neurology | 比較各 ASM（含 LEV）用於特發性全面型癲癇（IGE）之療效與安全性 |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Review/Meta-analysis | Epilepsy & Behavior | LEV 用於 IGE 肌陣攣發作（含青少年肌陣攣癲癇）之療效與安全性統合分析 |
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | LEV 對比 Phenobarbital 治療新生兒癲癇之隨機對照試驗 |
| [30487494](https://pubmed.ncbi.nlm.nih.gov/30487494/) | 2018 | RCT | Mymensingh Medical Journal | Phenobarbital 與 LEV 治療兒童癲癇之隨機對照試驗 |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Review/Meta-analysis | Neurocritical Care | LEV 用於神經重症患者癲癇預防之系統性回顧與統合分析 |
| [38316735](https://pubmed.ncbi.nlm.nih.gov/38316735/) | 2024 | Guideline | Neurocritical Care | 中重度創傷性腦損傷住院患者癲癇預防臨床指引 |
| [36209676](https://pubmed.ncbi.nlm.nih.gov/36209676/) | 2022 | Review/Network Meta-analysis | Seizure | 苯二氮平類抗藥性癲癇重積之治療系統性回顧與網絡統合分析 |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | LEV 於癲癇治療之全面性回顧，涵蓋肌陣攣及全面性強直陣攣發作等適應症 |
| [35538830](https://pubmed.ncbi.nlm.nih.gov/35538830/) | 2023 | Meta-analysis | CNS & Neurological Disorders Drug Targets | LEV 與 Phenytoin 用於兒童癲癇重積之安全性與有效性比較 |
| [40975024](https://pubmed.ncbi.nlm.nih.gov/40975024/) | 2025 | Meta-analysis | Clinical Neurology and Neurosurgery | LEV 與 Phenobarbitone 用於新生兒癲癇之療效與安全性系統性回顧 |

## 香港上市資訊

目前 Levetiracetam 未於香港取得藥品許可證（未上市，登記數 0），無法提供品名、劑型與核准適應症資訊。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
證據等級達 L2（有 Phase 2 隨機雙盲安慰劑對照試驗 NCT00105040，且多篇統合分析／指引支持 LEV 於相關癲癇族群之療效），機轉上與光敏感／視覺誘發癲癇具合理連結；但直接針對「視覺誘發癲癇」此一特定亞型的確效證據仍屬間接外推，且該藥於香港未上市。

**若要推進需要：**
- TFDA／HK 仿單警語與禁忌資料（DG001，Blocking，目前無法進入安全性初評）
- 詳細作用機轉資料（DG002，透過 DrugBank API 查詢補齊）
- 香港藥品上市登記狀態確認與許可證申請規劃
- 針對視覺誘發癲癇亞型的直接臨床證據（現有試驗多為全面型癲癇或創傷後癲癇預防之外推）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

