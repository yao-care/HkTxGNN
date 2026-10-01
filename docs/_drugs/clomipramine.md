---
layout: default
title: Clomipramine
parent: 高證據等級 (L1-L2)
nav_order: 214
evidence_level: L2
indication_count: 10
---

# Clomipramine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Clomipramine：從（原適應症資料缺漏）到焦慮症（含恐慌症／懼曠症）

## 一句話總結

Clomipramine 是一種三環抗憂鬱藥，香港有 4 張許可證，但本次資料未提供核准適應症文字。
TxGNN 模型預測它可能對**焦慮症 (Anxiety Disorder)** 有效。
目前有 **18 個相關臨床試驗登記**（多為強迫症 OCD）和 **20 篇文獻**，但真正直接支持的試驗多屬強迫症，且主要研究年代久遠。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺漏（香港許可證未附適應症文字） |
| 預測新適應症 | 焦慮症 (Anxiety Disorder) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。根據文獻，Clomipramine 是強效的血清素再回收抑制劑，其活性代謝物 desmethylclomipramine 也會抑制正腎上腺素再回收。

這種血清素與正腎上腺素的雙重作用，與強迫症和恐慌症的療效相符。這些疾病在傳統分類中都屬於焦慮症範疇。

需要注意：登記的試驗幾乎都是強迫症，而強迫症本來就是 Clomipramine 的已知適應症，因此並非真正的「新用途」訊號。非強迫症的焦慮證據主要來自恐慌症與懼曠症的文獻，包括與 diazepam、paroxetine、認知治療的對照試驗。

## 臨床試驗證據

以下為與 Clomipramine 最相關的試驗（其餘多為非藥物介入或以其他藥物為主的研究，未列出）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00004310](https://clinicaltrials.gov/study/NCT00004310) | Phase 2 | 未知 | 76 | 強迫症患者靜脈與口服 Clomipramine 比較 |
| [NCT00466609](https://clinicaltrials.gov/study/NCT00466609) | Phase 4 | 完成 | 54 | 對第一線藥物無反應的強迫症，比較 fluoxetine 加 quetiapine 或加 clomipramine |
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Phase 4 | 完成 | 21 | SSRI 治療失敗的強迫症，比較 quetiapine 與 clomipramine 增效（樣本小） |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | NA | 完成 | 26 | 強迫症藥物反應預測，隨機分派 clomipramine 或 escitalopram |
| [NCT00254735](https://clinicaltrials.gov/study/NCT00254735) | Phase 3 | 完成 | 44 | Quetiapine 加在 SSRI／clomipramine 基礎治療上，用於嚴重強迫症 |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | 完成 | 124 | 兒童強迫症，SRI 部分反應者加上認知行為治療 |
| [NCT01148316](https://clinicaltrials.gov/study/NCT01148316) | NA | 完成 | 144 | 兒童青少年精神疾病適應性治療策略，涵蓋 clomipramine 與 SSRI |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | 終止 | 407 | 老年精神科患者藥物安全性監測，非特定適應症 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | 網絡統合分析 | Cochrane Database Syst Rev | 成人恐慌症藥物治療比較 |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2026 | 系統性回顧 | Psychother Psychosom | 難治型焦慮症的藥物、心理與神經刺激治療 |
| [10665629](https://pubmed.ncbi.nlm.nih.gov/10665629/) | 1999 | RCT | J Clin Psychiatry | 12 週安慰劑對照，比較 paroxetine、clomipramine 與認知治療於恐慌症 |
| [10066007](https://pubmed.ncbi.nlm.nih.gov/10066007/) | 1999 | RCT | Acta Psychiatr Scand | 180 名恐慌症患者，高低劑量 clomipramine 均優於安慰劑 |
| [9585709](https://pubmed.ncbi.nlm.nih.gov/9585709/) | 1998 | RCT | Am J Psychiatry | 比較有氧運動、clomipramine 與安慰劑於恐慌症 |
| [7621388](https://pubmed.ncbi.nlm.nih.gov/7621388/) | 1995 | RCT | Can J Psychiatry | 108 名懼曠症女性，比較 clomipramine、行為治療、合併及安慰劑 |
| [6373161](https://pubmed.ncbi.nlm.nih.gov/6373161/) | 1984 | RCT | Curr Med Res Opin | 社區診所懼曠症與社交畏懼症，clomipramine 對照 diazepam |
| [11277602](https://pubmed.ncbi.nlm.nih.gov/11277602/) | 2001 | 臨床研究 | J Psychopharmacol | 81 名恐慌症患者，70.3% 達完全緩解 |
| [2178909](https://pubmed.ncbi.nlm.nih.gov/2178909/) | 1990 | Review | Drugs | Clomipramine 在強迫症與恐慌症的藥理與療效回顧 |
| [22204483](https://pubmed.ncbi.nlm.nih.gov/22204483/) | 2012 | Review | Curr Top Med Chem | 強迫症與恐慌症／懼曠症治療策略 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-45562 | ANAFRANIL TAB 25MG S/C | 資料缺漏 | 資料缺漏 |
| HK-45537 | ANAFRANIL TAB 10MG S/C | 資料缺漏 | 資料缺漏 |
| HK-40592 | APO-CLOMIPRAMINE TAB 10MG | 資料缺漏 | 資料缺漏 |
| HK-41079 | APO-CLOMIPRAMINE TAB 25MG | 資料缺漏 | 資料缺漏 |

## 安全性考量

安全性資訊請參考原廠仿單。

文獻中另有提及的風險訊號（非仿單資料）：抗膽鹼作用、癲癇發作（約 0.4%）、心臟與過量毒性、年輕族群的自殺風險警語、個案報告的全血球減少及誘發抽搐樣症狀（tourettism）。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
恐慌症與懼曠症有多個對照試驗支持，機轉合理，且藥物已在香港上市。但這些試驗年代久遠、規模小、未登記於試驗註冊平台，強迫症試驗也不算真正的新適應症，因此證據等級保守定為 L2。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症（目前為阻斷性資料缺口）
- 補齊作用機轉資料（DrugBank）
- 針對非強迫症焦慮亞型（恐慌症、懼曠症）進行近期的統合分析或隨機對照試驗
- 制定心臟、抗膽鹼與自殺風險的監測計畫

**其他預測適應症（供參考）：**
- 重度憂鬱症、內因性憂鬱症：Clomipramine 本就屬抗憂鬱藥，非真正新用途。前者為 L2（Proceed with Guardrails），後者為 L3（研究議題）
- 懼曠症：與恐慌症證據重疊，同為 L2
- 注意力不足過動症：僅有其他三環藥的類效應證據，且兒童安全性疑慮大，建議 Hold
- 偏執型、思覺失調型、類分裂型、表演型人格障礙、嬰兒良性陣發性斜頸：無直接證據或僅為模型預測，多半是知識圖譜的假象，建議 Hold
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

