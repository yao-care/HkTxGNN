---
layout: default
title: Imiglucerase
parent: 中證據等級 (L3-L4)
nav_order: 454
evidence_level: L4
indication_count: 10
---

# Imiglucerase
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Imiglucerase：從戈謝氏症到 Hurler 症候群

## 一句話總結

Imiglucerase 是重組葡萄糖腦苷脂酶（glucocerebrosidase），用於戈謝氏症（Gaucher disease）的酵素替代療法（ERT）。許可證資料未載明適應症，此處依文獻判斷。
TxGNN 模型預測它可能對 **Hurler 症候群（MPS I）** 有效，但目前**沒有臨床試驗**，只有 **2 篇一般性綜述**，且沒有直接的機轉依據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未登載（依文獻為戈謝氏症的酵素替代療法） |
| 預測新適應症 | Hurler 症候群 (Hurler syndrome) |
| TxGNN 預測分數 | 99.52% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Imiglucerase 是重組人類葡萄糖腦苷脂酶，經修飾後暴露甘露糖殘基，由巨噬細胞的甘露糖受體攝入。它作用於葡萄糖神經醯胺（glucosylceramide）。

Hurler 症候群和戈謝氏症同屬溶小體儲積症（lysosomal storage disorder），治療方式都是靜脈輸注、靠甘露糖受體標靶的酵素替代。模型給出高分，很可能是反映這種類別層級的相似性。

但兩者缺陷的酵素和基質完全不同。Hurler 症候群是 IDUA（α-L-艾杜糖醛酸酶）缺乏，累積的是葡萄糖胺聚醣。Imiglucerase 水解的是葡萄糖神經醯胺，無法補足 IDUA 的缺陷。因此這個預測只有類別層級的關聯，沒有基質層級的機轉支持。Hurler 症候群本身已有專屬的酵素替代療法。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Review | Proc Natl Acad Sci U S A | 回顧以 PET 對酵素替代療法進行影像追蹤。文中提到 ERT 已用於戈謝氏症、法布瑞氏症、Hurler 症候群等疾病，但這並非 imiglucerase 用於 Hurler 症候群的證據 |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de Médecine Interne | 回顧溶小體儲積症的酵素替代療法，說明 imiglucerase（Cerezyme）取代胎盤來源的 alglucerase，用於戈謝氏症。屬一般性綜述，無 Hurler 症候群的直接數據 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60392 | CEREZYME POWDER FOR CONCENTRATE FOR SOLUTION FOR INF 400IU（廠商：SANOFI HONG KONG LIMITED） | 許可證未登載 | 許可證未登載 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- Hurler 症候群的預測只有類別層級的關聯。Imiglucerase 無法補足 IDUA 缺陷，且沒有臨床試驗，僅有 2 篇一般性綜述，目前不建議推進。
- 補充說明：同一份分析中，「伴隨骨骼病變的溶小體儲積症」（實為骨骼型戈謝氏症）有 1 項 Phase 4 單臂試驗（NCT04656600）、1 項 Phase 3 延伸試驗（NCT01842841，為另一種酵素 velaglucerase alfa）和多篇世代研究，建議為 Proceed with Guardrails。但這基本上是符合既有適應症的用途，不是新的再利用機會。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌資料，這是進入安全性篩選的前提。
- 補齊許可證的核准適應症與劑型，以確認原適應症。
- 補充作用機轉資料（例如查詢 DrugBank）。
- 若仍要探討 Hurler 症候群，需有基質層級的機轉理由或前臨床證據，例如 imiglucerase 是否對 IDUA 缺乏模型有任何作用。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

