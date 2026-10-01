---
layout: default
title: Triazolam
parent: 中證據等級 (L3-L4)
nav_order: 890
evidence_level: L3
indication_count: 1
---

# Triazolam
{: .fs-9 }

證據等級: **L3** | 預測適應症: **1** 個
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

# Triazolam：從原適應症（資料未登載）到入睡與維持睡眠障礙（失眠）

## 一句話總結

Triazolam 是短效的苯二氮平類（benzodiazepine）鎮靜安眠藥，本次提供的資料未登載原適應症。
TxGNN 模型預測它可能對**入睡與維持睡眠障礙（Sleep disorder, initiating and maintaining sleep）**有效，
目前**無登記的臨床試驗**，但有 **19 篇文獻**（含 1 份臨床指引、2 篇系統性回顧）支持這個方向。
這很可能是已知的標示內用途，而非真正的老藥新用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 入睡與維持睡眠障礙（失眠） |
| TxGNN 預測分數 | 99.72% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。依一般藥理知識（非來自本次資料），Triazolam 是 GABA-A 受體苯二氮平結合位的正向異位調節劑。它會增加氯離子通道開啟頻率，產生中樞抑制與鎮靜作用，與入睡困難及睡眠維持困難的病理相符。

文獻也把 Triazolam 歸為短效安眠藥，用於失眠的短期治療。因此 TxGNN 的高分（99.72%）與已確立的藥物與疾病關係一致。原適應症欄位為空，較可能是資料品質缺漏，需對照香港衛生署核准的仿單確認。

文獻同時指出，這類藥物在長者有跌倒、認知受損、依賴與隔日鎮靜等風險。停藥後也可能出現反彈性失眠（rebound insomnia）。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | 臨床指引 | J Clin Sleep Med | 美國睡眠醫學會針對個別藥物制定的成人慢性失眠藥物治療建議 |
| [40110890](https://pubmed.ncbi.nlm.nih.gov/40110890/) | 2025 | 系統性回顧／統合分析 | Psychiatry Clin Neurosci | 比較各類安眠藥（含苯二氮平類）併用抗憂鬱劑，治療合併失眠的重度憂鬱症之療效與安全性 |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | 系統性回顧／網絡統合分析 | Sleep | 比較各種安眠藥用於長者失眠的療效與安全性 |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs Aging | 長者失眠的藥物治療建議；行為療法為首選，必要時搭配藥物 |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | 回顧長者使用安眠藥的安全性與療效，指出藥動學可能改變 |
| [9161660](https://pubmed.ncbi.nlm.nih.gov/9161660/) | 1997 | Review | Ann Pharmacother | 比較 Zolpidem 與 Triazolam 的療效與安全性 |
| [8573298](https://pubmed.ncbi.nlm.nih.gov/8573298/) | 1995 | Review | Drug Saf | 短效安眠藥評估 |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Review | J Clin Psychopharmacol | 回顧睡眠實驗室研究，指出停用 Triazolam 後可能出現反彈性失眠 |
| [19682231](https://pubmed.ncbi.nlm.nih.gov/19682231/) | 2010 | 人體研究 | J Sleep Res | 探討 Triazolam 與 Zolpidem 對睡眠相關動作學習的影響 |
| [1319429](https://pubmed.ncbi.nlm.nih.gov/1319429/) | 1992 | Review | J Clin Psychiatry | 苯二氮平類安眠藥的藥理學，說明 Triazolam 屬短半衰期藥物 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-00495 | HALCION TAB 0.25 MG（廠商：PFIZER CORPORATION HONG KONG LIMITED） | 未登載 | 未登載 |

## 安全性考量

安全性資訊請參考原廠仿單。

另依文獻提示，長者使用此類藥物須特別留意跌倒、認知受損、依賴與隔日鎮靜；停藥後可能出現反彈性失眠。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- TxGNN 分數很高，文獻以臨床指引與系統性回顧為主，方向一致，且該藥已在香港上市。
- 但沒有登記的臨床試驗，仿單、原適應症與作用機轉資料也缺漏，證據上限為 L3。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌，並補齊原適應症欄位。
- 確認上述系統性回顧與指引是否納入 Triazolam 的 RCT，若有，可考慮將證據等級上調至 L2 或 L1。
- 從 DrugBank 補齊作用機轉資料。
- 建立使用規範：短期使用、最低有效劑量，長者須加強風險評估。

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

