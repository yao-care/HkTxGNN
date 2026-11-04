---
layout: default
title: Omalizumab
parent: 僅模型預測 (L5)
nav_order: 644
evidence_level: L5
indication_count: 9
monitor_inn: "OMALIZUMAB"
predicted_indications: ["bronchitis", "atopic eczema", "dermatitis", "bronchial neoplasm (disease)", "acne keloid", "acrodermatitis chronica atrophicans", "hydroa vacciniforme, familial", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease"]
last_modified_at: 2026-11-04
description: "Omalizumab：預測新適應症為支氣管炎 (bronchitis)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Omalizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Omalizumab: 支氣管炎 (bronchitis)
{: .text-alpha }

## 一句話總結

Omalizumab 是一種針對免疫球蛋白 E (IgE) 的人源化單株抗體。
TxGNN 模型預測它可能對**支氣管炎 (bronchitis)** 有效，但目前沒有已發表的研究直接支持 omalizumab 用於支氣管炎，證據等級為 **L5**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 支氣管炎 (bronchitis) |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 8 張／共 8 張） |
| 許可證數 | 8 張（有效 8 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Omalizumab 與游離 IgE 結合，降低其濃度，並減少 FcεRI 在肥大細胞與嗜鹼性球上的表現，進而減輕過敏性氣道發炎。目前缺乏詳細的作用機轉資料（DrugBank 未提供），以上為已知的藥理描述。

支氣管炎並不是以 IgE 為主導的獨立疾病，機轉上的連結相當間接。模型給出的高分，較可能反映疾病之間在模型中的相近性，而不是直接的臨床證據。

目前唯一與支氣管炎相關的試驗規模很小，且研究對象並未明確界定為支氣管炎病人，因此不足以支持這項預測。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | 完成 | 11 | 安慰劑對照試驗，探討 omalizumab 對持續性嗜酸性球支氣管炎合併氣喘病人的減少類固醇用量效果。樣本數極小，且發表結果顯示 omalizumab 的效果可能不足 |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2 | 完成 | 382 | 針對慢性自發性蕁麻疹的劑量探索研究，與支氣管炎關聯薄弱 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Review | Clin Rev Allergy Immunol | 回顧 omalizumab 的核准與上市後經驗，主要針對過敏性氣喘 |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Review | Expert Opin Pharmacother | 討論吸菸相關氣道疾病（含慢性支氣管炎）對氣喘病人的影響，並非 omalizumab 專門研究 |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Cohort | Curr Med Res Opin | 兒童過敏性氣喘使用 omalizumab 的安全性合併分析 |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case report | J Investig Allergol Clin Immunol | 支氣管熱成形術後發生塑型性支氣管炎的罕見病例 |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Review | Masui | 氣喘或慢性支氣管炎病人的術前管理 |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Review | Allergol Immunopathol | 單株抗體在兒科預防與治療的應用概述 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68678 | XOLAIR 預充式注射器 150MG/ML | 注射劑 | 資料未載明 |
| HK-68676 | XOLAIR 預充式注射筆 150MG/ML | 注射劑 | 資料未載明 |
| HK-65301 | XOLAIR 預充式注射器 150MG/ML | 注射劑 | 資料未載明 |
| HK-68679 | XOLAIR 預充式注射器 300MG/2ML | 注射劑 | 資料未載明 |
| HK-68680 | XOLAIR 預充式注射器 75MG/0.5ML | 注射劑 | 資料未載明 |

## 安全性考量

- **藥物交互作用**：已查詢到 8 筆。其中 Omacetaxine mepesuccinate 為中度 (Moderate) 交互作用；鋅鹽類（硫酸鋅、醋酸鋅、葡萄糖酸鋅、氯化鋅）、紫錐花 (Echinacea) 與維生素 E 為輕度 (Minor)。另有一筆為藥理資料，標的為免疫球蛋白重鏈恆定區 ε (IGHE)，即 IgE。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有已發表研究支持 omalizumab 用於支氣管炎，現有試驗與文獻皆屬間接相關，因此證據等級為 L5。TxGNN 的高分不能取代臨床證據。

**若要推進需要：**
- 針對明確定義之支氣管炎族群（例如嗜酸性球支氣管炎）的對照試驗
- 作用機轉資料，以及支氣管炎中 IgE 角色的相關佐證
- 取得香港原廠仿單，完成警語與禁忌症的安全性審查

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

