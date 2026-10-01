---
layout: default
title: Efavirenz
parent: 中證據等級 (L3-L4)
nav_order: 303
evidence_level: L4
indication_count: 3
---

# Efavirenz
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Efavirenz：從 HIV-1 感染到貓免疫缺陷病毒相關疾病

## 一句話總結

Efavirenz 是一種非核苷類逆轉錄酶抑制劑（NNRTI），在香港已上市，使用於人類 HIV 治療的抗病毒藥物。
TxGNN 模型預測它可能對**貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome)** 有效，
但目前僅有 **1 篇體外生化／結構研究**支持，無直接的臨床試驗證據（列出的 2 個試驗皆為人類 HIV-1 研究，Efavirenz 僅為對照藥）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未提供（許可證資料中適應症欄位為空白） |
| 預測新適應症 | 貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 99.80% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Efavirenz 屬於 NNRTI 類抗逆轉錄病毒藥物，直接抑制病毒逆轉錄酶。貓免疫缺陷病毒（FIV）同為慢病毒，會造成類似後天免疫缺乏的症候群，因此在機轉上可能有交叉活性。

2023 年一篇生化與結構比較研究，將 nevirapine、efavirenz、rilpivirine 與 FIV 及 HIV 的逆轉錄酶進行比較，提示 NNRTI 對 FIV 可能有潛力。但這只是體外／結構層次的證據，沒有貓的活體療效或安全性資料。

需要注意：TxGNN 的高分（0.998）僅是知識圖譜的模型預測。此外，NNRTI 對 HIV-1 逆轉錄酶具高度專一性，對其他慢病毒（如野生型 SIV）通常效果不佳，因此此預測仍需實驗驗證。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | 完成 | 208 | Dolutegravir 用於未治療過的 HIV-1 成人之劑量選擇；Efavirenz 僅為對照，無貓或 FIV 族群 |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | 完成 | 844 | Dolutegravir + abacavir/lamivudine 對比 Atripla（含 Efavirenz）用於人類 HIV-1；僅為間接證據 |

以上試驗皆為人類 HIV-1 研究，並未檢驗 Efavirenz 對 FIV 或貓的療效。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | 體外生化／結構研究 | Journal of Veterinary Science | 比較 nevirapine、efavirenz、rilpivirine 對 FIV 與 HIV 逆轉錄酶的作用，探討 NNRTI 治療 FIV 的潛力 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66814 | APT-EFAVIRENZ TABLETS 600MG | 未提供 | 未提供 |
| HK-61617 | EFAVIRENZ SANDOZ TABLETS 600MG | 未提供 | 未提供 |
| HK-66482 | EFAVIRENZ TABLETS USP 600MG | 未提供 | 未提供 |
| HK-66634 | EFAVIRENZ TABLETS 200MG | 未提供 | 未提供 |
| HK-59769 | ESTIVA-600 TAB 600MG | 未提供 | 未提供 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
目前僅有一篇體外生化／結構研究，且缺乏貓的活體療效與安全性資料。列出的臨床試驗皆為人類 HIV-1 研究，與此預測無直接關聯。高 TxGNN 分數只是模型預測。

**若要推進需要：**
- FIV 感染貓的體外細胞培養抗病毒活性資料
- 貓的藥動學與安全性資料
- 取得香港衛生署仿單，確認警語與禁忌
- 補齊藥物作用機轉（MOA）資料
- 確認獸醫用藥的法規途徑，因為香港許可證為人用藥品

---

## 其他預測適應症（供參考）

### 猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)
- TxGNN 分數：99.80%，證據等級 L4，建議 Hold
- 有多篇獼猴 RT-SHIV（帶有 HIV-1 逆轉錄酶的嵌合病毒）模型研究，例如 [PMID 15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/)（2004）與 [PMID 15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/)（2005），評估 Efavirenz 單用或合併療法。
- 這些屬於抗病毒治療與抗藥性的動物模型研究，並非顯示對野生型 SIV 有效；野生型 SIV 一般對 NNRTI 不敏感，也不支持新的人類臨床適應症。
- 唯一列出的試驗 NCT00863668 已撤回（0 人），且與 Efavirenz 無關。

### 伴有共濟失調步態、無語言及皮質白質減少的神經發展障礙
- TxGNN 分數：99.77%，證據等級 L5，建議 Hold
- 無臨床試驗與文獻，也無法從資料建立與 Efavirenz 抗病毒機轉的連結，僅為模型預測。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

