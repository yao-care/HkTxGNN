---
layout: default
title: Nonivamide
parent: 僅模型預測 (L5)
nav_order: 529
evidence_level: L5
indication_count: 10
---

# Nonivamide
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

# Nonivamide：從外用止痛到肺動脈高血壓

## 一句話總結

Nonivamide（DrugBank DB11324）是辣椒素（capsaicin）類似物、TRPV1 受體促效劑，目前已知作為外用止痛成分使用，台灣尚未上市、無核准適應症記錄。TxGNN 模型預測它可能對**肺動脈高血壓 (Pulmonary Hypertension)** 有效，但目前沒有任何臨床試驗或文獻支持這個方向，純屬模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無核准適應症記錄（台灣未上市；已知作為外用止痛成分） |
| 預測新適應症 | 肺動脈高血壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 99.81% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏正式的作用機轉（MOA）欄位資料，原適應症記錄也是空的。根據 TxGNN 推論所附的機轉假說，Nonivamide 是辣椒素類似物、TRPV1 受體促效劑，目前已知用途是外用止痛貼片成分。

肺動脈高血壓這個預測的推論路徑是：TRPV1 訊號與血管張力調節、肺血管內皮功能在理論上有關聯。但評估報告本身也註明，這個關聯「無任何體內/臨床資料支持其對肺動脈壓的直接作用，純屬 KG embedding 相似度推論」。

由於缺乏原適應症佐證資料、也沒有任何臨床前實驗支持，這個預測的生物學合理性目前僅停留在假說階段——這正是評分系統將其列為 L5（純模型預測、無實際研究）的原因。

---

## 臨床試驗證據

目前無相關臨床試驗登記（ClinicalTrials.gov、ICTRP 均查無資料）。

## 文獻證據

目前無相關文獻（PubMed 查無資料）。

---

## 香港上市資訊

Nonivamide 目前於台灣未上市，無任何許可證記錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 本次評估的 10 個預測適應症全部為 TxGNN 純模型推論（evidence_level L5、decision_stage S0），沒有任何臨床試驗、文獻或臨床前資料支持。
- 藥物本身台灣未上市，原適應症與安全性資料（TFDA 仿單警語/禁忌）皆缺失，屬 Blocking 等級資料缺口，尚無法進入 S1 安全性初評。

**若要推進需要：**
- 補齊 TFDA（或相關藥監機關）仿單警語與禁忌症資料，才能進入 S1 安全性初評
- 補齊 DrugBank 詳細 MOA 資料，釐清機轉關聯性
- 針對排名靠前的預測適應症（肺動脈高血壓、周邊動脈疾病等）尋找臨床前/體外實驗證據，驗證 TRPV1 訊號路徑假說是否成立
- 部分預測（如急性淋巴性白血病、心室心律不整、CPVT）在評估報告中已被機轉分析標註為「模型雜訊」或「偽陽性」，建議優先排除，避免投入後續資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

