---
layout: default
title: Sodium Carbonate
parent: 僅模型預測 (L5)
nav_order: 819
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
description: "Sodium Carbonate：預測新適應症為馬尾症候群 (Cauda Equina Syndrome)（證據等級 L5）。原適應症：許可證未載明"
monitor_inn: "Sodium carbonate"
predicted_indications: ["cauda equina syndrome", "anaphylaxis", "food-dependent exercise-induced anaphylaxis", "obsolete neurogenic bladder (disease)", "dry eye syndrome", "ventricular tachycardia"]
---

# Sodium Carbonate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Sodium carbonate：從（原適應症未載明）到 馬尾症候群（Cauda Equina Syndrome）等預測適應症
{: .text-alpha }

## 一句話總結

Sodium carbonate（碳酸鈉）是一種鹼化劑／緩衝劑，在香港有 1 張有效許可證，但許可證上未載明原適應症。
TxGNN 模型對多個疾病給出高分預測；在已整理的預測中，相對較值得探討的是**乾眼症 (Dry Eye Syndrome)** 與**乾燥症 (Sjögren Syndrome)**。
目前**沒有任何臨床試驗**，僅有 **1 篇間接相關文獻**，整體屬於模型預測階段，證據薄弱。

---

## 快速總覽

此處以預測排名第 1 的疾病呈現，其他預測見下方補充表。

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明 |
| 預測新適應症（排名第 1） | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 0.9980 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

### 前 10 名預測概覽

| 排名 | 預測疾病 | TxGNN 分數 | 證據等級 | 建議 |
|------|---------|-----------|---------|------|
| 1 | 馬尾症候群 (Cauda Equina Syndrome) | 0.9980 | L5 | Hold |
| 2 | 過敏性休克 (Anaphylaxis) | 0.9972 | L5 | Hold |
| 3 | 食物依賴運動誘發過敏性休克 | 0.9963 | L5 | Hold |
| 4 | 神經源性膀胱（本體論已淘汰術語） | 0.9962 | L5 | Hold |
| 5 | 乾眼症 (Dry Eye Syndrome) | 0.9958 | L5 | Research Question |
| 6 | 心室頻脈 (Ventricular Tachycardia) | 0.9918 | L5 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 sodium carbonate 屬於鹼化劑／緩衝劑，香港的上市產品為檸檬口味的 ENO 水果鹽（泡騰式抗酸類產品）。

就排名第 1 的馬尾症候群而言，這是需要手術處理的壓迫性神經急症，與鹼化劑之間找不到合理的機轉連結，其分數來自 TxGNN 模型（深度學習），可能只反映模型學到的相關疾病之間的相似性，並非生物學證據。過敏性休克、心律不整等其他預測也同樣沒有機轉或臨床支持。

相對而言，乾眼症與乾燥症有一項間接線索：一項 2017 年的探索性研究使用碳酸鈉／碳酸氫鈉與木糖醇噴劑，搭配專業口腔衛生處置，用於原發性乾燥症患者。其可能作用是局部緩衝唾液 pH 與清潔黏膜，只能視為口乾症狀的局部緩解，並非疾病修飾作用，也無法直接推論到眼表疾病。若要探討乾眼症，還需先確立鹼性溶液在眼部的安全性與耐受性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下為乾眼症與乾燥症預測共同對應的文獻，以及過敏性休克預測所連結的文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27813150](https://pubmed.ncbi.nlm.nih.gov/27813150/) | 2017 | 探索性臨床研究 | Gerodontology | 評估碳酸氫鈉／木糖醇噴劑搭配非手術牙周治療用於原發性乾燥症患者；可用的摘要被截斷，研究設計與人數無法確認 |
| [34600046](https://pubmed.ncbi.nlm.nih.gov/34600046/) | 2021 | 前臨床製劑／通透性研究 | Eur J Pharm Sci | 探討舌下腎上腺素的穩定性與通透性，並非以碳酸鈉作為治療；至多與製劑 pH 緩衝有關 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-20004 | LEMON FLAVOURED ENO FRUIT SALT（持有人：HALEON HONG KONG LIMITED） | 未載明 | 未載明 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第 1 的預測（馬尾症候群）及多數其他預測屬純計算推論，無試驗、無文獻、無機轉依據，證據等級為 L5。
- 乾眼症與乾燥症雖為 L4，但僅有一篇間接的口腔噴劑研究，不足以支持用於眼部或疾病治療，可列為後續研究問題（Research Question），而非推進開發。

**若要推進需要：**
- 取得詳細的作用機轉資料（MOA）
- 取得香港原廠仿單的警語與禁忌資訊，以進行安全性篩選
- 確認 PMID 27813150 的完整研究設計、樣本數與結果
- 若研究乾眼症，需先評估鹼性溶液的眼部安全性、耐受性及劑型／給藥途徑的相容性
- 釐清許可證上的核准適應症，以確認原適應症
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

