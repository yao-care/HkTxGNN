---
layout: default
title: Prulifloxacin
parent: 中證據等級 (L3-L4)
nav_order: 745
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Prulifloxacin：預測新適應症為心臟疾病 (heart disease)（證據等級 L4）。原適應症：香港許可證未載明核准適應症"
monitor_inn: "PRULIFLOXACIN"
predicted_indications: ["heart disease", "Laubry-Pezzi syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "genetic syndromic Pierre Robin syndrome", "partial deletion of the long arm of chromosome 7"]
---

# Prulifloxacin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

## Prulifloxacin：從細菌感染（原適應症資料缺漏）到心臟疾病
{: .text-alpha }

## 一句話總結

Prulifloxacin 是一種氟喹諾酮類（fluoroquinolone）抗菌藥物，為 ulifloxacin 的前驅藥。
TxGNN 模型預測它可能對**心臟疾病 (heart disease)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇**動物實驗文獻，且該文獻討論的是心律不整的安全性風險，並非療效證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症 |
| 預測新適應症 | 心臟疾病 (heart disease) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知資訊，prulifloxacin 的活性代謝物 ulifloxacin 屬於氟喹諾酮類抗菌藥物，一般認為其作用是抑制細菌 DNA gyrase 與 topoisomerase IV。這一機轉與心臟疾病的病理並無明確關聯。

氟喹諾酮類藥物整體上帶有 QT 間期延長及心血管安全性的疑慮，因此該類藥物對心臟的訊號偏向風險而非助益。0.9994 的高分僅是模型預測，沒有臨床資料支持，且「heart disease」一詞範圍過於籠統。

其餘四個預測（Laubry-Pezzi 症候群、兩種 Pierre Robin 症候群、第 7 號染色體長臂部分缺失）皆為罕見先天性或染色體疾病，抗菌藥物沒有合理的藥理作用，推測是知識圖譜結構相似性造成的假訊號，且均無任何試驗或文獻。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15018156](https://pubmed.ncbi.nlm.nih.gov/15018156/) | 2004 | 前臨床動物研究 | The Journal of Toxicological Sciences | 以兔心律不整模型比較 prulifloxacin 活性代謝物 NM394（ulifloxacin）與 sparfloxacin、gatifloxacin、levofloxacin 的致心律不整作用與 QT 間期變化。屬安全性評估，並非心臟疾病療效研究。 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60581 | UNIDROX TAB 600MG（李氏大藥廠） | 未載明 | 未載明 |

---

## 安全性考量

- **類別性風險**：氟喹諾酮類藥物與 QT 間期延長及罕見的心室心律不整（如尖端扭轉型心室頻脈）有關，前述動物研究即在探討此問題。對於預測的新適應症為心臟疾病，這點尤其值得注意。

其餘警語、禁忌症及藥物交互作用資料未能取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但缺乏機轉依據與臨床證據；唯一的文獻是動物安全性研究，且氟喹諾酮類對心臟的訊號偏向風險。
- 其他四項預測同樣屬於缺乏合理藥理基礎的模型假訊號。

**若要推進需要：**
- 取得香港仿單的警語、禁忌症及核准適應症資料，完成安全性篩選
- 補齊詳細的作用機轉資料（DrugBank）
- 明確界定具體的心臟疾病亞型，並找出任何支持療效而非風險的實質證據
- 在有合理機轉與初步證據之前，不建議投入進一步的再利用研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

