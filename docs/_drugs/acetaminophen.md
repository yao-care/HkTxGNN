---
layout: default
title: Acetaminophen
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 1
---

# Acetaminophen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Acetaminophen：從解熱鎮痛到伴腦幹先兆偏頭痛

## 一句話總結

Acetaminophen（乙醯胺酚，即 paracetamol）是常見的解熱鎮痛成分，在香港已有多張許可證。
TxGNN 模型預測它可能對**伴腦幹先兆偏頭痛 (Migraine with Brainstem Aura)** 有效。
目前**沒有臨床試驗登記**，有 **20 篇文獻**，但都是一般偏頭痛的間接證據，沒有針對此亞型的直接研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 伴腦幹先兆偏頭痛 (Migraine with Brainstem Aura) |
| TxGNN 預測分數 | 99.15% |
| 證據等級 | L3（僅有一般偏頭痛的系統性證據評估與回顧，無此亞型的直接證據；資料包原標示為 L4） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Acetaminophen 是已確立的急性偏頭痛止痛藥。一般認為其中樞鎮痛作用可能涉及 COX 抑制，以及血清素與大麻素路徑的調節，但這些機轉在本資料包中沒有 DrugBank 資料可佐證。

文獻顯示，acetaminophen 被美國頭痛學會的急性偏頭痛治療證據評估納入討論，也被建議為孕期頭痛的一線症狀治療。這些證據都來自一般偏頭痛。伴腦幹先兆偏頭痛是偏頭痛的亞型，因此機轉上可能適用，但沒有此亞型的直接研究。

要注意兩點：
- 0.99 的分數是模型預測，不是臨床證據。
- Acetaminophen 本來就用於偏頭痛，這可能不算真正的老藥新用。原適應症欄位為空，較可能是資料缺漏。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

RCT 類型依論文標題判斷。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11112243](https://pubmed.ncbi.nlm.nih.gov/11112243/) | 2000 | RCT | Archives of Internal Medicine | 以隨機、雙盲、安慰劑對照的族群研究，評估 acetaminophen 治療偏頭痛的療效與安全性 |
| [9482363](https://pubmed.ncbi.nlm.nih.gov/9482363/) | 1998 | RCT | Archives of Neurology | 三項雙盲、隨機、安慰劑對照試驗，評估 acetaminophen + aspirin + caffeine 複方緩解偏頭痛疼痛的效果 |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | RCT | Clinical Therapeutics | 綜合三項隨機安慰劑對照試驗，比較同一複方對經期相關偏頭痛與非經期偏頭痛的效果 |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | 指引／系統性證據評估 | Headache | 美國頭痛學會更新急性偏頭痛各種藥物治療的證據評估 |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handbook of Clinical Neurology | 偏頭痛持續狀態（發作超過 72 小時）的定義、負擔與病例系列回顧 |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Review | Neurologic Clinics | 孕期與產褥期頭痛，指出 acetaminophen 為一線症狀治療 |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | Cureus | 孕期與哺乳期偏頭痛的關聯與治療方式 |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Review | Cureus | 孕期偏頭痛的急性與預防性治療回顧 |
| [16018227](https://pubmed.ncbi.nlm.nih.gov/16018227/) | 2005 | Review | Pediatric Annals | 兒童偏頭痛的急性與預防性治療策略 |
| [27993427](https://pubmed.ncbi.nlm.nih.gov/27993427/) | 2017 | Review | Brain & Development | 兒童偏頭痛的診斷與治療實務回顧 |

## 香港上市資訊

資料包共列出 20 張許可證，以下為其中 5 張。劑型與核准適應症欄位在資料中為空白。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-64902 | PARCEMOL PLAIN TAB 500MG (BLUE) | NEOCHEM PHARMACEUTICAL LABORATORIES LTD. |
| HK-64351 | PARACETAMOL ORAL SUSPENSION 250MG/5ML | BRIGHT FUTURE PHARMACEUTICALS FACTORY |
| HK-64150 | ROTER DISSOLVABLE PARACETAMOL GRANULES 500MG | COOPER CONSUMER HEALTH HK LIMITED |
| HK-67265 | HOVID PARACETAMOL ORAL SUSPENSION SUGAR FREE 250MG/5ML | HOVID LIMITED |
| HK-42035 | ENDOPAIN SUSP FOR CHILDREN 125MG/5ML | MEDIPHARMA LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 現有證據都是一般偏頭痛的間接證據，沒有臨床試驗，也沒有針對伴腦幹先兆亞型的研究。
- 香港衛生署仿單的警語與禁忌資料缺漏，屬阻擋性缺口，無法進入安全性篩選。
- 目前只能視為研究問題。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌症、核准適應症），補齊安全性資料。
- 從 DrugBank 補上作用機轉（MOA）。
- 確認原適應症與這是否算真正的老藥新用。
- 搜尋伴腦幹先兆偏頭痛的專門文獻，或評估是否可從一般偏頭痛的證據外推。

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

