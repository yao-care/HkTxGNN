---
layout: default
title: Citalopram
parent: 高證據等級 (L1-L2)
nav_order: 143
evidence_level: L2
indication_count: 5
---

# Citalopram
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

# Citalopram：從憂鬱症到強迫症

## 一句話總結

Citalopram 是高選擇性血清素再回收抑制劑（SSRI），原本廣泛用於憂鬱症治療。TxGNN 模型預測它可能對**強迫症 (Obsessive-Compulsive Disorder)** 有效，目前有 **30 個臨床試驗**和 **16 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 憂鬱症（國際核准適應症；香港未登記） |
| 預測新適應症 | 強迫症 (Obsessive-Compulsive Disorder) |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Citalopram 是目前選擇性最高的 SSRI 之一，透過抑制突觸前膜的血清素轉運體（SERT），提升突觸間隙的 5-HT 濃度，進而調節神經迴路功能。其高度受體選擇性使它對組胺、膽鹼及腎上腺素受體的干擾極低，在 SSRI 家族中耐受性相對突出。

強迫症的核心病理機轉涉及皮質-紋狀體-視丘-皮質迴路（CSTC loop）的過度激活，以及 5-HT 系統功能失調。研究顯示，OCD 患者前額葉皮質與紋狀體之間的訊號傳遞異常，而血清素對此迴路具有直接調節作用。正是基於這個機轉，目前所有被核准用於 OCD 的藥物（包括 fluvoxamine、fluoxetine、sertraline、paroxetine 及 clomipramine）均屬 SRI 類別，機轉關聯性屬最高等級（A 級）。

特別值得注意的是：Citalopram 的活性 S-對映體——Escitalopram——已在多項 Phase 2/3 臨床試驗中被直接驗證用於 OCD 治療，且 Citalopram 本身亦有針對治療阻抗性 OCD 的隨機試驗紀錄（PMID 10572334）及兒童 OCD 開放標籤研究（PMID 12839522）。兩者機轉完全一致，差異僅在於 Escitalopram 去除了無活性 R-對映體，因此以 Escitalopram 的臨床證據作為 Citalopram 的間接支持具有高度合理性。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00305500](https://clinicaltrials.gov/study/NCT00305500) | Phase 3 | 完成 | 100 | 18 週開放標籤研究，探討高劑量 Escitalopram（>20 mg/d，最高 50 mg/d）治療 OCD 的耐受性與療效 |
| [NCT00723060](https://clinicaltrials.gov/study/NCT00723060) | Phase 4 | 完成 | 176 | 前瞻性隨機雙盲多中心試驗，比較 Escitalopram 20 mg 與 40 mg 在 OCD 的療效（Y-BOCS、HAM-D、CGI 評分） |
| [NCT00116532](https://clinicaltrials.gov/study/NCT00116532) | Phase 4 | 完成 | 30 | 直接評估 Escitalopram 治療 OCD 的療效，確定最佳治療劑量 |
| [NCT00086645](https://clinicaltrials.gov/study/NCT00086645) | Phase 2 | 完成 | 149 | **唯一大樣本直接使用 Citalopram 的 RCT（n=149）**，評估兒童自閉症高重複行為（OCD 核心症狀），結果顯示療效未優於安慰劑，需謹慎解讀 |
| [NCT00215137](https://clinicaltrials.gov/study/NCT00215137) | Phase 2 | 完成 | 14 | 先導研究，直接評估 Escitalopram 治療 OCD 的安全性與療效，設計嚴謹 |
| [NCT00680602](https://clinicaltrials.gov/study/NCT00680602) | Phase 4 | 完成 | 158 | 大型 RCT，比較認知行為治療（GCBT）與 SSRI（Fluoxetine）在 OCD 的一線療效，確立 SSRI 地位 |
| [NCT00115011](https://clinicaltrials.gov/study/NCT00115011) | Phase 4 | 完成 | 30 | 評估 Escitalopram 治療皮膚搔抓症（OCD 譜系疾患）的療效，提供 OCD 譜系支持性間接證據 |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | 完成 | 26 | OCD 藥物反應預測因子研究，受試者隨機接受 clomipramine 或 escitalopram，同時探索生物標記 |
| [NCT00708240](https://clinicaltrials.gov/study/NCT00708240) | Phase 4 | 不明 | 40 | 青少年 OCD 患者 Escitalopram 療效、安全性及執行功能、腦部活化變化研究 |
| [NCT00609531](https://clinicaltrials.gov/study/NCT00609531) | Phase 1 | 完成 | 12 | **直接使用 Citalopram**，以 fMRI 評估其對自閉症重複行為的影響，提供機轉影像學依據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35121274](https://pubmed.ncbi.nlm.nih.gov/35121274/) | 2022 | 網絡 Meta 分析 | J Psychiatric Research | 兒童及青少年 OCD 藥理與心理治療網絡比較，SSRI 為有效一線選項 |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta 回顧 | Frontiers in Psychiatry | 抗憂鬱藥（含 SSRI）在兒童青少年 OCD 急性治療中的療效、耐受性與自殺風險系統評估 |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta 分析 | J Affective Disorders | OCD 相較其他焦慮症安慰劑反應較低，但抗憂鬱藥（SSRI）治療仍具有效性 |
| [38703743](https://pubmed.ncbi.nlm.nih.gov/38703743/) | 2024 | 回顧研究 | Comprehensive Psychiatry | OCD 患者長期使用超標準劑量 SRI 的安全性與耐受性長期研究回顧 |
| [10572334](https://pubmed.ncbi.nlm.nih.gov/10572334/) | 1999 | 開放性試驗 | European Psychiatry | **直接相關**：Citalopram 用於治療阻抗性 OCD 的 90 天隨機開放標籤試驗（n=16），比較單藥與聯合 clomipramine |
| [10471169](https://pubmed.ncbi.nlm.nih.gov/10471169/) | 1999 | 案例系列 | Int Clinical Psychopharmacology | **直接相關**：專論 Citalopram 治療 OCD，探討 SRI 的 OCD 神經生物學基礎及臨床應用 |
| [12839522](https://pubmed.ncbi.nlm.nih.gov/12839522/) | 2003 | 開放標籤研究 | Psychiatry Clinical Neurosciences | **直接相關**：Citalopram 治療兒童及青少年 OCD 的 8 週初步報告（n=15），結果顯示 Y-BOCS 顯著改善 |
| [22305974](https://pubmed.ncbi.nlm.nih.gov/22305974/) | 2012 | 回顧研究 | BMJ Clinical Evidence | OCD 完整疾病概述，涵蓋 SSRI 作為主要治療選項的臨床證據摘要 |
| [12607204](https://pubmed.ncbi.nlm.nih.gov/12607204/) | 2000 | 回顧研究 | World J Biological Psychiatry | OCD 血清素神經生物學機轉完整回顧，支持 SSRI 在 OCD 治療的理論基礎 |
| [35818708](https://pubmed.ncbi.nlm.nih.gov/35818708/) | 2022 | 系統回顧 | Expert Opinion Pharmacotherapy | OCD 相關人格疾患藥理治療 RCT 的系統回顧，補充 OCD 譜系用藥依據 |

---

## 香港上市資訊

Citalopram 目前**未在香港衛生署登記上市**，無任何許可證記錄。若考慮在香港臨床研究或使用，需依照衛生署特別藥物申請途徑辦理。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Citalopram 與所有已核准 OCD 藥物共享相同作用機轉（SSRI/SERT 抑制），機轉關聯性達最高等級；其活性對映體 Escitalopram 已有 Phase 3 RCT 直接支持（證據等級 L2），且 Citalopram 本身亦有 3 篇直接相關臨床文獻（PMID 10572334、10471169、12839522），預測合理性高。

**若要推進需要：**
- 補充完整安全性資料（原廠仿單警語與禁忌症，特別是 **QTc 延長風險**，此為 Citalopram 的已知劑量相關不良反應）
- 釐清 Citalopram 與 Escitalopram 在 OCD 治療的劑量等效關係
- 評估以已有更強 OCD 直接臨床證據的 **Escitalopram** 作為優先替代方案的可行性
- 依香港衛生署規定申辦特別藥物進口許可或開展本地臨床試驗登記
- 制定針對特殊族群（兒童青少年、老年）的安全性監測計畫
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

