---
layout: default
title: Cabotegravir
parent: 僅模型預測 (L5)
nav_order: 142
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Cabotegravir：預測新適應症為類風濕性關節炎 (Rheumatoid Arthritis)（證據等級 L5）。原適應症：香港許可證資料未載明核准適應症（依藥理分類，屬 HIV 整合酶抑制劑）"
monitor_inn: "CABOTEGRAVIR"
predicted_indications: ["rheumatoid arthritis", "sclerosing cholangitis", "bronchitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "severe nonproliferative diabetic retinopathy"]
---

# Cabotegravir
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

## Cabotegravir：從 HIV 感染到類風濕性關節炎
{: .text-alpha }

## 一句話總結

Cabotegravir 是一種 HIV 整合酶抑制劑（INSTI），在香港以 Vocabria 品牌上市，有口服錠劑與長效注射劑型。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效。
目前**沒有任何臨床試驗或文獻**支持，這僅是模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症（依藥理分類，屬 HIV 整合酶抑制劑） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 0.9945 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Cabotegravir 處方資料（Prescribing Information）「Mechanism of Action」與「Microbiology」段（非官方翻譯）：「Cabotegravir是一種HIV-1抗反轉錄病毒藥物。[…] Cabotegravir藉由與嵌合酶活性位點結合，並阻斷反轉錄病毒去氧核糖核酸（DNA）嵌合中的股轉移步驟，而抑制HIV嵌合酶；此步驟為HIV複製週期所必需。在使用純化重組HIV-1嵌合酶進行的股轉移分析中，cabotegravir的平均50%抑制濃度（IC 50）值為3.0 nM。」英文原文："Cabotegravir is an HIV-1 antiretroviral drug. […] Cabotegravir inhibits HIV integrase by binding to the integrase active site and blocking the strand transfer step of retroviral deoxyribonucleic acid (DNA) integration that is essential for the HIV replication cycle. The mean 50% inhibitory concentration (IC 50 ) value of cabotegravir in a strand transfer assay using purified recombinant HIV-1 integrase was 3.0 nM."（[DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3)，版本日期 2025-04-11；查閱日期 2026-11-19）。根據已知資訊，Cabotegravir 屬於 HIV 整合酶抑制劑，其作用是阻斷病毒 DNA 整合入宿主基因組。這個機轉與類風濕性關節炎的病理（TNF、IL-6、JAK/STAT、B/T 細胞訊號）沒有已知的直接關聯。

以目前資料，無法建立兩者之間合理的機轉連結。0.9945 的分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，不能視為生物學上的證據。

TxGNN 另外預測的其他適應症（原發性硬化性膽管炎、支氣管炎、一種極罕見的遺傳發育症候群、重度非增殖性糖尿病視網膜病變）同樣沒有臨床或文獻支持，也缺乏機轉依據，分數雖高（0.9903–0.9922），但仍為純模型預測，證據等級均為 L5，建議均為 Hold。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67297 | VOCABRIA PROLONGED-RELEASE SUSPENSION FOR INJECTION 600MG/3ML | 長效注射懸浮液 | 許可證資料未載明 |
| HK-67298 | VOCABRIA TABLETS 30MG | 錠劑 | 許可證資料未載明 |
| HK-67296 | VOCABRIA PROLONGED-RELEASE SUSPENSION FOR INJECTION 400MG/2ML | 長效注射懸浮液 | 許可證資料未載明 |

三張許可證皆由 GlaxoSmithKline Limited 持有，均為單方製劑且狀態有效。

---

## 安全性考量

- **藥物交互作用**：已查詢到 7 項中度交互作用，均屬含多價陽離子的抗酸劑或補充劑：
  - 碳酸鈣 (Calcium carbonate)
  - 氫氧化鋁 (Aluminum hydroxide)
  - 碳酸鎂 (Magnesium carbonate)
  - 氫氧化鎂 (Magnesium hydroxide)
  - 氧化鎂 (Magnesium oxide)
  - 碳酸氫鈉 (Sodium bicarbonate)
  - 檸檬酸鈉 (Sodium citrate)

警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數，沒有臨床試驗、文獻或可成立的機轉依據（證據等級 L5）。
- 原適應症、作用機轉與仿單安全性資料目前也不完整，無法進一步評估。

**若要推進需要：**
- 取得香港衛生署仿單，補齊核准適應症、警語與禁忌症
- 補充 Cabotegravir 的作用機轉資料（如 DrugBank）
- 針對類風濕性關節炎進行文獻與臨床試驗系統性檢索，並評估是否有任何免疫調節相關的前臨床證據
- 若日後有證據出現，再評估長效注射劑型與新適應症的給藥途徑是否相容

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Vocabria (cabotegravir sodium) prescribing information, ViiV Healthcare Company](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=66d450fb-cca4-476c-b0c7-c0730e3e4cf3) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

