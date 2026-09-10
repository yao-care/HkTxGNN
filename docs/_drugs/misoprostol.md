---
layout: default
title: Misoprostol
parent: 中證據等級 (L3-L4)
nav_order: 502
evidence_level: L3
indication_count: 2
---

# Misoprostol
{: .fs-9 }

證據等級: **L3** | 預測適應症: **2** 個
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

# Misoprostol：原適應症資料缺失 → 續發性閉經（Amenorrhea）預測

## 一句話總結

Misoprostol（DB00929）目前查無香港核准適應症紀錄，作用機轉資料亦缺失。
TxGNN 模型預測它可能對**續發性閉經 (Amenorrhea)** 有效，
目前有 **0 個臨床試驗**和 **7 篇文獻**支持這個方向，但多數文獻探討的是「終止妊娠/子宮排空」而非典型閉經治療，需人工核實適應症對應是否正確。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 尚無資料（香港未上市，且藥物層級原適應症紀錄缺失） |
| 預測新適應症 | 續發性閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.64% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料庫記錄，但根據已知藥理特性，Misoprostol 為 PGE1 類似物，可誘發子宮收縮、軟化子宮頸並促使子宮內容物排出。這個機轉在「稽留流產／萎縮性胚胎」等需誘導子宮排空的臨床情境中已有支持，與續發性閉經（可能因妊娠物滯留或子宮內膜相關病變所致）存在間接關聯。

**重要保留意見**：檢索到的 7 篇文獻中，多數（如 mifepristone + misoprostol 用於終止超早期妊娠、missed abortion 處置）探討的核心主題是「終止妊娠／子宮排空」，而非典型定義下「原發性／續發性閉經」的治療。TxGNN 的 `disease_name` 對應疑似為疾病本體映射過寬所致，兩者可能非同一適應症，須人工核實本體對應是否正確後才能推進下一階段評估。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | 低劑量 mifepristone 併自行給藥 misoprostol 用於超早期人工流產，療效、安全性與可接受度良好 |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT | Reproductive Sciences | 劑量遞減試驗：mifepristone（150→50mg）併 200µg misoprostol 終止超早期妊娠之療效與安全性 |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Cohort | Human Reproduction | 預期月經前使用低劑量 mifepristone 併 misoprostol，評估預防非預期妊娠之可行性 |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Cohort | J Obstet Gynaecol Res | 自行給藥低劑量 mifepristone 併 misoprostol 用於早期妊娠終止之安全性與有效性 |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Review | BMJ | 稽留流產與萎縮性胚胎之藥物處置，misoprostol 用於促使子宮內容物排出 |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | 異常子宮出血之子宮內膜消融術處置回顧（背景資料，與 misoprostol 無直接治療關聯） |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case Report | Cureus | 妊娠急性脂肪肝病例，患者以閉經、噁心等症狀表現（背景描述，非 misoprostol 治療研究） |

---

## 安全性考量

安全性資訊（主要警語、禁忌症、藥物交互作用）目前皆缺失，屬於 **Blocking 等級資料缺口**（DG001：香港仿單警語/禁忌未取得），此缺口直接影響是否能進入 S1 安全性初評階段。建議請參考原廠仿單，並優先補齊此項資料。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 文獻證據雖有 7 篇（含 2 篇 Phase RCT 等級研究），但主題多聚焦於「終止妊娠」而非「閉經治療」，適應症對應存在疑慮，需人工核實後才能認定證據有效支持此預測方向。
- 安全性�843資料（仿單警語/禁忌）為 Blocking 缺口，且該藥物目前在香港無許可證、未上市，無法進行 S1 安全性初評。

**若要推進需要：**
- 人工核實 TxGNN `amenorrhea (disease)` 本體映射是否正確對應目標臨床情境（而非誤映射自「終止妊娠」相關研究）
- 取得香港（或參考地區）仿單警語與禁忌症資料，解除 DG001 Blocking 缺口
- 補齊 Misoprostol 作用機轉（MOA）詳細資料（DG002）
- 評估是否有本地上市／申請許可證的可能性

*註：第二預測候選「atypical coarctation of aorta」（分數 99.30%）因無任何臨床試驗或文獻證據支持，且屬機轉外推（該用途臨床上多用 alprostadil 而非 misoprostol），評為 L5/Hold，不納入本次重點評估。*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

