---
layout: default
title: Valproic Acid
parent: 僅模型預測 (L5)
nav_order: 908
evidence_level: L5
indication_count: 5
---

# Valproic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Valproic Acid（丙戊酸）：從癲癇到三叉神經腫瘤

## 一句話總結

Valproic Acid 是廣譜抗癲癇藥，在香港以 Epilim Chrono 緩釋錠上市（許可證未載明適應症，癲癇為依藥理類別推斷）。
TxGNN 模型預測它可能對**三叉神經腫瘤 (Trigeminal Nerve Neoplasm)** 有效，但目前**沒有任何臨床試驗**，僅有 **1 篇文獻**，且該文獻談的是 Sturge-Weber 症候群，並非腫瘤，因此實質證據幾乎為零。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明（依藥理類別推斷為癲癇） |
| 預測新適應症 | 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Valproic Acid 是已知的組蛋白去乙醯化酶（HDAC）抑制劑，在前臨床研究中顯示抗腫瘤活性，所以一般性的抗腫瘤推論在機轉上說得通。

不過這個預測缺少臨床支持。唯一連結到的文獻是 1997 年的 Sturge-Weber 症候群病例系列，那是一種血管性神經皮膚疾病，不是三叉神經腫瘤。TxGNN 分數很高（0.9997），但這只是模型的圖譜推論，沒有任何實際臨床證據佐證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | 回顧 14 例 Sturge-Weber 症候群的臨床特徵、病程與治療反應；疾病與三叉神經腫瘤無直接關聯 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-39205 | EPILIM CHRONO TAB 500MG | SANOFI HONG KONG LIMITED |
| HK-39203 | EPILIM CHRONO TAB 200MG | SANOFI HONG KONG LIMITED |
| HK-39204 | EPILIM CHRONO TAB 300MG | SANOFI HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有臨床試驗，唯一的文獻也與目標疾病無關，屬於純模型預測（L5）。
- 香港仿單的警語與禁忌資料尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症
- 補充完整的作用機轉（MOA）資料
- 系統性搜尋 Valproic Acid 用於顱神經腫瘤或神經腫瘤的前臨床與臨床文獻
- 同一份資料中，**三叉神經痛 (Trigeminal Neuralgia)**（L3）與**視覺性癲癇 (Visual Epilepsy)**（L3）的證據較強，可優先作為研究問題。這兩項偏向既有抗癲癇或神經痛用途的延伸，不是全新的老藥新用。

> 本報告僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

