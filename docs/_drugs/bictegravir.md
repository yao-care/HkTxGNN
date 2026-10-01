---
layout: default
title: Bictegravir
parent: 中證據等級 (L3-L4)
nav_order: 117
evidence_level: L4
indication_count: 3
---

# Bictegravir
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Bictegravir：從 HIV-1 感染到猴免疫缺乏病毒感染

## 一句話總結

Bictegravir 是 HIV-1 整合酶股轉移抑制劑（INSTI），為 Biktarvy 複方的成分之一，原本用於 HIV-1 感染治療。
TxGNN 模型預測它可能對**猴免疫缺乏病毒感染 (Simian Immunodeficiency Virus Infection)** 有效。
目前**沒有臨床試驗**，只有 **3 篇前臨床或機轉文獻**支持，SIV 主要價值是作為 HIV 的轉譯研究模型。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明適應症；依藥物類別推論為 HIV-1 感染 |
| 預測新適應症 | 猴免疫缺乏病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。不過 Bictegravir 屬於 HIV-1 整合酶股轉移抑制劑，這類藥物的機轉已被充分證實：抑制病毒整合酶，阻止病毒 DNA 插入宿主基因組。

SIV 的整合酶在結構上與 HIV-1 整合酶相近，文獻也支持這一點：
- Bictegravir 在體外對 SIVmac239 有活性，包括對 INSTI 產生抗藥性的變異株。
- HIV/SIV intasome 結構研究顯示，兩者的抑制劑結合方式相似。

需要注意的是，SIV 是非人類靈長類的病毒，不是人類適應症。這個預測的價值主要在於動物模型與轉譯研究，例如測試 HIV 治療與治癒策略，而不是替人類開出新用途。

TxGNN 分數很高，但模型可能只是反映知識圖譜中 HIV/SIV 相鄰的關係，不能視為獨立證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | 體外抗病毒研究 | Antimicrob Agents Chemother | Bictegravir 與 Cabotegravir 對抗 INSTI 的 SIVmac239 及 HIV-1 變異株仍具抗病毒活性 |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Review（結構生物學） | FEBS J | 整理 HIV/SIV intasome 結構，說明 INSTI 結合方式與病毒逃脫機轉；Bictegravir 對抗藥性有較高的基因屏障 |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | 前臨床動物模型 | Front Immunol | 建立可同時測試 SIV 與 HIV 抗病毒策略的人源化小鼠模型 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65914 | BIKTARVY TABLETS（廠商：GILEAD SCIENCES HONG KONG LIMITED） | 未載明 | 未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據只有前臨床研究與機轉研究（L4），沒有任何臨床試驗。
- SIV 是非人類病毒，不屬於人類藥物再利用的臨床適應症。
- 建議把它當作研究問題：Bictegravir 可作為 HIV 治療與治癒研究的動物模型工具藥，而不是臨床開發方向。

**若要推進需要：**
- 釐清研究目的：若目標是動物模型研究，需另行設計非人類靈長類或人源化小鼠的實驗。
- 補齊 DrugBank 的作用機轉資料，並取得香港衛生署仿單的警語與禁忌症。
- 本次預測名單中的另外兩項（貓後天免疫缺乏症候群、伴隨共濟失調步態的神經發育障礙）都沒有任何試驗或文獻支持，也沒有可信的機轉連結，不建議進一步投入。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

