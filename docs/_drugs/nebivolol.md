---
layout: default
title: Nebivolol
parent: 僅模型預測 (L5)
nav_order: 611
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "NEBIVOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome"]
description: "Nebivolol：預測新適應症為Malignant hypertensive renal disease（證據等級 L5）。香港藥劑製品註冊：5 張（有效 5 張）"
---

# Nebivolol
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

## Nebivolol: Malignant hypertensive renal disease
{: .text-alpha }

## 一句話總結

Nebivolol 是一種 β1 選擇性阻斷劑，原本用於治療高血壓。
但目前**沒有相關臨床試驗**，也**沒有直接針對此適應症的文獻**，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Malignant hypertensive renal disease |
| TxGNN 預測分數 | 0.9942 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Nebivolol 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「BYSTOLIC 產生降血壓反應的作用機轉尚未確立。可能涉及的因素包括：心率降低、心肌收縮力降低、由大腦血管運動中樞傳至周邊的緊張性交感神經輸出減少、腎素活性受抑制，以及血管擴張和周邊血管阻力降低。」英文原文："The mechanism of action of the antihypertensive response of BYSTOLIC has not been definitively established. Possible factors that may be involved include: decreased heart rate, decreased myocardial contractility, diminution of tonic sympathetic outflow to the periphery from cerebral vasomotor centers, suppression of renin activity and vasodilation and decreased peripheral vascular resistance."（[DailyMed: Bystolic (nebivolol hydrochloride) prescribing information, Allergan, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8)，版本日期 2024-08-01；查閱日期 2026-11-19）。根據已知資訊，Nebivolol 是 β1 選擇性阻斷劑，並可透過一氧化氮 (NO) 介導產生血管擴張，其降血壓療效在一般高血壓中已被證實，機轉上可能與高血壓相關疾病有關聯。

不過，惡性腎血管性高血壓主要由腎動脈狹窄引起腎素－血管收縮素系統活化所驅動，是一種獨特且屬緊急狀況的疾病，與一般高血壓的病理機轉並不相同。因此，0.994 的高分僅是模型預測，不能直接視為療效證據。

同一批預測中，還包括惡性高血壓性腎病（排名 2，分數 0.9942）、肺動脈高壓（排名 3、4，分數 0.9939）及 Braddock 症候群（排名 5，分數 0.9914）。這些預測目前同樣缺乏直接的臨床證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無針對惡性腎血管性高血壓的相關文獻。

作為參考，排名 4 的預測（肺高壓，與缺氧或肺病相關）有少量間接文獻，多為前臨床研究或其他疾病情境，不能直接支持本適應症：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23506636](https://pubmed.ncbi.nlm.nih.gov/23506636/) | 2013 | 臨床比較試驗 | Int J Cardiol | 比較 carvedilol、nebivolol、bisoprolol 在中度心衰竭的多參數表現 |
| [21045724](https://pubmed.ncbi.nlm.nih.gov/21045724/) | 2011 | 臨床研究 | J Hypertens | 比較選擇性與非選擇性 β 阻斷劑在高海拔低氧下的 24 小時血壓影響 |
| [19789971](https://pubmed.ncbi.nlm.nih.gov/19789971/) | 2009 | Review | Cardiovasc Drugs Ther | 探討 β 阻斷劑對心衰竭患者肺功能的影響 |
| [32128711](https://pubmed.ncbi.nlm.nih.gov/32128711/) | 2020 | 前臨床（動物） | Pharmacol Rep | Nebivolol 在大鼠急性腎損傷模型中具腎保護作用 |
| [36947849](https://pubmed.ncbi.nlm.nih.gov/36947849/) | 2023 | 前臨床（動物） | Can J Physiol Pharmacol | Nebivolol 經 AKT1/Hif-1α/eNOS 路徑減輕 methotrexate 引起的腎毒性 |

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-67318 | NEBIVOLOL STELLA TABLETS 5MG | 單一成分 | HONG KONG MEDICAL SUPPLIES LTD | 有效 |
| HK-68319 | NEBIVOLOL SANDOZ TABLETS 5MG | 單一成分 | SANDOZ HONG KONG LIMITED | 有效 |
| HK-65104 | NEBILET TABLETS 1.25MG | 單一成分 | A. MENARINI HONG KONG LIMITED | 有效 |
| HK-59922 | NEBILET TAB 5MG | 單一成分 | A. MENARINI HONG KONG LIMITED | 有效 |

上表列出其中 4 張（共 5 張）。

<!-- licenses:end -->

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜關聯，非仿單原文）：肝衰竭、肝病、膽囊疾病、糖尿病、糖尿病酮酸中毒、周邊血管疾病、間歇性跛行、周邊動脈疾病、低血糖、房室傳導阻滯、支氣管疾病、病態竇症候群、家族性病態竇症候群。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 中度：Epinephrine、Hydrocortisone、Hyoscyamine、Bupropion、Triamcinolone、Morphine、Atropine、Dexamethasone、Canagliflozin、Dapagliflozin、Chlorpropamide
  - 輕度：Acetylsalicylic acid、Magnesium oxide
- 肺高壓方面，β 阻斷劑可能降低心輸出量與右心室功能，使用上需特別謹慎。

詳細警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 5 個預測適應症皆僅有模型分數，證據等級為 L5（肺高壓一項有間接前臨床文獻，為 L4），且沒有任何臨床試驗。
- 惡性腎血管性高血壓病理機轉特殊且屬緊急狀況，與 Nebivolol 的已知作用不完全吻合。

**若要推進需要：**
- 補充 Nebivolol 的作用機轉資料（MOA）
- 取得香港衛生署仿單的警語與禁忌資料，並完成安全性篩選
- 針對惡性腎血管性高血壓進行系統性文獻回顧，尋找直接的臨床或病例證據
- 評估在腎素依賴性高血壓下，β 阻斷劑與現行標準治療的比較及風險
- 如有初步臨床訊號，再規劃小型探索性試驗

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Bystolic (nebivolol hydrochloride) prescribing information, Allergan, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=8b8ad213-1dc8-454e-a524-075685c0e1a8) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

