---
layout: default
title: Moroctocog Alfa
parent: 僅模型預測 (L5)
nav_order: 598
evidence_level: L5
indication_count: 8
monitor_inn: "MOROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
last_modified_at: 2026-10-28
description: "Moroctocog Alfa：預測新適應症為原發性血小板釋放障礙（證據等級 L5）。原適應症：知識圖譜記錄為血友病"
---

# Moroctocog Alfa
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

## Moroctocog alfa：從血友病到原發性血小板釋放障礙
{: .text-alpha }

## 一句話總結

Moroctocog alfa 是重組第八凝血因子（B 區域刪除型），在 TxGNN 知識圖譜中記錄的原有用途為血友病。
TxGNN 模型預測它可能對**原發性血小板釋放障礙 (primary release disorder of platelets)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄為血友病（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 原發性血小板釋放障礙 |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Moroctocog alfa 是重組第八凝血因子，作用是補充內源性凝血路徑中缺乏的第八因子，用於血友病相關出血的治療。

血小板釋放障礙是血小板顆粒分泌功能的缺陷，並非第八因子缺乏，兩者在機轉上的關聯薄弱。即使有任何益處，也只可能是間接的（例如支持凝血酶生成），屬於推測。高預測分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據。

其他排名較前的預測疾病（資料中共 8 項）同樣缺乏證據：

| 排名 | 預測疾病 | 預測分數 | 機轉關聯評估 |
|------|---------|---------|-------------|
| 2 | 假性血管性血友病 (pseudo-von Willebrand disease) | 0.9997 | 缺陷在血小板 GPIbα，外源性第八因子無法矯正主要缺陷，僅在路徑層面可能合理 |
| 3 | 血小板無力症 (Glanzmann thrombasthenia) | 0.9996 | 缺陷在整合素 αIIbβ3，標準處置為血小板輸注、重組第七因子與抗纖溶藥，無支持證據 |
| 4 | 後天性凝血因子缺乏 (acquired coagulation factor deficiency) | 0.9988 | 機轉上最連貫，但後天性血友病多由抑制性自體抗體造成，標準第八因子常無效，且此詞也涵蓋第八因子無法補充的其他因子缺乏 |
| 5 | Scott 症候群 | 0.9986 | 第八因子屬於 tenase 複合物，路徑上有鬆散關聯，但補充第八因子無法恢復缺失的膜表面 |
| 6 | 膠原蛋白受體缺陷所致出血體質 | 0.9973 | 血小板功能障礙且第八因子正常，無明確作用標的 |
| 7 | 先天性血小板低下所致出血性疾病 | 0.9972 | 問題在血小板數量或功能，補充第八因子無法解決 |
| 8 | flood factor deficiency | 0.9911 | 術語不明確，無法對應已知凝血疾病，需先釐清 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66835 | XYNTHA 凍乾粉末及溶劑注射液 250IU | 注射劑（粉末及溶劑） | 資料未載明 |
| HK-66834 | XYNTHA 凍乾粉末及溶劑注射液 1000IU | 注射劑（粉末及溶劑） | 資料未載明 |
| HK-66836 | XYNTHA 凍乾粉末及溶劑注射液 500IU | 注射劑（粉末及溶劑） | 資料未載明 |

三張許可證均為單一成分產品，持有人為 Pfizer Corporation Hong Kong Limited，狀態皆為有效。

## 安全性考量

安全性資訊請參考原廠仿單。目前針對藥物交互作用的查詢也未找到相關紀錄。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測的新適應症都只有模型預測，沒有臨床試驗或文獻直接研究，證據等級為 L5。
- 排名第一的血小板釋放障礙在機轉上與第八因子缺乏無關，高分數不足以支持推進。

**若要推進需要：**
- 補充詳細的作用機轉資料與香港仿單中的核准適應症、警語及禁忌症。
- 優先評估機轉上較合理的「後天性凝血因子缺乏」，並釐清抑制性抗體問題。
- 釐清「flood factor deficiency」的定義，確認是否為資料誤植。
- 先進行系統性文獻檢索與臨床前或機轉研究，再考慮是否值得啟動臨床研究。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

