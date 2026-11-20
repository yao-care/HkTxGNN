---
layout: default
title: Bisoprolol
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 4
monitor_inn: "Bisoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
last_modified_at: 2026-11-20
description: "Bisoprolol：預測新適應症為惡性高血壓性腎病 (malignant hypertensive renal disease)（證據等級 L5）。香港藥劑製品註冊：18 張（有效 18 張）"
---

# Bisoprolol
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

## Bisoprolol：β1 選擇性阻斷劑 → 惡性高血壓性腎病 (malignant hypertensive renal disease)
{: .text-alpha }

## 一句話總結

Bisoprolol 是一種 β1 選擇性阻斷劑，在香港已有多張單方許可證並在市場上流通。
TxGNN 模型預測它可能對**惡性高血壓性腎病 (malignant hypertensive renal disease)** 有效。
目前**沒有任何臨床試驗或文獻**直接支持此預測，僅屬模型層級的假設。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 惡性高血壓性腎病 (malignant hypertensive renal disease) |
| TxGNN 預測分數 | 0.9994 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 18 張／共 18 張） |
| 許可證數 | 18 張（有效 18 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Bisoprolol 處方資料（Prescribing Information）「Clinical Pharmacology」段（非官方翻譯）：「BISOPROLOL FUMARATE 是一種 beta 1 選擇性（心臟選擇性）腎上腺素受體阻斷劑，在其治療劑量範圍內不具顯著的膜穩定活性或內在擬交感神經活性。然而，心臟選擇性並非絕對，在較高劑量（≥ 20 mg）時，bisoprolol fumarate 亦會抑制主要位於支氣管及血管肌肉組織中的 beta 2 腎上腺素受體；因此，為維持選擇性，使用最低有效劑量十分重要。」英文原文："BISOPROLOL FUMARATE is a beta 1 -selective (cardioselective) adrenoceptor blocking agent without significant membrane stabilizing activity or intrinsic sympathomimetic activity in its therapeutic dosage range. Cardioselectivity is not absolute, however, and at higher doses (≥ 20 mg) bisoprolol fumarate also inhibits beta 2 -adrenoceptors, chiefly located in the bronchial and vascular musculature; to retain selectivity it is therefore important to use the lowest effective dose."（[DailyMed: bisoprolol fumarate prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6517d564-ea55-4084-a8ab-34fea548c24e)，版本日期 2026-11-11；查閱日期 2026-11-19）。Bisoprolol 屬於 β1 選擇性阻斷劑，可降低心率、心輸出量並減少腎素釋放，進而降低血壓。

惡性高血壓性腎病是血壓長期未獲控制所引發的嚴重併發症，因此在「降低血壓、減少腎素釋放」這一點上，機轉上存在合理的關聯。

不過需要保留的是：惡性高血壓通常需要快速的靜脈降壓處置，口服 β 阻斷劑並非標準第一線治療。模型分數很高，但可能主要反映疾病名稱與高血壓的相似性，而非實際療效證據。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63998 | BISO TABLETS 5MG | 未記載 | 未記載 |
| HK-67481 | BISOCORD 5 TABLETS 5MG | 未記載 | 未記載 |
| HK-68824 | JECEBISO TABLETS 2.5MG | 未記載 | 未記載 |
| HK-60688 | APO-BISOPROLOL TAB 10MG | 未記載 | 未記載 |
| HK-29917 | CONCOR 5 FILM-COATED TAB 5MG | 未記載 | 未記載 |

## 安全性考量

- **藥物交互作用**：本報告彙整的資料顯示共有 100 筆交互作用紀錄，以下為部分中度交互作用的藥物：
  - Epinephrine
  - Hydrocortisone
  - Bupropion
  - Morphine
  - Atropine
  - Dexamethasone
  - 多種鈣鹽（如 Calcium carbonate、Calcium gluconate）

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有模型預測，沒有任何直接針對惡性高血壓性腎病的臨床試驗或文獻，證據等級為 L5。
- 惡性高血壓通常需要靜脈快速降壓，口服 bisoprolol 並非標準處置，高分數可能來自與高血壓的名稱相似性。

**若要推進需要：**
- 補齊 bisoprolol 的作用機轉資料
- 取得香港衛生署仿單的警語與禁忌症
- 進行針對惡性高血壓性腎病的文獻回顧，並評估是否有可行的臨床研究設計
- 由臨床專家審視此預測是否具實際治療意義

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: bisoprolol fumarate prescribing information, ANI Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=6517d564-ea55-4084-a8ab-34fea548c24e) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

