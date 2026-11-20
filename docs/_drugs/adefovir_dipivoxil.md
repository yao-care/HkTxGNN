---
layout: default
title: Adefovir Dipivoxil
parent: 僅模型預測 (L5)
nav_order: 26
evidence_level: L5
indication_count: 9
monitor_inn: "ADEFOVIR DIPIVOXIL"
predicted_indications: ["chronic hepatitis C virus infection", "HIV infectious disease", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "hepatitis C virus infection", "hepatitis E virus infection", "hepatitis, viral, animal", "hepatitis A virus infection"]
last_modified_at: 2026-11-20
description: "Adefovir Dipivoxil：預測新適應症為慢性C型肝炎病毒感染 (chronic hepatitis C virus infection)（證據等級 L5）。香港藥劑製品註冊：2 張（有效 2 張）"
---

# Adefovir Dipivoxil
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

## Adefovir Dipivoxil：核苷酸類逆轉錄酶抑制劑 → 慢性C型肝炎病毒感染 (chronic hepatitis C virus infection)
{: .text-alpha }

## 一句話總結

Adefovir Dipivoxil 是一種口服核苷酸類（nucleotide analogue）抗病毒藥物，主要抑制病毒 DNA 聚合酶／逆轉錄酶。
TxGNN 模型預測它可能對**慢性C型肝炎病毒感染 (chronic hepatitis C virus infection)** 有效，
但目前**沒有直接研究此疾病的臨床試驗或文獻**，現有資料僅為一般病毒性肝炎的綜述，證據相當薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 慢性C型肝炎病毒感染 (chronic hepatitis C virus infection) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Adefovir Dipivoxil 處方資料（Prescribing Information）「Mechanism of Action」與「Microbiology」段（非官方翻譯）：「Adefovir 為一種抗病毒藥物。[…] Adefovir 為單磷酸腺苷的非環狀核苷酸類似物，可經細胞激酶磷酸化為活性代謝物 adefovir diphosphate。Adefovir diphosphate 藉由與天然受質去氧腺苷三磷酸競爭，以及在嵌入病毒 DNA 後造成 DNA 鏈終止，而抑制 HBV DNA 聚合酶（反轉錄酶）。」英文原文："Adefovir is an antiviral drug. […] Adefovir is an acyclic nucleotide analog of adenosine monophosphate which is phosphorylated to the active metabolite adefovir diphosphate by cellular kinases. Adefovir diphosphate inhibits HBV DNA polymerase (reverse transcriptase) by competing with the natural substrate deoxyadenosine triphosphate and by causing DNA chain termination after its incorporation into viral DNA."（[DailyMed: adefovir dipivoxil prescribing information, Apotex Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=08e07fae-3191-b6a3-c894-d3a8cc53923f)，版本日期 2025-07-22；查閱日期 2026-11-19）。依一般藥理知識，Adefovir 是核苷酸類似物，其活性代謝物抑制 B 型肝炎病毒（HBV）的 DNA 聚合酶／逆轉錄酶。

C 型肝炎病毒（HCV）是 RNA 病毒，依賴 NS5B RNA 依賴性 RNA 聚合酶複製，與 Adefovir 的作用標的不同，因此機轉上沒有明確的活性依據。

TxGNN 的高分較可能反映模型中與 B 型肝炎在特徵上的相近，而非對 C 型肝炎的實際療效。現有文獻多為涵蓋 B 型與 C 型肝炎治療的綜述，沒有任何一篇提供 Adefovir 對 C 型肝炎的專屬療效資料，因此證據等級定為 L5。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下為資料中與此預測相關度最高的文獻，皆為一般病毒性肝炎的綜述或指引，並未直接研究 Adefovir 對 C 型肝炎的療效：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18221137](https://pubmed.ncbi.nlm.nih.gov/18221137/) | 2006 | Review | Recent Patents on Anti-infective Drug Discovery | 長效干擾素用於慢性 B 型肝炎，並列出 Adefovir 為已核准藥物之一 |
| [15588803](https://pubmed.ncbi.nlm.nih.gov/15588803/) | 2004 | Review | Best Pract Res Clin Gastroenterol | 慢性病毒性肝炎治療策略，Adefovir 屬 B 型肝炎核苷類藥物 |
| [16699274](https://pubmed.ncbi.nlm.nih.gov/16699274/) | 2006 | Review | Digestive Diseases | B 型與 C 型肝炎的既有及新興療法 |
| [25027705](https://pubmed.ncbi.nlm.nih.gov/25027705/) | 2014 | Review | Minerva Gastroenterol Dietol | B、C 型肝炎抗病毒藥物及其對腎功能的影響 |
| [22370225](https://pubmed.ncbi.nlm.nih.gov/22370225/) | 2012 | Guideline | Orvosi Hetilap | 匈牙利 B、C、D 型肝炎診療共識指引 |
| [16107195](https://pubmed.ncbi.nlm.nih.gov/16107195/) | 2005 | Review | Expert Rev Anti Infect Ther | Peginterferon-alpha2a 用於 B 型肝炎 |
| [15918324](https://pubmed.ncbi.nlm.nih.gov/15918324/) | 2004 | Review | Lijecnicki Vjesnik | 病毒性肝炎的治療與預防 |
| [19149648](https://pubmed.ncbi.nlm.nih.gov/19149648/) | 2009 | Review | Medicinal Chemistry | Bicyclol 用於慢性 B、C 型肝炎，與 Adefovir 無直接關聯 |
| [24797262](https://pubmed.ncbi.nlm.nih.gov/24797262/) | 2014 | Cohort | Viral Immunology | 停用抗病毒治療後 HBeAg 血清轉換相關細胞激素（B 型肝炎） |
| [31572002](https://pubmed.ncbi.nlm.nih.gov/31572002/) | 2019 | Cohort | Cancer Management and Research | 核苷（酸）類似物對 HBV 相關小肝癌存活的影響 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63344 | HEPTOVANCE TABLET 10MG | 未記載 | 未記載 |
| HK-64175 | APO-ADEFOVIR TABLETS 10MG | 未記載 | 未記載 |

本地資料中兩張許可證皆為單一成分製劑，目前均為有效狀態。

## 安全性考量

- **藥物交互作用**：資料中共記錄 25 筆交互作用，其中列出的包括 Pantoprazole、Morphine、Omeprazole、Lansoprazole、Lactulose、Potassium chloride、Prednisolone、Ranitidine、Famotidine、Warfarin、Heparin、Ibuprofen 等，風險等級均未分類。
- **腎毒性**：文獻指出 Adefovir 在較高劑量用於 HIV 時，腎毒性為劑量限制性副作用；長期使用時亦有研究探討腎功能異常的監測（PMID 27858892）。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
沒有任何臨床試驗或文獻直接研究 Adefovir 對慢性 C 型肝炎的效果。HCV 為 RNA 病毒，與 Adefovir 的作用標的在機轉上缺乏明確關聯，高預測分數很可能只是模型的相近性假象。因此證據等級僅為 L5。

**若要推進需要：**
- 體外 HCV 複製子（replicon）試驗，確認是否有任何抗 HCV 活性
- 作用機轉的明確依據，說明為何一個 DNA 聚合酶／逆轉錄酶抑制劑可能影響 HCV
- 與現有直接作用抗病毒藥物（DAA）的比較，評估臨床上是否有必要
- 腎功能監測與安全性計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: adefovir dipivoxil prescribing information, Apotex Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=08e07fae-3191-b6a3-c894-d3a8cc53923f) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

