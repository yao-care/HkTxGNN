---
layout: default
title: Durvalumab
parent: 僅模型預測 (L5)
nav_order: 304
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Durvalumab：預測新適應症為前列腺尿道尿路上皮癌 (Prostatic Urethra Urothelial Carcinoma)（證據等級 L5）。原適應症：移行細胞癌"
---

# Durvalumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Durvalumab：從移行細胞癌到前列腺尿道尿路上皮癌

## 一句話總結

Durvalumab 是一種針對 PD-L1 的免疫檢查點抑制劑，原本用於移行細胞癌（尿路上皮癌）的治療。
TxGNN 模型預測它可能對**前列腺尿道尿路上皮癌 (Prostatic Urethra Urothelial Carcinoma)** 有效，
但該疾病目前**沒有直接的臨床試驗或文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 移行細胞癌（來自知識圖譜；香港許可證未登載適應症文字） |
| 預測新適應症 | 前列腺尿道尿路上皮癌 (Prostatic Urethra Urothelial Carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Durvalumab 已知為抗 PD-L1 的單株抗體，透過阻斷 PD-L1 與 PD-1/CD80 的結合，解除腫瘤對 T 細胞的抑制。

前列腺尿道尿路上皮癌在組織學上屬於尿路上皮癌，與原適應症（移行細胞癌）屬於同一腫瘤譜系，因此阻斷 PD-L1 在機轉上有合理性。

不過，0.9998 的 TxGNN 分數僅為計算預測，並未包含此特定部位的臨床或文獻證據，不能視為療效證明。

---

## 臨床試驗證據

此預測適應症目前無相關臨床試驗登記。

---

## 文獻證據

此預測適應症目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65929 | IMFINZI CONCENTRATE FOR SOLUTION FOR INFUSION 500MG/10ML | 未登載 | 未登載 |
| HK-65928 | IMFINZI CONCENTRATE FOR SOLUTION FOR INFUSION 120MG/2.4ML | 未登載 | 未登載 |

兩張許可證均由 ASTRAZENECA HONG KONG LIMITED 持有，狀態皆為有效。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（免疫檢查點抑制劑），非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：資料庫共記錄 81 項交互作用，以下為部分範例：
  - **嚴重（Major）**：Adalimumab
  - **中度（Moderate）**：皮質類固醇類（Hydrocortisone、Dexamethasone、Prednisone、Prednisolone、Methylprednisolone、Budesonide、Betamethasone、Triamcinolone、Deflazacort）、Roflumilast、Alemtuzumab、Anakinra、Alefacept、破傷風類毒素疫苗、炭疽疫苗
  - **輕微（Minor）**：各種鋅製劑（醋酸鋅、葡萄糖酸鋅、硫酸鋅、氯化鋅）

  這些多屬免疫調節或免疫抑制相關藥物，可能影響免疫檢查點抑制劑的作用，使用時需留意。

其他警語與禁忌症資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅有模型分數支持，沒有任何直接的臨床試驗或文獻，證據等級為 L5。
- 雖然腫瘤譜系與原適應症相同，機轉上合理，但仍不足以支持推進。

**若要推進需要：**
- 取得此特定部位（前列腺尿道）的臨床或真實世界證據。
- 補齊作用機轉資料與香港仿單的警語、禁忌症及核准適應症。
- 評估是否可由相鄰的尿路上皮癌研究（例如 NCT02812420、NCT03912818）外推，並與專家討論其適用性。

---

### 補充：其他預測適應症的證據概況

為供參考，同一藥物其他排名較前的預測中，證據略多者為：

| 預測適應症 | 證據等級 | 現有證據 | 建議 |
|-----------|---------|---------|------|
| 腎盂肉瘤樣移行細胞癌 | L3 | 1 個早期 Phase 1 試驗（NCT02812420，n=54，進行中） | Research Question |
| 浸潤性膀胱尿路上皮癌肉瘤樣變異型 | L3 | 1 個提前終止的 Phase 2 試驗（NCT03912818，僅 7 人）及 NCT02812420 | Research Question |
| 子宮頸管癌 | L3 | 1 個完成的 Phase 1 試驗（NCT03452332，n=20）及間接文獻 | Research Question |

其餘預測（腎盂乳突狀尿路上皮癌、子宮韌帶腺癌、子宮頸腺樣囊性癌等）均僅有模型預測（L5），建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

