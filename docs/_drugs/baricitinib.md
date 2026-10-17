---
layout: default
title: Baricitinib
parent: 僅模型預測 (L5)
nav_order: 95
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Baricitinib：預測新適應症為Colobomatous Microphthalmia-Rhizomelic Dysplasia 症候群（證據等級 L5）。原適應症：類風濕性關節炎 (Rheumatoid Arthritis)"
monitor_inn: "BARICITINIB"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Baricitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Baricitinib：從類風濕性關節炎到 Colobomatous Microphthalmia-Rhizomelic Dysplasia 症候群

## 一句話總結

Baricitinib 是一種口服藥物，原本用於治療類風濕性關節炎。
TxGNN 模型預測它可能對 **Colobomatous Microphthalmia-Rhizomelic Dysplasia 症候群**有效（預測分數極高，99.94%）。
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| 預測新適應症 | Colobomatous Microphthalmia-Rhizomelic Dysplasia 症候群 |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

另一個預測適應症為 Brachydactyly-Syndactyly 症候群（分數 99.94%，同為 L5、Hold），同樣沒有臨床試驗或文獻支持。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Baricitinib 已知屬於 JAK1/JAK2 抑制劑，透過調節 JAK-STAT 訊號傳遞發揮免疫調節作用，這也是它用於類風濕性關節炎的基礎。

然而，這個新適應症是一種罕見的發育異常症候群（眼部缺損、小眼球、肢根型骨骼發育不良）。以現有資料，無法建立 JAK-STAT 訊號與此疾病之間的生物學連結。先天性發育異常通常源自胚胎期的發育模式缺陷，一般不預期能被免疫調節藥物逆轉。

因此，這個預測較可能反映知識圖譜中的網路鄰近性假象，而非真正的藥理作用。目前只能視為產生假說的訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65664 | OLUMIANT TABLETS 4MG | 錠劑 | 資料未提供 |
| HK-65663 | OLUMIANT TABLETS 2MG | 錠劑 | 資料未提供 |

兩張許可證皆為單方、有效，持證商為 ELI LILLY ASIA, INC.。

## 安全性考量

- **藥物交互作用**：共查得 100 筆交互作用，以下為部分主要項目：
  - **Major（重大）**：Hydrocortisone、Triamcinolone、Betamethasone、Budesonide、Dexamethasone、Prednisolone、Prednisone 等皮質類固醇；Deferiprone；Ibritumomab tiuxetan；Iobenguane (I-131)；Tositumomab (I-131)
  - **Moderate（中度）**：Morphine、Acetylsalicylic acid（阿斯匹靈）、Nitisinone、Opium
  - **Minor（輕微）**：Zinc acetate、Zinc gluconate、Zinc sulfate
- 針對發育異常類疾病的患者族群，需特別留意 JAK 抑制劑在妊娠期間的潛在致畸風險。

主要警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個預測適應症都只有模型分數支持，沒有臨床試驗或文獻，證據等級為 L5。
- 機轉上無法連結 JAK 抑制與先天性發育異常，且藥物交互作用多，不建議在此階段推進。

**若要推進需要：**
- 取得詳細的藥物作用機轉資料（MOA），並釐清 JAK-STAT 與此疾病的生物學關聯
- 取得香港衛生署仿單的警語與禁忌症資料
- 進行前臨床或機轉研究，驗證預測是否具有生物學基礎
- 評估預測是否來自知識圖譜的網路假象
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

