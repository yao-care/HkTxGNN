---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 396
evidence_level: L5
indication_count: 5
---

# Indacaterol
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

# Indacaterol：從支氣管擴張劑（LABA）到腎因性抗利尿激素分泌不當症候群

## 一句話總結

Indacaterol 目前尚未於香港取得上市許可，僅知其藥理類別為長效β2腎上腺素受體促效劑（LABA），臨床試驗脈絡顯示主要用於慢性阻塞性肺病（COPD）的支氣管擴張治療。
TxGNN 模型預測它可能對罕見遺傳性疾病**腎因性抗利尿激素分泌不當症候群（Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD）**有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，機轉分析也顯示兩者病理路徑無已知關聯。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無許可證資料（尚未於香港上市；藥理類別為 LABA，用於支氣管擴張） |
| 預測新適應症 | 腎因性抗利尿激素分泌不當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| TxGNN 預測分數 | 99.54% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Indacaterol 的正式作用機轉（MOA）資料目前缺失（[Data Gap]，見 DG002）。根據其他候選適應症試驗脈絡可知，該藥屬於選擇性長效β2腎上腺素受體促效劑（LABA），機轉上作用於支氣管平滑肌的β2受體，達到支氣管擴張效果，主要用於 COPD 相關治療。

NSIAD 是一種罕見的 X 染色體性聯遺傳疾病，致病機轉為血管加壓素 V2 受體（AVPR2）的功能獲得性突變，導致腎臟集尿管在無 ADH 刺激下持續活化水分再吸收路徑。此病理路徑與 Indacaterol 作用的支氣管平滑肌β2受體訊號**沒有已知的分子或藥理學交集**。

換言之，這個預測目前僅來自 TxGNN 的統計關聯分數，缺乏任何機轉假說、臨床前資料、臨床試驗或文獻佐證，合理性偏低。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

Indacaterol 目前未於香港取得上市許可，無許可證資料。

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：TFDA/香港仿單警語與禁忌資料目前缺失，且此缺口被標記為 **Blocking**（DG001），代表在補齊前無法進入安全性初評（S1）階段。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測適應症（NSIAD）證據等級為 L5——零臨床試驗、零文獻、且機轉分析明確指出無已知病理關聯，統計預測分數無法單獨支撐推進。
- 藥物本身尚未於香港上市，且安全性�settings存在 Blocking 等級資料缺口（DG001），無法進行下一階段安全性評估。
- 其餘候選適應症（headache disorder、trigeminal autonomic cephalalgia、paratenonitis、calcific tendinitis）證據等級同為 L4-L5，其中 headache disorder 雖有 2 個已完成的 Phase 3/4 試驗，但均為 COPD 相關研究、頭痛僅作為不良反應紀錄，與「治療頭痛」的假說無關（relevance grade C）。整體候選清單目前均不具推進條件。

**若要推進需要：**
- 補齊 Indacaterol 完整作用機轉（MOA）資料（DG002，High，來源：DrugBank API）
- 取得 TFDA／香港仿單完整警語與禁忌資訊（DG001，Blocking，來源：官網 PDF 解析）
- 針對 NSIAD 尋找 β2 促效劑相關的臨床前或機轉研究，建立藥理學合理性；若持續無法建立關聯，建議終止此方向調查
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

