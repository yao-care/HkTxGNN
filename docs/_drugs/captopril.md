---
layout: default
title: Captopril
parent: 僅模型預測 (L5)
nav_order: 156
evidence_level: L5
indication_count: 3
monitor_inn: "CAPTOPRIL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
last_modified_at: 2026-10-27
description: "Captopril：預測新適應症為惡性高血壓性腎病 (malignant hypertensive renal disease)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Captopril
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

## Captopril：血管收縮素轉換酶抑制劑 → 惡性高血壓性腎病 (malignant hypertensive renal disease)
{: .text-alpha }

## 一句話總結

Captopril 是一種血管收縮素轉換酶（ACE）抑制劑，屬降血壓類藥物。
TxGNN 模型預測它可能對**惡性高血壓性腎病 (malignant hypertensive renal disease)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇文獻**（為診斷用途的病例報告），證據相當有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 惡性高血壓性腎病 (malignant hypertensive renal disease) |
| TxGNN 預測分數 | 0.9928 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 12 張／共 12 張） |
| 許可證數 | 12 張（有效 12 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知的藥物類別而言，Captopril 是 ACE 抑制劑，可減少血管收縮素 II 所媒介的血管收縮與醛固酮分泌。

惡性高血壓合併腎臟受損，與腎素—血管收縮素系統（RAS）過度活化密切相關，因此從機轉上看，ACE 抑制劑用於此病在生物學上是合理的。

不過，目前取得的唯一文獻是一例以 Captopril 腎圖進行診斷的病例報告，患者最終是腎細胞癌，並非惡性高血壓性腎病，也沒有提供治療效果的證據。此外，ACE 抑制劑用於高血壓合併腎功能不全的患者時，有急性腎損傷與高血鉀的風險，雙側腎動脈狹窄者尤需注意。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28902735](https://pubmed.ncbi.nlm.nih.gov/28902735/) | 2017 | 病例報告 | Clinical Nuclear Medicine | Captopril 腎圖呈陽性，但無腎動脈狹窄，實為巨大嫌色細胞腎細胞癌；腎切除後腎素依賴型高血壓緩解。屬診斷用途，無治療證據 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44589 | CAPRIL TAB 25MG | 未記載 | 未記載 |
| HK-59936 | CAPTOPRIL FARMOZ TAB 50MG | 未記載 | 未記載 |
| HK-36331 | APO-CAPTO TAB 25MG | 未記載 | 未記載 |
| HK-41933 | RILCAPTON TAB 25MG | 未記載 | 未記載 |
| HK-42701 | CAPTOPRIL STADA 25 TAB 25MG | 未記載 | 未記載 |

本地資料共有 12 張有效的單方許可證，此處僅列出 5 張。

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，其中多為中度，例如與糖皮質激素（Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone）、降血糖藥（Metformin、Alogliptin、Canagliflozin、Dapagliflozin、Empagliflozin）、Bupropion、Morphine、阿斯匹靈等併用。制酸劑（氫氧化鋁、碳酸鈣）為輕度。
- **臨床注意**：ACE 抑制劑用於高血壓合併腎功能不全者，需留意急性腎損傷與高血鉀，尤其是雙側腎動脈狹窄的患者。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉上合理且分數很高（0.9928），但沒有任何直接研究此疾病治療效果的臨床試驗或文獻，唯一文獻僅為診斷用途的病例報告，證據等級為 L5。
- 惡性高血壓合併腎功能受損時使用 ACE 抑制劑有腎損傷與高血鉀風險，需先釐清安全性。

**若要推進需要：**
- 針對惡性高血壓性腎病的臨床研究或回溯性世代分析，評估療效與腎功能結果
- 完整的作用機轉資料
- 香港原廠仿單的警語與禁忌症
- 腎功能與血鉀監測方案，以及雙側腎動脈狹窄患者的排除標準
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

