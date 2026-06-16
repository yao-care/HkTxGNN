---
layout: default
title: Carbetocin
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 2
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

# Carbetocin：從產後子宮收縮不良到 Isotretinoin-Like Syndrome

## 一句話總結

Carbetocin（卡貝縮宮素）是一種 oxytocin receptor agonist，臨床上用於預防剖腹產後子宮收縮不良與產後出血。TxGNN 模型預測它可能與 **Isotretinoin-Like Syndrome** 及 **Goodman Syndrome** 有關聯，預測分數分別達 99.1% 與 99.1%，然而目前兩個適應症均**無任何臨床試驗或文獻支持**，屬純模型預測結果。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 產後子宮收縮不良（剖腹產後出血預防）|
| 預測新適應症 #1 | Isotretinoin-Like Syndrome |
| 預測新適應症 #2 | Goodman Syndrome |
| TxGNN 預測分數 | 99.1%（#1）/ 99.1%（#2）|
| 證據等級 | L5（僅模型預測，無實際研究）|
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

Carbetocin 是合成的 oxytocin 類似物，透過激動子宮肌層的 oxytocin receptor，引發持續性的子宮收縮，臨床主要用於預防剖腹產後的子宮無力與大量出血。其作用靶點明確：oxytocin receptor（OXTR），屬 G protein-coupled receptor（Gq 路徑）。

**Isotretinoin-like syndrome**（又稱 retinoic acid embryopathy）是孕期暴露於 isotretinoin 所致的致畸形症候群，表現為顱顏、心臟、CNS 及胸腺異常，本質上是胚胎發育缺陷。Oxytocin 系統雖在顱顏發育中有部分表現，但與 retinoic acid 信號路徑的交集極為間接，carbetocin 並不具備矯正胚胎發育異常的已知機轉。

**Goodman syndrome**（acrocephalopolysyndactyly type IV，或 CACP syndrome / PRG4 突變）屬罕見遺傳性骨骼畸形，涉及顱縫早閉或軟骨/滑液蛋白缺陷。Oxytocin receptor 激動對顱縫融合或 PRG4 蛋白表現均無直接調控作用，治療合理性缺乏生物學依據。

TxGNN 的高分（0.991）極可能來自知識圖譜的拓撲近鄰性雜訊，而非真實的治療機轉連結。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 台灣上市資訊

Carbetocin 在台灣目前**未取得藥品許可證**，無上市記錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
兩個預測適應症均為 L5 等級，無任何臨床試驗或文獻支持，且機轉關聯性分析顯示 carbetocin 的 oxytocin receptor 激動路徑與這兩個罕見症候群（胚胎致畸形症、遺傳性骨骼畸形）在生物學上缺乏直接關聯，TxGNN 高分屬圖譜預測雜訊的可能性高，不宜推進再利用評估。

**若要重新評估需要：**
- 補充 carbetocin 完整 MOA 資料（建議查詢 DrugBank API，填補 DG002 缺口）
- 確認 TFDA 仿單警語與禁忌（DG001 為 Blocking 等級，需優先補齊）
- 若未來有文獻指向 oxytocin 系統與胚胎發育/罕見遺傳症候群的直接機轉連結，再重新進入評估流程
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

