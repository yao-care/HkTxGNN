---
layout: default
title: Etravirine
parent: 僅模型預測 (L5)
nav_order: 355
evidence_level: L5
indication_count: 8
monitor_inn: "ETRAVIRINE"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "fibroma of prostate", "Brenner tumor", "benign reproductive system neoplasm", "benign prostate phyllodes tumor", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-30
description: "Etravirine：預測新適應症為猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)（證據等級 L5）。原適應症：本報告彙整的香港許可證資料中未載明核准適應症"
---

# Etravirine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Etravirine：從 HIV 感染到猿猴免疫缺陷病毒感染
{: .text-alpha }

## 一句話總結

Etravirine 是一種非核苷類逆轉錄酶抑制劑（NNRTI），知識圖譜記錄的原適應症為 HIV 感染與愛滋病。
TxGNN 模型預測它可能對**猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)** 有效，但目前**沒有臨床試驗**，只有 **1 篇間接的前臨床文獻**，證據相當薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本報告彙整的香港許可證資料中未載明核准適應症；知識圖譜記錄的相關關係為 HIV 感染、愛滋病 |
| 預測新適應症 | 猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的藥物分類，Etravirine 屬於 NNRTI，作用是抑制 HIV-1 逆轉錄酶，阻止病毒複製。

SIV 與 HIV 同屬慢病毒，因此在概念上存在關聯。不過，SIV 的逆轉錄酶性質上較接近 HIV-2，對 NNRTI 天生較不敏感，所以任何活性都必須另行驗證。

TxGNN 模型（深度學習）給出的高分，可能反映模型學到的相關疾病之間的相似性（例如與 HIV 原適應症的相似性），並非生物學證據。此外，SIV 感染主要是動物模型疾病，除作為前臨床模型外，沒有直接的人類臨床意義。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | 前臨床（體外） | Molecular Pharmaceutics | 奈米粒子載體的抗病毒藥物組合可協同抑制 HIV 的游離病毒與細胞間傳播；研究對象為 HIV，並非 SIV，屬間接證據 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61470 | INTELENCE TAB 200MG | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關係**（非仿單內容）：慢性 C 型肝炎病毒感染、C 型肝炎病毒感染、慢性 B 型肝炎病毒感染、周邊神經系統疾病、周邊神經病變。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 中度：Rabeprazole、Omeprazole、Cimetidine、Clarithromycin、Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Aprepitant、Pioglitazone、Saxagliptin、Linagliptin、Glimepiride、Chlorpropamide、Metronidazole 等
  - 輕微：Ranitidine

其餘安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何直接研究猿猴免疫缺陷病毒感染的臨床試驗或文獻，唯一的文獻是 HIV 的間接前臨床研究，因此證據等級為 L5。
- SIV 逆轉錄酶對 NNRTI 天生較不敏感，且此疾病為動物模型，缺乏人類轉譯價值。

**若要推進需要：**
- 在 SIV 感染模型中進行 Etravirine 的體外與動物活性實驗，確認逆轉錄酶敏感性
- 釐清此預測在研究上的實際用途（例如僅作為前臨床模型），再決定是否值得投入
- 取得詳細的作用機轉資料，並下載香港衛生署的仿單以補足警語與禁忌症

---

**附註：本次其他預測適應症（皆建議 Hold，證據等級 L5）**

| 預測適應症 | TxGNN 分數 | 說明 |
|-----------|-----------|------|
| 貓後天免疫缺乏症候群 | 0.9998 | 貓免疫缺陷病毒的逆轉錄酶對 NNRTI 敏感性差；屬獸醫適應症，無文獻與試驗 |
| 伴共濟失調步態、無語言及皮質白質減少的神經發展障礙 | 0.9997 | 未發現機轉關聯，分數可能反映 TxGNN 模型（深度學習）學到的相關疾病間相似性，並非生物學證據 |
| 前列腺纖維瘤 | 0.9972 | 無機轉依據，也無證據 |
| Brenner 瘤 | 0.9970 | 無機轉依據，也無證據 |
| 良性生殖系統腫瘤 | 0.9970 | 疾病類別過於廣泛，高分可能來自本體論鄰近性 |
| 良性前列腺葉狀腫瘤 | 0.9965 | 無機轉依據，也無證據 |
| 已廢棄之家族性複合型高脂血症 | 0.9964 | 該術語已廢棄，且無降脂機轉依據 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

