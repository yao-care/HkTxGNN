---
layout: default
title: Propylene Glycol
parent: 僅模型預測 (L5)
nav_order: 741
evidence_level: L5
indication_count: 10
monitor_inn: "PROPYLENE GLYCOL"
predicted_indications: ["bronchitis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "nuclear senile cataract", "cortical cataract", "senile cataract", "diabetic cataract", "diabetes mellitus type 2 associated cataract", "mature cataract", "craniostenosis cataract"]
last_modified_at: 2026-10-28
description: "Propylene Glycol：預測新適應症為支氣管炎 (Bronchitis)（證據等級 L5）。原適應症：乾眼症、乾眼病"
---

# Propylene Glycol
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

## Propylene Glycol：從乾眼症到支氣管炎
{: .text-alpha }

## 一句話總結

Propylene Glycol（丙二醇）是眼用潤滑液中常見的成分，知識圖譜中記錄的相關用途為乾眼症與乾眼病（xerophthalmia）。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，但目前**沒有臨床試驗**，僅有 **3 篇間接文獻**，且文獻內容多屬電子菸的呼吸道風險，並非治療證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 乾眼症、乾眼病（知識圖譜中記錄的關聯，香港許可證未載明適應症文字） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，丙二醇在眼用製劑中主要作為保濕劑與溶劑，用於緩解乾眼不適，並沒有已知的藥理機轉可延伸到支氣管炎。

坦白說，這個預測的合理性很低。檢索到的文獻中，丙二醇是電子菸煙液的載體，被視為潛在的呼吸道刺激物，這是安全性疑慮，而不是治療依據。TxGNN 模型（深度學習）給出的高分，可能反映的是模型學到的相關疾病之間的相似性，而不是生物學證據。

其他排名較前的預測（糖尿病視網膜病變、各型白內障等）同樣只有模型預測或間接證據，沒有任何一項顯示丙二醇本身具療效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | 討論長期使用電子菸是否導致肺部疾病，與吸菸引起的 COPD（含慢性支氣管炎）作對照 |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | 電子菸煙液與氣溶膠含有呼吸道刺激物，可能與氣喘惡化有關 |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | 前臨床（動物） | Respir Res | 槲皮素在 COPD 小鼠模型中降低肺部發炎，與丙二醇無直接關係 |

以上文獻均未直接研究丙二醇治療支氣管炎。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59636 | SYSTANE ULTRA LUBRICANT EYE DROPS | 未載明 | 未載明 |
| HK-61280 | SYSTANE ULTRA LUBRICANT EYE DROPS PRESERVATIVE FREE | 未載明 | 未載明 |
| HK-67320 | SYSTANE ULTRA LUBRICANT EYE DROPS | 未載明 | 未載明 |

三張許可證皆為單一成分、有效狀態，持證商為 ALCON HONG KONG LTD。

---

## 安全性考量

安全性資訊請參考原廠仿單。

另外，本報告彙整的文獻提示，丙二醇作為電子菸載體時可能刺激呼吸道，若考慮吸入途徑須特別留意。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 支氣管炎的預測僅有模型分數，沒有臨床試驗，文獻也只涉及丙二醇的呼吸道刺激風險，因此證據等級為 L5。
- 丙二醇的已知角色是保濕劑與溶劑，沒有可支持治療支氣管炎的機轉。

**若要推進需要：**
- 取得作用機轉資料，確認是否存在任何抗發炎或黏液調節作用
- 針對吸入途徑進行呼吸道安全性評估
- 取得香港原廠仿單，補齊警語與禁忌資訊
- 在有直接針對支氣管炎的研究出現之前，不建議投入進一步開發
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

