---
layout: default
title: Dorzolamide
parent: 高證據等級 (L1-L2)
nav_order: 290
evidence_level: L2
indication_count: 10
---

# Dorzolamide
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Dorzolamide：從青光眼到原發性遺傳性青光眼

## 一句話總結

Dorzolamide 是局部使用的碳酸酐酶抑制劑眼藥水，屬於已上市的抗青光眼藥物。
TxGNN 模型預測它可能對**原發性遺傳性青光眼 (Primary Hereditary Glaucoma)** 有效，
目前有 **1 個臨床試驗**（Phase 2，已完成，主要為兒童青光眼），**0 篇文獻**直接支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 原發性遺傳性青光眼 (Primary Hereditary Glaucoma) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 10 張 |
| 建議決策 | Hold |

> 香港許可證資料中沒有核准適應症文字，因此無法列出原適應症。Dorzolamide 本身是已上市的抗青光眼藥，此預測屬於同一疾病家族內的延伸，並非全新的老藥新用。

## 為什麼這個預測合理？

DrugBank 目前缺少詳細的作用機轉欄位。根據分析，Dorzolamide 抑制睫狀上皮的碳酸酐酶 II，減少房水生成，進而降低眼壓 (IOP)。這個機轉適用於各種以眼壓升高為特徵的青光眼。

原發性遺傳性青光眼同樣是眼壓升高造成視神經損傷的疾病。因此降眼壓在機轉上說得通，TxGNN 的高分也反映它與青光眼疾病群的距離很近。

不過目前無法確認遺傳性或兒童型青光眼是否涵蓋在既有適應症內。唯一的臨床訊號是一個兒童青光眼試驗，但試驗標題被截斷，無法確認受試者是否為先天性或遺傳性，也無法確認使用的碳酸酐酶抑制劑是否為 Dorzolamide。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | 完成 | 37 | 評估 latanoprost 與 dorzolamide 對手術後仍控制不佳的原發性兒童青光眼的降眼壓效果與安全性（2009-07 至 2016-11） |

## 文獻證據

目前無相關文獻

## 香港上市資訊

共 10 張許可證，列出其中 5 張：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-40713 | TRUSOPT EYE SOLUTION 2% | SANTEN PHARMACEUTICAL (HONG KONG) LIMITED |
| HK-66812 | REZLOD EYE DROPS SOLUTION 20MG/ML | I & C (HONG KONG) LIMITED |
| HK-64039 | DORZO EYE DROPS 2%W/V | CHEMILLENNIUM INTERNATIONAL (HK) LIMITED |
| HK-46578 | COSOPT OPHTHALMIC SOLUTION | SANTEN PHARMACEUTICAL (HONG KONG) LIMITED |
| HK-61930 | DORZOLAMIDE AND TIMOLOL STADA EYE DROPS | STADA PHARMACEUTICALS (ASIA) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉合理，但證據只有一個 Phase 2 試驗，且試驗族群（是否為遺傳性、是否使用 Dorzolamide）未能確認。
- 香港仿單的警語與禁忌資料缺漏（屬阻擋性缺口），無法進入安全性篩選。這個預測目前只能視為「研究問題」。

**若要推進需要：**
- 查閱 NCT01527682 完整登記內容，確認受試者診斷與所用藥物。
- 取得香港衛生署仿單，補齊警語與禁忌症。
- 補充 DrugBank 的作用機轉與原適應症欄位。
- 評估兒童及遺傳性青光眼族群的用藥安全性。

**補充：** 同一批預測中，「開角型青光眼」(rank 6、7) 證據最強，有多個已完成的 Phase 3 試驗與系統性回顧，證據等級為 L1。但這屬於既有適應症，並非新發現。禿髮、心臟衰竭、呼吸衰竭等其他預測缺乏可信的機轉與證據，多半是知識圖譜的推論假象，建議 Hold。

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

