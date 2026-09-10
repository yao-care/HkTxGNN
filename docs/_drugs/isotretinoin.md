---
layout: default
title: Isotretinoin
parent: 僅模型預測 (L5)
nav_order: 419
evidence_level: L5
indication_count: 2
---

# Isotretinoin
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

# ISOTRETINOIN：原適應症資料缺失，TxGNN 預測惡性腎血管性高血壓

## 一句話總結

ISOTRETINOIN（DrugBank ID: DB00982）目前原始適應症與作用機轉資料均缺失，且在香港未上市（0 張許可證）。
TxGNN 模型預測它可能對**惡性腎血管性高血壓 (Malignant Renovascular Hypertension)** 有效，
但目前**無任何臨床試驗、ICTRP 登記或文獻**支持，證據等級僅為 **L5（純模型預測）**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（無登記資料） |
| 預測新適應症 | 惡性腎血管性高血壓 (Malignant Renovascular Hypertension) |
| TxGNN 預測分數 | 99.01% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，DrugBank 查詢結果亦未提供 ISOTRETINOIN 的原始適應症與 MOA 說明，因此無法建立原適應症與新適應症之間的直接關聯。

理論上，維生素 A 酸類（retinoid）藥物在動物模型中曾被探討對腎臟纖維化與 RAAS（腎素-血管收縮素-醛固酮）路徑具有調節作用，這是 retinoid 類藥物與惡性高血壓性腎病之間唯一可想像的機轉切入點。但 ISOTRETINOIN（13-cis 型）與「惡性腎血管性高血壓」之間，目前沒有任何直接或間接的機轉文獻佐證。

第二個預測結果「惡性高血壓性腎病 (malignant hypertensive renal disease)」與第一個預測分數完全相同（0.9901），且屬於高度重疊的疾病概念，顯示 TxGNN 在此案例中辨識出的是同一群相近疾病節點，而非兩個獨立驗證的訊號。整體而言，這個連結目前僅為模型輸出的統計預測，缺乏機轉合理性支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

ISOTRETINOIN 目前在香港未上市，無許可證資料。

## 安全性考量

安全性資訊請參考原廠仿單。

（註：仿單警語、禁忌症與 DDI 查詢均無資料，且「TFDA 仿單警語/禁忌」被標記為 Blocking 等級資料缺口，尚無法進行 S1 安全性初評。）

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅為 L5，無任何臨床試驗、ICTRP 登記或文獻支持這項預測。
- 原始適應症、作用機轉（MOA）與安全性資料均缺失，其中仿單警語/禁忌屬於 Blocking 等級缺口，無法進入下一階段安全性初評。
- 藥物在香港未上市，短期內無實際落地路徑。

**若要推進需要：**
- 取得 TFDA/原廠仿單警語與禁忌症資料（解除 Blocking 缺口）
- 補齊 DrugBank 作用機轉（MOA）資料，釐清 retinoid 類藥物與腎血管性高血壓的機轉可能性
- 確認 ISOTRETINOIN 原始核准適應症，作為機轉關聯性分析基礎
- 針對兩個高度相似的預測疾病，擴大文獻與試驗檢索範圍（含動物實驗、case report）以尋找間接證據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

