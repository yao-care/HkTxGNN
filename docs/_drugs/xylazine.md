---
layout: default
title: Xylazine
parent: 僅模型預測 (L5)
nav_order: 803
evidence_level: L5
indication_count: 4
---

# Xylazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Xylazine：原適應症資料缺乏，探索偏頭痛（Migraine Disorder）方向

## 一句話總結

> Xylazine（DrugBank ID: DB11477）目前於香港未上市，本 Evidence Pack 亦未記載其原始核准適應症。
> TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
> 目前僅有 **0 個臨床試驗**和 **1 篇背景文獻**支持，且該文獻並非針對 xylazine 之直接研究。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本 Evidence Pack 未記載（無 original_indications 資料） |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.64%（KG 排名第 7,088 位） |
| 證據等級 | L5（僅有模型預測，無藥物特異性研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

官方作用機轉（MOA）資料目前缺失。根據 TxGNN 知識圖譜的推論路徑與藥理分類，xylazine 屬於 **α2-腎上腺素受體促效劑（α2-adrenergic agonist）**，與臨床上曾用於偏頭痛預防的 clonidine 屬同一藥理類別。

由於本 Evidence Pack 未記載 xylazine 的原始核准適應症（`original_indications` 為空），無法比較原適應症與新適應症之間的臨床關聯性。此處的機轉推論主要建立在**藥理類別效應**上：α2 促效劑被認為可透過調節血管張力與皮質擴散性去極化（cortical spreading depolarization）影響偏頭痛的發作機制。

需特別注意，唯一相關文獻（PMID 27122032）探討的是初級感覺皮質對擴散性去極化的易感性，屬於基礎神經科學背景研究，**並未針對 xylazine 進行實際測試**，此關聯純粹來自 TxGNN 知識圖譜的間接推論路徑，證據強度為最低等級 L5，仍需藥物特異性的臨床前或臨床研究佐證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27122032](https://pubmed.ncbi.nlm.nih.gov/27122032/) | 2016 | 基礎神經科學研究（非藥物特異） | The Journal of Neuroscience | 探討初級感覺皮質對擴散性去極化（spreading depolarization）的易感性，此現象與偏頭痛先兆的感覺症狀有關；研究並未涉及 xylazine，屬機轉背景文獻 |

---

## 香港上市資訊

Xylazine 目前於香港未取得任何藥品許可證（未上市），無許可證資料可列出。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（本 Evidence Pack 中主要警語、禁忌症與藥物交互作用資料均缺失，屬阻斷性資料缺口 DG001，需先取得 TFDA/原廠仿單資料才能進行安全性初評。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅為 L5，目前唯一相關文獻並非針對 xylazine 之直接研究，且無任何臨床試驗支持。
- 缺乏作用機轉（MOA）與仿單安全性資料（警語、禁忌症），無法進行基本的安全性初評（S1 階段被阻斷）。

**若要推進需要：**
- 取得 TFDA 或原廠仿單之警語與禁忌症資料（對應 DG001，屬阻斷性缺口）
- 補齊 xylazine 明確的作用機轉資料（對應 DG002）
- 尋找 xylazine 特異性的臨床前藥理研究或病例報告，驗證其對偏頭痛的實際效果
- 釐清 xylazine 於其他地區的原始核准適應症，以評估適應症延伸的合理性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

