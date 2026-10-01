---
layout: default
title: Papain
parent: 僅模型預測 (L5)
nav_order: 652
evidence_level: L5
indication_count: 10
---

# Papain
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Papain：從香港已上市的木瓜蛋白酶製劑到原發性血小板釋放障礙

## 一句話總結

Papain（木瓜蛋白酶）是一種半胱胺酸蛋白酶，目前在香港有 5 張藥品許可證。
TxGNN 模型預測它可能對**原發性血小板釋放障礙 (Primary Release Disorder of Platelets)** 有效。
目前**沒有臨床試驗**，僅檢索到 **1 篇文獻**，且該文獻與 Papain 和此疾病皆無關，因此這只是模型預測，沒有實際研究支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 原發性血小板釋放障礙 (Primary Release Disorder of Platelets) |
| TxGNN 預測分數 | 98.22% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料，DrugBank 的 MOA 欄位尚未取得。已知 Papain 是一種半胱胺酸蛋白酶，現有資料中沒有它影響血小板顆粒釋放的證據。

原適應症資料也不完整：香港 5 張許可證均未附核准適應症文字，因此無法評估原適應症與新適應症的關聯。

整體而言，這個預測**缺乏合理的機轉依據**。0.98 的高分來自知識圖譜的關聯推論，沒有臨床或實驗證據支持，不應視為有效性的訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38430019](https://pubmed.ncbi.nlm.nih.gov/38430019/) | 2024 | 其他（動物實驗） | Cell Mol Biol (Noisy-le-Grand) | 在兔骨關節炎模型比較富白血球與貧白血球的富血小板血漿（PRP）對軟骨的作用。與 Papain 及血小板釋放障礙皆無關，不構成支持證據 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-33430 | CHLORAFRESH LOZ | MEYER PHARMACEUTICALS LTD |
| HK-33429 | DESOPAIN LOZ | MEYER PHARMACEUTICALS LTD |
| HK-20578 | CARICOSE SYRUP | CHRISTO PHARM LTD |
| HK-25565 | ENZYME CO TAB | CHRISTO PHARM LTD |
| HK-01651 | APPEZYM TAB (S/C) | JEAN-MARIE PHARMACAL CO LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，唯一一篇文獻與 Papain 和此疾病無關，證據等級僅為 L5。
- 蛋白酶沒有已知的血小板釋放機轉，預測缺乏生物學依據。
- 同一份預測清單的前 10 名皆為 L5、建議 Hold。其中 Glanzmann 血小板無力症和 HER2 陽性乳癌的文獻，只是把 Papain 當作實驗試劑（處理血小板、切割抗體成 Fab 片段），不是治療證據。「breast tumor luminal A or B」的 19 篇文獻是對 "B" 的關鍵字誤配，內容與此疾病無關。

**若要推進需要：**
- 補齊 Papain 的作用機轉（DrugBank MOA）。
- 取得香港衛生署仿單的警語與禁忌資料，並確認各許可證的核准適應症與劑型。
- 找到 Papain 作為治療藥物影響血小板功能的實質研究（體外或動物實驗），否則不建議投入資源。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

