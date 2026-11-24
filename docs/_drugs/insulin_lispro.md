---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 475
evidence_level: L5
indication_count: 9
monitor_inn: "INSULIN LISPRO"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "drug-induced localized lipodystrophy", "pancreatic agenesis", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
last_modified_at: 2026-11-24
description: "Insulin Lispro：預測新適應症為自體免疫性卵巢炎 (autoimmune oophoritis)（證據等級 L5）。原適應症：第 2 型糖尿病、第 1 型糖尿病、糖尿病酮酸中毒"
---

# Insulin Lispro
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

## Insulin Lispro：從糖尿病到自體免疫性卵巢炎
{: .text-alpha }

## 一句話總結

Insulin lispro 是速效型胰島素類似物，知識圖譜中記錄的用途為第 1 型與第 2 型糖尿病、糖尿病酮酸中毒等。
TxGNN 模型預測它可能對**自體免疫性卵巢炎 (autoimmune oophoritis)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持，屬於純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第 2 型糖尿病、第 1 型糖尿病、糖尿病酮酸中毒（知識圖譜記錄的關聯；香港許可證資料未提供適應症文字） |
| 預測新適應症 | 自體免疫性卵巢炎 (autoimmune oophoritis) |
| TxGNN 預測分數 | 0.9978 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Insulin Lispro 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「調節葡萄糖代謝是胰島素及胰島素類似物（包括insulin lispro產品）的主要作用。胰島素透過刺激骨骼肌及脂肪的周邊葡萄糖攝取，以及抑制肝臟葡萄糖生成，從而降低血糖。」英文原文："Regulation of glucose metabolism is the primary activity of insulins and insulin analogs, including insulin lispro products. Insulins lower blood glucose by stimulating peripheral glucose uptake by skeletal muscle and fat, and by inhibiting hepatic glucose production."（[DailyMed: Admelog (insulin lispro) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12ec9e3f-e2ac-43a1-b334-8b6538cf2bb0)，版本日期 2026-09-03；查閱日期 2026-11-19）。Insulin lispro 是胰島素類似物，知識圖譜記錄其與糖尿病相關疾病有關聯，但本報告所編資料並未提供其機轉描述。

自體免疫性卵巢炎常與自體免疫多腺體症候群並存，而後者可能包含第 1 型糖尿病。因此模型的高分，較可能反映「共同的自體免疫共病」，而不是胰島素對卵巢自體免疫的治療作用。

胰島素預期無法治療免疫介導的卵巢損傷。此預測目前僅是計算層面的關聯，缺乏任何可驗證的機轉支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-60381 | HUMALOG 100 U/ML KWIKPEN SOLUTION FOR INJECTION | 單一成分 | ELI LILLY ASIA, INC. | 有效 |
| HK-42887 | HUMALOG INJ 3ML CARTRIDGE 100U/ML | 單一成分 | ELI LILLY ASIA, INC. | 有效 |
| HK-42886 | HUMALOG INJ 100U/ML | 單一成分 | ELI LILLY ASIA, INC. | 有效 |
| HK-60379 | HUMALOG MIX50 100 U/ML KWIKPEN SUSPENSION FOR INJECTION | 複方 | ELI LILLY ASIA, INC. | 有效 |
| HK-60380 | HUMALOG MIX25 100 U/ML KWIKPEN SUSPENSION FOR INJECTION | 複方 | ELI LILLY ASIA, INC. | 有效 |

<!-- licenses:end -->

以上 5 張許可證皆由 ELI LILLY ASIA, INC. 持有，狀態有效。

---

## 安全性考量

- **藥物交互作用**：共查得 100 筆交互作用，以下為部分中度等級項目：
  - 擬交感神經藥物與支氣管擴張劑：Phenylephrine、Pseudoephedrine、Epinephrine、Salbutamol、Formoterol
  - β 阻斷劑：Acebutolol
  - 其他降血糖藥物：Metformin、Alogliptin、Albiglutide
  - 荷爾蒙類：Estradiol、Ethinylestradiol、Levonorgestrel、Hydrocortisone
  - 其他：Acetazolamide、Hydrochlorothiazide、Doxycycline、Alpelisib、Ethanol

其餘警語與禁忌資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型，沒有任何研究直接探討 insulin lispro 用於自體免疫性卵巢炎，證據等級為 L5。
- 機轉上，胰島素不太可能改變免疫介導的卵巢損傷，高分較可能源於與第 1 型糖尿病的共病關聯。

**其他排名較前的預測也宜謹慎看待：**
- 硫胺素反應性功能障礙症候群、僵人症候群、局限性僵肢症候群：關聯可能來自合併的糖尿病，胰島素僅能處理糖尿病成分，無法處理核心疾病。
- 藥物誘發局部脂肪失養症：這是胰島素注射的已知不良反應，屬安全訊號，不是再利用候選。
- 胰臟發育不全：唯一文獻（PMID 12150359）談的是第 2 型糖尿病的胰島素治療，並未直接研究此疾病，故不能作為直接證據；胰島素補充本就是標準處置，並非新機轉。

**若要推進需要：**
- 先釐清自體免疫性卵巢炎患者是否有任何胰島素相關的臨床或文獻訊號
- 補充作用機轉資料與香港仿單的警語及禁忌
- 若有意探討，應先做機轉或前臨床研究，再考慮臨床試驗設計

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Admelog (insulin lispro) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=12ec9e3f-e2ac-43a1-b334-8b6538cf2bb0) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

