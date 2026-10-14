---
layout: default
title: Insulin Degludec
parent: 高證據等級 (L1-L2)
nav_order: 470
evidence_level: L1
indication_count: 5
---

# Insulin Degludec
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

# Insulin Degludec：從糖尿病到第 1 型糖尿病

## 一句話總結

Insulin Degludec 是超長效基礎胰島素類似物，原本用於糖尿病與糖尿病酮酸中毒的治療。
TxGNN 模型預測它可能對**第 1 型糖尿病 (Type 1 Diabetes Mellitus)** 有效，
目前有 **40 個臨床試驗**和 **20 篇文獻**支持這個方向。
需特別說明：第 1 型糖尿病本來就屬於該藥的核准使用範圍，因此這並非真正的藥物再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 糖尿病、糖尿病酮酸中毒（香港許可證未提供適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 第 1 型糖尿病 (Type 1 Diabetes Mellitus) |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA 欄位無內容）。但就已知藥理而言，Insulin Degludec 是超長效基礎胰島素類似物，透過結合胰島素受體，補充第 1 型糖尿病患者缺乏的內生性胰島素，提供平穩而持久的基礎降血糖效果。

第 1 型糖尿病屬於「糖尿病」大類，本來就是該藥的標準使用情境，所以 TxGNN 給出極高分數（99.44%）與其既有藥理相符。這比較像是模型對既有適應症的「再確認」，而不是發現新用途。

排名第 2 至第 5 的預測（自體免疫性卵巢炎、Opsismodysplasia、硫胺素反應性功能障礙症候群、局部僵硬肢體症候群）完全沒有臨床試驗或文獻支持，僅屬網路關聯推論，證據等級皆為 L5，建議 Hold，不建議投入資源。

---

## 臨床試驗證據

資料中共有 40 個相關試驗，以下列出最相關的 10 個（以已完成的 Phase 3 與直接評估 degludec 者優先）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02034513](https://clinicaltrials.gov/study/NCT02034513) | Phase 3 | 完成 | 501 | SWITCH 1：degludec 與 glargine（皆搭配 aspart）在第 1 型糖尿病的安全性與療效交叉比較 |
| [NCT01835431](https://clinicaltrials.gov/study/NCT01835431) | Phase 3 | 完成 | 362 | degludec/aspart 與 detemir 用於兒童及青少年第 1 型糖尿病 |
| [NCT00978627](https://clinicaltrials.gov/study/NCT00978627) | Phase 3 | 完成 | 548 | degludec/aspart 與 detemir + aspart 用於第 1 型糖尿病（含延伸期） |
| [NCT01569841](https://clinicaltrials.gov/study/NCT01569841) | Phase 3 | 完成 | 24 | 以連續血糖監測比較 degludec 與 glargine 的血糖控制 |
| [NCT05463744](https://clinicaltrials.gov/study/NCT05463744) | Phase 3 | 完成 | 692 | 每週一次基礎胰島素 efsitora 對比 degludec（degludec 為對照組） |
| [NCT04075513](https://clinicaltrials.gov/study/NCT04075513) | Phase 4 | 完成 | 343 | Toujeo 與 Tresiba 以連續血糖監測比較目標範圍內血糖及變異度 |
| [NCT00612040](https://clinicaltrials.gov/study/NCT00612040) | Phase 2 | 完成 | 178 | 兩種 degludec 配方與 glargine 的 16 週 treat-to-target 比較 |
| [NCT02500706](https://clinicaltrials.gov/study/NCT02500706) | Phase 3 | 完成 | 1108 | 快速作用 aspart 與 NovoRapid 併用 degludec 於成人（degludec 為背景治療） |
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Phase 3 | 完成 | 834 | 快速作用 aspart 與 NovoRapid 併用 degludec 於兒童及青少年（degludec 為背景治療） |
| [NCT02392117](https://clinicaltrials.gov/study/NCT02392117) | N/A | 完成 | 1262 | 真實世界觀察研究，評估 Tresiba 於第 1、2 型糖尿病的安全性與有效性 |

註：其餘多為 Phase 1 藥效／藥動學研究，以及部分以 degludec 為背景治療的試驗，間接性較高。

---

## 文獻證據

資料中共有 20 篇文獻，以下列出最相關的 10 篇（RCT > 系統性回顧／統合分析 > 其他）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT 試驗：degludec 與 detemir 用於懷孕的第 1 型糖尿病婦女（非劣性試驗） |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6：每週一次 icodec 與每日一次 degludec 於第 1 型糖尿病的比較 |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | Lancet | QWINT-5：每週一次 efsitora 與 degludec 於成人第 1 型糖尿病的非劣性比較 |
| [40903851](https://pubmed.ncbi.nlm.nih.gov/40903851/) | 2025 | RCT（資料分類為 Cohort） | Diabetes Obes Metab | 早期 degludec 併用靜脈胰島素輸注處理糖尿病酮酸中毒 |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | 統合分析 | Clin Ther | degludec 與其他長效基礎胰島素類似物於第 1、2 型糖尿病的療效與耐受性比較 |
| [40627908](https://pubmed.ncbi.nlm.nih.gov/40627908/) | 2025 | 統合分析 | J Diabetes Complications | degludec 與 efsitora 的療效與安全性比較 |
| [33662147](https://pubmed.ncbi.nlm.nih.gov/33662147/) | 2021 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | （超）長效胰島素類似物用於第 1 型糖尿病 |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | 系統性回顧／網絡統合分析 | Value Health | 成人第 1 型糖尿病基礎胰島素方案的相對療效與安全性 |
| [40742780](https://pubmed.ncbi.nlm.nih.gov/40742780/) | 2025 | Post hoc 分析 | Diabetes Technol Ther | ONWARDS 6 的連續血糖監測指標與低血糖分析 |
| [35147781](https://pubmed.ncbi.nlm.nih.gov/35147781/) | 2022 | 真實世界研究 | Acta Diabetol | 第 1 型糖尿病孕婦使用 degludec 的妊娠結果 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62700 | TRESIBA FLEXTOUCH SOLUTION FOR INJECTION IN PRE-FILLED PEN 100U/ML | 注射劑（預填充筆） | 未提供 |
| HK-67541 | TRESIBA FLEXTOUCH SOLUTION FOR INJECTION IN PRE-FILLED PEN 100U/ML | 注射劑（預填充筆） | 未提供 |
| HK-62699 | TRESIBA FLEXTOUCH SOLUTION FOR INJECTION IN PRE-FILLED PEN 200U/ML | 注射劑（預填充筆） | 未提供 |
| HK-68120 | XULTOPHY SOLUTION FOR INJECTION IN PRE-FILLED PEN 100 UNITS/ML + 3.6MG/ML | 注射劑（預填充筆） | 未提供 |
| HK-67704 | RYZODEG FLEXTOUCH SOLUTION FOR INJECTION IN PRE-FILLED PEN 100U/ML 70/30 | 注射劑（預填充筆） | 未提供 |

共 8 張有效許可證（皆為單方登記，無已註銷），持有者為 Novo Nordisk Hong Kong Limited。

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用，以下為部分中度等級項目：
  - 擬交感神經藥物：Phenylephrine、Pseudoephedrine、Epinephrine、Salbutamol、Formoterol
  - β 阻斷劑：Acebutolol
  - 其他降血糖藥物：Metformin、Pioglitazone、Alogliptin、Albiglutide
  - 荷爾蒙類：Estradiol、Levonorgestrel、Norethisterone、Hydrocortisone
  - 其他：Doxycycline、Hydrochlorothiazide、Alpelisib、Ethanol

  輕度等級者包括外用的 Hydrocortisone、Alclometasone。

其餘警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 第 1 型糖尿病是 Insulin Degludec 既有的標準使用情境，有多個已完成的 Phase 3 試驗、統合分析與 Cochrane 回顧支持，證據等級為 L1。這屬於既有適應症的確認，而非新的再利用機會。
- 香港已有 8 張有效許可證，但資料中沒有核准適應症文字與仿單安全性資訊，須先補齊才能做完整安全性評估。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 補充詳細的作用機轉資料
- 若目標是真正的再利用，應轉向其他預測適應症，但其餘四項預測目前僅有模型預測（L5），建議暫緩（Hold）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

