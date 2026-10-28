---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 431
evidence_level: L5
indication_count: 8
monitor_inn: "GUSELKUMAB"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "renal osteodystrophy", "congenital hypotrichosis with juvenile macular dystrophy", "primary release disorder of platelets", "Glanzmann thrombasthenia", "non-renal secondary hyperparathyroidism"]
last_modified_at: 2026-10-23
description: "Guselkumab：預測新適應症為藥物誘發性骨質疏鬆症（證據等級 L5）。原適應症：許可證資料未載明"
---

# Guselkumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Guselkumab：從已上市適應症（許可證未載明）到藥物誘發性骨質疏鬆症
{: .text-alpha }

## 一句話總結

Guselkumab 是一種 IL-23 p19 抑制劑，在香港已有 2 張有效許可證，但許可證資料中未載明核准適應症。
TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆症 (drug-induced osteoporosis)** 有效，
目前**沒有臨床試驗，也沒有文獻**直接支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 藥物誘發性骨質疏鬆症 |
| TxGNN 預測分數 | 0.9984 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Guselkumab 是 IL-23 p19 亞單位抑制劑。本報告所整理的資料中缺乏詳細的作用機轉資料，以上機轉描述來自藥物類別的一般認知。

IL-23/IL-17 訊號路徑在發炎性骨流失中可能扮演角色，因此理論上可能與藥物（例如糖皮質素）誘發的骨質疏鬆有關。但這個連結目前仍屬推測，唯一的支持是較高的 TxGNN 預測分數，沒有任何臨床試驗或文獻佐證。

此外，由於許可證資料未載明原適應症，無法比較原適應症與新適應症之間的關聯性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65944 | TREMFYA 預填充注射器 100mg/1ml 注射液 | 注射液 | 許可證資料未載明 |
| HK-67037 | TREMFYA 預填充注射筆 100mg/1ml 注射液 | 注射液 | 許可證資料未載明 |

兩張許可證均為單一成分製劑，持有者為 Johnson & Johnson (Hong Kong) Ltd.。

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下列出部分主要項目：
  - **重大 (Major)**：Adalimumab
  - **中度 (Moderate)**：Simvastatin、Apixaban、Warfarin、Rivaroxaban、Tacrolimus、Theophylline、Fentanyl、Nifedipine、Lidocaine
  - **輕微 (Minor)**：多種鋅製劑（硫酸鋅、醋酸鋅、葡萄糖酸鋅、氯化鋅）

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有 TxGNN 模型預測，沒有任何直接研究藥物誘發性骨質疏鬆症的臨床試驗或文獻，證據等級為 L5。
- 機轉連結屬推測，且許可證資料、作用機轉與仿單警語皆有缺口。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 補充詳細的作用機轉資料（MOA）
- 進行文獻回顧，尋找 IL-23 抑制與骨代謝或糖皮質素誘發骨流失的前臨床或臨床證據
- 若有初步證據，再評估進行探索性研究的可行性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

