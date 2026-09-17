---
layout: default
title: Vasopressin
parent: 僅模型預測 (L5)
nav_order: 791
evidence_level: L5
indication_count: 2
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

<div id="pharmacist">

## 藥師評估報告

</div>

# 血管加壓素（Vasopressin）：從（原適應症資料缺失）到先天性凝血酶原缺乏症

## 一句話總結

Vasopressin（血管加壓素，DrugBank ID：DB00067）目前無原適應症與作用機轉資料可供比對。
TxGNN 模型預測它可能對**先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)** 有效，
目前僅有 **3 篇文獻**、且與此適應症的直接關聯性偏弱，**無任何臨床試驗**支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（Evidence Pack 未提供） |
| 預測新適應症 | 先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Evidence Pack 中未提供 Vasopressin 的原適應症與 MOA 資訊，
因此無法從機轉角度說明其與先天性凝血酶原缺乏症之間的關聯性。

現有的 3 篇相關文獻，內容多聚焦於後天性血友病 A、先天性第 V 因子合併第 VIII 因子缺乏症，
以及 DDAVP（一種血管加壓素類似物）在凝血因子缺乏個案中的應用，但**均非直接針對「先天性凝血酶原缺乏症」或「Vasopressin」本身**的研究。
換言之，這個預測目前主要建立在 TxGNN 模型的關聯性推論上，尚缺乏直接的臨床或機轉證據支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21115138](https://pubmed.ncbi.nlm.nih.gov/21115138/) | 2011 | Review | Autoimmunity Reviews | 後天性血友病 A 的診斷、病因、臨床表現與治療選項回顧 |
| [2607619](https://pubmed.ncbi.nlm.nih.gov/2607619/) | 1989 | Case report | Rinsho Ketsueki | 先天性第 V 因子合併第 VIII 因子缺乏症個案中使用 DDAVP 治療 |
| [1942544](https://pubmed.ncbi.nlm.nih.gov/1942544/) | 1991 | Case report | Rinsho Ketsueki | 先天性第 V 因子合併第 VIII 因子缺乏症孕婦剖腹產時使用第 VIII 因子濃縮製劑替代治療 |

> 註：以上文獻均與「先天性凝血酶原缺乏症」及「Vasopressin」無直接對應關係，僅在凝血功能障礙領域具間接參考價值。

---

## 香港上市資訊

Vasopressin 目前在香港**未上市**，無許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（Evidence Pack 標註 TFDA 仿單警語/禁忌為「Blocking」等級的資料缺口，作用機轉資料則為「High」等級缺口，兩者均需補齊後方可進行安全性初評。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測目前僅有 TxGNN 模型分數與 3 篇關聯性薄弱的文獻支持，缺乏直接研究此藥物與此適應症的臨床或機轉證據。
- 藥物於香港未上市，且原適應症、作用機轉、仿單警語與禁忌等關鍵安全性資料均為缺口，尚無法進行安全性初評（S1）。

**若要推進需要：**
- 補齊 TFDA／原廠仿單的警語與禁忌資料（Blocking 等級缺口）
- 查詢 DrugBank API 取得完整作用機轉（MOA）資料（High 等級缺口）
- 補充原適應症資訊，以評估與先天性凝血酶原缺乏症之機轉關聯性
- 尋找直接研究 Vasopressin 於凝血因子缺乏症應用的臨床試驗或文獻
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

