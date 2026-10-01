---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 370
evidence_level: L5
indication_count: 5
---

# Filgrastim
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

# Filgrastim：從嗜中性白血球相關治療到血小板釋放異常疾病

## 一句話總結

Filgrastim 是 G-CSF（顆粒球群落刺激因子），主要作用於嗜中性白血球譜系。本次提供的香港許可證資料未載明原適應症。
TxGNN 模型預測它可能對**血小板原發性釋放異常 (Primary Release Disorder of Platelets)** 有效，但目前只有 **0 個直接相關臨床試驗**和 **1 篇間接相關文獻**，且機轉上找不到合理連結。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 血小板原發性釋放異常 (Primary Release Disorder of Platelets) |
| TxGNN 預測分數 | 99.998% |
| 證據等級 | L4（僅有間接文獻，未直接檢驗此疾病） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Filgrastim 是 G-CSF 類生物製劑，已知主要作用在嗜中性白血球譜系，促進其增生與分化。

血小板原發性釋放異常是血小板顆粒分泌或釋放功能缺陷所致。G-CSF 不參與血小板顆粒分泌的調控，也不是促血小板生成劑，兩者之間沒有已知的機轉關聯。

這個高分預測較可能是知識圖譜中節點距離相近所產生的假象，而非真正的藥理連結。原 MOA 資料缺漏，因此無法進一步交叉驗證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | 健康捐贈者幹細胞動員研究（類型未明確） | Frontiers in Immunology | G-CSF 動員健康捐贈者周邊血幹細胞時，會優先動員特定淋巴球亞群。與血小板疾病無直接關係 |

## 香港上市資訊

香港共有 8 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-45427 | NEUPOGEN PRE-FILLED SYRINGE 0.3MG/0.5ML | AMGEN HONG KONG LIMITED |
| HK-60951 | NIVESTIM SOLUTION FOR INJECTION/INFUSION IN PRE-FILLED SYRINGE 300MCG/0.5ML | PFIZER CORPORATION HONG KONG LIMITED |
| HK-64300 | ZARZIO SOLUTION FOR INJECTION OR INFUSION IN PRE-FILLED SYRINGE 48MU/0.5ML | SANDOZ HONG KONG LIMITED |
| HK-35878 | NEUPOGEN INJ 0.3MG/ML | AMGEN HONG KONG LIMITED |
| HK-68517 | ACCOFIL SOLUTION FOR INJECTION OR INFUSION IN PRE-FILLED SYRINGE 30MU/0.5ML | JACOBSON MARKETING LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測缺乏機轉依據與直接臨床證據。唯一的文獻是健康捐贈者幹細胞動員研究，並未檢驗 G-CSF 對此疾病的作用。
- 同一藥物的其他預測（pseudo-von Willebrand disease、Glanzmann thrombasthenia、Scott syndrome、先天性血小板減少出血性疾病）同樣無機轉支持，建議一併 Hold。
- 這些疾病中即使用到 G-CSF，也僅是移植動員或支持性用途，並非針對疾病本身治療。

**若要推進需要：**
- 補齊 DrugBank 的作用機轉（MOA）資料，重新評估機轉連結
- 取得香港衛生署仿單，確認警語、禁忌與核准適應症
- 尋找 G-CSF 用於血小板功能異常的直接臨床或前臨床證據，否則不建議投入資源

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

