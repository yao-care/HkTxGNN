---
layout: default
title: Fluoxetine
parent: 中證據等級 (L3-L4)
nav_order: 385
evidence_level: L4
indication_count: 5
---

# Fluoxetine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Fluoxetine：從憂鬱症到分裂樣人格障礙

## 一句話總結

Fluoxetine（氟西汀）是選擇性血清素再回收抑制劑（SSRI），一般用於憂鬱症等情緒與焦慮相關疾病。
TxGNN 模型預測它可能對**分裂樣人格障礙 (Schizoid Personality Disorder)** 有效，但目前**沒有臨床試驗**，3 篇文獻也都只是間接相關，證據僅屬機轉推論層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 憂鬱症等（依一般藥理知識；香港許可證資料未提供核准適應症文字） |
| 預測新適應症 | 分裂樣人格障礙 (Schizoid Personality Disorder) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 尚未取得）。Fluoxetine 屬於 SSRI，可提高突觸間血清素濃度，其在情緒與焦慮症狀上的療效已被廣泛使用。

分裂樣人格障礙屬 Cluster A 人格障礙，患者常有社交孤立，並可能伴隨憂鬱、焦慮或社交焦慮。血清素調節可能改善這些共病症狀，但這只是推論，尚未有分裂樣人格障礙的直接研究證實。

0.999 的 TxGNN 分數來自知識圖譜預測，不是臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29955451](https://pubmed.ncbi.nlm.nih.gov/29955451/) | 2016 | Review | The Mental Health Clinician | 回顧 Cluster A 人格障礙（含分裂樣）的藥物治療，顯示相關證據有限 |
| [10929788](https://pubmed.ncbi.nlm.nih.gov/10929788/) | 2000 | Cohort | Comprehensive Psychiatry | 評估 148 名身體臆形症患者的人格障礙與特質，其中 26 人參與 fluvoxamine 治療研究；並非針對分裂樣人格障礙的療效 |
| [16390895](https://pubmed.ncbi.nlm.nih.gov/16390895/) | 2006 | Cohort | American Journal of Psychiatry | 追蹤憂鬱症患者 6 個月治療的病程與預測因子，與分裂樣人格障礙無直接關聯 |

以上文獻都沒有直接評估 fluoxetine 對分裂樣人格障礙的療效。

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證。資料未提供劑型與核准適應症文字，劑型僅由品名判斷為膠囊。

| 許可證號 | 品名 | 劑型 | 廠商 |
|---------|------|------|------|
| HK-68820 | APO-FLUOXETINE CAPSULES 20MG | 膠囊 | HIND WING CO LTD |
| HK-35706 | MAGRILAN CAP 20MG | 膠囊 | STAR MEDICAL SUPPLIES LTD |
| HK-68648 | AROZAC CAPSULES 10MG | 膠囊 | APT PHARMA LIMITED |
| HK-41383 | APO-FLUOXETINE CAP 20MG | 膠囊 | HIND WING CO LTD |
| HK-60977 | FLUOXETINE CAPSULES BP 20MG | 膠囊 | AUROBINDO PHARMA LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻也只有間接證據，目前僅為模型預測加上機轉推論。
- 香港藥品仿單的警語與禁忌尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署藥品仿單的警語與禁忌資料
- 補齊 DrugBank 作用機轉資料
- 針對分裂樣人格障礙設計專屬的臨床研究，或補足直接證據
- 同批預測中，**分裂樣型人格障礙 (Schizotypal Personality Disorder)** 是唯一有 fluoxetine 直接用於該疾病的研究（PMID 1853957，1991；PMID 9448667，1998；均為早期非對照研究，且合併境界型人格障礙患者），可優先評估為研究方向
- 嬰兒良性陣發性斜頸的預測沒有任何證據，且涉及嬰幼兒用藥，需另做安全性評估

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

