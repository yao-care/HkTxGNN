---
layout: default
title: Selenium
parent: 中證據等級 (L3-L4)
nav_order: 788
evidence_level: L4
indication_count: 1
---

# Selenium
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Selenium：從 未載明原適應症 到 硬化性膽管炎

## 一句話總結

Selenium（硒）在香港有 4 張上市許可證，劑型包含輸注濃縮液、注射液與口服溶液，但資料中未載明原適應症。
TxGNN 模型預測它可能對**硬化性膽管炎 (Sclerosing Cholangitis)** 有效，預測分數很高。
不過目前**沒有臨床試驗**，只有 **5 篇間接文獻**，且都沒有顯示療效，證據仍相當薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 硬化性膽管炎 (Sclerosing Cholangitis) |
| TxGNN 預測分數 | 99.04% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 尚未取得）。因此無法把預測連結到明確的藥物標靶，只能根據文獻做合理推測。

硒是麩胱甘肽過氧化酶 (glutathione peroxidase) 與其他硒蛋白的輔因子，參與抗氧化防禦。氧化壓力與膽汁淤積性肝病、肝纖維化有關，這是兩者之間可能的機轉連結。

現有文獻顯示，原發性硬化性膽管炎 (PSC) 患者的肝臟有硒與銅滯留，且脂溶性營養素攝取不足。這些發現指出 PSC 患者的微量元素狀態有改變，**並不代表補充硒有治療效果**。TxGNN 分數雖然高，但這是圖譜模型的預測，目前沒有任何文獻記載其治療機轉。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9053974](https://pubmed.ncbi.nlm.nih.gov/9053974/) | 1995 | 觀察性研究 | Scand J Gastroenterol | 研究 32 名 PSC 患者的微量元素代謝，發現肝臟有銅與硒滯留 |
| [39601354](https://pubmed.ncbi.nlm.nih.gov/39601354/) | 2025 | 觀察性研究 | Liver Int | PSC 患者的飲食品質不佳，脂溶性維生素攝取不足（與北歐營養建議比較） |
| [29148959](https://pubmed.ncbi.nlm.nih.gov/29148959/) | 2017 | 臨床個案 | JPEN | 一名 PSC 合併潰瘍性結腸炎、嚴重吸收不良的病人，探討靜脈營養與脂質乳劑的影響（間接相關） |
| [17109383](https://pubmed.ncbi.nlm.nih.gov/17109383/) | 2006 | 前臨床（小鼠） | Proteomics | 比較毒性誘發肝纖維化與硬化性膽管炎小鼠模型的肝臟蛋白質體變化 |
| [18941372](https://pubmed.ncbi.nlm.nih.gov/18941372/) | 2008 | 回顧 | Eur J Cancer Prev | 大腸直腸癌化學預防藥物回顧（間接相關） |

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68022 | SELENIUM AGUETTANT CONCENTRATE FOR SOLUTION FOR INFUSION 100MCG/10ML | HONG KONG MEDICAL SUPPLIES LTD |
| HK-63846 | SELESYN ORAL SOLUTION 100MCG/2ML | VIUTURE MEDICAL CONSULTANCY LIMITED |
| HK-63948 | SELESYN SOLUTION FOR INJECTION 500MCG/10ML | VIUTURE MEDICAL CONSULTANCY LIMITED |
| HK-63847 | SELESYN SOLUTION FOR INJECTION 100MCG/2ML | VIUTURE MEDICAL CONSULTANCY LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。目前尚未取得香港衛生署的仿單警語與禁忌資料，藥物交互作用查詢也無結果。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數很高，但沒有臨床試驗，文獻也只顯示 PSC 患者的微量元素狀態異常，沒有證據顯示補充硒能改善病情。
- 作用機轉與仿單安全性資料都還缺漏，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單（警語、禁忌、核准適應症）
- 從 DrugBank 補齊作用機轉資料
- 搜尋硒補充用於 PSC 或膽汁淤積性肝病的介入性研究（臨床試驗與文獻）
- 評估給藥途徑與 PSC 患者的相容性（目前尚待確認）
- 釐清 PSC 患者肝臟硒滯留的方向與意義，是缺乏、過量還是代謝異常，再決定補充是否合理

---

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

