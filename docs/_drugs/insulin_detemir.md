---
layout: default
title: Insulin Detemir
parent: 高證據等級 (L1-L2)
nav_order: 471
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Insulin Detemir：預測新適應症為第 1 型糖尿病 (Type 1 Diabetes Mellitus)（證據等級 L1）。原適應症：糖尿病、糖尿病酮酸中毒"
monitor_inn: "INSULIN DETEMIR"
predicted_indications: ["type 1 diabetes mellitus", "autoimmune oophoritis", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome"]
---

# Insulin Detemir
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

# Insulin Detemir：從糖尿病到第 1 型糖尿病

## 一句話總結

Insulin Detemir 是長效基礎胰島素類似物，原本用於糖尿病與糖尿病酮酸中毒的治療。
TxGNN 模型預測的首要適應症為**第 1 型糖尿病 (Type 1 Diabetes Mellitus)**，目前有 **40 個臨床試驗**和 **20 篇文獻**支持。
需要說明的是，第 1 型糖尿病本身就是此藥的核准用途，因此這項預測屬於既有適應症的驗證，並非真正的新用途開發。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 糖尿病、糖尿病酮酸中毒（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 第 1 型糖尿病 (Type 1 Diabetes Mellitus) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未收錄）。依據已知藥理資訊，Insulin Detemir 是可溶性長效胰島素類似物，結合胰島素受體，補充不足的內生性胰島素以降低血糖。文獻指出，它透過脂肪酸側鏈（肉豆蔻酸）與白蛋白可逆結合，使吸收緩慢、作用可長達約 24 小時，藥動學變異比 NPH 胰島素小。

第 1 型糖尿病的核心問題是胰島素絕對缺乏，需終身使用胰島素，與藥物原適應症（糖尿病）直接相符。因此 TxGNN 的高分預測與既有藥理一致，屬於適應症內的驗證。

另外，排名第 2 至第 5 的預測（自體免疫性卵巢炎、Opsismodysplasia、硫胺素反應性功能障礙症候群、典型僵人症候群）皆無臨床試驗與文獻支持，多半來自共病或訊號通路的圖譜關聯，並非藥理上的治療依據，建議暫緩（Hold）。

---

## 臨床試驗證據

共有 40 個相關試驗登記，以下列出最相關的 10 個：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00595374](https://clinicaltrials.gov/study/NCT00595374) | Phase 3 | 完成 | 114 | Detemir + aspart 對比 NPH + aspart，成人第 1 型糖尿病血糖控制與安全性 |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Phase 3 | 完成 | 330 | 比較新舊製程 Detemir 的 12 個月安全性與療效 |
| [NCT00312156](https://clinicaltrials.gov/study/NCT00312156) | Phase 3 | 完成 | 347 | Detemir 對比 NPH 用於兒童與青少年第 1 型糖尿病 |
| [NCT00184639](https://clinicaltrials.gov/study/NCT00184639) | Phase 3 | 完成 | 71 | Detemir 對比 Semilente MC，兒童至年輕成人 32 週療效與安全性 |
| [NCT00322257](https://clinicaltrials.gov/study/NCT00322257) | Phase 3 | 終止 | 596 | 吸入型餐時胰島素對比注射 aspart（兩組均搭配 Detemir），Detemir 非比較變項 |
| [NCT00978627](https://clinicaltrials.gov/study/NCT00978627) | Phase 3 | 完成 | 548 | IDegAsp 對比 Detemir + aspart 基礎－餐時療法 |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | 完成 | 362 | IDegAsp 對比 Detemir，兒童與青少年第 1 型糖尿病 |
| [NCT00117780](https://clinicaltrials.gov/study/NCT00117780) | Phase 4 | 完成 | 520 | Detemir 每日一次與兩次的療效與安全性比較 |
| [NCT01440439](https://clinicaltrials.gov/study/NCT01440439) | Phase 4 | 未知 | 30 | Detemir 對比 Glargine，運動期間血糖控制（規模小） |
| [NCT01542463](https://clinicaltrials.gov/study/NCT01542463) | N/A | 完成 | 4,464 | 大型非介入性研究，觀察安全性、血糖控制與體重 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT 試驗：Degludec 對比 Detemir 用於懷孕第 1 型糖尿病婦女的非劣性比較 |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | (超)長效胰島素類似物用於第 1 型糖尿病的效益與低血糖風險 |
| [23243636](https://pubmed.ncbi.nlm.nih.gov/23243636/) | 2012 | 系統性回顧 | Drugs Today | 兒童與青少年第 1 型糖尿病的胰島素類似物 |
| [21878861](https://pubmed.ncbi.nlm.nih.gov/21878861/) | 2011 | 系統性回顧／統合分析 | Pol Arch Med Wewn | Detemir 與 NPH 在第 1 型糖尿病的比較 |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | 系統性回顧／網絡統合分析 | Value Health | 成人第 1 型糖尿病基礎胰島素方案的相對療效與安全性 |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | 系統性回顧／統合分析 | Clin Ther | Degludec 對比 Glargine 與 Detemir 的療效與耐受性 |
| [17326333](https://pubmed.ncbi.nlm.nih.gov/17326333/) | 2006 | Review | Vasc Health Risk Manag | Detemir 可降低低血糖（特別是夜間）風險，藥動學變異較小 |
| [15516157](https://pubmed.ncbi.nlm.nih.gov/15516157/) | 2004 | Review | Drugs | Detemir 作用較 NPH 可預測，個體內變異較小 |
| [20539842](https://pubmed.ncbi.nlm.nih.gov/20539842/) | 2010 | Review | Vasc Health Risk Manag | 與 NPH 相比低血糖率較低 |
| [17881328](https://pubmed.ncbi.nlm.nih.gov/17881328/) | 2007 | 藥理學回顧 | Endocrinol Metab Clin North Am | Detemir 的分子特性與藥效學 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65011 | LEVEMIR FLEXPEN SOLUTION FOR INJECTION IN PRE-FILLED PEN 100U/ML | 注射劑（預充填筆） | 許可證資料未載明 |
| HK-53538 | LEVEMIR FLEXPEN INJ 100U/ML | 注射劑（預充填筆） | 許可證資料未載明 |
| HK-67929 | LEVEMIR FLEXPEN SOLUTION FOR INJECTION IN PRE-FILLED PEN 100U/ML | 注射劑（預充填筆） | 許可證資料未載明 |

三張許可證皆由 Novo Nordisk Hong Kong Limited 持有，狀態均為有效。

---

## 安全性考量

- **藥物交互作用**：資料庫共收錄 100 筆交互作用，以下為部分中度交互作用：
  - 擬交感神經藥物（Phenylephrine、Pseudoephedrine、Epinephrine、Salbutamol、Formoterol）
  - β 阻斷劑（Acebutolol）
  - 其他降血糖藥（Metformin、Pioglitazone、Alogliptin、Albiglutide）
  - 其他：Hydrochlorothiazide、Acetazolamide、Doxycycline、Ethanol、Estradiol、Ethinylestradiol、Hydrocortisone、Alpelisib
  - 局部用 Hydrocortisone、Alclometasone 為輕度交互作用。

主要警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 第 1 型糖尿病為 Insulin Detemir 的既有適應症，已有多個已完成的 Phase 3 試驗（如 NCT00595374、NCT00447382、NCT00312156）及多篇系統性回顧支持，證據等級達 L1，且在香港有 3 張有效許可證。
- 其餘預測適應症（自體免疫性卵巢炎等）缺乏任何試驗與文獻，建議暫緩。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認核准適應症、警語與禁忌症
- 補充作用機轉（MOA）資料
- 若關注真正的新適應症，需針對排名第 2 至第 5 的預測另行進行機轉與前臨床驗證
- 實務使用時須監測低血糖，並留意與擬交感神經藥物、β 阻斷劑及其他降血糖藥合併使用的情況
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

