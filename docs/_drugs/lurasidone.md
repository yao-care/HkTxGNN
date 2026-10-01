---
layout: default
title: Lurasidone
parent: 僅模型預測 (L5)
nav_order: 536
evidence_level: L5
indication_count: 10
---

# Lurasidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Lurasidone：從非典型抗精神病藥到躁狂型雙相情感障礙

## 一句話總結

Lurasidone 是非典型抗精神病藥，在香港以 LATUDA 品牌上市。
TxGNN 模型預測它可能對**躁狂型雙相情感障礙 (Manic Bipolar Affective Disorder)** 有效。
目前有 **14 個臨床試驗**和 **20 篇文獻**與雙相情感障礙相關，但多數證據針對雙相憂鬱與維持期，並未明確顯示對急性躁狂有效。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 躁狂型雙相情感障礙 (Manic Bipolar Affective Disorder) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L1（證據主要針對雙相憂鬱與維持期，非急性躁狂） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據分析資料，Lurasidone 屬非典型抗精神病藥，作用於 D2 與 5-HT2A/5-HT7 受體（拮抗）及 5-HT1A 受體（部分促效）。這種受體組合在機轉上適合用於情緒發作的控制。

雙相情感障礙包含躁狂、憂鬱與維持期。目前 Phase 3 證據集中在雙相 I 型憂鬱（單用，或併用鋰鹽/valproate）、認知功能與長期安全性。躁狂與雙相憂鬱同屬雙相情感障礙，模型因此給出高分預測，但現有資料**無法直接證明對急性躁狂有效**。

此外，許可證資料中的原適應症欄位為空，無法核對現行核准適應症與預測適應症的關係，這一點需要補查。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01358357](https://clinicaltrials.gov/study/NCT01358357) | Phase 3 | 完成 | 965 | 雙盲安慰劑對照 RCT：Lurasidone 併用鋰鹽或 divalproex，用於雙相 I 型預防復發 |
| [NCT02046369](https://clinicaltrials.gov/study/NCT02046369) | Phase 3 | 完成 | 350 | 6 週雙盲安慰劑對照：兒童與青少年雙相 I 型憂鬱 |
| [NCT01986101](https://clinicaltrials.gov/study/NCT01986101) | Phase 3 | 完成 | 525 | 雙盲安慰劑對照：SM-13496（Lurasidone 開發代號）用於雙相 I 型憂鬱 |
| [NCT02731612](https://clinicaltrials.gov/study/NCT02731612) | Phase 3 | 完成 | 100 | 6 週雙盲安慰劑對照：輔助治療改善緩解期雙相患者認知功能（ELICE-BD） |
| [NCT02147379](https://clinicaltrials.gov/study/NCT02147379) | Phase 3 | 完成 | 53 | 隨機開放標籤：Lurasidone 對比常規治療，改善緩解期雙相 I 型認知功能 |
| [NCT01575561](https://clinicaltrials.gov/study/NCT01575561) | Phase 3 | 完成 | 377 | 12 週開放標籤延伸：Lurasidone 併用鋰鹽或 divalproex 的長期安全性 |
| [NCT01986114](https://clinicaltrials.gov/study/NCT01986114) | Phase 3 | 完成 | 495 | SM-13496 用於雙相 I 型的長期療效與安全性 |
| [NCT01914393](https://clinicaltrials.gov/study/NCT01914393) | Phase 3 | 完成 | 702 | 104 週開放標籤延伸：兒童與青少年長期安全性與療效 |
| [NCT04383691](https://clinicaltrials.gov/study/NCT04383691) | Phase 3 | 提前終止 | 124 | 6 週安慰劑對照：雙相 I 型憂鬱，因提前終止而解讀受限 |
| [NCT06433635](https://clinicaltrials.gov/study/NCT06433635) | Phase 4 | 進行中（不再招募） | 2726 | 序貫多重分派隨機試驗：比較 Lurasidone 等四種雙相憂鬱治療 |

注意：上表沒有任何以急性躁狂為主要終點的完成試驗。唯一針對躁狂的 [NCT01932541](https://clinicaltrials.gov/study/NCT01932541)（兒童與青少年躁狂）已撤銷，入組人數為 0。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39557452](https://pubmed.ncbi.nlm.nih.gov/39557452/) | 2024 | 系統性回顧與劑量反應統合分析 | BMJ Mental Health | 探討 Lurasidone 用於雙相憂鬱的最佳劑量、療效、可接受性與代謝/內分泌影響 |
| [37595997](https://pubmed.ncbi.nlm.nih.gov/37595997/) | 2023 | 網絡統合分析 | Lancet Psychiatry | 比較急性雙相憂鬱各種藥物的療效與耐受性 |
| [38487836](https://pubmed.ncbi.nlm.nih.gov/38487836/) | 2024 | 網絡統合分析 | European Psychiatry | 比較 5 種 FDA 核准非典型抗精神病藥（含 Lurasidone）用於雙相憂鬱，納入 16 項 RCT |
| [33177610](https://pubmed.ncbi.nlm.nih.gov/33177610/) | 2021 | 系統性回顧與網絡統合分析 | Molecular Psychiatry | 比較抗精神病藥與情緒穩定劑在雙相維持期的效果 |
| [29536616](https://pubmed.ncbi.nlm.nih.gov/29536616/) | 2018 | 臨床指引 | Bipolar Disorders | CANMAT/ISBD 2018 雙相情感障礙處置指引 |
| [34599629](https://pubmed.ncbi.nlm.nih.gov/34599629/) | 2021 | 臨床指引 | Bipolar Disorders | CANMAT/ISBD 雙相情感障礙混合發作處置建議 |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | Review | JAMA | 雙相情感障礙的診斷與治療綜述 |
| [38618207](https://pubmed.ncbi.nlm.nih.gov/38618207/) | 2024 | 網絡統合分析 | EClinicalMedicine | 抗精神病藥與情緒穩定劑對雙相患者代謝的影響 |
| [42580772](https://pubmed.ncbi.nlm.nih.gov/42580772/) | 2026 | 傘式回顧 | BMJ | 各年齡層與情緒階段雙相情感障礙的實證介入 |
| [24170243](https://pubmed.ncbi.nlm.nih.gov/24170243/) | 2014 | 評論 | Am J Psychiatry | Lurasidone 與雙相情感障礙 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64806 | LATUDA TABLETS 40MG | 錠劑（依品名） | 資料未載明 |
| HK-64804 | LATUDA TABLETS 80MG | 錠劑（依品名） | 資料未載明 |
| HK-67186 | LATUDA TABLETS 20MG | 錠劑（依品名） | 資料未載明 |

三張許可證的持有廠商皆為 DKSH Hong Kong Limited。

## 安全性考量

現有資料中沒有警語、禁忌症與藥物交互作用的內容（DDI 查詢無結果），請參考原廠仿單。

依機轉與文獻，若推進評估，建議納入以下監測：
- **代謝監測**：抗精神病藥有體重增加與代謝影響的文獻證據
- **錐體外症狀（EPS）監測**
- **CYP3A4 交互作用審查**

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個完成的 Phase 3 RCT（含 965 人的鋰鹽/valproate 輔助預防復發試驗），證明 Lurasidone 在雙相情感障礙有實質臨床證據，且香港已有 3 張許可證上市。
- 但證據集中在雙相憂鬱與維持期，缺乏急性躁狂的直接證據，推進時必須限縮範圍並補足資料。

**若要推進需要：**
- 取得香港衛生署仿單（警語與禁忌症，此為阻斷性缺口）
- 確認 Lurasidone 現行核准適應症，並判斷「躁狂」是否為實際要評估的目標
- 尋找以急性躁狂為主要終點的試驗證據
- 補齊 DrugBank 作用機轉資料
- 建立代謝與錐體外症狀監測計畫，並審查 CYP3A4 交互作用

**其他預測適應症：** 排名 2–10 的預測（如視網膜失養症、無腦回畸形、近視相關疾病、Charcot-Marie-Tooth 病等）皆僅有模型預測，沒有臨床試驗或相關文獻，機轉上也無合理連結，證據等級為 L5，建議 Hold。

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

