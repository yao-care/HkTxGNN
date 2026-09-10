---
layout: default
title: Oxyquinoline
parent: 中證據等級 (L3-L4)
nav_order: 549
evidence_level: L4
indication_count: 10
---

# Oxyquinoline
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Oxyquinoline：從（原適應症資料缺失）到骨關節炎

## 一句話總結

Oxyquinoline（DrugBank ID: DB11145）目前在香港未上市，且原始核准適應症與作用機轉資料皆缺失。
TxGNN 模型預測它可能對**骨關節炎 (Osteoarthritis)** 有效，
但目前僅有 **1 個臨床試驗**（性質為顯影劑生物分布研究，非療效試驗）和 **1 篇文獻**（測試對象為結構類似物 Clioquinol，非同一藥物），證據強度薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（Evidence Pack 未提供，且香港未上市無許可證可查） |
| 預測新適應症 | 骨關節炎 (Osteoarthritis) |
| TxGNN 預測分數 | 98.40% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Oxyquinoline 的詳細作用機轉資料（MOA 標記為 [Data Gap]），也沒有原始核准適應症紀錄，因此無法從機轉層面直接論證其用於骨關節炎的合理性。

現有的兩項證據皆屬間接關聯而非直接證據：唯一的臨床試驗（NCT07139431）是以 [89Zr]-Oxine 作為**細胞放射性標記劑**，追蹤細胞治療產品 NCR100 注射入膝關節後的生物分布，Oxine 在此僅扮演顯影工具的角色，並非被測試的治療性介入。唯一的文獻則是關於 **Clioquinol**（一種鹵化 8-hydroxyquinoline，與 Oxyquinoline 結構相關但非同一化合物）在果蠅模型中的抗衰老效應，與骨關節炎軟骨細胞衰老病理有理論上的間接連結，但這是不同化合物的臨床前資料。

整體而言，TxGNN 的高分預測（98.40%）目前主要反映知識圖譜嵌入層面的相似性，缺乏針對 Oxyquinoline 本身的直接療效證據支持。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07139431](https://clinicaltrials.gov/study/NCT07139431) | Phase 1 | 尚未招募 | 6 | 評估 [89Zr]-Oxine-NCR100 注射劑於膝關節局部注射後的細胞生物分布，屬顯影追蹤研究，非療效試驗（相關性評級 C） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40570982](https://pubmed.ncbi.nlm.nih.gov/40570982/) | 2025 | 臨床前/機轉研究 | Free Radical Biology & Medicine | Clioquinol（結構類似物）延長果蠅壽命、改善代謝恆定，並提及其在骨關節炎與神經退化疾病中的潛在活性 |

---

## 安全性考量

安全性資訊請參考原廠仿單。（TFDA 仿單警語與禁忌資料為此案的阻斷性缺口 DG001，需優先補齊才能進行 S1 安全性初評；DDI 查詢亦無結果）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一的臨床試驗並非測試 Oxyquinoline 本身的治療效果，唯一的文獻探討的是結構類似物而非同一藥物，證據等級僅達 L4 且性質皆為間接關聯。
- 藥物缺乏 MOA、原始適應症及安全性（警語/禁忌）資料，屬於阻斷性資料缺口（DG001），無法進行安全性初評。

**若要推進需要：**
- 透過 DrugBank API 查詢並補齊 Oxyquinoline 的作用機轉（DG002）
- 取得 TFDA（或其他藥監局）官方仿單，解析警語與禁忌症（DG001，阻斷性缺口）
- 釐清 Oxyquinoline 與 Clioquinol 在化學結構與藥理活性上的異同，避免將類似物證據直接套用
- 若確認機轉合理，針對骨關節炎進行更聚焦的文獻與試驗檢索（目前查詢僅各命中 1 筆）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

