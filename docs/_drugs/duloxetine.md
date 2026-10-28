---
layout: default
title: Duloxetine
parent: 僅模型預測 (L5)
nav_order: 302
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
monitor_inn: "DULOXETINE"
predicted_indications: ["benign paroxysmal torticollis of infancy", "agoraphobia", "obsessive-compulsive disorder", "paranoid personality disorder", "schizotypal personality disorder", "schizoid personality disorder", "histrionic personality disorder (disease)", "Ohdo syndrome and variants", "ligneous conjunctivitis", "blepharophimosis - intellectual disability syndrome, Ohdo type"]
description: "Duloxetine：預測新適應症為嬰兒良性陣發性斜頸 (Benign paroxysmal torticollis of infancy)，排名第 1（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Duloxetine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Duloxetine: 嬰兒良性陣發性斜頸 (Benign paroxysmal torticollis of infancy)，排名第 1；證據最完整者為強迫症 (OCD)，排名第 3 (benign paroxysmal torticollis of infancy)
{: .text-alpha }

## 一句話總結

Duloxetine 是一種血清素－正腎上腺素再回收抑制劑（SNRI），原本用於重度憂鬱症、焦慮症、纖維肌痛等適應症。
TxGNN 模型預測分數最高的新適應症為「陣發性斜頸（嬰兒期）」，但該項僅有模型預測、沒有任何研究支持。
證據最完整的預測方向是**強迫症 (Obsessive-Compulsive Disorder)**，目前有 **3 個臨床試驗**和 **19 篇文獻**，其中包含 1 項雙盲對照試驗。以下報告以此方向為主軸，並說明排名第一的預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 嬰兒良性陣發性斜頸 (Benign paroxysmal torticollis of infancy)，排名第 1；證據最完整者為強迫症 (OCD)，排名第 3 (benign paroxysmal torticollis of infancy) |
| TxGNN 預測分數 | 0.9985 |
| 證據等級 | 嬰兒良性陣發性斜頸 L5；強迫症 L2 |
| 香港上市 | 上市中（有效許可證 20 張／共 20 張） |
| 許可證數 | 20 張（有效 20 張） |
| 建議決策 | 嬰兒良性陣發性斜頸：Hold；強迫症：Proceed with Guardrails（作為研究性問題） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Duloxetine 屬於 SNRI 類抗憂鬱藥，能同時抑制血清素與正腎上腺素的再回收。

**強迫症方向：** 抑制血清素再回收是強迫症一線藥物治療（SSRI、clomipramine）的核心機轉，因此 duloxetine 在機轉上有合理性。不過，一般而言 SNRI 在強迫症的證據弱於 SSRI。多篇回顧文獻將 SNRI 定位為「可考慮的選項」，而非標準治療。

**排名第 1 的嬰兒良性陣發性斜頸：** 這是兒童期、可能與離子通道（如 CACNA1A）相關、屬偏頭痛譜系的疾患。目前沒有任何臨床試驗或文獻支持，SNRI 的機轉依據也未建立，且嬰兒用藥有安全性疑慮。0.9985 的高分來自 TxGNN 模型（深度學習），可能只是反映模型學到的相關疾病間相似性，並非生物學證據。

**其他預測：** 排名 4–7 的人格障礙症分數完全相同（0.9978），推測反映 TxGNN 模型（深度學習）學到的疾病類別層級相似性，而非藥物特異性證據。排名 8–10（Ohdo 症候群及其變異、木樣結膜炎）屬罕見遺傳或代謝疾病，均無合理機轉連結，也無證據。排名 2 的懼曠症（agoraphobia）僅有恐慌症的開放標籤研究與個案報告間接支持。

---

## 臨床試驗證據

以下為強迫症方向的試驗（排名第 1 的預測無臨床試驗登記）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00464698](https://clinicaltrials.gov/study/NCT00464698) | Phase 4 | 完成 | 20 | 直接評估 duloxetine 治療強迫症的療效；樣本小，可能為開放標籤 |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | 完成 | 26 | 預測強迫症藥物反應；隨機分配 clomipramine 或 escitalopram，曾用過這兩種藥者改用 duloxetine，並非直接的療效驗證 |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | 未知 | 8800 | 焦慮症抗憂鬱藥療效與初始嚴重度的個別病患資料統合分析，僅間接相關 |

---

## 文獻證據

僅列出與強迫症最相關的 10 篇（依 RCT > 回顧 > 個案報告排序）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27811556](https://pubmed.ncbi.nlm.nih.gov/27811556/) | 2016 | RCT | J Clin Psychopharmacol | 雙盲對照試驗，評估 duloxetine 加成治療難治型強迫症 |
| [25637377](https://pubmed.ncbi.nlm.nih.gov/25637377/) | 2015 | 開放標籤研究 | Int J Neuropsychopharmacol | 評估 duloxetine 治療強迫症（DSM-IV）的療效 |
| [31749717](https://pubmed.ncbi.nlm.nih.gov/31749717/) | 2019 | 系統性回顧 | Front Psychiatry | 彙整 duloxetine 在憂鬱症與廣泛性焦慮症以外精神疾患的證據 |
| [16669725](https://pubmed.ncbi.nlm.nih.gov/16669725/) | 2006 | 回顧 | J Clin Psychiatry | 評述 SNRI（venlafaxine、clomipramine）在強迫症的抗強迫作用，作為 SSRI 之外的替代選項 |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | 回顧 | Expert Opin Pharmacother | 回顧具明顯血清素作用的抗憂鬱藥在強迫症的雙盲研究 |
| [21779536](https://pubmed.ncbi.nlm.nih.gov/21779536/) | 2011 | 回顧 | Innov Clin Neurosci | 探討 SNRI 作為強迫症藥物替代方案的可能性 |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | 統合分析 | J Affect Disord | 強迫症的安慰劑與抗憂鬱藥反應低於其他焦慮症 |
| [18208931](https://pubmed.ncbi.nlm.nih.gov/18208931/) | 2008 | 個案系列 | J Psychopharmacol | 難治型強迫症患者由 SRI 轉換為 duloxetine |
| [39735048](https://pubmed.ncbi.nlm.nih.gov/39735048/) | 2024 | 個案報告 | Cureus | 超治療劑量 duloxetine 合併認知行為治療用於難治型強迫症合併憂鬱 |
| [19483491](https://pubmed.ncbi.nlm.nih.gov/19483491/) | 2009 | 個案報告 | Clin Neuropharmacol | 高劑量 duloxetine 治療難治型強迫症，達持續完全緩解 |

另有懼曠症方向的間接文獻（恐慌症開放標籤研究 PMID 19228176 等），證據等級為 L3。

---

## 香港上市資訊

Duloxetine 在香港共有 20 張有效許可證（皆為單方，無已註銷者）。資料中未載明核准適應症文字與劑型。列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53843 | CYMBALTA CAP 60MG（Eli Lilly Asia） | 未載明 | 未載明 |
| HK-53844 | CYMBALTA CAP 30MG（Eli Lilly Asia） | 未載明 | 未載明 |
| HK-64014 | DULOXETINE SANDOZ DELAYED RELEASE CAPSULES 30MG（Sandoz） | 未載明（緩釋膠囊） | 未載明 |
| HK-64013 | DULOXETINE SANDOZ DELAYED RELEASE CAPSULES 60MG（Sandoz） | 未載明（緩釋膠囊） | 未載明 |
| HK-65544 | SEBATA GASTRO-RESISTANT CAPSULES 30MG（LSB） | 未載明（耐胃酸膠囊） | 未載明 |

---

## 安全性考量

- **知識圖譜標示的相關禁忌疾病：** 高血壓、姿勢性低血壓、癲癇、雙相情緒障礙、肝病（含肝硬化、脂肪肝、肝炎）、膽囊疾病、高血糖、凝血疾病、物質濫用/依賴、狹角型青光眼、抗精神病藥惡性症候群、抗利尿激素分泌不當症候群、血清素症候群等。此資料來自知識圖譜，並非仿單內容。
- **藥物交互作用：** 資料庫共 100 筆交互作用（以下為已列出的前 20 筆摘要）。
  - 嚴重（Major）：bupropion、lorcaserin、diethylpropion、dolasetron、dexfenfluramine
  - 中度（Moderate）：epinephrine、morphine、乙醯水楊酸（aspirin）、cimetidine 等
  - 輕微（Minor）：famotidine、ranitidine、rabeprazole 等
- 使用於兒童與嬰兒（排名第 1 的預測）有額外的安全性顧慮。

仿單警語與禁忌資料尚缺，請參考原廠仿單。

---

## 結論與下一步

**決策：**
- 嬰兒良性陣發性斜頸（排名 1）及排名 4–10 的各項預測：**Hold**
- 強迫症：**Proceed with Guardrails**（作為研究性問題）

**理由：**
- 排名前列的預測分數雖高（>0.9960），但除強迫症與懼曠症外，其餘全無臨床試驗與文獻，僅屬計算推論，且多項預測缺乏合理機轉。
- 強迫症有 1 項雙盲對照試驗（限於難治型的加成治療）、1 項 Phase 4 試驗與開放標籤研究，但樣本小，未達 Phase 3 RCT 的標準，證據等級為 L2。

**若要推進需要：**
- 補齊作用機轉資料與香港仿單的警語及禁忌
- 設計較大規模、以 duloxetine 單用或加成治療強迫症的隨機對照試驗，並與 SSRI 比較
- 確認難治型強迫症加成治療的劑量與監測計畫，並針對高血壓、肝病、血清素症候群風險與重大藥物交互作用擬定管理措施
- 排名第 1 的預測需先有機轉或前臨床依據，再考慮兒童族群的安全性評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

