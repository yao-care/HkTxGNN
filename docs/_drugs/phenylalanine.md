---
layout: default
title: Phenylalanine
parent: 僅模型預測 (L5)
nav_order: 580
evidence_level: L5
indication_count: 2
---

# Phenylalanine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Phenylalanine：從必需胺基酸到硬化性膽管炎（低可信度預測）

## 一句話總結

Phenylalanine（苯丙胺酸）是人體必需胺基酸，目前未於香港上市為藥品，也無核准適應症紀錄。
TxGNN 模型預測它對**硬化性膽管炎 (Sclerosing Cholangitis)** 有效，
但檢視 4 篇相關文獻後判斷，此關聯很可能是知識圖譜的**實體混淆**（酪胺酸 tyrosine、含苯丙胺酸序列的趨化胜肽 FMLP 被誤連結為 phenylalanine 本身），不構成真實藥理支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無公開核准適應症（本品未於香港上市，屬營養/胺基酸補充成分） |
| 預測新適應症 | 硬化性膽管炎 (Sclerosing Cholangitis) |
| TxGNN 預測分數 | 99.43% |
| 證據等級 | L5（僅模型預測，無實質支持證據） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 phenylalanine 詳細的作用機轉（MOA）資料。作為必需胺基酸，其生理角色是蛋白質合成前驅物及酪胺酸（tyrosine）的代謝來源，本身並無已知的抗發炎或膽道保護機轉。

檢視支持此預測的 4 篇文獻後發現，其中多數並非真正指向游離態 phenylalanine：
- PMID 15790420 討論的是**酪胺酸（tyrosine）**血中濃度與疲勞的關聯，與 phenylalanine 是不同分子；
- PMID 8000512、2103382 討論的是 **FMLP（formyl-methionyl-leucyl-phenylalanine）**，一種細菌趨化胜肽，雖名稱含 "phenylalanine" 字串，但藥理性質與游離胺基酸完全不同；且 PMID 8000512 顯示 FMLP 在大鼠是**誘發**膽管炎，方向與「治療」相反。

因此，這個預測合理性偏低，較可能是 TxGNN 知識圖譜上因字串/實體相似而產生的連結雜訊，而非真實的機轉關聯。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | Cohort | BMC Gastroenterology | 探討原發性膽汁性肝硬化/硬化性膽管炎患者血中**酪胺酸**濃度與疲勞的關聯（非 phenylalanine） |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | Cohort/Metabolomics | J Clin Exp Hepatol | 膽管癌血清代謝體特徵分析，未針對 phenylalanine 治療效果 |
| [8000512](https://pubmed.ncbi.nlm.nih.gov/8000512/) | 1994 | Animal model | J Gastroenterology | FMLP（含苯丙胺酸序列的胜肽）於大鼠**誘發**小膽管炎，方向為致病而非治療 |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | Assay method | J Gastroenterol Hepatol | FMLP 之腸肝循環檢測方法學研究，非療效證據 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

（本評估未取得 TFDA/香港仿單警語、禁忌症及藥物交互作用資料，屬 Blocking 等級資料缺口，需補齊後才能進行安全性初評。）

---

## 附註：第二項預測（Rank 2）

TxGNN 同時預測 phenylalanine 對**先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)** 有效（分數 99.26%）。唯一相關試驗 NCT06227429 之標的藥物實為 **Nitisinone**（非 phenylalanine，且機轉相反——Nitisinone 會使血中 phenylalanine/tyrosine 升高），該試驗已 WITHDRAWN、招募人數 0，不構成證據。此關聯同樣判斷為資料庫連結雜訊，證據等級 L5，建議 Hold。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 兩項預測（硬化性膽管炎、先天性凝血酶原缺乏症）皆屬 L5（僅模型分數，無實質研究支持），且經逐篇檢視後，相關文獻/試驗實際指向不同分子（酪胺酸、FMLP、Nitisinone）而非 phenylalanine 本身，判斷為知識圖譜實體混淆導致的假陽性可能性高。
- 本品未於香港上市，也缺乏仿單安全性資料（Blocking 缺口），S1 安全性初評無法進行。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，Blocking）
- 取得 phenylalanine 明確作用機轉資料（DG002，High）
- 針對兩項預測重新確認 TxGNN 知識圖譜中的實體對應是否有字串混淆問題（tyrosine vs phenylalanine、FMLP vs phenylalanine、Nitisinone vs phenylalanine），必要時提報模型資料清洗
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

