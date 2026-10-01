---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 467
evidence_level: L5
indication_count: 5
---

# Insulin Lispro
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

# Insulin Lispro：從糖尿病到自體免疫性卵巢炎

## 一句話總結

Insulin lispro 是速效胰島素類似物，原本用於血糖控制（糖尿病治療）。
TxGNN 模型預測它可能對**自體免疫性卵巢炎 (Autoimmune Oophoritis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 自體免疫性卵巢炎 (Autoimmune Oophoritis) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般而言，insulin lispro 是速效胰島素類似物，透過胰島素受體降低血糖。本次輸入資料中的許可證未記載適應症，「糖尿病」是依藥理常識補充，並非來自香港許可證欄位。

自體免疫性卵巢炎與其他自體免疫內分泌疾病（如多腺體自體免疫症候群中的第 1 型糖尿病）常同時出現。胰島素只能處理併發的糖尿病，無法治療卵巢炎本身。因此 0.998 的高分較可能來自知識圖譜中的關聯，並非藥理上的直接證據。

排名前 5 的預測（另有硬直人症候群、硫胺素反應性功能障礙症候群、Opsismodysplasia）都屬於類似情況，多為共病關聯或訊號通路層級的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-60381 | HUMALOG 100 U/ML KWIKPEN SOLUTION FOR INJECTION | ELI LILLY ASIA, INC. |
| HK-42887 | HUMALOG INJ 3ML CARTRIDGE 100U/ML | ELI LILLY ASIA, INC. |
| HK-42886 | HUMALOG INJ 100U/ML | ELI LILLY ASIA, INC. |
| HK-60379 | HUMALOG MIX50 100 U/ML KWIKPEN SUSPENSION FOR INJECTION | ELI LILLY ASIA, INC. |
| HK-60380 | HUMALOG MIX25 100 U/ML KWIKPEN SUSPENSION FOR INJECTION | ELI LILLY ASIA, INC. |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測（L5），沒有試驗或文獻。
- 機轉上，胰島素只能治療共病的糖尿病，沒有直接治療卵巢炎的依據。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌資料。
- 補充 DrugBank 作用機轉資料。
- 進行文獻與試驗檢索，確認是否有胰島素直接影響卵巢自體免疫的證據。
- 確認預測是否只反映共病關聯，若是則不建議作為再利用候選。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

