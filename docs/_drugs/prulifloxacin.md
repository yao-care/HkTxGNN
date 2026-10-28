---
layout: default
title: Prulifloxacin
parent: 僅模型預測 (L5)
nav_order: 745
evidence_level: L5
indication_count: 10
monitor_inn: "PRULIFLOXACIN"
predicted_indications: ["heart disease", "Laubry-Pezzi syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "genetic syndromic Pierre Robin syndrome", "partial deletion of the long arm of chromosome 7", "orofacial clefting syndrome", "pulmonary valve disease", "disorder of fucoglycosan synthesis", "mitral valve disease", "Jeune syndrome situs inversus"]
last_modified_at: 2026-10-28
description: "Prulifloxacin：預測新適應症為心臟疾病 (heart disease)（證據等級 L5）。原適應症：本次整理的資料中，香港許可證未載明核准適應症"
---

# Prulifloxacin
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

## Prulifloxacin：從細菌感染到心臟疾病（heart disease）
{: .text-alpha }

## 一句話總結

Prulifloxacin 是氟喹諾酮類抗菌藥物 ulifloxacin 的前驅藥，在香港已有一張上市許可證。
TxGNN 模型預測它可能對**心臟疾病 (heart disease)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇**動物實驗文獻，且該文獻探討的是心律不整的安全風險，而非療效。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次整理的資料中，香港許可證未載明核准適應症 |
| 預測新適應症 | 心臟疾病 (heart disease) |
| TxGNN 預測分數 | 0.9994 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥物分類，prulifloxacin 是氟喹諾酮類抗菌藥物 ulifloxacin 的前驅藥，一般認為其作用是抑制細菌的 DNA gyrase 與 topoisomerase IV。

就目前資料而言，找不到能連結此機轉與心臟疾病治療的生物學依據。此高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

此外，氟喹諾酮類藥物有 QT 間期延長的心臟安全疑慮，這反而不利於把它用於心臟疾病。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15018156](https://pubmed.ncbi.nlm.nih.gov/15018156/) | 2004 | 動物實驗（臨床前） | The Journal of Toxicological Sciences | 在兔子心律不整模型中，比較 prulifloxacin 活性代謝物 NM394 (UFX) 與 sparfloxacin 等三種喹諾酮類藥物對 QT 間期與致心律不整的影響。此研究屬安全性評估，並非心臟疾病的療效證據。 |

此文獻探討的是藥物引發心律不整的風險，並未證明對心臟疾病有治療效果。依規則，沒有研究直接探討預測疾病的療效，因此證據等級定為 L5。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60581 | UNIDROX TAB 600MG | 未載明 | 未載明 |

## 安全性考量

- **心臟安全性**：臨床前研究（PMID 15018156）評估氟喹諾酮類藥物的 QT 間期延長與致心律不整風險，顯示此類藥物需留意心臟安全，對心臟疾病族群尤須審慎。

其餘安全性資訊（警語、禁忌症、藥物交互作用）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，唯一的文獻是安全性動物研究，且機轉上缺乏連結，預測分數高來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。
- 氟喹諾酮類的心臟安全疑慮，與心臟疾病的治療方向相悖。

**若要推進需要：**
- 取得香港仿單，確認核准適應症、警語與禁忌症
- 補充詳細的作用機轉資料
- 若仍想探索，需先釐清具體的心臟疾病類型，並提出直接支持療效的臨床前或臨床研究，同時完成心臟安全性（QT）評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

