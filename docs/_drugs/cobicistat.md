---
layout: default
title: Cobicistat
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 3
monitor_inn: "COBICISTAT"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-11-24
description: "Cobicistat：預測新適應症為貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome)（證據等級 L5）。原適應症：HIV 感染、愛滋病"
---

# Cobicistat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Cobicistat：從 HIV 感染到貓後天免疫缺陷症候群
{: .text-alpha }

## 一句話總結

Cobicistat 在知識圖譜中記錄的原適應症為 HIV 感染與愛滋病，臨床上作為藥物動力學增強劑，與其他抗病毒藥物合併使用。
TxGNN 模型預測它可能對**貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個預測，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染、愛滋病（知識圖譜記錄；香港許可證資料未提供適應症文字） |
| 預測新適應症 | 貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Cobicistat 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Cobicistat是細胞色素P450 3A（CYP3A）的機轉型抑制劑。Cobicistat抑制CYP3A介導的代謝，可增加CYP3A受質atazanavir及darunavir的全身暴露量。」英文原文："Cobicistat is a mechanism-based inhibitor of cytochrome P450 3A (CYP3A). Inhibition of CYP3A-mediated metabolism by cobicistat increases the systemic exposure of CYP3A substrates atazanavir and darunavir."（[DailyMed: Tybost (cobicistat) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3784c35c-e87f-410c-900b-8fd6313c6010)，版本日期 2026-02-10；查閱日期 2026-11-19）。根據已知資訊，cobicistat 是一種 CYP3A 抑制劑，用來提高合併使用之抗逆轉錄病毒藥物的血中濃度，本身沒有直接的抗病毒活性。

貓免疫缺乏病毒（FIV）與 HIV 同屬慢病毒，因此這個高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據。但這屬於獸醫領域的適應症，且任何效益都必須依賴搭配有活性的抗病毒藥物，單獨使用 cobicistat 的合理性不足。

其他兩項預測（猴免疫缺乏病毒感染、伴隨共濟失調步態與無語言的神經發育障礙）同樣沒有證據：前者是 HIV 的靈長類動物模型，後者是罕見遺傳疾病，與 cobicistat 的藥理沒有明顯關聯，分數來自 TxGNN 模型（深度學習），可能只反映模型學到的相關疾病之間的相似性，並非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-64960 | PREZCOBIX TABLETS 800MG/150MG | 複方 | JOHNSON & JOHNSON (HONG KONG) LTD. | 有效 |
| HK-65912 | SYMTUZA TABLETS | 複方 | JOHNSON & JOHNSON (HONG KONG) LTD. | 有效 |

<!-- licenses:end -->

這兩張許可證為含 cobicistat 的複方產品，不能用來說明單一成分 cobicistat 的核准狀況。

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為部分例子：
  - 嚴重（Major）：Loperamide、Triamcinolone、Cisapride、Budesonide
  - 中度（Moderate）：Hydrocortisone、Aprepitant、Betamethasone、Clarithromycin、Repaglinide、Metoclopramide
  - 輕微（Minor）：Prucalopride

  這些交互作用多與 CYP3A 抑制有關，任何新用途都需審慎評估。

其餘警語與禁忌資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何臨床試驗或文獻直接研究這個疾病，證據等級為 L5。
- 預測的疾病屬於獸醫領域，與人類臨床應用無關；cobicistat 本身沒有抗病毒活性，且交互作用數量多。

**若要推進需要：**
- 補充 cobicistat 的作用機轉資料
- 取得香港仿單的警語、禁忌與核准適應症
- 針對 FIV 的前臨床或動物研究證據（若確有獸醫開發意圖）
- 釐清此預測是否有任何人類臨床價值，否則不建議投入資源

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Tybost (cobicistat) prescribing information, Gilead Sciences, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3784c35c-e87f-410c-900b-8fd6313c6010) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

