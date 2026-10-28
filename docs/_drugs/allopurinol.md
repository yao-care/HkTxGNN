---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
monitor_inn: "ALLOPURINOL"
predicted_indications: ["hepatic porphyria", "hepatoportal sclerosis", "early-onset familial noncirrhotic portal hypertension", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "inflammatory myopathy with abundant macrophages"]
last_modified_at: 2026-10-28
description: "Allopurinol：預測新適應症為肝性紫質症（證據等級 L5）。原適應症：痛風、高尿酸血症、急性尿酸腎病變"
---

# Allopurinol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Allopurinol：從痛風到肝性紫質症
{: .text-alpha }

## 一句話總結

Allopurinol 是黃嘌呤氧化酶抑制劑類藥物，知識圖譜中記錄的使用方向為痛風、高尿酸血症與急性尿酸腎病變。
TxGNN 模型預測它可能對**肝性紫質症 (Hepatic Porphyria)** 有效，但目前**沒有臨床試驗**，僅有 **2 篇間接文獻**（一篇假說、一篇大鼠前臨床研究），證據非常有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 痛風、高尿酸血症、急性尿酸腎病變（知識圖譜中記錄的關係；香港許可證資料未提供適應症文字） |
| 預測新適應症 | 肝性紫質症 |
| TxGNN 預測分數 | 0.9995 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Allopurinol 一般已知為黃嘌呤氧化酶抑制劑，用於降低尿酸，但本次整理的資料並未收錄此機轉。

在機轉上，較早期的前臨床研究曾提到，allopurinol 可能影響大鼠肝臟的血基質（heme）代謝，並調節 ALA 合成酶活性。ALAS1 被誘導是急性肝性紫質症中紫質前驅物堆積的關鍵，因此這是一個合理但間接的連結。

不過，作用方向並不明確：allopurinol 在某些情境下也被視為可能與紫質症惡化相關。目前沒有任何人體資料顯示它有益，因此這個預測應視為假說，而非有實證的療效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | 假說／回顧 | Medical Hypotheses | 提出以色胺酸或抑制色胺酸 2,3-雙加氧酶利用血基質，來針對 ALA 合成酶進行代謝調控，作為急性肝性紫質症的潛在療法；未直接研究 allopurinol |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | 前臨床（大鼠） | Biochemical Pharmacology | 探討 carbamazepine 對大鼠肝臟血基質代謝的影響及其加重肝性紫質症的機轉；未直接研究 allopurinol |

上述文獻皆未直接以 allopurinol 治療肝性紫質症為研究對象，因此證據等級維持 L5。

## 香港上市資訊

資料顯示 allopurinol 在香港為已上市的單一成分藥品，目前整理到 20 張有效許可證（實際數量可能更多）。以下列出 5 張主要許可證，所提供資料中皆無核准適應症與劑型文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-35846 | ALLOPURINOL TAB 100MG（HOVID） | 錠劑（100 mg） | 資料未提供 |
| HK-66571 | ALLOPURINOL TCK TABLETS 100MG | 錠劑（100 mg） | 資料未提供 |
| HK-21594 | SYNPURINOL TAB 100MG | 錠劑（100 mg） | 資料未提供 |
| HK-33568 | APO-ALLOPURINOL TAB 300MG | 錠劑（300 mg） | 資料未提供 |
| HK-10041 | ZYLORIC 300 TAB 300MG | 錠劑（300 mg） | 資料未提供 |

## 安全性考量

- **知識圖譜記錄的禁忌關係**（非仿單內容）：肝臟疾病、膽囊疾病、腎功能不全、過敏性血管炎、皮膚白血球破裂性血管炎、過敏性皮膚血管炎、抗腎絲球基底膜疾病。
- **藥物交互作用**：共查詢到 100 筆，以下為已列出者中屬中度的項目：
  - Aluminum hydroxide
  - Attapulgite
  - Kaolin
  - Magaldrate
  - Sucralfate

  Amoxicillin、Chlorpropamide 為輕度；其餘多數（如 metformin、omeprazole、morphine 等）分級未知。

另外，預測新適應症為肝性紫質症，而知識圖譜中已記錄肝臟疾病為禁忌關係，使用前須特別審慎。其他安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有臨床試驗，也沒有直接研究 allopurinol 與肝性紫質症的文獻，僅屬 L5 的模型預測。
- 作用方向不明（可能有益，也可能加重紫質症），且知識圖譜記錄肝臟疾病為禁忌關係。

**若要推進需要：**
- 補齊 allopurinol 的作用機轉資料
- 取得香港仿單的警語與禁忌資料
- 進行針對 allopurinol 與血基質／ALAS1 代謝的專門前臨床研究，釐清作用方向
- 評估對紫質症病人的安全性，再考慮是否進入臨床研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

