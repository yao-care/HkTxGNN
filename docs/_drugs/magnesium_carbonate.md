---
layout: default
title: Magnesium Carbonate
parent: 高證據等級 (L1-L2)
nav_order: 469
evidence_level: L2
indication_count: 5
---

# Magnesium Carbonate
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Magnesium Carbonate：從制酸劑到活動性消化性潰瘍

## 一句話總結

Magnesium Carbonate（碳酸鎂，DB09481）為傳統鹼性制酸劑，原始適應症資料目前缺失（DrugBank 未收錄）。
TxGNN 模型預測它可能對**活動性消化性潰瘍 (Active Peptic Ulcer Disease)** 有效，
目前無相關臨床試驗登記，但有 **4 篇文獻**（含 2 篇 RCT）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 活動性消化性潰瘍 (Active Peptic Ulcer Disease) |
| TxGNN 預測分數 | 99.96%（排名第 1180） |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。根據現有證據，Magnesium Carbonate 屬於鹼性制酸劑（antacid）類別，其藥理特性是中和胃酸、提升胃內 pH 值，並降低胃蛋白酶活性。

這正是活動性消化性潰瘍傳統的對症與輔助治療機轉——藉由降低酸性刺激，減少對潰瘍面的持續傷害，進而促進黏膜癒合。早期的雙盲臨床試驗已直接驗證制酸劑類藥物對十二指腸與前幽門潰瘍的癒合效果，機轉上與 TxGNN 的預測方向一致。

需注意的是，現有文獻多以複方制酸劑（如 antacid suspension、Caved-S 等）而非碳酸鎂單方進行測試，機轉上可外推但仍屬於藥物類別層級的證據，而非碳酸鎂單一成分的直接驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7034155](https://pubmed.ncbi.nlm.nih.gov/7034155/) | 1981 | RCT | Scandinavian Journal of Gastroenterology | 制酸劑/抗膽鹼藥 vs cimetidine vs 安慰劑治療活動性十二指腸／前幽門潰瘍，3 週癒合率制酸劑組 50%、cimetidine 組 67%（皆優於安慰劑，p<0.005） |
| [6755656](https://pubmed.ncbi.nlm.nih.gov/6755656/) | 1982 | RCT | Scand J Gastroenterol Suppl | 同系列研究，制酸劑/抗膽鹼藥、cimetidine、安慰劑治療前幽門與十二指腸潰瘍 |
| [3003883](https://pubmed.ncbi.nlm.nih.gov/3003883/) | 1985 | RCT | Scandinavian Journal of Gastroenterology | 高纖維飲食合併制酸劑治療活動性十二指腸潰瘍，4 週癒合率高纖組 67.5% vs 低纖組 60%（無顯著差異），顯示制酸劑本身有效性 |
| [35720246](https://pubmed.ncbi.nlm.nih.gov/35720246/) | 2022 | In-vitro | Medicine and Pharmacy Reports | 評估摩洛哥市售制酸劑之酸中和能力（ANC）等藥學特性 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
制酸劑類藥物於活動性消化性潰瘍已有多個早期雙盲 RCT 支持療效，機轉合理且明確；但碳酸鎂單方缺乏直接臨床試驗證據，且香港未上市、MOA 與安全性資料皆屬缺口，須謹慎推進。

**若要推進需要：**
- 補齊作用機轉（MOA）資料
- 取得原廠仿單警語、禁忌症與藥物交互作用資料（目前為 Blocking 缺口，無法進入安全性初評）
- 確認碳酸鎂單方（非複方）在消化性潰瘍的直接臨床證據
- 評估香港上市可行性（目前無許可證登記）

---

### 附：其他 TxGNN 預測適應症（供研究參考）

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|------|-----------|---------|---------|------|
| 1 | 活動性消化性潰瘍 | 99.96% | L2 | S3 | Proceed with Guardrails |
| 2 | 消化性潰瘍穿孔 | 99.95% | L5 | S0 | Hold（外科急症，機轉不適用） |
| 3 | 胃空腸吻合口潰瘍 | 99.95% | L3 | S1 | Research Question |
| 4 | 胃十二指腸炎 | 99.94% | L4 | S1 | Research Question |
| 5 | 胃潰瘍 | 99.82% | L2 | S3 | Proceed with Guardrails |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

