---
layout: default
title: Avapritinib
parent: 僅模型預測 (L5)
nav_order: 85
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-17
description: "Avapritinib：預測新適應症為軸向脊椎骨幹骺端發育不良 (axial spondylometaphyseal dysplasia)（證據等級 L5）。原適應症：胃腸道基質瘤 (gastrointestinal stromal tumor)"
monitor_inn: "Avapritinib"
predicted_indications: ["axial spondylometaphyseal dysplasia", "bilateral parasagittal parieto-occipital polymicrogyria", "amyotrophic lateral sclerosis", "trichomegaly-retina pigmentary degeneration-dwarfism syndrome", "amyotrohpic lateral sclerosis type 22", "lower motor neuron syndrome with late-adult onset", "lethal arthrogryposis-anterior horn cell disease syndrome", "monomelic amyotrophy", "Mills syndrome"]
---

# Avapritinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Avapritinib：從胃腸道基質瘤到軸向脊椎骨幹骺端發育不良
{: .text-alpha }

## 一句話總結

Avapritinib 原本用於治療胃腸道基質瘤 (gastrointestinal stromal tumor)。
TxGNN 模型預測它可能對**軸向脊椎骨幹骺端發育不良 (axial spondylometaphyseal dysplasia)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃腸道基質瘤 (gastrointestinal stromal tumor) |
| 預測新適應症 | 軸向脊椎骨幹骺端發育不良 (axial spondylometaphyseal dysplasia) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 3 張） |
| 許可證數 | 3 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Avapritinib 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Avapritinib是一種酪胺酸激酶抑制劑，其標靶為KIT D816V、PDGFRA及PDGFRA D842突變體，以及多種KIT外顯子11、11/17及17突變體，於生化分析中的半數最大抑制濃度（IC 50）低於25 nM。PDGFRA及KIT的某些突變可導致此等受體的自體磷酸化及持續性活化，從而可促成腫瘤及肥大細胞增殖。」英文原文："Avapritinib is a tyrosine kinase inhibitor that targets KIT D816V, PDGFRA and PDGFRA D842 mutants as well as multiple KIT exon 11, 11/17 and 17 mutants with half maximal inhibitory concentrations (IC 50s ) less than 25 nM in biochemical assays. Certain mutations in PDGFRA and KIT can result in the autophosphorylation and constitutive activation of these receptors which can contribute to tumor and mast cell proliferation."（[DailyMed: Ayvakit (avapritinib) prescribing information, Blueprint Medicines Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=645c887c-8cd4-4623-8da9-ac223d71a8b9)，版本日期 2026-10-20；查閱日期 2026-11-19）。根據已知資訊，Avapritinib 是 KIT/PDGFRA 激酶抑制劑，在胃腸道基質瘤中的療效與這兩個標的相關。

然而，軸向脊椎骨幹骺端發育不良是罕見的骨骼疾病（文獻提及可能與 CFAP410/C21orf2 相關），與 KIT 或 PDGFRA 訊號傳遞沒有已知的關聯。**目前無法建立機轉上的合理連結**，0.9992 的高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，不代表生物學上的支持。

### 其他排名前列的預測

排名前 10 的預測皆為 L5（僅模型預測、無臨床或文獻證據），建議皆為 Hold：

| 排名 | 預測疾病 | TxGNN 分數 | 說明 |
|------|---------|-----------|------|
| 2 | 雙側旁矢狀頂枕多小腦回 | 0.9992 | 與 KIT/PDGFRA 無已知關聯 |
| 3 | 肌萎縮性脊髓側索硬化症 (ALS) | 0.9992 | 僅有假說層級：其他 KIT 抑制劑（如 masitinib）曾被研究；但 Avapritinib 無資料，且有認知不良反應與顱內出血風險 |
| 4 | 睫毛過長-視網膜色素變性-侏儒症候群 | 0.9992 | 極罕見，無已知關聯 |
| 5 | ALS 易感性 | 0.9991 | 與 ALS 重疊，可能為重複的本體論詞條 |
| 6 | ALS 第 22 型 | 0.9991 | 與 TUBA4A 變異相關，可能只是 TxGNN 模型（深度學習）學到的相關疾病相似性 |
| 7 | 晚發性下運動神經元症候群 | 0.9991 | 可能來自 TxGNN 模型（深度學習）學到的運動神經元疾病相似性 |
| 8 | 致死性關節攣縮-前角細胞疾病症候群 | 0.9990 | 全身性激酶抑制劑缺乏生物學依據 |
| 9 | 單肢肌萎縮症 | 0.9989 | 屬良性、自限性疾病，風險效益不利 |
| 10 | Mills 症候群 | 0.9989 | 可能僅反映 TxGNN 模型（深度學習）學到的 ALS 相關疾病相似性 |

前 10 名中有 5 個與運動神經元疾病相關，可能反映 TxGNN 模型（深度學習）學到的相關疾病相似性，而非獨立的訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67292 | AYVAKIT TABLETS 100MG | 未提供 | 未提供 |
| HK-67293 | AYVAKIT TABLETS 200MG | 未提供 | 未提供 |
| HK-67294 | AYVAKIT TABLETS 300MG | 未提供 | 未提供 |

三張許可證皆為單方，其中 HK-67293（AYVAKIT TABLETS 200MG）已註銷、其餘兩張有效，持證商為 CSTONE PHARM (HK) HOLDING LIMITED。

<!-- review:begin hk-lic-20261117-avapritinib-1 -->

> **查核更正（2026-11-17）**：原文為「三張許可證皆為單方、有效，」。已更正：HK-67293 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-lic-20261117-avapritinib-1 -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（KIT/PDGFRA 激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：資料庫共收錄 100 筆交互作用，其中以下為部分重要項目：
  - **嚴重 (Major)**：Aprepitant、Acetylsalicylic acid（阿斯匹靈）、Clarithromycin、Dexamethasone、Cobicistat、Deferasirox、Deferiprone、Ibritumomab tiuxetan、Tositumomab (I-131)、Samarium (153Sm) lexidronam
  - **中度 (Moderate)**：Cimetidine、Clotrimazole、Miconazole、Fenfluramine、Dexfenfluramine、Sibutramine、Glycerol phenylbutyrate、Metreleptin、Troglitazone、Strontium chloride Sr-89

其他警語與禁忌症資料請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測新適應症僅有 TxGNN 模型分數支持，沒有臨床試驗、文獻，也沒有合理的機轉連結。
- Avapritinib 已知有神經認知不良反應與出血風險，對罕見骨骼或神經退化性疾病的風險效益難以支持。

**若要推進需要：**
- 補齊 Avapritinib 的作用機轉資料，並分析 KIT/PDGFRA 與預測疾病的生物學關聯
- 取得香港仿單的警語、禁忌與核准適應症資料，完成安全性篩選
- 進行文獻與試驗檢索，確認是否存在前臨床證據
- 若要探索，優先考慮機轉假說較明確的 ALS，並評估中樞神經穿透性與安全性

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「三張許可證皆為單方、有效，」→「三張許可證皆為單方，其中 HK-67293（AYVAKIT TABLETS 20」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Ayvakit (avapritinib) prescribing information, Blueprint Medicines Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=645c887c-8cd4-4623-8da9-ac223d71a8b9) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

