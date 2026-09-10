---
layout: default
title: Lithium Carbonate
parent: 僅模型預測 (L5)
nav_order: 459
evidence_level: L5
indication_count: 5
---

# Lithium Carbonate
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

# Lithium Carbonate：原適應症資料缺失，預測用於 Pseudoachondroplasia（假性軟骨發育不全症）

## 一句話總結

Lithium Carbonate（DB14509）目前在本 Evidence Pack 中未收錄原始核准適應症與作用機轉資料。
TxGNN 模型預測它可能對**Pseudoachondroplasia（假性軟骨發育不全症）**有效，
但目前**無任何臨床試驗、無任何文獻**支持，僅為模型層級的推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料庫未收錄（無許可證或原適應症紀錄） |
| 預測新適應症 | Pseudoachondroplasia（假性軟骨發育不全症） |
| TxGNN 預測分數 | 99.98%（排名 792） |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空）。根據 TxGNN 推論給出的機轉假說：
Pseudoachondroplasia 主因為 COMP 基因突變，導致軟骨細胞內質網蛋白堆積與細胞凋亡；
Lithium 已知為 GSK-3β 抑制劑，理論上可活化 Wnt/β-catenin 及自噬路徑，可能影響軟骨細胞分化與蛋白清除機制。

**需特別說明：此關聯僅為 TxGNN 知識圖譜推論的間接機轉假說，並無任何直接實驗或臨床資料支持。** 由於本次 Evidence Pack 也未取得 Lithium 的原始核准適應症資訊，無法進一步比對原適應症與新適應症之間的臨床關聯性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

此藥物目前尚未在香港取得任何藥品許可證（許可證數：0）。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
本預測完全缺乏臨床試驗與文獻證據支持（證據等級 L5），作用機轉僅為模型推論假說，且藥物尚未在香港上市，安全性資料亦付之闕如，目前不具備進入下一階段評估的條件。

**若要推進需要：**
- 取得藥品仿單警語與禁忌症資料（Blocking，用於通過 S1 安全性初評）
- 查證 Lithium 的正式作用機轉（MOA），釐清與骨骼發育路徑的實際關聯
- 補充 Lithium 原始核准適應症資訊，以評估與新適應症的臨床關聯性
- 尋找是否有臨床前（動物/細胞）研究可驗證 GSK-3β 抑制與 COMP 相關軟骨病變的關係
- 註：同批預測另有 4 個相近分數的罕見骨骼疾病候選適應症（acromesomelic dysplasia、colobomatous microphthalmia-rhizomelic dysplasia syndrome、brachyolmia、myosclerosis），均為同等級（L5/Hold），證據狀況相同，建議一併觀察後續文獻更新。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

