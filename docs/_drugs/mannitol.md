---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 543
evidence_level: L5
indication_count: 5
---

# Mannitol
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

# Mannitol：從滲透性利尿劑到腎因性抗利尿激素不適當分泌症候群

## 一句話總結

Mannitol 是一種滲透性利尿劑，在香港有 3 張注射劑許可證。
TxGNN 模型預測它可能對**腎因性抗利尿激素不適當分泌症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效。
目前有 **0 個臨床試驗**和 **1 篇文獻**（僅為低鈉血症的一般性回顧），證據非常薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 腎因性抗利尿激素不適當分泌症候群 (NSIAD) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Mannitol 屬於滲透性利尿劑，可經由滲透作用增加尿液排出。理論上，這可能促進自由水排出。

NSIAD 是 V2 受體功能獲得性突變所致，即使沒有 ADH，腎臟仍持續滯留水分。Mannitol 的滲透性利尿雖可能幫助排水，但同時也可能造成移位性低鈉血症，反而使病情複雜化。

整體而言，這個預測**沒有直接的機轉支持**，99.97% 的高分只是知識圖譜的推論結果，不代表臨床上有效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | 說明低鈉血症評估的十大常見陷阱，強調正確診斷病因對處置很重要。內容並未討論 mannitol 用於 NSIAD |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-21527 | OSMITROL (MANNITOL) INJ 20% "VIAFLEX" | Baxter Healthcare Limited |
| HK-28237 | OSMOFUNDIN IV INFUSION 20% | B. Braun Medical (HK) Ltd |
| HK-43086 | NEUROLITE FOR INJ WITH BUFFER VIAL | Global Medical Solutions Hong Kong Limited |

## 安全性考量

安全性資訊請參考原廠仿單。

另外，mannitol 造成的暫時性容積擴張與移位性低鈉血症，可能與 NSIAD 這類水分滯留、低鈉的病況衝突，須特別留意。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅為 L5，沒有任何臨床試驗，唯一的文獻也與 mannitol 無直接關聯。
- 機轉上缺乏支持，且有移位性低鈉血症的潛在風險。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊核准適應症、警語與禁忌症
- 補充 mannitol 的作用機轉資料（如 DrugBank）
- 搜尋 mannitol 與 NSIAD 或低鈉血症的直接臨床或機轉研究
- 評估移位性低鈉血症對此適應症的安全性影響

其他預測適應症（急性肺心症、運動誘發惡性高熱、惡性高熱易感性、家族性週期性麻痺）同樣為 Hold，其中部分可能來自 dantrolene 製劑含 mannitol 賦形劑的圖譜關聯，並非 mannitol 本身有療效。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

