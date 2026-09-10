---
layout: default
title: Olanzapine
parent: 僅模型預測 (L5)
nav_order: 540
evidence_level: L5
indication_count: 3
---

# Olanzapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Olanzapine：老藥新用評估（3 項預測適應症）

## 一句話總結

Olanzapine 原適應症資料缺失（原廠仿單、機轉皆為待補資料，且尚未於香港上市），已知其為廣效受體拮抗劑類抗精神病藥物。TxGNN 針對此藥物產出 **3 項**高分預測新適應症，其中**懼曠症 (Agoraphobia)** 證據等級最高（L3，7 篇文獻含 1 篇開放標籤試驗），其餘兩項（嬰兒良性陣發性斜頸、輕鬱症）證據薄弱甚至趨近於零，其中一項已被標註為高度疑似模型偽陽性。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（原廠仿單/機轉資料待補，DG002） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |

**三項預測適應症比較：**

| 排名 | 預測新適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議決策 |
|------|-------------|-----------|---------|---------|---------|
| 1 | 嬰兒良性陣發性斜頸 (Benign Paroxysmal Torticollis of Infancy) | 99.54% | L5 | S0 | Hold |
| 2 | 懼曠症 (Agoraphobia) | 99.47% | L3 | S1 | Research Question |
| 3 | 輕鬱症 (Dysthymic Disorder) | 99.28% | L4 | S0 | Hold |

---

## 為什麼這個預測合理？

**目前缺乏詳細的作用機轉資料（DG002，High severity）**。以下分析根據 Olanzapine 已知藥理輪廓（D2/D1/D4、5-HT2A/5-HT2C/5-HT3/5-HT6、α1、H1、M 受體拮抗）與各預測適應症之關聯性論述：

**懼曠症（排名 2，證據最強）**：Olanzapine 的 5-HT2A/5-HT2C 拮抗與鎮靜/抗焦慮作用，機轉上可支持作為 SSRI/SNRI 治療反應不佳之恐慌/懼曠症患者的加強藥物。但需注意，現有文獻幾乎全部聚焦於「恐慌障礙 (panic disorder)」而非懼曠症本身，兩者為不同診斷實體，直接證據屬外推性質。

**輕鬱症（排名 3）**：第二代抗精神病藥物作為情感疾患加強治療的機轉推論（D2/5-HT2A 調節情緒迴路）具一般性合理性，但針對輕鬱症本身、且確實使用 Olanzapine 的直接證據僅一篇個案系列（且合併邊緣性人格障礙，非單純輕鬱症族群），其餘文獻多為泛用 SGA 回顧或不同藥物（amisulpride、取代苯醯胺類）之間接證據。

**嬰兒良性陣發性斜頸（排名 1，TxGNN 分數最高但證據最弱）**：此為嬰幼兒自限性陣發性斜頸／前庭偏頭痛譜系疾患，與 Olanzapine 之 D2/5-HT 受體拮抗機轉無已知病理生理連結，且抗精神病藥物於此年齡層及此適應症無使用基礎。**無任何臨床試驗或文獻佐證，高度疑似為模型偽陽性**，不建議進一步投入資源。

---

## 臨床試驗證據

目前無相關臨床試驗登記（三項預測適應症之 ClinicalTrials.gov 與 ICTRP 查詢結果皆為 0 筆）。

---

## 文獻證據

### 懼曠症 (Agoraphobia) — 7 篇

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2025 | Review | Psychotherapy and Psychosomatics | 難治型焦慮疾患之藥物、心理治療與神經刺激治療整合性回顧 |
| [26635099](https://pubmed.ncbi.nlm.nih.gov/26635099/) | 2016 | Review | Expert Opinion on Pharmacotherapy | 難治型恐慌障礙系統性回顧，約 1/3 患者治療後仍有持續症狀 |
| [16415705](https://pubmed.ncbi.nlm.nih.gov/16415705/) | 2006 | Open-label trial | J Clin Psychopharmacology | 31 名 SSRI 治療反應不佳之恐慌障礙（含懼曠症）患者，加用低劑量 Olanzapine (5mg/d) 12 週開放標籤試驗，評估療效與耐受性 |
| [25012437](https://pubmed.ncbi.nlm.nih.gov/25012437/) | 2014 | Cohort | J Affective Disorders | 共病焦慮疾患（含懼曠症）與強迫症對雙相情感疾患 24 個月臨床結果之影響 |
| [15470803](https://pubmed.ncbi.nlm.nih.gov/15470803/) | 2004 | Case Report | Pharmacopsychiatry | Olanzapine 併用 paroxetine 使難治型恐慌障礙患者完全緩解之個案報告 |
| [10739446](https://pubmed.ncbi.nlm.nih.gov/10739446/) | 2000 | Case Report | Am J Psychiatry | Olanzapine 與恐慌發作相關之個案報告（無摘要） |
| [17099612](https://pubmed.ncbi.nlm.nih.gov/17099612/) | 2006 | Case Report | Psychiatria Danubina | 恐慌障礙合併懼曠症與精神病共病之認知行為治療個案 |

### 輕鬱症 (Dysthymic Disorder) — 5 篇

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Review (Cochrane) | Cochrane Database Syst Rev | 第二代抗精神病藥物用於重鬱症與輕鬱症之系統性回顧 |
| [10578457](https://pubmed.ncbi.nlm.nih.gov/10578457/) | 1999 | Case Series | Biological Psychiatry | Olanzapine 於邊緣性人格障礙合併輕鬱症患者之安全性與療效開放標籤試驗 |
| [22938165](https://pubmed.ncbi.nlm.nih.gov/22938165/) | 2012 | Review | Bipolar Disorders | 難治型成人雙相情感疾患之實證治療選項回顧 |
| [11920152](https://pubmed.ncbi.nlm.nih.gov/11920152/) | 2002 | Review（不同藥物類別） | Molecular Psychiatry | 取代苯醯胺類（如 sulpiride）於輕鬱症與思覺失調症陰性症狀之潛力回顧 |
| [34727399](https://pubmed.ncbi.nlm.nih.gov/34727399/) | 2021 | Systematic Review（不同藥物） | Human Psychopharmacology | Amisulpride 用於精神疾患憂鬱症狀之療效統合分析 |

### 嬰兒良性陣發性斜頸 (Benign Paroxysmal Torticollis of Infancy)

目前無相關文獻。

---

## 香港上市資訊

Olanzapine（DB00334）尚未於香港上市，無許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。目前 TFDA/香港仿單警語與禁忌症資料缺失（**DG001，Blocking**），此為進入 S1 安全性初評的阻斷性缺口，需優先補齊。

---

## 結論與下一步

**整體決策：Hold**

**理由：**
- 安全性資料缺失屬 Blocking 等級（DG001），任何預測適應症皆無法進入 S1 安全性初評。
- 三項預測中僅懼曠症具中等證據（L3），可列為後續研究問題；其餘兩項證據不足或疑似偽陽性，不建議投入資源。

**若要推進需要：**
- 補齊 Olanzapine 原廠仿單警語、禁忌症與 DDI 資料（DG001，來源：TFDA/香港官方仿單）
- 補齊詳細作用機轉資料（DG002，來源：DrugBank API）
- 若聚焦懼曠症方向，建議針對懼曠症（而非恐慌障礙）族群設計前瞻性研究，釐清是否可外推現有恐慌障礙證據
- 嬰兒良性陣發性斜頸此預測建議標記為低優先/疑似偽陽性，暫不投入後續資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

