---
layout: default
title: Imidacloprid
parent: 僅模型預測 (L5)
nav_order: 391
evidence_level: L5
indication_count: 5
---

# Imidacloprid
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

# IMIDACLOPRID：從殺蟲劑用途到馬尾症候群（預測，證據不足）

## 一句話總結

Imidacloprid 是一種新菸鹼類（neonicotinoid）殺蟲劑，作用於昆蟲的菸鹼型乙醯膽鹼受體（nAChR），**並非人類核准用藥，也沒有原始人類適應症**。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 有效（預測分數 99.99%），
但目前**沒有任何臨床試驗或文獻證據**支持此關聯，證據等級為最低的 L5。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無（本藥物為農用殺蟲劑，未登記任何人類治療適應症） |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（僅有模型預測，無任何試驗或文獻） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 imidacloprid 正式的人類作用機轉（MOA）資料（DrugBank 查詢為 Data Gap）。根據其藥理分類，imidacloprid 是**昆蟲選擇性的 nAChR 促效劑**，對哺乳類 nAChR 的親和力極低，這是其作為殺蟲劑對哺乳動物相對低毒的藥理基礎。

值得特別說明的是：**這個機轉特性本身就是反對此次預測的理由，而非支持理由**。馬尾症候群屬於神經壓迫急症，臨床上以手術減壓為主要治療手段，與藥物性 nAChR 調節缺乏合理的治療機轉關聯。此外，imidacloprid 完全缺乏人類中樞/周邊神經系統的藥動與安全性資料，無從評估其是否能安全地作用於人體神經系統。

因此，TxGNN 給出的 99.99% 高分應被理解為**知識圖譜層級的統計關聯**，而非具有生物學或臨床意義的機轉證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Imidacloprid 目前**未於香港上市**，無許可證資訊。（`total_licenses = 0`）

---

## 其他 TxGNN 預測適應症一覽

本評估包 (Evidence Pack) 同時列出了 5 個 TxGNN 預測適應症，為求完整揭露，摘要如下：

| 排名 | 預測適應症 | TxGNN 分數 | 證據概況 | 決策 |
|------|-----------|-----------|---------|------|
| 1 | 馬尾症候群 (Cauda Equina Syndrome) | 99.99% | 無試驗、無文獻 | Hold |
| 2 | Obsolete Neurogenic Bladder | 99.98% | 無試驗、無文獻；且該疾病詞條為本體論中已棄用（obsolete），資料品質存疑 | Hold |
| 3 | 大腸激躁症 (Irritable Bowel Syndrome) | 99.88% | 3 個試驗，均為非藥物介入（骨療手法、MRI 診斷、腸胃動力觀察），與 imidacloprid 無關 | Hold |
| 4 | Non-syndromic Esophageal Malformation | 99.63% | 無試驗、無文獻；屬先天結構性疾病，與藥物機轉無合理連結 | Hold |
| 5 | 食道疾病 (Esophageal Disease) | 99.49% | 39 個試驗（經核對後均與 imidacloprid 無關，屬檢索誤匹配）；1 篇文獻為獸醫學跳蚤/蜱蟲滴劑研究，與人類食道疾病無實質關聯 | Hold |

**五個候選適應症的證據等級均為 L5，決策階段均為 S0，建議均為 Hold。**

---

## 安全性考量

安全性資訊請參考原廠仿單（本藥物並無人類用藥安全性資料，香港與台灣官方均無仿單警語/禁忌症紀錄）。

---

## 結論與下一步

**決策：Hold**

**理由：**
- Imidacloprid 本質上是農用殺蟲劑，並非核准人類用藥，缺乏任何原始適應症、MOA 正式資料及人類安全性資料。
- 五個 TxGNN 預測適應症中，證據最強的仍僅為知識圖譜統計關聯（L5），排名第 1-2、4 的候選完全無臨床試驗或文獻支持；第 3、5 名雖有檢索命中，但經人工核對後均與 imidacloprid 無實質相關（非藥物介入研究、檢索誤匹配、獸醫學研究）。
- 機轉上，imidacloprid 對哺乳類 nAChR 親和力低，與馬尾症候群等神經科適應症缺乏合理的治療機轉連結，此點反而降低了預測的可信度。

**若要推進需要（可能性極低，僅供記錄）：**
- 補齊 imidacloprid 的人類藥動/藥效（PK/PD）與毒理資料
- 確認是否存在任何動物模型或體外研究支持其對神經/腸胃系統的治療潛力
- 重新檢視 TxGNN 模型對此藥物-疾病配對的訓練資料品質，排除知識圖譜雜訊或本體論錯誤（如「obsolete」疾病詞條）的干擾

> **整體建議：本候選藥物暫不建議投入後續資源進行 S1 安全性初評或證據收集，除非出現新的機轉或人類用藥安全性資料。**
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

