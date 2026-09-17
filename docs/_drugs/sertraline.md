---
layout: default
title: Sertraline
parent: 僅模型預測 (L5)
nav_order: 683
evidence_level: L5
indication_count: 5
---

# Sertraline
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

# Sertraline：老藥新用評估 — Schizoid Personality Disorder（類分裂性人格障礙）

## 一句話總結

Sertraline（DB01104）是 SSRI 類藥物，但此 Evidence Pack 未提供香港上市資料與原始核准適應症（未上市，0 張許可證）。
TxGNN 模型排名第一預測其可能對**類分裂性人格障礙 (Schizoid Personality Disorder)** 有效，
但目前**無任何臨床試驗或文獻**支持，證據等級為最低的 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（Evidence Pack 中 `original_indications` 為空） |
| 預測新適應症 | Schizoid Personality Disorder（類分裂性人格障礙） |
| TxGNN 預測分數 | 99.93%（rank 1876） |
| 證據等級 | L5（無臨床試驗、無文獻，純模型預測） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（Data Gap DG002，嚴重度 High）。根據該預測適應症的機轉推理，SSRI 理論上可能改善合併之焦慮/情緒症狀，但 schizoid PD 核心特徵為社交退縮與情感疏離，缺乏血清素路徑與此人格病理直接關聯的機轉證據，此預測純屬 TxGNN 知識圖譜統計關聯，無實際生物學支持。

值得注意的是，本次預測清單中前 4 名（rank 1876-1879）的 TxGNN 分數幾乎完全相同（0.9993353486061096），且全部集中於人格障礙光譜（schizoid、schizotypal、histrionic、paranoid PD）。這顯示模型在此分數區間對個別人格障礙的鑑別力偏低，較可能反映 sertraline 在知識圖譜中與精神科節點的廣泛連結，而非針對特定人格障礙的精確預測。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

此藥物目前未在香港上市，無許可證資料。

## 其他預測適應症總覽

由於此候選為多適應症評估（candidate_id: TW-DB01104-multi），列出全部 5 個預測結果供比較：

| 排名 | 預測適應症 | 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|------|---------|---------|------|
| 1 | Schizoid personality disorder | 99.93% | L5 | S0 | Hold |
| 2 | Schizotypal personality disorder | 99.93% | L3 | S1 | **Research Question** |
| 3 | Histrionic personality disorder | 99.93% | L4 | S0 | Hold |
| 4 | Paranoid personality disorder | 99.93% | L4 | S0 | Hold |
| 5 | Benign paroxysmal torticollis of infancy | 99.55% | L5 | S0 | Hold（判斷為知識圖譜雜訊，與 SSRI 機轉無生物學合理性） |

其中僅 rank 2（schizotypal PD）有 1 個已完成小型臨床試驗（NCT00169988, n=8, sertraline 單用 vs. 併用 risperidone）及 1 篇 Case Report，達到 L3/S1，是唯一值得列為研究假說的方向；其餘皆停留在 Hold。

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 需特別注意：TFDA/香港仿單警語與禁忌症資料缺口（DG001）被標記為 **Blocking** 等級，其影響為「無法進入 S1 安全性初評」——這是不論證據等級高低都必須優先解決的硬性限制。

## 結論與下一步

**決策：Hold**

**理由：**
- 安全性資料缺口為 Blocking 等級（DG001），無法進入 S1 安全性初評，是決策的硬性限制。
- 排名第一的預測適應症（schizoid PD）證據等級僅 L5，無任何臨床試驗或文獻支持，機轉關聯亦薄弱。
- 此藥物在香港未上市（0 張許可證），需另行評估在地化路徑。

**若要推進需要：**
- 優先取得 TFDA/香港仿單完整警語與禁忌症資料（Blocking，須最先解決）
- 補充 Sertraline 作用機轉（MOA）資料（DG002）
- 若考慮唯一達 S1 的候選方向（schizotypal PD），需要更大樣本的臨床試驗佐證（現有試驗僅 n=8）
- 釐清香港上市策略（目前 0 張許可證，屬未上市藥物）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

