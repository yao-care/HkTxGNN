---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 318
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Emtricitabine：預測新適應症為貓後天免疫缺陷症候群 (Feline Acquired Immunodeficiency Syndrome)（證據等級 L5）。原適應症：HIV 感染、AIDS"
monitor_inn: "EMTRICITABINE"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Emtricitabine
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

## Emtricitabine：從 HIV 感染到貓後天免疫缺乏症候群
{: .text-alpha }

## 一句話總結

Emtricitabine 是一種核苷類逆轉錄酶抑制劑，原本用於治療 HIV 感染與 AIDS。
TxGNN 模型預測它可能對**貓後天免疫缺陷症候群 (Feline Acquired Immunodeficiency Syndrome)** 有效，
目前**沒有臨床試驗**，只有 **1 篇文獻**（前臨床／獸醫研究）直接支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染、AIDS |
| 預測新適應症 | 貓後天免疫缺陷症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 15 張／共 15 張） |
| 許可證數 | 15 張（有效 15 張） |
| 建議決策 | Hold |

> 補充：排名第 2 的「猴免疫缺陷病毒感染 (SIV)」有較多獼猴研究，但屬於 HIV 預防的動物模型，並不構成新的人類適應症。排名第 3 的神經發育疾患沒有任何證據支持。

## 為什麼這個預測合理？

根據美國 FDA 核准的 Emtricitabine 處方資料（Prescribing Information）「Mechanism of Action」與「Microbiology」段（非官方翻譯）：「Emtricitabine 是一種抗反轉錄病毒藥物。[…] FTC 是一種胞苷（cytidine）的合成核苷類似物，經細胞酵素磷酸化後形成 emtricitabine 5'-三磷酸（FTC-TP），FTC-TP 透過與天然受質 deoxycytidine 5'-三磷酸競爭，以及嵌入新生的病毒 DNA 而導致鏈終止，從而抑制 HIV-1 反轉錄酶（RT）的活性。FTC-TP 對哺乳動物 DNA 聚合酶 α、β、ε 及粒線體 DNA 聚合酶 γ 為弱抑制劑。」英文原文："Emtricitabine is an antiretroviral drug. […] FTC, a synthetic nucleoside analog of cytidine, is phosphorylated by cellular enzymes to form emtricitabine 5'-triphosphate (FTC-TP), which inhibits the activity of the HIV-1 reverse transcriptase (RT) by competing with the natural substrate deoxycytidine 5'-triphosphate and by being incorporated into nascent viral DNA resulting in chain termination. FTC-TP is a weak inhibitor of mammalian DNA polymerases α, β, ε, and mitochondrial DNA polymerase γ."（[DailyMed: Emtriva (emtricitabine) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d6599395-3944-44f9-97f2-e0424c6b6a1f)，版本日期 2026-11-06；查閱日期 2026-11-19）。根據已知資訊，emtricitabine 是核苷類逆轉錄酶抑制劑 (NRTI)，透過在細胞內磷酸化後終止病毒 DNA 鏈延長來抑制複製。其在 HIV 感染中的療效已被證實。

貓免疫缺陷病毒 (FIV) 是與 HIV 相近的慢病毒，同樣依賴逆轉錄酶，因此機轉上有合理性。FIV 在貓身上造成的進行性免疫功能障礙，與 HIV 在人類的表現相似。

但需要注意：目前唯一的直接證據是 2023 年一篇以 dolutegravir、tenofovir、emtricitabine 組合治療 FIV 感染貓的研究，該研究評估的是整個組合療法，無法單獨確認 emtricitabine 的療效。獸醫用藥的安全性與劑量也尚未建立。0.999 的高分較可能反映 HIV 類似的生物學特性，而非臨床資料支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

**預測適應症（貓免疫缺陷症候群）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | 前臨床／獸醫研究 | Viruses | 以 dolutegravir、tenofovir、emtricitabine 組合療法治療 FIV 感染貓，評估藥動學與臨床結果；僅標題層級評估，無法確認 emtricitabine 單獨療效 |

**相關動物模型文獻（猴免疫缺陷病毒／SHIV，排名第 2 預測）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | 前臨床動物研究 | J Infect Dis | 口服 FTC/TAF 可保護獼猴免於直腸 SHIV 感染 |
| [26743846](https://pubmed.ncbi.nlm.nih.gov/26743846/) | 2016 | 前臨床動物研究 | J Infect Dis | FTC/TDF 在合併披衣菌與陰道滴蟲感染的獼猴中仍可預防陰道 SHIV 感染 |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | 前臨床動物研究 | J Infect Dis | 口服 TAF/FTC 或單用 TAF 對獼猴陰道 SHIV 感染的保護效果 |
| [24914761](https://pubmed.ncbi.nlm.nih.gov/24914761/) | 2014 | 前臨床動物研究 | AIDS Res Hum Retroviruses | VLP 疫苗合併部分保護性口服 PrEP 可預防獼猴 SHIV 感染 |
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | 前臨床病毒學研究 | J Virol | SIV 的 M184V 突變在治療後迅速出現，且適應性下降 |
| [22918448](https://pubmed.ncbi.nlm.nih.gov/22918448/) | 2012 | 回顧 | Curr Opin HIV AIDS | 彙整 MSM 族群抗病毒預防的動物與臨床資料 |
| [22964889](https://pubmed.ncbi.nlm.nih.gov/22964889/) | 2012 | 回顧 | Curr Opin HIV AIDS | 抗病毒預防的動物模型經驗與未來方向 |
| [20874040](https://pubmed.ncbi.nlm.nih.gov/20874040/) | 2010 | 回顧 | Pharmacotherapy | 全身性 HIV 暴露前預防的回顧 |

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-64704 | DESCOVY TABLETS 200MG/25MG | 複方 | GILEAD SCIENCES HONG KONG LIMITED | 有效 |
| HK-57749 | TRUVADA TAB (IRELAND) | 複方 | GILEAD SCIENCES HONG KONG LIMITED | 有效 |
| HK-56076 | TRUVADA TAB | 複方 | GILEAD SCIENCES HONG KONG LIMITED | 有效 |
| HK-65914 | BIKTARVY TABLETS | 複方 | GILEAD SCIENCES HONG KONG LIMITED | 有效 |
| HK-65912 | SYMTUZA TABLETS | 複方 | JOHNSON & JOHNSON (HONG KONG) LTD. | 有效 |

上表列出其中 5 張（共 15 張）。

<!-- licenses:end -->

另有其他許可證（含多家學名藥與 ODEFSEY 等）；含本藥成分的許可證皆為複方，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表。

<!-- review:begin hk-lic-20261124b-emtricitabine-1 -->

> **查核更正（2026-11-24）**：原文為「另有 10 張單方許可證（含多家學名藥與 ODEFSEY 等），皆為有效狀態。」。已更正：依衞生署藥物辦公室註冊名單的成分欄，含本藥成分的許可證皆為複方；原句的單一成分／複方說法或張數跟註冊名單不符（舊報告依證據包以「;;」切成分，每張都算成單方）。張數見本頁快速總覽與許可證表（2026-11-24 核對）。依據：[衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261124b-emtricitabine-1 -->

## 安全性考量

- **藥物交互作用**：共查得 20 筆，其中 **Major** 等級 2 筆：Leflunomide、Teriflunomide。Moderate 等級包括 Cobicistat、Methotrexate、Cladribine、Clofarabine、Interferon beta-1a/1b、Orlistat、Naltrexone 等；Eribulin 為 Minor。
- **知識圖譜標示的疾病禁忌關聯**（非仿單內容）：肝衰竭、肝病、腎病、乳酸中毒、Fanconi 腎小管症候群、慢性 B 型／C 型肝炎、長 QT 症候群、癲癇等。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一直接證據是一篇組合療法的獸醫前臨床研究（L4），無法歸因於 emtricitabine 單一藥物；且貓並非人類適應症，高 TxGNN 分數缺乏臨床資料支持。
- SIV 相關的獼猴研究支持 emtricitabine 的機轉與 PrEP 轉譯模型價值，但並未開啟新的人類適應症，人類 HIV 適應症本已核准。

**若要推進需要：**
- 確認 FIV 研究中 emtricitabine 的單獨貢獻與結果全文
- 建立貓的藥動學、劑量與安全性資料
- 補充 emtricitabine 的作用機轉資料
- 取得香港仿單的警語與禁忌症資料，並補齊各許可證的核准適應症
- 明確釐清此預測的目標（獸醫用途或僅作為研究模型），再決定是否投入資源

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Emtriva (emtricitabine) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=d6599395-3944-44f9-97f2-e0424c6b6a1f) |
| 2026-11-24 | 「另有 10 張單方許可證（含多家學名藥與 ODEFSEY 等），皆為有效狀態。」→「另有其他許可證（含多家學名藥與 ODEFSEY 等）；含本藥」 | 更正 | [衞生署藥物辦公室：藥劑製品註冊名單（DrugList.xml，data.gov.hk；證據包 Release data-20261123-235245）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

