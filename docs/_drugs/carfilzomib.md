---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Carfilzomib：預測新適應症為CMM7（黑色素瘤相關條目）（證據等級 L5）。原適應症：漿細胞骨髓瘤 (plasma cell myeloma)"
monitor_inn: "CARFILZOMIB"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "vulvar melanoma (disease)", "melanoma"]
---

# Carfilzomib
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

# Carfilzomib：從多發性骨髓瘤到黑色素瘤

## 一句話總結

Carfilzomib 是蛋白酶體抑制劑，原本用於漿細胞骨髓瘤（多發性骨髓瘤）的治療。
TxGNN 模型預測它可能對**黑色素瘤相關疾病**有效，其中最高分的是 CMM7，另有一般黑色素瘤 (Melanoma) 等條目。
目前**沒有臨床試驗**，僅有 **4 篇文獻**（均為前臨床、計算或機轉研究）。證據非常有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 漿細胞骨髓瘤 (plasma cell myeloma)（香港許可證未列出核准適應症文字，此為知識圖譜資料） |
| 預測新適應症 | CMM7（黑色素瘤相關條目） |
| TxGNN 預測分數 | 99.37% |
| 證據等級 | L5（僅有模型預測，無實際研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

其他預測的黑色素瘤相關適應症：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 |
|------|------|-----------|---------|
| 2 | 兒童軟腦膜黑色素瘤 (pediatric leptomeningeal melanoma) | 99.30% | L5 |
| 3 | 上皮樣細胞葡萄膜黑色素瘤 (epithelioid cell uveal melanoma) | 99.23% | L5 |
| 4 | 外陰黑色素瘤 (vulvar melanoma) | 99.19% | L5 |
| 5 | 黑色素瘤 (melanoma) | 99.03% | L4 |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，carfilzomib 屬於蛋白酶體抑制劑，在漿細胞骨髓瘤中的療效已被證實。機轉上，抑制蛋白酶體可能干擾腫瘤細胞的存活路徑，因此理論上可能適用於黑色素瘤。但這是推論，並無針對 CMM7 的直接證據支持。

排名前四的預測（CMM7、兒童軟腦膜黑色素瘤、葡萄膜黑色素瘤、外陰黑色素瘤）沒有任何臨床試驗或文獻。分數很可能反映知識圖譜中與其他黑色素瘤節點的網絡鄰近性。此外，葡萄膜黑色素瘤的生物學特性與皮膚黑色素瘤不同，軟腦膜疾病還涉及藥物是否能進入中樞神經系統的問題，目前皆無資料支持。

一般「黑色素瘤」條目有較多間接線索：2021 年一項小鼠 B16-F1 黑色素瘤細胞研究顯示，carfilzomib 與 bortezomib 合併使用可增強細胞凋亡，指向蛋白酶體抑制是可能的作用機制。不過這只是細胞層級的前臨床證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下針對「黑色素瘤」預測條目（其他預測條目無文獻）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | 體外研究（小鼠細胞株） | Biology | Carfilzomib 與 bortezomib 合併使用，可在 B16-F1 黑色素瘤細胞中誘導凋亡，並活化多種 caspase |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | 計算研究（分子對接/模擬） | Journal of Biomolecular Structure & Dynamics | 針對多種癌症（含黑色素瘤）激酶標靶的藥物再利用分子對接研究，屬電腦模擬 |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | 前臨床/機轉研究 | Molecular Cancer Research | ZFAND2A 基因調控人類黑色素瘤細胞存活（與 carfilzomib 的關聯未獲證實） |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | 前臨床/機轉研究 | Matrix Biology | 骨髓瘤藥物（含 bortezomib、carfilzomib）經 NF-κB 路徑誘導 heparanase 表現，可能促成更具侵襲性的腫瘤表型（與黑色素瘤的關聯未獲證實） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65431 | KYPROLIS FOR INJECTION 30MG/VIAL（Amgen Hong Kong） | 注射劑（資料未列明） | 資料未列明 |
| HK-64828 | KYPROLIS FOR INJECTION 60MG/VIAL（Amgen Hong Kong） | 注射劑（資料未列明） | 資料未列明 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（蛋白酶體抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項（一般包含血液學參數及肝腎功能） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：資料庫共記錄 100 筆交互作用，以下為部分列出的項目：
  - **Major（重大）**：Oxandrolone、Oxymetholone、Stanozolol、Deferiprone、Samarium (153Sm) lexidronam、Aminocaproic acid、Avatrombopag、重組抗血友病因子、人類類血友病因子（von Willebrand factor）、人類 C1 酯酶抑制劑、重組凝血因子 VIIa、人類凝血因子 X、Conestat alfa
  - **Moderate（中度）**：Metronidazole、Naltrexone、Rosuvastatin、Simvastatin、Tinidazole、Palifermin、Strontium chloride Sr-89

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測的黑色素瘤適應症都沒有臨床試驗，證據等級為 L5（最高的「黑色素瘤」條目為 L4，僅有細胞與機轉層級的前臨床資料）。
- 缺乏作用機轉資料與香港仿單的安全性資訊，目前不足以進入安全性篩選。

**若要推進需要：**
- 補充 DrugBank 的作用機轉資料與香港衛生署仿單的警語、禁忌症
- 以人類黑色素瘤細胞株及動物模型驗證 carfilzomib 單藥或合併療法的療效
- 針對葡萄膜與軟腦膜黑色素瘤評估各自的生物學差異與中樞神經系統穿透性
- 評估蛋白酶體抑制劑與現有黑色素瘤標準治療合併使用的可行性
- 確認香港許可證的核准適應症與劑型資訊
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

