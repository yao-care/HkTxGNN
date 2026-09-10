---
layout: default
title: Laronidase
parent: 中證據等級 (L3-L4)
nav_order: 437
evidence_level: L3
indication_count: 2
---

# Laronidase
{: .fs-9 }

證據等級: **L3** | 預測適應症: **2** 個
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

# Laronidase：從黏多醣症第一型 (MPS I) 到具骨骼侵犯之溶酶体贮積症

## 一句話總結

Laronidase 是重組人類 α-L-iduronidase 酵素替代療法，原本用於治療黏多醣症第一型 (MPS I)。
TxGNN 模型預測它對**具骨骼侵犯之溶酶体贮積症 (Lysosomal Storage Disease with Skeletal Involvement)** 有效，
目前有 **4 篇文獻**支持——但需注意，此病名實質上與 MPS I 高度重疊，此預測更像是模型確認既有適應症，而非發現全新用途。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 黏多醣症第一型 (Mucopolysaccharidosis I, MPS I)（香港無許可證資料，依文獻整理） |
| 預測新適應症 | 具骨骼侵犯之溶酶体贮積症 (Lysosomal Storage Disease with Skeletal Involvement) |
| TxGNN 預測分數 | 99.31%（模型排名第 11,496 位） |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails（見下文說明，實質為既有適應症確認） |

---

## 為什麼這個預測合理？

Laronidase 的官方 MOA 欄位目前缺乏正式資料（DrugBank 查詢待補，列為 High 等級資料缺口）。但依文獻整理，Laronidase 是重組人類 α-L-iduronidase 酵素，其藥理機轉是外源性補充 MPS I 患者體內缺乏的該酵素，分解堆積的醣胺聚醣 (GAG，包括 dermatan sulfate 與 heparan sulfate)，屬酵素替代療法 (ERT) 的核心機轉。

TxGNN 預測的「具骨骼侵犯之溶酶体贮積症」實質上是 MPS I（Hurler / Hurler-Scheie / Scheie 症候群）的廣義描述，骨骼侵犯正是 MPS I 的典型臨床表現之一。因此這個預測並非典型的「老藥新用」假說，而是模型正確辨識出藥物與其核心已知藥理標的之間的直接對應關係。

**重要提醒**：本 Evidence Pack 同時包含第二個候選——Sanfilippo syndrome (MPS III)，TxGNN 分數 99.22%，但機轉分析判定**不成立**：Sanfilippo 症候群的病因是 heparan sulfamidase、NAGLU、HGSNAT 或 GNS 等酵素缺乏，與 laronidase 補充的 α-L-iduronidase 屬於不同代謝路徑，無生化活性關聯。此候選被評為 L5 證據等級、S0 決策階段，建議 **Hold**，很可能是知識圖譜將「MPS」大類疾病節點過度泛化所致的偽陽性關聯，不建議進一步投入資源。

---

## 臨床試驗證據

目前無相關臨床試驗登記（查詢日期 2026-03-26，ClinicalTrials.gov 與 ICTRP 均無篩選結果）。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Review | BioDrugs | 介紹 laronidase 作為 MPS I（含 Hurler syndrome）酵素替代療法的開發歷程，取得美歐孤兒藥資格及 FDA 快速審查 |
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Review | Pediatric Endocrinology Reviews | 說明 MPS I 由 α-L-iduronidase 缺乏導致 GAG 堆積，涵蓋 Hurler、Scheie 及中間型的疾病光譜與診斷方式 |
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Cohort/Case series | Pediatric Neurology | Scheie syndrome（減弱型 MPS I）患者接受酵素替代療法 6.5 年追蹤，記錄骨骼、肝脾及關節活動度變化 |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | In vitro mechanistic study | Biological & Pharmaceutical Bulletin | 證實 laronidase 主要經由 mannose-6-phosphate 受體被 MPS I 患者纖維母細胞與成骨細胞攝取並運送至溶酶體 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：香港仿單警語與禁忌症資料目前為 Blocking 等級缺口（無法進入 S1 安全性初評），需先取得原廠/藥監局仿單後才能完成安全性評估。

---

## 結論與下一步

**決策：Proceed with Guardrails**（僅限確認既有適應症之機轉關聯，非新適應症拓展）

**理由：**
- 預測結果本質上是 TxGNN 對藥物已知核心適應症（MPS I）的機轉確認，證據等級 L3，但缺乏對照試驗與正式安全性資料。
- Laronidase 香港未上市（0 張許可證），且仿單警語/禁忌症資料缺失（Blocking），無法完成基本安全性初評。
- 第二候選 Sanfilippo syndrome 機轉不成立，判定為 Hold，不建議投入資源。

**若要推進需要：**
- 取得 TFDA/香港仿單警語與禁忌症資料，完成 S1 安全性初評（Blocking 缺口）
- 補齊 DrugBank 正式 MOA 資料
- 釐清「具骨骼侵犯之溶酶体贮積症」與現行 MPS I 適應症之邊界，確認是否具備獨立於既有適應症的臨床開發價值
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

