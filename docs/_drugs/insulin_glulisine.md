---
layout: default
title: Insulin Glulisine
parent: 高證據等級 (L1-L2)
nav_order: 465
evidence_level: L1
indication_count: 5
---

# Insulin Glulisine
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Insulin Glulisine：從糖尿病血糖控制到第 1 型糖尿病

## 一句話總結

Insulin glulisine（商品名 Apidra）是速效人類胰島素類似物，用於餐時血糖控制。
TxGNN 預測它對**第 1 型糖尿病 (Type 1 Diabetes Mellitus)** 有效，目前有 **50 個臨床試驗**和 **19 篇文獻**。
這個預測很可能只是知識圖譜中既有的藥物與疾病關聯，**不是新的老藥新用發現**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 第 1 型糖尿病 (Type 1 Diabetes Mellitus) |
| TxGNN 預測分數 | 99.55% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

香港許可證資料未載明核准適應症，原適應症欄位因此省略。依文獻（PMID 19496630），本藥核准用於改善成人、青少年與兒童糖尿病的血糖控制。

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。依文獻，Insulin glulisine 是 3(B)-Lys、29(B)-Glu 的人類胰島素類似物，會結合胰島素受體並降低血糖。它比一般人類胰島素起效更快、作用時間更短，約 1 小時達高峰，持續約 4 小時，適合餐前或餐後立即注射。

第 1 型糖尿病是胰島素絕對缺乏的疾病，外源性胰島素直接補充缺少的激素，機轉上完全吻合。這個高分預測（99.55%）最可能反映知識圖譜中已有的藥物與疾病連結，而不是新穎的再利用訊號。因此不宜將它包裝成再利用發現。

---

## 臨床試驗證據

共 50 個試驗，其中多項直接針對第 1 型糖尿病。以下列出 10 個最相關者。
資料庫摘要只有試驗設計與目的，未提供結果，因此「主要發現」欄寫的是研究設計與目標。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Phase 3 | 完成 | 250 | 第 1 型糖尿病，28 週隨機對照，檢驗 glulisine 相對 lispro 的 HbA1c 非劣性與安全性 |
| [NCT00271284](https://clinicaltrials.gov/study/NCT00271284) | Phase 3 | 完成 | 88 | 交叉隨機，比較搭配 glulisine 的 glargine 與 detemir 對空腹血糖變異度的影響 |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Phase 3 | 完成 | 59 | 12 週，胰島素幫浦 (CSII) 中 glulisine 與 aspart 的安全性比較（導管阻塞、低血糖等） |
| [NCT00546702](https://clinicaltrials.gov/study/NCT00546702) | Phase 3 | 完成 | 142 | 開放、非隨機，搭配 glargine 治療 26 週，評估 HbA1c 變化與安全性 |
| [NCT00467376](https://clinicaltrials.gov/study/NCT00467376) | Phase 3 | 完成 | 485 | 第 1 或 2 型糖尿病，12 週，與 lispro 比較療效與低血糖頻率 |
| [NCT00964574](https://clinicaltrials.gov/study/NCT00964574) | Phase 4 | 完成 | 68 | 第 1 型糖尿病搭配 glargine，開放非隨機，評估療效、劑量與病人滿意度 |
| [NCT01202474](https://clinicaltrials.gov/study/NCT01202474) | Phase 4 | 完成 | 100 | 兒童與青少年 Apidra 加 Lantus，評估 HbA1c 達標比例（俄羅斯） |
| [NCT01678235](https://clinicaltrials.gov/study/NCT01678235) | Phase 4 | 完成 | 64 | 兒童幫浦治療，雙盲交叉比較 glulisine 與 aspart 對高升糖指數餐後血糖的影響 |
| [NCT00913497](https://clinicaltrials.gov/study/NCT00913497) | Phase 4 | 完成 | 16 | 學齡前兒童交叉試驗，比較 glulisine 與 aspart 對早餐後血糖的影響 |
| [NCT00489190](https://clinicaltrials.gov/study/NCT00489190) | Phase 4 | 完成 | 45 | 12 週皮下注射，收集療效與安全性資料 |

至少 NCT00290979、NCT00271284、NCT00046150、NCT00546702 四項屬已完成的 Phase 3 第 1 型糖尿病試驗，其中前三項為隨機試驗，符合 L1 條件。
Evidence Pack 中另有一個 Phase 3 試驗（NCT01792830）是心臟手術後的第 2 型糖尿病，不能作為第 1 型糖尿病的證據。

---

## 文獻證據

共 19 篇，以下列出 10 篇（優先 RCT，其次系統性回顧與 Review）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Horm Metab Res | 多國、開放、平行組試驗，683 位成人第 1 型糖尿病隨機分組，比較 glulisine 與 lispro 的療效與安全性 |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technol Ther | 幫浦治療中 glulisine 與 aspart、lispro 的三方交叉隨機比較，關注導管阻塞 |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | 臨床試驗 | Diabetes Technol Ther | 兒童與青少年 26 週基礎-餐時方案，標題指出 glulisine 與 lispro 療效及安全性相當 |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | 臨床試驗 | Diabetes Obes Metab | 日本第 1 型糖尿病患者以 glargine 為基礎胰島素，比較 glulisine 與 lispro |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | 系統性回顧 | Drugs Today | 兒童與青少年第 1 型糖尿病的胰島素類似物，涵蓋 lispro、aspart、glulisine |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | 核准用於成人、青少年與兒童糖尿病；起效較快，與 lispro 對血糖的效果相近 |
| [16706558](https://pubmed.ncbi.nlm.nih.gov/16706558/) | 2006 | Review | Drugs | 起效較快、作用時間短於一般人類胰島素；第 1 型糖尿病大型試驗中 HbA1c 控制與其相近 |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | 比較性臨床研究 | Acta Diabetol | 幫浦治療的第 1 型糖尿病患者，比較 glulisine 與 lispro、aspart 的 HbA1c、空腹血糖、高低血糖與酮酸中毒發生率 |
| [28544684](https://pubmed.ncbi.nlm.nih.gov/28544684/) | 2017 | 臨床研究 | Pediatr Int | 20 位兒童用於 CSII 一年，餐後血糖顯著改善（早餐後由 192.5 降至 162.0 mg/dL） |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | PK/PD 研究 | Diabetes Care | 兒童與青少年第 1 型糖尿病，餐前注射 glulisine 與一般人類胰島素的藥動學、餐後血糖與安全性比較 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56757 | APIDRA SOLOSTAR SOLUTION FOR INJ 100 UNITS/ML (PRE-FILLED PEN) | 注射液（預填筆，依品名判斷） | 許可證資料未載明 |

持證商：SANOFI HONG KONG LIMITED。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個完成的 Phase 3 第 1 型糖尿病試驗（含隨機對照）與 RCT 文獻，療效證據充分。
- 這是已上市的胰島素，預測反映的是既有用途，並非新的再利用發現。同時香港仿單的警語與禁忌資料尚缺。

**若要推進需要：**
- 取得衛生署（Department of Health）仿單，確認香港核准適應症，補齊警語與禁忌（目前為阻擋性資料缺口）。
- 補上 DrugBank 的作用機轉資料。
- 報告與對外呈現時，不要將本項標示為再利用發現。

**其他預測適應症：** 硫胺素反應性功能障礙症候群、Opsismodysplasia、局部僵硬肢體症候群、典型僵人症候群，證據等級皆為 L5，無試驗與文獻。
它們多半反映糖尿病共病或自體免疫關聯，並非胰島素的治療效果，建議 **Hold**。

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

