---
layout: default
title: Acetazolamide
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
monitor_inn: "ACETAZOLAMIDE"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "unclassified intestinal pseudoobstruction"]
last_modified_at: 2026-10-28
description: "Acetazolamide：預測新適應症為運動誘發惡性高熱 (exercise-induced malignant hyperthermia)（證據等級 L5）。香港藥劑製品註冊：3 張（有效 3 張）"
---

# Acetazolamide
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

## Acetazolamide：碳酸酐酶抑制劑 → 運動誘發惡性高熱 (exercise-induced malignant hyperthermia)
{: .text-alpha }

## 一句話總結

Acetazolamide 是一種碳酸酐酶抑制劑，在香港已有單一成分製劑上市。
TxGNN 模型預測它可能對**運動誘發惡性高熱 (exercise-induced malignant hyperthermia)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 運動誘發惡性高熱 (exercise-induced malignant hyperthermia) |
| TxGNN 預測分數 | 0.9995 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Acetazolamide 處方資料（Prescribing Information）「Clinical Pharmacology」段（非官方翻譯）：「Acetazolamide為一種強效碳酸酐酶抑制劑，可有效控制液體分泌（例如某些類型的青光眼）、治療某些痙攣性疾病（例如癲癇），以及在異常液體滯留的情況下（例如心因性水腫）促進利尿。Acetazolamide並非汞類利尿劑。」英文原文："Acetazolamide is a potent carbonic anhydrase inhibitor, effective in the control of fluid secretion (e.g., some types of glaucoma), in the treatment of certain convulsive disorders (e.g., epilepsy), and in the promotion of diuresis in instances of abnormal fluid retention (e.g., cardiac edema). Acetazolamide is not a mercurial diuretic."（[DailyMed: acetazolamide prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8e48a25-5f6c-4b5a-a5f2-ee87aabea33b)，版本日期 2026-11-10；查閱日期 2026-11-19）。Acetazolamide 屬於碳酸酐酶抑制劑，一般認為其作用是改變體內酸鹼平衡。

從機轉推測，酸鹼平衡改變可能影響肌肉的興奮—收縮偶聯，這是此預測唯一可想像的連結。但這純屬推測，沒有資料支持。惡性高熱的核心機制是 ryanodine 受體功能異常與鈣離子調節失衡，而 ryanodine 受體並非 acetazolamide 已知的作用標的。

因此，0.9995 的高分只代表模型預測，不等同於有實際的療效依據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50001 | ACETAZOLAMIDE 250 TAB 250MG (REMEDICA) | 未記載 | 未記載 |
| HK-36263 | APO-ACETAZOLAMIDE TAB 250MG | 未記載 | 未記載 |
| HK-16895 | ACETAZOLAMIDE TAB 250MG (WHITE) | 未記載 | 未記載 |

三張許可證均為單一成分製劑，狀態皆為有效。

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為部分重點：
  - 嚴重（Major）：乙醯水楊酸（Acetylsalicylic acid，即阿斯匹靈）、Cisapride
  - 中度（Moderate）：多種降血糖藥（如 Acarbose、Chlorpropamide、Canagliflozin、Dapagliflozin、Alogliptin、Dulaglutide）、Amphotericin B 各劑型、皮質類固醇（如 Dexamethasone、Betamethasone、Beclomethasone dipropionate）、Bisacodyl、Castor oil
  - 輕微（Minor）：Doxycycline
- **與預測相關的安全訊號**：本藥可能造成腸道麻痺性腸阻塞（adynamic ileus）的個案報告，以及在肝硬化患者中可能因尿液鹼化、氨排出減少而誘發高血氨與腦病變。若未來考慮心肌病變或腸道相關方向，需特別留意。

完整警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 對於主要預測的運動誘發惡性高熱，沒有任何臨床試驗或文獻，機轉上也缺乏合理連結，證據等級為 L5。
- 目前不建議投入進一步開發資源，除非能先建立機轉層面的支持。

**若要推進需要：**
- 釐清碳酸酐酶抑制與 ryanodine 受體、鈣離子調節之間是否存在可驗證的機轉連結
- 進行系統性文獻檢索與前臨床（細胞或動物模型）驗證
- 取得完整的作用機轉資料與香港仿單的警語及禁忌症
- 評估運動、高熱狀態下使用本藥（可能造成脫水與電解質失衡）的安全性

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: acetazolamide prescribing information, Chartwell RX, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e8e48a25-5f6c-4b5a-a5f2-ee87aabea33b) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

