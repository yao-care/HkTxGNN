---
layout: default
title: Darunavir
parent: 僅模型預測 (L5)
nav_order: 247
evidence_level: L5
indication_count: 4
monitor_inn: "DARUNAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-28
description: "Darunavir：預測新適應症為Feline acquired immunodeficiency syndrome（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Darunavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Darunavir: Feline acquired immunodeficiency syndrome
{: .text-alpha }

## 一句話總結

Darunavir 是 HIV 蛋白酶抑制劑，知識圖譜中記錄的原適應症為 HIV 感染與愛滋病。
TxGNN 模型預測它可能對**猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)** 有效，但目前僅有 **4 篇非人靈長類前臨床文獻**，且無任何臨床試驗，屬於研究假說階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Feline acquired immunodeficiency syndrome |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 17 張／共 17 張） |
| 許可證數 | 17 張（有效 17 張） |
| 建議決策 | Hold（列為研究問題） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 darunavir 為 HIV-1 蛋白酶抑制劑，其在 HIV 感染中的角色已廣為人知。

SIV 是與 HIV 親緣相近的慢病毒，其蛋白酶與 HIV 蛋白酶有一定相似性，因此 HIV 蛋白酶抑制劑可能作為猴子抗病毒療法的組成。但這屬於推論：檢索到的文獻是以多藥併用的抗反轉錄病毒療法（cART）為主，無法分離出 darunavir 單藥的貢獻。

需要注意，猴 SIV 模型本身是 HIV 研究的替代模型，因此對人類的新增再利用價值有限。TxGNN 的高分很可能反映的是與 HIV/AIDS 在網絡上的鄰近性，而非已驗證的活性。

另外三個預測（貓愛滋病、一種罕見神經發展障礙、已廢止的家族性複合型高脂血症）均無試驗與文獻支持，也沒有明確的機轉關聯，其中高脂血症反而與蛋白酶抑制劑常見的血脂異常副作用相衝突。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下列文獻均為非人靈長類前臨床研究，以併用療法為主，並非 darunavir 單藥的直接研究。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | 前臨床（獼猴） | PloS one | 在 SIV 感染的中國恆河猴中，研究 cART 併用 HDAC 抑制劑 SAHA 對病毒庫的影響 |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | 前臨床（猴） | AIDS | 金製劑 auranofin 併用 ART，可限制病毒庫，並在停藥後抑制病毒量 |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | 前臨床（獼猴） | PLoS pathogens | 高強度多藥 ART 可達長期病毒抑制，並限制猴愛滋模型中的病毒庫 |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | 前臨床（獼猴） | AIDS research and human retroviruses | 比較兩種共同配方的注射型 cART 方案在 SIV 感染獼猴中的效果 |

## 香港上市資訊

香港共有 17 張單一成分的有效許可證，以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-58980 | PREZISTA TAB 600MG（Johnson & Johnson） | 未提供 | 未提供 |
| HK-63272 | PREZISTA TABLETS 800MG（Johnson & Johnson） | 未提供 | 未提供 |
| HK-66733 | DARUNAVIR SANDOZ TABLETS 800MG（Sandoz） | 未提供 | 未提供 |
| HK-67175 | DARUNAVIR KRKA TABLETS 600MG（Sino Pacific） | 未提供 | 未提供 |
| HK-66782 | DAVARINO TABLETS 600MG（I & C） | 未提供 | 未提供 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：肝衰竭、肝病、膽囊疾病、高血糖、肝硬化、糖尿病、糖尿病酮酸中毒、慢性 C 型肝炎、C 型肝炎、慢性 B 型肝炎、高三酸甘油脂血症、血友病。
- **藥物交互作用**：共查得 100 筆，以下為部分例子。
  - 重度：Cisapride。
  - 中度：降血糖藥（acarbose、metformin、pioglitazone、alogliptin、saxagliptin、canagliflozin、dapagliflozin、chlorpropamide）、皮質類固醇（hydrocortisone、dexamethasone、betamethasone、budesonide、triamcinolone）、clarithromycin、aprepitant。

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一有文獻的預測（SIV 感染）僅有前臨床併用療法研究，無法歸因於 darunavir，且動物模型本身即為 HIV 的替代模型，對人類的再利用價值有限。
- 其餘預測缺乏試驗、文獻與合理機轉，其中兩項（貓愛滋病、罕見神經發展障礙）超出人類再利用範疇或缺乏關聯，一項為已廢止的疾病概念。

**若要推進需要：**
- 取得 darunavir 的作用機轉資料與香港仿單的警語、禁忌內容。
- 若要驗證 SIV 方向，需有 darunavir 單藥或明確納入該藥的對照研究。
- 評估各預測疾病是否屬於人類用藥的合理再利用目標。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

