---
layout: default
title: Teprotumumab
parent: 僅模型預測 (L5)
nav_order: 732
evidence_level: L5
indication_count: 10
---

# Teprotumumab
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

# Teprotumumab：從（原適應症資料缺失）到 Monosomy X（單一 X 染色體缺失症）

## 一句話總結

Teprotumumab（DrugBank ID: DB06343）目前香港未上市，且 Evidence Pack 未提供其核准適應症與作用機轉資料。
TxGNN 模型預測其可能對 **Monosomy X（單一 X 染色體缺失，Turner 症候群核心病因）** 有效，
但目前**無任何臨床試驗、無文獻佐證**，且此預測缺乏生物學合理性。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（Evidence Pack 未提供，需向原廠仿單或 DrugBank 補查） |
| 預測新適應症 | Monosomy X（單一 X 染色體缺失症） |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L5（僅有模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為資料缺口，見 DG002，嚴重度 High）。根據既有藥理學知識推斷（非源自本次 Evidence Pack 的 DrugBank 欄位），Teprotumumab 為 IGF-1R（胰島素樣生長因子受體）單株抗體拮抗劑，但此推斷未經 Evidence Pack 正式驗證。

由於原適應症資訊本次未提供，無法比對原適應症與 Monosomy X 之間的臨床關聯性。從純機轉角度分析，Monosomy X 屬於染色體結構異常疾病（性染色體缺失），其病理生理與 IGF-1R/胰島素受體訊號路徑並無已知的直接生物學連結。

值得注意的是，本次預測清單中 rank 1–10 有多達 6 項與性染色體異常相關（monosomy X、mosaic monosomy X、mixed gonadal dysgenesis、Turner syndrome、sex chromosome disorder of sex development、X chromosome number anomaly），且另有 2 項為食道靜脈曲張、1 項為粒線體疾病、1 項為一般靜脈曲張——這些疾病彼此病理機轉高度異質，卻共享極相近的 TxGNN 分數（99.3%–99.8%）。此現象較可能反映**知識圖譜拓樸相似性**（例如節點連結模式相近），而非真實藥理機轉訊號，建議在缺乏機轉假說與實證支持前，不宜視為可信的老藥新用候選。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

此藥物目前於香港**未上市**，無許可證資料。

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：本次 Evidence Pack 標記「TFDA 仿單警語/禁忌」為**阻斷性（Blocking）資料缺口**（DG001），影響評估已無法進入 S1 安全性初評階段；此為決策為 Hold 的重要原因之一。

## 結論與下一步

**決策：Hold**

**理由：**
- 全部 10 個預測適應症均為 L5 證據等級（無任何臨床試驗或文獻佐證），評分模型建議亦全數為 Hold。
- 排名第一的 Monosomy X 與藥物已知/推斷機轉（IGF-1R 拮抗）缺乏生物學合理性連結。
- 關鍵安全性資料（仿單警語、禁忌症）為阻斷性資料缺口，無法完成基本安全性初評。
- 藥物原始適應症與作用機轉資料本身亦缺失，無法建立機轉延伸的推論基礎。

**若要推進需要：**
- 補齊 TFDA／香港衛生署原廠仿單警語與禁忌症資料（DG001，阻斷性）
- 透過 DrugBank API 查證正式作用機轉（DG002）
- 補充原始核准適應症資訊，作為機轉延伸分析的基準
- 若後續機轉資料顯示與 IGF-1 軸相關（如 Turner 症候群常見之生長遲滯／IGF-1 異常），需進一步釐清 Teprotumumab 為拮抗劑而非促效劑，是否與臨床需求方向一致
- 建議優先重新檢視此批預測是否為知識圖譜拓樸偏誤（topology artifact），而非個別追加證據收集
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

