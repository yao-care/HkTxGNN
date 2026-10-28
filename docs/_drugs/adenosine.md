---
layout: default
title: Adenosine
parent: 僅模型預測 (L5)
nav_order: 27
evidence_level: L5
indication_count: 1
monitor_inn: "ADENOSINE"
predicted_indications: ["obsolete bundle branch block"]
last_modified_at: 2026-10-28
description: "Adenosine：預測新適應症為已廢棄的束支傳導阻滯 (obsolete bundle branch block)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Adenosine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Adenosine：腺苷受體促效劑 → 已廢棄的束支傳導阻滯 (obsolete bundle branch block)
{: .text-alpha }

## 一句話總結

Adenosine 是腺苷類藥物，目前在香港有注射劑型上市。
TxGNN 模型預測它可能對**已廢棄的束支傳導阻滯 (obsolete bundle branch block)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 已廢棄的束支傳導阻滯 (obsolete bundle branch block) |
| TxGNN 預測分數 | 0.9994 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就一般藥理知識而言，Adenosine 作用於房室結的 A1 受體，可減緩傳導，因此與心臟傳導相關疾病在機轉上有一定關聯。

然而，束支傳導阻滯屬於房室結以下（結下）的傳導缺陷，減緩傳導並不是這類疾病的治療效果。此外，「束支傳導阻滯」這個詞在疾病本體分類中已被標示為廢棄（obsolete），因此這個高分預測可能只是來自已淘汰的疾病節點，而非真正的藥物再利用訊號。

整體而言，0.9994 的預測分數很高，但沒有任何臨床證據佐證，解讀時必須非常保守。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-43112 | ADENOSCAN INJ 3MG/ML | 注射劑 | 本地資料未記錄 |
| HK-18525 | HEPATOSWISS FOR IV INFUSION INJ | 靜脈輸注注射劑 | 本地資料未記錄 |
| HK-18057 | HEPATOSWISS IM INJ | 肌肉注射劑 | 本地資料未記錄 |

## 安全性考量

- **藥物交互作用**（共查得 100 筆，以下列出主要者）：
  - 嚴重（Major）：Cisapride、Dolasetron、Papaverine
  - 中度（Moderate）：Famotidine、Clarithromycin、Granisetron、Levofloxacin、Ondansetron、Palonosetron

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型，沒有臨床試驗或文獻佐證，證據等級為 L5。
- 目標疾病為已廢棄的疾病名稱，且束支傳導阻滯屬結下缺陷，腺苷減緩傳導的作用在機轉上並不合理，預測可能是分類節點造成的假象。

**若要推進需要：**
- 確認該廢棄疾病節點對應的現行疾病名稱，重新評估預測是否仍有意義
- 補充 Adenosine 的作用機轉資料
- 取得香港原廠仿單的警語與禁忌症資料
- 在有明確臨床或機轉證據前，不建議投入進一步開發
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

