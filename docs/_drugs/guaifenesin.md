---
layout: default
title: Guaifenesin
parent: 僅模型預測 (L5)
nav_order: 430
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "GUAIFENESIN"
predicted_indications: ["nasal cavity disease", "faucial diphtheria", "cervical disc degenerative disorder", "papillary conjunctivitis"]
description: "Guaifenesin：預測新適應症為鼻腔疾病 (nasal cavity disease)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Guaifenesin
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

## Guaifenesin: 鼻腔疾病 (nasal cavity disease)
{: .text-alpha }

## 一句話總結

Guaifenesin（癒創甘油醚）是一種祛痰劑，原本用於過敏性鼻炎、血管運動性鼻炎、咽炎、感冒等上呼吸道症狀。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇文獻**（回顧性質）間接提及，證據相當有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 鼻腔疾病 (nasal cavity disease) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Guaifenesin 是祛痰劑，作用是稀釋並促進氣道黏液排出。鼻腔疾病與其已知的鼻炎、感冒、鼻咽炎等適應症高度相關，因此機轉上可能適用於鼻腔疾病中的黏液分泌問題。

需要注意的是，0.9998 的高分來自 TxGNN 模型（深度學習），可能反映模型從相關疾病間學到的相似性，而非生物學證據，也不代表出現了新的作用機轉。因此這個預測較像是既有用途的延伸，而不是真正的新用途。其他排名較低的預測（如咽白喉、頸椎椎間盤退化、乳頭狀結膜炎）同樣缺乏可信的機轉連結，多半只是模型學到的相關疾病相似性，並非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12487405](https://pubmed.ncbi.nlm.nih.gov/12487405/) | 2002 | Review | Logopedics, Phoniatrics, Vocology | 探討聲樂工作者隱性呼吸道過敏的治療策略；一般避免使用抗組織胺，含 Guaifenesin 的鼻充血緩解劑可能有幫助，類固醇對常年性過敏較有用 |

此文獻為針對嗓音使用者的回顧，僅間接提及 Guaifenesin，不能視為直接證據。

## 香港上市資訊

香港共有 20 張有效的單方許可證，以下列出 5 張主要者（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-62004 | MUCINEX EXTENDED-RELEASE TABLETS 600MG | Reckitt Benckiser Hong Kong Ltd |
| HK-63897 | MUCINEX EXTENDED-RELEASE TABLETS 1200MG | Reckitt Benckiser Hong Kong Ltd |
| HK-51114 | ROBITUSSIN EX SYRUP 20MG/ML | Haleon Hong Kong Limited |
| HK-36928 | BREACOL SYRUP | A. Menarini Hong Kong Limited |
| HK-47305 | GUFENSIN TAB 200MG | Christo Pharm Ltd |

## 安全性考量

知識圖譜中列出的相關禁忌疾病（非仿單內容，僅供參考）包括：高血壓、肝衰竭／肝病、癲癇、慢性阻塞性肺病、消化性潰瘍、腎臟疾病、胰臟炎、血小板低下、腎上腺皮質功能不全、甲狀腺功能低下、焦慮與精神病性疾患、紫質症、發炎性腸病等。這些多半來自含有其他成分的複方資料，需與實際單方仿單核對。

藥物交互作用查詢未找到資料。其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，文獻僅 1 篇間接提及的回顧，且缺乏作用機轉資料；高分主要來自與既有適應症的重疊，不代表有新的療效證據。

**若要推進需要：**
- 補齊 Guaifenesin 作用機轉（MOA）資料
- 取得並解析香港衛生署仿單，確認核准適應症、警語與禁忌
- 釐清「鼻腔疾病」的具體疾病範圍，並與既有鼻炎適應症區分，確認是否真屬新適應症
- 搜尋並評估 Guaifenesin 用於鼻腔黏液相關症狀的對照研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

