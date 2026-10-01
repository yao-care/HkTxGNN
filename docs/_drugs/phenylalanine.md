---
layout: default
title: Phenylalanine
parent: 中證據等級 (L3-L4)
nav_order: 677
evidence_level: L4
indication_count: 2
---

# Phenylalanine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **2** 個
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

# Phenylalanine：從原適應症未載明到硬化性膽管炎

## 一句話總結

Phenylalanine（苯丙胺酸）在香港有 20 張許可證，但來源資料沒有記載原適應症。
TxGNN 模型預測它可能對**硬化性膽管炎 (Sclerosing Cholangitis)** 有效，但目前**沒有臨床試驗**，只有 **4 篇間接文獻**，且都不是治療效果的證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 硬化性膽管炎 (Sclerosing Cholangitis) |
| TxGNN 預測分數 | 99.43% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Phenylalanine 是必需胺基酸，在香港的許可證產品多為胺基酸輸液類製劑。但原適應症資料缺漏，無法確認其已證實的療效，也無法從原適應症推論機轉是否適用於硬化性膽管炎。

現有文獻只能提供間接線索。一項觀察性研究發現，血漿酪胺酸（苯丙胺酸的代謝產物）與原發性膽汁性膽管炎 (PBC) 及硬化性膽管炎 (PSC) 患者的疲勞有關。這只是症狀與代謝物的關聯，並非治療效果。

另外兩篇早期研究探討含苯丙胺酸或酪胺酸的細菌趨化肽（N-formyl peptide），涉及腸道細菌肽引發的發炎路徑。這與把游離苯丙胺酸當藥物使用是兩回事。

TxGNN 的高分（99.43%）僅是知識圖譜預測，不能視為臨床支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15790420](https://pubmed.ncbi.nlm.nih.gov/15790420/) | 2005 | 世代研究 | BMC Gastroenterology | 探討 PBC 與 PSC 患者的胺基酸模式異常及其與疲勞的關係（摘要僅載明研究目的） |
| [32025163](https://pubmed.ncbi.nlm.nih.gov/32025163/) | 2020 | 世代研究 | J Clin Exp Hepatol | 以質譜分析膽管癌與良性肝膽疾病的血清代謝體，尋找發病機轉線索與早期生物標記 |
| [8000512](https://pubmed.ncbi.nlm.nih.gov/8000512/) | 1994 | 動物研究 | J Gastroenterol | 大鼠結腸炎模型經直腸給予細菌趨化肽 fMLT 後誘發小膽管炎，用於研究 PSC 的發病機轉 |
| [2103382](https://pubmed.ncbi.nlm.nih.gov/2103382/) | 1990 | 實驗室檢測研究 | J Gastroenterol Hepatol | 以放射免疫分析證實人體內細菌趨化肽存在腸肝循環 |

這四篇都沒有評估苯丙胺酸作為治療藥物的效果。

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-57540 | AMINOL-S INJ | WINGS PHARMACEUTICAL LTD |
| HK-62100 | AMINOGEN-S SOLUTION FOR INFUSION | WINGS PHARMACEUTICAL LTD |
| HK-60459 | PAN-VASOL SOLUTION FOR INJECTION | FALKAN MEDICAL LIMITED |
| HK-58914 | PAN-AMIN G INJ | OTSUKA PHARMACEUTICAL (H.K.) LIMITED |
| HK-59165 | LA-FLAMING INJ. | FALKAN MEDICAL LIMITED |

共 20 張許可證，此處列出 5 張。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻也只有間接的症狀關聯、生物標記與動物模型研究，缺乏苯丙胺酸治療硬化性膽管炎的直接證據。
- 作用機轉與原適應症資料缺漏，無法驗證預測的合理性，且尚缺安全性資料，無法進入安全性篩選。

**若要推進需要：**
- 補齊 DrugBank 的作用機轉與原適應症資料
- 取得香港衛生署的仿單，釐清警語與禁忌
- 提出苯丙胺酸與硬化性膽管炎之間具體的機轉假說，並以前臨床研究驗證

**補充：** 第二項預測「先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)」（分數 99.26%）屬 L5，建議同樣為 Hold。目前找到的唯一試驗 NCT06227429 研究的是另一種藥物 nitisinone，且已撤回、零收案，沒有可信的機轉連結，高分可能只是知識圖譜的假象。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

