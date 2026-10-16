---
layout: default
title: Teprotumumab
parent: 僅模型預測 (L5)
nav_order: 861
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Teprotumumab：預測新適應症為monosomy X（證據等級 L5）。原適應症：內分泌性眼球突出（endocrine exophthalmos）"
monitor_inn: "Teprotumumab"
predicted_indications: ["monosomy X", "esophageal varices without bleeding", "esophageal varices with bleeding", "mixed gonadal dysgenesis", "mitochondrial oxidative phosphorylation disorder due to nuclear DNA anomalies", "Turner syndrome due to structural X chromosome anomalies", "mosaic monosomy X", "sex chromosome disorder of sex development", "varicose disease", "X chromosome number anomaly"]
---

# Teprotumumab
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

# Teprotumumab：從內分泌性眼球突出到 monosomy X（透納氏症相關）

## 一句話總結

Teprotumumab 是一種 IGF-1R 抑制型單株抗體，原本用於內分泌性眼球突出（甲狀腺眼病相關）。
TxGNN 模型預測它可能對 **monosomy X (Monosomy X)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 內分泌性眼球突出（endocrine exophthalmos） |
| 預測新適應症 | monosomy X |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Teprotumumab 是 IGF-1R 抑制型單株抗體，在內分泌性眼球突出中透過阻斷眼眶纖維母細胞的 IGF-1R 訊號發揮作用。

Monosomy X（透納氏症）的特徵為身材矮小與性腺發育不全，與 GH/IGF-1 軸的生長調控有關，這可能是模型產生關聯的原因。然而，阻斷 IGF-1R 在機轉上預期會抑制而非促進生長，與治療目標相反。因此這個預測缺乏明確的合理機轉，較可能反映知識圖譜中的網路相近性，而非真實的治療訊號。

其他排名前 10 的預測（食道靜脈曲張、混合性性腺發育不全、粒線體氧化磷酸化疾病、靜脈曲張等）同樣沒有機轉依據或臨床證據。其中多項為 X 染色體異常或性染色體發育異常的相近疾病，分數高度集中，顯示可能來自相同的圖譜訊號，而非各自獨立的證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68834 | TEPEZZA POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG（Amgen Hong Kong Limited） | 未提供 | 未提供 |

## 安全性考量

- **藥物交互作用**：本次彙整的資料顯示共 45 筆交互作用紀錄，其中列出的項目皆為中度（Moderate），主要為降血糖藥物，例如：
  - 雙胍類／TZD 類：Metformin、Pioglitazone
  - SGLT2 抑制劑：Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin
  - DPP-4 抑制劑：Alogliptin、Saxagliptin、Linagliptin
  - GLP-1 類：Albiglutide、Dulaglutide、Semaglutide、Exenatide
  - 磺醯脲類：Chlorpropamide、Glimepiride、Glipizide、Glyburide、Acetohexamide
  - 其他：Acarbose、人類胰島素

  與降血糖藥物併用時，宜留意血糖變化並加強監測。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型（證據等級 L5），沒有臨床試驗或文獻佐證。
- IGF-1R 阻斷在機轉上與透納氏症的生長需求相反，且排名前 10 的預測皆無合理的機轉依據。

**若要推進需要：**
- 取得香港衛生署的藥品仿單（警語、禁忌症與核准適應症），完成安全性初篩
- 補充詳細的作用機轉資料（MOA）
- 針對 monosomy X 進行機轉與前臨床研究，確認是否存在合理的生物學連結
- 若仍無支持證據，建議改為評估排名較後、但機轉更接近 IGF-1R 訊號的其他候選適應症
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

