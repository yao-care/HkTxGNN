---
layout: default
title: Titanium Dioxide
parent: 僅模型預測 (L5)
nav_order: 883
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Titanium Dioxide：預測新適應症為藥物誘發性骨質疏鬆症 (Drug-induced Osteoporosis)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "Titanium dioxide"
predicted_indications: ["drug-induced osteoporosis", "diabetic retinopathy", "diabetic cataract", "severe nonproliferative diabetic retinopathy", "immature cataract", "tetanic cataract", "mature cataract", "diabetes mellitus type 2 associated cataract", "craniostenosis cataract", "nuclear senile cataract"]
---

# Titanium Dioxide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Titanium dioxide：從（原適應症未載明）到藥物誘發性骨質疏鬆症
{: .text-alpha }

## 一句話總結

Titanium dioxide（二氧化鈦）在香港以 EPICOR CREAM 單方製劑上市，但本報告彙整的資料中沒有載明其核准適應症。
TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆症 (Drug-induced Osteoporosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 藥物誘發性骨質疏鬆症 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 99.9998% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Titanium dioxide 主要作為惰性賦形劑、色素與紫外線濾劑使用，並不是傳統意義上具有明確藥理標的的活性成分。

從現有資料來看，找不到能連結二氧化鈦與藥物誘發性骨質疏鬆症的機轉。TxGNN 分數雖然極高，但沒有任何臨床試驗或文獻佐證，**這個預測很可能是知識圖譜運算產生的假象 (artifact)**，不宜視為有意義的治療訊號。

其他排名前 10 的預測（糖尿病視網膜病變、各型白內障等）同樣沒有可支持的證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測（藥物誘發性骨質疏鬆症），目前無相關文獻。

作為參考，排名第 2 的預測「糖尿病視網膜病變」檢索到 5 篇文獻，但**均未顯示治療療效**：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36197877](https://pubmed.ncbi.nlm.nih.gov/36197877/) | 2022 | 分析方法 | Analytical Chemistry | 用 TiO2 微粒純化血漿細胞外囊泡，作為分析工具 |
| [41637842](https://pubmed.ncbi.nlm.nih.gov/41637842/) | 2026 | Review | J Trace Elem Med Biol | 金屬奈米粒子在糖尿病的機轉與治療展望，與視網膜病變僅間接相關 |
| [38078945](https://pubmed.ncbi.nlm.nih.gov/38078945/) | 2023 | 分析方法 | Analytical Chemistry | 細胞外囊泡與脂蛋白攜帶之循環 RNA 分析系統 |
| [39566751](https://pubmed.ncbi.nlm.nih.gov/39566751/) | 2025 | 前臨床影像 | Methods | 超小 TiO2 奈米粒子－螢光素結合物用於眼底螢光血管攝影（診斷用途） |
| [20059246](https://pubmed.ncbi.nlm.nih.gov/20059246/) | 2009 | 技術/模型研究 | J Biomed Optics | 視網膜血氧測量用的動態眼球模型 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-01669 | EPICOR CREAM | 未載明 | 未載明 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測均為 L5（僅有模型預測），沒有臨床試驗，文獻也未顯示治療效果，且缺乏機轉依據。
- 二氧化鈦主要是惰性賦形劑與紫外線濾劑，預測結果很可能是圖譜假象，不建議投入資源。

**若要推進需要：**
- 取得香港衛生署仿單，確認原適應症、警語與禁忌症
- 補充作用機轉資料（例如查詢 DrugBank）
- 提出二氧化鈦與骨代謝（或眼科疾病）的生物學合理性，並找到前臨床證據
- 釐清劑型與給藥途徑是否能達到目標組織
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

