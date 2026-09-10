---
layout: default
title: Norfloxacin
parent: 僅模型預測 (L5)
nav_order: 531
evidence_level: L5
indication_count: 5
---

# Norfloxacin
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

# Norfloxacin：從細菌感染治療到 Polyclonal Hyperviscosity Syndrome

## 一句話總結

Norfloxacin 是 fluoroquinolone 類抗生素，原用於細菌感染治療（抑制細菌 DNA gyrase/topoisomerase IV）。
TxGNN 模型預測它可能對**多株性高黏滯血症 (Polyclonal Hyperviscosity Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，屬於純模型分數預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（無許可證與適應症紀錄） |
| 預測新適應症 | Polyclonal Hyperviscosity Syndrome |
| TxGNN 預測分數 | 99.70% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Norfloxacin 詳細的作用機轉資料庫紀錄，但根據證據包內的機轉描述，Norfloxacin 為 fluoroquinolone 類抗生素，主要透過抑制細菌 DNA gyrase/topoisomerase IV 達到抗菌效果。

多株性高黏滯血症屬於漿細胞疾病相關的病生理異常（血漿蛋白黏滯度增高），與抗生素的抗菌機轉之間**沒有已知的生物學關聯路徑**。證據包本身也明確指出「無法建立合理生物學路徑」。

換言之，此預測目前僅為 TxGNN 模型分數所驅動，缺乏機轉層面的合理性支持，也沒有原始適應症資料可供比對關聯性。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他 TxGNN 候選適應症（次要，僅供參考）

同批預測中另有 4 個候選適應症，證據強度同樣薄弱，決策均為 Hold：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 備註 |
|------|------|-----------|---------|------|
| 2 | Hyperamylasemia | 99.70% | L5 | 無臨床/文獻證據，機轉無關聯 |
| 3 | Congenital Analbuminemia | 99.67% | L5 | 遺傳性肝臟合成缺陷，機轉無關聯 |
| 4 | Blood Group Incompatibility | 99.55% | L5 | 免疫/輸血醫學議題，機轉無關聯 |
| 5 | Punctate Epithelial Keratoconjunctivitis | 99.54% | L4 | 有 2 篇文獻但探討對象為微孢子蟲感染，非細菌性，藥理機轉不匹配（抗菌 vs 抗寄生蟲） |

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測適應症（Polyclonal Hyperviscosity Syndrome）無任何臨床試驗或文獻佐證，機轉上也無合理連結，證據等級僅 L5。
- 藥物本身在香港未上市（0 張許可證），且原適應症、MOA、安全性資料均缺失，無法完成基本安全性初評。

**若要推進需要：**
- 補齊 TFDA/香港衛生署仿單警語與禁忌症資料（DG001，Blocking）
- 取得 DrugBank 完整 MOA 資料（DG002，High）
- 若要評估 rank 5（角結膜炎）候選，需釐清 fluoroquinolone 對微孢子蟲感染是否有實證支持，目前文獻對象與藥物適應機轉不一致
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

