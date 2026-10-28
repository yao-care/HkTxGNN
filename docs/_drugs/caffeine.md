---
layout: default
title: Caffeine
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 8
monitor_inn: "CAFFEINE"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "trigeminal autonomic cephalalgia", "vein disease"]
last_modified_at: 2026-10-27
description: "Caffeine：預測新適應症為鼻腔疾病 (nasal cavity disease)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Caffeine
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

## Caffeine：腺苷受體拮抗型中樞神經興奮劑 → 鼻腔疾病 (nasal cavity disease)
{: .text-alpha }

## 一句話總結

Caffeine（咖啡因）是一種黃嘌呤類中樞神經興奮劑，在香港已有單方許可證上市。
TxGNN 模型預測它可能對**鼻腔疾病 (nasal cavity disease)** 有效，
但目前**沒有臨床試驗**，僅有 **3 篇間接相關文獻**（藥理學回顧、鼻用凝膠的前臨床製劑研究、動物實驗），無法直接支持此預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 鼻腔疾病 (nasal cavity disease) |
| TxGNN 預測分數 | 0.9991 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Caffeine 為腺苷受體拮抗劑與磷酸二酯酶抑制劑，並可能活化氣道的苦味受體（TAS2R）。這些受體分布於鼻腔與肺部，可能影響黏膜纖毛清除與局部先天免疫，因此在機轉上存在理論上的連結。

另有一項前臨床研究開發了咖啡因鼻用溫感凝膠，顯示經鼻給藥在技術上可行，但該研究針對的是睡眠剝奪後的認知表現，並非鼻腔疾病。

整體而言，這個預測的分數很高，但沒有任何研究直接以鼻腔疾病為對象，因此只能視為待驗證的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | 回顧 | Pharmacology & Therapeutics | 苦味受體表現於鼻腔與肺部等組織，回顧其藥理及在人類氣道的角色 |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | 前臨床製劑研究 | Current Drug Delivery | 咖啡因鼻用溫感凝膠用於改善睡眠剝奪後的認知，未涉及鼻腔疾病 |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | 動物實驗 | Cancer Research | 紅茶與咖啡因抑制大鼠肺部致癌，與鼻腔疾病無直接關聯 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67099 | CAFFEINE CITRATE SOLUTION FOR INJECTION 10MG/1ML | 未記載 | 未記載 |
| HK-64696 | PEYONA SOLUTION FOR INFUSION AND ORAL SOLUTION 20MG/ML | 未記載 | 未記載 |
| HK-50322 | CAFFEINE CITRATE INJ 10MG/ML | 未記載 | 未記載 |
| HK-01025 | HO CHAI KUNG TJI THUNG SAN | 未記載 | 未記載 |
| HK-50462 | NORMET TAB | 未記載 | 未記載 |

本地資料共列出 20 張有效許可證，此清單可能不完整，上表僅列出其中 5 張。

## 安全性考量

- **藥物交互作用**：已查得 75 筆交互作用，其中較需留意的有：
  - 重大：Cocaine（鼻用）、Cocaine（外用）
  - 中度：Alosetron、Obeticholic acid、Adenosine、Anagrelide、Bendamustine、Capmatinib、Ciprofloxacin、Cycloserine、Dipyridamole、Duloxetine 等
  - 輕度：Acetylsalicylic acid、Cimetidine、Atazanavir、Disulfiram

其他警語與禁忌資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然 TxGNN 分數很高（0.9991），但目前沒有任何研究直接探討 Caffeine 對鼻腔疾病的作用，僅有機轉推論與製劑可行性研究，證據等級為 L5。

**若要推進需要：**
- 取得詳細的作用機轉資料，特別是苦味受體在鼻黏膜的功能證據
- 以鼻腔疾病（如過敏性或血管運動性鼻炎）為對象的前臨床或探索性臨床研究
- 評估經鼻給藥的局部耐受性與全身暴露風險
- 取得香港原廠仿單的警語、禁忌與核准適應症文字，以完成安全性篩選
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

