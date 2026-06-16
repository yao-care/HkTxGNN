---
layout: default
title: Ceftazidime
parent: 中證據等級 (L3-L4)
nav_order: 150
evidence_level: L4
indication_count: 10
---

# Ceftazidime
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

# Ceftazidime：從細菌感染症到高澱粉酶血症

## 一句話總結

Ceftazidime 是第三代頭孢菌素類抗生素，對革蘭氏陰性菌（含 *Pseudomonas aeruginosa*）具有廣效殺菌活性，全球廣泛用於複雜性細菌感染治療。
TxGNN 模型預測它可能對**高澱粉酶血症 (Hyperamylasemia)** 有效，
目前有 **0 個臨床試驗**和 **1 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港未上市，無已核准適應症資料 |
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia) |
| TxGNN 預測分數 | 99.51% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，Ceftazidime 是第三代頭孢菌素（beta-lactam）抗生素，透過結合細菌青黴素結合蛋白（PBPs）來抑制細胞壁合成，對 *E. coli*、*Klebsiella* spp.、*Pseudomonas aeruginosa* 等革蘭氏陰性菌具有強效殺菌活性。其在複雜性尿路感染、院內肺炎及菌血症中的療效已被大量臨床研究證實。

**高澱粉酶血症（Hyperamylasemia）** 指血清澱粉酶濃度超過正常上限的實驗室發現，常見於急性胰腺炎、ERCP 術後或慢性腎臟病，本身為異常指標而非獨立診斷。部分研究指出膽道細菌感染可能是 ERCP 術後胰腺炎的輔助誘發因子，因此預防性抗生素理論上可能間接減少術後澱粉酶的過度升高。

然而，澱粉酶升高的核心驅動力為機械性損傷或炎症級聯反應，而非細菌直接作用。Ceftazidime 對澱粉酶水平並無任何直接藥理機轉，連結基礎薄弱。TxGNN 的高分預測較可能反映知識圖譜中「感染→膽道炎→胰腺炎→澱粉酶升高」的間接路徑，而非真實的藥物再利用信號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [11985972](https://pubmed.ncbi.nlm.nih.gov/11985972/) | 2001 | RCT | Journal of Gastrointestinal Surgery | 前瞻性研究評估 ERCP 術前例行性抗生素預防對術後胰腺炎及高澱粉酶血症的影響；預防性抗生素可降低化膿性感染風險，但對澱粉酶水平的直接影響尚不確定，不足以支持 Ceftazidime 用於此適應症 |

---

## 香港上市資訊

Ceftazidime 在香港目前**未取得任何上市許可**（共 0 張許可證），無已核准適應症資料。如需臨床使用，須透過特殊進口管道（Special Drugs Permit）向香港衞生署申請。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Hyperamylasemia 為實驗室指標而非獨立疾病診斷，Ceftazidime 對澱粉酶水平缺乏直接藥理機轉。目前無任何直接相關臨床試驗，唯一文獻亦僅間接涉及 ERCP 術後抗生素預防，無法支撐此再利用方向。此外，Ceftazidime 在香港尚無上市許可，進一步增加臨床推進的障礙。

> **附注：** TxGNN 模型對本藥物的其他預測中，**尿路感染（Rank 4）** 具備 L1 等級臨床證據及「Proceed with Guardrails」建議，遠優於本報告焦點的 Hyperamylasemia。建議優先評估 UTI 方向的報告。

**若要推進 Hyperamylasemia 方向需要：**
- 補充 Ceftazidime 完整作用機轉（MOA）資料（來源：DrugBank API）
- 取得香港衞生署上市核准或特殊進口許可
- 針對「抗生素預防 ERCP 術後胰腺炎」且以澱粉酶為主要終點的前瞻性試驗
- 至少一個機轉層面的細菌感染-澱粉酶連結研究
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

