---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 935
evidence_level: L5
indication_count: 5
---

# Zidovudine
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

# Zidovudine：從 HIV 感染治療到猴免疫缺陷病毒感染

## 一句話總結

Zidovudine（AZT）是一種核苷類逆轉錄酶抑制劑，香港有 8 張許可證，但資料中未載明原適應症。
TxGNN 預測它可能對**猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)** 有效。
目前**沒有臨床試驗**，只有 **20 篇文獻**，且幾乎都是獼猴等動物實驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L4（僅有前臨床／動物研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

> 香港許可證資料未載明核准適應症，故本表省略「原適應症」。

## 為什麼這個預測合理？

Zidovudine 是核苷類逆轉錄酶抑制劑 (NRTI)。SIV 是慢病毒，其逆轉錄酶與 HIV 同源，所以抗病毒活性在生物學上說得通。目前缺乏 DrugBank 的詳細作用機轉資料，上述說明來自預測的機轉推論。

不過，SIV 只感染非人類靈長類，是研究 HIV 的動物模型，不是人類疾病。這個預測支持的是 HIV 的作用機轉，並沒有帶來新的人類藥物再利用機會。

此外，同一份資料中的「先天性 HIV 感染」預測有較強的人類證據，這才是 zidovudine 較有價值的方向（見結論）。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下 10 篇皆屬動物或前臨床研究，沒有 RCT。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1489181](https://pubmed.ncbi.nlm.nih.gov/1489181/) | 1992 | 動物研究 | Antimicrob Agents Chemother | 口服 AZT 可預防幼年恆河猴感染 SIV |
| [7695293](https://pubmed.ncbi.nlm.nih.gov/7695293/) | 1995 | 動物研究 | Antimicrob Agents Chemother | 新生獼猴立即服用 AZT，可預防感染或降低病毒量，並延緩 AIDS 發病 |
| [7797947](https://pubmed.ncbi.nlm.nih.gov/7797947/) | 1995 | 動物研究 | J Infect Dis | AZT 未能預防感染，但延長存活期，並降低腦脊髓液病毒量 |
| [7848683](https://pubmed.ncbi.nlm.nih.gov/7848683/) | 1994 | 動物研究 | AIDS Res Hum Retroviruses | 在食蟹獼猴急性感染期，觀察 AZT 對病毒量與免疫變化的影響 |
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | 動物研究 | AIDS | 以 AZT、拉米夫定與茚地那韋進行暴露後預防，評估對獼猴陰道傳染的效果 |
| [2016686](https://pubmed.ncbi.nlm.nih.gov/2016686/) | 1991 | 動物研究 | J Acquir Immune Defic Syndr | AZT 與 3'-氟胸苷皆無法預防感染，後者延遲抗原出現的效力約為前者的 10 倍 |
| [7690823](https://pubmed.ncbi.nlm.nih.gov/7690823/) | 1993 | 動物研究（待分類） | J Infect Dis | 比較感染後不同時間點開始給 AZT 的效果 |
| [9021180](https://pubmed.ncbi.nlm.nih.gov/9021180/) | 1997 | 前臨床（體外病毒學） | Antimicrob Agents Chemother | 產生 AZT 抗藥性（Q151M 突變）的 SIV 突變株，仍可在新生獼猴引起 AIDS |
| [8452370](https://pubmed.ncbi.nlm.nih.gov/8452370/) | 1993 | 體外研究 | Antimicrob Agents Chemother | AZT 可抑制 SIV 在巨噬細胞中造成的細胞融合，並與中和抗體比較 |
| [22713337](https://pubmed.ncbi.nlm.nih.gov/22713337/) | 2012 | 前臨床 | Antimicrob Agents Chemother | 研究新型 NRTI（EFdA）對 SIV 的作用，與 zidovudine 無直接關係 |

## 香港上市資訊

資料中的劑型與核准適應症皆為空白，故省略這兩欄。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-57407 | VICK-ZIDOVUDINE CAP 100MG | VICKMANS LABORATORIES LTD |
| HK-57408 | VICK-ZIDOVUDINE CAP 250MG | VICKMANS LABORATORIES LTD |
| HK-59602 | RETROVIR ORAL SOLUTION 10MG/ML | GLAXOSMITHKLINE LIMITED |
| HK-42757 | RETROVIR IV INFUSION 10MG/ML | GLAXOSMITHKLINE LIMITED |
| HK-66688 | ZIDOVUDINE TABLETS USP 300MG | VIATRIS HEALTHCARE HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- SIV 是動物模型，並非人類適應症，證據只有前臨床等級（L4）。
- 預測分數雖高（99.96%），但沒有臨床試驗，也沒有新的人類使用價值。

**若要推進需要：**
- 補齊香港衛生署仿單的警語、禁忌與核准適應症（目前為阻擋性缺口）。
- 補充 DrugBank 的作用機轉資料。
- 改評估同一份預測中的**先天性 HIV (congenital HIV)**：
  - 已有多個 Phase 3 試驗，包括預防母嬰傳染。
  - 初步評估等級為 L2，建議列為研究問題。
  - 需先確認各試驗中 zidovudine 是試驗藥物、對照組還是背景療法。
  - 需一併評估血液毒性、心臟功能與孕期先天畸形的安全訊號。
- 其餘預測（神經發育障礙、已廢止的家族性複合型高脂血症）僅有模型分數，沒有任何試驗或文獻支持，也找不到合理的機轉關聯，不建議投入資源。

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

