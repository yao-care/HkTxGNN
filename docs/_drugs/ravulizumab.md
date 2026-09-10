---
layout: default
title: Ravulizumab
parent: 僅模型預測 (L5)
nav_order: 637
evidence_level: L5
indication_count: 5
---

# Ravulizumab
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

# Ravulizumab：原適應症資料缺口，預測新適應症為先天性嗜中性球低下症（G6PC3缺乏型）

## 一句話總結

Ravulizumab（DrugBank DB11580）目前在香港未上市，且原始適應症與作用機轉資料均為缺口（Evidence Pack 標記為 Blocking／High 等級資料缺口）。
TxGNN 模型預測它可能對**體染色體隱性遺傳型重度先天性嗜中性球低下症（G6PC3缺乏型）**有效，
預測分數高達 **99.96%**，但目前**沒有任何臨床試驗或文獻**佐證。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（DrugBank 與許可證資料均未取得，見 DG002） |
| 預測新適應症 | 體染色體隱性遺傳型重度先天性嗜中性球低下症（G6PC3缺乏型）(Autosomal Recessive Severe Congenital Neutropenia due to G6PC3 Deficiency) |
| TxGNN 預測分數 | 99.96%（模型排名第 1301） |
| 證據等級 | L5（僅有模型預測，無臨床試驗或文獻） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Ravulizumab 的作用機轉（MOA）資料，且未取得原始核准適應症紀錄，因此無法進行機轉關聯性分析（此為 Evidence Pack 中分別標記為 High／Blocking 等級的資料缺口，見 DG002、DG001）。

TxGNN 模型是基於藥物-疾病知識圖譜的關聯強度進行預測。本次前 5 名預測適應症（G6PC3缺乏型重度先天性嗜中性球低下症、週期性血球生成症、原發性高草酸尿症、重度先天性嗜中性球低下症、CXCR2缺乏型重度先天性嗜中性球低下症）多集中於嗜中性球低下／造血系統相關的罕見遺傳疾病，顯示模型可能捕捉到某種共通的網路關聯模式，但因缺乏原始適應症與機轉資料佐證，此假說目前無法驗證，僅能視為模型層級的訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

Ravulizumab 目前於香港未取得藥品許可證（0 張），無登記資料可供列表。

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他預測候選（供參考）

| 排名 | 預測適應症 | TxGNN 分數 |
|------|-----------|-----------|
| 2 | 週期性血球生成症 (Cyclic Hematopoiesis) | 99.94% |
| 3 | 原發性高草酸尿症 (Primary Hyperoxaluria) | 99.90% |
| 4 | 重度先天性嗜中性球低下症 (Severe Congenital Neutropenia) | 99.87% |
| 5 | CXCR2缺乏型重度先天性嗜中性球低下症 | 99.86% |

以上候選同樣皆無臨床試驗或文獻佐證，僅為模型分數排序。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有 TxGNN 模型預測分數（99.96%），無任何臨床試驗或文獻支持，證據等級為最低的 L5。
- 安全性仿單資料（警語、禁忌）為 Blocking 等級資料缺口，無法進行 S1 安全性初評。
- 原始核准適應症與作用機轉皆未知，無法建立機轉關聯性論述。

**若要推進需要：**
- 取得 TFDA／原廠仿單中的警語與禁忌症（DG001，Blocking，優先處理）
- 透過 DrugBank API 查詢完整作用機轉資料（DG002，High）
- 補齊原始核准適應症紀錄，以利機轉關聯性分析
- 持續監測是否出現與此 5 項候選適應症相關的臨床試驗或文獻（目前查詢結果皆為 0 筆）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

