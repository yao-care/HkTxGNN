---
layout: default
title: Hydroquinone
parent: 中證據等級 (L3-L4)
nav_order: 438
evidence_level: L4
indication_count: 4
---

# Hydroquinone
{: .fs-9 }

證據等級: **L4** | 預測適應症: **4** 個
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

# Hydroquinone：預測新適應症為脂漏性角化症 (Seborrheic Keratosis)

## 一句話總結

Hydroquinone（對苯二酚）是外用美白／淡斑成分，在香港有含此成分的乳膏上市。
TxGNN 模型預測它可能對**脂漏性角化症 (Seborrheic Keratosis)** 有效，
但目前**沒有直接相關的臨床試驗**，只有 **2 篇間接文獻**，證據仍屬初步。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 脂漏性角化症 (Seborrheic Keratosis) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏經 DrugBank 確認的作用機轉資料。以下說明是根據 Hydroquinone 已知的藥理作用推論，尚未經資料庫驗證。Hydroquinone 會抑制酪胺酸酶 (tyrosinase)，減少黑色素合成，因此常用於淡化色素沉著。

脂漏性角化症及其變異型黑色丘疹性皮膚病 (dermatosis papulosa nigra) 的病灶常帶有色素。從機轉上看，Hydroquinone 有機會淡化這些病灶的顏色。但它不作用於角質細胞增生，所以無法針對病灶本身。這個連結偏向美觀層面且屬間接，不能視為疾病治療的直接證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33046430](https://pubmed.ncbi.nlm.nih.gov/33046430/) | 2021 | 前瞻性觀察研究 | J Plast Reconstr Aesthet Surg | 針對亞洲患者臉部色素性疾病提出組合治療流程；研究對象為一般色素疾病，並非專門針對脂漏性角化症 |
| [17373158](https://pubmed.ncbi.nlm.nih.gov/17373158/) | 2007 | Review | J Drugs Dermatol | 回顧黑色丘疹性皮膚病的治療選項；其組織學與脂漏性角化症無明顯差異，患者多因美觀求診 |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-64187 | TRI-LUSTRA CREAM | LSB (HK) LIMITED |
| HK-54161 | TRI-LUMA CREAM | GALDERMA HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 模型分數很高，但沒有直接針對脂漏性角化症的臨床試驗，現有文獻也只是間接相關。
- 機轉上只能淡化色素，無法處理角質細胞增生，因此不建議推進。

**若要推進需要：**
- 取得香港衛生署 (Department of Health) 仿單的警語與禁忌資料，這是進入安全性篩選的必要條件
- 補齊 DrugBank 的作用機轉資料
- 尋找或設計針對脂漏性角化症（或黑色丘疹性皮膚病）的對照試驗
- 確認外用劑型與目標病灶的給藥途徑是否相容

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證後方可應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

