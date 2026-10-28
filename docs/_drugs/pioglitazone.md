---
layout: default
title: Pioglitazone
parent: 僅模型預測 (L5)
nav_order: 701
evidence_level: L5
indication_count: 9
monitor_inn: "PIOGLITAZONE"
predicted_indications: ["opsismodysplasia", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy", "pancreatic agenesis"]
last_modified_at: 2026-10-28
description: "Pioglitazone：預測新適應症為Opsismodysplasia（骨發育不良症）（證據等級 L5）。原適應症：第二型糖尿病"
---

# Pioglitazone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Pioglitazone：從第二型糖尿病到類脂肪營養不良與罕見疾病（預測首位：Opsismodysplasia）
{: .text-alpha }

## 一句話總結

Pioglitazone 是 PPAR-gamma 促效劑（胰島素增敏劑），在知識圖譜中記錄的用途為第二型糖尿病。
TxGNN 模型預測它可能對**骨發育不良症 (Opsismodysplasia)** 有效，但目前**沒有任何臨床試驗或直接研究該疾病的文獻**，僅屬模型預測（證據等級 L5）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第二型糖尿病（知識圖譜中記錄的關聯；本次整理的香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | Opsismodysplasia（骨發育不良症） |
| TxGNN 預測分數 | 0.9959 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Pioglitazone 屬於 thiazolidinedione 類，為 PPAR-gamma 促效劑，可提升胰島素敏感性。

Opsismodysplasia 是由 INPPL1 突變（SHIP2 缺陷）引起的罕見骨骼發育不良，會影響 PI3K/AKT 與胰島素訊號。此與 Pioglitazone 之間的連結僅屬推測，分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病間學到的相似性，並非生物學證據。此外，thiazolidinedione 可能降低骨形成、增加骨折風險，用於骨骼疾病存在潛在安全疑慮。

其他排名較前的預測包括：

| 排名 | 預測疾病 | 分數 | 說明 |
|------|---------|------|------|
| 2 | 典型僵人症候群 (Classic stiff person syndrome) | 0.9950 | 可能因與糖尿病、自體免疫共病而被關聯；僅有理論上的 PPAR-gamma 抗發炎機轉 |
| 3 | 局部僵硬肢症候群 (Focal stiff limb syndrome) | 0.9950 | 與僵人症候群分數相同，應是疾病相似性傳遞 |
| 4 | 硫胺素反應性功能障礙症候群 | 0.9948 | 以硫胺素補充為既定療法 |
| 5–8 | 各類局部脂肪營養不良 | 0.9918–0.9930 | PPAR-gamma 促進脂肪細胞分化有理論依據，但局部病灶使用全身性治療的益處存疑 |
| 9 | 胰臟發育不全 (Pancreatic agenesis) | 0.9918 | Pioglitazone 需有內源性胰島素才有效，機轉上不太可能有益 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

首位預測（Opsismodysplasia）目前無相關文獻。
以下 7 篇為排名第 9 之胰臟發育不全所檢索到的文獻，內容均涉及第二型糖尿病、thiazolidinedione 或 PPAR 促效劑，並未直接研究該疾病，僅供背景參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16644631](https://pubmed.ncbi.nlm.nih.gov/16644631/) | 2006 | RCT | Diabetes Care | Muraglitazar 與 Pioglitazone 對照，用於二甲雙胍控制不佳的第二型糖尿病，改善血糖與血脂 |
| [22068250](https://pubmed.ncbi.nlm.nih.gov/22068250/) | 2012 | Review | Endocr Pract | 針對胰島素阻抗與 β 細胞功能障礙治療糖尿病前期 |
| [20859539](https://pubmed.ncbi.nlm.nih.gov/20859539/) | 2010 | Review | Vasc Health Risk Manag | Pioglitazone 與 alogliptin 合併治療第二型糖尿病 |
| [23680744](https://pubmed.ncbi.nlm.nih.gov/23680744/) | 2013 | Review | Hosp Pract | Thiazolidinedione 的多重效應，包含保護 β 細胞功能 |
| [15892654](https://pubmed.ncbi.nlm.nih.gov/15892654/) | 2005 | Review | Curr Mol Med | PPAR-gamma 促效劑的臨床意義 |
| [15832493](https://pubmed.ncbi.nlm.nih.gov/15832493/) | 2002 | Review | Treat Endocrinol | Rosiglitazone 用於第二型糖尿病 |
| [12149047](https://pubmed.ncbi.nlm.nih.gov/12149047/) | 2002 | Review | Drugs | Rosiglitazone 用於第二型糖尿病的回顧 |

## 香港上市資訊

目前整理到至少 20 張單一成分許可證（清單可能不完整），皆為有效狀態。以下列出 5 張：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-57967 | ZOLID TAB 45MG | 未載明 | 未載明 |
| HK-47884 | ACTOS TAB 30MG | 未載明 | 未載明 |
| HK-47882 | ACTOS TAB 15MG | 未載明 | 未載明 |
| HK-58692 | APO-PIOGLITAZONE TAB 30MG | 未載明 | 未載明 |
| HK-56745 | GLITTER-15 TAB 15MG | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜中記錄的禁忌關聯（非仿單內容）**：腎臟疾病、肝臟疾病、膽囊疾病、充血性心衰竭、腎上腺皮質功能不全 (Addison 病)、多種腦下垂體功能不全與低促性腺激素性性腺功能低下等。
- **藥物交互作用**：共檢索到 100 筆，以下為部分範例。
  - 中度：Abiraterone、Phenylephrine、Acetazolamide、Formoterol、Pseudoephedrine、Epinephrine、Hydrocortisone、Salbutamol、Ethanol、Hydrochlorothiazide、Alpelisib
  - 輕度：Nifedipine、Ethinylestradiol、Lipoic acid、Amcinonide

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測均無臨床試驗或直接針對該疾病的文獻支持，僅為 TxGNN 模型（深度學習）的預測，可能反映模型從相關疾病間學到的相似性，並非生物學證據（L5）。
- 首位預測的骨骼疾病還有骨質安全疑慮；胰臟發育不全在機轉上也不合理。

**若要推進需要：**
- 補充作用機轉資料與香港仿單的警語、禁忌。
- 優先評估機轉較合理的方向（如脂肪營養不良類），先做系統性文獻回顧與病例資料蒐集。
- 針對首位預測，進行 INPPL1/SHIP2 與 PPAR-gamma 的前臨床機轉研究，並評估骨骼安全性。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

