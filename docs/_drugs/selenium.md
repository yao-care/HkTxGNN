---
layout: default
title: Selenium
parent: 僅模型預測 (L5)
nav_order: 803
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Selenium：預測新適應症為硬化性膽管炎 (Sclerosing Cholangitis)（證據等級 L5）。原適應症：資料中未載明"
---

# Selenium
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Selenium：從（原適應症未載明）到硬化性膽管炎

## 一句話總結

Selenium（硒）是人體必需的微量元素，目前在香港有 4 張單一成分許可證，但本次compiled 資料中未載明其核准適應症。
TxGNN 模型預測它可能對**硬化性膽管炎 (Sclerosing Cholangitis)** 有效，但目前**沒有臨床試驗**，僅有 **5 篇**觀察性或間接相關的文獻，證據屬於模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未載明 |
| 預測新適應症 | 硬化性膽管炎 (Sclerosing Cholangitis) |
| TxGNN 預測分數 | 99.04% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。硒是麩胱甘肽過氧化酶（glutathione peroxidase）及多種硒蛋白的必要成分，參與抗氧化防禦。

在膽汁淤積性肝病中，氧化壓力與發炎被認為是致病因素之一，也與肝纖維化有關。因此理論上，硒的抗氧化作用可能減緩膽汁淤積性肝損傷。不過這只是合理的推測，尚未經證實。

需要特別注意的是，現有文獻顯示原發性硬化性膽管炎 (PSC) 患者的肝臟有硒與銅滯留，但這可能反映代謝改變或膽汁淤積本身，而非治療標靶，作用方向（有益或有害）並不明確。此外，硒是靜脈營養的組成成分，與靜脈營養相關肝病的膽汁淤積有關，但與 PSC 本身無直接關聯。目前沒有證據顯示補充硒能改善 PSC 的預後。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39601354](https://pubmed.ncbi.nlm.nih.gov/39601354/) | 2025 | Cohort | Liver Int | PSC 患者脂溶性維生素攝取與整體飲食品質偏低，並與北歐營養建議比較 |
| [9053974](https://pubmed.ncbi.nlm.nih.gov/9053974/) | 1995 | Cohort | Scand J Gastroenterol | 32 位 PSC 患者的微量元素代謝研究，顯示肝臟有銅與硒滯留 |
| [29148959](https://pubmed.ncbi.nlm.nih.gov/29148959/) | 2017 | Cohort（個案） | JPEN J Parenter Enteral Nutr | 重度吸收不良合併 PSC 與潰瘍性結腸炎患者的靜脈營養調整，討論氧化壓力與抗氧化狀態 |
| [17109383](https://pubmed.ncbi.nlm.nih.gov/17109383/) | 2006 | 前臨床（小鼠蛋白質體學） | Proteomics | 比較毒性誘發肝纖維化與硬化性膽管炎小鼠模型的肝臟蛋白質變化 |
| [18941372](https://pubmed.ncbi.nlm.nih.gov/18941372/) | 2008 | Review | Eur J Cancer Prev | 大腸直腸癌化學預防的回顧，與硬化性膽管炎關聯性間接 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68022 | SELENIUM AGUETTANT CONCENTRATE FOR SOLUTION FOR INFUSION 100MCG/10ML | 未載明 | 未載明 |
| HK-63846 | SELESYN ORAL SOLUTION 100MCG/2ML | 未載明 | 未載明 |
| HK-63948 | SELESYN SOLUTION FOR INJECTION 500MCG/10ML | 未載明 | 未載明 |
| HK-63847 | SELESYN SOLUTION FOR INJECTION 100MCG/2ML | 未載明 | 未載明 |

---

## 安全性考量

- **藥物交互作用**（共 6 筆，來源：DDInter）：
  - **嚴重**：Dimercaprol
  - **中度**：Levofloxacin、Triethylenetetramine、Deferiprone、Tolevamer、Eltrombopag

其他安全性資訊（警語、禁忌症）請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數雖高（99.04%），但僅屬計算預測，沒有任何臨床試驗，文獻也僅為觀察性或間接相關的研究。
- 肝臟硒滯留的意義與作用方向不明，且缺乏作用機轉與仿單安全性資料，目前不宜推進。

**若要推進需要：**
- 補充 DrugBank 的作用機轉資料，並釐清硒與 PSC 病理（氧化壓力、纖維化）的機轉連結
- 取得香港衛生署核准適應症與仿單的警語、禁忌症
- 進行 PSC 患者血中與肝臟硒狀態的研究，釐清硒缺乏或滯留的臨床意義
- 前臨床（如 Abcb4 基因剔除小鼠）驗證硒補充的效果，再評估早期臨床試驗
- 評估與 PSC 常用藥物及上述交互作用藥物的併用風險，以及不同給藥途徑（口服或注射）的適用性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

