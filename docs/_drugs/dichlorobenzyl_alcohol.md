---
layout: default
title: Dichlorobenzyl Alcohol
parent: 中證據等級 (L3-L4)
nav_order: 232
evidence_level: L4
indication_count: 2
---

# Dichlorobenzyl Alcohol
{: .fs-9 }

證據等級: **L4** | 預測適應症: **2** 個
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

# Dichlorobenzyl Alcohol：從抗菌防腐劑到支氣管炎

## 一句話總結

Dichlorobenzyl Alcohol（DCBA）是一種廣為人知的表面抗菌/抗病毒成分，常見於口腔喉糖含片（如 Strepsils）中使用，在台灣目前無已核准上市藥品。TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，目前有 **1 篇文獻**間接支持此方向，但無臨床試驗數據，整體證據基礎薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無已核准適應症（已知用途：口腔抗菌含片成分） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.21% |
| 證據等級 | L4 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 標記為 Data Gap）。根據已知資訊，DCBA（2,4-二氯苄醇）是一種表面抗菌/抗病毒劑，長期作為喉糖含片（如 Strepsils）的活性成分，對口腔及咽喉部位的細菌與病毒具局部抑制效果。

支氣管炎部分由細菌或病毒感染所誘發，理論上與 DCBA 的殺菌機轉有間接關聯。然而，此推論存在根本性的藥理侷限：DCBA 的抗菌作用主要基於局部黏膜接觸，目前缺乏針對下呼吸道的全身性滲透與藥物分佈資料，口服或吸入途徑的系統性抗菌效能無充分藥理資料支撐。

因此，TxGNN 的預測雖有表面上的生物學合理性，但機轉關聯屬**間接推論層級**，距離臨床應用尚有相當距離。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [1036939](https://pubmed.ncbi.nlm.nih.gov/1036939/) | 1976 | Case/Observation | Arzneimittel-Forschung | 25 名慢性支氣管炎患者服用 clenbuterol（化學名含 3,5-dichlorobenzyl alcohol 結構）9 個月期間，觀察到血清肌酸激酶（CK）活性升高現象，屬 MM 型同功酶；本文主題為 clenbuterol，與 DCBA 本身之直接療效無關 |

> ⚠️ **注意**：上述文獻研究對象為 clenbuterol（其化學全名含 dichlorobenzyl alcohol 結構片段），並非以 DCBA 作為獨立治療藥物的研究，與本預測適應症之相關性屬間接。

---

## 台灣上市資訊

台灣目前無 Dichlorobenzyl Alcohol 相關許可證。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 第二順位預測：偏頭痛 (Migraine Disorder)

| 項目 | 內容 |
|------|------|
| TxGNN 預測分數 | 99.02% |
| 證據等級 | L5 |
| 建議決策 | Hold |

目前無任何已知機轉可連結 DCBA 與偏頭痛治療。偏頭痛主要涉及 CGRP 訊號路徑、三叉神經血管系統、5-HT 受體調控等機轉，DCBA 的抗菌/防腐藥理與上述路徑無已知交集。無臨床試驗，無相關文獻。TxGNN 高分可能源自疾病節點的網路拓撲位置，而非生物學機轉的直接對應。**不建議優先推進。**

---

## 結論與下一步

**決策：Hold**

**理由：**
DCBA 對支氣管炎的預測在機轉上屬間接推論，缺乏系統性（口服/吸入）藥理資料支撐，且目前無任何針對性臨床試驗或直接相關文獻，在台灣亦無核准上市記錄，整體證據等級僅 L4，尚不足以支持進一步開發評估。

**若要推進需要：**
- 補充 DCBA 的完整作用機轉（MOA）資料（建議查詢 DrugBank API）
- 確認 DCBA 的藥物動力學特性：口服/吸入後是否能有效到達下呼吸道
- 搜尋 DCBA 專屬（非 clenbuterol）的體外或動物模型抗菌研究
- 評估是否有適當的給藥途徑（吸入劑型）可用於支氣管炎適應症
- 安全性資料補強：取得 TFDA 仿單或 DrugBank 警語/禁忌資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

