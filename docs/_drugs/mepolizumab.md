---
layout: default
title: Mepolizumab
parent: 中證據等級 (L3-L4)
nav_order: 401
evidence_level: L4
indication_count: 5
---

# Mepolizumab
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Mepolizumab：從嗜酸性球介導疾病（原適應症資料缺口）到免疫性血小板減少症

## 一句話總結

Mepolizumab 是一款以 IL-5 為標靶的生物製劑，但其正式登記的原始適應症與作用機轉資料目前尚未收錄（已知資料缺口），文獻線索顯示其臨床應用情境與嗜伊紅性球增多症候群（HES）相關。TxGNN 模型預測它可能對**免疫性血小板減少症 (thrombocytopenia due to immune destruction)** 有效，目前僅有 **1 篇個案報告**支持這個方向，**無任何相關臨床試驗登記**，證據強度薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料庫未收錄（DG002 資料缺口）；文獻線索顯示與嗜伊紅性球增多症候群（HES）相關 |
| 預測新適應症 | 免疫性血小板減少症 (Thrombocytopenia due to Immune Destruction) |
| TxGNN 預測分數 | 99.66% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前藥物資料庫缺乏 mepolizumab 正式登記的作用機轉描述（DG002），無法直接引用官方 MOA 文字。但從既有文獻與模型推論脈絡可看出，mepolizumab 屬於抗 IL-5 標靶生物製劑，其原始臨床應用情境集中於嗜酸性球（eosinophil）介導的疾病，本次證據包中兩篇相關文獻皆以嗜伊紅性球增多症候群（HES）為討論主軸。

新預測適應症「免疫性血小板減少症」與 HES 之間的關聯，目前僅能追溯到一則個案報告：一名類固醇抗藥性的嗜酸性球免疫失調患者，合併血栓性微血管病變，在使用 mepolizumab 治療後獲得緩解。這提示嗜酸性球活化可能在特定病例中間接誘發免疫性血小板破壞，但**這是 HES 的續發表現，並非 mepolizumab 對血小板路徑的直接作用機轉**，關聯性屬於推論性質，尚未有機轉層級的直接證據。

值得注意的是，TxGNN 針對本藥物同時預測了另外 4 個血小板相關疾病（rank 2–5），其中 rank 2「原發性血小板釋放障礙」僅有 1 篇 HES 治療回顧文獛間接提及 mepolizumab，rank 3–5（假性 von Willebrand 病、自體免疫性血小板減少、Glanzmann 血小板無力症）則完全沒有文獛或試驗證據支持，且其機轉分析本身即指出這些疾病屬於遺傳性結構缺陷或抗體介導機轉，與 IL-5 訊號路徑無生物學交集，很可能是知識圖譜嵌入空間的偽陽性關聯，建議優先排除、不列入後續研究。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case Report | Blood Cells, Molecules & Diseases | 一名類固醇抗藥性、合併血栓性微血管病變的嗜酸性球免疫失調病例，經 mepolizumab 治療後病況緩解 |

---

## 安全性考量

安全性資訊請參考原廠仿單。（本評估之藥品仿單警語、禁忌症與藥物交互作用資料目前均為阻斷性缺口 DG001，無法完成 S1 安全性初評）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有 1 篇個案報告支持此適應症方向，無任何臨床試驗登記，證據等級為 L4，且機轉關聯屬間接推論（HES 續發表現，非直接作用於血小板破壞路徑）。
- 本藥物尚未在香港上市（0 張許可證），且仿單警語/禁忌症資料存在阻斷性缺口（DG001），無法完成基本安全性初評。
- 其餘 4 個同批預測適應症（rank 2–5）證據更薄弱甚至完全缺乏支持，其中 3 項（假性 von Willebrand 病、自體免疫性血小板減少、Glanzmann 血小板無力症）機轉上與 IL-5 路徑無交集，應視為模型雜訊優先排除。

**若要推進需要：**
- 補齊 TFDA/香港藥品仿單警語與禁忌症資料，解除 DG001 阻斷性缺口
- 取得 mepolizumab 完整作用機轉（MOA）資料，解除 DG002
- 尋找針對「IL-5 抑制與免疫性血小板破壞」更直接的機轉研究或病例系列，而非僅依賴單一個案報告
- 確認是否已有或計劃中的香港上市/臨床試驗申請
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

