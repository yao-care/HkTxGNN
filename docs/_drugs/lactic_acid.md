---
layout: default
title: Lactic Acid
parent: 僅模型預測 (L5)
nav_order: 502
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lactic Acid：預測新適應症為非典型主動脈縮窄 (Atypical coarctation of aorta)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "Lactic acid"
predicted_indications: ["atypical coarctation of aorta", "aortic malformation", "non-syndromic esophageal malformation", "amenorrhea (disease)", "dry eye syndrome", "esophageal disease", "double outlet right ventricle with atrioventricular septal defect, pulmonary stenosis, heterotaxy", "excretory apparatus of the lacrimal system anomaly", "eye disease", "cauda equina syndrome"]
---

# Lactic Acid
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

# Lactic acid：從（原適應症未載明）到先天性主動脈縮窄（非典型）

## 一句話總結

Lactic acid（乳酸）是人體內源性代謝物，在香港有 7 張單一成分許可證，但本次整理的資料中未載明核准適應症。
TxGNN 模型預測它可能對**非典型主動脈縮窄 (atypical coarctation of aorta)** 有效，但目前**沒有任何臨床試驗與相關文獻**支持，僅為模型預測（L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 非典型主動脈縮窄 (Atypical coarctation of aorta) |
| TxGNN 預測分數 | 99.59% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。乳酸是內源性代謝物，在香港以外用溶液、火棉膠（collodion）、血液透析與血液濾過溶液，以及複方乳酸鈉注射液等形式上市。

在已整理的資料中，找不到任何文獻或試驗把乳酸與主動脈縮窄連結起來。主動脈縮窄是結構性先天異常，通常以手術或介入治療處理，藥理上缺乏讓乳酸發揮作用的合理途徑。0.996 的高分只反映知識圖譜上的鄰近關係，不能視為機轉證據。

其他排名前 10 的預測（如主動脈畸形、食道畸形、閉經、乾眼症、食道疾病、眼疾、馬尾症候群等）同樣沒有可信的治療機轉。部分文獻甚至顯示潛在的不利訊號，例如乳酸會上調巨噬細胞 VEGF 並促進脈絡膜新生血管，吲哚-3-乳酸則降低食道鱗狀細胞癌的抗 PD-1 療效。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測（非典型主動脈縮窄）目前無相關文獻。

為提供參考，以下列出排名第 2 的「主動脈畸形」中相關性最高的文獻。這些研究均與乳酸治療本身無直接關係：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3367436](https://pubmed.ncbi.nlm.nih.gov/3367436/) | 1988 | 前臨床/動物 | Journal of Vascular Surgery | 兔子主動脈縮窄模型中，研究主動脈壁呼吸與糖解代謝和動脈粥樣硬化易感性的關係 |
| [25157439](https://pubmed.ncbi.nlm.nih.gov/25157439/) | 2015 | 前臨床/動物（器械） | Catheterization and Cardiovascular Interventions | 聚左旋乳酸（PLLA）可降解支架用於兔降主動脈，評估可行性與中期結果；PLLA 是材料而非乳酸藥物 |
| [32382764](https://pubmed.ncbi.nlm.nih.gov/32382764/) | 2020 | 病例系列 | Pediatric Cardiology | 以 PLLA 可吸收微板外部懸吊，處理先天性心臟病嬰兒的支氣管軟化 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-42195 | VERRUFILM SOLUTION | 未載明 | 未載明 |
| HK-67340 | COLLOPAINT COLLODION | 未載明 | 未載明 |
| HK-67554 | DUOCARE COLLODION | 未載明 | 未載明 |
| HK-67322 | COLLOFILM COLLODION | 未載明 | 未載明 |
| HK-12847 | DUOFILM LIQ | 未載明 | 未載明 |

另有 2 張許可證：HK-55926（複方乳酸鈉哈特曼氏注射液）與 HK-62237（PRISMASOL B0，血液濾過與血液透析溶液），共 7 張，皆為有效的單一成分許可證。

---

## 安全性考量

- **藥物交互作用**：共查得 17 筆交互作用，無嚴重等級，以中度與輕度為主。
  - 中度：Doxycycline、Tetracycline、Minocycline、Demeclocycline、Oxytetracycline、Acetylsalicylic acid、Salicylic acid (sodium)、Ephedrine、Pseudoephedrine
  - 輕度：Chlorpropamide、Tolazamide、Glipizide、Glyburide、Acetohexamide、Tolbutamide、Methotrexate

其餘警語與禁忌症資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症皆停留在 L5，沒有臨床試驗，文獻也無法支持乳酸作為治療藥物。
- 首位預測是需手術或介入處理的結構性先天異常，缺乏藥理合理性；部分適應症（食道疾病、眼疾）的文獻甚至出現不利訊號。

**若要推進需要：**
- 釐清乳酸在香港各許可證下的核准適應症與劑型。
- 取得詳細的作用機轉資料，評估與任一預測適應症的機轉關聯。
- 取得原廠仿單的警語與禁忌症，完成安全性篩選。
- 若仍要探索，建議優先重新篩選機轉較合理的適應症（如與乳酸代謝或局部外用相關的皮膚、婦科方向），並先進行前臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

