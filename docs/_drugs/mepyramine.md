---
layout: default
title: Mepyramine
parent: 中證據等級 (L3-L4)
nav_order: 555
evidence_level: L4
indication_count: 4
---

# Mepyramine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **4** 個
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

# Mepyramine：從第一代 H1 抗組織胺到過敏性蕁麻疹

## 一句話總結

Mepyramine 是第一代組織胺 H1 受體拮抗劑，在香港以 2% 乳膏形式上市。
TxGNN 模型預測它可能對**過敏性蕁麻疹 (Allergic Urticaria)** 有效。
目前沒有臨床試驗，只有 **5 篇文獻**，其中 1 篇是犬隻血管性水腫的獸醫研究，其餘為前臨床或機轉研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 過敏性蕁麻疹 (Allergic Urticaria) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，資料庫中的原適應症與 MOA 欄位皆為空白。
從文獻可知，Mepyramine 是第一代 H1 受體拮抗劑，這類藥物用來緩解過敏反應與蕁麻疹。

過敏性蕁麻疹由肥大細胞釋放組織胺所驅動。阻斷 H1 受體是對應這條路徑的機轉，因此預測在藥理上合理。

不過，現有資料沒有任何人體研究。TxGNN 的高分只是模型預測，不算證據。另外，原適應症不明，無法確認這個用途是否已在仿單上核准。推進前應先查證標示適應症，再判定是否屬於真正的再利用。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21033572](https://pubmed.ncbi.nlm.nih.gov/21033572/) | 2010 | 獸醫臨床研究（隨機分組） | Pol J Vet Sci | 27 隻血管性水腫犬隻，分為治療組（15 隻）與安慰劑組（12 隻），結論認為 Mepyramine 可能有幫助 |
| [34758144](https://pubmed.ncbi.nlm.nih.gov/34758144/) | 2021 | 前臨床機轉研究 | FASEB J | Mepyramine 可直接阻斷痛覺神經的電壓門控鈉通道，可能是外用止痛作用的機轉 |
| [18222495](https://pubmed.ncbi.nlm.nih.gov/18222495/) | 2008 | 前臨床體外研究 | Neuropharmacology | Mepyramine 與 diphenhydramine 會抑制 KCNQ/M 鉀通道，可能與過量時的神經毒性有關 |
| [34387278](https://pubmed.ncbi.nlm.nih.gov/34387278/) | 2021 | 體外受體親和力評估 | Curr Opin Allergy Clin Immunol | 評估乾眼症用藥的受體親和力，與蕁麻疹的關聯間接 |
| [29371669](https://pubmed.ncbi.nlm.nih.gov/29371669/) | 2018 | 體外工具開發 | Sci Rep | 開發螢光 H1 受體配體以研究結合動力學，屬研究工具，並非療效證據 |

## 香港上市資訊

許可證資料中的劑型與核准適應症皆為空白。品名顯示以下皆為 2% 乳膏。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-57757 | TERAMIN CREAM 2% | EUROPHARM LAB CO LTD |
| HK-30055 | METOPIC CREAM 2% | EUROPHARM LAB CO LTD |
| HK-57756 | SYNPYRAMINE CREAM 2% | EUROPHARM LAB CO LTD |
| HK-23629 | MEPYRAMINE CREAM 2% | MARCHING PHARMACEUTICAL LIMITED |
| HK-49356 | PROTAMIN CREAM 2% | MARCHING PHARMACEUTICAL LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉上合理，但沒有任何人體研究，證據等級僅 L4，僅有的疾病相關資料是犬隻研究。
- 香港仿單的警語與禁忌資料缺口屬於阻斷性問題（DG001），無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，確認標示適應症（是否已含蕁麻疹）、警語與禁忌
- 補齊 Mepyramine 的作用機轉資料（DrugBank）
- 檢索人體臨床研究，尤其是外用或口服 Mepyramine 用於蕁麻疹的研究
- 確認劑型與給藥途徑：香港現有產品皆為外用乳膏，需評估是否適用於蕁麻疹
- 其他預測適應症目前也建議維持 Hold：鼻腔疾病（L4，僅有其他抗組織胺的動物模型文獻，且需先界定具體疾病）、急性喉咽炎與寒冷性蕁麻疹（L5，無任何研究）

本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

