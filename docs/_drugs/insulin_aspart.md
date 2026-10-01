---
layout: default
title: Insulin Aspart
parent: 高證據等級 (L1-L2)
nav_order: 461
evidence_level: L1
indication_count: 5
---

# Insulin Aspart
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

# Insulin Aspart：從速效胰島素類似物到第 1 型糖尿病

## 一句話總結

Insulin Aspart 是速效胰島素類似物，資料中未列出原適應症，實際上就是糖尿病的血糖控制用藥。
TxGNN 模型預測它可能對**第 1 型糖尿病 (Type 1 Diabetes Mellitus)** 有效，
目前有 **50 個臨床試驗**（其中多個為已完成的 Phase 3 隨機試驗）和 **20 篇文獻**支持。
需注意：這是藥物的既有主要用途，並非真正的老藥新用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 第 1 型糖尿病 (Type 1 Diabetes Mellitus) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張 |
| 建議決策 | Proceed with Guardrails |

香港許可證資料中的核准適應症欄位皆為空白，因此未列出「原適應症」。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Insulin Aspart 是速效胰島素類似物，
會結合胰島素受體，補充第 1 型糖尿病患者缺乏的內源性胰島素。

第 1 型糖尿病是胰臟 β 細胞遭自體免疫破壞、造成胰島素缺乏的疾病。
補充胰島素是其治療核心，因此 TxGNN 給出很高的分數（99.95%）。

這個預測反映的是藥物既有的主要用途，不是新發現。
原適應症與原始 MOA 欄位在輸入資料中是空的，屬於資料完整性問題，不是新證據。
把它當成老藥新用候選之前，應先對照香港核准的仿單適應症。

## 臨床試驗證據

以下列出最相關的 10 個試驗，共 50 個。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01486940](https://clinicaltrials.gov/study/NCT01486940) | Phase 3 | 完成 | 598 | 隨機分組比較 detemir 加 aspart 與 NPH 加人類胰島素（基礎-餐時方案），對象為第 1 型糖尿病。標題被截斷，aspart 的角色需再確認 |
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | 完成 | 350 | BEGIN Young 1：兒童與青少年第 1 型糖尿病，degludec 對 detemir，以 aspart 作為餐時胰島素，26 週療效與安全性 |
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Phase 3 | 完成 | 834 | 更快速型 aspart 對 NovoRapid（皆併用 degludec），對象為兒童與青少年第 1 型糖尿病 |
| [NCT01134107](https://clinicaltrials.gov/study/NCT01134107) | Phase 3 | 完成 | 133 | 雙盲交叉，胰島素幫浦使用 lispro 與 aspart 的比較，對象為第 1 型糖尿病 |
| [NCT00046150](https://clinicaltrials.gov/study/NCT00046150) | Phase 3 | 完成 | 59 | 12 週，胰島素幫浦 (CSII) 使用 HMR1964 與 aspart 的安全性比較，對象為第 1 型糖尿病 |
| [NCT00447382](https://clinicaltrials.gov/study/NCT00447382) | Phase 3 | 完成 | 330 | 兩種製程的 detemir 安全性比較，以 aspart 作為餐時胰島素，52 週 |
| [NCT04711382](https://clinicaltrials.gov/study/NCT04711382) | 不適用（觀察性） | 完成 | 438 | 比利時真實世界研究，第 1 型糖尿病由傳統餐時胰島素轉換為 Fiasp（更快速型 aspart） |
| [NCT05224258](https://clinicaltrials.gov/study/NCT05224258) | 不適用（器材） | 完成 | 240 | MiniMed 780G 系統搭配 Fiasp，成人與兒童第 1 型糖尿病居家使用 |
| [NCT03659799](https://clinicaltrials.gov/study/NCT03659799) | Phase 4 | 完成 | 40 | 雙盲隨機交叉，比較 aspart 與 Fiasp 對餐後運動期間血糖波動的影響 |
| [NCT01773798](https://clinicaltrials.gov/study/NCT01773798) | Phase 1 | 完成 | 33 | degludec/aspart 的藥效與藥動學研究，支持藥理但不是療效試驗 |

## 文獻證據

以下列出最相關的 10 篇。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37804858](https://pubmed.ncbi.nlm.nih.gov/37804858/) | 2023 | RCT | Lancet Diabetes Endocrinol | CopenFast：懷孕與產後的第 1、2 型糖尿病，比較更快速型 aspart 與 aspart 對胎兒生長的影響 |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT：懷孕的第 1 型糖尿病，degludec 對 detemir（皆併用 aspart）的非劣性試驗 |
| [40129237](https://pubmed.ncbi.nlm.nih.gov/40129237/) | 2025 | RCT | Diabetes Obes Metab | 雙盲交叉，成人第 1 型糖尿病使用非自動化胰島素幫浦與連續血糖監測，比較更快速型 aspart 與 aspart 的療效與安全性 |
| [21333580](https://pubmed.ncbi.nlm.nih.gov/21333580/) | 2011 | 系統性回顧 | Diabetes Metab | 比較 aspart 與人類胰島素在第 1、2 型糖尿病的療效與安全性 |
| [12215068](https://pubmed.ncbi.nlm.nih.gov/12215068/) | 2002 | Review | Drugs | 多數第 1 型糖尿病的隨機試驗中，餐前 aspart 的 HbA1c 顯著低於人類胰島素 |
| [39115159](https://pubmed.ncbi.nlm.nih.gov/39115159/) | 2024 | 世代研究 | Diabet Med | 第 1 型糖尿病懷孕的真實世界資料，比較 aspart 與其他餐時胰島素的血糖控制與安全性 |
| [31902063](https://pubmed.ncbi.nlm.nih.gov/31902063/) | 2020 | Review | Diabetes Ther | 成人第 1 型糖尿病的胰島素治療策略：多數採基礎/餐時方案，部分患者可考慮幫浦 |
| [29978361](https://pubmed.ncbi.nlm.nih.gov/29978361/) | 2019 | Review | Clin Pharmacokinet | 更快速型 aspart 的藥動學與藥效學：20 分鐘時降血糖效果更強 |
| [41697686](https://pubmed.ncbi.nlm.nih.gov/41697686/) | 2026 | Review | JAMA | 第 1 型糖尿病總覽：β 細胞遭自體免疫破壞造成胰島素缺乏，並有微血管與大血管併發症 |
| [30789066](https://pubmed.ncbi.nlm.nih.gov/30789066/) | 2019 | Review | Expert Opin Drug Metab Toxicol | 回顧 degludec/aspart 預混製劑用於第 1 型糖尿病的可能性 |

## 香港上市資訊

共 14 張許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-55341 | NOVORAPID FLEXPEN INJ 100U/ML | Novo Nordisk Hong Kong Limited |
| HK-68191 | NOVORAPID FLEXPEN SOLUTION FOR INJECTION IN PRE-FILLED PEN 100U/ML | Novo Nordisk Hong Kong Limited |
| HK-67493 | FIASP FLEXTOUCH SOLUTION FOR INJECTION IN PRE-FILLED PEN 100U/ML 3ML | Novo Nordisk Hong Kong Limited |
| HK-67494 | FIASP PENFILL SOLUTION FOR INJECTION IN CARTRIDGE 100U/ML 3ML | Novo Nordisk Hong Kong Limited |
| HK-68936 | KIRSTY SOLUTION FOR INJECTION IN PRE-FILLED PEN 300 UNITS/3ML | Primedica Limited |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有多個已完成的 Phase 3 隨機試驗與多篇 RCT、系統性回顧，證據等級達 L1。
但這是 Insulin Aspart 的既有主要用途，不是新適應症；
部分試驗中 aspart 只是餐時背景用藥或對照組，不是被測試的主角。

**若要推進需要：**
- 對照香港衛生署核准的仿單適應症，確認第 1 型糖尿病是否已在標示內，再決定是否視為老藥新用候選
- 補充作用機轉與原適應症資料
- 取得香港仿單的警語與禁忌症
- 逐一確認被截斷標題的試驗（如 NCT01486940、NCT01513473）中 aspart 的實際角色

**其他預測適應症：**
- 永久性新生兒糖尿病（證據等級 L4）：僅有 1 篇胰島素治療的回顧文獻，且未涉及 aspart，建議作為研究問題，先做 aspart 在新生兒與嬰兒（含幫浦使用）的用法、劑量與安全性回顧
- 自體免疫性卵巢炎、Opsismodysplasia、硫胺素反應性功能異常症候群（證據等級 L5）：僅有模型預測，無試驗或文獻，建議 Hold

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

