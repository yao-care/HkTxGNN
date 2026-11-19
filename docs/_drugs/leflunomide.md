---
layout: default
title: Leflunomide
parent: 僅模型預測 (L5)
nav_order: 516
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-17
monitor_inn: "LEFLUNOMIDE"
predicted_indications: ["brachydactyly-syndactyly syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
description: "Leflunomide：預測新適應症為短指併指症候群 (brachydactyly-syndactyly syndrome)（證據等級 L5）。香港藥劑製品註冊：15 張（有效 14 張）"
---

# Leflunomide
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

## Leflunomide: 短指併指症候群 (brachydactyly-syndactyly syndrome)
{: .text-alpha }

## 一句話總結

Leflunomide 原本用於治療類風濕性關節炎與乾癬性關節炎。
TxGNN 模型預測它可能對**短指併指症候群 (Brachydactyly-Syndactyly Syndrome)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 短指併指症候群 (brachydactyly-syndactyly syndrome) |
| TxGNN 預測分數 | 0.9993 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 14 張／共 15 張） |
| 許可證數 | 15 張（有效 14 張） |
| 建議決策 | Hold |

另有一個排名第 2 的預測：**眼缺損小眼症－近端肢體發育不良症候群**（分數 0.9993，同樣為 L5、無試驗與文獻、建議 Hold）。本報告以排名第 1 的預測為主。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就一般藥理知識而言，Leflunomide（透過活性代謝物 teriflunomide）會抑制二氫乳清酸脫氫酶 (DHODH)，減少增生中淋巴球的嘧啶合成，因此可用於自體免疫性關節炎。這是背景知識，並非本次彙整資料所提供。

短指併指症候群屬於發育性的先天畸形，是肢體構造形成異常。從現有資料看不出免疫調節、抗增生藥物如何能矯正這類結構性缺陷，原適應症與新適應症之間也沒有明確關聯。0.9993 的 TxGNN 分數只是計算預測，並無實證支持。

此外，Leflunomide 已知具有致畸性，用於發育性疾病的情境尤其需要審慎。若要繼續評估，必須先從疾病生物學提出路徑層級的機轉假說。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 15 張單方許可證（14 張有效；HK-46486 已註銷），以下列出 5 張主要許可證（許可證資料未提供劑型與核准適應症文字）：

<!-- review:begin hk-lic-20261117-leflunomide-1 -->

> **查核更正（2026-11-17）**：原文為「香港共有 15 張有效單方許可證，」。已更正：HK-46486 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-lic-20261117-leflunomide-1 -->

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-46487 | ARAVA TAB 20MG | SANOFI HONG KONG LIMITED |
| HK-46488 | ARAVA TAB 10MG | SANOFI HONG KONG LIMITED |
| HK-46486 | ARAVA TAB 100MG | SANOFI HONG KONG LIMITED |
| HK-54040 | APO-LEFLUNOMIDE TAB 20MG | HIND WING CO LTD |
| HK-58159 | PMS-LEFLUNOMIDE TAB 10MG | TRENTON-BOMA LTD |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：肝衰竭、肝病、慢性 B 型／C 型肝炎、腎臟疾病、血小板低下、嗜中性白血球低下、顆粒球缺乏症、全血球低下、貧血、周邊神經病變、間質性肺病、肺囊蟲症、麴菌病等。此為知識圖譜的藥物－疾病關聯，並非仿單原文。
- **藥物交互作用**：共查得 100 筆，以下為部分主要項目：
  - 重大 (Major)：Acarbose、Hydrocortisone、Pioglitazone、Bupropion、Triamcinolone、Acetylsalicylic acid（阿斯匹靈）、Dexamethasone、Betamethasone、Budesonide、Clarithromycin、Minocycline、Naltrexone
  - 中度 (Moderate)：Metronidazole、Chlorpropamide、Acetohexamide
- **致畸性**：Leflunomide 已知具致畸風險，對發育性疾病的預測尤須留意。

仿單的警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個預測都只有模型分數，沒有臨床試驗與文獻，且缺乏機轉依據。
- 預測的疾病為先天發育畸形，而藥物具致畸性，風險效益關係不利。

**若要推進需要：**
- 取得 Leflunomide 的作用機轉資料，並提出與短指併指症候群致病路徑相連的機轉假說
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選
- 文獻與臨床前研究的系統性檢索，確認是否有任何支持證據
- 評估此預測在臨床上是否具可行的使用情境（目標族群、給藥時機與致畸風險管理）

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「香港共有 15 張有效單方許可證，」→「香港共有 15 張單方許可證（14 張有效；HK-46486 已註銷），」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

