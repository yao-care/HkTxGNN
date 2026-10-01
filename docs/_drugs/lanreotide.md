---
layout: default
title: Lanreotide
parent: 僅模型預測 (L5)
nav_order: 499
evidence_level: L5
indication_count: 5
---

# Lanreotide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Lanreotide：從（原適應症未載明）到多毛症

## 一句話總結

Lanreotide 是一種體抑素（somatostatin）類似物，目前在香港有 3 張上市許可證，但資料中未載明原適應症。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。
Lanreotide 屬於體抑素類似物，一般認為主要作用於 SSTR2 與 SSTR5 受體，抑制生長激素 (GH) 與 IGF-1。

但從機轉看，這個預測並不理想。IGF-1 訊號有助於毛囊生長，降低 IGF-1 若有影響，方向應是減少毛髮生長，與治療多毛症的目標相反。因此這個連結偏推測，也可能只是知識圖譜的假象。

TxGNN 分數雖高（99.97%），但沒有任何試驗、文獻或前臨床資料佐證，目前只能視為模型輸出，不能視為有效證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-51884 | SOMATULINE AUTOGEL INJ 90MG (PREFILLED-SYRINGE) | BEAUFOUR IPSEN INTERNATIONAL (HONG KONG) LIMITED |
| HK-51885 | SOMATULINE AUTOGEL INJ 60 MG (PREFILLED-SYRINGE) | BEAUFOUR IPSEN INTERNATIONAL (HONG KONG) LIMITED |
| HK-51886 | SOMATULINE AUTOGEL INJ 120MG (PREFILLED-SYRINGE) | BEAUFOUR IPSEN INTERNATIONAL (HONG KONG) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測（L5），沒有臨床試驗、文獻或前臨床證據。
- 機轉上，抑制 GH/IGF-1 與治療多毛症的方向相反，可信度低。

**若要推進需要：**
- 取得詳細的作用機轉資料（DrugBank MOA）。
- 取得香港衛生署仿單，確認原適應症、警語與禁忌症。
- 尋找體抑素類似物與毛髮生長之間的前臨床或病例報告證據。
- 釐清 TxGNN 預測的來源路徑，判斷是否為知識圖譜假象。

**補充：**同一藥物的其他預測（牙周相關畸形症候群、Dandy-Walker 畸形相關症候群、遺傳性毛幹異常、Ambras 型先天性全身多毛症）同樣只有模型分數。牙周相關的檢索文獻均為一般牙周炎文獻，完全未提及 lanreotide，不構成藥物特異性證據。這些預測目前都不建議推進。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

