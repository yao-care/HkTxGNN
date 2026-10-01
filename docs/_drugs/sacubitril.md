---
layout: default
title: Sacubitril
parent: 僅模型預測 (L5)
nav_order: 780
evidence_level: L5
indication_count: 5
---

# Sacubitril
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

# Sacubitril：從心臟衰竭到腦小血管疾病 1 型（伴或不伴眼部異常）

## 一句話總結

Sacubitril 是 Sacubitril/Valsartan 複方（商品名 Entresto）的成分之一，文獻指出該複方用於射血分率降低的心臟衰竭。
TxGNN 模型預測它可能對**腦小血管疾病 1 型（伴或不伴眼部異常，brain small vessel disease 1 with or without ocular anomalies）**有效。
目前**沒有臨床試驗**，17 篇文獻都在介紹疾病本身，沒有任何一篇評估此藥，因此證據僅止於模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心臟衰竭（依文獻推斷，香港許可證資料未載明適應症） |
| 預測新適應症 | 腦小血管疾病 1 型，伴或不伴眼部異常 |
| TxGNN 預測分數 | 99.58% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Sacubitril 是 Sacubitril/Valsartan 複方的一部分，由 neprilysin 抑制劑（前驅藥）與血管張力素受體阻斷劑 valsartan 組成，其成分在心臟衰竭與高血壓中的療效已被證實。

這個預測的合理性很低。腦小血管疾病 1 型屬於單基因疾病（COL4A1 相關），病因是基底膜與小血管的膠原蛋白缺陷。Neprilysin 抑制加上血管張力素受體阻斷，都無法修補這個膠原缺陷。0.996 的高分只反映知識圖譜上的關聯，不代表有生物學依據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下 10 篇為 17 篇文獻中的代表，皆為疾病或眼部先天異常的綜述，**沒有一篇研究 Sacubitril 或 Sacubitril/Valsartan**。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35882526](https://pubmed.ncbi.nlm.nih.gov/35882526/) | 2023 | Review | J Med Genet | Axenfeld-Rieger 症候群的前房異常與全身表現 |
| [39097141](https://pubmed.ncbi.nlm.nih.gov/39097141/) | 2024 | Review | Prog Retin Eye Res | 先天性前房眼疾的基因型與表現型關聯 |
| [36926528](https://pubmed.ncbi.nlm.nih.gov/36926528/) | 2023 | Review | Clin Ophthalmol | Axenfeld-Rieger 症候群的眼科表現，與 FOXC1、PITX2 突變相關 |
| [30182440](https://pubmed.ncbi.nlm.nih.gov/30182440/) | 2018 | Review | Am J Med Genet C | 前腦無裂畸形的神經病理譜系 |
| [33870948](https://pubmed.ncbi.nlm.nih.gov/33870948/) | 2022 | Review | J Neuroophthalmol | 視神經發育不全的眼科、全身與基因發現 |
| [11941259](https://pubmed.ncbi.nlm.nih.gov/11941259/) | 2002 | Review | J Fr Ophtalmol | 先天性巨角膜，易併發青光眼 |
| [16848213](https://pubmed.ncbi.nlm.nih.gov/16848213/) | 2006 | Review（病例報告） | Acta Med Croatica | 雙行睫毛的個案與治療 |
| [10498002](https://pubmed.ncbi.nlm.nih.gov/10498002/) | 1999 | Review | Optom Vis Sci | 傾斜視盤症候群的表現與併發症 |
| [6782689](https://pubmed.ncbi.nlm.nih.gov/6782689/) | 1981 | Review | Surv Ophthalmol | 眼部缺損的病因與遺傳 |
| [6390155](https://pubmed.ncbi.nlm.nih.gov/6390155/) | 1983 | Review | Neurol Clin | 視盤異常與顱內疾病的鑑別 |

## 香港上市資訊

香港共有 9 張許可證，以下列出 5 張主要許可證。資料中未載明劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-65171 | ENTRESTO TABLETS 50MG (SINGAPORE) | NOVARTIS PHARMACEUTICALS (HK) LIMITED |
| HK-65172 | ENTRESTO TABLETS 200MG (SINGAPORE) | NOVARTIS PHARMACEUTICALS (HK) LIMITED |
| HK-65320 | ENTRESTO TABLETS 50MG | NOVARTIS PHARMACEUTICALS (HK) LIMITED |
| HK-65170 | ENTRESTO TABLETS 100MG (SINGAPORE) | NOVARTIS PHARMACEUTICALS (HK) LIMITED |
| HK-65318 | ENTRESTO TABLETS 100MG | NOVARTIS PHARMACEUTICALS (HK) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，文獻也都沒有研究此藥，證據等級為 L5。
- 這是單基因膠原缺陷疾病，找不到可信的機轉連結，不建議投入資源。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌（目前為阻擋性資料缺口）。
- 補上 DrugBank 的作用機轉資料。
- 若要繼續，需先有生物學上的機轉假說，或疾病模型的實驗數據。

**其他預測適應症的參考：**
同一份預測中，**糖尿病腎病變（diabetic nephropathy）**的證據明顯較強（L4）。它有 1 個 Phase 4 隨機對照試驗（NCT06501651，尚未招募），以及多篇囓齒類前臨床研究和 PARADIGM-HF 次分析（PMID 29661699）。若要投入評估，建議改以此適應症為優先。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選須經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

