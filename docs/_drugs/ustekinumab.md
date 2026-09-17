---
layout: default
title: Ustekinumab
parent: 僅模型預測 (L5)
nav_order: 783
evidence_level: L5
indication_count: 5
---

# Ustekinumab
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

# Ustekinumab：從乾癬到皮膚炎 (Dermatitis)

## 一句話總結

> Ustekinumab（DrugBank ID: DB05679）依文獻證據為 IL-12/IL-23 p40 antagonist，已知核准用於乾癬、乾癬性關節炎、克隆氏症與潰瘍性大腸炎等自體免疫疾病（結構化許可證資料目前缺失，見下方說明）。
> TxGNN 模型預測它可能對**皮膚炎 (Dermatitis)** 有效，
> 目前有 **7 個臨床試驗**（含 2 個已完成的 Phase 2 RCT 直接針對異位性皮膚炎）和 **20+ 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 乾癬 (Psoriasis) 等（依文獻引用，結構化欄位資料缺失，見 DG001/DG002） |
| 預測新適應症 | 皮膚炎 (Dermatitis) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2（已完成 Phase 2 雙盲安慰劑對照 RCT） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Evidence Pack 中結構化的 `original_moa` 欄位標記為缺失（DG002），但收集到的文獻本身提供了機轉描述：PMID 27304428 指出「Ustekinumab is an IL-12/IL-23p40 antagonist that suppresses Th1, Th17 and Th22 activation」；PMID 36208443 進一步說明其為「human interleukin-12 and -23 antagonist」，已核准用於乾癬、乾癬性關節炎、克隆氏症、潰瘍性大腸炎。

異位性皮膚炎（atopic dermatitis）與乾癬同屬 Th1/Th17/Th22 軸活化相關的慢性炎症性皮膚疾病，兩者在免疫病理機轉上有重疊，這也是多篇文獻（如 PMID 29164954 系統性回顧）探討 IL-12/23 抑制劑跨適應症應用的理論基礎。

日本第二期臨床試驗（NCT01945086, PMID 28338223）已直接驗證 ustekinumab 在重度異位性皮膚炎患者中的療效與安全性，支持 TxGNN 預測方向具有實質機轉與臨床證據支撐，而非單純圖譜關聯推論。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01806662](https://clinicaltrials.gov/study/NCT01806662) | Phase 2 | 完成 | 32 | Ustekinumab 用於對前線治療反應不佳的慢性異位性皮膚炎，隨機化先導性研究 |
| [NCT01945086](https://clinicaltrials.gov/study/NCT01945086) | Phase 2 | 完成 | 79 | 日本重度異位性皮膚炎患者，雙盲安慰劑對照，評估兩劑量 ustekinumab 之療效與安全性 |
| [NCT02074982](https://clinicaltrials.gov/study/NCT02074982) | Phase 3 | 完成 | 676 | Secukinumab 與 ustekinumab 於中重度斑塊型乾癬之療效比較（CLEAR 研究） |
| [NCT05535738](https://clinicaltrials.gov/study/NCT05535738) | Phase 2/3 | 招募中 | 45 | 以接觸性皮膚炎模型結合生物製劑（含 ustekinumab 類別）研究皮膚發炎機轉 |
| [NCT01356758](https://clinicaltrials.gov/study/NCT01356758) | N/A | 完成 | 126 | 重度乾癬患者使用生物製劑之心血管風險評估 |
| [NCT07041112](https://clinicaltrials.gov/study/NCT07041112) | N/A | 完成 | 1000 | 皮膚乾癬患者生物製劑十年存活率之藥物基因學觀察性研究 |
| [NCT07352566](https://clinicaltrials.gov/study/NCT07352566) | Phase 4 | 未開始招募 | 10 | 皮內微裝置測試 FDA 核准藥物（含異位性皮膚炎與乾癬適應症）之皮膚遞送 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27304428](https://pubmed.ncbi.nlm.nih.gov/27304428/) | 2017 | RCT (Phase II) | Exp Dermatol | 33 名中重度異位性皮膚炎患者接受 ustekinumab，評估療效與安全性 |
| [28338223](https://pubmed.ncbi.nlm.nih.gov/28338223/) | 2017 | RCT (Phase II) | Br J Dermatol | 日本重度異位性皮膚炎雙盲安慰劑對照試驗，驗證 ustekinumab 療效與安全性 |
| [33074565](https://pubmed.ncbi.nlm.nih.gov/33074565/) | 2021 | 系統性回顧/Meta-analysis | Allergy | 為 EAACI 臨床指引彙整異位性皮膚炎全身性治療證據 |
| [29098604](https://pubmed.ncbi.nlm.nih.gov/29098604/) | 2018 | 系統性回顧/Meta-analysis | Am J Clin Dermatol | 評估生物製劑於異位性皮膚炎之療效，含 ustekinumab |
| [29164954](https://pubmed.ncbi.nlm.nih.gov/29164954/) | 2018 | 系統性回顧 | J Dermatolog Treat | 系統性回顧 ustekinumab 於異位性皮膚炎治療之證據 |
| [36208443](https://pubmed.ncbi.nlm.nih.gov/36208443/) | 2022 | Review | Dermatol Ther | 綜整 ustekinumab 適應症外使用（off-label）之文獻與臨床試驗 |
| [39201826](https://pubmed.ncbi.nlm.nih.gov/39201826/) | 2024 | Narrative Review | Children (Basel) | 兒童異位性皮膚炎、乾癬等疾病之生物製劑治療綜述 |
| [33849369](https://pubmed.ncbi.nlm.nih.gov/33849369/) | 2022 | 真實世界證據 | J Dermatolog Treat | 分析真實世界中 ustekinumab 用於異位性皮膚炎之療效 |
| [39987634](https://pubmed.ncbi.nlm.nih.gov/39987634/) | 2025 | 真實世界安全性分析 | Int Immunopharmacol | 基於 FDA FAERS 資料庫分析 ustekinumab 用於乾癬/乾癬性關節炎之安全性 |
| [31514420](https://pubmed.ncbi.nlm.nih.gov/31514420/) | 2019 | Review | Children (Basel) | 兒童乾癬與異位性皮膚炎之生物製劑治療選項綜述 |

---

## 安全性考量

> 安全性資訊請參考原廠仿單。目前 `key_warnings`、`contraindications`、`DDI` 皆為資料缺口（DG001，Blocking 等級），需優先補齊才能進行 S1 安全性初評。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 雖有 2 個已完成的 Phase 2 雙盲安慰劑對照 RCT（NCT01945086、NCT01806662）及多篇系統性回顧支持 ustekinumab 用於異位性皮膚炎的療效訊號（證據等級 L2），但香港目前**未上市、無任何許可證**，且安全性資料為 **Blocking** 等級缺口（DG001），無法進入下一階段安全性初評。

**若要推進需要：**
- 取得原廠仿單或香港藥品安全性資料（警語、禁忌、DDI）— 對應 DG001
- 補齊結構化作用機轉資料（DrugBank API 查詢）— 對應 DG002
- 確認香港藥品進口／上市法規路徑（現為 0 張許可證）
- 若鎖定異位性皮膚炎適應症，需規劃 Phase 3 RCT 以確立療效（現有僅為 Phase 2 證據）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

