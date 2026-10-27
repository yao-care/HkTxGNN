---
layout: default
title: Tenecteplase
parent: 僅模型預測 (L5)
nav_order: 857
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Tenecteplase：預測新適應症為後下壁心肌梗塞 (Posteroinferior Myocardial Infarction)（證據等級 L5）。原適應症：心肌梗塞、冠狀動脈血栓"
monitor_inn: "TENECTEPLASE"
predicted_indications: ["congenital coronary artery anomaly", "coronary stenosis"]
---

# Tenecteplase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Tenecteplase：從心肌梗塞到後下壁心肌梗塞
{: .text-alpha }

## 一句話總結

Tenecteplase 是一種纖維蛋白專一性的組織型纖溶酶原活化劑，原本用於急性心肌梗塞的溶栓治療。
TxGNN 模型預測它可能對**後下壁心肌梗塞 (Posteroinferior Myocardial Infarction)** 有效，
但目前**沒有臨床試驗**，也**沒有針對此亞型的文獻**，僅有模型預測支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心肌梗塞、冠狀動脈血栓（香港許可證未載明適應症文字） |
| 預測新適應症 | 後下壁心肌梗塞 (Posteroinferior Myocardial Infarction) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Tenecteplase 是纖維蛋白專一性的組織型纖溶酶原活化劑，
其在急性心肌梗塞（STEMI）中的療效已被證實，機轉上是溶解冠狀動脈內的血栓，因此理論上適用於同樣由血栓性冠狀動脈阻塞所致的心肌梗塞亞型。

後下壁心肌梗塞是心肌梗塞依解剖位置劃分的亞型，與已核准的心肌梗塞適應症本質相同。
因此 0.9987 的高分主要反映與既有適應症的重疊，並非真正的新適應症訊號。預測合理，但屬於重複性質。

排名接近的其他預測也值得留意：後側壁心肌梗塞（同為 99.87%，同屬心肌梗塞亞型）、間隔心肌梗塞（99.85%）、冠狀動脈狹窄（99.53%，有少量文獻）。先天性冠狀動脈異常（99.61%）的機轉依據薄弱，因為它不是以血栓為主的疾病。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無針對後下壁心肌梗塞的相關文獻。

作為參考，排名第 5 的預測「冠狀動脈狹窄」有以下較相關的研究（僅為間接證據）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/) | 2020 | 隨機可行性/安全性研究 | Am J Cardiol | ICE T-TIMI 49：40 名接受直接 PCI 的病人隨機接受冠狀動脈內低劑量 TNK (4 mg) 或生理食鹽水，評估可行性與安全性 |
| [16053952](https://pubmed.ncbi.nlm.nih.gov/16053952/) | 2005 | 比較研究 | J Am Coll Cardiol | CAPITAL AMI：比較 TNK 輔助血管成形術與單用 TNK 溶栓於高風險 STEMI |
| [16139127](https://pubmed.ncbi.nlm.nih.gov/16139127/) | 2005 | 小型臨床研究 | J Am Coll Cardiol | 冠狀動脈內纖維蛋白專一性溶栓劑輸注，有助於慢性完全阻塞病變的經皮再通 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49440 | METALYSE FOR INJ 10,000U | 注射劑 | 未提供 |

## 安全性考量

- **藥物交互作用**：共查得 100 筆交互作用，以下為部分重點：
  - 嚴重（Major）：Abciximab、Apixaban、Betrixaban、Acalabrutinib、Avapritinib、Deferasirox、Ibritumomab tiuxetan、Tositumomab
  - 中度（Moderate）：Acetylsalicylic acid（阿斯匹靈）、Ibuprofen、Ketorolac、Celecoxib、Aminocaproic acid、Omega-3 脂肪酸、Fenfluramine、Dexfenfluramine、Sibutramine

多數嚴重交互作用與出血風險增加有關，與其他抗凝血、抗血小板藥物併用時須特別留意。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 後下壁心肌梗塞屬於 Tenecteplase 已核准的心肌梗塞適應症之亞型，高分主要反映適應症重疊，並無獨立的再利用訊號，且沒有任何針對此亞型的試驗或文獻。
- 在所有預測中，「冠狀動脈狹窄」有較多間接文獻（含小型隨機可行性研究），可作為後續研究問題，但同樣缺乏確證性證據。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 補充詳細的作用機轉資料
- 確認後下壁、後側壁等心肌梗塞亞型是否已涵蓋於現行核准的 MI 適應症中，若已涵蓋則無需另行申請
- 若要探討冠狀動脈內給藥等新用途，需設計前瞻性對照研究並建立出血風險監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

