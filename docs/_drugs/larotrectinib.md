---
layout: default
title: Larotrectinib
parent: 僅模型預測 (L5)
nav_order: 512
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
monitor_inn: "Larotrectinib"
predicted_indications: ["multiple endocrine neoplasia", "HER2 positive breast carcinoma"]
description: "Larotrectinib：預測新適應症為多發性內分泌腫瘤 (multiple endocrine neoplasia)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Larotrectinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Larotrectinib: 多發性內分泌腫瘤 (multiple endocrine neoplasia)
{: .text-alpha }

## 一句話總結

Larotrectinib 是一種選擇性 TRK 抑制劑（TRKA/B/C），在香港已有 3 張有效許可證。
TxGNN 模型預測它可能對**多發性內分泌腫瘤 (Multiple Endocrine Neoplasia, MEN)** 有效。
目前僅有 **1 個臨床試驗**（泛腫瘤籃式試驗）和 **2 篇間接相關文獻**，證據相當有限，屬於研究假說階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 多發性內分泌腫瘤 (multiple endocrine neoplasia) |
| TxGNN 預測分數 | 0.9924 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Larotrectinib 是選擇性 TRK 抑制劑，以不分腫瘤類型（tumor-agnostic）的方式用於 NTRK 融合陽性的實體腫瘤。

然而，MEN 症候群主要由 **RET（MEN2）或 MEN1 基因變異**驅動，而非 NTRK。因此兩者在機轉上的連結是間接的：只有在 NTRK 融合陽性的內分泌腫瘤，或 RET 驅動的甲狀腺癌（相關文獻討論激酶抑制劑與脫靶抗藥機制）情境下，才可能有關聯。對 MEN 本身而言，這個機轉並未被確立。

TxGNN 的高分更適合視為計算上的線索，而非有力的生物學證據。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02465060](https://clinicaltrials.gov/study/NCT02465060) | Phase 2 | 進行中（不再招募） | 6452 | NCI-MATCH：依基因檢測結果分派治療的籃式試驗，納入 NTRK 融合陽性腫瘤的 larotrectinib 組。非 MEN 專屬，無 MEN 特定結果 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31322645](https://pubmed.ncbi.nlm.nih.gov/31322645/) | 2019 | Review | Endocrine Reviews | 回顧晚期甲狀腺癌的激酶抑制劑治療，包含突變特異性適應症 |
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | 前臨床／機轉研究 | NPJ Precision Oncology | 一名 RET 突變甲狀腺髓質癌患者接受 selpercatinib 後的脫靶抗藥機制 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66491 | VITRAKVI CAPSULES 100MG | 膠囊 | 資料庫未載明 |
| HK-66492 | VITRAKVI CAPSULES 25MG | 膠囊 | 資料庫未載明 |
| HK-66493 | VITRAKVI ORAL SOLUTION 20MG/ML | 口服液 | 資料庫未載明 |

三張許可證皆由 BAYER HEALTHCARE LIMITED 持有，狀態為有效。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（TRK 激酶抑制劑），非傳統細胞毒性化療 |

其餘細胞毒性相關項目（骨髓抑制、致吐性、監測項目、處置防護）：請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為部分重點。
  - **重大 (Major)**：Clarithromycin
  - **中度 (Moderate)**：Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide、Omeprazole、Cimetidine、Aprepitant、Pioglitazone、Saxagliptin、Clotrimazole 等
  - **輕微 (Minor)**：Naloxegol

其他安全性資訊（警語、禁忌症）請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- MEN 的致病驅動基因為 RET 或 MEN1，與 TRK 抑制的關聯是間接的；唯一的臨床試驗是不限腫瘤類型的籃式試驗，沒有 MEN 專屬的療效資料。
- 目前證據僅屬研究假說層級，不足以支持進一步推進。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 補充詳細的作用機轉資料（MOA）
- 釐清 MEN 患者中是否存在 NTRK 融合陽性的亞群，並以生物標記篩選
- 檢視 NCI-MATCH 中 larotrectinib 組是否有內分泌腫瘤個案及其結果
- 若確有 NTRK 融合陽性的內分泌腫瘤，可考慮以個案或小型籃式研究驗證

---

## 其他預測適應症備註

TxGNN 的其他高分預測目前證據更弱，建議皆暫緩（Hold）：

- **HER2 陽性乳癌**：僅有前臨床研究（使用 entrectinib 與 pacritinib，並非 larotrectinib）及一例分泌型乳癌個案報告，該癌種屬 ETV6-NTRK3 融合驅動，與 HER2 陽性疾病不同。
- **乳癌其他亞型（管腔 A/B 型等）**：文獻多為 NTRK 融合癌症的一般性回顧，缺乏亞型特異證據；NTRK 融合在這些亞型中罕見，需以生物標記篩選。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

