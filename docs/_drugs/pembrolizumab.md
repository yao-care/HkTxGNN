---
layout: default
title: Pembrolizumab
parent: 僅模型預測 (L5)
nav_order: 673
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Pembrolizumab：預測新適應症為牙齦纖維瘤病 (Fibromatosis, Gingival)（證據等級 L5）。原適應症：非小細胞肺癌、肺癌、轉移性黑色素瘤"
monitor_inn: "PEMBROLIZUMAB"
predicted_indications: ["fibromatosis, gingival", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "hamartoma of lung", "fibroma of lung"]
---

# Pembrolizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Pembrolizumab：從非小細胞肺癌到牙齦纖維瘤病

## 一句話總結

Pembrolizumab（KEYTRUDA）是一種抗 PD-1 的免疫檢查點抑制劑，原本用於非小細胞肺癌、肺癌與轉移性黑色素瘤。
TxGNN 模型預測它可能對**牙齦纖維瘤病 (Fibromatosis, Gingival)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個預測，僅為模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌、肺癌、轉移性黑色素瘤（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 牙齦纖維瘤病 (Fibromatosis, Gingival) |
| TxGNN 預測分數 | 99.40% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Pembrolizumab 是針對 PD-1（PDCD1，CD279）的抗體，透過阻斷 PD-1 路徑，恢復 T 細胞對腫瘤的免疫反應，已在多種癌症中取得核准。

牙齦纖維瘤病是牙齦組織的良性纖維性過度增生，可能為遺傳性或藥物誘發。PD-1 阻斷在其發病機轉中沒有已知的角色，因此目前**無法建立可信的機轉關聯**。0.994 的高分僅是模型預測，不代表臨床上有效。

此外，原適應症（惡性腫瘤）與預測適應症（良性纖維增生）在疾病性質上差異很大，兩者的相似性分析尚未完成。

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
| HK-64228 | KEYTRUDA SOLUTION FOR INJECTION 100MG/4ML | 注射液 | 許可證資料未載明 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（抗 PD-1 單株抗體），非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**（共 13 筆紀錄）：
  - **重大 (Major)**：Lenalidomide、Pomalidomide、Thalidomide
  - **中度 (Moderate)**：Hydrocortisone、Triamcinolone、Dexamethasone、Betamethasone、Budesonide、Prednisolone、Prednisone、Methylprednisolone、Deflazacort（皆為皮質類固醇）
  - 另有藥理資料顯示其作用標的為 PD-1 (PDCD1)。

其他警語與禁忌症資料不足，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型（L5），沒有臨床試驗或文獻佐證，且 PD-1 阻斷與牙齦纖維瘤病之間缺乏機轉關聯。
- 良性疾病使用具免疫相關不良反應風險的抗癌免疫療法，風險效益比不佳。

**若要推進需要：**
- 釐清 PD-1 路徑與牙齦纖維化之間是否有任何生物學證據
- 取得詳細的作用機轉資料與原廠仿單安全性資訊（警語、禁忌症）
- 先進行前臨床或機轉研究，再評估是否值得進一步探討

---

## 補充：其他預測適應症

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 備註 |
|------|-----------|-----------|---------|------|
| 2 | 包涵體肌病合併早發性 Paget 病（伴或不伴額顳葉失智） | 99.37% | L5 | 無機轉關聯；免疫檢查點抑制劑本身可能引起肌炎，需留意安全性 |
| 3 | 肺錯構瘤 | 99.35% | L5 | 良性病變，無 PD-1 抑制的依據 |
| 4 | 肺門癌 | 99.35% | L4 | 實質上是現有肺癌適應症的解剖亞型，不算真正的藥物再利用；僅有個案報告，建議列為研究問題 |
| 5 | 肺纖維瘤 | 99.34% | L5 | 無機轉關聯，無試驗與文獻 |

在這些候選中，**肺門癌**與既有適應症最接近，但其效益主要應參考非小細胞肺癌的試驗數據，而非作為新的再利用機會。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

