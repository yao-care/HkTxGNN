---
layout: default
title: Letermovir
parent: 僅模型預測 (L5)
nav_order: 520
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Letermovir：預測新適應症為外陰陰道念珠菌病 (Vulvovaginal Candidiasis)（證據等級 L5）。原適應症：巨細胞病毒感染 (Cytomegalovirus infection)"
monitor_inn: "LETERMOVIR"
predicted_indications: ["vulvovaginal candidiasis"]
---

# Letermovir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Letermovir：從巨細胞病毒感染到外陰陰道念珠菌病
{: .text-alpha }

## 一句話總結

Letermovir 是一種抗巨細胞病毒（CMV）藥物，原本用於治療 CMV 感染。
TxGNN 模型預測它可能對**外陰陰道念珠菌病 (Vulvovaginal Candidiasis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 巨細胞病毒感染 (Cytomegalovirus infection) |
| 預測新適應症 | 外陰陰道念珠菌病 (Vulvovaginal Candidiasis) |
| TxGNN 預測分數 | 0.9988 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Letermovir 處方資料（Prescribing Information）「Mechanism of Action」與「Microbiology」段（非官方翻譯）：「PREVYMIS 是一種抗 CMV 的抗病毒藥物。[…] Letermovir 抑制 CMV DNA 末端酶複合體（pUL51、pUL56 及 pUL89），該複合體為病毒 DNA 加工及包裝所必需。生化特性分析及電子顯微鏡檢查顯示，letermovir 會影響正確單位長度基因組的產生，並干擾病毒顆粒成熟。」英文原文："PREVYMIS is an antiviral drug against CMV. […] Letermovir inhibits the CMV DNA terminase complex (pUL51, pUL56, and pUL89) which is required for viral DNA processing and packaging. Biochemical characterization and electron microscopy demonstrated that letermovir affects the production of proper unit length genomes and interferes with virion maturation."（[DailyMed: Prevymis (letermovir) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1b49df80-be4f-47e0-a0b7-123f3e69395b)，版本日期 2026-01-14；查閱日期 2026-11-19）。就已知藥理而言，Letermovir 抑制 CMV DNA 終止酶複合體（pUL56/pUL51/pUL89），這個標的是疱疹病毒特有的，在念珠菌（真菌）中沒有已知的同源物。

因此，從現有資料看不出 Letermovir 具有抗黴菌活性的合理機轉。病毒感染與黴菌感染的病原體類型、藥物標的都不同，兩者之間缺乏直接的藥理關聯。

TxGNN 模型（深度學習）給出的高分（0.9988）沒有任何試驗或文獻佐證。這個分數可能反映模型學到的相關疾病之間的相似性，例如與其他抗感染藥物的共同關聯，或與免疫功能低下患者常見疾病的關聯，而非生物學證據或真正的藥理效果。這個預測應謹慎看待。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66124 | PREVYMIS TABLETS 240MG | — | — |
| HK-66125 | PREVYMIS CONCENTRATE FOR SOLUTION FOR INFUSION 240MG/12ML | — | — |
| HK-66122 | PREVYMIS CONCENTRATE FOR SOLUTION FOR INFUSION 480MG/24ML | — | — |
| HK-66123 | PREVYMIS TABLETS 480MG | — | — |

以上 4 張許可證皆為單一成分製劑，狀態有效，持證商為 MERCK SHARP & DOHME (ASIA) LTD。

---

## 安全性考量

- **藥物交互作用**：本報告彙整的資料共有 100 筆交互作用紀錄，以下為部分例子：
  - **嚴重（Major）**：Eliglustat、Naloxegol、Cisapride
  - **中度（Moderate）**：Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone、Omeprazole、Lansoprazole、Aprepitant、Clarithromycin、Pioglitazone、Glimepiride、Saxagliptin 等

警語與禁忌症的資料不足，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何臨床試驗或文獻佐證（證據等級 L5）。
- Letermovir 的已知標的為病毒特有，對念珠菌沒有明確的藥理依據。高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

**若要推進需要：**
- 補充作用機轉（MOA）資料，並確認是否有任何對真菌的活性依據
- 進行體外抗念珠菌活性試驗，作為最基本的前臨床證據
- 取得香港衛生署的仿單，補齊警語與禁忌症資料
- 確認給藥途徑與劑型是否適用於陰道局部或全身治療
- 在上述證據出現之前，不建議投入進一步開發資源

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Prevymis (letermovir) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1b49df80-be4f-47e0-a0b7-123f3e69395b) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

