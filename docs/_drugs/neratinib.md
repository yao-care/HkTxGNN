---
layout: default
title: Neratinib
parent: 高證據等級 (L1-L2)
nav_order: 603
evidence_level: L2
indication_count: 10
---

# Neratinib
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Neratinib：從 HER2 陽性乳癌到 Normal Breast-like 亞型乳癌

## 一句話總結

Neratinib 是不可逆的 pan-HER 酪胺酸激酶抑制劑，原本用於 HER2 陽性乳癌，包括早期乳癌的延長輔助治療。
TxGNN 模型預測它可能對 **Normal Breast-like 亞型乳癌 (normal breast-like subtype of breast carcinoma)** 有效。
目前只有 **1 個已完成的 Phase 2 臨床試驗**，且沒有直接相關文獻，證據薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HER2 陽性乳癌（依 Evidence Pack 的機轉說明推斷；香港許可證未列適應症文字） |
| 預測新適應症 | Normal Breast-like 亞型乳癌 (normal breast-like subtype of breast carcinoma) |
| TxGNN 預測分數 | 99.68% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

DrugBank 目前缺乏詳細的作用機轉資料。根據 Evidence Pack 的說明，Neratinib 是不可逆的 pan-HER（EGFR/HER2/HER4）酪胺酸激酶抑制劑，其療效已在 HER2 陽性乳癌中獲得證實。

新舊適應症同屬乳癌，但關聯並不直接。「Normal breast-like」是知識圖譜（KG）本體論的對應標籤，和唯一的試驗族群並不吻合。該試驗 NCT01670877 收的是 HER2 未擴增、但帶有 HER2 突變的轉移性乳癌，機轉上可能是 ERBB2 活化突變，並合併 fulvestrant 使用。

因此，這個預測比較適合視為「值得研究的問題」，而不是已有充分證據支持的新用途。目前只有 Phase 2 證據，且沒有相關文獻。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01670877](https://clinicaltrials.gov/study/NCT01670877) | Phase 2 | 完成 | 56 | Neratinib 單用或合併 fulvestrant，用於 HER2 未擴增但有 HER2 突變的轉移性乳癌；結果未在資料中提供。與「normal breast-like」族群僅間接對應 |

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66416 | NERLYNX TABLETS 40MG | — | — |

廠商為 PIERRE FABRE DERMO-COSMETIQUE HONG-KONG LIMITED。許可證資料未提供劑型與適應症文字。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（pan-HER 酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單；Evidence Pack 特別提到需管理腹瀉 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **腹瀉**：文獻（PMID 39153126）指出，Neratinib 的胃腸道副作用明顯，常導致停藥。Evidence Pack 建議搭配腹瀉預防性處置。

其餘安全性資訊（警語、禁忌症、藥物交互作用）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有 1 個 Phase 2 試驗支持，且族群與「normal breast-like」標籤只是間接對應，也沒有文獻佐證。
- 香港的安全性資料仍有缺口（Evidence Pack 標為 Blocking），無法進入安全性篩選。

**若要推進需要：**
- 釐清「normal breast-like」在臨床上對應哪一群病人，或與 HR 陽性乳癌的預測項目合併評估。
- 取得 NCT01670877 的結果與 HER2 突變族群的療效數據。
- 補上香港衛生署仿單的警語與禁忌症，以及 DrugBank 的作用機轉資料。
- 補做 Neratinib 與新適應症的相關文獻檢索。

**補充：** 同一份 Evidence Pack 中，預測排名 2、3 的 HR 陽性與 HR 陰性乳癌證據較強（ExteNET Phase 3 等，建議 Proceed with Guardrails）。不過這些屬於 HER2 陽性族群，已是核准適應症，不算真正的老藥新用。

*本報告結果僅供研究參考，不構成醫療建議。預測適應症需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

