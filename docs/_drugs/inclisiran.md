---
layout: default
title: Inclisiran
parent: 僅模型預測 (L5)
nav_order: 458
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran：從降低 LDL-C（高膽固醇血症）到鉀缺乏症

## 一句話總結

Inclisiran 是靶向 PCSK9 的 siRNA 藥物，作用是降低 LDL-C。
TxGNN 模型預測它可能對**鉀缺乏症 (Potassium Deficiency Disease)** 有效，但目前**沒有任何臨床試驗或文獻**支持，只是模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 鉀缺乏症 (Potassium Deficiency Disease) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據已知資訊，Inclisiran 是 PCSK9 靶向的 siRNA，透過抑制 PCSK9 來降低 LDL-C。

在機轉上，我們找不到它與鉀代謝的合理關聯。PCSK9 沉默與鉀恆定沒有已知關係，0.9993 的高分只是知識圖譜推論的結果。

因此這個預測目前**不具說服力**。TxGNN 排名為第 2013 名，缺乏任何實證支持，應視為需要排除或重新驗證的訊號。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67211 | LEQVIO SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 284MG/1.5ML（廠商：NOVARTIS PHARMACEUTICALS (HK) LIMITED） | 注射液（預充填針筒） | 未提供 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測（L5），沒有任何臨床試驗或文獻，且機轉上找不到 PCSK9 沉默與鉀缺乏之間的關聯。
- 同一份資料中排名前 10 的其他預測適應症也都是 L5、Hold。其中「主動脈畸形」配對到的 2 個 Phase 3 試驗，實際是兒童家族性高膽固醇血症試驗，並非該疾病的證據。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌與核准適應症。
- 補充 DrugBank 的作用機轉資料。
- 在 ClinicalTrials.gov 與 PubMed 進行針對性檢索，確認是否有 Inclisiran 與鉀缺乏症（或低血鉀）的直接研究。
- 若檢索後仍無任何證據，建議不再投入資源，或改評估其他預測適應症。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

