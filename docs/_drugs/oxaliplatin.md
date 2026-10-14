---
layout: default
title: Oxaliplatin
parent: 高證據等級 (L1-L2)
nav_order: 649
evidence_level: L2
indication_count: 4
---

# Oxaliplatin
{: .fs-9 }

證據等級: **L2** | 預測適應症: **4** 個
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

# Oxaliplatin：從大腸癌轉移到惡性胸膜間皮瘤

## 一句話總結

Oxaliplatin（奧沙利鉑）是第三代鉑類化療藥物，原本用於結腸惡性腫瘤的轉移治療。
TxGNN 模型預測它可能對**惡性胸膜間皮瘤 (Malignant Pleural Mesothelioma)** 有效，
目前有 **3 個臨床試驗登記**（其中 2 個直接針對間皮瘤）和 **19 篇文獻**支持這個方向，但現有活性屬中等程度。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 結腸惡性腫瘤轉移（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 惡性胸膜間皮瘤 (Malignant Pleural Mesothelioma) |
| TxGNN 預測分數 | 99.68% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 18 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。根據已知資訊，Oxaliplatin 是鉑類 DNA 交聯劑，會形成股內加成物（intrastrand adducts），抑制 DNA 複製與轉錄。這與 cisplatin 的細胞毒性機轉相同，而 cisplatin 正是間皮瘤標準化療的骨幹。

原適應症（大腸癌轉移）與新適應症（間皮瘤）都是以鉑類為基礎的化療可以發揮作用的惡性腫瘤，因此機轉上具合理性。已有多項 Phase II 研究把 Oxaliplatin 與 gemcitabine、raltitrexed、vinorelbine 或 bortezomib 併用。

需要注意的是，報告的活性屬中等，與其他鉑類雙藥組合相近，並未明顯優於 cisplatin/pemetrexed 標準療法。另有一項研究（raltitrexed + oxaliplatin 作為二線治療）因無客觀反應而提前終止。極高的 TxGNN 分數與既有的臨床訊號一致，但不代表療效優越。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | 未知 | 29 | Bortezomib + Oxaliplatin 用於曾接受治療的胸膜或腹膜間皮瘤；結果未公布 |
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | 完成 | 29 | Oxaliplatin + Gemcitabine 作為一線或二線治療胸膜或腹膜間皮瘤，評估反應率；樣本數小 |
| [NCT07532902](https://clinicaltrials.gov/study/NCT07532902) | Phase 1 | 招募中 | 60 | BMS-986504 合併標準療法用於 MTAP 缺失之轉移性實體瘤；Oxaliplatin 僅為可能的背景治療，間接相關 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase II | Clin Lung Cancer | Gemcitabine + Oxaliplatin 多中心研究，25 位間皮瘤病人 |
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase II | J Clin Oncol | Raltitrexed + Oxaliplatin 用於間皮瘤（70 位病人），顯示有活性 |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase II | Lung Cancer | Vinorelbine + Oxaliplatin 作為未治療胸膜間皮瘤的一線治療 |
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Phase II | Tumori | Oxaliplatin + Raltitrexed 用於無法手術的胸膜間皮瘤之前導研究 |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | Phase II / 觀察性 | J Occup Med Toxicol | Gemcitabine + Oxaliplatin 用於 pemetrexed 治療後的間皮瘤 |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase II | Lung Cancer | Raltitrexed + Oxaliplatin 作為二線治療無客觀反應（14 位病人），試驗提前終止 |
| [15261443](https://pubmed.ncbi.nlm.nih.gov/15261443/) | 2004 | Review | Lung Cancer | 間皮瘤化療的過去結果與新進展 |
| [12610498](https://pubmed.ncbi.nlm.nih.gov/12610498/) | 2003 | Review | Br J Cancer | 傳統細胞毒性藥物反應率很少超過 30%，新組合較有前景 |
| [10936465](https://pubmed.ncbi.nlm.nih.gov/10936465/) | 2000 | Review | Crit Rev Oncol Hematol | Oxaliplatin 臨床活性回顧 |
| [31455014](https://pubmed.ncbi.nlm.nih.gov/31455014/) | 2019 | 基礎研究 | Int J Mol Sci | 化療藥物（含 oxaliplatin）對免疫檢查點表現的影響，為合併免疫治療提供依據 |

---

## 香港上市資訊

香港共有 18 張有效的單方許可證（均為注射濃縮液），主要如下。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55336 | ELOXATIN CONCENTRATE FOR SOLUTION FOR INFUSION 5MG/ML（Sanofi） | 輸注用濃縮液 | 未載明 |
| HK-63464 | OXALIPLATIN HOSPIRA 50MG/10ML（Pfizer） | 輸注用濃縮液 | 未載明 |
| HK-62512 | OXALIPLATIN SANDOZ 100MG/20ML | 輸注用濃縮液 | 未載明 |
| HK-57283 | OXALIPLATIN-TEVA 5MG/ML | 輸注用濃縮液 | 未載明 |
| HK-59547 | OXITAN INJ 5MG/ML（Fresenius Kabi） | 注射劑 | 未載明 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（鉑類，DNA 交聯劑） |
| 骨髓抑制風險 | 中度（本次資料未含詳細毒性描述，請以仿單為準） |
| 致吐性分級 | 中度（依藥物類別判斷） |
| 監測項目 | CBC（含分類）、肝腎功能、電解質、周邊神經症狀 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

---

## 安全性考量

- **知識圖譜標示的相關疾病風險（非仿單文字）**：腎臟疾病、肝臟疾病、膽囊疾病、周邊神經系統疾病／周邊神經病變、間質性肺病、肺纖維化、膿輸尿管。
- **藥物交互作用**：資料庫共查得 100 筆，以下為部分範例。
  - **嚴重 (Major)**：Dolasetron
  - **中度 (Moderate)**：Famotidine、Amphotericin B、Loperamide、Mesalazine、Metronidazole、Clarithromycin、Vancomycin、Levofloxacin、Palonosetron 等

完整的警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 1 個已完成的 Phase II 試驗（NCT00859469）以及多項直接針對間皮瘤的 Phase II 研究，且機轉與標準鉑類療法相同。但試驗規模小，活性僅屬中等，沒有證據顯示優於現行標準療法，因此以「研究問題」層級推進較為恰當。
- 其他預測適應症（上皮樣、肉瘤樣間皮瘤、惡性臟層胸膜腫瘤）的證據多為間接或僅限腹膜間皮瘤，宜暫緩（Hold）。

**若要推進需要：**
- 與 cisplatin/pemetrexed 標準療法進行比較的隨機對照試驗，或至少較大型的 Phase II 研究
- 補充詳細的作用機轉（MOA）資料
- 取得香港衛生署仿單的警語與禁忌症資料，完成安全性篩選
- 針對腎、肝、周邊神經與肺部疾病族群的安全性監測計畫
- 釐清是否適用於特定組織亞型，以及與免疫檢查點抑制劑合併的可能性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

