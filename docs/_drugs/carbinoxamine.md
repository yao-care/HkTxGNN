---
layout: default
title: Carbinoxamine
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 5
monitor_inn: "Carbinoxamine"
predicted_indications: ["nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "recalcitrant atopic dermatitis", "IgE responsiveness, atopic"]
last_modified_at: 2026-11-17
description: "Carbinoxamine：預測新適應症為鼻腔疾病 (nasal cavity disease)（證據等級 L5）。香港藥劑製品註冊：12 張（有效 11 張）"
---

# Carbinoxamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Carbinoxamine：第一代 H1 抗組織胺 → 鼻腔疾病 (nasal cavity disease)
{: .text-alpha }

## 一句話總結

Carbinoxamine 是一種抗組織胺藥物，在香港已有多張單一成分許可證上市。
TxGNN 模型預測它可能對**鼻腔疾病 (nasal cavity disease)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 鼻腔疾病 (nasal cavity disease) |
| TxGNN 預測分數 | 0.9988 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 11 張／共 12 張） |
| 許可證數 | 12 張（有效 11 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Carbinoxamine 屬於第一代 H1 抗組織胺類藥物，一般認為透過阻斷組織胺 H1 受體，減輕過敏反應造成的鼻塞、流鼻水等症狀。

「鼻腔疾病」是範圍很廣、不具體的疾病類別，過敏性鼻炎等常見鼻部疾病本來就屬於其中一部分。模型給出高分，很可能反映的是這種類別上的重疊，而不是針對某個特定疾病找到了新的作用標的。

因此，這個預測目前只能視為方向性的提示。要判斷它是否具有實際的再利用價值，必須先界定更具體的鼻腔疾病亞型，再尋找對應的臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-32014 | NATIFED SYRUP | 未記載 | 未記載 |
| HK-34395 | BECAME TAB | 未記載 | 未記載 |
| HK-54148 | LONGTEC TAB | 未記載 | 未記載 |
| HK-56159 | BECAME TAB | 未記載 | 未記載 |
| HK-08596 | METOMIN TAB | 未記載 | 未記載 |

本品共有 12 張單一成分許可證（11 張有效；HK-54148 已註銷），此處僅列出 5 張主要許可證。

<!-- review:begin hk-lic-20261117-carbinoxamine-1 -->

> **查核更正（2026-11-17）**：原文為「本品共有 12 張有效的單一成分許可證，」。已更正：HK-54148 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-lic-20261117-carbinoxamine-1 -->

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為部分重點：
  - 重大 (Major)：氯化鉀 (Potassium chloride)、檸檬酸鉀 (Potassium citrate)
  - 中度 (Moderate)：抗膽鹼類藥物，如 Hyoscyamine、Atropine、Glycopyrronium、Dicyclomine、Scopolamine；中樞神經或腸胃道作用藥物，如 Morphine、Loperamide、Metoclopramide、Dronabinol、Opium

  這些交互作用多與抗膽鹼作用疊加或中樞抑制加成有關，合併使用時應留意。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究此預測疾病，證據等級為 L5。
- 預測的疾病類別過於籠統，高分很可能只是反映與既有過敏性鼻部適應症的重疊。

**若要推進需要：**
- 界定更具體的鼻腔疾病亞型，作為明確的研究目標
- 取得詳細的作用機轉資料
- 取得香港衛生署的仿單，確認警語與禁忌症
- 系統性搜尋針對該亞型的臨床試驗與文獻，評估是否有超出既有適應症的新增價值

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「本品共有 12 張有效的單一成分許可證，」→「本品共有 12 張單一成分許可證（11 張有效；HK-54148 已註銷），」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

