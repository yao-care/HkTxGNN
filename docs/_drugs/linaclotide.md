---
layout: default
title: Linaclotide
parent: 僅模型預測 (L5)
nav_order: 531
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Linaclotide：預測新適應症為馬尾症候群 (Cauda Equina Syndrome)（證據等級 L5）。原適應症：腸躁症、困難梭狀芽孢桿菌結腸炎、神經循環性衰弱"
monitor_inn: "LINACLOTIDE"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "insomnia (disease)"]
---

# Linaclotide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Linaclotide：從腸躁症到馬尾症候群
{: .text-alpha }

## 一句話總結

Linaclotide 是一種鳥苷酸環化酶-C（GC-C）促效劑，原本用於腸躁症（irritable bowel syndrome）等腸胃道疾病。
TxGNN 模型預測它可能對**馬尾症候群（Cauda Equina Syndrome）**有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測，且機轉上缺乏合理連結。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腸躁症、困難梭狀芽孢桿菌結腸炎、神經循環性衰弱（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Linaclotide 屬於 GC-C 促效劑，可提高細胞內外 cGMP 濃度，作用集中在腸道局部，全身吸收極低。

馬尾症候群是腰薦神經根受壓迫造成的神經學急症，與 linaclotide 的作用路徑沒有已知關聯。模型的高分可能來自知識圖譜中與腸道、膀胱功能障礙（如便秘、神經性腸道）表型的網路鄰近性。

Linaclotide 至多可能緩解此類病人繼發的便秘症狀，無法處理神經壓迫或神經損傷本身。因此這項預測的合理性偏低，不宜視為真正的藥物再利用機會。

### 其他預測適應症（供參考）

| 排名 | 預測疾病 | 預測分數 | 評估 |
|------|---------|---------|------|
| 2 | 神經性膀胱（ontology 已標示為過時術語） | 99.89% | 無直接機轉連結，無試驗與文獻；建議先對應到現行術語（如神經性下泌尿道功能障礙）再評估 |
| 3 | 失眠 (Insomnia) | 99.51% | 全身暴露極低，中樞作用不太可能；若有關聯，也只是腸道症狀改善後的間接效果 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64139 | LINZESS CAPSULES 290MCG（ASTRAZENECA HONG KONG LIMITED） | 未提供 | 未提供 |

## 安全性考量

- **藥物交互作用**：已查詢到 56 筆交互作用，以下列出主要的中度項目：
  - Levonorgestrel（中度）
  - Ethinylestradiol（中度）
  - Norethisterone（中度）
  - Levothyroxine（中度）
  - Thyroid, porcine（中度）
  - 其餘多為輕度，涉及 PPI（如 rabeprazole、esomeprazole）、NSAID（如 ibuprofen、diclofenac、ketorolac）及各類瀉劑（如 bisacodyl、docusate、polyethylene glycol）

主要警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型，沒有任何臨床試驗或文獻佐證，證據等級為 L5。
- 機轉上，linaclotide 局部作用於腸道、全身暴露極低，與馬尾症候群的神經壓迫病理沒有合理連結。

**若要推進需要：**
- 取得香港仿單的警語與禁忌症，並補齊作用機轉資料
- 釐清模型高分的來源（例如是否由神經性腸道或膀胱表型驅動）
- 若有臨床興趣，將目標改為「馬尾症候群繼發便秘」這類症狀性適應症，並做系統性文獻檢索
- 神經性膀胱需先對應到現行疾病術語後再重新評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

