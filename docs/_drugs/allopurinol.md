---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Allopurinol：預測新適應症為肝性卟啉症 (Hepatic Porphyria)（證據等級 L5）。原適應症：痛風、高尿酸血症、急性尿酸腎病變"
monitor_inn: "ALLOPURINOL"
predicted_indications: ["hepatic porphyria", "hepatoportal sclerosis", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "primitive portal vein thrombosis", "early-onset familial noncirrhotic portal hypertension", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "idiopathic eosinophilic myositis"]
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

# Allopurinol：從痛風到肝性卟啉症

## 一句話總結

Allopurinol 是黃嘌呤氧化酶（xanthine oxidase）抑制劑，原本用於痛風、高尿酸血症與急性尿酸腎病變。
TxGNN 模型預測它可能對**肝性卟啉症 (Hepatic Porphyria)** 有效，但目前**沒有臨床試驗**，僅有 **2 篇間接文獻**（一篇假說論文、一篇大鼠研究），證據非常薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 痛風、高尿酸血症、急性尿酸腎病變 |
| 預測新適應症 | 肝性卟啉症 (Hepatic Porphyria) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Allopurinol 是黃嘌呤氧化酶抑制劑，透過減少尿酸生成來治療痛風與高尿酸血症。

與肝性卟啉症可能的關聯在於血基質（heme）代謝。有文獻指出 Allopurinol 可能影響肝臟血基質代謝，也有報告提到它會降解肝臟細胞色素 P450 的血基質，理論上可能改變 5-胺基乙醯丙酸合成酶（ALA synthase）的調控。一篇 2019 年的假說論文也提出，以代謝方式調控 ALA synthase 可能成為急性肝性卟啉症的治療方向。

不過，方向性並不確定。Allopurinol 在某些情境下反而被視為可能誘發卟啉症的藥物，因此它可能加重而非改善病情。這項預測目前較像是圖譜相似性的結果，缺乏直接的臨床資料支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | 假說/回顧 | Medical Hypotheses | 提出以色胺酸或抑制色胺酸 2,3-雙加氧酶利用血基質，來調控肝臟 ALA synthase，作為急性肝性卟啉症的潛在療法（非 Allopurinol 直接研究） |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | 動物研究（大鼠） | Biochemical Pharmacology | 研究 carbamazepine 對大鼠肝臟血基質代謝的影響，探討其加重肝性卟啉症的機轉（非 Allopurinol 直接研究） |

兩篇文獻都沒有直接檢驗 Allopurinol 對卟啉症患者的療效。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-35846 | ALLOPURINOL TAB 100MG | — | — |
| HK-66571 | ALLOPURINOL TCK TABLETS 100MG | — | — |
| HK-21594 | SYNPURINOL TAB 100MG | — | — |
| HK-30121 | ALLOPURINOL TAB 100MG | — | — |
| HK-52620 | SYNORID TAB 100MG | — | — |

共 20 張有效單方許可證，此處僅列出前 5 張；目前整理的資料中未包含劑型與核准適應症文字。

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（來自知識圖譜，非仿單文字）：肝臟疾病、膽囊疾病、腎功能不全、過敏性血管炎（含皮膚白血球破碎性血管炎、過敏性皮膚血管炎）、抗腎絲球基底膜疾病。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 中度：氫氧化鋁（Aluminum hydroxide）、Attapulgite、高嶺土（Kaolin）、Magaldrate、Sucralfate
  - 輕度：Amoxicillin、Chlorpropamide
  - 其他（等級未知）：Metformin、Omeprazole、Pantoprazole、Glimepiride、Doxycycline、Morphine 等
- 針對本次預測適應症，Allopurinol 本身可能被視為卟啉症的潛在誘發因子，使用上須特別謹慎。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，僅有一篇假說論文與一篇大鼠研究（且皆非直接針對 Allopurinol），屬於 L5 等級的模型預測。
- 機轉方向不明，Allopurinol 在某些情境下可能加重卟啉症，安全疑慮大於潛在效益。

**若要推進需要：**
- 取得詳細的作用機轉資料，釐清 Allopurinol 對血基質合成與 ALA synthase 的實際影響方向
- 進行前臨床研究，確認它在卟啉症模型中是改善還是誘發病情
- 取得香港仿單的警語與禁忌資料，完成安全性篩選
- 評估是否有病例報告或登錄資料，說明卟啉症患者使用 Allopurinol 的實際經驗
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

