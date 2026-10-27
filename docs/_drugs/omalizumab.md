---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 644
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Omalizumab：預測新適應症為支氣管炎 (Bronchitis)（證據等級 L5）。原適應症：氣喘、內因性氣喘、過敏性氣喘、特發性蕁麻疹"
monitor_inn: "OMALIZUMAB"
predicted_indications: ["bronchitis", "atopic eczema", "obstructive lung disease", "dermatitis", "bronchial neoplasm (disease)"]
---

# Omalizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Omalizumab 是抗 IgE 單株抗體，原本用於氣喘（含過敏性氣喘）與特發性蕁麻疹。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，但直接證據很薄弱：目前僅有 **2 個臨床試驗**（相關性皆為 C 級）和 **7 篇文獻**，多數內容其實是在談氣喘。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 氣喘、內因性氣喘、過敏性氣喘、特發性蕁麻疹（來自知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.999% |
| 證據等級 | L4（僅有間接的機轉與氣喘相關研究，無支氣管炎直接證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Omalizumab 可結合游離 IgE，降低 FcεRI 介導的肥大細胞與嗜鹼性球活化，因此對過敏性氣道發炎有效，這也是它用於過敏性氣喘的基礎。

氣喘與支氣管炎同屬呼吸道疾病，且部分患者（例如氣喘合併嗜酸性球性支氣管炎，或氣喘—COPD 重疊）同時具有過敏性氣道發炎。因此在這類特定表型中，抗 IgE 治療理論上可能有幫助。

但需要留意：一般慢性支氣管炎（如吸菸相關）並非 IgE 驅動的疾病，機轉與支氣管炎的連結是間接的。高預測分數可能反映的是與氣喘在網絡上的相近性，而非實際療效。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | 完成 | 11 | 在氣喘合併嗜酸性球性支氣管炎患者中，評估加用 Omalizumab 是否能減少 prednisone 用量（安慰劑對照）；樣本極小，結果未提供 |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | 完成 | 382 | QGE031 用於慢性自發性蕁麻疹的劑量探索試驗（有 Omalizumab 作為對照）；與支氣管炎無直接關聯 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | 安全性合併分析 | Curr Med Res Opin | 評估 Omalizumab 在過敏性氣喘兒童的安全性 |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Cohort | Postepy Dermatol Alergol | 中老年重度過敏性氣喘—COPD 重疊患者使用生物製劑可能有幫助 |
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | 回顧 Omalizumab 在氣喘的核准與上市後經驗 |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | 討論吸菸相關氣道疾病（含慢性支氣管炎）合併氣喘的治療挑戰 |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergol Immunopathol | 單株抗體在兒科預防與治療的應用概述 |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui | 支氣管氣喘或慢性支氣管炎患者的術前處置，提及 Omalizumab 可用於重度過敏性氣喘 |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case report | J Investig Allergol Clin Immunol | 支氣管熱成形術後發生塑型性支氣管炎的罕見病例 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68678 | XOLAIR SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 150MG/ML | 注射劑 | 未提供 |
| HK-68676 | XOLAIR SOLUTION FOR INJECTION IN PRE-FILLED PEN 150MG/ML | 注射劑 | 未提供 |
| HK-65301 | XOLAIR SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 150MG/ML | 注射劑 | 未提供 |
| HK-68679 | XOLAIR SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 300MG/2ML | 注射劑 | 未提供 |
| HK-68680 | XOLAIR SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 75MG/0.5ML | 注射劑 | 未提供 |

（共 8 張有效許可證，皆由 Novartis Pharmaceuticals (HK) Limited 持有；此處僅列出 5 張。）

## 安全性考量

- **藥物交互作用**：共查得 8 筆。多數為輕微（Minor）等級，包括鋅製劑（硫酸鋅、醋酸鋅、葡萄糖酸鋅、氯化鋅）、紫錐花、維生素 E；另有 1 筆中度（Moderate）：Omacetaxine mepesuccinate。

警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 與支氣管炎直接相關的證據僅有一個 11 人的小型試驗（針對氣喘合併嗜酸性球性支氣管炎），文獻多為氣喘相關，並非支氣管炎的療效證據。
- 一般慢性支氣管炎並非 IgE 驅動，高 TxGNN 分數可能只是反映與氣喘的網絡相近性。

**若要推進需要：**
- 明確界定目標族群（例如過敏性或嗜酸性球性支氣管炎、氣喘—COPD 重疊表型），而非泛指支氣管炎
- 取得 NCT02049294 的結果資料，並設計針對該表型的對照試驗
- 補齊作用機轉資料（MOA）
- 取得香港仿單中的警語、禁忌症與核准適應症，完成安全性篩選
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

