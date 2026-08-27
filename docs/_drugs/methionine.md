---
layout: default
title: Methionine
parent: 僅模型預測 (L5)
nav_order: 405
evidence_level: L5
indication_count: 10
---

# Methionine
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

# Methionine：原適應症資料缺失，預測可能適用於 Acne（痤瘡）

## 一句話總結

Methionine（DrugBank ID：DB00134）是一種必需胺基酸，本次評估組並未收錄其原始核准適應症與作用機轉資料（Data Gap）。TxGNN 模型在其眾多候選適應症中，將 **Acne（痤瘡）** 列為評分最高的預測標的（分數 **99.9996%**），但目前僅有 **4 篇文獻**支持、**無任何臨床試驗**，且證據方向與治療假說並不一致，證據等級評定為 **L5**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無公開資料（本評估組未收錄，屬資料缺口） |
| 預測新適應症 | Acne (痤瘡) |
| TxGNN 預測分數 | 99.9996%（該藥物全部候選適應症中排名第 27） |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Methionine 的作用機轉（MOA）資料，其原始核准適應症也未收錄於本次評估組。根據模型推論的理論基礎，Methionine 是 homocysteine 的代謝前驅物，理論上與含硫胺基酸代謝路徑相關，這可能是模型將其與痤瘡連結的統計基礎。

然而，支持這個預測的文獻證據方向其實相反：其中一篇文獻描述的是異維A酸（isotretinoin，一種用於治療囊腫型痤瘡的藥物）會「升高」患者血漿 homocysteine 濃度，這是該藥物的**副作用觀察**，並非「補充 Methionine 可改善痤瘡」的治療性證據。其餘文獻涉及 MTHFR 基因突變新生兒腦病變、Sweet氏症候群、嗜中性球 C5a 功能觀察，與痤瘡致病機轉的關聯性也相當薄弱。

整體而言，此預測較接近知識圖譜的統計相似性推論，缺乏可驗證、方向一致的生物學路徑說明，機轉合理性偏低。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11277950](https://pubmed.ncbi.nlm.nih.gov/11277950/) | 2001 | Cohort（藥物副作用觀察） | International Journal of Dermatology | 異維A酸治療囊腫型痤瘡患者血漿 homocysteine 濃度升高，屬藥物副作用觀察，非 Methionine 治療性證據 |
| [39357918](https://pubmed.ncbi.nlm.nih.gov/39357918/) | 2024 | Case Report | BMJ Case Reports | MTHFR 基因突變新生兒病例，合併新生兒痤瘡、稀疏毛髮、類馬凡氏體型等表現 |
| [3859500](https://pubmed.ncbi.nlm.nih.gov/3859500/) | 1985 | Case Report/Observational | Journal of the American Academy of Dermatology | Sweet氏症候群合併囊腫結節型痤瘡患者的嗜中性球趨化活性觀察 |
| [3161955](https://pubmed.ncbi.nlm.nih.gov/3161955/) | 1985 | Observational | The Journal of Investigative Dermatology | 感染性與非感染性皮膚疾病（含痤瘡）患者嗜中性球 C5a 功能短暫缺失之體外觀察 |

## 香港上市資訊

目前未於香港藥品許可證資料庫中登記（本藥品尚未上市）。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一支持 Acne 適應症的文獻證據方向薄弱且相反（描述的是他藥副作用觀察，而非 Methionine 治療效果），證據等級僅 L5，無臨床試驗佐證。
- Methionine 的作用機轉（MOA）與仿單安全性資料（警語、禁忌症）均為缺口，其中仿單資料缺口屬 Blocking 等級，尚無法進入安全性初評（S1）。

**若要推進需要：**
- 取得香港衛生署核准仿單的警語與禁忌症資料（Blocking，需優先補齊）
- 取得 Methionine 明確的作用機轉資料，以評估與 Acne 的機轉關聯性是否成立
- 針對 Acne 適應症尋找具治療意圖（而非藥物副作用觀察）的直接證據，如體外/動物治療性研究或早期臨床試驗
- 另可留意本候選藥物中證據等級較高的白內障相關預測（cortical cataract、nuclear senile cataract、mature cataract，評為 L4／S1／Research Question）：這些適應症有多篇動物與離體研究支持 methionine→cysteine→麩胱甘肽（GSH）抗氧化路徑對水晶體透明度的潛在保護作用，機轉關聯性明顯優於 Acne，但仍缺乏人體介入性試驗資料，可作為後續研究方向的優先參考
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

