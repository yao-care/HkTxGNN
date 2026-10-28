---
layout: default
title: Pinazepam
parent: 僅模型預測 (L5)
nav_order: 700
evidence_level: L5
indication_count: 7
monitor_inn: "PINAZEPAM"
predicted_indications: ["insomnia (disease)", "alcohol withdrawal delirium", "antidepressant type abuse", "hallucinogen abuse", "barbiturate abuse", "anxiety", "sleep disorder, initiating and maintaining sleep"]
last_modified_at: 2026-10-23
description: "Pinazepam：預測新適應症為失眠 (Insomnia)（證據等級 L5）。原適應症：香港許可證未載明核准適應症"
---

# Pinazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Pinazepam：從焦慮症到失眠
{: .text-alpha }

## 一句話總結

Pinazepam 是一種 1,4-苯二氮平類（benzodiazepine）藥物，也是 N-desmethyldiazepam（nordazepam）的前驅藥物，一般作為抗焦慮藥使用。
TxGNN 模型預測它可能對**失眠 (Insomnia)** 有效，但目前**沒有任何臨床試驗或文獻**直接研究此適應症，證據僅來自模型預測與藥物類別推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症 |
| 預測新適應症 | 失眠 (Insomnia) |
| TxGNN 預測分數 | 0.9995 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Pinazepam 是苯二氮平類藥物，進入體內後轉換為活性代謝物 N-desmethyldiazepam。該代謝物是 GABA-A 受體的正向異位調節劑，可產生抗焦慮與鎮靜作用，因此在機轉上與助眠有合理的關聯。

不過，這個預測分數很高，主要反映的是它與其他苯二氮平類藥物的類別相似性，而非 pinazepam 本身的臨床證據。此外，活性代謝物半衰期長，可能造成隔日鎮靜，若要作為助眠藥使用，需要另外評估。

另有兩項相關預測：「睡眠障礙（入睡及維持睡眠困難）」與失眠本質上是同一個臨床概念，同樣沒有直接研究支持。

目前缺乏詳細的作用機轉（MOA）資料，以上說明是依苯二氮平類別與代謝物特性所作的推論。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對失眠本身，**目前無相關文獻**。

以下是與 pinazepam 相關、被歸在「焦慮」預測項下的文獻（並非直接研究失眠），僅供背景參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [6147192](https://pubmed.ncbi.nlm.nih.gov/6147192/) | 1984 | Review | Clinical Therapeutics | 回顧 pinazepam 的藥理特性與療效；其特點是 N-1 位置的 propargyl 基團，毒性低於 diazepam，動物實驗中可控制焦慮與攻擊行為，催眠效果與運動協調損害較低 |
| [240369](https://pubmed.ncbi.nlm.nih.gov/240369/) | 1975 | 前臨床毒理／藥理 | Arzneimittel-Forschung | 與 diazepam 相比，pinazepam 毒性、催眠與肌肉鬆弛作用較低 |
| [26359](https://pubmed.ncbi.nlm.nih.gov/26359/) | 1978 | 前臨床藥理 | Arzneimittel-Forschung | 在大鼠條件性情緒反應試驗中，pinazepam 的活性超過 diazepam 的兩倍 |
| [6809477](https://pubmed.ncbi.nlm.nih.gov/6809477/) | 1982 | 藥物動力學 | Eur J Clin Pharmacol | 6 名健康男性口服 10 mg，確認 pinazepam 為 N-desmethyldiazepam 的前驅藥物 |
| [6147314](https://pubmed.ncbi.nlm.nih.gov/6147314/) | 1983 | 藥物動力學 | Int J Clin Pharmacol Res | 健康受試者單次口服 10 mg 的藥動學，符合二室模型 |
| [6150857](https://pubmed.ncbi.nlm.nih.gov/6150857/) | 1984 | 藥物動力學 | Eur J Clin Pharmacol | 25 名足月孕婦的胎盤transfer研究 |

值得注意的是，這些文獻以前臨床與藥動學研究為主，其中一項 1975 年的研究指出 pinazepam 的催眠活性低於 diazepam，這對助眠用途並不有利。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-32129 | DOMAR CAP 5MG | 未載明 | 未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

另外，從藥物類別來看，苯二氮平類具有依賴與濫用風險，且 pinazepam 的長效活性代謝物可能造成隔日鎮靜。這是依類別特性所作的提醒，並非來自許可證仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 失眠的預測僅來自模型與苯二氮平類別推論，沒有直接研究，證據等級為 L5。
- 現有文獻顯示 pinazepam 的催眠活性較 diazepam 低，且長效代謝物有隔日鎮靜的疑慮，目前不足以支持推進。

**若要推進需要：**
- 取得香港仿單，確認核准適應症、警語與禁忌症
- 補充詳細的作用機轉資料
- 檢視 1984 年綜述（PMID 6147192）中的臨床療效資料
- 針對失眠進行臨床試驗或系統性文獻搜尋，並評估隔日鎮靜與依賴風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

