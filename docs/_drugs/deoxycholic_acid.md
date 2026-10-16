---
layout: default
title: Deoxycholic Acid
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Deoxycholic Acid：預測新適應症為糖尿病腎病變 (Diabetic Nephropathy)（第 3 名預測，為唯一有間接文獻的預測）（證據等級 L5）。原適應症：目前資料未記載"
monitor_inn: "DEOXYCHOLIC ACID"
predicted_indications: ["autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies", "diabetic nephropathy"]
---

# Deoxycholic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Deoxycholic Acid：從皮下脂肪（原適應症資料缺漏）到糖尿病腎病變

## 一句話總結

Deoxycholic Acid（去氧膽酸）是一種次級膽酸，在香港以注射劑（BELKYRA）及口服錠劑（ENZYPLEX）形式上市，但目前取得的資料中沒有記載原核准適應症。
TxGNN 模型預測排名最高的新適應症為極罕見的遺傳性血管疾病，但其中最具生物學合理性的是**糖尿病腎病變 (Diabetic Nephropathy)**。
目前有 **0 個臨床試驗**和 **4 篇間接相關文獻**（皆為前臨床或觀察性研究，沒有一篇直接測試去氧膽酸），整體證據仍屬模型預測階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前資料未記載（許可證的核准適應症欄位為空白） |
| 預測新適應症 | 糖尿病腎病變 (Diabetic Nephropathy)（第 3 名預測，為唯一有間接文獻的預測） |
| TxGNN 預測分數 | 99.32% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

> 說明：TxGNN 排名第 1、第 2 的預測分別為「常染色體顯性家族性血尿－視網膜小動脈迂曲－攣縮症候群」（99.49%）與「腦小血管病 1 型（伴或不伴眼部異常）」（99.49%），兩者均無任何臨床試驗或文獻，也無法建立機轉關聯，建議皆為 Hold。以下以糖尿病腎病變為主要評估對象，因為它是唯一有可供討論之文獻的預測。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知去氧膽酸是一種次級膽酸，注射於皮下可用於溶解脂肪（BELKYRA 為其注射劑型），但其在糖尿病腎病變上的直接機轉並未被證實。

間接的生物學合理性來自膽酸訊號：糖尿病腎病變患者的膽酸代謝出現改變，而膽酸訊號（如 FXR/TGR5 路徑）在前臨床模型中與腎臟保護有關。檢索到的 4 篇文獻都在描述膽酸譜變化或調節膽酸的介入（腸道菌相調節、relaxin、奈米顆粒遞送、代謝體學分析），從標題看，沒有一篇是以去氧膽酸作為治療藥物進行測試。

此外，去氧膽酸作為注射劑使用時屬局部給藥，若要用於腎臟疾病，全身暴露量與腎臟效應需另行評估。至於排名前兩名的罕見血管疾病，其高分較可能來自知識圖譜中的鄰近關聯，而非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下為糖尿病腎病變預測的相關文獻（皆為間接證據，非去氧膽酸的直接研究）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39384774](https://pubmed.ncbi.nlm.nih.gov/39384774/) | 2024 | 觀察性（世代／代謝體學） | Nutrition & Diabetes | 糖尿病腎病變患者的膽酸代謝隨疾病進展呈階段性改變 |
| [36996678](https://pubmed.ncbi.nlm.nih.gov/36996678/) | 2023 | 前臨床（STZ 誘導糖尿病小鼠） | Biomedicine & Pharmacotherapy | Relaxin 具腎臟保護作用，同時伴隨膽酸濃度上升 |
| [33378964](https://pubmed.ncbi.nlm.nih.gov/33378964/) | 2021 | 前臨床（動物模型） | Biomedicine & Pharmacotherapy | 中藥顆粒劑 QiDiTangShen 調節腸道菌相並改善糖尿病腎病變小鼠的膽酸譜 |
| [38377553](https://pubmed.ncbi.nlm.nih.gov/38377553/) | 2024 | 前臨床（奈米顆粒） | ACS Biomaterials Science & Engineering | 以腸道吸收的奈米顆粒降低氧化壓力與血管收縮，用於治療糖尿病腎病變 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65660 | BELKYRA SOLUTION FOR INJECTION 20MG/2ML（Allergan Hong Kong） | 注射液 | 資料未記載 |
| HK-06544 | ENZYPLEX TAB（Unam Corporation） | 錠劑 | 資料未記載 |

## 安全性考量

- **藥物交互作用**：資料庫共查得 67 筆交互作用，以下為部分中度（Moderate）等級項目，主要集中於抗凝血、抗血小板與溶栓藥物，可能增加出血風險：
  - Acetylsalicylic acid（阿斯匹靈）
  - Clopidogrel
  - Apixaban
  - Fondaparinux
  - Dalteparin
  - Alteplase
  - Abciximab
  - Cilostazol
  - 另有 Ibritumomab tiuxetan、Tositumomab 等放射免疫治療藥物

警語與禁忌症資料目前缺乏，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 三個預測的證據等級皆為 L5，沒有任何臨床試驗，也沒有直接測試去氧膽酸的文獻。
- 糖尿病腎病變雖有膽酸訊號的間接合理性，但仍僅是預測加關聯性證據；前兩名的罕見血管疾病則完全無法建立機轉關聯。
- 此外，目前缺少作用機轉、原核准適應症與仿單安全性資料，無法進行安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊核准適應症、警語與禁忌症
- 補充 DrugBank 的作用機轉資料，釐清去氧膽酸與 FXR/TGR5 等路徑的關聯
- 進行去氧膽酸（而非其他膽酸或介入）在糖尿病腎病變細胞或動物模型中的前臨床驗證
- 評估局部注射與口服劑型的全身暴露量與腎臟安全性
- 在上述資料補齊前，不建議投入罕見血管疾病預測的後續研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

