---
layout: default
title: Streptomycin
parent: 中證據等級 (L3-L4)
nav_order: 820
evidence_level: L4
indication_count: 5
---

# Streptomycin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Streptomycin：從細菌感染到結膜炎

## 一句話總結

Streptomycin（鏈黴素）是一種胺基糖苷類抗生素，香港許可證資料未載明原核准適應症。
TxGNN 模型預測它可能對**結膜炎 (Conjunctivitis)** 有效，但目前**沒有相關臨床試驗**，只有 **18 篇文獻**（多為歷史性或間接證據）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明適應症文字 |
| 預測新適應症 | 結膜炎 (Conjunctivitis) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。以下依一般藥理知識說明：Streptomycin 是胺基糖苷類抗生素，結合細菌 30S 核糖體次單位，抑制細菌蛋白質合成。因此對敏感的結膜病原菌，機轉上有可能適用。

文獻只支持特定感染，主要是兔熱病（Parinaud 眼腺症候群）與結核性結膜炎，一般細菌性結膜炎並無支持證據。1950 年代曾有摩洛哥季節性結膜炎的 Streptomycin 滴眼試驗，但屬歷史性研究，證據層級低。眼科已有許多成熟的抗生素可用，因此這個預測的臨床價值有限。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3317953](https://pubmed.ncbi.nlm.nih.gov/3317953/) | 1987 | Review | Survey of Ophthalmology | 回顧眼科使用的胺基糖苷類抗生素，內容以 Tobramycin 為主 |
| [38298538](https://pubmed.ncbi.nlm.nih.gov/38298538/) | 2023 | Review | Frontiers in Microbiology | 兔熱病治療的實驗與臨床資料，結膜炎為其臨床表現之一 |
| [19941479](https://pubmed.ncbi.nlm.nih.gov/19941479/) | 2010 | Review | Current Medicinal Chemistry | 被忽視的細菌性疾病（Buruli 潰瘍、砂眼） |
| [38941282](https://pubmed.ncbi.nlm.nih.gov/38941282/) | 2024 | Case report | Am J Case Rep | 兔熱病桿菌感染引起 Parinaud 眼腺症候群 |
| [19584516](https://pubmed.ncbi.nlm.nih.gov/19584516/) | 2009 | Case report | Indian J Med Microbiol | 家族性兔熱病病例，包含淋巴結炎與咽炎表現 |
| [15442493](https://pubmed.ncbi.nlm.nih.gov/15442493/) | 1950 | Case report | La Semana Medica | 原發性結核性結膜炎，以全身與局部 Streptomycin 治療 |
| [13075256](https://pubmed.ncbi.nlm.nih.gov/13075256/) | 1953 | 歷史臨床研究 | Rev Int Trachome | 摩洛哥季節性結膜炎，比較 Streptomycin 與 chloramine 滴眼的預防與治療效果 |
| [13075257](https://pubmed.ncbi.nlm.nih.gov/13075257/) | 1953 | 歷史臨床研究 | Rev Int Trachome | 摩洛哥南部季節性結膜炎，比較 Streptomycin 洗眼液與 Aureomycin 藥膏 |
| [18132879](https://pubmed.ncbi.nlm.nih.gov/18132879/) | 1949 | 實驗研究 | Am J Ophthalmol | Streptomycin 對 Hemophilus 引起的實驗性結膜炎之療效 |
| [21484175](https://pubmed.ncbi.nlm.nih.gov/21484175/) | 2011 | 觀察性研究 | J Ophthalmic Inflamm Infect | 奈及利亞拉哥斯結膜炎病原菌、抗生素抗藥性與質體分析 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62354 | STREPTOMYCIN SULPHATE REIG JOFRE POWDER FOR SOLUTION FOR INJECTION 1G | 未載明（品名為注射用粉劑） | 未載明 |
| HK-11269 | NEODIARISTIN POWDER (VET) | 未載明 | 未載明（獸醫用產品） |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 結膜炎沒有任何臨床試驗，文獻多為 1949–1953 年的歷史研究、個案報告或間接證據，且僅支持兔熱病、結核等特定感染。
- 香港仿單的警語與禁忌資料缺漏，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症。
- 從 DrugBank 補充作用機轉資料。
- 釐清目標病原與給藥途徑。現有許可證僅見注射劑，眼用劑型不明。
- 與現有眼科抗生素做比較評估，確認是否有臨床價值。

另外四個預測適應症（感染後血管炎、後細菌性疾病、感染後症候群、感染性尿道狹窄）的證據更弱，同樣建議 Hold。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

