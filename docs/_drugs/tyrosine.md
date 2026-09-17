---
layout: default
title: Tyrosine
parent: 僅模型預測 (L5)
nav_order: 779
evidence_level: L5
indication_count: 10
---

# Tyrosine
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

# Tyrosine：從（無核准適應症）到馬尾症候群（Cauda Equina Syndrome）— 預測，證據不支持

## 一句話總結

Tyrosine 是必需胺基酸，目前查無核准適應症、香港亦未上市。
TxGNN 模型預測其對**馬尾症候群 (Cauda Equina Syndrome)** 有效（分數 99.77%），
但複核後僅有 **1 篇文獻**且與本適應症無直接關聯，判定為知識圖譜雜訊，證據等級 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 查無核准適應症紀錄 |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Tyrosine 的詳細作用機轉（MOA）資料，且此藥物並無查得的核准適應症紀錄，故無法比較原始適應症與預測適應症之間的關聯性。

根據人工複核，本項預測**缺乏合理的機轉基礎**：馬尾症候群為結構性神經壓迫疾病，與胺基酸 Tyrosine 補充並無已知病理生理連結。唯一支持文獻（PMID 17341045）內容為透明細胞肉瘤（clear cell sarcoma）病例報告，與馬尾症候群及 Tyrosine 皆無直接關聯，判定為知識圖譜（KG）節點共現雜訊而非真實訊號。

因此，本預測目前僅具探索性質，尚不具備進一步開發的機轉合理性。

> **附註**：Evidence Pack 中同時列出的其他 9 個候選適應症（obsolete neurogenic bladder、angle-closure glaucoma、hyperthyroidism、POTS、hyperthyroxinemia、TRβ 抗性、traumatic glaucoma、aqueous misdirection、neovascular glaucoma），複核結論同樣為 Hold：多數證據為 KG 雜訊，或如 hyperthyroidism / neovascular glaucoma 案例，檢索結果實為「Tyrosine Kinase Inhibitor（TKI 藥物類別）」或「CLS-AX 抗VEGF藥物」的詞彙混淆，並非胺基酸 Tyrosine 本身；POTS 案例則出現機轉方向相反（alpha-methyl-p-tyrosine 為合成抑制劑，非補充型 tyrosine）的矛盾證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17341045](https://pubmed.ncbi.nlm.nih.gov/17341045/) | 2006 | Case Report | Neurosurgical Focus | 透明細胞肉瘤病例報告，起源於 S1 神經根，與馬尾症候群及 Tyrosine 補充無關，屬 KG 共現雜訊 |

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **資料缺口（Blocking）**：TFDA/香港仿單警語與禁忌資料目前缺失（DG001），無法進行 S1 安全性初評。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測適應症（馬尾症候群）證據等級僅 L5，唯一文獻與適應症無直接關聯，機轉上無合理連結。
- 藥物缺乏原始適應症與 MOA 資料，且香港未上市；仿單警語/禁忌資料為 Blocking 缺口（DG001），無法進入下一階段安全性評估。
- 其餘候選適應症複核後多為 KG 雜訊或存在藥物類別混淆（Tyrosine vs. Tyrosine Kinase Inhibitor），不具備推進基礎。

**若要推進需要：**
- 取得 TFDA/香港仿單警語與禁忌資料（DG001，Blocking）
- 補充 DrugBank MOA 資料（DG002）
- 針對候選適應症重新執行人工文獻複核，排除 TKI 類藥物與胺基酸 Tyrosine 的詞彙混淆
- 若持續無法排除 KG 雜訊，建議將此候選案排除於近期 repurposing pipeline 之外
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

