---
layout: default
title: Rasburicase
parent: 僅模型預測 (L5)
nav_order: 760
evidence_level: L5
indication_count: 10
monitor_inn: "RASBURICASE"
predicted_indications: ["hypouricemia, renal", "hypoxanthine guanine phosphoribosyltransferase partial deficiency", "hepatic porphyria", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "primitive portal vein thrombosis", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "renal tubular acidosis", "disorder of phenylalanine metabolism"]
last_modified_at: 2026-10-28
description: "Rasburicase：預測新適應症為腎性低尿酸血症 (Hypouricemia, Renal)（證據等級 L5）。原適應症：高尿酸血症"
---

# Rasburicase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Rasburicase：從高尿酸血症到腎性低尿酸血症（預測）
{: .text-alpha }

## 一句話總結

Rasburicase 是重組尿酸氧化酶，知識圖譜中記錄其與高尿酸血症相關。
TxGNN 模型預測它可能對**腎性低尿酸血症 (Hypouricemia, Renal)** 有效，但目前**沒有任何臨床試驗或文獻**支持，且機轉上反而有安全疑慮，建議暫緩。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高尿酸血症（知識圖譜中記錄的關聯；香港許可證未提供適應症文字） |
| 預測新適應症 | 腎性低尿酸血症 (Hypouricemia, Renal) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中未收錄）。根據一般藥理知識，Rasburicase 是重組尿酸氧化酶，可將尿酸轉化為尿囊素，降低血中尿酸。

然而，腎性低尿酸血症本身就是血清尿酸偏低的疾病（常見於 URAT1/SLC22A12 或 GLUT9 功能喪失）。對這類病人再降低尿酸沒有治療依據，還可能造成傷害。因此這個高分預測（0.9999）來自 TxGNN 模型（深度學習），可能反映模型在相關疾病之間學到的相似性，而非生物學證據。

此外，其他排名較前的預測（如次發於肝臟疾病、門脈高壓、紫質症、苯丙胺酸代謝異常等）同樣缺乏機轉依據，其分數同樣來自 TxGNN 模型（深度學習），可能反映模型在相關疾病之間學到的相似性，而非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49808 | FASTURTEC FOR INJ 1.5MG | 未提供 | 未提供（廠商：SANOFI HONG KONG LIMITED） |

## 安全性考量

- **藥物交互作用**：共查得 13 筆，其中重大 (Major) 等級 2 筆：
  - Prilocaine
  - Nitrous acid（亞硝酸）
- 其餘為中度 (Moderate) 交互作用，主要為局部或眼用麻醉藥（Tetracaine、Lidocaine、Benzocaine、Cocaine、Proparacaine、Oxybuprocaine、Cinchocaine）及 Idelalisib。
- 其他警語、禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究此疾病，證據等級僅為 L5。
- 腎性低尿酸血症本身尿酸已偏低，進一步降尿酸缺乏機轉依據且可能有害。

**若要推進需要：**
- 取得詳細的作用機轉資料
- 取得香港仿單的警語與禁忌症
- 重新檢視是否有更合理的候選適應症（例如與尿酸代謝相關的急性狀況），並以文獻或試驗佐證
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

