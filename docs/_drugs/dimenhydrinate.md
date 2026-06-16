---
layout: default
title: Dimenhydrinate
parent: 中證據等級 (L3-L4)
nav_order: 237
evidence_level: L4
indication_count: 2
---

# Dimenhydrinate
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

# Dimenhydrinate：從暈動症到過敏性蕁麻疹

## 一句話總結

Dimenhydrinate 是由 Diphenhydramine（第一代 H1 受體拮抗劑）與 8-chlorotheophylline（腺苷拮抗劑）組成的複方藥物，傳統上用於預防和治療暈動症（動暈症）及噁心嘔吐。TxGNN 模型預測它可能對**過敏性蕁麻疹（Allergic Urticaria）** 有效，目前有 **0 個臨床試驗**和 **1 篇文獻**（動物藥動學研究）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 暈動症（Motion Sickness）、噁心／嘔吐 |
| 預測新適應症 | 過敏性蕁麻疹（Allergic Urticaria） |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，Dimenhydrinate 是 Diphenhydramine 與 8-chlorotheophylline 的複合鹽。Diphenhydramine 為第一代 H1 受體拮抗劑，可競爭性抑制組織胺與 H1 受體的結合；8-chlorotheophylline 則為腺苷拮抗劑，主要作用是拮抗鎮靜效果，以維持藥物的清醒狀態。

過敏性蕁麻疹的核心病理機轉為：過敏原觸發肥大細胞脫顆粒，釋放大量組織胺，引起 H1 受體介導的血管擴張、血漿外滲及瘙癢。Diphenhydramine 作為 Dimenhydrinate 的活性成分，理論上可透過阻斷 H1 受體來抑制這些反應，此為 TxGNN 預測的機轉基礎。

然而，有幾點重要限制需要評估：其一，臨床蕁麻疹治療指引目前以第二代 H1 抗組織胺（如 Cetirizine、Loratadine）為一線標準療法，鎮靜副作用更低；其二，8-chlorotheophylline 成分對蕁麻疹無已知療效，可能帶來額外的中樞興奮副作用；其三，目前完全缺乏 Dimenhydrinate 本身針對此適應症的直接臨床資料，預測僅能透過其活性成分間接推論。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | 藥動學研究 | Veterinary Dermatology | 比較健康犬口服及靜脈注射 Diphenhydramine 與口服 Dimenhydrinate 後的藥動學；發現 Dimenhydrinate 口服吸收優於單純 Diphenhydramine，並觀察了組織胺誘發風團的藥效反應，提示 Dimenhydrinate 作為 Diphenhydramine 的給藥形式具有潛在優勢 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
目前僅有 1 篇動物藥動學研究提供間接支持，完全缺乏 Dimenhydrinate 用於過敏性蕁麻疹的人體臨床證據；加之現行治療指引以第二代非鎮靜抗組織胺為標準療法，Dimenhydrinate 的鎮靜特性與複合成分構成應用上的實質障礙，短期內不具推進條件。

**若要推進需要：**
- 補充 Dimenhydrinate 的完整作用機轉資料（建議查詢 DrugBank API，填補 DG002）
- 取得原廠仿單的安全性警語與禁忌症（建議下載 TFDA 或 WHO/EMA 仿單 PDF，填補 DG001）
- 設計 Dimenhydrinate 與第二代抗組織胺的頭對頭（head-to-head）比較研究方案
- 評估 8-chlorotheophylline 成分在蕁麻疹適應症中的獨立風險效益比
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

