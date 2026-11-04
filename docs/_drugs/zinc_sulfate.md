---
layout: default
title: Zinc Sulfate
parent: 高證據等級 (L1-L2)
nav_order: 955
evidence_level: L2
indication_count: 4
last_modified_at: 2026-11-04
monitor_inn: "ZINC SULFATE"
predicted_indications: ["pharyngitis", "nasal cavity disease", "acute laryngopharyngitis", "congenital prothrombin deficiency"]
description: "Zinc Sulfate：預測新適應症為咽炎 (pharyngitis)（證據等級 L2）。原適應症：本地許可證資料未記載適應症"
---

# Zinc Sulfate
{: .fs-9 }

證據等級: **L2** | 預測適應症: **4** 個
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

Zinc Sulfate（硫酸鋅）是一種鋅補充劑，於香港多用於眼用製劑與營養輸液成分。
TxGNN 模型預測它可能對**咽炎 (pharyngitis)** 有效，
目前有 **1 個臨床試驗**和 **2 篇文獻**與此方向相關，證據等級為 **L2**，但多屬術後或放療後咽喉痛，並非感染性咽炎，屬間接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 咽炎 (pharyngitis) |
| TxGNN 預測分數 | 0.9985 |
| 證據等級 | L2 |
| 香港上市 | 上市中（有效許可證 7 張／共 7 張） |
| 許可證數 | 7 張（有效 7 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，鋅在口咽部可能具有局部抗病毒活性、調節發炎反應，並有助於黏膜修復，因此機轉上可能適用於咽炎。

臨床資料主要來自術後喉嚨痛與放療相關黏膜炎的研究，與一般感染性咽炎的族群不同，因此這項預測目前仍屬於「研究假說」層級，需要在感染性咽炎族群中直接驗證。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02405832](https://clinicaltrials.gov/study/NCT02405832) | NA | 完成 | 87 | 隨機、雙盲、安慰劑對照試驗，評估術前口含鋅錠對全身麻醉插管後喉嚨痛的影響；結果顯示可降低術後喉嚨痛的發生率與嚴重度，但族群為插管後而非感染性咽炎 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23720981](https://pubmed.ncbi.nlm.nih.gov/23720981/) | 2013 | RCT | Journal of the Medical Association of Thailand | 頭頸癌患者補充硫酸鋅以減輕放療引起的口腔黏膜炎與咽炎；隨機試驗未見明顯益處 |
| [20123362](https://pubmed.ncbi.nlm.nih.gov/20123362/) | 2010 | 病例報告／觀察性 | Oral Surg Oral Med Oral Pathol Oral Radiol Endod | 扁桃腺切除術後長期味覺異常的恢復，探討鋅缺乏可能的角色，與咽炎治療僅間接相關 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-46124 | OPTO-PHARM EYE WASH | 未記載 | 未記載 |
| HK-46363 | V-ROHTO EYE DROPS | 未記載 | 未記載 |
| HK-40758 | NEW EYE RUBY EYE DROPS | 未記載 | 未記載 |
| HK-60855 | SMOFKABIVEN PERIPHERAL EMULSION FOR INFUSION | 未記載 | 未記載 |
| HK-60482 | SMOFKABIVEN EMULSION FOR INFUSION | 未記載 | 未記載 |

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，其中較值得注意的中度交互作用包括 alendronic acid、risedronic acid、ibandronate（雙磷酸鹽類）、tetracycline 與 baloxavir marboxil，可能與鋅在腸道的螯合作用有關，併用時需注意服藥間隔。其餘多為輕度交互作用（如多種免疫抑制劑與皮質類固醇）。

其他警語與禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
有一項隨機、安慰劑對照試驗顯示鋅錠可降低術後喉嚨痛，但放療相關咽炎的隨機試驗未見益處，且兩者皆非感染性咽炎，證據等級為 L2，屬下限。TxGNN 分數很高（0.9985），可作為研究方向，但不宜直接推論臨床療效。

**若要推進需要：**
- 在感染性（病毒性或細菌性）咽炎族群中進行隨機對照試驗
- 取得詳細的作用機轉資料與局部給藥（如口含錠）的劑型可行性評估
- 取得原廠仿單中的警語與禁忌症，並建立與雙磷酸鹽類、四環黴素類等藥物的併用間隔指引

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

