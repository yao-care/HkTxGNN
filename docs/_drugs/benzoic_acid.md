---
layout: default
title: Benzoic Acid
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 10
monitor_inn: "BENZOIC ACID"
predicted_indications: ["bronchitis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "dry eye syndrome", "palmar fibromatosis", "Ledderhose disease", "infantile digital fibromatosis", "hereditary angioedema with C1Inh deficiency", "posterior leukoencephalopathy syndrome", "C1 inhibitor deficiency"]
last_modified_at: 2026-11-17
description: "Benzoic Acid：預測新適應症為支氣管炎 (bronchitis)（證據等級 L5）。香港藥劑製品註冊：34 張（有效 34 張）"
---

# Benzoic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Benzoic Acid：抗菌防腐／角質溶解劑 → 支氣管炎 (bronchitis)
{: .text-alpha }

## 一句話總結

Benzoic Acid（苯甲酸）是一種具防腐、抗菌與外用角質溶解及抗黴菌作用的成分。
TxGNN 模型預測它可能對**支氣管炎 (bronchitis)** 有效，但目前**沒有臨床試驗**，僅有 2 篇間接相關文獻，且皆未直接研究苯甲酸，因此屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 支氣管炎 (bronchitis) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 34 張／共 34 張） |
| 許可證數 | 34 張（有效 34 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。苯甲酸一般作為防腐劑與外用抗菌、抗黴菌、角質溶解成分使用，主要見於外用製劑與浸泡粉劑。

就現有資料而言，找不到苯甲酸與支氣管炎之間可信的機轉關聯。取得的兩篇文獻，一篇討論瑞格列奈（repaglinide）用於第 2 型糖尿病，另一篇討論可溶性環氧化物水解酶抑制劑在吸菸誘發 COPD 的動物模型，兩者都沒有研究苯甲酸。

因此，0.9998 的高分僅代表模型計算結果，不能視為療效證據。香港現有製劑皆為外用或粉劑型態，與呼吸道疾病的給藥途徑也不相符。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11577798](https://pubmed.ncbi.nlm.nih.gov/11577798/) | 2001 | Review | Drugs | 瑞格列奈在第 2 型糖尿病的治療回顧；與苯甲酸及支氣管炎無直接關係 |
| [22180869](https://pubmed.ncbi.nlm.nih.gov/22180869/) | 2012 | 動物研究 | Am J Respir Cell Mol Biol | 可溶性環氧化物水解酶抑制劑用於吸菸誘發 COPD 模型；未涉及苯甲酸 |

## 香港上市資訊

本地許可證資料中的核准適應症文字與劑型均未記載，香港共有 34 張含本藥成分的許可證（全部有效；皆為複方）。已登記的產品包括 JEAUBAO POWDER（HK-57660）、WHITFIELD'S OINT（HK-09902）、NAFUGIN CREAM（HK-17373）、NEBODERM SPRAY（HK-45960）、COMPOUND BENZOIC ACID OINT（HK-45764）等，目前均為有效狀態。

<!-- review:begin hk-lic-20261117-benzoic_acid-1 -->

> **查核更正（2026-11-17）**：原文為「本地許可證資料中的核准適應症文字與劑型均未記載，且清單可能不完整。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 34 張含本藥成分的許可證（全部有效；皆為複方）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-benzoic_acid-1 -->

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何直接研究苯甲酸與支氣管炎的臨床試驗或文獻，證據等級為 L5，僅為模型預測。
- 現有外用製劑的給藥途徑與呼吸道疾病不符，且找不到合理的機轉關聯。

**若要推進需要：**
- 取得苯甲酸的作用機轉資料，並評估其與支氣管炎病理的關聯。
- 進行體外或動物模型的前臨床研究。
- 評估適合呼吸道的給藥途徑與劑型。
- 取得原廠仿單的警語、禁忌與交互作用資訊，進行安全性篩檢。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「本地許可證資料中的核准適應症文字與劑型均未記載，且清單可能不完整。」→「本地許可證資料中的核准適應症文字與劑型均未記載，香港共有 3」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

