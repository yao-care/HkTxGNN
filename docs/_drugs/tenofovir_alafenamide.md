---
layout: default
title: Tenofovir Alafenamide
parent: 僅模型預測 (L5)
nav_order: 729
evidence_level: L5
indication_count: 3
---

# Tenofovir Alafenamide
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

# Tenofovir Alafenamide：原適應症資料缺口 → TxGNN 預測「猴免疫缺陷病毒感染」（動物模型，非人類適應症）

## 一句話總結

Tenofovir Alafenamide (TAF) 的原始核准適應症與作用機轉資料目前為**資料缺口**，僅能從候選機轉推論得知其為核苷酸反轉錄酶抑制劑類抗病毒藥物。
TxGNN 模型將其最高分預測連結到 **Simian Immunodeficiency Virus (SIV) infection（猴免疫缺陷病毒感染）**，預測分數 **99.89%**，但支持證據全數來自**動物模型研究**，且該疾病本身不感染人類，**無法轉譯為人類臨床適應症**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（DrugBank/TFDA 均未提供核准適應症文字） |
| 預測新適應症 | Simian immunodeficiency virus infection（猴免疫缺陷病毒感染，靈長類動物疾病） |
| TxGNN 預測分數 | 99.89%（rank 3015） |
| 證據等級 | L4（僅有前臨床/動物模型研究，無人類臨床試驗證據） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Tenofovir Alafenamide 的官方作用機轉（MOA）資料。根據候選適應症提供的機轉推論，TAF 是 tenofovir 的前驅藥，經細胞內磷酸化轉換為 tenofovir diphosphate 後抑制反轉錄酶活性，屬於核苷酸反轉錄酶抑制劑（NRTI）類別的抗病毒藥物。

SIV 與 HIV 同屬慢病毒屬（lentivirus），兩者反轉錄酶結構高度同源，因此 TAF 對 SIV 具有生化機轉上的合理性——這也是所有支持文獻皆聚焦於猴模型 PrEP/PEP（暴露前後預防）研究的原因。

**但關鍵限制是：SIV 是靈長類動物專屬的病毒，不感染人類。** 這個「適應症」實質上是「TAF 用於猴模型以驗證其對人類 HIV 預防潛力」的動物實驗設計，而非可直接對應到人類病患的老藥新用標的。此外，Evidence Pack 中排名第 2（feline acquired immunodeficiency syndrome，貓愛滋病）與第 3（罕見神經發育疾病）的候選，證據等級僅 L5，且機轉推論分別被標註為「純跨物種類比、無直接驗證」與「極可能是知識圖譜偽關聯」，同樣不具備推進價值。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03577782](https://clinicaltrials.gov/study/NCT03577782) | Phase 1/2 | 未知 | 12 | Vedolizumab 併用抗反轉錄病毒藥物治療 HIV 感染者，主體藥物與適應症皆非 TAF-SIV 直接相關，關聯性評級為 C（資料庫關鍵字誤配對） |

⚠️ 此為唯一比對到的試驗，且相關性評級偏低，**不構成 TAF 對 SIV 有效的臨床證據**。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38134382](https://pubmed.ncbi.nlm.nih.gov/38134382/) | 2024 | 動物模型（猴） | J Infect Dis | TAF/EVG 陰道植入劑於暴露前後 4 小時給藥仍具 93–100% 抗 SHIV 保護力 |
| [31362305](https://pubmed.ncbi.nlm.nih.gov/31362305/) | 2019 | 動物模型（猴） | J Infect Dis | 口服 TAF/FTC 複方或 TAF 單方預防猴模型陰道 SHIV 感染 |
| [27465645](https://pubmed.ncbi.nlm.nih.gov/27465645/) | 2016 | 動物模型（猴） | J Infect Dis | 口服 FTC+TAF 預防猴模型直腸 SHIV 感染（PrEP 潛力） |
| [39632836](https://pubmed.ncbi.nlm.nih.gov/39632836/) | 2024 | 動物模型（猴） | Nat Commun | 早期治療介入合併超長效抗病毒藥物達成猴模型 SHIV 緩解 |
| [35913838](https://pubmed.ncbi.nlm.nih.gov/35913838/) | 2022 | 動物模型（猴） | J Antimicrob Chemother | 可生物降解 TAF 緩釋植入物之陰道保護安全性與療效 |
| [16810108](https://pubmed.ncbi.nlm.nih.gov/16810108/) | 2006 | 動物模型（幼猴） | J Acquir Immune Defic Syndr | 口服 TDF 與局部 GS-7340（TAF 前身）保護幼猴對抗重複口服 SIV 攻毒 |
| [39559349](https://pubmed.ncbi.nlm.nih.gov/39559349/) | 2024 | 動物模型（人源化小鼠） | Front Immunol | 雙用途人源化小鼠模型可同時測試 SIV 與 HIV 抗病毒策略 |
| [31730629](https://pubmed.ncbi.nlm.nih.gov/31730629/) | 2019 | 動物模型方法學 | PLoS One | 訓練恆河猴每日口服 ARV 之方法學，供 HIV 預防/治療臨床前評估 |
| [22740713](https://pubmed.ncbi.nlm.nih.gov/22740713/) | 2012 | 動物模型（SHIV） | J Infect Dis | 口服 PrEP 期間急性 SHIV 感染可降低發炎反應與 CD4 細胞流失 |

**注意：以上 9 篇文獻全數為動物模型研究（Tier 3），無人類臨床證據，且均聚焦於 HIV 預防（PrEP/PEP）情境下的 SHIV/SIV 動物模型，而非「治療人類 SIV 感染」。**

---

## 香港上市資訊

目前 Tenofovir Alafenamide (DB09299) **尚未於香港取得任何藥品許可證**（0 張）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 頂端候選適應症（SIV 感染）為靈長類動物專屬疾病，不感染人類，證據等級雖標示 L4，但全部證據來自動物模型研究，**無法轉譯為人類臨床適應症**。
- 排名第 2、3 的候選（貓愛滋病、罕見神經發育疾病）證據等級僅 L5，機轉推論本身已被標註為跨物種類比或知識圖譜偽關聯，不具推進價值。
- 原始適應症、作用機轉（MOA）、香港上市狀態、安全性警語/禁忌症等關鍵資料均為缺口（DG001 為 Blocking 等級），目前**無法進行 S1 安全性初評**。

**若要推進需要：**
- 補齊 TAF 原廠仿單/TFDA 核准適應症與 MOA 資料（解除 DG001、DG002）
- 若欲評估 HIV 相關人類適應症，應改以人類 HIV 臨床試驗與文獻重新檢索，而非現有的 SIV/SHIV 動物模型資料
- 排除本次候選清單中 SIV、FIV 等動物專屬疾病及機轉不合理的候選，重新執行 TxGNN 篩選或人工複核
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

