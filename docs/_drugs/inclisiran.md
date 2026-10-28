---
layout: default
title: Inclisiran
parent: 僅模型預測 (L5)
nav_order: 466
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Inclisiran：預測新適應症為鉀缺乏症 (Potassium Deficiency Disease)（證據等級 L5）。原適應症：目前缺乏香港許可證的適應症文字資料"
monitor_inn: "Inclisiran"
predicted_indications: ["potassium deficiency disease", "esophageal disease", "atypical coarctation of aorta", "migraine disorder", "non-syndromic esophageal malformation", "migraine with brainstem aura", "aortic malformation", "esophageal ulcer", "Raynaud disease"]
---

# Inclisiran
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Inclisiran：從 PCSK9 相關高膽固醇血症治療到「鉀缺乏症」的模型預測
{: .text-alpha }

## 一句話總結

Inclisiran 是一種靶向 PCSK9 mRNA 的 siRNA 藥物，在香港以 LEQVIO 預填充注射劑上市。
TxGNN 模型預測它可能對**鉀缺乏症 (Potassium Deficiency Disease)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前缺乏香港許可證的適應症文字資料 |
| 預測新適應症 | 鉀缺乏症 (Potassium Deficiency Disease) |
| TxGNN 預測分數 | 0.9993 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中未收錄）。根據已知資訊，Inclisiran 是一種 siRNA，作用於肝細胞中的 PCSK9 mRNA，以降低 LDL-C。

然而，PCSK9 靜默與鉀的體內恆定沒有已知關聯。這個高分預測看起來是模型的假象（artifact），沒有任何臨床或文獻資料支持。因此，本報告**不認為此預測在機轉上合理**，僅將其視為需要進一步驗證的計算假說。

其他排名靠前的預測（食道疾病、非典型主動脈縮窄、偏頭痛、雷諾氏病等）同樣缺乏機轉依據與實證資料。

## 臨床試驗證據

目前無與「鉀缺乏症」相關的臨床試驗登記。

補充說明：在排名第 8 的預測（主動脈畸形）下，雖然關聯了兩項 Inclisiran 的 Phase 3 試驗，但它們實際上是兒童家族性高膽固醇血症研究，與主動脈畸形並無直接關係，也與本報告的主要預測無關：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06597019](https://clinicaltrials.gov/study/NCT06597019) | Phase 3 | 招募中 | 60 | 評估 Inclisiran 用於 6 至未滿 12 歲異合子家族性高膽固醇血症（HeFH）兒童的安全性與療效 |
| [NCT06597006](https://clinicaltrials.gov/study/NCT06597006) | Phase 3 | 招募中 | 9 | 評估 Inclisiran 用於 2 至未滿 12 歲同合子家族性高膽固醇血症（HoFH）兒童的安全性與療效 |

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67211 | LEQVIO SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 284MG/1.5ML（廠商：NOVARTIS PHARMACEUTICALS (HK) LIMITED） | 預填充注射劑（依品名） | 許可證資料未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測缺乏機轉依據，且沒有任何臨床試驗或文獻支持，證據等級僅為 L5。
- 排名前 10 的預測皆為 L5 且建議 Hold，其中唯一關聯到試驗的項目（主動脈畸形），其試驗也與該疾病無關。

**若要推進需要：**
- 補齊 Inclisiran 的作用機轉資料與香港仿單的警語、禁忌症資料
- 取得香港許可證的核准適應症文字，以釐清原適應症
- 若要探討鉀代謝相關性，需先進行基礎機轉或觀察性研究，確認是否有生物學上的合理連結
- 在缺乏上述證據前，不建議投入資源於此再利用方向
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

