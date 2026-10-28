---
layout: default
title: Aztreonam
parent: 僅模型預測 (L5)
nav_order: 92
evidence_level: L5
indication_count: 10
monitor_inn: "AZTREONAM"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "Ureaplasma urethritis", "gonococcal urethritis", "blood group incompatibility", "premalignant hematological system disease", "epiglottitis", "monoclonal gammopathy", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-10-23
description: "Aztreonam：預測新適應症為高澱粉酶血症 (hyperamylasemia)（證據等級 L5）。原適應症：香港許可證未載明適應症文字"
---

# Aztreonam
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

## Aztreonam：從尿路感染等革蘭氏陰性菌感染到高澱粉酶血症
{: .text-alpha }

## 一句話總結

Aztreonam 是單環 β-內醯胺（monobactam）類抗生素，知識圖譜中記錄它與尿路感染、綠膿桿菌感染、腹膜炎、大腸桿菌感染等感染性疾病有關。
TxGNN 模型（深度學習）預測它可能對**高澱粉酶血症 (hyperamylasemia)** 有效，但目前**沒有任何臨床試驗或文獻**支持，機轉上也不合理；這個分數可能只反映模型學到的相關疾病之間的相似性，並非生物學證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症文字；知識圖譜記錄的相關疾病為尿路感染、綠膿桿菌感染、腹膜炎、鼻硬結症、大腸桿菌感染、子宮內膜炎（僅為知識圖譜關聯，非核准適應症） |
| 預測新適應症 | 高澱粉酶血症 (hyperamylasemia) |
| TxGNN 預測分數 | 0.9973 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知資訊，Aztreonam 是單環 β-內醯胺類抗生素，作用方式是結合細菌的 PBP-3 而抑制細胞壁合成，只對需氧的革蘭氏陰性菌有效。

高澱粉酶血症是血液生化指標的異常，不是感染性疾病。抗菌藥物對它沒有已知的直接作用，兩者之間找不到合理的機轉連結。

TxGNN 分數雖然很高（0.9973），但這個分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據，沒有任何臨床或文獻佐證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68891 | EMBLAVEO POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 1.5G/0.5G（輝瑞） | 未載明 | 未載明 |

說明：
- 本報告所用資料只有 1 張許可證，狀態為有效。
- 該產品的規格（1.5G/0.5G）顯示它可能含兩種成分，因此不能用這張許可證來描述 Aztreonam 單一成分的核准或上市情形。
- 許可證資料未提供適應症文字，所以無法由此確認任何已核准用途。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜，不是仿單內容）：腎臟疾病、輸尿管積膿、肝臟疾病、膽囊疾病、困難梭狀芽孢桿菌結腸炎、新生兒壞死性腸炎、支氣管疾病。實際禁忌症請以原廠仿單為準。
- **藥物交互作用**：共查到 27 筆，以下為資料中列出的主要項目。
  - 中度：Picosulfuric acid、Dicoumarol、Warfarin。使用抗凝血劑時，建議留意凝血功能。
  - 嚴重度未分級：Pantoprazole、Omeprazole、Lansoprazole、Morphine、Vancomycin、Hydrocortisone、Dexamethasone、Ondansetron、Metronidazole、Amphotericin B、Acetylsalicylic acid、Heparin、Salbutamol、Fluconazole、Tacrolimus、Amikacin、Acyclovir 等。

其餘安全性資訊（警語、官方禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 高澱粉酶血症沒有任何臨床試驗或文獻，機轉上也不合理，證據等級僅為 L5。
- 同批預測中，有些候選疾病有間接證據，例如淋病性尿道炎有 1980 年代的單劑治療研究和 2020 年的單臂試驗。這類屬於可再研究的問題，而不是本項預測的證據。

**若要推進需要：**
- 確認這項預測是否只是模型從相關疾病學到的相似性，而非生物學證據；若有生物學上的合理假說，需先提出明確的機轉依據。
- 取得原廠仿單，確認警語、禁忌症與核准適應症，並釐清 HK-68891 是單方還是複方。
- 若要評估其他預測，優先考慮有間接文獻的感染性疾病（如淋病性尿道炎），並注意其抗藥性報告與現行治療指引。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

