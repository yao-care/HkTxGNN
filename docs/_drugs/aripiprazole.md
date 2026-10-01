---
layout: default
title: Aripiprazole
parent: 高證據等級 (L1-L2)
nav_order: 69
evidence_level: L1
indication_count: 10
---

# Aripiprazole
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Aripiprazole：從抗精神病藥到重度情感障礙

## 一句話總結

Aripiprazole 是一種非典型抗精神病藥，作用於 D2/5-HT1A 部分促效與 5-HT2A 拮抗。
TxGNN 模型預測它可能對**重度情感障礙 (Major Affective Disorder)** 有效，
目前有 **50 個臨床試驗**和 **20 篇文獻**支持這個方向。
但這個藥已在雙相情感障礙與憂鬱症輔助治療中使用，此訊號較接近「既有用途的印證」，而非全新的再利用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 重度情感障礙 (Major Affective Disorder) |
| TxGNN 預測分數 | 99.62% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據藥理特性，Aripiprazole 是 D2/5-HT1A 部分促效劑，同時是 5-HT2A 拮抗劑。這個受體組合與情緒障礙的藥理相符，也是它被用於抗憂鬱劑反應不佳的憂鬱症輔助治療，以及雙相情感障礙的原因。

從證據看，已有多個 Phase 3 隨機、雙盲、安慰劑對照試驗，在重度憂鬱症患者身上測試 Aripiprazole 作為抗憂鬱劑的輔助治療。另有大型 Phase 4 試驗（樣本數超過 1,000 人）針對雙相 I 型障礙的維持治療。系統性回顧與網絡統合分析也涵蓋了這類輔助治療策略。

需要注意兩點：
- 資料中未提供原適應症，香港許可證的核准適應症文字也是空白，因此無法在本報告中確認本地標示範圍。
- 部分試驗標題被截斷，族群（單極或雙極、成人或兒童）需要逐一確認。

## 臨床試驗證據

共 50 個相關試驗，以下列出 10 個最相關者（Phase 3 完成的對照試驗與大型雙相試驗優先）。資料中僅提供試驗目的與設計，未提供結果數值。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00095758](https://clinicaltrials.gov/study/NCT00095758) | Phase 3 | 完成 | 1200 | 14 週雙盲安慰劑對照，評估 Aripiprazole 輔助抗憂鬱劑治療重度憂鬱症的安全性與療效 |
| [NCT00095823](https://clinicaltrials.gov/study/NCT00095823) | Phase 3 | 完成 | 1200 | 多中心隨機雙盲安慰劑對照，設計同上（14 週輔助治療） |
| [NCT00105196](https://clinicaltrials.gov/study/NCT00105196) | Phase 3 | 完成 | 349 | 14 週雙盲安慰劑對照，先經 8 週抗憂鬱劑療效不足者再加入 Aripiprazole |
| [NCT00683852](https://clinicaltrials.gov/study/NCT00683852) | Phase 3 | 完成 | 225 | 雙盲安慰劑對照，評估較低劑量 Aripiprazole 於抗憂鬱劑反應不足者的療效 |
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | 完成 | 586 | 日本試驗，Aripiprazole 對照安慰劑，併用 SSRI 或 SNRI 治療重度憂鬱症 |
| [NCT02046564](https://clinicaltrials.gov/study/NCT02046564) | Phase 3 | 完成 | 412 | ASC-01（Aripiprazole/Sertraline 複方）對照 Sertraline 單方，用於對 Sertraline 反應不完全者 |
| [NCT01421342](https://clinicaltrials.gov/study/NCT01421342) | Phase 3 | 完成 | 1522 | VAST-D：比較 Aripiprazole 輔助、Bupropion 輔助與換藥，看重度憂鬱症緩解率 |
| [NCT00261443](https://clinicaltrials.gov/study/NCT00261443) | Phase 4 | 完成 | 1270 | Aripiprazole 併用 Lithium 或 Valproate，用於雙相 I 型障礙長期維持 |
| [NCT00277212](https://clinicaltrials.gov/study/NCT00277212) | Phase 4 | 完成 | 1169 | Aripiprazole 併用 Lamotrigine，用於雙相 I 型障礙近期躁症或混合發作後的長期維持 |
| [NCT00110461](https://clinicaltrials.gov/study/NCT00110461) | Phase 3 | 完成 | 296 | 兒童與青少年雙相 I 型障礙，比較兩種劑量 Aripiprazole 的安全性與療效 |

另有進行中的 [NCT03423680](https://clinicaltrials.gov/study/NCT03423680)（Phase 3，招募中，390 人），評估 Aripiprazole 輔助治療雙相 I/II 型的憂鬱發作。

## 文獻證據

共 20 篇相關文獻，以下列出 10 篇（系統性回顧與統合分析優先）。摘要只有部分內容，以下僅摘述研究目的。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38669232](https://pubmed.ncbi.nlm.nih.gov/38669232/) | 2024 | 系統性回顧/統合分析（RCT） | PLoS One | 評估 Aripiprazole 或 Bupropion 輔助與換藥，用於難治型憂鬱症或重度憂鬱症的療效與安全性 |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | 系統性回顧/網絡統合分析 | J Affect Disord | 比較難治型憂鬱症各種輔助藥物的療效與停藥率 |
| [38219278](https://pubmed.ncbi.nlm.nih.gov/38219278/) | 2024 | 系統性回顧/網絡統合分析 | Neuropsychopharmacol Rep | 比較 Brexpiprazole、Aripiprazole 與安慰劑，用於日本抗憂鬱劑反應不足的重度憂鬱症 |
| [34167174](https://pubmed.ncbi.nlm.nih.gov/34167174/) | 2021 | 系統性回顧/統合分析 | Prim Care Companion CNS Disord | 評估 Aripiprazole 輔助治療重度憂鬱症的長期（≥6 個月）緩解率與副作用 |
| [37746943](https://pubmed.ncbi.nlm.nih.gov/37746943/) | 2023 | 系統性回顧/網絡統合分析 | Medicine | 比較 4 種非典型抗精神病藥輔助治療成人重度憂鬱症的療效與安全性 |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | 系統性回顧/統合分析 | Psychol Med | 評估抗精神病藥單方與輔助治療成人重度憂鬱症的療效與安全性 |
| [36961650](https://pubmed.ncbi.nlm.nih.gov/36961650/) | 2023 | RCT | CNS Drugs | 兩個月長效針劑（960 mg）用於思覺失調症或雙相 I 型障礙，評估安全性、耐受性與藥動學 |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | Review | Psychiatr Clin North Am | 難治型憂鬱症藥物治療，非典型抗精神病藥為研究最多的輔助選項 |
| [36855876](https://pubmed.ncbi.nlm.nih.gov/36855876/) | 2023 | Review | Am J Psychiatry | 難治型憂鬱症治療格局，探討抗精神病藥的定位 |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | 雙相情感障礙的診斷與治療 |

## 香港上市資訊

共 20 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症文字，因此改列廠商。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67614 | APO-ARIPIPRAZOLE TABLETS 5MG | HIND WING CO LTD |
| HK-65003 | ARIPIPRAZOLE ACTAVIS TABLETS 5MG | TEVA PHARMACEUTICAL HONG KONG LIMITED |
| HK-66048 | ARIPIPRAZOLE TABLETS 15MG | HONG KONG MEDICAL SUPPLIES LTD |
| HK-68342 | ZYKALOR TABLETS 10MG | MEDOCHEMIE (HONG KONG) LIMITED |
| HK-66046 | ARIPIPRAZOLE TABLETS 5MG | HONG KONG MEDICAL SUPPLIES LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

評估時需特別留意（來自預測理由與文獻）：
- 靜坐不能（akathisia）與代謝方面的不良反應。
- 衝動控制相關不良事件：系統性回顧（PMID 38227009）整理了 Aripiprazole 引起衝動或強迫行為的病例報告。
- 青少年族群需更謹慎。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有多個已完成的 Phase 3 安慰劑對照試驗與多篇統合分析，證據等級為 L1，療效方向明確。
但這個訊號多半是對既有用途的確認，且香港許可證的適應症文字缺漏，本地標示範圍尚未確認，因此附帶防護條件推進。

**若要推進需要：**
- 取得香港衛生署的仿單，確認核准適應症、警語與禁忌症（目前是阻斷性缺口）。
- 逐一確認試驗族群（單極或雙極、成人或兒童），因部分試驗標題被截斷。
- 補齊 DrugBank 的作用機轉資料。
- 釐清此適應症在本地是否已屬標示內用途，決定是否算真正的再利用。
- 建立針對靜坐不能、代謝與衝動控制問題的監測計畫，並特別留意青少年。

**其他預測適應症：**
- 拔毛症（trichotillomania）為 L3，僅有小型開放式試驗與病例報告，唯一的隨機試驗尚未招募，且 Aripiprazole 本身有誘發衝動強迫行為的報告，建議列為研究問題。
- 其餘 8 項預測（如 Phelan-McDermid 症候群等）證據等級皆為 L5，僅有模型預測，建議暫緩（Hold）。

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

