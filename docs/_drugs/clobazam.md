---
layout: default
title: Clobazam
parent: 中證據等級 (L3-L4)
nav_order: 211
evidence_level: L4
indication_count: 10
last_modified_at: 2026-11-24
monitor_inn: "Clobazam"
predicted_indications: ["febrile infection-related epilepsy syndrome", "perioral myoclonia with absences", "photosensitive occipital lobe epilepsy", "atypical childhood epilepsy with centrotemporal spikes", "cryptogenic late-onset epileptic spasms", "childhood onset epileptic encephalopathy", "benign occipital epilepsy", "early-onset epileptic encephalopathy and intellectual disability due to GRIN2A mutation", "restless legs syndrome", "polymicrogyria with optic nerve hypoplasia"]
description: "Clobazam：預測新適應症為Febrile infection-related epilepsy syndrome（證據等級 L4）。香港藥劑製品註冊：3 張（有效 3 張）"
---

# Clobazam
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

## Clobazam: Febrile infection-related epilepsy syndrome
{: .text-alpha }

## 一句話總結

Clobazam 是一種苯二氮平類（1,5-benzodiazepine）抗癲癇藥，原本用於 Lennox-Gastaut 症候群與腦回狀頭皮（cutis verticis gyrata）。
TxGNN 模型預測它可能對**熱性感染相關癲癇症候群（FIRES）**有效，
但目前**沒有臨床試驗**，僅有 **2 篇**間接相關文獻（病例系列與個案報告，且均未直接測試 clobazam）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Febrile infection-related epilepsy syndrome |
| TxGNN 預測分數 | 0.9982 |
| 證據等級 | L4 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold（列為研究問題，暫不推進） |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Clobazam 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Clobazam 是一種 1,5-benzodiazepine，其確切作用機轉尚未完全明瞭，但一般認為涉及經由結合於 GABA A 受體的 benzodiazepine 位點而增強 GABA 能神經傳導。」英文原文："The exact mechanism of action for clobazam, a 1,5-benzodiazepine, is not fully understood but is thought to involve potentiation of GABAergic neurotransmission resulting from binding at the benzodiazepine site of the GABA A receptor."（[DailyMed: Onfi (clobazam) prescribing information, Lundbeck Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de03bd69-2dca-459c-93b4-541fd3e9571c)，版本日期 2026-10-16；查閱日期 2026-11-19）。根據已知資訊，Clobazam 是 GABA-A 受體的正向異位調節劑。FIRES 是一種難治性癲癇性腦病變，臨床上常使用 midazolam、lorazepam、巴比妥類等 GABA 能藥物，因此機轉上有合理性。

不過，目前提供的文獻談的是其他藥物（腸道給予 lorazepam、perampanel），並未直接測試 clobazam。此預測目前主要建立在藥物類別層級的推論，屬於間接支持。

此外，排名較後的預測（如 perioral myoclonia with absences、restless legs syndrome 等）幾乎只有模型分數支持，證據更為薄弱，因此本報告以排名第一的 FIRES 為主軸。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35770765](https://pubmed.ncbi.nlm.nih.gov/35770765/) | 2022 | 世代研究／病例系列 | Epileptic Disord | 腸道給予 lorazepam 可作為 midazolam 依賴型 FIRES 患者的撤藥替代策略（未涉及 clobazam） |
| [39958143](https://pubmed.ncbi.nlm.nih.gov/39958143/) | 2025 | 個案報告 | Cureus | 一名 13 歲男童使用 perampanel，可能有助於降低巴比妥類依賴（未涉及 clobazam） |

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-67412 | TAPCLOB ORAL SUSPENSION 5MG/5ML | 單一成分 | THE INTERNATIONAL MEDICAL COMPANY LIMITED | 有效 |
| HK-05574 | FRISIUM 10 TAB 10MG | 單一成分 | DKSH HONG KONG LIMITED | 有效 |
| HK-67411 | TAPCLOB ORAL SUSPENSION 10MG/5ML | 單一成分 | THE INTERNATIONAL MEDICAL COMPANY LIMITED | 有效 |

<!-- licenses:end -->

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用，以下列出較重要者：
  - **嚴重（Major）**：Morphine（含脂質體劑型）、Eliglustat
  - **中度（Moderate）**：Bupropion、Aprepitant、Omeprazole、Esomeprazole、Lansoprazole、Cimetidine、Clarithromycin、Fenfluramine、Metoclopramide 等
  - **輕微（Minor）**：多種制酸劑（氫氧化鎂、氫氧化鋁、碳酸鈣等）

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 模型分數雖高（0.9982），但目前沒有任何臨床試驗，文獻也未直接評估 clobazam 對 FIRES 的效果，證據停留在 L4（僅有機轉推論與間接文獻）。
- 作用機轉資料與仿單安全性資料（警語、禁忌症）仍有缺口，尚無法進入安全性篩選。

**若要推進需要：**
- 取得 Clobazam 的作用機轉資料（如透過 DrugBank）
- 下載並解析香港衛生署的仿單，補齊警語、禁忌症與核准適應症
- 檢索 clobazam 用於 FIRES 或 NORSE 的直接病例報告／回溯性研究
- 評估 FIRES 患者（多為兒童、常需重症照護）是否適合口服劑型（懸液劑 TAPCLOB 可能較合適），並釐清與常用 GABA 能藥物合併使用時的交互作用風險

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Onfi (clobazam) prescribing information, Lundbeck Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=de03bd69-2dca-459c-93b4-541fd3e9571c) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

