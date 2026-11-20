---
layout: default
title: Canakinumab
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 9
monitor_inn: "CANAKINUMAB"
predicted_indications: ["hepatic infarction", "hepatic veno-occlusive disease", "peliosis hepatis", "syndrome with combined immunodeficiency", "periodic fever-infantile enterocolitis-autoinflammatory syndrome", "extracutaneous mastocytoma", "Blau syndrome", "monosomy X", "liver angiosarcoma"]
last_modified_at: 2026-10-28
description: "Canakinumab：預測新適應症為肝梗塞 (hepatic infarction)（證據等級 L5）。香港藥劑製品註冊：1 張（有效 1 張）"
---

# Canakinumab
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

## Canakinumab：介白素-1β 單株抗體 → 肝梗塞 (hepatic infarction)
{: .text-alpha }

## 一句話總結

Canakinumab 是一種抑制介白素-1β (IL-1β) 的單株抗體。
TxGNN 模型預測它可能對**肝梗塞 (hepatic infarction)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 肝梗塞 (hepatic infarction) |
| TxGNN 預測分數 | 0.9986 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Canakinumab 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Canakinumab 是一種 IgG1/κ 同型的人類抗人類 IL-1β 單株抗體。Canakinumab 會與人類 IL-1β 結合，並藉由阻斷其與 IL-1 受體的交互作用而中和其活性，但不會與 IL-1α 或 IL-1 受體拮抗劑（IL-1ra）結合。」英文原文："Canakinumab is a human monoclonal anti-human IL-1β antibody of the IgG1/κ isotype. Canakinumab binds to human IL-1β and neutralizes its activity by blocking its interaction with IL-1 receptors, but it does not bind IL-1α or IL-1 receptor antagonist (IL-1ra)."（[DailyMed: Ilaris (canakinumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d271f3b-e4f9-4d80-8dcf-28d49123f80e)，版本日期 2026-06-08；查閱日期 2026-11-19）。根據已知資訊，canakinumab 是 IL-1β 的單株抗體，
理論上可抑制 IL-1β 所驅動的發炎反應。

肝梗塞是肝組織缺血造成的壞死，缺血後常伴隨無菌性發炎。
理論上，阻斷 IL-1β 可能減輕這類缺血相關的發炎反應。
然而，這只是推測，並沒有任何已建立的直接機轉連結。

整體而言，此預測純粹來自計算模型 (TxGNN)，沒有臨床試驗或文獻佐證，
需要先經過基礎研究與回溯性資料驗證，才能判斷是否值得推進。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65635 | ILARIS SOLUTION FOR INJECTION 150MG/ML | 注射液 | 本地資料未記載 |

## 安全性考量

- **藥物交互作用**：已查得 100 筆潛在交互作用，主要包括：
  - 中度：皮質類固醇（hydrocortisone、triamcinolone、dexamethasone、betamethasone、budesonide、prednisolone、prednisone）、simvastatin
  - 中度：抗凝血藥（apixaban、rivaroxaban、warfarin、dicoumarol）
  - 中度：放射性藥物（ibritumomab tiuxetan、tositumomab、iobenguane I-131）
  - 輕度：鋅鹽類（zinc acetate、zinc gluconate、zinc sulfate）

警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 肝梗塞的預測分數雖高 (0.9986)，但沒有任何直接研究該疾病的臨床試驗或文獻，證據等級為 L5。
- 機轉連結僅為理論推測，且缺乏作用機轉與仿單安全性資料。

**若要推進需要：**
- 補齊 canakinumab 的作用機轉資料與香港仿單的警語、禁忌症
- 建立肝梗塞中 IL-1β 參與的基礎或動物模型證據
- 回溯性文獻或病例資料，評估 IL-1 阻斷在缺血性肝損傷的可行性
- 評估目標族群的感染風險與藥物交互作用監測計畫

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Ilaris (canakinumab) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=7d271f3b-e4f9-4d80-8dcf-28d49123f80e) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

