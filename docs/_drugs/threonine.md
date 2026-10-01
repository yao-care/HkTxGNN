---
layout: default
title: Threonine
parent: 僅模型預測 (L5)
nav_order: 858
evidence_level: L5
indication_count: 1
---

# Threonine
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

# Threonine：從原適應症未記載到胃輕癱

## 一句話總結

Threonine（蘇胺酸）是必需胺基酸，在香港有多項含此成分的產品上市，但資料中沒有記載原適應症。
TxGNN 模型預測它可能對**胃輕癱 (Gastroparesis)** 有效，但目前**沒有臨床試驗**，只有 **1 篇文獻**，而且該文獻並未把蘇胺酸當作治療手段來研究，實際證據等同於零。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未記載 |
| 預測新適應症 | 胃輕癱 (Gastroparesis) |
| TxGNN 預測分數 | 99.32% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，蘇胺酸也沒有登錄原適應症。已知它是必需胺基酸，存在於多種胺基酸輸液與營養製劑中，但這不足以說明它對胃輕癱有治療作用。

TxGNN 分數很高（99.32%），但這只是知識圖譜的推論結果。唯一檢索到的文獻（PMID 28627597）研究的是糖尿病大鼠胃平滑肌細胞凋亡，以及 PI3K-AKT-mTOR 和 AMPK-mTOR 訊號路徑，並沒有以蘇胺酸作為介入措施。

這個關聯很可能是名稱造成的假象：AKT 和 mTOR 都是絲胺酸/蘇胺酸激酶（serine/threonine kinase），文獻是因為名稱相符而被配對，並非蘇胺酸本身有療效。目前沒有證據顯示兩者之間存在可驗證的機轉關聯。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28627597](https://pubmed.ncbi.nlm.nih.gov/28627597/) | 2017 | 前臨床／病理生理研究 | Molecular Medicine Reports | 在糖尿病胃輕癱大鼠模型中，探討胃平滑肌細胞凋亡及 PI3K-AKT-mTOR、AMPK-mTOR 訊號的變化；未評估蘇胺酸作為治療 |

## 香港上市資訊

下列為含蘇胺酸的主要許可證（共 20 張，列出 5 張）：

| 許可證號 | 品名 | 製造／申請商 |
|---------|------|-------------|
| HK-32089 | KETOSTERIL TAB | Fresenius Kabi Hong Kong Limited |
| HK-57540 | AMINOL-S INJ | Wings Pharmaceutical Ltd |
| HK-62100 | AMINOGEN-S SOLUTION FOR INFUSION | Wings Pharmaceutical Ltd |
| HK-60459 | PAN-VASOL SOLUTION FOR INJECTION | Falkan Medical Limited |
| HK-58914 | PAN-AMIN G INJ | Otsuka Pharmaceutical (H.K.) Limited |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅 L5：沒有臨床試驗，唯一的文獻不是以蘇胺酸為介入的研究，關聯很可能來自 serine/threonine kinase 的名稱巧合。
- 缺少原適應症、作用機轉和安全性資料，無法進入安全性初篩。

**若要推進需要：**
- 取得香港衛生署的仿單（警語、禁忌症、適應症）
- 補充 DrugBank 的作用機轉資料
- 檢索以蘇胺酸（或含蘇胺酸的胺基酸製劑）作為介入、針對胃輕癱的直接研究
- 若找不到直接證據，建議把此預測視為假陽性，不再投入資源

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

