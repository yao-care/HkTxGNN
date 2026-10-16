---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 431
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Guselkumab：預測新適應症為藥物誘發性骨質疏鬆症 (Drug-induced Osteoporosis)（證據等級 L5）。原適應症：乾癬"
monitor_inn: "GUSELKUMAB"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "psoriasis", "diabetic retinopathy", "renal osteodystrophy"]
---

# Guselkumab
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

# Guselkumab：從斑塊型乾癬到藥物誘發性骨質疏鬆症

## 一句話總結

Guselkumab（商品名 TREMFYA）是抗 IL-23 p19 的單株抗體，目前已知用於乾癬類疾病。
TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆症 (Drug-induced Osteoporosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 乾癬（依本報告彙整資料的機轉說明推定；香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 藥物誘發性骨質疏鬆症 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Guselkumab 專一結合 IL-23 的 p19 次單元，阻斷 IL-23/Th17 免疫軸。這條路徑在乾癬中會驅動角質細胞過度增生與斑塊形成。

IL-23/IL-17 訊號與發炎性骨流失有關，所以機轉上存在理論連結。不過，藥物誘發性骨質疏鬆症（例如類固醇引起者）主要由其他機制造成，IL-23 並非核心角色。目前沒有任何臨床或文獻證據佐證，0.998 的高分只是計算模型的預測結果。

另外要注意，本次資料中排名第 3 的「乾癬」有大量證據，但那是 guselkumab 既有的上市用途，屬於已知用藥的確認，不算真正的藥物再利用。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 補充：既有適應症（乾癬）的證據概況

以下僅供對照，不支持骨質疏鬆症的預測。

| 項目 | 內容 |
|------|------|
| 相關臨床試驗 | 多項已完成的 Phase 3 試驗，例如 [NCT03090100](https://clinicaltrials.gov/study/NCT03090100)（對比 secukinumab，n=1048）、[NCT02207231](https://clinicaltrials.gov/study/NCT02207231)（n=837） |
| 代表性文獻 | [28057360](https://pubmed.ncbi.nlm.nih.gov/28057360/)（VOYAGE 1，RCT，對比 adalimumab）、[28057361](https://pubmed.ncbi.nlm.nih.gov/28057361/)（VOYAGE 2，RCT） |
| 該項證據等級 | L1 |

## 香港上市資訊

許可證資料未載明劑型與核准適應症文字，因此下表僅列出可確認的資訊。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-65944 | TREMFYA 預充填注射針筒 100mg/1ml 注射液 | JOHNSON & JOHNSON (HONG KONG) LTD. |
| HK-67037 | TREMFYA 預充填注射筆 100mg/1ml 注射液 | JOHNSON & JOHNSON (HONG KONG) LTD. |

## 安全性考量

- **藥物交互作用**：資料庫共收錄 100 筆交互作用，以下列出部分代表性項目。
  - **嚴重 (Major)**：Adalimumab
  - **中度 (Moderate)**：Warfarin、Apixaban、Rivaroxaban、Dicoumarol、Simvastatin、Tacrolimus、Theophylline、Aminophylline、Roflumilast、Lidocaine、Fentanyl、Hydrocodone、Nifedipine、破傷風類毒素疫苗
  - **輕微 (Minor)**：各種鋅鹽（硫酸鋅、醋酸鋅、葡萄糖酸鋅、氯化鋅）

警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 骨質疏鬆症和機轉相關的預測目前只有模型分數，沒有任何試驗或文獻。
- 機轉連結偏理論性，證據等級僅 L5。

**若要推進需要：**
- 補充 IL-23 抑制與骨代謝（如類固醇引起的骨流失）的前臨床或機轉研究
- 系統性搜尋 IL-23 抑制劑與骨密度、骨折相關的文獻或觀察性資料
- 取得香港原廠仿單，確認核准適應症、警語與禁忌症
- 取得完整作用機轉資料，並評估目標族群（長期使用類固醇者）的安全性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

