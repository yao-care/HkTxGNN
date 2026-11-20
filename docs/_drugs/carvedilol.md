---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 4
monitor_inn: "CARVEDILOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
last_modified_at: 2026-11-20
description: "Carvedilol：預測新適應症為惡性高血壓腎病變 (malignant hypertensive renal disease)（證據等級 L5）。香港藥劑製品註冊：22 張（有效 22 張）"
---

# Carvedilol
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

## Carvedilol：非選擇性 β 阻斷劑兼 α1 阻斷劑 → 惡性高血壓腎病變 (malignant hypertensive renal disease)
{: .text-alpha }

## 一句話總結

Carvedilol 是兼具 β1/β2 與 α1 受體阻斷作用的心血管用藥。
TxGNN 模型預測它可能與 **惡性高血壓腎病變 (malignant hypertensive renal disease)** 相關，預測分數為 0.9955。
目前沒有針對此疾病的臨床試驗或文獻，證據僅停留在模型預測層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 惡性高血壓腎病變 (malignant hypertensive renal disease) |
| TxGNN 預測分數 | 0.9955 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 22 張／共 22 張） |
| 許可證數 | 22 張（有效 22 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Carvedilol 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「COREG 是一種外消旋混合物，其中非選擇性 β-腎上腺素受體阻斷活性存在於 S(-) 鏡像異構物，而 α1-腎上腺素阻斷活性則以相同效力存在於 R(+) 及 S(-) 兩種鏡像異構物。COREG 不具內在擬交感神經活性。」英文原文："COREG is a racemic mixture in which nonselective β-adrenoreceptor blocking activity is present in the S(-) enantiomer and α1-adrenergic blocking activity is present in both R(+) and S(-) enantiomers at equal potency. COREG has no intrinsic sympathomimetic activity."（[DailyMed: Coreg (carvedilol) prescribing information, Waylis Therapeutics LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=07c619c6-4a0c-445e-94fa-664a54f68a39)，版本日期 2026-07-31；查閱日期 2026-11-19）。依現有資訊，Carvedilol 同時阻斷 β1、β2 與 α1 腎上腺素受體，能降低血管阻力與交感神經張力。從機轉上看，這種降壓作用與高血壓造成腎臟損傷時的血壓控制有關。

這項預測較可能反映疾病在醫學本體分類上與高血壓相近，而非獨立的實證。另外，惡性高血壓腎病變屬於合併器官損傷的高血壓急症，臨床上通常需要快速、可滴定的注射降壓處置。口服 Carvedilol 不會是第一線選擇。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 安全性考量

- **藥物交互作用**：本報告彙整的資料顯示共有 100 筆交互作用紀錄。
  - 重大等級：Epinephrine。
  - 中度等級（部分）：Hydrocortisone、Hyoscyamine、Bupropion、Triamcinolone、Morphine、Atropine、Dexamethasone、Canagliflozin、Acetohexamide。
  - 輕微等級（部分）：Acetylsalicylic acid、Aluminum hydroxide。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 對此疾病沒有任何臨床試驗或文獻，證據等級為 L5，僅有模型預測。
- 此疾病屬於高血壓急症，口服 Carvedilol 在臨床定位上不明確。

**若要推進需要：**
- 找出直接研究 Carvedilol 用於惡性高血壓腎病變或相關腎損傷的臨床或臨床前證據。
- 補齊詳細的作用機轉資料，以及香港仿單的警語與禁忌症。
- 評估此族群中口服 β/α 阻斷劑相對於現行標準處置的定位與安全性。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Coreg (carvedilol) prescribing information, Waylis Therapeutics LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=07c619c6-4a0c-445e-94fa-664a54f68a39) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

