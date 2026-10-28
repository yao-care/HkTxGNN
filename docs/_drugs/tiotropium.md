---
layout: default
title: Tiotropium
parent: 高證據等級 (L1-L2)
nav_order: 881
evidence_level: L1
indication_count: 5
monitor_inn: "TIOTROPIUM"
predicted_indications: ["obstructive lung disease", "respiratory malformation", "Rienhoff syndrome", "hyperlucent lung", "tracheal stenosis"]
last_modified_at: 2026-10-28
description: "Tiotropium：預測新適應症為阻塞性肺病（證據等級 L1）。原適應症：知識圖譜記錄為支氣管炎、氣喘、肺氣腫"
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

## Tiotropium：從氣喘與支氣管炎到阻塞性肺病
{: .text-alpha }

## 一句話總結

Tiotropium 是長效抗膽鹼支氣管擴張劑，知識圖譜中記錄的原適應症包括支氣管炎、氣喘與肺氣腫。
TxGNN 模型預測它可能對**阻塞性肺病 (Obstructive lung disease)** 有效，
目前有多個直接以慢性阻塞性肺病 (COPD) 為對象的 Phase 3 臨床試驗，以及多篇相關文獻支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄為支氣管炎、氣喘、肺氣腫（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 阻塞性肺病 |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L1 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 核准許可證數 | 4 張（有效 4 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未收錄 MOA）。根據文獻，Tiotropium 是一種長效蕈毒鹼受體拮抗劑（LAMA），可阻斷氣道平滑肌的 M3 受體，降低膽鹼性張力，產生持續的支氣管擴張。其與 M3 受體解離緩慢，因此可每日一次給藥。

阻塞性肺病（主要是 COPD）與知識圖譜中記錄的支氣管炎、氣喘、肺氣腫密切相關，同屬氣道阻塞性疾病。因此這個預測較接近原有用途的延伸，而非全新的跨疾病再利用，高分數與已知藥理相符。

## 臨床試驗證據

以下列出與阻塞性肺病（COPD）最相關的試驗（共 10 個）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00240435](https://clinicaltrials.gov/study/NCT00240435) | Phase 3 | 完成 | 491 | 隨機雙盲，Tiotropium Respimat 5 與 10 mcg 對比安慰劑及 ipratropium，評估支氣管擴張療效 |
| [NCT01431274](https://clinicaltrials.gov/study/NCT01431274) | Phase 3 | 完成 | 2624 | Tiotropium+Olodaterol 複方對比單一成分，52 週療效與安全性（TONado 1） |
| [NCT00157235](https://clinicaltrials.gov/study/NCT00157235) | Phase 3 | 完成 | 234 | 對比安慰劑，評估肺復健期間對運動耐受度的影響 |
| [NCT00144326](https://clinicaltrials.gov/study/NCT00144326) | Phase 3 | 完成 | 250 | 對比安慰劑，評估 12 週對日常活動量的影響 |
| [NCT00877383](https://clinicaltrials.gov/study/NCT00877383) | Phase 3 | 完成 | 1142 | Indacaterol 加 Tiotropium 對比單用 Tiotropium，12 週 |
| [NCT00900731](https://clinicaltrials.gov/study/NCT00900731) | Phase 3 | 完成 | 1598 | Indacaterol 對比 Tiotropium，12 週肺功能比較 |
| [NCT01854645](https://clinicaltrials.gov/study/NCT01854645) | Phase 3 | 完成 | 2103 | 多種吸入療法對比安慰劑與開放標示 Tiotropium，24 週 |
| [NCT02172443](https://clinicaltrials.gov/study/NCT02172443) | Phase 3 | 完成 | 50 | Tiotropium 膠囊對比 ipratropium MDI，支氣管擴張療效（樣本較小） |
| [NCT04780984](https://clinicaltrials.gov/study/NCT04780984) | Phase 2 | 完成 | 116 | 隨機劑量範圍研究，評估藥效學與安全性 |
| [NCT04999930](https://clinicaltrials.gov/study/NCT04999930) | N/A | 完成 | 100 | Respimat 搭配或不搭配 Aerochamber，比較療效與病人滿意度 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28877027](https://pubmed.ncbi.nlm.nih.gov/28877027/) | 2017 | RCT | N Engl J Med | 探討長期使用 Tiotropium 對輕中度 COPD 肺功能及其下降速度的影響 |
| [29779416](https://pubmed.ncbi.nlm.nih.gov/29779416/) | 2018 | RCT | Am J Respir Crit Care Med | SUNSET 試驗：長期三合一療法降階至 indacaterol/glycopyrronium |
| [25046211](https://pubmed.ncbi.nlm.nih.gov/25046211/) | 2014 | 系統性回顧 | Cochrane Database Syst Rev | Tiotropium 對比安慰劑用於 COPD |
| [23728670](https://pubmed.ncbi.nlm.nih.gov/23728670/) | 2013 | 系統性回顧 | Cochrane Database Syst Rev | 吸入類固醇加 LABA 複方對比 Tiotropium |
| [19402836](https://pubmed.ncbi.nlm.nih.gov/19402836/) | 2009 | 統合分析 | Respirology | Tiotropium 於中國穩定期 COPD 患者的療效與安全性 |
| [32727455](https://pubmed.ncbi.nlm.nih.gov/32727455/) | 2020 | Review | Respir Res | Tiotropium 於 COPD 的臨床開發回顧 |
| [33095662](https://pubmed.ncbi.nlm.nih.gov/33095662/) | 2021 | Review | Curr Med Res Opin | Tiotropium+Olodaterol 降低 COPD 急性惡化 |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Review | Ann Pharmacother | Ipratropium 與 Tiotropium 併用的療效與安全性 |
| [10069510](https://pubmed.ncbi.nlm.nih.gov/10069510/) | 1999 | 文獻回顧 | Life Sci | Tiotropium 的作用機轉考量及在阻塞性肺病的臨床特性 |
| [12010082](https://pubmed.ncbi.nlm.nih.gov/12010082/) | 2002 | Review | Drugs | 對 M1、M2、M3 受體的拮抗作用，18 μg 每日一次改善肺功能 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51091 | SPIRIVA CAP FOR INHALATION 18MCG | 吸入膠囊 | 請參考原廠仿單 |
| HK-57639 | SPIRIVA RESPIMAT SOL FOR INHAL 2.5MCG | 吸入溶液 | 請參考原廠仿單 |
| HK-50663 | SPIRIVA CAP FOR INHAL 18MCG (COMBOPACK) | 吸入膠囊 | 請參考原廠仿單 |
| HK-64356 | SPIOLTO RESPIMAT INHALATION SOLUTION 2.5MCG/2.5MCG | 吸入溶液 | 請參考原廠仿單 |

以上 4 張許可證均為有效狀態，持有人為 Boehringer Ingelheim (HK) Ltd。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單文字）：良性攝護腺肥大、腎功能不全、閉角型青光眼、膀胱頸阻塞。
- **藥物交互作用**：資料共查得 100 筆，主要為與其他抗膽鹼藥物併用，多屬中度，包括 hyoscyamine、atropine、glycopyrronium、clidinium、dicyclomine、trospium、scopolamine、methscopolamine、propantheline 等。另有 eluxadoline、prucalopride、吸入型人類胰島素屬中度；cimetidine 為輕度。併用多種抗膽鹼藥物可能加重口乾、尿滯留、眼壓升高等抗膽鹼作用。
- 其餘警語與禁忌資料請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個已完成的 Phase 3 隨機對照試驗（如 NCT00240435、NCT01431274、NCT00157235）直接在 COPD 族群中研究 Tiotropium，並有 NEJM 的 RCT 及 Cochrane 系統性回顧支持，證據等級為 L1。
- 阻塞性肺病與其原有用途高度重疊，近乎既有用途，主要風險在於抗膽鹼作用的安全性管理。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認核准適應症、警語與禁忌（目前許可證資料未載明適應症文字）。
- 補充詳細作用機轉資料。
- 針對有閉角型青光眼、攝護腺肥大、膀胱頸阻塞或腎功能不全的病人，訂定使用前篩檢與監測計畫，並留意與其他抗膽鹼藥物併用。

**其他預測的說明：** 其餘預測（呼吸道畸形、Rienhoff 症候群、透明肺、氣管狹窄）缺乏直接研究或機轉依據，目前建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

