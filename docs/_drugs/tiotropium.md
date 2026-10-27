---
layout: default
title: Tiotropium
parent: 高證據等級 (L1-L2)
nav_order: 881
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Tiotropium：預測新適應症為阻塞性肺病 (Obstructive Lung Disease)（證據等級 L1）。原適應症：支氣管炎、氣喘、肺氣腫"
monitor_inn: "TIOTROPIUM"
predicted_indications: ["obstructive lung disease", "respiratory malformation", "Rienhoff syndrome"]
---

# Tiotropium
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Tiotropium：從支氣管炎／氣喘／肺氣腫到阻塞性肺病
{: .text-alpha }

## 一句話總結

Tiotropium（噻托溴銨）是長效抗蕈毒鹼支氣管擴張劑，原本用於支氣管炎、氣喘與肺氣腫等呼吸道疾病。
TxGNN 模型預測它可能對**阻塞性肺病 (Obstructive Lung Disease)** 有效，目前有**多項臨床試驗**和**多篇文獻**支持。需注意：這與原適應症高度重疊，屬於**仿單內既有用途**，並非真正的新適應症再利用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 支氣管炎、氣喘、肺氣腫（香港許可證未載明核准適應症文字，此處依知識圖譜適應症資料） |
| 預測新適應症 | 阻塞性肺病 (Obstructive Lung Disease) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。依已知藥理，Tiotropium 屬於長效蕈毒鹼拮抗劑 (LAMA)，主要阻斷氣道平滑肌上的 M3 受體，降低膽鹼性支氣管張力，產生持續的支氣管擴張，每日一次即可。

阻塞性肺病是涵蓋慢性阻塞性肺病 (COPD) 與氣喘的上位疾病類別，其核心特徵是氣流受限，而這正是 Tiotropium 直接作用的目標。因此模型的高分預測具有機轉上的合理性。

需特別強調，這個預測大多屬於**既有適應症的延伸**，與原適應症（支氣管炎、氣喘、肺氣腫）重疊，並非全新的治療領域。

## 臨床試驗證據

下列為與「阻塞性肺病」最相關的試驗（依相關性分級與規模挑選，共列 10 項）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00240435](https://clinicaltrials.gov/study/NCT00240435) | Phase 3 | 完成 | 491 | Respimat 吸入 Tiotropium 5/10 mcg 對比安慰劑與 ipratropium，評估 COPD 支氣管擴張療效 |
| [NCT01431274](https://clinicaltrials.gov/study/NCT01431274) | Phase 3 | 完成 | 2,624 | Tiotropium＋Olodaterol 固定複方對比單一成分，52 週療效與安全性（TONADO 1） |
| [NCT00877383](https://clinicaltrials.gov/study/NCT00877383) | Phase 3 | 完成 | 1,142 | Indacaterol 併用 Tiotropium 對比 Tiotropium 單用，12 週 |
| [NCT00900731](https://clinicaltrials.gov/study/NCT00900731) | Phase 3 | 完成 | 1,598 | Indacaterol 對比 Tiotropium，12 週，中重度 COPD |
| [NCT01854645](https://clinicaltrials.gov/study/NCT01854645) | Phase 3 | 完成 | 2,103 | PT003、PT005、PT001 對比安慰劑與開放標籤 Tiotropium，24 週 |
| [NCT00157235](https://clinicaltrials.gov/study/NCT00157235) | Phase 3 | 完成 | 234 | Tiotropium 對比安慰劑，對肺復健期間運動耐受度的影響 |
| [NCT00144326](https://clinicaltrials.gov/study/NCT00144326) | Phase 3 | 完成 | 250 | Tiotropium 對比安慰劑，12 週日常活動量（加速度計） |
| [NCT02172443](https://clinicaltrials.gov/study/NCT02172443) | Phase 3 | 完成 | 50 | Tiotropium 18 mcg 膠囊對比 ipratropium 定量吸入器 |
| [NCT02172807](https://clinicaltrials.gov/study/NCT02172807) | Phase 3 | 完成 | 201 | Tiotropium 18/36 µg 對比 oxitropium，4 週 |
| [NCT04780984](https://clinicaltrials.gov/study/NCT04780984) | Phase 2 | 完成 | 116 | Tiotropium 吸入溶液三種劑量的藥效、相對生體可用率與安全性 |

此外，另有 Tiotropium 於氣喘的 Phase 3 試驗（如 NCT01316380、NCT00772538），支持其於阻塞性氣道疾病的更廣泛應用。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | N Engl J Med | 長期使用 Tiotropium 於輕中度早期 COPD，評估肺功能改善與下降速度 |
| [29779416](https://pubmed.ncbi.nlm.nih.gov/29779416/) | 2018 | RCT | Am J Respir Crit Care Med | SUNSET 試驗：長期三合一療法降階為 Indacaterol/Glycopyrronium |
| [16844726](https://pubmed.ncbi.nlm.nih.gov/16844726/) | 2006 | Meta-analysis | Thorax | Tiotropium 於穩定期 COPD 的臨床事件、症狀、肺功能與不良事件 |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | Systematic review | Cochrane Database Syst Rev | Tiotropium 對比安慰劑（含 Soft Mist 吸入器）用於 COPD |
| [23728670](https://pubmed.ncbi.nlm.nih.gov/23728670/) | 2013 | Systematic review | Cochrane Database Syst Rev | 吸入類固醇＋LABA 複方對比 Tiotropium 的相對效益與風險 |
| [21672999](https://pubmed.ncbi.nlm.nih.gov/21672999/) | 2011 | Meta-analysis | BMJ | Tiotropium 霧化吸入器與死亡率相關性的系統性回顧 |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Review | Respir Res | Tiotropium 於 COPD 的臨床開發回顧 |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Review | Curr Med Res Opin | Tiotropium＋Olodaterol 用於降低與管理 COPD 急性惡化 |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | 機轉／臨床概述 | Life Sci | Tiotropium 的機轉考量與阻塞性肺病臨床特性 |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Review | Drugs | 拮抗 M1、M2、M3 受體，對 M3 解離慢，可每日一次給藥 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51091 | SPIRIVA CAP FOR INHALATION 18MCG | 吸入膠囊 | 資料未載明 |
| HK-57639 | SPIRIVA RESPIMAT SOL FOR INHAL 2.5MCG | 吸入溶液 | 資料未載明 |
| HK-50663 | SPIRIVA CAP FOR INHAL 18MCG (COMBOPACK) | 吸入膠囊（組合包） | 資料未載明 |
| HK-64356 | SPIOLTO RESPIMAT INHALATION SOLUTION 2.5MCG/2.5MCG | 吸入溶液 | 資料未載明 |

以上 4 張許可證均為有效，持證商為 Boehringer Ingelheim (HK) Ltd。

## 安全性考量

- **禁忌／需謹慎的疾病**（來自知識圖譜的藥物－疾病禁忌關聯，非仿單文字）：良性前列腺增生、腎功能不全、閉角型青光眼、膀胱頸阻塞。
- **藥物交互作用**：資料庫共查得 100 筆。多數為與其他抗膽鹼藥物併用造成的中度交互作用，包括 Hyoscyamine、Atropine、Glycopyrronium、Clidinium、Dicyclomine、Trospium、Scopolamine、Propantheline 等，須留意抗膽鹼作用疊加（口乾、尿滯留、眼壓升高等）。另有 Eluxadoline、Prucalopride 及吸入型胰島素為中度；Cimetidine 為輕度。
- 相關臨床試驗（NCT06525051）也針對 Tiotropium 對前房參數與眼壓的影響進行評估，與青光眼風險相呼應。

其他警語請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多項已完成的 Phase 3 隨機對照試驗與頂級期刊文獻（含 NEJM RCT、Cochrane 與 meta-analysis），證據等級達 L1。但此預測本質上屬於既有用途，並非新的再利用機會。

**若要推進需要：**
- 取得香港原廠仿單，確認核准適應症、警語與禁忌（目前許可證資料未載明適應症）
- 補充詳細作用機轉資料
- 針對高風險族群（前列腺肥大、閉角型青光眼、膀胱頸阻塞、腎功能不全）建立安全性監測計畫
- 評估吸入器技術與裝置選擇（HandiHaler 或 Respimat）對療效的影響

---

**補充說明：其他預測適應症**

- **呼吸道畸形 (Respiratory malformation)**：無可信的機轉連結，相關試驗實為囊性纖維化或 COPD 研究，TxGNN 高分可能是網絡鄰近性的假象。建議 **Hold**。
- **Rienhoff 症候群**：無任何試驗或文獻，僅為計算預測。建議 **Hold**。
- **重度早發性 COPD**：僅有 1 項回溯性比較研究，屬由一般 COPD 外推，列為研究問題。
- **慢性阻塞性肺病 (COPD)**：證據充分（L1），同樣屬既有標準治療，並非新用途。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

