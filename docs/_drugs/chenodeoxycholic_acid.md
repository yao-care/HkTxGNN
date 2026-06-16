---
layout: default
title: Chenodeoxycholic Acid
parent: 中證據等級 (L3-L4)
nav_order: 158
evidence_level: L4
indication_count: 5
---

# Chenodeoxycholic Acid
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Chenodeoxycholic Acid：從腦腱黃瘤病到同合子家族性高膽固醇血症

## 一句話總結

Chenodeoxycholic acid (CDCA) 是人體天然初級膽汁酸，在腦腱黃瘤病（CTX）治療中已有明確地位，透過補充膽汁酸來修正 CYP27A1 缺陷導致的代謝失調。TxGNN 模型預測它可能對**同合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia, HoFH)** 有效，目前有 **0 個臨床試驗**和 **1 篇間接文獻**支持這個方向，整體證據極為有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腦腱黃瘤病（CTX）— 膽汁酸合成缺陷症（資料庫無正式許可紀錄，依文獻佐證） |
| 預測新適應症 | 同合子家族性高膽固醇血症 (Homozygous Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

CDCA 的主要作用機轉目前缺乏詳細資料記錄（Data Gap）。根據已知文獻，CDCA 作為初級膽汁酸，可透過激活核受體 **FXR（Farnesoid X Receptor）**，進而抑制 CYP7A1（膽固醇 7α-羥化酶），減少膽固醇向膽汁酸轉化的整體通量。在 CTX 中，CDCA 的補充可修正 CYP27A1 基因突變導致的膽汁酸缺乏，抑制膽固醇醇（cholestanol）的異常堆積。

然而，CDCA 對 HoFH 的機轉關聯性相當薄弱。**HoFH 的核心病理為 LDL 受體功能完全喪失**，導致循環中 LDL-C 極度升高。CDCA 透過 FXR-SHP 路徑雖可微幅調節肝臟脂質代謝，但對 LDL 受體缺失的代償效果極為有限，遠不及 PCSK9 抑制劑、lomitapide 或血漿置換等現有 HoFH 標準療法。

TxGNN 的高預測分數（99.57%）很可能來自知識圖譜中 **CTX ↔ 膽固醇代謝 ↔ HoFH** 的共享節點連結，屬間接機轉推斷，而非直接治療路徑的證據。目前唯一相關文獻（CTX 綜合回顧）亦未涉及 CDCA 對 HoFH 的療效研究，需審慎看待此預測的臨床轉化潛力。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [25424010](https://pubmed.ncbi.nlm.nih.gov/25424010/) | 2014 | Narrative Review | Orphanet Journal of Rare Diseases | CTX 完整回顧：CYP27A1 基因突變導致膽汁酸合成減少及膽固醇醇異常堆積，CDCA 是目前主要治療選項 |

> ⚠️ 注意：此篇文獻為 CTX 疾病回顧，並非針對 HoFH 的 CDCA 治療研究，與預測適應症僅有間接關聯。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- HoFH 的核心缺陷（LDL 受體功能完全喪失）與 CDCA 的膽汁酸代謝機轉缺乏直接藥理關聯，無法預期有意義的臨床療效
- 目前完全缺乏 CDCA 用於 HoFH 的臨床試驗，唯一文獻為 CTX 的間接回顧，無法支撐推進決策

**若未來要重新評估，需要：**
- 確認 CDCA 完整的作用機轉資料（MOA），特別是 FXR 路徑對 LDL-C 的調控幅度量化
- 評估 CDCA 在混合性脂質代謝障礙（非純 LDL 受體缺失型）的潛在應用場景
- 確認當前許可規格及安全性資訊（藥品仿單警語、禁忌症、DDI），目前均為資料缺口
- 注意 Rank 4、5 預測適應症（家族性混合高脂血症、高尿酸血症）在資料庫中已標記為 **obsolete（廢棄術語）**，若沿用需先核對當前疾病分類
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

