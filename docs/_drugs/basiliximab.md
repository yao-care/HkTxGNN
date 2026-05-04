---
layout: default
title: Basiliximab
parent: 中證據等級 (L3-L4)
nav_order: 83
evidence_level: L3
indication_count: 10
---

# Basiliximab
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Basiliximab：從器官移植排斥預防到漿細胞骨髓瘤

## 一句話總結

Basiliximab 是一種嵌合型抗 IL-2 受體（CD25）單株抗體，原本用於預防腎臟移植後的急性排斥反應。TxGNN 模型預測它可能對**漿細胞骨髓瘤 (Plasma Cell Myeloma)** 有效，目前有 **3 個臨床試驗**和 **3 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 預防腎臟移植後急性排斥反應（免疫抑制誘導治療） |
| 預測新適應症 | 漿細胞骨髓瘤 (Plasma Cell Myeloma) |
| TxGNN 預測分數 | 95.61% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 資料尚待補充）。根據藥物類別，Basiliximab 是一種嵌合型 IgG1κ 單株抗體，透過競爭性阻斷 IL-2 受體的 α 鏈（CD25）來抑制 IL-2 驅動的 T 細胞增殖，從而發揮免疫調節效果。

多發性骨髓瘤（MM）的腫瘤微環境中，調節性 T 細胞（Treg）大量積累，且持續高度表現 CD25。這些 Treg 細胞主動抑制抗骨髓瘤的免疫應答，形成免疫逃脫機制。在自體造血幹細胞移植（ASCT）的情境下，Basiliximab 可在移植前後靶向耗竭 Treg，解除對抗腫瘤免疫的抑制，進而強化移植後免疫重建的抗骨髓瘤效應（Treg depletion strategy）。在異體移植情境中，Basiliximab 亦可調控移植物抗宿主病（GvHD）與移植物抗骨髓瘤效應（GvM）之間的平衡。

已完成的 Phase 1 先導試驗（NCT01526096，n=30）直接在 MM 患者的 ASCT 情境中驗證了上述概念，研究結果於 2020 年發表於免疫腫瘤學期刊（PMID 31940591），提供了概念驗證的初步人體證據。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01526096](https://clinicaltrials.gov/study/NCT01526096) | Phase 1 | 完成 | 30 | 直接測試 ASCT 前 Basiliximab 耗竭 Treg 之可行性與安全性，為 MM 患者最核心的先導試驗，結果已正式發表（PMID 31940591） |
| [NCT00975975](https://clinicaltrials.gov/study/NCT00975975) | Phase 2 | 完成 | 17 | 非骨髓抑制性異體移植後使用 Basiliximab + 環孢素預防 GvHD，適應症含血液腫瘤（包含骨髓瘤），提供機轉驗證及間接安全性數據 |
| [NCT00594308](https://clinicaltrials.gov/study/NCT00594308) | — | 提前終止 | 10 | 比較 Basiliximab + 環孢素 vs 單用環孢素預防 GvHD，因提前終止（未達計畫樣本）而無有效效力數據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31940591](https://pubmed.ncbi.nlm.nih.gov/31940591/) | 2020 | Phase 1 臨床試驗報告 | Journal for Immunotherapy of Cancer | ASCT 後 Treg 快速重建與骨髓瘤進展相關；Basiliximab 耗竭 Treg 在 MM 患者中具可行性，為直接概念驗證 |
| [12476283](https://pubmed.ncbi.nlm.nih.gov/12476283/) | 2002 | 前瞻性病例系列 | Bone Marrow Transplantation | 17 名異體 SCT 後類固醇難治性急性 GvHD 患者（含骨髓瘤病例）使用 Basiliximab，耐受性良好，提供早期安全性數據 |
| [28320553](https://pubmed.ncbi.nlm.nih.gov/28320553/) | 2017 | 個案報告 | American Journal of Kidney Diseases | 4 例骨髓瘤緩解後腎臟移植病例（使用 Basiliximab 誘導），探討骨髓瘤根治後移植可行性 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
Phase 1 先導試驗（NCT01526096）已完成並發表，初步驗證 ASCT 情境下 Basiliximab 耗竭 Treg 的可行性與安全性，概念驗證具備初步基礎；然而目前僅有 n=30 的 Phase 1 數據，缺乏隨機對照 Phase 2/3 效力證據，尚不足以支持直接推進至臨床應用。

**若要推進需要：**
- 設計 Phase 2 隨機對照試驗，驗證 ASCT + Basiliximab 對 MM 患者無進展存活期（PFS）及總體存活期（OS）的效益
- 補充 Basiliximab 詳細作用機轉（MOA）資料，確認 Treg 耗竭效應的生物標記（如 CD4⁺CD25⁺Foxp3⁺ Treg 比例）
- 評估香港藥品取得可行性（目前未在港上市，需評估進口或研究用藥途徑）
- 完整安全性資料補充：仿單警語、禁忌症、與標準 MM 治療藥物（如 bortezomib、lenalidomide）的交互作用
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

