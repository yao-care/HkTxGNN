---
layout: default
title: Rivaroxaban
parent: 僅模型預測 (L5)
nav_order: 657
evidence_level: L5
indication_count: 4
---

# Rivaroxaban
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Rivaroxaban：從 抗凝血治療 到 類風濕性關節炎

## 一句話總結

Rivaroxaban（DB06228）是 Factor Xa 抑制劑，臨床上用於抗凝血治療；由於原適應症許可證資料缺失，僅能依藥物已知藥理類別描述。TxGNN 模型將**類風濕性關節炎 (Rheumatoid Arthritis)** 列為最高分預測適應症，但目前**無相關臨床試驗**、僅有 **3 篇文獻**，且經評估後均與 RA 治療機轉無直接關聯。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（許可證清單為空，未於香港上市） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA: [Data Gap]）。根據已知藥理分類，rivaroxaban 為口服 Factor Xa 抑制劑，屬抗凝血藥物類別。

**評估結論：此預測機轉關聯性薄弱。** 現有文獻僅涉及自體免疫疾病患者的凝血酶生成異常（屬於 RA 共病之血栓風險升高現象），以及一般靜脈血栓栓塞治療綜述，並未提出 rivaroxaban 作為 RA 疾病調節治療的機轉或療效證據。TxGNN 的高分很可能反映「RA 患者血栓風險升高 → 常合併使用抗凝藥物」這一共病關聯，而非 rivaroxaban 對 RA 本身具有治療作用。此為典型的知識圖譜共現偏誤（confounding by comorbidity），並非有效的老藥新用機轉假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | 下肢靜脈血栓栓塞（DVT/PE）診斷與治療綜述，未涉及 RA |
| [34175144](https://pubmed.ncbi.nlm.nih.gov/34175144/) | 2021 | Cohort/Lab | Rev Med Interne | 探討自體免疫疾病患者凝血酶生成試驗，用於評估血栓風險而非治療 RA |
| [29621248](https://pubmed.ncbi.nlm.nih.gov/29621248/) | 2018 | Cohort | PLoS ONE | 比較房顫患者使用 rivaroxaban 與 apixaban 之服藥順從性，與 RA 無關 |

## 香港上市資訊

目前未在香港上市，無許可證資料。

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：TFDA/香港仿單警語、禁忌症與藥物交互作用資料均為缺口（DG001，Blocking），目前無法進行 S1 安全性初評。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅 L5（無臨床試驗、文獻與適應症無直接治療關聯），且評估已明確指出這是共病關聯而非治療機轉。
- 藥物 MOA 與安全性仿單資料均缺失（DG001 為 Blocking 缺口），無法進行後續安全性初評。

**若要推進需要：**
- 補齊 TFDA/香港仿单警語與禁忌症資料（DG001）
- 補齊 DrugBank 完整 MOA 資料（DG002）
- 尋找 rivaroxaban 直接作用於 RA 疾病機轉（如抗發炎、免疫調節路徑）的機轉研究，而非僅止於共病血栓風險文獻

---

### 附註：其他預測適應症（同一藥物，均建議 Hold）

本次 Evidence Pack 同時評估了 4 個候選適應症，除上述 RA 外，其餘三項證據更弱或機轉更不合理：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 主要問題 |
|------|------|-----------|---------|---------|
| 2 | Gout（痛風） | 99.51% | L5 | 唯一文獻為降尿酸藥 benzbromarone 與 CYP450 的藥物交互作用研究，與 rivaroxaban 療效無關 |
| 3 | HIV infectious disease | 99.17% | L4 | 所有證據（含 1 個 Phase 2 試驗、7 篇文獻）皆圍繞「HIV 患者合併房顫/VTE 時使用 rivaroxaban 之出血風險與抗病毒藥交互作用」，屬安全性議題而非抗病毒治療證據 |
| 4 | Brachydactyly-syndactyly syndrome（先天性肢端發育疾病） | 99.10% | L5 | 無任何臨床試驗或文獻，亦無生物學合理性 |

四項預測均建議 **Hold**，本藥物目前不具備進入下一階段評估（S1）的證據基礎。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

