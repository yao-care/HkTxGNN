---
layout: default
title: Calcium Lactate
parent: 中證據等級 (L3-L4)
nav_order: 128
evidence_level: L4
indication_count: 2
---

# Calcium Lactate
{: .fs-9 }

證據等級: **L4** | 預測適應症: **2** 個
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

# Calcium Lactate：從鈣補充劑到 Calcium-Alkali Syndrome

## 一句話總結

Calcium Lactate（乳酸鈣）是一種鈣補充劑，用於補充人體所需鈣質，在香港目前無上市許可。
TxGNN 模型以 **99.76%** 的高分預測其可能對 **Calcium-Alkali Syndrome（鈣鹼綜合症）** 有效；
然而機轉分析顯示，此為**因果誤判（False Positive）**：乳酸鈣是鈣鹼綜合症的**誘因而非治療藥物**，現有唯一文獻（1 篇 Case Report）亦記錄其致病案例，而非治療應用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 鈣補充劑（香港無核准許可證） |
| 預測新適應症 | Calcium-Alkali Syndrome（鈣鹼綜合症） |
| TxGNN 預測分數 | 99.76% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

> ⚠️ **此預測存在因果方向性誤判，請謹慎解讀。**

Calcium-Alkali Syndrome（舊稱 Milk-Alkali Syndrome）是由**過量攝取鈣與可吸收鹼**共同導致的三聯症：高鈣血症（Hypercalcemia）、代謝性鹼中毒（Metabolic Alkalosis）、以及急性腎功能損傷（Acute Kidney Injury）。**乳酸鈣作為可溶性鈣鹽，正是此綜合症的病因之一，而非治療手段。** 在確診或疑似 CAS 患者中繼續補充鈣劑，將直接加重高鈣血症，存在明確的臨床安全風險。

TxGNN 模型之所以給出高分（0.9976），最可能的原因是知識圖譜中「鈣補充劑」與「鈣鹼綜合症」之間存在強關聯性——但這是**致病性關聯（causal link）**，而非**治療性關聯（therapeutic link）**。模型目前無法自動區分「藥物導致疾病」與「藥物治療疾病」的方向性差異，屬已知的圖譜推論盲點。

目前缺乏詳細的作用機轉（MOA）資料。乳酸鈣的主要藥理作用為提供可溶性鈣離子，用於糾正低鈣血症，此機轉在 CAS 適應症上不適用。

---

## 臨床試驗證據

> **注意：** 以下試驗均非直接研究「乳酸鈣用於治療 Calcium-Alkali Syndrome」，相關性極低。ClinicalTrials.gov 檢索共回傳 12 筆結果，下列 10 筆依相關性排序呈現。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01839578](https://clinicaltrials.gov/study/NCT01839578) | NA | 未知 | 30 | 敗血性休克 CRRT 患者：枸橼酸局部抗凝 vs 肝素系統性抗凝；枸橼酸螯合鈣後需同步補鈣，間接涉及鈣代謝管理（邊際相關） |
| [NCT05393362](https://clinicaltrials.gov/study/NCT05393362) | NA | 完成 | 65 | 老年心衰患者心臟復健計畫之生物力學、心肺功能及射血分率評估，與目標適應症無關 |
| [NCT00711009](https://clinicaltrials.gov/study/NCT00711009) | Phase 3 | 完成 | 206 | 抗病毒初治 HIV-1 感染者：Lopinavir/Ritonavir 搭配不同骨幹藥物比較，與目標適應症無關 |
| [NCT04563845](https://clinicaltrials.gov/study/NCT04563845) | Phase 1 | 完成 | 50 | GSK3640254（HIV 整合酶抑制劑）心臟安全性 QTc 評估，與目標適應症無關 |
| [NCT03836729](https://clinicaltrials.gov/study/NCT03836729) | Phase 1 | 完成 | 16 | GSK3640254 與 TAF/FTC 藥動學交互作用研究，與目標適應症無關 |
| [NCT03816696](https://clinicaltrials.gov/study/NCT03816696) | Phase 1 | 完成 | 16 | GSK3640254 與 Dolutegravir 雙向 PK 交互作用研究，與目標適應症無關 |
| [NCT04263142](https://clinicaltrials.gov/study/NCT04263142) | Phase 1 | 完成 | 39 | GSK3640254 錠劑 vs 膠囊相對生物可用性及食物效應評估，與目標適應症無關 |
| [NCT02981602](https://clinicaltrials.gov/study/NCT02981602) | Phase 2 | 完成 | 31 | IONIS-HBVRx 用於慢性 B 型肝炎初治患者安全性與抗病毒活性評估，與目標適應症無關 |
| [NCT04857892](https://clinicaltrials.gov/study/NCT04857892) | Phase 1 | 完成 | 41 | GSK3640254／Dolutegravir 固定劑量複方與個別給藥之相對生物可用性研究，與目標適應症無關 |
| [NCT03984825](https://clinicaltrials.gov/study/NCT03984825) | Phase 1 | 完成 | 23 | GSK3640254 對口服避孕藥（EE/LNG）藥動學影響之單向交互作用研究，與目標適應症無關 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31968342](https://pubmed.ncbi.nlm.nih.gov/31968342/) | 2020 | Case Report | Am J Nephrology | 全甲狀腺切除術後副甲狀腺功能低下患者因需長期大量補鈣（含鈣鹽製劑），導致 Calcium-Alkali Syndrome 的病例報告；研究記錄的是鈣補充**引發** CAS，而非治療應用 |

---

## 香港上市資訊

Calcium Lactate 在香港目前**無上市許可**，藥物登記資料庫中無相關許可證紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
此案為知識圖譜模型的典型**因果方向性誤判（Causation-Therapy Confusion）**：乳酸鈣是 Calcium-Alkali Syndrome 的致病誘因，現有唯一文獻正是記錄其致病案例，在 CAS 患者中給予鈣劑將直接加重高鈣血症與腎損傷，具有明確臨床風險，不建議以此方向推進再利用研究。第 2 順位預測適應症——原發性骨礦化缺陷（evidence level L5）——目前無任何臨床試驗或文獻支持，屬純模型預測階段。

**若要推進需要：**
- 將 Calcium-Alkali Syndrome 在分析資料庫中標記為 **Causation Artifact**，排除後續再利用評估
- 評估骨礦化缺陷（第 2 適應症）在特定亞型（如 Rickets、Osteomalacia）中補充鈣質的理論可行性，需先取得 MOA 資料及前臨床研究（建議查詢 DrugBank API）
- 香港無上市許可，任何適應症若進入後期評估，需規劃藥品取得途徑與藥監局溝通策略
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

