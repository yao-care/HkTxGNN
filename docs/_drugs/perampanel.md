---
layout: default
title: Perampanel
parent: 僅模型預測 (L5)
nav_order: 681
evidence_level: L5
indication_count: 1
monitor_inn: "PERAMPANEL"
predicted_indications: ["beta-ketothiolase deficiency"]
last_modified_at: 2026-10-23
description: "Perampanel：預測新適應症為β-酮硫解酶缺乏症（證據等級 L5）。原適應症：局部癲癇、局部運動性癲癇"
---

# Perampanel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Perampanel：從局部癲癇到 β-酮硫解酶缺乏症
{: .text-alpha }

## 一句話總結

Perampanel 是一種抗癲癇藥物，原本用於局部癲癇（知識圖譜中記錄為 partial epilepsy 與 partial motor epilepsy）。
TxGNN 模型預測它可能對 **β-酮硫解酶缺乏症 (beta-ketothiolase deficiency)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 局部癲癇、局部運動性癲癇（來自知識圖譜記錄；香港許可證未載明核准適應症文字） |
| 預測新適應症 | β-酮硫解酶缺乏症 |
| TxGNN 預測分數 | 0.9979 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 7 張／共 7 張） |
| 許可證數 | 7 張（有效 7 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，perampanel 是選擇性、非競爭性的 AMPA 型麩胺酸受體拮抗劑，用於控制癲癇發作。

β-酮硫解酶缺乏症（ACAT1/T2 缺乏）是異白胺酸與酮體代謝的先天性代謝異常，特徵為反覆發作的酮酸中毒，嚴重發作後可能留下神經學後遺症。

AMPA 受體拮抗作用與這個酵素缺陷之間，目前**沒有已確立的直接生物學連結**。可能的關聯只能是間接的，例如控制代謝危機後的癲癇發作，或減輕興奮性毒性傷害，但這些都屬推測。0.9979 的高分來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62764 | FYCOMPA TABLETS 6MG | 未載明 | 未載明 |
| HK-62762 | FYCOMPA TABLETS 4MG | 未載明 | 未載明 |
| HK-62763 | FYCOMPA TABLETS 2MG | 未載明 | 未載明 |
| HK-62761 | FYCOMPA TABLETS 8MG | 未載明 | 未載明 |
| HK-67556 | FYCOMPA ORAL SUSPENSION 0.5MG/ML | 未載明（口服懸浮液） | 未載明 |

共 7 張單一成分許可證，上表列出其中 5 張，其餘為 FYCOMPA TABLETS 12MG（HK-62759）與 10MG（HK-62760）。

## 安全性考量

- **藥物交互作用**：已查得 56 筆交互作用紀錄，以下為部分例子：
  - 中度：Morphine、Codeine、Hydrocodone、Opium（鴉片類）、Dexamethasone、Metoclopramide、Promethazine、Chlorpheniramine、Dextromethorphan、Chloroquine、Hydroxychloroquine、Dronabinol、Nabilone、Ethanol
  - 輕度：Clarithromycin

  多項中度交互作用涉及中樞神經抑制藥物，合併使用時需留意嗜睡與鎮靜加成。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有 TxGNN 模型的高分預測，沒有任何直接研究該疾病的臨床試驗或文獻，證據等級為 L5。
- 機轉上沒有明確的連結，目前不足以支持推進。

**若要推進需要：**
- 補充 perampanel 的作用機轉資料，並分析其與異白胺酸／酮體代謝的可能關聯
- 進行前臨床或機轉研究，驗證 AMPA 受體拮抗對該疾病神經後遺症的作用
- 取得香港仿單的警語與禁忌症資料，完成安全性篩檢
- 評估此罕見代謝疾病的病人族群與可行的臨床研究設計
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

