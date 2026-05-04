---
layout: default
title: Dihydrostreptomycin
parent: 僅模型預測 (L5)
nav_order: 204
evidence_level: L5
indication_count: 10
---

# Dihydrostreptomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Dihydrostreptomycin：從細菌感染到骨關節炎

## 一句話總結

Dihydrostreptomycin 是 Streptomycin 的氫化衍生物，屬於 Aminoglycoside 類抗生素，歷史上曾用於結核病等細菌感染的治療，但因嚴重耳毒性問題已在多國撤市。
TxGNN 模型預測它可能對**骨關節炎 (Osteoarthritis)** 有效，預測分數達 **98.25%**，
目前有 **0 個臨床試驗**和 **1 篇動物研究文獻**支持這個方向，整體臨床證據極為薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌感染（Aminoglycoside 類抗生素，歷史上用於結核病等） |
| 預測新適應症 | 骨關節炎 (Osteoarthritis) |
| TxGNN 預測分數 | 98.25% |
| 證據等級 | L4（僅有動物研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Dihydrostreptomycin 的詳細作用機轉資料。根據已知資訊，它是 Streptomycin 的氫化衍生物，屬 Aminoglycoside 類抗生素，主要透過與細菌核糖體 30S 亞基結合來抑制蛋白質合成，達到殺菌效果。

從 Aminoglycoside 類藥物特性推論，與骨關節炎可能存在兩條假設性連結：
1. **間接抗炎效果**：Aminoglycoside 對革蘭氏陰性菌感染所引發的反應性關節炎可能有間接抗炎作用，但細菌感染並非退化性骨關節炎的主要病因，此連結在機轉上薄弱。
2. **Nonsense read-through 機轉**：部分 Aminoglycoside 類藥物具有無義突變通讀特性，理論上可能影響軟骨基質合成相關基因的無義突變表現，但此機轉高度假設性，且缺乏任何人類骨關節炎的直接證據。

整體而言，TxGNN 的高分預測很可能源於知識圖譜中骨關節炎節點與鄰近疾病的拓樸相似性，而非真實的生物學機轉，機轉推論可靠性極低。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [48510](https://pubmed.ncbi.nlm.nih.gov/48510/) | 1975 | 獸醫病例系列（動物研究） | Journal of the American Veterinary Medical Association | 12 頭牛的跗關節退化性關節病（初發性／繼發性）進行關節腔內注射治療，含 Dihydrostreptomycin 成分，提供初步動物模型觀察 |

> ⚠️ **注意**：此文獻為 1975 年（51 年前）的獸醫動物研究，與人類骨關節炎臨床應用的相關性極低，不構成人體適用的臨床依據。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **重要背景**：Dihydrostreptomycin 已知具有比 Streptomycin 更高的耳毒性（ototoxicity）風險，包括不可逆性聽力損失，此為其在多國撤出人類用藥市場的主因。在考慮任何再利用方向前，此安全性問題應列為首要評估項目。

---

## 結論與下一步

**決策：Hold**

**理由：**
Dihydrostreptomycin 因嚴重耳毒性已在多國撤市，目前完全缺乏用於骨關節炎的人類臨床試驗；唯一相關文獻為半世紀前的獸醫動物研究，機轉推論高度假設性且無直接支持。在安全性疑慮未解、臨床證據基礎近乎為零的情況下，不建議繼續推進此再利用方向。

**若要推進需要：**
- 釐清 Dihydrostreptomycin 在香港及目標市場的現行法規狀態（是否已正式撤市或仍具有獸醫用途許可）
- 補充完整的作用機轉資料（MOA），特別是與軟骨代謝的潛在交集
- 補充安全性資料（耳毒性劑量反應關係、可逆性評估）
- 評估是否改以同類但安全性更佳的 Aminoglycoside（如 Gentamicin）作為替代研究基礎，再評估 read-through 機轉的可行性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

