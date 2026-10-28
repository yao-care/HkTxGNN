---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 644
evidence_level: L5
indication_count: 10
monitor_inn: "OMALIZUMAB"
predicted_indications: ["bronchitis", "atopic eczema", "obstructive lung disease", "dermatitis", "bronchial neoplasm (disease)", "acne keloid", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease"]
last_modified_at: 2026-10-28
description: "Omalizumab：預測新適應症為支氣管炎（證據等級 L5）。原適應症：氣喘、過敏性氣喘、慢性蕁麻疹"
---

# Omalizumab
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

## Omalizumab：從氣喘到支氣管炎
{: .text-alpha }

## 一句話總結

Omalizumab 是一種抗 IgE 單株抗體，知識圖譜記錄的原適應症包括氣喘與慢性自發性蕁麻疹。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，但目前僅有 **2 個間接相關的臨床試驗**和 **7 篇文獻**，且沒有任何研究直接針對支氣管炎本身，證據偏弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 氣喘、過敏性氣喘、慢性蕁麻疹（來自知識圖譜的記錄關聯；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 支氣管炎 |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 8 張／共 8 張） |
| 許可證數 | 8 張（有效 8 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Omalizumab 是一種與游離 IgE 結合的人源化單株抗體，可降低游離 IgE 並減少 FcεRI 介導的肥大細胞與嗜鹼性球活化，這與過敏性氣道發炎相關。

支氣管炎並非獨立的 IgE 介導疾病。現有證據多與過敏性氣喘及氣喘合併慢性阻塞性肺病（COPD）重疊有關，而不是支氣管炎本身。模型的高分來自 TxGNN 模型（深度學習），可能反映模型學到的支氣管炎與氣喘等相關疾病之間的相似性，而不是生物學證據。

唯一較貼近的情境是「持續性嗜酸性球支氣管炎」合併氣喘的患者，但該試驗規模極小，且人群並非一般支氣管炎。

## 臨床試驗證據

這兩個試驗都沒有直接研究支氣管炎，相關性為間接。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | 完成 | 11 | 雙盲安慰劑對照，評估 Omalizumab 對氣喘合併嗜酸性球支氣管炎患者減少類固醇用量的效果；樣本極小，人群不等同於一般支氣管炎 |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | 完成 | 382 | QGE031 用於慢性自發性蕁麻疹的劑量探索試驗；與支氣管炎關聯薄弱 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Cohort | Curr Med Res Opin | 合併分析 Omalizumab 在過敏性氣喘兒童的安全性 |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohort | Postepy Dermatol Alergol | 中老年重度過敏性氣喘合併 COPD 重疊患者使用生物製劑可能有益 |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | Omalizumab 在氣喘的核准與上市後經驗 |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | 吸菸相關氣道疾病（含慢性支氣管炎）合併氣喘的治療挑戰 |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui | 氣喘或慢性支氣管炎患者的術前管理，提及 Omalizumab 可用於重度過敏性氣喘 |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergol Immunopathol | 單株抗體在小兒預防與治療的應用概述 |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case Report | J Investig Allergol Clin Immunol | 支氣管熱成形術後罕見的塑型性支氣管炎病例 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68678 | XOLAIR 預充式注射器 150MG/ML | 注射劑 | 資料未載明 |
| HK-68676 | XOLAIR 預充式注射筆 150MG/ML | 注射劑 | 資料未載明 |
| HK-65301 | XOLAIR 預充式注射器 150MG/ML | 注射劑 | 資料未載明 |
| HK-68679 | XOLAIR 預充式注射器 300MG/2ML | 注射劑 | 資料未載明 |
| HK-68680 | XOLAIR 預充式注射器 75MG/0.5ML | 注射劑 | 資料未載明 |

以上為 8 張許可證中的前 5 張，全部為單一成分、有效狀態。

## 安全性考量

- **藥物交互作用**：共查得 8 筆。其中中度為 Omacetaxine mepesuccinate；輕度包括硫酸鋅、醋酸鋅、葡萄糖酸鋅、氯化鋅、紫錐花（Echinacea）與維生素 E。另有藥理資料指出其作用標的為 IgE 重鏈（IGHE）。

其他警語與禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何研究直接針對支氣管炎，僅有間接相關的小型試驗與氣喘文獻，因此證據等級為 L5。
- 高預測分數來自 TxGNN 模型（深度學習），可能反映模型學到的支氣管炎與氣喘等相關疾病之間的相似性，而非獨立的療效訊號，也不是生物學證據。

**若要推進需要：**
- 釐清目標族群（例如嗜酸性球支氣管炎或有明確過敏／第二型發炎表型者），而非一般支氣管炎。
- 針對該族群設計有對照的臨床研究。
- 取得詳細作用機轉資料與香港仿單的警語及禁忌症。
- 補齊香港許可證的核准適應症文字。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

