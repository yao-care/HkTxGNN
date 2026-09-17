---
layout: default
title: Insulin Glulisine
parent: 高證據等級 (L1-L2)
nav_order: 402
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

# Insulin Glulisine：從糖尿病血糖控制到第1型糖尿病（TxGNN 確認既有適應症，非真正老藥新用）

## 一句話總結

Insulin Glulisine（商品名 Apidra）是速效胰島素類似物，臨床上用於糖尿病患者的餐前（bolus）血糖控制。TxGNN 模型評分最高的候選是**第1型糖尿病 (Type 1 Diabetes Mellitus)**，有 **75+ 個臨床試驗**與 **19 篇文獻**支持，但這實際上是藥物既有的標準適應症，而非新發現的老藥新用機會。其餘4個候選適應症皆為 L5 等級，僅有分子層次或共病層次的間接推論，缺乏臨床實證。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料庫未記錄正式適應症文字（臨床已知：糖尿病患者血糖控制） |
| 預測新適應症 | 第1型糖尿病 (Type 1 Diabetes Mellitus)（實為既有適應症，非新發現） |
| TxGNN 預測分數 | 99.55% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空值，屬 High 等級資料缺口）。根據臨床已知資訊，Insulin Glulisine 是速效胰島素類似物，透過補充外源性胰島素直接治療胰島素缺乏，是第1型糖尿病基礎-餐前（basal-bolus）治療方案中的標準成分之一。

**需要特別指出的是**：TxGNN 排名第一的預測適應症「第1型糖尿病」本身就是這個藥物的核心臨床用途，而非新發現的老藥新用機會。根據隨附的 repurposing_rationale 分析，這代表模型正確識別了知識圖譜中既有的「胰島素—糖尿病」藥理關係，而非發掘新關聯——換言之，這並非真正的「再利用」候選，高分只是模型驗證了常識。

至於排名2-5的候選（甲硫胺酸反應性功能障礙症候群、opsismodysplasia、局部型與典型型 stiff person 症候群），皆屬罕見疾病中「糖尿病為共病或部分表現型」的間接關聯（例如 stiff person 症候群與 T1DM 因共享抗 GAD65 自體免疫機轉而常共病），並非胰島素 glulisine 對這些疾病本身的病因有特異治療作用。這些候選證據等級均為 L5，僅有模型預測，無任何臨床試驗或文獻支持。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01202474](https://clinicaltrials.gov/study/NCT01202474) | Phase 4 | 完成 | 100 | Apidra 併用 Lantus 於俄羅斯兒童青少年T1DM basal-bolus療法之療效安全性 |
| [NCT02688933](https://clinicaltrials.gov/study/NCT02688933) | Phase 4 | 完成 | 638 | Toujeo(U300) vs Lantus 於成人T1DM之CGM血糖控制比較 |
| [NCT02685449](https://clinicaltrials.gov/study/NCT02685449) | Phase 4 | 未知 | 70 | 兒童T1DM於CSII給藥情境下純蛋白餐所需胰島素劑量之交叉試驗 |
| [NCT00546702](https://clinicaltrials.gov/study/NCT00546702) | Phase 3 | 完成 | 142 | Glulisine併用Glargine於T1DM患者26週療效安全性之非隨機試驗 |
| [NCT00290979](https://clinicaltrials.gov/study/NCT00290979) | Phase 3 | 完成 | 250 | Glulisine vs Insulin Lispro於T1DM之28週非劣性隨機對照試驗 |
| [NCT00467376](https://clinicaltrials.gov/study/NCT00467376) | Phase 3 | 完成 | 485 | Glulisine vs Insulin Lispro（併用Lantus）於T1/2DM患者之隨機對照試驗 |
| [NCT04974528](https://clinicaltrials.gov/study/NCT04974528) | Phase 3 | 完成 | 319 | 吸入式Afrezza vs 速效胰島素類似物(含glulisine)於兒童T1/2DM之隨機對照試驗 |
| [NCT00271284](https://clinicaltrials.gov/study/NCT00271284) | Phase 3 | 完成 | 88 | Glargine vs Detemir併用Glulisine於T1DM血糖變異度之交叉隨機試驗 |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Phase 3 | 完成 | 59 | HMR1964(glulisine) vs Insulin Aspart於CSII之安全性隨機對照試驗 |
| [NCT01792830](https://clinicaltrials.gov/study/NCT01792830) | Phase 3 | 完成 | 175 | Glargine-based出院方案於心臟手術後高血糖T2DM病人之前瞻性研究 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16308840](https://pubmed.ncbi.nlm.nih.gov/16308840/) | 2005 | RCT | Horm Metab Res | Glulisine vs Insulin Lispro於683名T1DM患者之多中心隨機對照試驗 |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | Systematic Review | Drugs of Today | 兒童青少年T1DM之胰島素類似物（含glulisine）系統性回顧 |
| [19496630](https://pubmed.ncbi.nlm.nih.gov/19496630/) | 2009 | Review | Drugs | Insulin Glulisine於糖尿病管理之藥物綜述 |
| [18076215](https://pubmed.ncbi.nlm.nih.gov/18076215/) | 2008 | Review (PK/PD) | Clin Pharmacokinet | Glulisine臨床藥物動力學與藥效學特性回顧 |
| [35933650](https://pubmed.ncbi.nlm.nih.gov/35933650/) | 2022 | Comparative Cohort | Acta Diabetol | Glulisine vs Lispro/Aspart用於T1DM胰島素幫浦治療之比較世代研究 |
| [21457066](https://pubmed.ncbi.nlm.nih.gov/21457066/) | 2011 | RCT | Diabetes Technol Ther | Glulisine vs Aspart/Lispro於CSII給藥之隨機對照試驗 |
| [21291333](https://pubmed.ncbi.nlm.nih.gov/21291333/) | 2011 | RCT | Diabetes Technol Ther | Glulisine vs Lispro於兒童T1DM basal-bolus療法26週療效安全性比較 |
| [16123473](https://pubmed.ncbi.nlm.nih.gov/16123473/) | 2005 | PK Study | Diabetes Care | 兒童青少年T1DM之glulisine藥物動力學與餐後血糖控制安全性 |
| [19614947](https://pubmed.ncbi.nlm.nih.gov/19614947/) | 2009 | Clinical Study | Diabetes Obes Metab | Glulisine於日本T1DM患者之療效安全性研究 |
| [26838553](https://pubmed.ncbi.nlm.nih.gov/26838553/) | 2016 | Case Report | Acta Diabetol | T1DM患者局部胰島素過敏經改用glulisine後顯著緩解之個案報告 |

---

## 安全性考量

安全性資訊請參考原廠仿單。目前 TFDA 仿單警語/禁忌資料缺失（屬 Blocking 等級資料缺口），無法完成安全性初評。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測「第1型糖尿病」實為此藥物既有的標準適應症，並非新發現的老藥新用機會——TxGNN 高分只是正確驗證了胰島素與糖尿病之間的既有藥理關係。
- 排名2-5的候選皆為 L5 等級，僅有分子鄰近性或共病層次的間接推論，無任何臨床試驗或文獻支持。
- 此藥物於本地區尚未取得許可證（0張），且仿單警語/禁忌資料為 Blocking 等級缺口，無法進行安全性初評。

**若要推進需要：**
- 取得正式仿單以完成安全性初評（DG001，Blocking）
- 補充 DrugBank 作用機轉資料（DG002，High）
- 若考慮本地上市，應以現行核准適應症（糖尿病血糖控制）申請許可證，而非以此候選作為老藥新用申請基礎
- 若仍要評估候選2-5，需先取得機轉層級以上的實證支持，目前不建議投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

