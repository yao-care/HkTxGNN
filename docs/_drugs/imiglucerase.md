---
layout: default
title: Imiglucerase
parent: 僅模型預測 (L5)
nav_order: 462
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
monitor_inn: "Imiglucerase"
predicted_indications: ["Hurler syndrome", "Scheie syndrome", "benign neoplasm of adrenal gland", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease"]
description: "Imiglucerase：預測新適應症為Hurler 症候群 (Hurler syndrome)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Imiglucerase
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

## Imiglucerase: Hurler 症候群 (Hurler syndrome)
{: .text-alpha }

## 一句話總結

Imiglucerase 是重組人類葡萄糖腦苷脂酶（glucocerebrosidase），原本用於戈謝氏症（Gaucher disease）的酵素替代療法。
TxGNN 模型預測它可能對 **Hurler 症候群 (Hurler syndrome)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇**一般性的溶小體儲積症酵素替代療法回顧文獻，證據非常薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Hurler 症候群 (Hurler syndrome) |
| TxGNN 預測分數 | 0.9952 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Imiglucerase 是重組葡萄糖腦苷脂酶，用於補充戈謝氏症患者缺乏的酵素，分解累積的葡萄糖腦苷脂（glucosylceramide）。

Hurler 症候群（黏多醣症 I 型，MPS I）則是 α-L-艾杜糖醛酸酶（alpha-L-iduronidase）缺乏所致，累積的受質是醣胺聚醣（glycosaminoglycans）。Imiglucerase 作用的受質與此完全不同，**無法取代缺乏的酵素**，因此沒有直接的機轉依據。兩者唯一的關聯是「同屬溶小體儲積症、皆可採酵素替代療法」這個類別概念。

高預測分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非真實的生物學證據。MPS I 已有專一的核准酵素替代療法（laronidase）。

同一份回顧文獻也用來支持 Scheie 症候群（MPS I 的較輕型）的預測，其限制相同。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de medecine interne | 回顧溶小體儲積症的酵素替代療法發展，從戈謝氏症的 alglucerase 到重組 imiglucerase，以及法布瑞氏症等；屬間接證據，未直接針對 Hurler 症候群 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60392 | CEREZYME POWDER FOR CONCENTRATE FOR SOLUTION FOR INF 400IU | 未載明（輸注濃縮液用粉劑） | 未載明 |

製造商為 SANOFI HONG KONG LIMITED。

## 安全性考量

- **藥物交互作用**：資料庫查得 1 筆中度（Moderate）交互作用，對象為 **Miglustat**（來源：DDInter）。

其他警語與禁忌症資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- Imiglucerase 與 Hurler 症候群缺乏的酵素不同，沒有機轉依據，也沒有任何臨床試驗，僅有一篇間接的回顧文獻。高預測分數可能只是模型的網路鄰近性假象。
- 此疾病已有專一的酵素替代療法，沒有明顯的未滿足需求支持以 imiglucerase 取代。

**若要推進需要：**
- 取得 Imiglucerase 作用機轉的完整資料
- 前臨床證據，證明其對 α-L-艾杜糖醛酸酶缺乏的受質有任何作用（目前機轉上不成立）
- 取得香港仿單的警語與禁忌症資料
- 如需在其他預測適應症中尋找方向，現有證據以「伴隨骨骼表現的溶小體儲積症」最多，但該文獻幾乎全是針對原適應症戈謝氏症，並非真正的新適應症
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

