---
layout: default
title: Nitrofurantoin
parent: 中證據等級 (L3-L4)
nav_order: 614
evidence_level: L4
indication_count: 5
---

# Nitrofurantoin
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

# Nitrofurantoin：從泌尿道感染到類風濕性關節炎（預測不受支持）

## 一句話總結

Nitrofurantoin（呋喃妥因）是一種抗菌藥，原本用於泌尿道感染。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，但目前**沒有任何臨床試驗**，檢索到的文獻也沒有支持療效，反而多為肺纖維化等安全性警訊。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 泌尿道感染（香港許可證資料未提供適應症文字，此為藥物的既有用途） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L4（證據包評定；實際上無支持療效的研究，文獻僅為安全性訊號） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

**目前這個預測缺乏合理的機轉支持。**

Nitrofurantoin 是抗菌藥，作用是透過反應性中間產物破壞細菌的核糖體蛋白與 DNA。目前沒有已知的抗發炎或免疫調節機轉，能解釋它對類風濕性關節炎的作用。

TxGNN 分數雖高達 99.89%，但檢索到的文獻並不支持。這些論文把 nitrofurantoin 描述為類風濕性關節炎患者的安全疑慮，包括藥物引起的肺纖維化、與 methotrexate 併用造成不可逆肺纖維化，以及抗生素暴露與類風濕性關節炎發作的關聯。這些是負面或傷害訊號，不是治療訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort | Scientific Reports | 以英國 CPRD 資料做自身對照病例系列，探討抗生素使用與類風濕性關節炎發作的關聯，屬風險評估而非療效 |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | 94 歲類風濕性關節炎患者長期使用 methotrexate，再加用 nitrofurantoin 後發生不可逆肺纖維化 |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | 回顧藥物引起的肺纖維化，nitrofurantoin 列為致病藥物之一 |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du Praticien | 回顧藥物引起的間質性肺病，nitrofurantoin 列為相關抗生素 |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | 類風濕性關節炎合併間質性肺纖維化住院患者預後不佳，與 nitrofurantoin 療效無關 |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Case report | Cureus | 自體免疫肝炎個案，鑑別診斷需排除 nitrofurantoin 等藥物引起的肝損傷 |

以上文獻沒有任何一篇顯示 nitrofurantoin 對類風濕性關節炎有治療效果。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-05065 | NITROFURANTOIN TAB 50MG (SYNCO) | SYNCO (H.K.) LIMITED |
| HK-43743 | APO-NITROFURANTOIN TAB 100MG | HIND WING CO LTD |
| HK-50570 | UROBID CAP | EUROPHARM LAB CO LTD |
| HK-43231 | UROBILIN CAP | EUROPHARM LAB CO LTD |
| HK-50571 | UROSINA CAP | EUROPHARM LAB CO LTD |

## 安全性考量

原廠仿單的警語與禁忌症資料尚未取得，請參考原廠仿單。以下為文獻中出現的安全性訊號：

- **肺毒性**：多篇文獻將 nitrofurantoin 列為藥物引起肺纖維化與間質性肺病的致病藥物。
- **藥物交互作用**：與 methotrexate 併用曾造成不可逆肺纖維化（個案報告），而類風濕性關節炎患者常使用 methotrexate。
- **肝毒性**：有藥物引起肝損傷的鑑別診斷報告。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，文獻只顯示風險，且找不到合理的作用機轉。高 TxGNN 分數僅是知識圖譜的輸出。
- 該藥與類風濕性關節炎常用藥 methotrexate 併用有肺毒性疑慮，風險大於潛在益處。

其他預測適應症也同樣建議 Hold：

| 預測適應症 | 證據等級 | 說明 |
|-----------|---------|------|
| 糖尿病腎病變 | L4 | 文獻僅顯示 nitrofurantoin 可用於糖尿病患者的泌尿道感染，並非治療腎病變；腎功能不全時療效降低、毒性風險升高 |
| 其他兩項罕見遺傳疾病 | L5 | 無臨床試驗，檢索到的文獻多為疾病表型的關鍵字命中，並未提及 nitrofurantoin |
| 短指併指症候群 | L5 | 無臨床試驗與文獻，也沒有藥理上的關聯 |

**若要推進需要：**
- 取得 nitrofurantoin 在類風濕性關節炎的前臨床或機轉證據，例如抗發炎或免疫調節作用。
- 取得香港衛生署仿單的警語與禁忌症，完成 S1 安全性篩選。
- 補齊 DrugBank 的作用機轉資料。
- 若無新證據，建議不再投入資源。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

