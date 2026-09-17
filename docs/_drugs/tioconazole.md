---
layout: default
title: Tioconazole
parent: 僅模型預測 (L5)
nav_order: 749
evidence_level: L5
indication_count: 3
---

# Tioconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Tioconazole：從抗黴菌（原適應症資料缺口）到外陰陰道炎 (Vulvovaginitis)

## 一句話總結

Tioconazole 是咪唑類（imidazole）廣效抗黴菌藥物，文獻顯示其原始定位為淺表黴菌感染（皮膚黴菌病、陰道念珠菌病）的局部治療，但本次 Evidence Pack 中「原適應症」與「作用機轉」欄位皆為資料缺口，需另行查證原廠仿單確認。TxGNN 模型預測它可能對**外陰陰道炎 (Vulvovaginitis)** 有效，目前有 **2 個臨床試驗**和 **20 篇文獻**支持這個方向，其中多篇為 tioconazole 直接針對陰道念珠菌感染的隨機對照試驗，但登記在案的臨床試驗均非 tioconazole 本身的試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（原廠核准適應症未提供，僅由文獻推測為淺表黴菌感染／陰道念珠菌病） |
| 預測新適應症 | 外陰陰道炎 (Vulvovaginitis) |
| TxGNN 預測分數 | 99.23% |
| 證據等級 | L2（文獻中有 tioconazole 本身的完成 RCT，但登記臨床試驗非本藥試驗） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為資料缺口，DG002）。根據文獻紀錄（PMID 3510114），tioconazole 是一種取代型咪唑類抗微生物藥物，體外對皮癬菌、酵母菌，以及部分披衣菌、滴蟲和格蘭氏陽性菌具有廣效活性，過去局部劑型已被證實可有效治療皮膚與陰道的淺表黴菌感染。

外陰陰道炎 (vulvovaginitis) 是一個涵蓋多種病因的統稱，其中念珠菌性外陰陰道炎 (candidal vulvovaginitis) 是最常見的亞型之一。由於 tioconazole 的抗黴菌光譜本就涵蓋 Candida 屬酵母菌，將其應用範圍由「陰道念珠菌病」延伸至更廣義的「外陰陰道炎」，在機轉上具有合理性——但需注意，這較接近既有適應症的延伸確認，而非全新機轉的老藥新用。

由於「原適應症」欄位本身是資料缺口，此機轉關聯性分析僅能依據文獻內容反推，建議優先補齊原廠仿單資料以確認官方核准適應症範圍。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06056947](https://clinicaltrials.gov/study/NCT06056947) | Phase 3 | 完成 | 577 | Fenticonazole+Tinidazole+Lidocaine 新劑型 vs Gynomax® XL，用於治療細菌性陰道炎、念珠菌性外陰陰道炎、滴蟲性陰道炎及混合感染（非 tioconazole 直接試驗，僅同適應症領域佐證） |
| [NCT03839875](https://clinicaltrials.gov/study/NCT03839875) | Phase 4 | 完成 | 116 | Gynomax® XL 單臂開放性研究，治療滴蟲性陰道炎、細菌性陰道炎、念珠菌性外陰陰道炎及混合感染（非 tioconazole 直接試驗） |

> 註：以上兩試驗評估的是其他抗黴菌複方藥物，並非 tioconazole 本身，僅作為同適應症領域的間接佐證。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3524439](https://pubmed.ncbi.nlm.nih.gov/3524439/) | 1986 | RCT | Antimicrob Agents Chemother | 單劑 tioconazole 6.5% 藥膏 vs 3 天 clotrimazole，兩組治癒率相近（84% vs 85%） |
| [6347833](https://pubmed.ncbi.nlm.nih.gov/6347833/) | 1983 | RCT | Gynakologische Rundschau | 雙盲比較 tioconazole 與安慰劑用於陰道念珠菌病，並評估全身吸收情形 |
| [3510114](https://pubmed.ncbi.nlm.nih.gov/3510114/) | 1986 | Review | Drugs | Tioconazole 抗微生物活性與淺表黴菌病治療用途的完整回顧 |
| [6873744](https://pubmed.ncbi.nlm.nih.gov/6873744/) | 1983 | Cohort | Gynakologische Rundschau | Tioconazole 藥膏 vs econazole 陰道栓劑，3 天療程療效與安全性開放性比較 |
| [6347834](https://pubmed.ncbi.nlm.nih.gov/6347834/) | 1983 | Cohort | Gynakologische Rundschau | Tioconazole 與 econazole 3 天療程開放性比較，療效與耐受性相近 |
| [4025721](https://pubmed.ncbi.nlm.nih.gov/4025721/) | 1985 | Cohort | Alabama J Med Sciences | Tioconazole 用於外陰陰道念珠菌病之臨床與細胞學評估 |
| [3485546](https://pubmed.ncbi.nlm.nih.gov/3485546/) | 1986 | Cohort | J Int Med Res | Tioconazole 2% 陰道乳膏用於滴蟲性陰道炎及混合感染，治癒率達 95% |
| [3984688](https://pubmed.ncbi.nlm.nih.gov/3984688/) | 1985 | Cohort | Acta Obstet Gynecol Scand | Tioconazole 2% 陰道乳膏治療陰道念珠菌病，黴菌學治癒率 88.5% |
| [6094282](https://pubmed.ncbi.nlm.nih.gov/6094282/) | 1984 | RCT | J Int Med Res | 局部 tioconazole 單劑 vs 全身性 ketoconazole 5 天療程比較，局部組症狀緩解較快 |
| [10470518](https://pubmed.ncbi.nlm.nih.gov/10470518/) | 1999 | Review | Comprehensive Therapy | 健康女性外陰陰道症狀之流行病學、診斷與治療回顧 |

## 香港上市資訊

Tioconazole 目前**未在香港上市**，無任何許可證登記資料（`total_licenses = 0`）。若要推進此適應症擴充，需先確認是否有廠商規劃於香港申請藥品許可證。

## 安全性考量

安全性資訊請參考原廠仿單。目前 Evidence Pack 中的仿單警語、禁忌症與藥物交互作用資料均為資料缺口（DG001，嚴重度 Blocking），此缺口已直接阻擋進入 S1 安全性初評階段，需優先自 TFDA/原廠官網取得仿單 PDF 並解析。

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然文獻中已有多篇 tioconazole 用於陰道念珠菌病（外陰陰道炎的常見亞型）的完成 RCT，機轉延伸具一定合理性；但安全性�522仿單資料為 Blocking 等級缺口，且藥物目前未在香港上市，無法進行完整風險評估。
- 登記於臨床試驗資料庫中的兩項試驗皆非 tioconazole 本身，證據強度需以歷史文獻的 RCT 為主，缺乏近期、註冊性的直接試驗支持。

**若要推進需要：**
- 補齊 TFDA／原廠仿單警語與禁忌症資料（DG001，Blocking）
- 補齊 tioconazole 詳細作用機轉資料（DG002，High）
- 確認官方核准之原適應症範圍，以利進行機轉關聯性分析
- 評估香港藥品許可證申請可行性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

