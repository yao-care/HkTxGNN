---
layout: default
title: Ponatinib
parent: 僅模型預測 (L5)
nav_order: 600
evidence_level: L5
indication_count: 2
---

# Ponatinib
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

# Ponatinib：原適應症資料缺失，TxGNN 預測新適應症為牙龈纖維瘤病

> 此份 Evidence Pack 缺乏原適應症登記資料（無許可證、無 original_indications），故標題無法依範本格式列出「原適應症」，以下如實反映此缺口。

## 一句話總結

Ponatinib 是一款多重酪氨酸激酶抑制劑（根據機轉描述作用於 BCR-ABL/FLT3/FGFR/PDGFR/VEGFR），目前未在香港上市，原適應症與作用機轉的正式登記資料皆缺失。TxGNN 模型預測它可能對**牙龈纖維瘤病 (Fibromatosis, Gingival)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，證據等級為最低的 **L5**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 牙龈纖維瘤病 (Fibromatosis, Gingival) |
| TxGNN 預測分數 | 99.04% |
| 證據等級 | L5（無臨床試驗、無文獻，僅有模型分數） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

官方 MOA 資料缺失（original_moa 為資料缺口，列為 High 等級缺口 DG002）。不過根據 evidence pack 中的機轉註記，ponatinib 是一款多重酪氨酸激酶抑制劑，標靶 BCR-ABL、FLT3、FGFR、PDGFR、VEGFR 等激酶。

牙龈纖維瘤病的病理機轉主要與遺傳性 SOS1/REST 基因突變，或特定藥物誘發（如 phenytoin、cyclosporine）有關，與 ponatinib 所標靶的激酶路徑目前並無已知病理機轉關聯。換言之，這個預測目前僅是 TxGNN 演算法基於知識圖譜相似性給出的分數，**沒有找到生物學合理性佐證**，機轉關聯性偏弱。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

目前查無許可證登記（市場狀態：未上市）。

## 安全性考量

安全性資訊請參考原廠仿單。

> 需特別注意：TFDA/香港衛生署仿單警語與禁忌症資料被列為 **Blocking** 等級缺口（DG001），影響為「無法進入 S1 安全性初評」，在補齊此資料前不應進行安全性相關決策。

## 結論與下一步

**決策：Hold**

**理由：**
- 本預測（牙龈纖維瘤病）僅有 TxGNN 模型分數（99.04%），無任何臨床試驗、文獻或機轉證據支持，證據等級為最低的 L5。
- 安全性資料存在 Blocking 等級缺口（DG001），尚無法進行 S1 安全性初評；藥物在香港亦未上市。

**若要推進需要：**
- 補齊仿單警語與禁忌症資料（DG001，Blocking）
- 補齊 DrugBank MOA 完整資料（DG002）
- 針對牙龈纖維瘤病取得體外或臨床前的機轉驗證證據，目前完全空缺

**備註：** 同一份 Evidence Pack 中另有第二預測——脂肪肉瘤 (liposarcoma)，證據等級 L4，有一篇臨床前激酶篩選文獻（PMID 29132397）支持部分脂肪肉瘤亞型與相關激酶路徑的關聯，機轉合理性略高於本篇的牙龈纖維瘤病預測，但仍無人體臨床試驗，同樣建議 Hold，可作為後續優先評估的候選方向。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

