---
layout: default
title: Prednisolone
parent: 高證據等級 (L1-L2)
nav_order: 726
evidence_level: L2
indication_count: 9
monitor_inn: "PREDNISOLONE"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "prolapse of lacrimal gland"]
last_modified_at: 2026-11-20
description: "Prednisolone：預測新適應症為斑禿 (Alopecia Areata)（證據等級 L2）。原適應症：香港許可證資料未載明核准適應症文字"
---

# Prednisolone
{: .fs-9 }

證據等級: **L2** | 預測適應症: **9** 個
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

## Prednisolone：從自體免疫疾病到斑禿
{: .text-alpha }

## 一句話總結

Prednisolone 是一種糖皮質激素（類固醇），在知識圖譜中記錄的相關用途包括自體免疫疾病、克隆氏症、腎上腺皮質功能不全與急性淋巴性白血病等。
TxGNN 模型預測它可能對**斑禿 (Alopecia Areata)** 有效。
目前沒有臨床試驗登記，但有 **1 篇安慰劑對照隨機試驗**（口服脈衝式 prednisolone）及多篇系統性回顧與綜述支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症文字；知識圖譜記錄的關聯包括自體免疫疾病、克隆氏症、腎上腺皮質功能不全等（屬知識圖譜關聯，非核准適應症） |
| 預測新適應症 | 斑禿 (Alopecia Areata) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L2 |
| 香港上市 | 上市中（有效許可證 40 張／共 40 張） |
| 許可證數 | 40 張（有效 40 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Prednisolone 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Prednisolone 是一種合成的腎上腺皮質類固醇藥物，主要具有糖皮質素特性。其中部分特性重現內生性糖皮質類固醇的生理作用，但其他特性則不一定反映任何腎上腺激素的正常功能；這些特性僅在投予大劑量治療劑量的本藥後才會出現。」英文原文："Prednisolone is a synthetic adrenocortical steroid drug with predominantly glucocorticoid properties. Some of these properties reproduce the physiological actions of endogenous glucocorticosteroids, but others do not necessarily reflect any of the adrenal hormones' normal functions; they are seen only after administration of large therapeutic doses of the drug."（[DailyMed: Orapred Odt (prednisolone sodium phosphate) prescribing information, Advanz Pharma (US) Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e379543-c4cf-4e72-953b-db15b7f0c2a1)，版本日期 2025-06-03；查閱日期 2026-11-19）。根據已知藥理，prednisolone 是糖皮質激素，具有廣泛的抗發炎與免疫抑制作用，包括抑制 T 細胞活化與細胞激素產生。

斑禿是 T 細胞媒介的自體免疫疾病，毛囊失去免疫豁免而遭攻擊。Prednisolone 的免疫抑制作用正好針對這個機轉，也與其在其他自體免疫疾病的用途相符。

需注意：療效以抑制為主，停藥後復發常見。長期全身性使用受限於副作用（如下視丘-腦下垂體-腎上腺軸抑制、骨質流失、代謝影響），因此多採脈衝或短期療程。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | RCT | J Am Acad Dermatol | 安慰劑對照的口服脈衝 prednisolone 治療斑禿 |
| [16310088](https://pubmed.ncbi.nlm.nih.gov/16310088/) | 2005 | 評論 | J Am Acad Dermatol | 對上述隨機試驗的批判性評讀，討論口服脈衝 prednisolone 的實用性 |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | 網絡統合分析 | Cochrane Database Syst Rev | 比較斑禿的多種治療（免疫抑制劑、生髮刺激劑、接觸免疫療法） |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | 系統性回顧 | Australas J Dermatol | 評估斑禿全身性治療的證據 |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | 回顧皮質類固醇脈衝療法的療效、復發率與副作用 |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatr Dermatol | 兒童斑禿脈衝類固醇的劑量與給藥方式 |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | 世代／開放標示研究 | Dermato-endocrinology | 中劑量 prednisolone 脈衝治療斑禿；早期有效，但副作用可能導致停藥 |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | 世代研究 | J Dtsch Dermatol Ges | 重度兒童斑禿先高劑量後低劑量的全身性類固醇；復發難免 |
| [32779249](https://pubmed.ncbi.nlm.nih.gov/32779249/) | 2020 | 回溯研究 | J Eur Acad Dermatol Venereol | 138 位慢性斑禿患者使用類固醇節省藥物的持續率 |
| [30294905](https://pubmed.ncbi.nlm.nih.gov/30294905/) | 2019 | 機轉研究 | J Cosmet Dermatol | 口服脈衝類固醇可能透過改變血清與組織 TNF-α 濃度發揮作用 |

## 香港上市資訊

以下為已登記的主要單一成分許可證（核准適應症文字於資料中未提供）：

<!-- review:begin hk-lic-20261117-prednisolone-1 -->

> **查核更正（2026-11-17）**：原文為「以下為已登記的主要單一成分許可證（清單可能不完整，核准適應症文字於資料中未提供）：」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊：共有 40 張含本藥成分的許可證（全部有效；單一成分 39 張、複方 1 張）（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-prednisolone-1 -->

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66155 | PREDNISOLONE TABLETS 5MG | 未載明 | 未載明 |
| HK-30888 | XEPASONE TAB 5MG | 未載明 | 未載明 |
| HK-55339 | PANADIN TAB 5MG | 未載明 | 未載明 |
| HK-62772 | KORUS PREDNISOLONE TABLETS 5MG | 未載明 | 未載明 |
| HK-66075 | SUNOSYN SYRUP 3MG/5ML | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：高血壓、癲癇、高血糖、充血性心衰竭、麻疹、單純皰疹病毒角膜炎、紫質症、尿素循環異常（如 CPS I 缺乏、瓜胺酸血症、高精胺酸血症）、腦下垂體功能低下與相關生長激素缺乏等。
- **藥物交互作用**：共查詢到 100 筆。主要包括：
  - 重度：Adalimumab
  - 中度：Zidovudine、Isotretinoin、Acarbose、Acebutolol、Acetazolamide、Ketorolac、Ibuprofen、Nifedipine、Ethinylestradiol、Aldesleukin、Alemtuzumab、Aliskiren 等
  - 輕度：Formoterol、Salbutamol

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有 1 項直接研究斑禿的安慰劑對照 RCT，並有多篇系統性回顧與綜述討論 prednisolone／類固醇脈衝療法，機轉上亦合理。但目前無臨床試驗登記，且停藥後復發常見、長期全身性使用有明確副作用風險，因此需設定防護條件。

**若要推進需要：**
- 取得香港許可證的核准適應症與仿單警語、禁忌資料
- 釐清脈衝或短期療程的劑量方案，並規劃復發後的處置
- 建立長期使用的安全監測計畫（血壓、血糖、骨密度、下視丘-腦下垂體-腎上腺軸功能）
- 檢視重度交互作用（如 adalimumab）與知識圖譜所列的禁忌族群
- 補充詳細的作用機轉資料

**其他預測適應症簡述：**
排名第 2 至第 9 的預測（毛囊黏蛋白症、休止期落髮、禿髮性毛囊炎等）目前均無直接支持 prednisolone 的證據，建議皆為 Hold。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「以下為已登記的主要單一成分許可證（清單可能不完整，核准適應症文字於資料中未提供）」→「以下為已登記的主要單一成分許可證（核准適應症文字於資料中未提」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Orapred Odt (prednisolone sodium phosphate) prescribing information, Advanz Pharma (US) Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e379543-c4cf-4e72-953b-db15b7f0c2a1) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

