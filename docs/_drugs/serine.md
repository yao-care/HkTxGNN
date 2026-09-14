---
layout: default
title: Serine
parent: 僅模型預測 (L5)
nav_order: 682
evidence_level: L5
indication_count: 5
---

# Serine
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

# Serine：從內生性胺基酸到家族性內臟肌病變（預測）

## 一句話總結

Serine 是人體內生性胺基酸，目前在香港**未上市**、亦無已知核准適應症或明確作用機轉資料。
TxGNN 模型預測它可能與**家族性內臟肌病變 (Familial Visceral Myopathy)** 有關聯，
但目前**沒有任何臨床試驗或文獻**支持此關聯，純粹為知識圖譜共現分數。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無核准適應症（未上市藥物，為內生性胺基酸） |
| 預測新適應症 | 家族性內臟肌病變 (Familial Visceral Myopathy) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Serine 是體內合成蛋白質、磷脂與神經傳導物質所需的非必需胺基酸，
但在此評估中並無作為治療藥物的核准適應症紀錄，因此無法比對「原適應症」與「新適應症」之間的機轉關聯性。

TxGNN 給出的分數（99.99%）雖然極高，但排名 (rank 364) 顯示這是在龐大候選集中相對後段的結果，
且模型本身僅反映知識圖譜中的節點共現關係，並非藥理學因果推論。在缺乏 MOA 與原適應症的情況下，
這類高分預測更可能反映 Serine 在代謝／基因路徑資料庫中與內臟肌病變相關基因的間接連結，
而非具有實際治療潛力的證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

Serine 目前未在香港以藥品身份上市，無許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測新適應症（家族性內臟肌病變）完全沒有臨床試驗或文獻支持，屬純模型預測（L5）。
- 藥物本身缺乏 MOA 與原適應症資料，且未在香港上市，無法進行機轉關聯性或安全性初評。
- 補充說明：Evidence Pack 中其餘 4 個候選適應症（intestinal obstruction、unclassified/myopathic intestinal pseudoobstruction、neuronal intestinal dysplasia type B）同樣缺乏有效證據——即使有命中的試驗與文獻，逐筆檢視後皆為關鍵字雜訊而非直接相關，全部維持 Hold。

**若要推進需要：**
- 取得 Serine 的作用機轉（MOA）資料（DrugBank API 查詢，DG002）
- 確認是否存在任何以 Serine 為治療介入的臨床前或機轉研究
- 若無法補齊上述資料，建議暫緩此候選藥物的再利用評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

