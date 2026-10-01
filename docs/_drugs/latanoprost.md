---
layout: default
title: Latanoprost
parent: 中證據等級 (L3-L4)
nav_order: 504
evidence_level: L3
indication_count: 5
---

# Latanoprost
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Latanoprost：從（許可證未載明原適應症）到原發性遺傳性青光眼

## 一句話總結

Latanoprost（DrugBank：DB00654）是一種眼用滴劑成分，在香港已有多張上市許可證，但許可證資料沒有記載原適應症。
TxGNN 模型預測它可能對**原發性遺傳性青光眼 (Primary Hereditary Glaucoma)** 有效，
目前有 **1 個臨床試驗**（Phase 2，已完成），**沒有文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 原發性遺傳性青光眼 (Primary Hereditary Glaucoma) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏輸入資料中的作用機轉描述。以下根據一般藥理知識補充：Latanoprost 是前列腺素 F2α (Prostaglandin F2-alpha) 類似物，透過增加葡萄膜鞏膜途徑 (uveoscleral) 的房水外流來降低眼內壓。降眼壓正是青光眼治療的核心策略，因此在機轉上與青光眼吻合。

TxGNN 給出 99.88% 的高分，但這只是知識圖譜的計算預測。由於許可證沒有記載原適應症，我們無法直接比對原適應症與新適應症的關聯。

要注意的是，目前唯一的臨床試驗針對的是兒童青光眼，測試的是前列腺素類似物加碳酸酐酶抑制劑的組合。它是否適用於「原發性遺傳性」這個亞型，仍需進一步確認。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01527682](https://clinicaltrials.gov/study/NCT01527682) | Phase 2 | 完成 | 37 | 評估 latanoprost 與 dorzolamide 對手術後仍控制不佳的原發性兒童青光眼的降眼壓效果與安全性（2009-07 至 2016-11） |

**證據限制：**
- 標題被截斷，無法確認青光眼的確切亞型（遺傳性／先天性或其他）。
- 資料未說明是否隨機分組及對照設計，不能視為已確認的 Phase 2 RCT。
- 試驗測試的是藥物組合，無法單獨看出 latanoprost 的貢獻。

因此證據等級維持 L3，待查證試驗紀錄後再考慮升級。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證。輸入資料未提供這些許可證的劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67041 | LATANOPROST TOA OPHTHALMIC SOLUTION 0.005% W/V | PRIMAL CHEMICAL CO LTD |
| HK-64425 | LATANO OPHTHALMIC SOLUTION 0.005%W/V | CHEMILLENNIUM INTERNATIONAL (HK) LIMITED |
| HK-65985 | MONOPOST EYE DROPS 50MCG/ML | HONG KONG MEDICAL SUPPLIES LTD |
| HK-64160 | XALAPRO EYE DROPS 0.005% W/V | ASPEN PHARMACARE ASIA LIMITED |
| HK-64335 | PROSDROP EYE DROPS SOLUTION 0.05MG/ML | LOTUS PHARMACEUTICAL HK LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。香港衛生署仿單的警語與禁忌資料目前尚未取得。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有 1 個 Phase 2 試驗，且試驗設計與亞型未獲確認，沒有任何文獻佐證。安全性的仿單資料尚未取得，無法進入安全性篩選（S1）階段。
- 同一份預測清單中的其他 4 項（內臟鈣化防禦、頭皮單純性毛髮稀少症、動脈型與靜脈型胸廓出口症候群）都只有模型預測，證據等級皆為 L5，建議同樣先擱置。其中毛髮稀少症在前列腺素類似物的藥理上有合理性（此類藥物已知會影響毛囊生長週期，如睫毛變化），但缺乏任何臨床資料。

**若要推進需要：**
- 查證 NCT01527682 的完整紀錄：青光眼亞型、是否隨機、對照組設計，以及 latanoprost 單獨的貢獻。
- 檢索針對原發性遺傳性（先天性）青光眼使用 latanoprost 的文獻。
- 下載並解析香港衛生署的仿單，取得警語與禁忌資料。
- 從 DrugBank 補齊作用機轉與原適應症資料，並確認許可證的核准適應症與劑型。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

