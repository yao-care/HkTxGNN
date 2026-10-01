---
layout: default
title: Loxapine
parent: 僅模型預測 (L5)
nav_order: 535
evidence_level: L5
indication_count: 5
---

# Loxapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Loxapine：從精神科急性躁動治療到躁狂型雙相情感障礙

## 一句話總結

Loxapine 是第一代抗精神病藥，香港已上市吸入粉劑劑型（Adasuve），文獻顯示其用於思覺失調症或雙相障礙相關的急性躁動。
TxGNN 模型預測它可能對**躁狂型雙相情感障礙 (Manic Bipolar Affective Disorder)** 有效。
目前沒有登記的臨床試驗，但有 **20 篇文獻**，其中包含 2 項 Phase III RCT 的統合分析。這些證據支持的是「雙相 I 型相關躁動」，不是躁狂症狀本身。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明；文獻顯示吸入劑型用於思覺失調症或雙相 I 型障礙相關的急性躁動 |
| 預測新適應症 | 躁狂型雙相情感障礙 (Manic Bipolar Affective Disorder) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1（證據為間接證據，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

DrugBank 記錄缺乏詳細的作用機轉欄位。根據預測理由，Loxapine 是二苯并氧氮平 (dibenzoxazepine) 類抗精神病藥，具有 D2 與 5-HT2A 受體拮抗作用。這個受體特性與急性躁狂治療中常用的抗精神病藥相同。

原用途（精神病相關躁動）與預測用途（雙相躁狂）在臨床上高度重疊，躁動本來就是躁狂發作常見的表現。直接證據來自吸入型 Loxapine 用於雙相 I 型障礙急性躁動的兩項 Phase III RCT 統合分析（PMID 22226343）。

需要留意的是，這些證據並未證明它能治療躁狂症候群本身，所以機轉連結屬於藥物類別層級的推論。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

文獻 PMID 29163985 提到兩項 Phase III 隨機、雙盲、安慰劑對照試驗（NCT00628589、NCT00721955），共納入 344 名思覺失調症躁動患者與 314 名雙相 I 型障礙患者。但這兩項試驗不在本證據包的臨床試驗欄位中，其狀態需另行確認。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29724638](https://pubmed.ncbi.nlm.nih.gov/29724638/) | 2018 | RCT（PLACID，評估者盲性） | Eur Neuropsychopharmacol | 比較吸入 Loxapine 與肌肉注射 aripiprazole 用於思覺失調症或雙相 I 型障礙急性躁動的療效與安全性 |
| [22226343](https://pubmed.ncbi.nlm.nih.gov/22226343/) | 2012 | 2 項 Phase III RCT 統合分析 | Int J Clin Pract | 以效應量描述吸入 Loxapine 對思覺失調症或雙相障礙躁動的療效 |
| [29163985](https://pubmed.ncbi.nlm.nih.gov/29163985/) | 2017 | RCT 反應者分析 | BJPsych Open | 兩項 Phase III 試驗中，5 或 10 mg 吸入 Loxapine 以 PANSS-EC 評估對躁動有效 |
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | 系統性回顧與統合分析 | Hum Psychopharmacol | 評估思覺失調症或雙相障礙躁動的短期藥物介入 |
| [23740380](https://pubmed.ncbi.nlm.nih.gov/23740380/) | 2013 | Review（藥物概述） | CNS Drugs | Adasuve 已在美國與歐盟核准用於雙相障礙或思覺失調症的急性躁動；血中濃度中位 2 分鐘達峰 |
| [31496709](https://pubmed.ncbi.nlm.nih.gov/31496709/) | 2019 | Review | Neuropsychiatr Dis Treat | 檢視吸入 Loxapine 用於思覺失調症或雙相 I 型障礙躁動的安全性、療效與病人接受度 |
| [30721526](https://pubmed.ncbi.nlm.nih.gov/30721526/) | 2019 | Review（專家評論） | Drugs R D | 討論吸入 Loxapine 處理雙相障礙與思覺失調症急性躁動的角色，強調非強制性處置 |
| [37581475](https://pubmed.ncbi.nlm.nih.gov/37581475/) | 2023 | Review | Expert Opin Pharmacother | 雙相障礙躁動常見於躁狂發作，核准的藥物選項有限 |
| [38301034](https://pubmed.ncbi.nlm.nih.gov/38301034/) | 2024 | Review（間接） | Prim Care Companion CNS Disord | 探討肌肉注射之外處理急性躁動的替代方式 |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review（間接，非 Loxapine 專屬） | Acta Psychiatr Scand | 回顧雙相躁狂的治療選項，包含情緒穩定劑與抗精神病藥的選擇 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67228 | ADASUVE INHALATION POWDER, PRE-DISPENSED 9.1MG（廠商：LEE'S PHARMACEUTICAL (H.K) LIMITED） | 吸入粉劑（依品名判斷） | 許可證資料未載明 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 吸入型 Loxapine 已有 Phase III RCT 支持用於雙相 I 型障礙的急性躁動，且香港已有上市許可證。
- 但證據針對的是「躁動」而非「躁狂症候群」，安全性資料與作用機轉資料也有缺口，因此不宜直接給 Go。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症，這是目前的阻斷性缺口
- 補充 DrugBank 的作用機轉資料
- 確認 NCT00628589、NCT00721955 的登記狀態與完整結果
- 釐清「雙相躁動」與「躁狂發作」的適應症界線，並確認香港核准適應症的實際文字
- 其餘 4 項預測（視網膜失養症、無腦回畸形、X 連鎖近視、糖基化先天異常）皆無臨床試驗與有效文獻，且缺乏機轉依據，建議維持 Hold

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

