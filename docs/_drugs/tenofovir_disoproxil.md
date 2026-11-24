---
layout: default
title: Tenofovir Disoproxil
parent: 僅模型預測 (L5)
nav_order: 859
evidence_level: L5
indication_count: 4
monitor_inn: "TENOFOVIR DISOPROXIL"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-11-24
description: "Tenofovir Disoproxil：預測新適應症為貓後天免疫缺乏症候群（證據等級 L5）。原適應症：慢性 B 型肝炎、HIV 感染、愛滋病"
---

# Tenofovir Disoproxil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Tenofovir Disoproxil：從慢性 B 型肝炎與 HIV 到貓後天免疫缺乏症候群
{: .text-alpha }

## 一句話總結

Tenofovir Disoproxil 是核苷酸類逆轉錄酶抑制劑，知識圖譜中記錄的原使用方向為慢性 B 型肝炎、HIV 感染與愛滋病。
TxGNN 模型預測排名第一的新適應症為**貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome)**，屬獸醫領域疾病。
目前**無臨床試驗**，僅有 **1 篇**直接相關的獸醫研究文獻，且該研究為複方抗病毒治療，不能單獨歸因於本藥，證據有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 B 型肝炎、HIV 感染、愛滋病（為知識圖譜中記錄的關聯，非香港許可證文字；已整理的許可證未載明適應症文字） |
| 預測新適應症 | 貓後天免疫缺乏症候群 |
| TxGNN 預測分數 | 0.9995 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 26 張／共 26 張） |
| 許可證數 | 26 張（有效 26 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Tenofovir Disoproxil 處方資料（Prescribing Information）「Mechanism of Action」與「Microbiology」段（非官方翻譯）：「Tenofovir disoproxil fumarate 為一種抗病毒藥物。[…] Tenofovir disoproxil fumarate 為腺苷單磷酸之非環狀核苷膦酸二酯類似物。Tenofovir disoproxil fumarate 須先經二酯水解轉化為 tenofovir，再經細胞酵素進行後續磷酸化，形成 tenofovir diphosphate（TFV-DP），即一種必然性鏈終止劑。」英文原文："Tenofovir disoproxil fumarate is an antiviral drug. […] Tenofovir disoproxil fumarate is an acyclic nucleoside phosphonate diester analog of adenosine monophosphate. Tenofovir disoproxil fumarate requires initial diester hydrolysis for conversion to tenofovir and subsequent phosphorylations by cellular enzymes to form tenofovir diphosphate (TFV-DP), an obligate chain terminator."（[DailyMed: Viread (tenofovir disoproxil fumarate) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=33fd6418-fbdc-42ca-a50d-ce2a476a5418)，版本日期 2025-02-18；查閱日期 2026-11-19）。根據已知資訊，Tenofovir 屬於核苷酸類逆轉錄酶抑制劑，可抑制病毒逆轉錄酶。

貓免疫缺乏病毒 (FIV) 是慢病毒，其逆轉錄酶與 HIV 相近，因此在機轉上有一定合理性。FIV 在貓身上造成的免疫功能進行性受損，也與 HIV 在人類身上的表現相似。

不過，這是獸醫適應症，與人類藥物再利用的關聯有限。所提供的唯一文獻是 Dolutegravir、Tenofovir、Emtricitabine 的複方治療研究，無法證明 Tenofovir 單獨有效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | 前臨床／獸醫研究 | Viruses | 在感染 FIV 的家貓中評估複方抗反轉錄病毒療法（Dolutegravir、Tenofovir、Emtricitabine）的藥物動力學與臨床結果；研究設計尚未確認 |

**評級說明：** 此文獻直接研究貓免疫缺乏病毒感染，但屬複方治療的前臨床／獸醫研究，且設計未確認，故證據等級以 L5 保守判定。

**其他預測方向（僅供參考）：**
- **猿猴免疫缺乏病毒感染**（排名第 2，分數 0.9995）：有多篇獼猴 SIV/SHIV 暴露前預防研究，顯示 TDF 單用或與 Emtricitabine 併用可提供部分保護，但這些屬動物資料，支持的是原有 HIV 方向，並非新的人類適應症。
- **伴隨共濟失調步態、無語言與皮質白質減少的神經發展障礙**（分數 0.9995）與**已過時的家族性複合型高脂血症**（分數 0.9960）：無臨床試驗、無文獻，亦無已知機轉關聯，僅為模型計算結果；後者的疾病術語已被本體論標為過時，不宜視為可行動的適應症。

## 香港上市資訊

香港含本藥成分的許可證包括單一成分與複方製劑，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表。許可證資料未載明核准適應症與劑型。以下列出 5 張主要許可證：

<!-- review:begin hk-lic-20261117-tenofovir_disoproxil-1 -->

> **查核更正（2026-11-24）**：原文為「已整理的許可證共 20 張，皆為單一成分、有效狀態，實際總數至少 20 張，清單可能不完整。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊；含本藥成分的許可證包括單一成分與複方製劑，張數見本頁快速總覽與許可證表（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-tenofovir_disoproxil-1 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-56075 | VIREAD TAB 300MG | 單一成分 | GILEAD SCIENCES HONG KONG LIMITED | 有效 |
| HK-57750 | VIREAD TAB 300MG (IRELAND) | 單一成分 | GILEAD SCIENCES HONG KONG LIMITED | 有效 |
| HK-65885 | TENOFOVIR SANDOZ TABLETS 300MG | 單一成分 | SANDOZ HONG KONG LIMITED | 有效 |
| HK-65259 | TENOFOVIR DISOPROXIL FUMARATE TABLETS 300MG | 單一成分 | VIATRIS HEALTHCARE HONG KONG LIMITED | 有效 |
| HK-64889 | TENOFOVIR DISOPROXIL FUMARATE TABLETS 300MG | 單一成分 | SINO PACIFIC PHARMA COMPANY LIMITED | 有效 |

上表列出其中 5 張（共 26 張）。

<!-- licenses:end -->

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜的藥物－疾病關係，並非仿單文字）：肝衰竭、肝病、腎臟疾病、Fanconi 腎小管症候群、乳酸中毒、低磷血症、骨軟化症、佝僂病、脂肪肝、非酒精性脂肪肝炎、C 型肝炎病毒感染、長 QT 症候群、尖端扭轉型心律不整、癲癇、焦慮症、精神分裂症等。實際用藥限制須以原廠仿單為準。
- **藥物交互作用**：資料庫查詢未找到相關紀錄。

其餘警語與禁忌資料缺乏，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測為獸醫適應症，僅有 1 篇複方治療的前臨床／獸醫文獻，無臨床試驗，且無法歸因於 Tenofovir 單獨作用，證據等級為 L5。
- 其餘預測（SIV 感染等）屬動物模型資料，只支持既有 HIV 方向，並未提供新的人類適應症，也無再利用機會。

**若要推進需要：**
- 補充作用機轉（MOA）資料
- 取得香港衛生署仿單的警語、禁忌與適應症文字
- 若要探討貓 FIV 方向，需要 Tenofovir 單藥的對照研究，並確認獸醫用藥的法規途徑
- 若要尋找人類新適應症，需另行評估其他具有人類疾病證據的預測項目

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「已整理的許可證共 20 張，皆為單一成分、有效狀態，實際總數至少 20 張，清單」→「香港含本藥成分的許可證包括單一成分與複方製劑，張數（含有效、」 | 更正（2026-11-24 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Viread (tenofovir disoproxil fumarate) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=33fd6418-fbdc-42ca-a50d-ce2a476a5418) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

