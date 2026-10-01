---
layout: default
title: Desvenlafaxine
parent: 僅模型預測 (L5)
nav_order: 258
evidence_level: L5
indication_count: 10
---

# Desvenlafaxine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Desvenlafaxine：從 SNRI 類抗憂鬱藥到強迫症

## 一句話總結

Desvenlafaxine 是 venlafaxine 的活性代謝物，屬於血清素-正腎上腺素再吸收抑制劑（SNRI）。
TxGNN 模型預測它可能對**強迫症 (Obsessive-Compulsive Disorder, OCD)** 有效。
目前有 **2 個相關臨床試驗**和 **4 篇文獻**，但沒有任何一項直接以 desvenlafaxine 治療強迫症，直接證據仍缺。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 強迫症 (Obsessive-Compulsive Disorder) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L4（僅有機轉推論與母藥 venlafaxine 的間接證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知藥理，desvenlafaxine 是 SNRI 類抗憂鬱藥，也是 venlafaxine 的活性代謝物。

強迫症已知對血清素系統藥物有反應，包括 clomipramine 和 SSRI，因此在類別層級上，SNRI 用於強迫症有合理的機轉連結。

不過，目前的直接臨床證據來自母藥 venlafaxine，而非 desvenlafaxine 本身。Venlafaxine 與 paroxetine 的雙盲比較（n=150）是最接近的證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03299166](https://clinicaltrials.gov/study/NCT03299166) | Phase 2/3 | 完成 | 426 | 評估 troriluzole 輔助治療對 SSRI、clomipramine、venlafaxine 或 desvenlafaxine 反應不足的強迫症患者。試驗藥物不是 desvenlafaxine |
| [NCT01527786](https://clinicaltrials.gov/study/NCT01527786) | Phase 3 | 完成 | 25 | Desvenlafaxine 用於產後憂鬱症的功能恢復先導研究。藥物相符但適應症不同，無法提供強迫症療效證據 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [14624187](https://pubmed.ncbi.nlm.nih.gov/14624187/) | 2003 | RCT | J Clin Psychopharmacol | 首個 SNRI 用於強迫症的雙盲比較，150 位患者，比較 venlafaxine 與 paroxetine 的療效和耐受性 |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Review | Expert Opin Pharmacother | 回顧具明顯血清素作用的抗憂鬱藥在強迫症的雙盲研究，支持血清素系統的關鍵角色 |
| [36686097](https://pubmed.ncbi.nlm.nih.gov/36686097/) | 2022 | Review | Cureus | 產後憂鬱症的綜合回顧，提到其可能導致母親日後發生強迫症和焦慮，與 desvenlafaxine 療效無直接關聯 |
| [40224942](https://pubmed.ncbi.nlm.nih.gov/40224942/) | 2025 | 臨床試驗（非強迫症） | Psychiatry Clin Psychopharmacol | Risperidone 增強治療抗憂鬱藥難治型身體症狀障礙，並非針對強迫症 |

## 香港上市資訊

共 7 張許可證，以下列出 5 張：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68804 | DESPAXOR EXTENDED-RELEASE TABLETS 50MG | SYNCO (H.K.) LIMITED |
| HK-67626 | APO-DESVENLAFAXINE EXTENDED-RELEASE TABLETS 50MG | HIND WING CO LTD |
| HK-65147 | PRISTIQ EXTENDED-RELEASE TABLETS 25MG | PFIZER CORPORATION HONG KONG LIMITED |
| HK-68803 | DESPAXOR EXTENDED-RELEASE TABLETS 100MG | SYNCO (H.K.) LIMITED |
| HK-59473 | PRISTIQ EXTENDED-RELEASE TAB 50MG | PFIZER CORPORATION HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 強迫症預測只有類別層級的機轉推論。現有的直接證據來自 venlafaxine，沒有 desvenlafaxine 用於強迫症的試驗。
- 香港仿單的警語與禁忌資料尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌與適應症資料。
- 補充作用機轉資料（例如查詢 DrugBank）。
- 尋找或設計 desvenlafaxine 用於強迫症的直接臨床研究，並與 venlafaxine 的證據做比較。

**其他預測適應症的參考：**
- **持續性憂鬱症 (Dysthymic Disorder)**：有 3 個 desvenlafaxine 相關試驗，其中 Phase 4 安慰劑對照（NCT01537068，n=59）為直接證據，但規模小、未提供結果，證據等級為 L2。
- **憂鬱型憂鬱症 (Melancholia)**：這項預測似乎對應重度憂鬱症，而該藥已在此適應症上市，較像原適應症而非新用途，需對照仿單確認。
- **人格障礙類、Ohdo 症候群、嬰兒良性陣發性斜頸**：沒有任何臨床試驗或文獻，也沒有合理機轉，可能是知識圖譜的假象。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

