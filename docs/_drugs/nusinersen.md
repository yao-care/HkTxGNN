---
layout: default
title: Nusinersen
parent: 僅模型預測 (L5)
nav_order: 533
evidence_level: L5
indication_count: 10
---

# Nusinersen
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

# Nusinersen：從脊髓性肌肉萎縮症到腎性低血鎂症

## 一句話總結

Nusinersen（Spinraza）是一種鞘內注射的反義寡核苷酸藥物，原用於治療脊髓性肌肉萎縮症（SMA），目前未在香港上市。TxGNN 模型預測它可能對**腎性低血鎂症 (Renal Hypomagnesemia)** 有效，但預測分數僅為邊界值 **50%**，且無任何臨床試驗或文獻支持，機轉分析亦未發現關聯性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 脊髓性肌肉萎縮症 (SMA)（未見於香港許可證資料，依 evidence pack 機轉描述推定） |
| 預測新適應症 | 腎性低血鎂症 (Renal Hypomagnesemia) |
| TxGNN 預測分數 | 50%（邊界值，排名第 2,418,929 位） |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Nusinersen 詳細的作用機轉資料（DrugBank 標示為 Data Gap）。根據已知資訊，Nusinersen 是靶向 SMN2 pre-mRNA 剪接的反義寡核苷酸（ASO），透過鞘內注射矯正 SMN 蛋白表現量，用於脊髓性肌肉萎縮症。

然而，evidence pack 提供的機轉分析明確指出：腎性低血鎂症主要成因為 CLDN16/CLDN19 等腎小管緊密連接蛋白基因突變，導致鎂離子再吸收缺陷，與 SMN2 剪接調控**無已知路徑重疊**。TxGNN 給出的 0.5 分僅為模型分數的邊界值，並非高信心預測。

值得注意的是，本次 evidence pack 中排名前 10 的預測適應症（包括全身性膿疱性乾癬、精索惡性腫瘤、先天性/後天性續發性紅血球增多症等）分數均同為 0.5，且各自的機轉分析都得出「無機轉關聯」的結論。這顯示目前模型對 Nusinersen 的預測整體訊號偏弱，尚未找到具機轉合理性的再利用方向。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Nusinersen 目前**未在香港上市**，無許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（註：TFDA/香港仿單警語與禁忌症資料目前為 Blocking 等級的資料缺口，尚無法完成安全性初評。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 預測分數僅為邊界值（50%），且完全無臨床試驗或文獻佐證。
- Evidence pack 內建的機轉分析已明確指出腎性低血鎂症與 Nusinersen 的 SMN2 剪接矯正機轉無關聯，機轉合理性不足。
- 藥物本身作用機轉（MOA）與安全性資料（警語、禁忌症）均為缺口，尚不具備進入 S1 安全性初評的條件。

**若要推進需要：**
- 補齊 Nusinersen 的 DrugBank MOA 資料。
- 取得 TFDA/香港仿單警語與禁忌症，解除 Blocking 等級資料缺口。
- 若後續模型版本對此藥物產生分數明顯更高、且機轉分析支持的候選適應症，應重新評估；目前 10 個候選皆為同分（0.5）且機轉不成立，不建議投入資源進一步查證。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

