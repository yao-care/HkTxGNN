---
layout: default
title: Lanreotide
parent: 僅模型預測 (L5)
nav_order: 508
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
monitor_inn: "LANREOTIDE"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "Ambras type hypertrichosis universalis congenita"]
description: "Lanreotide：預測新適應症為多毛症 (hypertrichosis (disease))（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Lanreotide: 多毛症 (hypertrichosis (disease))
{: .text-alpha }

## 一句話總結

Lanreotide 是一種體抑素（somatostatin）類似物，原本用於肢端肥大症、腦下垂體機能亢進與腦下垂體巨人症。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 多毛症 (hypertrichosis (disease)) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Lanreotide 屬於體抑素類似物，能抑制生長激素 (GH) 與 IGF-1 的分泌，這是它治療肢端肥大症的基礎。

IGF-1 訊號可能影響毛囊生長，因此理論上藥物可能調節毛髮生長。但毛髮過多症成因多元，包括先天性與藥物誘發型，目前沒有直接的機轉或臨床證據支持這個連結。這項預測的分數（0.9997）來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據，應視為待驗證的假說。

其他預測的適應症（牙齒／牙周異常的畸形症候群 0.9996、Dandy-Walker 畸形相關症候群 0.9996、遺傳性毛幹異常 0.9996、安布拉斯型全身性先天多毛症 0.9996）同樣只有 TxGNN 模型（深度學習）的分數，沒有試驗或文獻。這些多屬先天性結構或基因缺陷，機轉上看不出體抑素類似物能改變它們，分數可能只反映模型學到的相關疾病之間的相似性，而非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51884 | SOMATULINE AUTOGEL INJ 90MG (PREFILLED-SYRINGE) | 預充填注射劑 | 未提供 |
| HK-51885 | SOMATULINE AUTOGEL INJ 60 MG (PREFILLED-SYRINGE) | 預充填注射劑 | 未提供 |
| HK-51886 | SOMATULINE AUTOGEL INJ 120MG (PREFILLED-SYRINGE) | 預充填注射劑 | 未提供 |

三張許可證均為單方製劑，持證商為 BEAUFOUR IPSEN INTERNATIONAL (HONG KONG) LIMITED。

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（來自模型知識圖譜，並非仿單內容）：高血壓、肝臟疾病、膽囊疾病、膽結石（膽囊結石、膽管結石）、高血糖、低血糖、甲狀腺功能低下（含黏液水腫、先天性甲狀腺功能低下）、腎功能不全。
- **藥物交互作用**：資料庫共記錄 100 筆交互作用，以下為列出的部分項目，皆為中度 (Moderate)，主要集中在降血糖藥物：
  - 口服降血糖藥：Acarbose、Alogliptin、Metformin、Pioglitazone、Canagliflozin、Dapagliflozin、Empagliflozin、Linagliptin、Chlorpropamide、Glimepiride
  - GLP-1 類藥物：Albiglutide、Dulaglutide、Semaglutide
  - 胰島素類：Insulin aspart、degludec、detemir、glargine、glulisine、human (isophane)、human (regular)
  - 使用這些藥物的病人需留意血糖變化。

其他仿單層級的警語與禁忌資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數（0.9997），沒有任何臨床試驗或文獻，證據等級為 L5。
- 多毛症的機轉連結只是推測，且藥物本身有血糖、膽囊等需要留意的安全性議題。

**若要推進需要：**
- 取得完整的作用機轉資料，並分析 GH/IGF-1 抑制與毛囊生長的關聯
- 系統性搜尋文獻與臨床試驗（含病例報告），確認是否有任何多毛症相關的實際觀察
- 取得香港衛生署仿單，補齊核准適應症、警語與禁忌
- 評估目標族群（如藥物誘發型多毛症）及給藥途徑是否可行，並權衡長期使用的風險與效益
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

