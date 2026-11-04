---
layout: default
title: Zinc Sulfate
parent: 僅模型預測 (L5)
nav_order: 955
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-04
monitor_inn: "ZINC SULFATE"
predicted_indications: ["pharyngitis", "nasal cavity disease", "acute laryngopharyngitis", "congenital prothrombin deficiency"]
description: "Zinc Sulfate：預測新適應症為咽炎 (pharyngitis)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Zinc Sulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Zinc Sulfate: 咽炎 (pharyngitis)
{: .text-alpha }

## 一句話總結

Zinc Sulfate（硫酸鋅）是一種鋅補充與微量元素成分，目前在香港有多張單一成分許可證。
TxGNN 模型預測它可能對**咽炎 (pharyngitis)** 有效，但目前僅有 **1 個相關的臨床試驗**和 **2 篇文獻**，且直接針對咽炎的證據為陰性或僅為間接證據，證據等級為 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 咽炎 (pharyngitis) |
| TxGNN 預測分數 | 0.9985 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 7 張／共 7 張） |
| 許可證數 | 7 張（有效 7 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，鋅在口咽部可能具有局部作用，包括抗病毒活性、調節發炎反應，以及支持黏膜修復。這是機轉上的推測，並非來自已證實的臨床療效。

不過，現有研究並不支持此推測。唯一直接針對咽炎的隨機試驗（PMID 23720981）探討的是放射線誘發的口腔黏膜炎與咽炎，並未顯示硫酸鋅有助益。鋅口含錠的試驗（NCT02405832）則針對插管後的術後喉嚨痛，屬於相關但不同的情況，不能等同於咽炎。

因此，這個高分預測目前主要是模型推算的結果，缺乏直接的臨床療效證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | 不適用 | 完成 | 87 | 隨機、雙盲、安慰劑對照，評估術前口服鋅口含錠對術後喉嚨痛發生率的影響；族群為插管後患者，非感染性咽炎 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | J Med Assoc Thai | 評估硫酸鋅補充對頭頸癌患者放射線誘發口腔黏膜炎與咽炎的效果；未顯示明確助益 |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | 病例報告／觀察性 | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | 探討扁桃腺切除術後長期味覺異常與鋅缺乏的可能關聯 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-46124 | OPTO-PHARM EYE WASH | 未記載 | 未記載 |
| HK-46363 | V-ROHTO EYE DROPS | 未記載 | 未記載 |
| HK-40758 | NEW EYE RUBY EYE DROPS | 未記載 | 未記載 |
| HK-60855 | SMOFKABIVEN PERIPHERAL EMULSION FOR INFUSION | 未記載 | 未記載 |
| HK-60482 | SMOFKABIVEN EMULSION FOR INFUSION | 未記載 | 未記載 |

## 安全性考量

- **藥物交互作用**：已查詢到多項交互作用，其中中度者包括 alendronic acid、risedronic acid、ibandronate（雙磷酸鹽類）、tetracycline 及 baloxavir marboxil；其餘多為輕度（如多種皮質類固醇與免疫抑制劑）。鋅可能與部分藥物在腸道結合而降低吸收，併用時宜錯開服藥時間。

其他警語與禁忌資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 直接針對咽炎（放射線誘發）的隨機試驗未顯示硫酸鋅有益，其餘證據僅為術後喉嚨痛等相關情況的間接資料，因此證據等級為 L5。
- TxGNN 分數雖高（0.9985），但缺乏支持療效的臨床證據，不足以推進。

**若要推進需要：**
- 針對感染性咽炎、以硫酸鋅或鋅製劑進行的隨機對照試驗
- 明確的作用機轉資料，以及適合咽喉局部使用的劑型與途徑評估
- 完整的安全性資料（警語、禁忌症），可由原廠仿單取得

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

