---
layout: default
title: Adapalene
parent: 僅模型預測 (L5)
nav_order: 25
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-17
description: "Adapalene：預測新適應症為血漿鋅偏高 (Zinc, elevated plasma)（證據等級 L5）。原適應症：痤瘡 (Acne)"
monitor_inn: "ADAPALENE"
predicted_indications: ["zinc, elevated plasma"]
---

# Adapalene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Adapalene：從痤瘡到血漿鋅偏高
{: .text-alpha }

## 一句話總結

Adapalene 是外用第三代類視黃醇（retinoid），原本用於治療痤瘡。
TxGNN 模型預測它可能對**血漿鋅偏高 (Zinc, elevated plasma)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 痤瘡 (Acne) |
| 預測新適應症 | 血漿鋅偏高 (Zinc, elevated plasma) |
| TxGNN 預測分數 | 0.9951 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 14 張／共 16 張） |
| 許可證數 | 16 張（有效 14 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Adapalene 是外用的第三代類視黃醇，一般認為其選擇性活化 RAR-beta 與 RAR-gamma 受體，用於調節毛囊角化與發炎，進而改善痤瘡。

血漿鋅偏高通常屬於實驗室或代謝上的發現，多與鋅攝取或補充過量、或鋅恆定失衡有關，並非類視黃醇受體調節已知可治療的疾病。此外，Adapalene 外用後的全身吸收極低，更難以想像它能對血漿鋅濃度產生系統性影響。

因此，**目前找不到可信的機轉連結**。0.9951 的分數僅是模型推算的結果。若要勉強推論，可能的方向包括類視黃醇對鋅結合蛋白或金屬硫蛋白（metallothionein）表現的影響，但目前沒有任何資料支持，屬於推測。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 16 張單方許可證（14 張有效；HK-67131、HK-64722 已註銷），以下列出 5 張主要許可證（資料中未提供劑型與核准適應症文字）：

<!-- review:begin hk-lic-20261117-adapalene-1 -->

> **查核更正（2026-11-17）**：原文為「香港共有 16 張有效的單方許可證，以下列出 5 張主要許可證」。已更正：HK-67131、HK-64722 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-lic-20261117-adapalene-1 -->

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44125 | DIFFERIN CREAM 0.1%（Galderma） | 乳膏 | 未提供 |
| HK-42052 | DIFFERIN GEL 0.1%（Galderma） | 凝膠 | 未提供 |
| HK-58329 | ADAPALENE GEL 0.1%（Lafarge） | 凝膠 | 未提供 |
| HK-58988 | EPIDUO GEL（Galderma） | 凝膠 | 未提供 |
| HK-66483 | EPIDUO FORTE GEL（Galderma） | 凝膠 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自模型知識圖譜，並非仿單內容）：光敏感性疾病 (photosensitivity disease)、光誘發反應 (photoparoxysmal response)、剝脫性皮膚炎 (exfoliative dermatitis)、皮膚炎 (dermatitis)。
- **藥物交互作用**：共查得 58 筆，但嚴重程度皆未分級（Unknown）。部分例子包括 Doxycycline、Tetracycline、Minocycline、Triamcinolone、Prednisone、Omeprazole、Ibuprofen、Fluconazole 等。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型（L5），沒有臨床試驗或文獻佐證，且找不到可信的作用機轉連結。
- 血漿鋅偏高屬實驗室或代謝指標異常，外用 Adapalene 的全身吸收又極低，生物學上的合理性很弱。

**若要推進需要：**
- 補齊作用機轉資料，並釐清類視黃醇是否會影響鋅恆定（例如金屬硫蛋白、鋅結合蛋白）。
- 做系統性文獻檢索，確認是否有類視黃醇與血漿鋅相關的先前研究。
- 評估臨床上是否有真正需要治療的目標族群，以及外用劑型是否可行。
- 取得香港衛生署仿單，補齊警語、禁忌症與核准適應症資料。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「香港共有 16 張有效的單方許可證，以下列出 5 張主要許可證」→「香港共有 16 張單方許可證（14 張有效；HK-67131、HK-64722 」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

