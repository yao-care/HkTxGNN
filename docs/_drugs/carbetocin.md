---
layout: default
title: Carbetocin
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Carbetocin：預測新適應症為isotretinoin-like syndrome（證據等級 L5）。原適應症：Prader-Willi 症候群、Noonan 症候群"
monitor_inn: "CARBETOCIN"
predicted_indications: ["isotretinoin-like syndrome", "Goodman syndrome"]
---

# Carbetocin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Carbetocin：從 Prader-Willi 症候群與 Noonan 症候群到 isotretinoin-like syndrome

## 一句話總結

Carbetocin 是一種長效型催產素（oxytocin）類似物，在本次資料中的原適應症為 Prader-Willi 症候群與 Noonan 症候群（來自知識圖譜）。
TxGNN 模型預測它可能對 **isotretinoin-like syndrome** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | Prader-Willi 症候群、Noonan 症候群（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | isotretinoin-like syndrome |
| TxGNN 預測分數 | 99.15% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Carbetocin 是長效型催產素類似物，作用標的為催產素受體（OXTR）。藥理資料指出，它臨床上用於預防子宮收縮乏力所致的產後出血，另有鼻用劑型（LV-101）正開發用於 Prader-Willi 症候群，目的是減輕極度飢餓感與暴食。

Isotretinoin-like syndrome 是類似視黃酸胚胎病變的發育性畸形疾病。就現有資料而言，**催產素受體促效作用與此疾病的病程之間，沒有明確的機轉關聯**。

此預測較可能來自知識圖譜中與原適應症（Prader-Willi、Noonan 症候群，皆為遺傳性症候群）相鄰的節點關係，而非生物學上的實質依據。因此分數雖高，仍應視為假說，不宜直接當作療效證據。

排名第二的預測為 Goodman syndrome（分數 99.06%，同樣無任何試驗或文獻），也缺乏機轉依據，判斷相同。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50670 | DURATOCIN INJ 100MCG/ML | 注射劑 | 資料中未載明 |

廠商：FERRING PHARMACEUTICALS LTD。

---

## 安全性考量

- **藥物交互作用**：藥理資料僅顯示 carbetocin 與催產素受體（OXTR）的作用標的關係，無具體藥物間交互作用等級可供參考。

其餘警語與禁忌症資料不足，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型（證據等級 L5），沒有臨床試驗或文獻佐證，且催產素受體促效作用與 isotretinoin-like syndrome 之間找不到合理機轉。
- 香港許可證的適應症文字缺漏，安全性資料也不足，目前無法進行安全性篩選。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並評估其與目標疾病病理的關聯
- 取得香港衛生署的仿單，確認核准適應症、警語與禁忌症
- 系統性檢索文獻與試驗登記，確認是否有任何支持證據
- 若仍認為有探索價值，先進行前臨床或機轉層面的驗證
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

