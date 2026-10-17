---
layout: default
title: Benazepril
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Benazepril：預測新適應症為惡性腎血管性高血壓 (Malignant Renovascular Hypertension)（證據等級 L5）。原適應症：高血壓 (Hypertension)"
monitor_inn: "Benazepril"
predicted_indications: ["malignant hypertensive renal disease"]
---

# Benazepril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Benazepril：從高血壓到惡性腎血管性高血壓

## 一句話總結

Benazepril 是一種血管收縮素轉換酶（ACE）抑制劑，原本用於治療高血壓。
TxGNN 模型預測它可能對**惡性腎血管性高血壓 (Malignant Renovascular Hypertension)** 有效，
但目前**沒有臨床試驗**，也沒有直接相關的文獻支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓 (Hypertension) |
| 預測新適應症 | 惡性腎血管性高血壓 (Malignant Renovascular Hypertension) |
| TxGNN 預測分數 | 99.65% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市（僅見動物用藥許可證） |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Benazepril 屬於 ACE 抑制劑類別，其在高血壓中的療效已被廣泛使用，機轉上可能適用於腎血管性高血壓。

腎血管性高血壓主要由腎素-血管收縮素系統（RAS）過度活化所驅動，而 ACE 抑制劑正是作用於這條路徑，因此在機轉上有合理的對應。不過，ACE 抑制劑在雙側腎動脈狹窄或單一腎臟狹窄的患者，可能造成急性腎功能惡化，需要審慎評估。

必須注意，99.65% 的高分僅是計算預測，很可能反映藥物已有高血壓適應症，以及其在知識圖譜中與相關疾病節點相近，並不代表有臨床證據。

其他預測適應症（同樣為 L5，無臨床證據）：

| 排名 | 預測適應症 | TxGNN 分數 | 建議 |
|------|-----------|-----------|------|
| 2 | 惡性高血壓腎病 (Malignant hypertensive renal disease) | 99.65% | Research Question |
| 3 | 機轉不明的多因素肺高壓 | 99.60% | Hold |
| 4 | 肺部疾病和/或缺氧所致肺高壓 | 99.60% | Hold |
| 5 | Braddock 症候群 | 99.44% | Hold |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對首要預測適應症（惡性腎血管性高血壓），目前無相關文獻。

另外，在排名第 4 的預測適應症（肺部疾病/缺氧所致肺高壓）下檢索到 3 篇文獻，但均為中藥方劑的動物實驗，與 Benazepril 及肺高壓皆無直接關聯，僅視為間接證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38803876](https://pubmed.ncbi.nlm.nih.gov/38803876/) | 2024 | 前臨床 | Heliyon | 加味真武湯透過調節氧化壓力與缺氧反應，延緩慢性腎衰竭進展 |
| [31007700](https://pubmed.ncbi.nlm.nih.gov/31007700/) | 2019 | 前臨床 | eCAM | 當歸芍藥散透過調節缺氧與自噬，改善大鼠腎纖維化 |
| [31317035](https://pubmed.ncbi.nlm.nih.gov/31317035/) | 2019 | 前臨床 | BioMed Res Int | 通心絡抑制內皮間質轉化，減輕大鼠心肌梗塞後心肌纖維化 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59960 | FORTEKOR FLAVOUR TAB 5MG (VET) | — | — |
| HK-59961 | FORTEKOR FLAVOUR TAB 20MG (VET) | — | — |
| HK-57852 | FORTEKOR TAB 2.5MG (VET) | — | — |

這 3 張許可證皆為動物用藥（VET），並非人用藥品。

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜，非仿單內容）：血管性水腫（含遺傳性、後天性及 RAS 阻斷劑誘發）、無尿症、肝衰竭與肝病、腎臟疾病、低血壓、胰臟炎、糖尿病與糖尿病酮酸中毒、全身性紅斑性狼瘡、嗜中性白血球低下與顆粒球缺乏症、鉀缺乏、副甲狀腺功能亢進、肝昏迷與肝性腦病變、結締組織疾病等。
- **藥物交互作用**：共查得 100 筆，已列出者皆為中度，主要為降血糖藥物，包括胰島素類（human、aspart、degludec、detemir、glargine、glulisine、lispro 等）、磺醯脲類（glimepiride、glipizide、glyburide、chlorpropamide、acetohexamide）、alogliptin、dapagliflozin、exenatide，另有 hydrocortisone 與 glycerin。
- 此外，ACE 抑制劑用於腎血管性病變時，需留意急性腎損傷與高血鉀風險。

人用藥品的警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型，沒有臨床試驗或直接文獻支持（L5）。
- 目前香港只有動物用藥許可證，且腎動脈狹窄患者有急性腎功能惡化的已知風險。

**若要推進需要：**
- 取得 Benazepril 的作用機轉資料與人用藥品仿單的警語與禁忌症
- 針對腎血管性高血壓及惡性高血壓腎病，系統性檢索 ACE 抑制劑的臨床試驗與文獻
- 評估雙側腎動脈狹窄、高血鉀與急性腎損傷的安全性監測計畫
- 確認人用劑型在香港的註冊狀況
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

