---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 704
evidence_level: L5
indication_count: 2
---

# Spironolactone
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

# Spironolactone：原適應症資料缺失 → 預測 Hypotrichosis Simplex of the Scalp

## 一句話總結

Spironolactone（DB00421）目前香港未上市，且原始適應症與作用機轉資料皆缺失。
TxGNN 模型預測其可能對**頭皮單純性少毛症 (Hypotrichosis Simplex of the Scalp)** 有效，
但目前**無任何臨床試驗或文獻**支持，且機轉合理性分析認為此預測**可能是假陽性**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（未提供 original_indications，亦無香港許可證資料） |
| 預測新適應症 | 頭皮單純性少毛症 (Hypotrichosis Simplex of the Scalp) |
| TxGNN 預測分數 | 99.26% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Spironolactone 的作用機轉資料（MOA 標記為缺失）。根據藥理學公開知識，Spironolactone 為醛固酮拮抗劑兼抗雄激素藥物，常見用於雄激素驅動之落髮（androgenetic alopecia）。

然而，本 Evidence Pack 內附的機轉關聯性分析明確指出：**此次預測的兩個適應症在生物學上可能與 Spironolactone 的已知機轉無關**。

- **Hypotrichosis simplex of the scalp** 為體染色體顯性遺傳疾病（與 CDSN、APCDD1 等基因突變相關），毛囊發育異常屬遺傳性問題，與雄激素訊號路徑無直接病理關聯。
- **Congenital hypotrichosis with milia** 為罕見遺傳症候群，涉及毛囊與皮脂腺發育缺陷，同樣非雄激素依賴性疾病。

分析認為，TxGNN 的高分（>99%）較可能反映知識圖譜中「hypotrichosis」節點與「androgenetic alopecia」等概念的語意鄰近性，而非真實的機轉證據，**應視為潛在假陽性**，不建議直接採信分數本身。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

此藥物目前尚未在香港上市，無許可證資料可供列出。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：本 Evidence Pack 標記「TFDA 仿單警語/禁忌」為 **Blocking** 等級資料缺口——這是進入下一階段安全性初評（S1）的必要條件，目前尚未補齊。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個預測適應症皆為 L5（僅有模型分數，無臨床試驗、無文獻、無觀察性研究支持）。
- 附帶的機轉分析本身即質疑此預測的生物學合理性，認為高分可能源於知識圖譜語意鄰近效應而非真實機轉關聯，存在假陽性風險。
- 藥物在香港未上市，且缺乏 MOA 與安全性（警語、禁忌、DDI）等基礎資料，尚不具備進入安全性初評（S1）的條件。

**若要推進需要：**
- 補齊 TFDA/香港衛生署仿單警語與禁忌症資料（Blocking 缺口 DG001）
- 補齊 Spironolactone 作用機轉資料，並釐清原始核准適應症（DrugBank 查詢，High 缺口 DG002）
- 針對此少毛症適應症方向，進行體外/體內機轉驗證研究，先排除假陽性可能，再考慮投入臨床試驗或文獻搜尋資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

