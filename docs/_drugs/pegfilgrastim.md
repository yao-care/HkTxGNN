---
layout: default
title: Pegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 658
evidence_level: L5
indication_count: 2
---

# Pegfilgrastim
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

# Pegfilgrastim：從嗜中性白血球減少症到嚴重非增殖性糖尿病視網膜病變

## 一句話總結

Pegfilgrastim 是長效型 G-CSF（顆粒球群落刺激因子）類似物，一般用於嗜中性白血球減少症（Evidence Pack 未收錄原適應症，此為一般藥理知識）。
TxGNN 模型預測它可能對**嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)** 有效。
目前**0 個臨床試驗**和 **0 篇文獻**支持，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（香港許可證未載明核准適應症） |
| 預測新適應症 | 嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

另有一個相關預測：**糖尿病視網膜病變 (Diabetic Retinopathy)**，分數 99.73%。它是上述疾病的上位概念，兩者不是獨立證據。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Pegfilgrastim 屬於 G-CSF 類藥物，一般用途與嗜中性白血球的生成有關，但其在糖尿病視網膜病變的機轉無法從現有資料驗證。

一個尚未驗證的假說是：G-CSF 可能動員骨髓來源的前驅細胞，進而影響糖尿病微血管的修復。但這只是推測。促血管新生或發炎相關的作用在晚期視網膜病變中也可能有害，作用方向目前未知。

99.89% 的高分是知識圖譜中的關聯，不是臨床證據。原適應症與新適應症的關聯性（相似度）也尚待評估。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-54933 | NEULASTIM PRE-FILLED SYRINGE INJ 6MG/0.6 ML | AMGEN HONG KONG LIMITED |
| HK-66770 | FULPHILA SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 6MG/0.6ML | PRIMEDICA LIMITED |
| HK-67124 | ZIEXTENZO SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 6MG/0.6ML | SANDOZ HONG KONG LIMITED |
| HK-68176 | PELGRAZ SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 6MG/0.6ML | JACOBSON MARKETING LIMITED |

四張許可證皆為預填充針筒注射劑（6 mg/0.6 mL），許可證資料未載明核准適應症。

---

## 安全性考量

安全性資訊請參考原廠仿單。

藥物交互作用查詢無結果。香港衛生署仿單的警語與禁忌尚未取得，這是目前的阻斷性資料缺口。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有 TxGNN 模型預測（L5），沒有任何臨床試驗或文獻。
- 作用方向不明，促血管新生或發炎效應還可能對晚期視網膜病變有害，所以不建議推進。

**若要推進需要：**
- 針對「G-CSF 與糖尿病視網膜病變」做專門文獻搜尋（前臨床與臨床）
- 補齊 DrugBank 的作用機轉資料，再分析機轉關聯
- 取得香港衛生署仿單的警語與禁忌資料，才能進入安全性篩選
- 評估給藥途徑相容性：目前為皮下注射預填充針筒，眼科用途所需途徑尚未釐清
- 評估原適應症與新適應症的相似度

---

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

