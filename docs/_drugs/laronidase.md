---
layout: default
title: Laronidase
parent: 僅模型預測 (L5)
nav_order: 511
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Laronidase：預測新適應症為伴有骨骼病變的溶小體儲積症 (lysosomal storage disease with skeletal involvement)（證據等級 L4）。原適應症：黏多醣症、Hurler 症候群、Hurler-Scheie 症候群、Scheie 症候群"
monitor_inn: "LARONIDASE"
predicted_indications: ["lysosomal storage disease with skeletal involvement", "Sanfilippo syndrome"]
---

# Laronidase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Laronidase：從黏多醣症 I 型到伴有骨骼病變的溶小體儲積症
{: .text-alpha }

## 一句話總結

Laronidase 是重組人類 α-L-艾杜糖醛酸酶（alpha-L-iduronidase），原本用於治療黏多醣症（Hurler、Hurler-Scheie、Scheie 症候群）。
TxGNN 模型預測它可能對**伴有骨骼病變的溶小體儲積症 (lysosomal storage disease with skeletal involvement)** 有效，但目前**沒有登記的臨床試驗**，僅有 **4 篇文獻**，且多屬原適應症範圍內的資料。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 黏多醣症、Hurler 症候群、Hurler-Scheie 症候群、Scheie 症候群 |
| 預測新適應症 | 伴有骨骼病變的溶小體儲積症 (lysosomal storage disease with skeletal involvement) |
| TxGNN 預測分數 | 0.9931 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Laronidase 是補充缺乏的 α-L-艾杜糖醛酸酶的酵素替代療法，用於黏多醣症 I 型（MPS I）。此病因溶小體水解酶缺乏，導致皮膚素硫酸 (dermatan sulfate) 與肝素硫酸 (heparan sulfate) 蓄積。

MPS I 本身就是一種溶小體儲積症，且骨骼病變（多發性骨發育不良，dysostosis multiplex）是其核心特徵。因此這個「新適應症」大致上是原適應症的重新標示或子集，**並非真正的藥物再利用**。TxGNN 的高分很可能反映本體論上與 MPS I 的緊密關係，而非新的治療訊號。

體外研究顯示，laronidase 可被培養的纖維母細胞與成骨細胞攝取，主要經甘露糖-6-磷酸受體進入溶小體，提供了對骨骼相關作用的細胞層面可能性。不過，酵素替代療法對軟骨、骨骼等缺乏血管的組織滲透有限，這是需要留意的限制。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Review | Pediatric Endocrinology Reviews | MPS I 為 α-L-艾杜糖醛酸酶缺乏所致，疾病譜涵蓋 Hurler、Hurler/Scheie 與 Scheie；以尿液 GAG 及酵素活性確診 |
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Review | BioDrugs | 概述 laronidase 的開發進程，已獲美國與歐洲孤兒藥資格 |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | 體外研究 | Biol Pharm Bull | 培養的 MPS I 纖維母細胞與成骨細胞可依劑量攝取 laronidase，主要經 M6P 受體進入溶小體 |
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | 病例報告 | Pediatric Neurology | 一名 Scheie 症候群男童接受 6.5 年酵素替代治療的追蹤，後期整體狀況出現下降（屬原適應症範圍） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56438 | ALDURAZYME CONC. SOLUTION FOR IV INFUSION 2.9MG/5ML（廠商：SANOFI HONG KONG LIMITED） | 靜脈輸注濃縮液 | — |

---

## 安全性考量

- **藥物交互作用**：已查詢到 2 筆，皆為輕微 (Minor) 等級，分別為 Chloroquine 與 Procaine。

其他安全性資訊（警語、禁忌症）請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測適應症本質上是 MPS I 原核准適應症的子集，並非新的治療方向，TxGNN 高分不代表有新的臨床訊號。
- 沒有針對此適應症的臨床試驗，現有文獻多屬原適應症範圍，證據等級僅 L4。

**若要推進需要：**
- 釐清此適應症是否真的與既有 MPS I 適應症不同，避免重複定位
- 作用機轉的詳細資料（MOA）
- 酵素在骨骼、軟骨組織的分布與療效資料
- 原廠仿單中的警語、禁忌症與核准適應症內容

---

## 附帶說明：排名第二的預測（Sanfilippo 症候群）

TxGNN 對 **Sanfilippo 症候群 (MPS III)** 的預測分數為 0.9922，證據等級 L4，建議同為 Hold，且**不建議推進**：

- MPS III 缺乏的是其他分解肝素硫酸的酵素（如 heparan N-sulfatase、N-acetyl-α-glucosaminidase），並非 α-L-艾杜糖醛酸酶，laronidase 無法補足缺失的酵素。
- MPS III 以中樞神經病變為主，而靜脈注射的 laronidase 難以穿越血腦屏障。
- 檢索到的文獻幾乎都在談 MPS I（包括一項 Phase 3 安慰劑對照試驗 [PMID 15126990](https://pubmed.ncbi.nlm.nih.gov/15126990/)，以及 2025 年的生物相似藥研究 [PMID 40830667](https://pubmed.ncbi.nlm.nih.gov/40830667/)），並不支持對 Sanfilippo 症候群的療效。
- 高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

