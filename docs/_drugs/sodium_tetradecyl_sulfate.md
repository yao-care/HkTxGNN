---
layout: default
title: Sodium Tetradecyl Sulfate
parent: 僅模型預測 (L5)
nav_order: 808
evidence_level: L5
indication_count: 10
---

# Sodium Tetradecyl Sulfate
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

# Sodium tetradecyl sulfate：從靜脈硬化治療到食道靜脈曲張（未出血）

## 一句話總結

Sodium tetradecyl sulfate（STS，十四烷基硫酸鈉）是一種清潔劑類靜脈硬化劑，在香港以 Fibro-Vein 注射液上市。
TxGNN 模型預測它可能對**未出血的食道靜脈曲張 (Esophageal varices without bleeding)** 有效。
目前**沒有臨床試驗登記**，但有 **20 篇文獻**。多數文獻研究的是已出血或急性出血的患者，或胃靜脈曲張，與預測的「未出血」族群不完全吻合。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明（藥理上屬靜脈硬化劑） |
| 預測新適應症 | 未出血的食道靜脈曲張 (Esophageal varices without bleeding) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2（依證據包評定；多為舊的活性對照試驗且無階段標示，從嚴認定可能偏低） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。以下是依硬化劑藥理推論：STS 是清潔劑型硬化劑，會破壞靜脈內皮，引起血栓與纖維化，使血管閉塞。

食道靜脈曲張本質上是擴張的靜脈，閉塞血管在機轉上說得通。STS 也確實被用於內視鏡靜脈曲張硬化治療，以及胃靜脈曲張的 BRTO（球囊閉塞逆行經靜脈閉塞術，使用泡沫或混合 lipiodol 的劑型）。

要注意兩點：
- 現有的隨機對照研究多為 STS 與其他硬化劑（polidocanol、ethanolamine oleate、sodium morrhuate）的比較，多數收治已出血的患者，無法確認是否納入未出血（預防性）族群。
- 目前實務上偏好套扎術與氰基丙烯酸酯，STS 的額外價值仍待確認。

## 臨床試驗證據

目前無相關臨床試驗登記。

（相鄰適應症「出血性食道靜脈曲張」下有 NCT05500625，為 EUS 導引線圈加氰基丙烯酸酯與 BRTO 的比較，針對胃靜脈曲張，STS 並非研究介入，僅屬間接參考。）

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1734694](https://pubmed.ncbi.nlm.nih.gov/1734694/) | 1992 | RCT | Am J Gastroenterol | 52 位食道靜脈曲張出血患者，1.5% STS 對 1% polidocanol，兩組曲張靜脈根除率皆為 88% |
| [8287811](https://pubmed.ncbi.nlm.nih.gov/8287811/) | 1993 | RCT（雙盲） | Endoscopy | 95 位靜脈曲張出血患者，3% STS 對 5% ethanolamine oleate 的療效與副作用比較 |
| [2279644](https://pubmed.ncbi.nlm.nih.gov/2279644/) | 1990 | RCT | Gastrointest Endosc | 41 位急性出血患者，STS 對 sodium morrhuate，死亡率 38% 對 25%（無顯著差異） |
| [8886633](https://pubmed.ncbi.nlm.nih.gov/8886633/) | 1996 | RCT | Endoscopy | 高張葡萄糖水對 STS，用於食道靜脈曲張根除後的胃靜脈曲張出血 |
| [30170340](https://pubmed.ncbi.nlm.nih.gov/30170340/) | 2019 | Review | J Gastroenterol Hepatol | BRTO 的近年發展，2000 年代後期起 STS 成為 ethanolamine oleate 之外的硬化劑選項 |
| [3443730](https://pubmed.ncbi.nlm.nih.gov/3443730/) | 1987 | 世代研究 | J Clin Gastroenterol | 24 位晚期肝病患者，探討 STS 硬化治療對食道的臨床與組織病理影響 |
| [8776100](https://pubmed.ncbi.nlm.nih.gov/8776100/) | 1996 | 回顧性調查 | J Clin Gastroenterol | 11 年、285 位食道胃靜脈曲張患者，含緊急、擇期與預防性注射，使用 2% STS 加造影劑 |
| [21353984](https://pubmed.ncbi.nlm.nih.gov/21353984/) | 2011 | 世代研究 | J Vasc Interv Radiol | 以 STS 泡沫做 BRTO 治療出血性胃靜脈曲張的初期經驗 |
| [28180928](https://pubmed.ncbi.nlm.nih.gov/28180928/) | 2017 | 世代研究 | Cardiovasc Intervent Radiol | STS 加 lipiodol 泡沫用於大型門體分流與胃底靜脈曲張的 BRTO，評估安全性與療效 |
| [37745308](https://pubmed.ncbi.nlm.nih.gov/37745308/) | 2023 | 世代研究 | Diagn Interv Radiol | 順行性泡沫硬化治療用於門脈高壓靜脈曲張出血 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 廠商 |
|---------|------|------|------|
| HK-62315 | FIBRO-VEIN SOLUTION FOR INJECTION 0.2% W/V | 注射液（依品名） | SINO-ASIA PHARMACEUTICAL SUPPLIES LTD |
| HK-62316 | FIBRO-VEIN SOLUTION FOR INJECTION 0.5% W/V | 注射液（依品名） | SINO-ASIA PHARMACEUTICAL SUPPLIES LTD |
| HK-62318 | FIBRO-VEIN SOLUTION FOR INJECTION 1% W/V | 注射液（依品名） | SINO-ASIA PHARMACEUTICAL SUPPLIES LTD |
| HK-62317 | FIBRO-VEIN SOLUTION FOR INJECTION 3% W/V | 注射液（依品名） | SINO-ASIA PHARMACEUTICAL SUPPLIES LTD |

四張許可證的資料均未載明核准適應症。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 本適應症沒有臨床試驗，文獻多針對出血或胃靜脈曲張，是否適用未出血族群無法確認。
- 香港衛生署仿單的警語與禁忌資料缺口屬阻斷性（Blocking），無法進入安全性篩選。
- 相鄰的「出血性食道靜脈曲張」證據較強（證據包評為 Proceed with Guardrails），可作為優先探討方向。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌資料。
- 補充 DrugBank 的作用機轉資料。
- 逐篇確認 RCT 的受試者是否納入未出血（預防性）患者。
- 與目前標準治療（套扎術、氰基丙烯酸酯）比較，確認 STS 的增益價值。
- 確認香港核准適應症與劑型，評估食道內視鏡注射用途是否屬仿單外使用。

本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

