---
layout: default
title: Olopatadine
parent: 僅模型預測 (L5)
nav_order: 643
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-17
description: "Olopatadine：預測新適應症為酒糟性結膜炎 (Rosacea Conjunctivitis)（證據等級 L5）。原適應症：過敏性鼻炎、血管運動性鼻炎、異位性結膜炎、乳突性結膜炎、春季結膜炎"
monitor_inn: "OLOPATADINE"
predicted_indications: ["rosacea conjunctivitis"]
---

# Olopatadine
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

## Olopatadine：從過敏性鼻炎與過敏性結膜炎到酒糟性結膜炎
{: .text-alpha }

## 一句話總結

Olopatadine 是一種抗組織胺藥物，原本用於過敏性鼻炎、血管運動性鼻炎，以及異位性、乳突性與春季結膜炎。
TxGNN 模型預測它可能對**酒糟性結膜炎 (Rosacea Conjunctivitis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏性鼻炎、血管運動性鼻炎、異位性結膜炎、乳突性結膜炎、春季結膜炎 |
| 預測新適應症 | 酒糟性結膜炎 (Rosacea Conjunctivitis) |
| TxGNN 預測分數 | 0.9941 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 9 張／共 9 張） |
| 許可證數 | 9 張（有效 9 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Olopatadine 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Olopatadine為組織胺H 1 受體拮抗劑。Olopatadine的抗組織胺活性已於離體組織、動物模型及人體中獲得證實。」英文原文："Olopatadine is a histamine H 1 receptor antagonist. The antihistaminic activity of olopatadine has been documented in isolated tissues, animal models, and humans."（[DailyMed: olopatadine hydrochloride prescribing information, Apotex Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3aa27224-7b72-38eb-0c21-b8d73525ee85)，版本日期 2026-09-15；查閱日期 2026-11-19）。根據藥理常識，Olopatadine 是選擇性組織胺 H1 受體拮抗劑，同時具有肥大細胞穩定作用，已核准用於過敏性結膜炎（異位性、春季、乳突性）。

酒糟性結膜炎（眼部酒糟）的成因，主要是瞼板腺功能障礙、淚膜不穩定、微生物或蠕形蟎參與，以及發炎介質（如 MMPs、IL-1、TNF-α），而非主要由 IgE 介導的組織胺釋放所致。若有組織胺參與的成分，Olopatadine 的效益可能僅限於緩解搔癢或結膜充血等症狀。

0.9941 的高分可能反映了 TxGNN 模型（深度學習）所學到的酒糟性結膜炎與其他相關結膜炎之間的相似性，純屬計算預測，並非生物學證據。以上機轉評估是依一般藥理知識，而非本報告所整理的資料。

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
| HK-64757 | PARADIN OPHTHALMIC SOLUTION 0.1%W/V | 眼用溶液 | 未提供 |
| HK-63185 | APO-OLOPATADINE OPHTHALMIC SOLUTION 0.1% W/V | 眼用溶液 | 未提供 |
| HK-56385 | PATADAY OPHTHALMIC SOLUTION 0.2% | 眼用溶液 | 未提供 |
| HK-66243 | OPLUS EYE DROPS 0.2% W/V | 眼藥水 | 未提供 |
| HK-68781 | TRANSHINE EYE DROPS 0.2% W/V | 眼藥水 | 未提供 |

此處僅列出 5 張，香港共有 9 張有效單方許可證，全部為有效狀態。

<!-- review:begin hk-lic-20261117-olopatadine-1 -->

> **查核更正（2026-11-17）**：原文為「香港共有 7 張有效單方許可證」。已更正：衞生署藥物辦公室註冊藥劑製品名單（2026-11-13 版）另有 HK-68992、HK-69255 屬於本藥的現行註冊（2026-03 版名單之後新增），原本沒有收進本頁資料（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)。

<!-- review:end hk-lic-20261117-olopatadine-1 -->

---

## 安全性考量

- **知識圖譜中的禁忌疾病**：下呼吸道疾病、鼻竇疾病、鼻腔疾病、上呼吸道疾病（此為知識圖譜關聯，並非仿單文字）。
- **藥物交互作用**：已查得 100 筆潛在交互作用，但嚴重度分級皆為未知。例如：Pantoprazole、Doxycycline、Clotrimazole、Metformin、Omeprazole、Cimetidine、Prednisone、Simvastatin、Epinephrine。

主要警語與正式禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 本預測只有模型分數支持，沒有任何臨床試驗或文獻（證據等級 L5）。
- 酒糟性結膜炎的主要病因並非組織胺介導，機轉上的關聯偏弱，頂多可能緩解症狀。
- 仿單的警語與禁忌症資料尚缺，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與核准適應症。
- 補充詳細的作用機轉資料（MOA）。
- 系統性檢索酒糟性結膜炎使用抗組織胺或肥大細胞穩定劑的臨床與文獻證據。
- 評估眼部酒糟中是否存在組織胺相關症狀（如搔癢、充血），再決定是否設計探索性研究。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「香港共有 7 張有效單方許可證」→「香港共有 9 張有效單方許可證」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: olopatadine hydrochloride prescribing information, Apotex Corp.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=3aa27224-7b72-38eb-0c21-b8d73525ee85) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

