---
layout: default
title: Valsartan
parent: 中證據等級 (L3-L4)
nav_order: 909
evidence_level: L4
indication_count: 5
---

# Valsartan
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

# Valsartan：從血管張力素 II 受體阻斷劑到惡性高血壓性腎病變

## 一句話總結

Valsartan 是血管張力素 II 第一型受體（AT1）阻斷劑，已在香港上市。本次資料未提供原適應症。
TxGNN 模型預測它可能對**惡性高血壓性腎病變 (Malignant Hypertensive Renal Disease)** 有效。
目前**沒有臨床試驗**，僅有 **1 篇**間接相關的前臨床文獻，且該文獻研究的不是 valsartan。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 惡性高血壓性腎病變 (Malignant Hypertensive Renal Disease) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。已知 Valsartan 是 AT1 受體阻斷劑。腎素－血管張力素系統（RAS）過度活化，是惡性高血壓及其腎臟損傷的可能成因之一，因此阻斷 AT1 在生物學上說得通。

不過，目前唯一的支持文獻（PMID 24368192）研究的是 avosentan，一種內皮素受體拮抗劑，不是 valsartan，也不是其他 ARB，最多只能算機轉相近。另有 1 篇文獻（PMID 11560862）指出 AT1 阻斷可預防致死性惡性高血壓，但它被歸在另一個預測適應症「惡性腎血管性高血壓」之下，且同樣是類別層級的前臨床證據。

TxGNN 的分數（0.9997）只是計算模型的預測，不是臨床證據。因為缺少原適應症與機轉資料，也無法和原適應症的關聯性做比對。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | 前臨床／實驗（依標題推斷） | Pharmacological Research | 在表現人類腎素與血管張力素原基因的雙基因轉殖大鼠中，avosentan 在不引起水分滯留的劑量下，對高血壓性腎病變具保護作用。研究藥物為內皮素拮抗劑，非 valsartan。 |

## 香港上市資訊

共 20 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-62376 | PMS-VALSARTAN TABLETS 320MG | TRENTON-BOMA LTD |
| HK-60971 | VALSACOR FILM-COATED TABLETS 80MG | TRENTON-BOMA LTD |
| HK-62346 | PMS-VALSARTAN TABLETS 40MG | TRENTON-BOMA LTD |
| HK-60970 | VALSACOR FILM-COATED TABLETS 160MG | TRENTON-BOMA LTD |
| HK-66401 | VALSARTAN TEVA TABLETS 80MG | TEVA PHARMACEUTICAL HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。本次未取得香港衛生署仿單的警語與禁忌資料，藥物交互作用查詢也無結果。

若未來評估相關的腎血管性高血壓，需特別注意：雙側腎動脈狹窄的患者使用 ARB 可能誘發急性腎損傷，需做專門的安全性審查。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何針對 valsartan 的臨床試驗，唯一的文獻是另一類藥物（內皮素拮抗劑）的動物研究。
- 目前只有 AT1 阻斷的機轉合理性與模型分數，證據層級停留在研究假設（L4）。
- 缺少仿單安全資料，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症。
- 從 DrugBank 補充作用機轉資料。
- 搜尋 valsartan 或其他 ARB 用於惡性高血壓腎病變的直接證據（動物實驗或人體研究）。
- 評估目標族群（惡性高血壓、可能合併腎功能受損）使用 ARB 的腎功能與血鉀風險。

**其他預測適應症（供參考）：** 惡性腎血管性高血壓（L4，有類別層級前臨床文獻）、非特定多因子肺高壓、缺氧／肺病相關肺高壓、Braddock 症候群（皆為 L5，僅有模型預測，所列文獻與 valsartan 無關）。

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

