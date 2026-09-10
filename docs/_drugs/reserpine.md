---
layout: default
title: Reserpine
parent: 僅模型預測 (L5)
nav_order: 641
evidence_level: L5
indication_count: 1
---

# Reserpine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Reserpine：原適應症資料缺失，預測用於難治型思覺失調症

## 一句話總結

Reserpine（DrugBank ID: DB00206）為傳統 rauwolfia 生物鹼類藥物，本資料集未收錄其原始適應症與正式作用機轉敘述。
TxGNN 模型預測它可能對**難治型思覺失調症 (Treatment-refractory Schizophrenia)** 有效，
但目前**沒有臨床試驗、沒有文獻**支持這個方向，證據等級為 **L5**（僅有模型預測）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（來源未收錄原始適應症） |
| 預測新適應症 | 難治型思覺失調症 (Treatment-refractory Schizophrenia) |
| TxGNN 預測分數 | 99.04% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

本資料集未收錄 Reserpine 正式的 MOA 敘述，但根據既有藥理知識推論：Reserpine 是 VMAT2（囊泡單胺轉運蛋白 2）不可逆抑制劑，會耗竭突觸前 dopamine、norepinephrine、serotonin 儲存。理論上降低中樞多巴胺傳導的方向，與典型抗精神病藥物（多巴胺 D2 拮抗）的作用邏輯一致，可能是 TxGNN 給出高相似度分數（0.99）的原因。

然而，由於 `original_moa` 與 `original_indications` 均無資料，這個機轉連結目前僅是模型基於知識圖譜拓樸相似性的推論，並非資料庫內驗證過的藥理敘述，需審慎看待。

更需注意的是，Reserpine 耗竭單胺的作用已知會誘發嚴重憂鬱與自殺風險，而難治型思覺失調症患者本身自殺風險已偏高，這在安全性上是明確疑慮，不宜僅憑機轉相似性就推進。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 安全性考量

安全性資訊請參考原廠仿單。

（註：TFDA/藥品仿單警語與禁忌資料為 Blocking 等級缺口，目前無法完成安全性初評。）

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有 TxGNN 模型預測（L5），沒有任何臨床試驗或文獻佐證機轉合理性；
- 藥品尚未在香港上市，且原始適應症、作用機轉、仿單警語/禁忌等關鍵安全性資料均缺失，加上 Reserpine 已知的憂鬱/自殺風險與難治型思覺失調症族群疊加，安全疑慮明確，不具備推進條件。

**若要推進需要：**
- 補齊 TFDA/藥品仿單警語與禁忌資料（Blocking，DG001）
- 補齊正式作用機轉來源（DrugBank API 查詢，DG002）
- 取得針對此適應症的臨床試驗或文獻證據
- 針對憂鬱/自殺風險在思覺失調症人群中的專門安全性評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

