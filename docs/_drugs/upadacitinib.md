---
layout: default
title: Upadacitinib
parent: 僅模型預測 (L5)
nav_order: 917
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Upadacitinib：預測新適應症為眼缺損小眼症－肢根型骨發育不良症候群 (Colobomatous Microphthalmia-Rhizomelic Dysplasia…（證據等級 L5）。原適應症：類風濕性關節炎（rheumatoid arthritis）"
monitor_inn: "UPADACITINIB"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Upadacitinib
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

## Upadacitinib：從類風濕性關節炎到 Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome
{: .text-alpha }

## 一句話總結

Upadacitinib 是一種 JAK 抑制劑，原本用於治療類風濕性關節炎。
TxGNN 模型預測它可能對**眼缺損小眼症－肢根型骨發育不良症候群 (Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測分數。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎（rheumatoid arthritis）；香港許可證未載明核准適應症文字 |
| 預測新適應症 | 眼缺損小眼症－肢根型骨發育不良症候群 (Colobomatous Microphthalmia-Rhizomelic Dysplasia Syndrome) |
| TxGNN 預測分數 | 0.9961 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Upadacitinib 已知為選擇性 JAK1 抑制劑，透過調節 JAK-STAT 訊號傳遞來抑制免疫發炎反應，因此在類風濕性關節炎等免疫介導疾病中具有療效。

然而，這個預測的新適應症是一種罕見的先天發育異常症候群（眼部缺損／小眼症，合併肢根型骨骼發育不良）。目前沒有找到 JAK-STAT 訊號與此症候群之間合理的生物學關聯。免疫調節藥物也不太可能逆轉已形成的結構性缺陷。

因此，這個高分預測來自 TxGNN 模型（深度學習），可能反映模型從相關疾病間學到的相似性，而非生物學證據，解讀時需格外保守。

此外，本報告資料中另有排名第 2 的預測：**短指併指症候群 (Brachydactyly-Syndactyly Syndrome)**（分數 0.9958）。它同樣是先天性肢體畸形，同樣沒有臨床試驗、文獻或機轉上的支持，建議比照處理。

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
| HK-67512 | RINVOQ PROLONGED-RELEASE TABLETS 30MG | 緩釋錠 | 未提供 |
| HK-66872 | RINVOQ PROLONGED-RELEASE TABLETS 15MG | 緩釋錠 | 未提供 |
| HK-68084 | RINVOQ PROLONGED-RELEASE TABLETS 45MG | 緩釋錠 | 未提供 |

以上三張許可證均為單方製劑，持有者為 ABBVIE LIMITED，狀態皆為有效。

---

## 安全性考量

- **藥物交互作用**：已查詢到共 100 筆交互作用，以下列出主要者：
  - **嚴重 (Major)**：
    - 皮質類固醇類：Hydrocortisone、Triamcinolone、Dexamethasone、Beclomethasone dipropionate、Betamethasone、Budesonide、Prednisone、Prednisolone
    - 其他：Clarithromycin、Cobicistat、Deferiprone、Iobenguane (I-131)
  - **中度 (Moderate)**：Aprepitant、Cimetidine、Miconazole、Deferasirox
  - **輕微 (Minor)**：鋅類製劑（Zinc sulfate、Zinc acetate、Zinc gluconate）
- **JAK 抑制劑類別風險**：此類藥物通常帶有嚴重感染、死亡率、惡性腫瘤、重大心血管事件 (MACE) 及血栓的黑框警語。本次整理的資料未包含香港仿單的警語與禁忌症，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測分數（0.9961），沒有臨床試驗、文獻，也缺乏作用機轉資料，證據等級僅為 L5。
- 預測的疾病為先天性結構畸形，與 JAK1 抑制的免疫調節機轉缺乏合理關聯，而藥物本身的安全風險與交互作用負擔不低，不適合在缺乏依據下推進。

**若要推進需要：**
- 取得香港仿單的警語與禁忌症，完成安全性篩選
- 補齊 Upadacitinib 的作用機轉資料（例如查詢 DrugBank）
- 找出 JAK-STAT 訊號與此症候群致病機制之間的生物學證據
- 進行前臨床或疾病模型研究，驗證是否有任何療效訊號
- 確認該罕見疾病是否有可行的治療目標與臨床終點
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

