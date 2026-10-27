---
layout: default
title: Insulin Glargine
parent: 僅模型預測 (L5)
nav_order: 472
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Insulin Glargine：預測新適應症為自體免疫性卵巢炎 (Autoimmune Oophoritis)（證據等級 L5）。原適應症：第 2 型糖尿病、第 1 型糖尿病、糖尿病酮酸中毒"
monitor_inn: "INSULIN GLARGINE"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia"]
---

# Insulin Glargine
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

## Insulin Glargine：從第 1 型與第 2 型糖尿病到自體免疫性卵巢炎
{: .text-alpha }

## 一句話總結

Insulin Glargine 是長效基礎胰島素類似物，原本用於第 1 型與第 2 型糖尿病（含糖尿病酮酸中毒）的治療。
TxGNN 模型預測它可能對**自體免疫性卵巢炎 (Autoimmune Oophoritis)** 有效，但目前**沒有臨床試驗與文獻**支持這個方向，僅為模型層級的預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第 2 型糖尿病、第 1 型糖尿病、糖尿病酮酸中毒（依知識圖譜資料） |
| 預測新適應症 | 自體免疫性卵巢炎 (Autoimmune Oophoritis) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Insulin Glargine 是長效胰島素類似物，其在糖尿病血糖控制上的療效已被證實，但機轉上是否適用於自體免疫性卵巢炎，現有資料無法確認。

可能的間接關聯有兩點：一是胰島素訊號會影響卵巢功能；二是自體免疫內分泌疾病常與自體免疫性糖尿病並存（多腺體自體免疫）。這些屬於假說層級的推論，**並沒有本報告所整理資料的實證支持**。

此外，預測分數雖高（99.88%），但僅代表知識圖譜中的關聯強度，不等同於治療效果。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56520 | LANTUS SOLOSTAR PRE-FILLED PEN INJ 100 UNITS/ML | 預填充注射筆（注射劑） | — |
| HK-64661 | TOUJEO 300 UNITS/ML SOLUTION FOR INJECTION IN PRE-FILLED PEN 450 UNITS/1.5ML | 預填充注射筆（注射劑） | — |
| HK-65078 | BASAGLAR KWIKPEN SOLUTION FOR INJECTION IN A PRE-FILLED PEN 300 UNITS/3ML | 預填充注射筆（注射劑） | — |
| HK-65079 | BASAGLAR SOLUTION FOR INJECTION IN A CARTRIDGE 300 UNITS/3ML | 卡式瓶注射劑 | — |
| HK-50530 | LANTUS INJ 100 UNITS/ML | 注射劑 | — |

另有 2 張許可證（HK-65637、HK-65638，SOLIQUA 複方預填充注射筆，含 GLP-1 受體促效劑 lixisenatide），共計 7 張有效許可證。核准適應症文字在登記資料中未提供。

## 安全性考量

- **藥物交互作用**：共查到 100 筆交互作用紀錄，以下為部分中度（Moderate）項目：
  - 其他降血糖藥：Metformin、Pioglitazone、Alogliptin、Albiglutide（可能增強降血糖作用）
  - 擬交感神經藥物與 β 受體作用劑：Epinephrine、Phenylephrine、Pseudoephedrine、Salbutamol、Formoterol
  - β 阻斷劑：Acebutolol（可能掩蓋低血糖症狀）
  - 其他：Hydrocortisone、Estradiol、Ethinylestradiol、Hydrochlorothiazide、Acetazolamide、Doxycycline、Ethanol、Alpelisib
  - 輕度（Minor）：外用 Hydrocortisone、外用 Alclometasone

主要警語與禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何臨床試驗或文獻佐證，證據等級為 L5。
- 作用機轉資料缺漏，且香港仿單的警語與禁忌症尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 補齊 Insulin Glargine 的作用機轉資料（MOA）
- 取得香港衛生署仿單，確認警語與禁忌症
- 進行自體免疫性卵巢炎的文獻與臨床試驗檢索，確認是否有任何直接證據
- 釐清預測是否僅反映與糖尿病的共病關聯（而非對卵巢炎本身的療效）
- 評估給藥途徑（注射）與目標疾病的相容性

**其他預測適應症備註：** 另有四項預測（硫胺素反應性功能障礙症候群、典型僵人症候群、局部僵肢症候群、Opsismodysplasia）同樣僅有模型分數、無實證支持，且多半可能反映與糖尿病的共病關聯，目前同樣建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

