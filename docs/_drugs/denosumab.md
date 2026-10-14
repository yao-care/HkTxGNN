---
layout: default
title: Denosumab
parent: 僅模型預測 (L5)
nav_order: 256
evidence_level: L5
indication_count: 2
---

# Denosumab
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

# Denosumab：從骨質疏鬆症到嚴重非增殖性糖尿病視網膜病變

## 一句話總結

Denosumab 是一種 RANKL 抑制劑，原本用於骨質疏鬆症（含停經後骨質疏鬆與藥物引起的骨質疏鬆）。
TxGNN 模型預測它可能對**嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)** 有效，
但目前**沒有臨床試驗**，也**沒有直接相關文獻**，僅屬模型預測。

> 說明：模型另預測「糖尿病視網膜病變 (Diabetic Retinopathy)」（分數 99.23%），有 2 篇間接文獻。以下主要以排名第一的預測適應症為準，並於相關段落補充第二項預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 骨質疏鬆症、停經後骨質疏鬆症、藥物引起的骨質疏鬆症（來自知識圖譜；香港許可證未提供核准適應症文字） |
| 預測新適應症 | 嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Denosumab 是針對 RANKL 的單株抗體，可抑制 RANK/RANKL 訊號，減少破骨細胞活化，進而降低骨流失。

RANK/RANKL 訊號也曾被報告與發炎及血管病變有關，理論上可能與視網膜微血管疾病有關聯。不過這只是**合理但尚未驗證的推測**，無法由目前資料證實。

第二項預測（糖尿病視網膜病變）有兩篇間接文獻。其中一篇 2024 年的真實世界世代研究與統合分析顯示，Denosumab 相較於雙磷酸鹽類，與較低的第 2 型糖尿病發生率、足部潰瘍風險及全因死亡率相關。該研究並未直接回答視網膜病變的療效。另一篇是糖尿病族群的 FRAX 骨折風險評估，與 Denosumab 對視網膜的作用無關。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

針對排名第一的預測（嚴重非增殖性糖尿病視網膜病變）：目前無相關文獻。

針對第二項預測（糖尿病視網膜病變），僅有以下間接文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38899553](https://pubmed.ncbi.nlm.nih.gov/38899553/) | 2024 | 世代研究／統合分析（依標題推斷，未經確認） | Diabetes, Obesity & Metabolism | Denosumab 相較雙磷酸鹽類，與較低的第 2 型糖尿病發生率、足部潰瘍風險及全因死亡率相關；未直接評估視網膜病變療效 |
| [36960265](https://pubmed.ncbi.nlm.nih.gov/36960265/) | 2023 | 觀察性／臨床工具評估（依標題推斷，未經確認） | Cureus | 評估第 2 型糖尿病成人使用 FRAX 工具的骨折風險；與 Denosumab 視網膜療效無直接關係 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68757 | WYOST SOLUTION FOR INJECTION 120MG/1.7ML（Sandoz） | 注射液 | 未提供 |
| HK-68756 | JUBBONTI SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 60MG/1ML（Sandoz） | 預充填注射液 | 未提供 |
| HK-61163 | XGEVA SOLUTION FOR INJECTION 120MG（Amgen） | 注射液 | 未提供 |
| HK-60588 | PROLIA SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 60MG/ML（Amgen） | 預充填注射液 | 未提供 |

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為部分中度（Moderate）等級項目：
  - 皮質類固醇：Hydrocortisone、Triamcinolone、Dexamethasone、Betamethasone、Budesonide、Prednisolone、Prednisone、Methylprednisolone
  - 免疫調節或抑制相關藥物：Tacrolimus、Mercaptopurine、Dupilumab、Levamisole
  - 放射性或放射免疫藥物：Ibritumomab tiuxetan、Tositumomab、Iobenguane (I-131)

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測目前僅有模型分數（99.63%），沒有臨床試驗和直接文獻，屬於 L5。第二項預測也只有間接文獻（L4），無法支持視網膜病變療效。
- 作用機轉資料缺漏，機轉連結無法驗證。

**若要推進需要：**
- 補齊 Denosumab 的作用機轉資料，並評估 RANK/RANKL 與視網膜微血管病變的機轉關聯
- 進行前臨床研究（如糖尿病視網膜病變動物模型）或回溯性世代研究，直接評估視網膜病變結局
- 取得香港衛生署核准仿單，確認警語、禁忌症與核准適應症
- 評估給藥途徑的可行性（目前為全身性注射劑，是否適合眼科用途尚待確認）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

