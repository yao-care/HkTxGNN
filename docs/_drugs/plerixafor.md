---
layout: default
title: Plerixafor
parent: 僅模型預測 (L5)
nav_order: 595
evidence_level: L5
indication_count: 5
---

# Plerixafor
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

# Plerixafor：原適應症資料缺口下的 Indolent Plasma Cell Myeloma 再利用預測

## 一句話總結

Plerixafor（DrugBank ID: DB06809）目前尚未於當地上市，原始適應症與作用機轉資料也尚未補齊（列為資料缺口）。
TxGNN 模型預測它可能對**惰性漿細胞骨髓瘤 (Indolent Plasma Cell Myeloma)** 有效，預測分數達 **99.97%**，
但目前**無任何臨床試驗或文獻**佐證，證據等級僅為 **L5（純模型預測）**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（Evidence Pack 未提供，藥物尚未於當地上市） |
| 預測新適應症 | Indolent Plasma Cell Myeloma（惰性漿細胞骨髓瘤） |
| TxGNN 預測分數 | 99.97%（rank 956） |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料，原始適應症紀錄也是空的，這兩項都已被標記為資料缺口（DG001、DG002）。
值得注意的是，本 Evidence Pack 中其他候選適應症（rank 2-4）的機轉分析提到 Plerixafor 具 **CXCR4 拮抗劑**活性，
這項資訊可作旁證參考，但**尚未**針對「indolent plasma cell myeloma」這個候選進行正式的機轉關聯分析
（`repurposing_rationale.mechanistic_link` 標示為 pending）。

CXCR4/CXCL12 軸在漿細胞於骨髓微環境中的滯留與遷移確有文獻描述的角色，理論上與漿細胞相關疾病存在潛在關聯，
但這僅是推論方向，並非本檔案中已完成的正式評估。

由於原適應症紀錄缺失、機轉分析未完成，且完全沒有臨床試驗或文獻資料，此預測目前僅停留在模型分數層級，
機轉合理性仍需待 MOA 資料補齊（DrugBank API 查詢）後才能正式判定。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

目前未於當地上市，無許可證資料。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 完全缺乏臨床試驗、文獻與當地上市/許可證資料，加上原適應症與作用機轉均列為資料缺口（DG001 為 Blocking、DG002 為 High），現階段不具備進入安全性初評（S1）的基礎。
- 本次評估另有 4 個候選適應症（CMM7、pediatric leptomeningeal melanoma、epithelioid cell uveal melanoma、bronchitis）分數更低，且已判定為 L5/Hold（多屬知識圖譜雜訊或機轉證據不足），故未於本報告主體呈現。

**若要推進需要：**
- 透過 DrugBank API 補齊作用機轉資料（DG002）
- 補齊當地仿單警語/禁忌，解除 S1 安全性初評的阻塞條件（DG001，Blocking）
- 針對 indolent plasma cell myeloma 完成正式機轉關聯分析（目前為 pending）
- 持續追蹤 ClinicalTrials.gov／PubMed 是否新增相關證據
- 補充原始適應症及上市登記資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

