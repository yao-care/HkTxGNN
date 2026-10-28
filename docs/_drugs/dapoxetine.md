---
layout: default
title: Dapoxetine
parent: 僅模型預測 (L5)
nav_order: 244
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Dapoxetine：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L4）。原適應症：早發性射精（Premature Ejaculation）、心因性性交疼痛"
monitor_inn: "DAPOXETINE"
predicted_indications: ["migraine disorder", "dysthymic disorder", "migraine with brainstem aura"]
---

# Dapoxetine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Dapoxetine：從早發性射精到偏頭痛
{: .text-alpha }

## 一句話總結

Dapoxetine 是一種短效型選擇性血清素再吸收抑制劑（SSRI），原本用於治療早發性射精。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
但目前**沒有臨床試驗**，僅有 **2 篇相關文獻**（其中只有 1 篇為 SSRI 類別的偏頭痛相關綜述），證據屬於間接、類別層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 早發性射精（Premature Ejaculation）、心因性性交疼痛 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 0.9934 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 許可證數 | 6 張（有效 6 張） |
| 建議決策 | Hold |

註：香港許可證資料中未提供核准適應症文字，故原適應症資料另有來源，並非本頁預測分數的依據；預測分數來自 TxGNN 模型（深度學習），可能反映模型在相關疾病間學到的相似性，並非生物學證據。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Dapoxetine 屬於 SSRI 類藥物，藥理資料顯示其作用標的為血清素轉運體（SERT，基因 SLC6A4）。其作用機轉推論自藥物類別，而非直接的原廠資料。

血清素失調被認為與偏頭痛的病理生理有關，其他 SSRI 也曾以仿單標示外用途探討用於偏頭痛預防。因此，從機轉上看，這個預測有一定的生物學合理性，但僅屬間接、類別層級的支持。

需要注意的是，Dapoxetine 設計為快速起效、半衰期短的隨需使用藥物，這與偏頭痛預防所需的長期規律給藥並不相符。TxGNN 分數雖高，但沒有 Dapoxetine 專屬的臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33998993](https://pubmed.ncbi.nlm.nih.gov/33998993/) | 2022 | Review | Current Neuropharmacology | 回顧 SSRI 的仿單標示外用途，範圍涵蓋偏頭痛等；屬類別層級證據，非 Dapoxetine 專屬 |
| [23504864](https://pubmed.ncbi.nlm.nih.gov/23504864/) | 2013 | Cohort | Urologia | 探討早發性射精患者使用 Dapoxetine 的治療依從性；與偏頭痛無直接關聯 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68318 | ADAPORIN TABLETS 60MG | 錠劑 | 資料未提供 |
| HK-66777 | OXETINE TABLETS 60MG | 錠劑 | 資料未提供 |
| HK-60174 | PRILIGY TAB 30MG | 錠劑 | 資料未提供 |
| HK-68951 | BF-DAPOXETINE FILM-COATED TABLETS 30MG | 膜衣錠 | 資料未提供 |
| HK-60175 | PRILIGY TAB 60MG | 錠劑 | 資料未提供 |

另有 HK-68541（BIDARLY TABLETS 30MG），共 6 張有效的單方許可證。

## 安全性考量

- **藥物交互作用**：藥理資料顯示其作用標的為血清素轉運體（SERT），屬 SSRI 類藥理作用；目前沒有具體藥物間交互作用的分級資料。

其餘警語與禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 偏頭痛預測僅有高分的模型預測和 SSRI 類別的間接文獻支持，沒有 Dapoxetine 專屬的臨床試驗。
- 藥物的短效、隨需使用特性與偏頭痛預防的長期給藥需求不吻合，且安全性資料尚未完整。

**若要推進需要：**
- 補齊作用機轉資料（MOA）
- 取得香港衛生署仿單的警語與禁忌症資料
- 蒐集 Dapoxetine 或同類 SSRI 用於偏頭痛預防的臨床證據
- 評估短效藥動學是否適合偏頭痛的治療情境
- 排序較低的「心境惡劣症」與「腦幹型先兆偏頭痛」目前僅有模型預測（L5），建議同樣暫緩，且後者可能與偏頭痛的訊號重疊
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

