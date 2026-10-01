---
layout: default
title: Isotretinoin
parent: 僅模型預測 (L5)
nav_order: 483
evidence_level: L5
indication_count: 2
---

# Isotretinoin
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

# Isotretinoin：從原適應症資料缺漏到惡性腎血管性高血壓

## 一句話總結

Isotretinoin 是一種維甲酸類（retinoid）藥物，在香港已有 13 張上市許可證，但本次資料未載明原適應症。
TxGNN 模型預測它可能對**惡性腎血管性高血壓 (Malignant Renovascular Hypertension)** 有效，另有一個分數相同的預測是惡性高血壓性腎病。
目前**沒有任何臨床試驗或文獻**支持，證據僅來自模型分數（L5）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 惡性腎血管性高血壓 (Malignant Renovascular Hypertension) |
| TxGNN 預測分數 | 99.01% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，也沒有原適應症資料，因此無法把藥物機轉和預測疾病逐項對照。Isotretinoin 屬於維甲酸類藥物，這是目前唯一可依循的機轉線索。

有報告指出，維甲酸訊號會影響腎臟近腎絲球細胞（juxtaglomerular cells）的腎素表現。這可能使腎素－血管張力素系統的活性上升而非下降，所以對高血壓的作用方向不確定，甚至可能不利。

另一個預測「惡性高血壓性腎病」的分數與本預測完全相同（99.01%），兩者很可能來自知識圖譜中的同一個鄰近區域，不應視為兩個獨立訊號。

整體來看，這個分數只能當作產生假說的線索，不能視為療效證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

共 13 張許可證，以下列出 5 張主要許可證。資料中未載明劑型與核准適應症，故省略這兩欄。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-55931 | REDUCAR CAP 10MG | HEALTH ALLIANCE INTERNATIONAL CO LTD |
| HK-56026 | REDUCAR CAP 20MG | HEALTH ALLIANCE INTERNATIONAL CO LTD |
| HK-20965 | ROACCUTANE CAP 10MG | ZUELLIG PHARMA LIMITED |
| HK-52035 | ACNOTIN 20 CAP 20MG | DCH AURIGA (HONG KONG) LIMITED - HEALTHCARE DIVISION |
| HK-50197 | ORATANE CAP 20MG | UNITED ITALIAN CORP (HK) LTD |

---

## 安全性考量

安全性資訊請參考原廠仿單。藥物交互作用查詢無結果。

依現有評估，isotretinoin 具致畸胎性，也會使血脂升高。對於心血管與腎臟風險偏高的族群，這兩點都是不利因素。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有試驗、文獻或機轉資料佐證。維甲酸訊號還可能推高腎素活性，作用方向不確定。
- 安全性上的疑慮（致畸胎性、血脂升高）也不利於在高風險心血管與腎臟族群使用。

**若要推進需要：**
- 系統性搜尋 PubMed 與 ClinicalTrials.gov，確認是否有相關研究。
- 補齊 isotretinoin 的作用機轉資料（可查詢 DrugBank），並做機轉審查，特別是腎素－血管張力素系統的作用方向。
- 取得香港衛生署仿單，補上警語與禁忌症，才能進入安全性篩選。
- 補齊各許可證的核准適應症，釐清原適應症。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

