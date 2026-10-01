---
layout: default
title: Dimenhydrinate
parent: 中證據等級 (L3-L4)
nav_order: 276
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

# Dimenhydrinate：從（原適應症未載明）到過敏性蕁麻疹

## 一句話總結

Dimenhydrinate（茶苯海明）是 diphenhydramine 與 8-chlorotheophylline 的鹽類，屬第一代 H1 抗組織胺，香港已有上市產品，但資料庫未記載其原適應症。
TxGNN 模型預測它可能對**過敏性蕁麻疹 (Allergic Urticaria)** 有效，
目前**無臨床試驗**，僅有 **1 篇文獻**（藥物動力學研究，且為犬隻試驗），證據相當薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 過敏性蕁麻疹 (Allergic Urticaria) |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（列為研究問題） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。不過 Dimenhydrinate 是 diphenhydramine 的 8-chlorotheophylline 鹽，而 diphenhydramine 是已知的第一代 H1 受體拮抗劑。

過敏性蕁麻疹由組織胺介導：組織胺作用於皮膚血管與感覺神經上的 H1 受體，造成風團與搔癢。阻斷 H1 受體理論上可緩解這些症狀，因此機轉上合理。

但需注意，這個連結是**間接的**：證據建立在 diphenhydramine 成分與抗組織胺類別效應上，並非 dimenhydrinate 本身的療效研究。此外，一般指引多優先建議第二代 H1 抗組織胺，因為第一代藥物有鎮靜與抗膽鹼副作用。核心問題是：dimenhydrinate 相較於已核准的 diphenhydramine 或第二代抗組織胺，是否有任何優勢。

**另一個預測：冷蕁麻疹 (Cold Urticaria)**（分數 99.24%）目前沒有任何臨床試驗或文獻，僅為模型預測，證據等級 L5，維持 Hold。機轉上同樣可透過 H1 拮抗推論，但沒有臨床資料支持。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30779257](https://pubmed.ncbi.nlm.nih.gov/30779257/) | 2019 | 藥物動力學先導研究（犬） | Veterinary Dermatology | 比較犬隻口服/靜脈注射 diphenhydramine 與口服 dimenhydrinate 的藥動學及對組織胺誘發風團的藥效。顯示 dimenhydrinate 可經口讓 diphenhydramine 進入體循環，但**未在人類蕁麻疹中驗證療效** |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-33287 | GRAFER TAB 50MG | 未載明 | 未載明 |
| HK-35110 | UNI-HYDRIN TAB 50MG | 未載明 | 未載明 |
| HK-35318 | UNI-HYDRIN SYRUP 15MG/5ML | 未載明 | 未載明 |
| HK-40589 | APO-DIMENHYDRINATE TAB 50MG | 未載明 | 未載明 |
| HK-63898 | DIMENHYDRINATE TABLETS 50MG | 未載明 | 未載明 |

（共 20 張許可證，此處列出 5 張。）

## 安全性考量

安全性資訊請參考原廠仿單。

補充：作為第一代 H1 抗組織胺，一般需留意鎮靜與抗膽鹼負擔。

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個預測適應症都沒有臨床試驗；過敏性蕁麻疹僅有一篇犬隻藥動學研究，並未測試蕁麻疹療效。證據只到機轉推論與模型預測層級。
- 香港許可證的適應症與安全性資料皆缺，無法進入安全性篩選。

**若要推進需要：**
- 補齊香港衛生署仿單的警語、禁忌與核准適應症
- 補充 DrugBank 的作用機轉資料
- 搜尋 diphenhydramine 或第一代抗組織胺用於蕁麻疹的人體臨床證據
- 釐清 dimenhydrinate 相較於 diphenhydramine 及第二代抗組織胺的定位與優勢

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

