---
layout: default
title: Amiloride
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 5
monitor_inn: "Amiloride"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-11-24
description: "Amiloride：預測新適應症為惡性高血壓性腎病 (malignant hypertensive renal disease)（證據等級 L5）。香港藥劑製品註冊：5 張（有效 5 張）"
---

# Amiloride
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

## Amiloride：鉀離子保留型利尿劑（ENaC 阻斷劑）→ 惡性高血壓性腎病 (malignant hypertensive renal disease)
{: .text-alpha }

## 一句話總結

Amiloride 是一種作用於遠端腎小管上皮鈉通道（ENaC）的鉀離子保留型利尿劑。
TxGNN 模型預測它可能對**惡性高血壓性腎病 (malignant hypertensive renal disease)** 有效，
但目前**沒有臨床試驗，也沒有直接研究此疾病的文獻**，僅有模型預測支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 惡性高血壓性腎病 (malignant hypertensive renal disease) |
| TxGNN 預測分數 | 0.9982 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Amiloride 處方資料（Prescribing Information）「Clinical Pharmacology」段（非官方翻譯）：「Amiloride HCl為一種保鉀（抗排鉀）藥物，具有弱效（與thiazide類利尿劑相比）的排鈉、利尿及降血壓活性。在部分臨床研究中，這些作用與thiazide類利尿劑的作用具有部分加成效果。」英文原文："Amiloride HCl is a potassium-conserving (antikaliuretic) drug that possesses weak (compared with thiazide diuretics) natriuretic, diuretic, and antihypertensive activity. These effects have been partially additive to the effects of thiazide diuretics in some clinical studies."（[DailyMed: amiloride hydrochloride prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5eedadbd-9be9-b920-e063-6394a90afa68)，版本日期 2026-11-11；查閱日期 2026-11-19）。根據已知藥理，Amiloride 阻斷遠端腎小管的上皮鈉通道（ENaC），減少鈉再吸收並降低血壓。

高血壓與高血壓性腎病在病理上相關，因此機轉上有生物學合理性。但此預測目前只來自模型分數，缺乏任何試驗或文獻佐證。此外，本藥既有的降壓用途與此預測高度重疊，較像是既有用途的延伸，而非獨立的再利用訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-25543 | AMILORIDE TAB 5MG | 單一成分 | JEAN-MARIE PHARMACAL CO LTD | 有效 |
| HK-25544 | AMITHIAZIDE TAB | 複方 | JEAN-MARIE PHARMACAL CO LTD | 有效 |
| HK-42186 | APO-AMILZIDE TAB 50/5MG | 複方 | HIND WING CO LTD | 有效 |
| HK-50535 | POLI-URETIC TAB | 複方 | NATURAL HEALTH RESOURCES COMPANY LIMITED | 有效 |
| HK-58537 | BILDURETIC TAB | 複方 | TRENTON-BOMA LTD | 有效 |

<!-- licenses:end -->

## 安全性考量

- **藥物交互作用**：本次彙整的資料顯示共 100 筆交互作用紀錄，其中列出的多為中度或輕度。中度者包括：
  - 皮質類固醇（Hydrocortisone、Betamethasone、Budesonide、Dexamethasone）
  - Metformin
  - SGLT2 抑制劑（Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin）
  - Exenatide
  - Bupropion
  - 瀉劑類（Bisacodyl、Castor oil、Glycerin、Lactitol、Lactulose）
  - Dronabinol

  輕度者包括 Doxycycline、Amoxicillin、Cimetidine。
- 其他安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測分數雖高，但沒有任何臨床試驗或直接研究該疾病的文獻，證據等級僅為 L5。
- 預測與藥物既有的降壓用途重疊，難以視為獨立的再利用機會。

**若要推進需要：**
- 取得 Amiloride 在惡性高血壓性腎病的臨床或觀察性研究證據
- 補充完整的作用機轉資料
- 取得香港仿單的警語與禁忌症，並評估腎功能受損患者的高血鉀風險
- 確認各許可證的核准適應症與劑型

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: amiloride hydrochloride prescribing information, Kesin Pharma Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5eedadbd-9be9-b920-e063-6394a90afa68) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

