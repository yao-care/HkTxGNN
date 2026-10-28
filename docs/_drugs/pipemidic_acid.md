---
layout: default
title: Pipemidic Acid
parent: 僅模型預測 (L5)
nav_order: 702
evidence_level: L5
indication_count: 10
monitor_inn: "PIPEMIDIC ACID"
predicted_indications: ["heart disease", "Laubry-Pezzi syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "genetic syndromic Pierre Robin syndrome", "partial deletion of the long arm of chromosome 7", "orofacial clefting syndrome", "pulmonary valve disease", "disorder of fucoglycosan synthesis", "mitral valve disease", "Jeune syndrome situs inversus"]
last_modified_at: 2026-10-23
description: "Pipemidic Acid：預測新適應症為心臟疾病（證據等級 L5）。原適應症：本報告所整理的資料中未載明"
---

# Pipemidic Acid
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

## Pipemidic Acid：從泌尿道感染相關用途到心臟疾病（模型預測）
{: .text-alpha }

## 一句話總結

Pipemidic Acid（吡哌酸）是一種喹諾酮類抗菌藥物，在香港已有上市許可證，但本報告所整理的資料中未載明核准適應症文字。
TxGNN 模型（深度學習）預測它可能對**心臟疾病 (heart disease)** 有效，但目前**沒有臨床試驗**，只有 **1 篇 1978 年的文獻**，且該文獻談的是腎功能不全與血液透析時的抗菌使用，並非心臟疾病。這個分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據，缺乏藥理支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本報告所整理的資料中未載明 |
| 預測新適應症 | 心臟疾病 |
| TxGNN 預測分數 | 0.9993 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

說明：資料中雖將此預測標為 L4，但唯一的文獻並未直接研究心臟疾病，依規則證據等級只能是 L5。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般已知 Pipemidic Acid 是喹諾酮類抗菌藥，作用於細菌 DNA 旋轉酶與拓撲異構酶 IV，用於抗菌治療。

心臟疾病屬於心血管結構或功能問題，與細菌拓撲異構酶抑制之間**沒有可信的機轉連結**。唯一檢索到的文獻討論的是此藥作為腎功能不全與血液透析患者的腎外抗生素，並未涉及心臟疾病。

因此，0.9993 的高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，不是藥理上的真實訊號，也不是生物學證據。其他排名前 10 的預測（如 Laubry-Pezzi 症候群、Pierre Robin 症候群、二尖瓣疾病、肺動脈瓣疾病等）同樣找不到合理機轉，多為先天性或結構性疾病，抗菌藥無對應標靶。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [372558](https://pubmed.ncbi.nlm.nih.gov/372558/) | 1978 | 臨床／回顧 | Journal d'urologie et de nephrologie | 探討 Pipemidic Acid 在腎功能不全與血液透析患者作為腎外抗生素的使用；未涉及心臟疾病，無摘要可供進一步摘要 |

此文獻並未直接研究心臟疾病，不能視為支持此預測的證據。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-32130 | UROTRACTIN CAP 400MG | 未載明 | 未載明 |

此為單一成分製劑，製造商為 DCH Auriga (Hong Kong) Limited - Healthcare Division，狀態為有效。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，唯一文獻未涉及心臟疾病，證據等級僅為 L5。
- 機轉上沒有合理連結，高分來自 TxGNN 模型（深度學習），可能只反映模型學到的相關疾病之間的相似性，並非生物學證據，不宜投入資源推進。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 取得詳細的作用機轉資料
- 若仍想探討此方向，需先有直接針對心臟疾病（例如感染性心內膜炎等具體情境）的機轉或前臨床證據
- 否則建議將此藥維持在原本的抗菌用途，不作為心臟疾病的再利用候選
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

