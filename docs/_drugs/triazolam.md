---
layout: default
title: Triazolam
parent: 僅模型預測 (L5)
nav_order: 905
evidence_level: L5
indication_count: 1
---

# Triazolam
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

# Triazolam：從失眠到入睡與維持睡眠障礙

## 一句話總結

Triazolam 是短效型苯二氮平類（benzodiazepine）安眠藥，原本即用於治療失眠。
TxGNN 模型預測它對**入睡與維持睡眠障礙 (Sleep disorder, initiating and maintaining sleep)** 有效，但這與原適應症基本重疊，屬於既有用途的確認，而非真正的新適應症。
目前無臨床試驗登記，有 **20 篇文獻**（含指引與統合分析）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 失眠 (Insomnia) |
| 預測新適應症 | 入睡與維持睡眠障礙 (Sleep disorder, initiating and maintaining sleep) |
| TxGNN 預測分數 | 99.72% |
| 證據等級 | L3（無已完成的 RCT；有系統性回顧、統合分析與指引） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉登錄資料。依已知藥理，Triazolam 是短效型苯二氮平類藥物，作為 GABA-A 受體的正向異位調節劑，增強抑制性神經傳導，進而促進入睡。

失眠的核心特徵就是難以入睡與難以維持睡眠，因此預測的疾病與原適應症在臨床上幾乎是同一件事。TxGNN 給出高分（99.72%）與此一致。也就是說，這個預測是對既有用途的確認，不是新的藥物再利用方向。

需注意 Triazolam 半衰期短，效益主要在入睡階段，對維持睡眠的支持相對較弱。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

下表依資料中的研究類型排序，優先列出統合分析與指引，其次為回顧。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40110890](https://pubmed.ncbi.nlm.nih.gov/40110890/) | 2025 | 統合分析 | Psychiatry Clin Neurosci | 比較各類安眠藥（含苯二氮平類）與抗憂鬱劑併用於伴失眠的重度憂鬱症之療效與安全性 |
| [27998379](https://pubmed.ncbi.nlm.nih.gov/27998379/) | 2017 | 指引 | J Clin Sleep Med | 美國睡眠醫學會成人慢性失眠藥物治療臨床指引，逐一評估個別藥物 |
| [33249496](https://pubmed.ncbi.nlm.nih.gov/33249496/) | 2021 | 系統性回顧／網絡統合分析 | Sleep | 比較各種安眠藥用於老年失眠的療效與安全性 |
| [38401406](https://pubmed.ncbi.nlm.nih.gov/38401406/) | 2024 | 系統性回顧／網絡統合分析 | Eur Neuropsychopharmacol | 評估安眠藥對隔日駕駛表現的殘留影響 |
| [39932761](https://pubmed.ncbi.nlm.nih.gov/39932761/) | 2025 | Review | Minerva Med | 失眠症概述：盛行率、日間症狀與健康風險 |
| [30058034](https://pubmed.ncbi.nlm.nih.gov/30058034/) | 2018 | Review | Drugs Aging | 老年失眠的藥物治療建議，行為療法為首選 |
| [27751669](https://pubmed.ncbi.nlm.nih.gov/27751669/) | 2016 | Review | Clin Ther | 老年人安眠藥的安全性與療效 |
| [2567741](https://pubmed.ncbi.nlm.nih.gov/2567741/) | 1989 | Review | J Clin Psychopharmacol | 回顧 triazolam 等短半衰期苯二氮平停藥後的反彈性失眠 |
| [9161660](https://pubmed.ncbi.nlm.nih.gov/9161660/) | 1997 | Review | Ann Pharmacother | 比較 zolpidem 與 triazolam 的療效與安全性 |
| [8573298](https://pubmed.ncbi.nlm.nih.gov/8573298/) | 1995 | Review | Drug Saf | 短效安眠藥的評估 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-00495 | HALCION TAB 0.25 MG（輝瑞香港） | 未提供 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎疾病**（來自藥物－疾病關聯，非仿單原文）：焦慮症、精神官能症、輕度憂鬱症（dysthymic disorder）、腎臟疾病、肝臟疾病、膽囊疾病、精神病性疾患、思覺失調樣疾患、情感型思覺失調症、阻塞性睡眠呼吸中止症、睡眠呼吸中止症候群、先天性中樞性低換氣症候群、重症肌無力、神經肌肉接合部疾病、物質相關疾患與物質濫用／依賴。
- **藥物交互作用**：共查得 100 筆。其中 **Morphine 為嚴重（Major）等級**，因中樞神經抑制疊加。中度（Moderate）包括 Clarithromycin、Cimetidine、Omeprazole、Ranitidine、Bupropion、Aprepitant、Metoclopramide、Miconazole、Clotrimazole 等。另有 Dexamethasone、Prednisone、制酸劑等輕微（Minor）交互作用。
- **臨床需留意的風險**：反彈性失眠、耐受性與依賴、隔日殘留作用、老年人跌倒與認知風險，以及與 CYP3A4 抑制劑及中樞神經抑制劑併用的風險。

仿單的警語與禁忌資料尚未取得，正式使用前請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 預測的適應症與原適應症（失眠）實質相同，臨床上已是既有用途，模型分數也很高。但本次資料中無臨床試驗，文獻以回顧、指引與統合分析為主，因此證據等級保守評為 L3。
- 安全性負擔明顯（依賴、反彈性失眠、隔日損害、藥物交互作用多），需設置使用防護。

**若要推進需要：**
- 取得香港衛生署仿單的警語、禁忌與核准適應症全文（目前缺漏，屬阻擋性資料缺口）
- 補充詳細作用機轉資料（如 DrugBank）
- 限定短期使用，並針對老年人制定劑量與跌倒風險管理計畫
- 建立 CYP3A4 抑制劑與中樞神經抑制劑（特別是鴉片類）併用的篩檢與警示機制
- 評估其與非藥物療法（如失眠認知行為治療）及其他安眠藥的比較定位
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

