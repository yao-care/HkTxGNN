---
layout: default
title: Metformin
parent: 僅模型預測 (L5)
nav_order: 568
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-17
description: "Metformin：預測新適應症為典型僵人症候群 (Classic Stiff Person Syndrome)（證據等級 L5）。原適應症：第二型糖尿病 (Type 2 Diabetes Mellitus)"
monitor_inn: "Metformin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
---

# Metformin
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

## Metformin：從第二型糖尿病到僵人症候群（Classic Stiff Person Syndrome）
{: .text-alpha }

## 一句話總結

Metformin（二甲雙胍）原本用於治療第二型糖尿病。
TxGNN 模型預測它可能對**典型僵人症候群 (Classic Stiff Person Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第二型糖尿病 (Type 2 Diabetes Mellitus) |
| 預測新適應症 | 典型僵人症候群 (Classic Stiff Person Syndrome) |
| TxGNN 預測分數 | 0.9945 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 112 張／共 114 張） |
| 許可證數 | 114 張（有效 112 張） |
| 建議決策 | Hold |

註：原適應症取自 TxGNN 模型（深度學習）所用的適應症資料，香港許可證的核准適應症文字在本次資料中皆為空白。預測分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病間學到的相似性，並非生物學證據。

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Metformin 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Metformin 是一種抗高血糖藥物，可改善第 2 型糖尿病患者的葡萄糖耐受性，降低基礎及餐後血漿葡萄糖。Metformin 可減少肝臟葡萄糖生成、減少腸道對葡萄糖的吸收，並透過增加周邊組織對葡萄糖的攝取與利用而改善胰島素敏感性。」英文原文："Metformin is an antihyperglycemic agent which improves glucose tolerance in patients with type 2 diabetes mellitus, lowering both basal and postprandial plasma glucose. Metformin decreases hepatic glucose production, decreases intestinal absorption of glucose, and improves insulin sensitivity by increasing peripheral glucose uptake and utilization."（[DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574)，版本日期 2026-09-21；查閱日期 2026-11-19）。Metformin 在第二型糖尿病的療效已被證實，一般認為其作用與改善胰島素敏感性、活化 AMPK 路徑有關，但這部分並非來自本次彙整的資料，僅供參考。

僵人症候群是一種自體免疫性神經疾病（常見抗 GAD65 抗體），常與第一型糖尿病及其他自體免疫疾病並存。因此可推測 Metformin 透過 AMPK 活化與免疫代謝調節可能有某種關聯。但 Metformin 的抗發炎作用在這類神經疾病中尚未被證實，本次資料也不支持任何直接機轉。

需要特別注意：同屬僵硬類疾病的**局限性僵肢症候群 (Focal Stiff Limb Syndrome)** 得到完全相同的分數 (0.9945)，顯示預測來自 TxGNN 模型（深度學習）中相近疾病的鄰近關係，而非獨立證據。

### 其他預測適應症（皆為 L5，建議 Hold）

| 排名 | 預測適應症 | TxGNN 分數 | 備註 |
|------|-----------|-----------|------|
| 2 | 局限性僵肢症候群 (Focal Stiff Limb Syndrome) | 0.9945 | 與排名 1 同分；分數來自 TxGNN 模型（深度學習），可能反映模型學到的相近疾病之間的相似性，而非生物學證據 |
| 3 | 骨發育不良症 (Opsismodysplasia) | 0.9940 | INPPL1 突變影響 PI3K/AKT 訊號，與 Metformin 的胰島素/AMPK/mTOR 路徑理論上有重疊，但未經驗證 |
| 4 | 硫胺素反應性功能異常症候群 (Thiamine-responsive Dysfunction Syndrome) | 0.9940 | Metformin 至多是治療合併的糖尿病，而非改善疾病本身；與有機陽離子轉運蛋白的交互作用也需留意 |
| 5 | 藥物誘發性局部脂肪營養不良 (Drug-induced Localized Lipodystrophy) | 0.9906 | 改善胰島素敏感性有生物學上的合理性，但局部型病理不同，相關性不確定 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 114 張含本藥成分的許可證（有效 112 張、已註銷 2 張；單一成分 76 張、複方 38 張）。以下列出 5 張主要許可證：

<!-- review:begin hk-lic-20261117-metformin-1 -->

> **查核更正（2026-11-17）**：原文為「香港共有 20 張有效單方許可證（無已註銷）。」。已更正：HK-54377 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。 現行名單另有產品名與成分相同的 HK-56689（METFORMIN TAB 500MG）與 2026-03 版名單之後新增的 HK-69116、HK-69117、HK-69131、HK-69132（單方）等，已補收（2026-11-17 核對）。 已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 114 張含本藥成分的許可證（有效 112 張、已註銷 2 張；單一成分 76 張、複方 38 張）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-lic-20261117-metformin-1 -->

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-27087 | GLUCOPHAGE TAB 500MG（Merck Pharmaceutical (HK)） | 未標示 | 未標示 |
| HK-50383 | GLUCOPHAGE TAB 1000MG（Merck Pharmaceutical (HK)） | 未標示 | 未標示 |
| HK-68753 | GLUCOPHAGE XR PROLONGED-RELEASE TABLETS 500MG（Merck Pharmaceutical (HK)） | 未標示 | 未標示 |
| HK-65175 | METFORMIN SANDOZ TABLETS 500MG（Sandoz Hong Kong） | 未標示 | 未標示 |
| HK-66869 | METPHAR XR 750 EXTENDED-RELEASE TABLETS 750MG（Primal Chemical） | 未標示 | 未標示 |

---

## 安全性考量

- **禁忌症（來自知識圖譜，非仿單內容）**：圖譜標示的相關疾病包括肝衰竭、腎臟疾病、胰臟炎、肝臟疾病、膽囊疾病、充血性心衰竭、腎上腺皮質功能不全、腦下垂體功能低下及相關先天性疾病（如 Kallmann 症候群、Sheehan 症候群）等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - **嚴重 (Major)**：Acetazolamide、乙醇 (Ethanol)
  - **中度 (Moderate)**：Dolutegravir、Abemaciclib、Ranitidine、Nifedipine、Ibuprofen、Ketorolac、Hydrochlorothiazide、Ethinylestradiol、Hydrocortisone、Epinephrine、Salbutamol 等
  - **輕微 (Minor)**：Acarbose、外用 Hydrocortisone

仿單的警語與禁忌症資料目前缺漏，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何臨床試驗或文獻佐證（證據等級 L5），且機轉連結屬推測。
- 排名 1 與 2 的分數完全相同（0.9945）；分數來自 TxGNN 模型（深度學習），可能反映模型學到的相近疾病之間的相似性，而非獨立的生物學證據。

**若要推進需要：**
- 取得 Metformin 的詳細作用機轉資料（MOA）
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選
- 系統性檢索 Metformin 與僵人症候群、抗 GAD65 自體免疫的文獻與試驗，確認是否存在支持證據
- 若有初步證據，再評估神經疾病族群使用的安全性與合適劑型

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「香港共有 20 張有效單方許可證（無已註銷）。」→「香港共有 114 張含本藥成分的許可證（有效 112 張、已」 | 更正（2026-11-17 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Metformin Hydrochloride Er (metformin hydrochloride) prescribing information, Leading Pharma, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3dca884d-ec44-496f-9eeb-31fd8fa3f574) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

