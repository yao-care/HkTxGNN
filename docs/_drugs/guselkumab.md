---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 431
evidence_level: L5
indication_count: 8
monitor_inn: "GUSELKUMAB"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "renal osteodystrophy", "congenital hypotrichosis with juvenile macular dystrophy", "primary release disorder of platelets", "Glanzmann thrombasthenia", "non-renal secondary hyperparathyroidism"]
last_modified_at: 2026-11-24
description: "Guselkumab：預測新適應症為藥物誘發性骨質疏鬆症（證據等級 L5）。原適應症：許可證資料未載明"
---

# Guselkumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Guselkumab：從已上市適應症（許可證未載明）到藥物誘發性骨質疏鬆症
{: .text-alpha }

## 一句話總結

Guselkumab 是一種 IL-23 p19 抑制劑，在香港已有 5 張有效許可證，但許可證資料中未載明核准適應症。
TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆症 (drug-induced osteoporosis)** 有效，
目前**沒有臨床試驗，也沒有文獻**直接支持這個方向，僅有模型預測。

<!-- review:begin hk-lic-20261117-guselkumab-1 -->

> **查核更正（2026-11-17）**：原文為「在香港已有 2 張有效許可證」。已更正：衞生署藥物辦公室註冊藥劑製品名單（2026-11-13 版）另有 HK-69234、HK-69235、HK-69236 屬於本藥的現行註冊（2026-03 版名單之後新增），原本沒有收進本頁資料（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261117-guselkumab-1 -->

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 藥物誘發性骨質疏鬆症 |
| TxGNN 預測分數 | 0.9984 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Guselkumab 是 IL-23 p19 亞單位抑制劑。根據美國 FDA 核准的 Guselkumab 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Guselkumab是一種人類單株IgG1λ抗體，可選擇性地與介白素23（IL-23）的p19次單元結合，並抑制其與IL-23受體的交互作用。IL-23是一種天然存在的細胞激素，參與正常的發炎及免疫反應。」英文原文："Guselkumab is a human monoclonal IgG1λ antibody that selectively binds to the p19 subunit of interleukin 23 (IL-23) and inhibits its interaction with the IL-23 receptor. IL-23 is a naturally occurring cytokine that is involved in normal inflammatory and immune responses."（[DailyMed: Tremfya (guselkumab) prescribing information, Janssen Biotech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e6dc9ae-1c4c-42d9-87aa-c315ecc51b56)，版本日期 2026-10-20；查閱日期 2026-11-19）。

IL-23/IL-17 訊號路徑在發炎性骨流失中可能扮演角色，因此理論上可能與藥物（例如糖皮質素）誘發的骨質疏鬆有關。但這個連結目前仍屬推測，唯一的支持是較高的 TxGNN 預測分數，沒有任何臨床試驗或文獻佐證。

此外，由於許可證資料未載明原適應症，無法比較原適應症與新適應症之間的關聯性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-65944 | TREMFYA SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 100MG/1ML | 單一成分 | JOHNSON & JOHNSON (HONG KONG) LTD. | 有效 |
| HK-67037 | TREMFYA SOLUTION FOR INJECTION IN PRE-FILLED PEN 100MG/1ML | 單一成分 | JOHNSON & JOHNSON (HONG KONG) LTD. | 有效 |

上表列出其中 2 張（共 5 張）。

<!-- licenses:end -->

兩張許可證均為單一成分製劑，持有者為 Johnson & Johnson (Hong Kong) Ltd.。

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下列出部分主要項目：
  - **重大 (Major)**：Adalimumab
  - **中度 (Moderate)**：Simvastatin、Apixaban、Warfarin、Rivaroxaban、Tacrolimus、Theophylline、Fentanyl、Nifedipine、Lidocaine
  - **輕微 (Minor)**：多種鋅製劑（硫酸鋅、醋酸鋅、葡萄糖酸鋅、氯化鋅）

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有 TxGNN 模型預測，沒有任何直接研究藥物誘發性骨質疏鬆症的臨床試驗或文獻，證據等級為 L5。
- 機轉連結屬推測，且許可證資料、作用機轉與仿單警語皆有缺口。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 補充詳細的作用機轉資料（MOA）
- 進行文獻回顧，尋找 IL-23 抑制與骨代謝或糖皮質素誘發骨流失的前臨床或臨床證據
- 若有初步證據，再評估進行探索性研究的可行性

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「在香港已有 2 張有效許可證」→「在香港已有 5 張有效許可證」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Tremfya (guselkumab) prescribing information, Janssen Biotech, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=1e6dc9ae-1c4c-42d9-87aa-c315ecc51b56) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

