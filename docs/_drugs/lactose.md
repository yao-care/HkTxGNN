---
layout: default
title: Lactose
parent: 僅模型預測 (L5)
nav_order: 503
evidence_level: L5
indication_count: 10
monitor_inn: "Lactose"
predicted_indications: ["esophageal varices with bleeding", "esophageal varices without bleeding", "varicose disease", "Steel syndrome", "cystinosis", "growth hormone insensitivity syndrome with immune dysregulation 2, autosomal dominant", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Immunoerythromyeloid hypoplasia", "familial apolipoprotein C-II deficiency", "hypophosphatasia"]
last_modified_at: 2026-10-28
description: "Lactose：預測新適應症為食道靜脈曲張伴出血（證據等級 L5）。原適應症：乳糖不耐症"
---

# Lactose
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

## Lactose：從乳糖不耐症到食道靜脈曲張伴出血
{: .text-alpha }

## 一句話總結

Lactose（乳糖）是一種雙醣，知識圖譜中記錄的相關情況為乳糖不耐症。
TxGNN 模型預測它可能對**食道靜脈曲張伴出血 (Esophageal Varices with Bleeding)** 有關，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 乳糖不耐症（知識圖譜中記錄的關係，非香港許可證核准適應症） |
| 預測新適應症 | 食道靜脈曲張伴出血 |
| TxGNN 預測分數 | 0.9993 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。乳糖是一種常見的膳食雙醣，也是藥品常用的賦形劑。香港的 5 張許可證在本報告所整理的資料中都沒有核准適應症文字，所以無法從許可證判斷乳糖本身的療效用途。

乳糖與食道靜脈曲張伴出血之間，沒有已確立的機轉關聯。唯一能想到的間接聯想是乳果糖（lactulose，一種相關的雙醣）用於肝硬化的肝性腦病變，但那是不同的化合物，不能作為乳糖有效的證據。

高分預測來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據。「出血」與「未出血」兩個變體的分數同為 0.9993，也支持這一點，兩者並非各自獨立的證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

下列 5 張許可證均為單一成分、有效狀態。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43329 | MICROGYNON 30 ED TAB | 未提供 | 未提供 |
| HK-56563 | YAZ TAB | 未提供 | 未提供 |
| HK-68562 | ALYSSA TABLETS | 未提供 | 未提供 |
| HK-65968 | MEDIAZ TABLETS | 未提供 | 未提供 |
| HK-59784 | QLAIRA TAB | 未提供 | 未提供 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他預測適應症（供參考）

TxGNN 另外預測了下列疾病，均無臨床試驗或文獻支持，證據等級皆為 L5，建議皆為 Hold，且未發現合理的機轉關聯。

| 排名 | 疾病 | TxGNN 分數 |
|------|------|-----------|
| 2 | 食道靜脈曲張不伴出血 | 0.9993 |
| 3 | 靜脈曲張疾病 | 0.9985 |
| 4 | Steel 症候群 | 0.9972 |
| 5 | 胱胺酸貯積症 (Cystinosis) | 0.9971 |
| 6 | 伴免疫失調的生長激素不敏感症候群 2 型（顯性遺傳） | 0.9963 |
| 7 | 核 DNA 異常所致粒線體氧化磷酸化疾病 | 0.9957 |
| 8 | 免疫紅血球骨髓發育不全 | 0.9952 |
| 9 | 家族性載脂蛋白 C-II 缺乏症 | 0.9947 |
| 10 | 低磷酸酶症 (Hypophosphatasia) | 0.9942 |

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何臨床試驗或文獻直接研究乳糖用於此疾病，也找不到合理的機轉，證據等級為 L5。
- 安全性資料（仿單警語與禁忌）尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌與核准適應症。
- 補充乳糖的作用機轉資料（例如查詢 DrugBank）。
- 以文獻回顧確認乳糖與食道靜脈曲張之間是否有任何直接研究；若無，不建議投入進一步資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

