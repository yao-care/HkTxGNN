---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 42
evidence_level: L5
indication_count: 3
monitor_inn: "ALPRAZOLAM"
predicted_indications: ["insomnia (disease)", "benign paroxysmal torticollis of infancy", "agoraphobia"]
last_modified_at: 2026-10-27
description: "Alprazolam：預測新適應症為失眠 (insomnia (disease))（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Alprazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Alprazolam：苯二氮平類 GABA-A 受體調節劑 → 失眠 (insomnia (disease))
{: .text-alpha }

## 一句話總結

Alprazolam 是苯二氮平類（benzodiazepine）藥物，在香港已有多張單方許可證上市。
TxGNN 模型預測它可能對**失眠 (insomnia (disease))** 有效，
但目前**沒有臨床試驗**登記，檢索到的文獻也多為間接證據，尚無直接以 alprazolam 治療失眠的對照試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 失眠 (insomnia (disease)) |
| TxGNN 預測分數 | 0.9981 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 14 張／共 14 張） |
| 許可證數 | 14 張（有效 14 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥物類別推論，alprazolam 屬於苯二氮平類，會增強 GABA-A 受體訊號，產生鎮靜與抗焦慮作用。這與失眠，尤其是合併焦慮的失眠，在機轉上有合理的連結。

不過這個連結是由藥物類別推論而來，並非來自已驗證的機轉資料。檢索到的文獻多為恐慌症回顧、苯二氮平使用量與經濟負擔、藥物動力學，以及 zolpidem 的減量研究，沒有任何一篇是針對 alprazolam 治療失眠的對照試驗。因此，0.9981 的分數僅代表模型的計算結果，不能視為療效證據。

另一方面，苯二氮平類的已知風險（依賴性、跌倒、認知受損）以及 100 筆已記錄的藥物交互作用，都是在沒有直接證據下不宜貿然推進的理由。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下列文獻與失眠的關聯多屬間接，並非直接研究 alprazolam 治療失眠的療效。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | 回溯性臨床研究 | Medicine | 督脈灸合併耳針與 alprazolam，用於冠心病合併失眠患者（116 人），觀察心功能與神經傳導物質變化；alprazolam 為對照組用藥，屬複合療法研究 |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | 橫斷面研究 | Medicine | 調查 COVID-19 康復者的失眠情形與影響因素，與 alprazolam 無直接關聯 |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | 統合分析 | Acta Pharm | 評估鎮靜劑用於老年慢性病患者的劑量、療效與不良反應 |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | 回顧 | Expert Opin Drug Metab Toxicol | 抗焦慮藥物的藥物動力學回顧 |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | 預測／經濟模型 | Value Health Reg Issues | 克羅埃西亞苯二氮平使用趨勢與經濟負擔；長期使用與記憶減退、依賴、跌倒相關 |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | 動物研究 | Aging | 小鼠反覆給予 alprazolam 造成粒線體功能失調及海馬依賴性記憶鞏固減弱 |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | 處方模式研究 | Sleep Med | 分析大型管理式醫療人群中失眠的處方特徵 |

## 香港上市資訊

香港共有 14 張單方許可證，皆為有效狀態，主要品牌包括 XANAX、ALPRAX、ZOLARAM 等。以下列出 5 張主要許可證，其餘未列出。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-17668 | XANAX TAB 0.5MG | 錠劑 | 本地資料未記載 |
| HK-17669 | XANAX TAB 0.25MG | 錠劑 | 本地資料未記載 |
| HK-51647 | ALPRAX 0.5 TAB 0.5MG | 錠劑 | 本地資料未記載 |
| HK-55271 | ZOLARAM 0.5 TAB 0.5MG | 錠劑 | 本地資料未記載 |
| HK-56775 | VICK-ALPRAZOLAM TAB 0.5MG | 錠劑 | 本地資料未記載 |

## 安全性考量

- **藥物交互作用**：共記錄 100 筆交互作用，其中最嚴重的為 Major 等級，包括與 Morphine 及 Morphine (liposomal) 併用（中樞神經與呼吸抑制風險）。Moderate 等級的包括 Aprepitant、Bupropion、Cimetidine、Clarithromycin、Clotrimazole、Dronabinol、Metoclopramide、Miconazole 等。抗酸劑（如氫氧化鋁、碳酸鈣、氧化鎂）及部分類固醇（如 Betamethasone、Dexamethasone）為 Minor 等級。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何直接研究 alprazolam 治療失眠的臨床試驗或文獻，證據僅停留在模型預測與藥物類別推論（L5）。
- 苯二氮平類的依賴、跌倒、認知受損風險，以及大量的藥物交互作用，使得在缺乏直接證據下不宜推進。

**若要推進需要：**
- 直接比較 alprazolam 與安慰劑或現行失眠標準治療的對照試驗（RCT）
- 取得完整的作用機轉資料與原廠仿單中的警語、禁忌症
- 針對老年人、肝腎功能不全者及併用鴉片類藥物者制定安全性監測計畫
- 釐清相對於現有失眠藥物，alprazolam 的使用定位與風險效益
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

