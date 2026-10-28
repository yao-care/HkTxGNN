---
layout: default
title: Imidacloprid
parent: 僅模型預測 (L5)
nav_order: 460
evidence_level: L5
indication_count: 9
monitor_inn: "IMIDACLOPRID"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "non-syndromic esophageal malformation", "esophageal disease", "mitral valve prolapse (disease)", "neurocirculatory asthenia", "familial mitral valve prolapse", "MVP1"]
last_modified_at: 2026-10-23
description: "Imidacloprid：預測新適應症為馬尾症候群 (Cauda Equina Syndrome)（證據等級 L5）。原適應症：許可證資料未載明適應症文字（產品為獸醫用）"
---

# Imidacloprid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Imidacloprid：從獸醫用途到馬尾症候群（模型預測，證據不足）
{: .text-alpha }

## 一句話總結

Imidacloprid 是新煙鹼類（neonicotinoid）殺蟲成分，在香港登記的產品皆為寵物用（獸醫用）外用滴劑。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬於模型推論，建議暫緩（Hold）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明適應症文字（產品為獸醫用） |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 許可證數 | 6 張（有效 6 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 imidacloprid 是昆蟲菸鹼型乙醯膽鹼受體（nAChR）的促效劑，對哺乳動物 nAChR 的親和力低得多。

馬尾症候群是脊髓末端神經根受壓迫的結構性神經急症，藥理上沒有明確理由認為 nAChR 促效劑能改善。這個高分來自 TxGNN 模型（深度學習），可能只反映模型從相關疾病之間學到的相似性，並非生物學證據，也無機轉或臨床資料支持。再者，imidacloprid 已知具有哺乳動物神經毒性，與神經系統疾病的治療目標相悖。

其他預測結果（神經源性膀胱、腸躁症、食道疾病、二尖瓣脫垂等）同樣只有模型分數，沒有試驗或文獻支持。其中「神經源性膀胱」在本體論中已被標記為過時術語，可信度更低；二尖瓣脫垂相關項目（含家族性與 MVP1）屬結構或遺傳性疾病，缺乏藥理依據，且彼此高度重複。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對馬尾症候群，目前無相關文獻。

在其他預測項目中，僅「食道疾病」有 1 篇文獻，但屬獸醫研究，不能作為人類證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29506575](https://pubmed.ncbi.nlm.nih.gov/29506575/) | 2018 | 獸醫研究（雙盲、安慰劑對照） | Parasites & Vectors | 比較 imidacloprid＋moxidectin 外用劑（Advocate）與注射型 doramectin，用於犬隻食道旋尾線蟲病；療效可能來自 moxidectin 的抗寄生蟲作用，與人類食道疾病無關 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55111 | ADVANTAGE 400 SOLN 400MG/4ML (VET) | 未載明 | 未載明 |
| HK-55109 | ADVANTAGE 250 SOLN 250MG/2.5ML (VET) | 未載明 | 未載明 |
| HK-57257 | ADVANTAGE 40 FOR CATS SOLUTION 40MG/0.4ML (VET) | 未載明 | 未載明 |
| HK-57256 | ADVANTAGE 80 FOR CATS SOLUTION 80MG/0.8ML (VET) | 未載明 | 未載明 |
| HK-55110 | ADVANTAGE 100 SOLN 100MG/ML (VET) | 未載明 | 未載明 |

另有 HK-55112（ADVANTAGE 40 SOLN 40MG/0.4ML，獸醫用）。以上 6 張皆為單一成分、有效的許可證，持有者為 UNIPET HOUSE COMPANY LIMITED。

---

## 安全性考量

安全性資訊請參考原廠仿單。

本次整理的資料中未查到藥物交互作用紀錄。另外，imidacloprid 在哺乳動物具有已知的神經毒性，而菸鹼受體促效作用可能加重自律神經相關症狀，若考慮用於人體需特別審慎。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有 TxGNN 模型（深度學習）的預測（證據等級 L5），分數可能反映模型從相關疾病間學到的相似性，並非生物學證據，也沒有直接研究馬尾症候群的試驗或文獻。
- 藥物本身為獸醫用殺蟲成分，缺乏作用機轉與人用安全性資料，且已知神經毒性與預測方向相衝突。

**若要推進需要：**
- 補齊 imidacloprid 的作用機轉與哺乳動物藥理、毒理資料
- 取得香港衛生署仿單的警語與禁忌資料
- 進行前臨床研究，驗證其對神經根壓迫或神經損傷模型是否有益
- 在確認機轉合理且安全性可接受之前，不建議進入臨床開發
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

