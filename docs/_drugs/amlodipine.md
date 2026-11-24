---
layout: default
title: Amlodipine
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 9
monitor_inn: "AMLODIPINE"
predicted_indications: ["brain stem infarction", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "cerebral artery occlusion", "Braddock syndrome", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
last_modified_at: 2026-11-24
description: "Amlodipine：預測新適應症為腦幹梗塞 (brain stem infarction)（證據等級 L5）。香港藥劑製品註冊：146 張（有效 141 張）"
---

# Amlodipine
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

## Amlodipine：鈣離子通道阻斷劑 → 腦幹梗塞 (brain stem infarction)
{: .text-alpha }

## 一句話總結

Amlodipine 是一種鈣離子通道阻斷劑，目前在香港已有多張單一成分許可證。
TxGNN 模型預測它可能對**腦幹梗塞 (brain stem infarction)** 有效，
但目前**沒有任何臨床試驗或文獻**直接研究這個疾病，證據僅來自模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 腦幹梗塞 (brain stem infarction) |
| TxGNN 預測分數 | 0.9994 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 141 張／共 146 張） |
| 許可證數 | 146 張（有效 141 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Amlodipine 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Amlodipine 為一種 dihydropyridine 類鈣拮抗劑（鈣離子拮抗劑或慢通道阻斷劑），可抑制鈣離子跨膜流入血管平滑肌及心肌。實驗數據顯示，amlodipine 可與 dihydropyridine 及非 dihydropyridine 結合位點結合。」英文原文："Amlodipine is a dihydropyridine calcium antagonist (calcium ion antagonist or slow-channel blocker) that inhibits the transmembrane influx of calcium ions into vascular smooth muscle and cardiac muscle. Experimental data suggest that amlodipine binds to both dihydropyridine and nondihydropyridine binding sites."（[DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487)，版本日期 2026-09-28；查閱日期 2026-11-19）。Amlodipine 屬於鈣離子通道阻斷劑，一般透過血管擴張與降低血壓發揮作用。

腦幹梗塞屬於缺血性腦血管疾病，而血壓控制是腦血管疾病預防的重要環節。模型給出的高分，可能反映的是 amlodipine 與腦血管相關疾病之間的網路關聯，而非針對腦幹梗塞本身的獨立證據。

需要注意的是，目前沒有針對腦幹梗塞的試驗或文獻，因此這項預測僅屬於假說層級，不能視為療效證明。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港含本藥成分的許可證包括單一成分與複方製劑，張數與有效張數見本頁快速總覽與「香港上市資訊」的許可證表。以下僅列出部分主要許可證，許可證記錄中未載明核准適應症文字。

<!-- review:begin hk-lic-20261117-amlodipine-1 -->

> **查核更正（2026-11-24）**：原文為「本地資料顯示 amlodipine 單一成分許可證目前均為有效狀態（有效 20 張、已註銷 0 張）。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊；含本藥成分的許可證包括單一成分與複方製劑，張數見本頁快速總覽與許可證表（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-amlodipine-1 -->

<!-- review:begin hk-lic-20261117-amlodipine-2 -->

> **查核更正（2026-11-24）**：原文為「以下僅列出部分主要許可證，清單可能並不完整；許可證記錄中未載明核准適應症文字。」。已更正：本頁資料原本只收錄部分註冊（最多 20 張），2026-11-17 依本站原本的收錄規則（成分對 DrugBank ID，單方、複方都收）對衞生署藥物辦公室註冊名單補齊本藥全部註冊；含本藥成分的許可證包括單一成分與複方製劑，張數見本頁快速總覽與許可證表（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)。

<!-- review:end hk-lic-20261117-amlodipine-2 -->

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-55770 | PMS-AMLODIPINE TAB 5MG | 單一成分 | TRENTON-BOMA LTD | 有效 |
| HK-65871 | AMLOCOR TABLETS 10MG | 單一成分 | HEALTHCARE PHARMASCIENCE LIMITED | 有效 |
| HK-56593 | AMLODIPINA FARMOZ TAB 5MG | 單一成分 | TRENTON-BOMA LTD | 有效 |
| HK-66898 | KARDAM 10 TABLETS 10MG | 單一成分 | AUROBINDO PHARMA LIMITED | 有效 |
| HK-63420 | AMDIVASC TABLETS 5MG | 單一成分 | EUROPHARM LAB CO LTD | 有效 |

上表列出其中 5 張（共 146 張）。

<!-- licenses:end -->

## 安全性考量

- **藥物交互作用**：本次彙整的資料顯示共有 100 筆交互作用記錄，其中列出的主要項目屬中度，包括皮質類固醇（hydrocortisone、betamethasone、budesonide、dexamethasone）、aprepitant、乙醯水楊酸（aspirin）、bupropion、clarithromycin、clotrimazole、canagliflozin、dapagliflozin，以及多種鈣製劑（如 calcium carbonate、calcium gluconate 等）。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 腦幹梗塞沒有任何直接相關的臨床試驗或文獻，證據等級為 L5，僅有模型預測。
- 高分可能反映的是 amlodipine 已知的血壓控制與腦血管相關作用，而非針對此疾病的新證據。

**若要推進需要：**
- 針對腦幹梗塞（或後循環缺血性中風）的臨床或觀察性研究
- 詳細的作用機轉資料（MOA）
- 取得香港仿單的警語與禁忌症資料，完成安全性篩選
- 釐清 amlodipine 相較於一般降壓治療在此族群的額外價值

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-24 | 「本地資料顯示 amlodipine 單一成分許可證目前均為有效狀態（有效 20 」→「香港含本藥成分的許可證包括單一成分與複方製劑，張數（含有效、」 | 更正（2026-11-24 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-24 | 「以下僅列出部分主要許可證，清單可能並不完整；許可證記錄中未載明核准適應症文字。」→「以下僅列出部分主要許可證，許可證記錄中未載明核准適應症文字。」 | 更正（2026-11-24 修訂，前版保留於紀錄） | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Sdamlo (amlodipine) prescribing information, Pangea Pharmaceuticals, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=886a7f97-60a4-4206-a6c7-5206069ed487) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

