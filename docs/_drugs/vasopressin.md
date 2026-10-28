---
layout: default
title: Vasopressin
parent: 僅模型預測 (L5)
nav_order: 928
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "VASOPRESSIN"
predicted_indications: ["congenital prothrombin deficiency", "drug-induced osteoporosis"]
description: "Vasopressin：預測新適應症為先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)（證據等級 L4）."
---

# Vasopressin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Vasopressin：從（原適應症未載明）到先天性凝血酶原缺乏症
{: .text-alpha }

## 一句話總結

Vasopressin（血管加壓素）在香港已有上市許可，但目前整理的資料中未載明其核准適應症。
TxGNN 模型預測它可能對**先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)** 有效，
但目前**沒有臨床試驗**，僅有 **3 篇文獻**，且內容多與去氨加壓素（desmopressin）相關，屬於間接證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency) |
| TxGNN 預測分數 | 0.9963 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Vasopressin 的相關文獻多半談的是其 V2 選擇性類似物去氨加壓素（DDAVP）。DDAVP 透過 V2 受體促使內皮細胞釋放儲存的第八凝血因子（FVIII）與血管性血友病因子（vWF），因此在 FVIII、FV 缺乏等狀態有合理的機轉依據。

然而，先天性凝血酶原（第二凝血因子）缺乏症並不屬於上述機轉可直接涵蓋的範圍，目前沒有已建立的機轉證據顯示 vasopressin 能改善凝血酶原缺乏。分數 0.9963 來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據。因此這個預測應視為待驗證的假說。

另外，檢索到的文獻研究對象是 desmopressin 而非 vasopressin 本身，不能直接推論 vasopressin 的療效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | 後天性血友病 A 的診斷、病因、臨床表現與治療選項回顧；病因為針對 FVIII 的自體抗體 |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case report | Rinsho Ketsueki | 1 例 43 歲男性先天性 FV、FVIII 合併缺乏，使用 DDAVP 治療（研究藥物為 desmopressin） |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case report | Rinsho Ketsueki | 1 例 25 歲孕婦先天性 FV、FVIII 合併缺乏，以 FVIII 濃縮製劑替代治療下完成剖腹產 |

這些文獻均未直接探討凝血酶原缺乏症，也未直接評估 vasopressin。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-07904 | PITRESSIN INJ 20U/ML | 未載明 | 未載明 |

製造商為 PFIZER CORPORATION HONG KONG LIMITED，狀態為有效。

---

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為部分主要項目：
  - **嚴重 (Major)**：Dolasetron、Cisapride、Papaverine、Macimorelin
  - **中度 (Moderate)**：Famotidine、Epinephrine、Loperamide、Chlorpropamide、Clarithromycin、Levofloxacin、Ondansetron、Granisetron、Palonosetron、Promethazine、Cilostazol、Heparin 等
  - **輕微 (Minor)**：Metronidazole

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何臨床試驗，文獻僅為間接證據（且研究藥物為 desmopressin），機轉上也缺乏支持 vasopressin 對凝血酶原缺乏的依據。TxGNN 分數高但證據僅達 L4。
- 另一個預測適應症「藥物引起的骨質疏鬆」僅有模型預測（L5），無任何研究支持，同樣建議 Hold。

**若要推進需要：**
- 補齊 vasopressin 的作用機轉資料（MOA）
- 取得香港仿單，確認核准適應症、警語與禁忌症
- 針對凝血酶原缺乏症，進行 vasopressin（而非 desmopressin）的機轉或前臨床研究
- 釐清 vasopressin 與 desmopressin 的差異，評估文獻證據是否可外推
- 評估與 QT 延長相關藥物（如 dolasetron、cisapride）等嚴重交互作用的風險管理
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

