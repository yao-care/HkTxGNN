---
layout: default
title: Emicizumab
parent: 僅模型預測 (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab：從先天性 A 型血友病到偽性類血友病性 von Willebrand 病 (Pseudo-von Willebrand disease)

## 一句話總結

Emicizumab 是模擬活化第 VIII 因子 (FVIIIa) 功能的雙特異性抗體，原本用於先天性 A 型血友病的預防治療。
TxGNN 模型預測它可能對 **偽性 von Willebrand 病 (pseudo-von Willebrand disease)** 有效，但**目前無任何臨床試驗或文獻**支持，機轉上也缺乏合理性，屬於高分但證據薄弱的預測。
本報告同時整理其他 9 個預測適應症，其中**後天性血友病 A** 的證據最強（見「其他預測適應症」章節）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 先天性 A 型血友病（依文獻描述；香港許可證未提供適應症文字） |
| 預測新適應症 | 偽性 von Willebrand 病 (pseudo-von Willebrand disease) |
| TxGNN 預測分數 | 99.99%（全體排名第 514） |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Emicizumab 是一種雙特異性抗體，能同時結合 FIXa 與 FX，取代 FVIII 的輔因子功能，促進凝血酶生成。

偽性 von Willebrand 病是血小板型疾病，成因是 GPIb 功能增強型突變，使血小板與 VWF 的親和力異常升高。Emicizumab 補的是凝血因子 (FVIII) 的功能，並不處理血小板缺陷。

因此這個高分主要來自知識圖譜中「出血性疾病」的鄰近關係，缺乏生物學上的直接支持。目前沒有臨床試驗或文獻。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-65932 | HEMLIBRA 注射液 60MG/0.4ML | ROCHE HONG KONG LIMITED |
| HK-65934 | HEMLIBRA 注射液 30MG/1ML | ROCHE HONG KONG LIMITED |
| HK-65935 | HEMLIBRA 注射液 150MG/1ML | ROCHE HONG KONG LIMITED |
| HK-65933 | HEMLIBRA 注射液 105MG/0.7ML | ROCHE HONG KONG LIMITED |

## 其他預測適應症

Evidence Pack 共含 10 個預測適應症，以下依證據強度整理。

| 排名 | 預測適應症 | 分數 | 證據等級 | 決策 | 說明 |
|-----|-----------|------|---------|------|------|
| 5 | 後天性凝血因子缺乏症（證據集中於**後天性血友病 A**） | 99.90% | L2 | Proceed with Guardrails | 機轉直接、有前瞻性研究，詳見下方 |
| 3 | Glanzmann 血小板無力症 | 99.98% | L4 | Hold | 缺陷在血小板聚集，Emicizumab 無法修復。相關文獻談的是 rFVIIa，並非 Emicizumab |
| 1 | 偽性 von Willebrand 病 | 99.99% | L5 | Hold | 見上文 |
| 2、4、6、7、9 | 原發性血小板釋放障礙、Scott 症候群、膠原蛋白受體缺陷、先天性血小板減少出血症、胎兒新生兒同種免疫性血小板減少症 | 99.5–99.99% | L5 | Hold | 缺陷在血小板，機轉上無支持，也無臨床證據 |
| 8 | 血栓性血小板減少性紫斑症 (TTP) | 99.61% | L5 | Hold | 促凝藥物在血栓性微血管病變中機轉不利，可能惡化病情。**視為偽陽性，不建議推進** |
| 10 | flood factor deficiency | 99.40% | L5 | Hold | 疾病名稱含糊，可能是資料映射錯誤，需先確認疾病本體條目 |

### 後天性血友病 A 的機轉

後天性血友病 A 是自體抗體中和 FVIII 所致。Emicizumab 結構上與 FVIII 無關，不會被抗 FVIII 抑制物中和，因此能直接恢復止血功能。

證據限於後天性血友病 A，不能推廣到所有後天性凝血因子缺乏。評為 L2 而非 L1，是因為前瞻性研究均為單臂、非隨機試驗，沒有 RCT。

### 相關臨床試驗

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) | N/A | 招募中 | 3000 | ATHN Transcends：非腫瘤性血液疾病治療安全性與效果的自然史觀察性世代研究。非介入性、非疾病特異，是否納入後天性血友病 A 病人尚無法確認 |

此試驗亦出現在 Glanzmann 血小板無力症的證據中，但同樣無法確認有納入該疾病的 Emicizumab 使用者。

### 相關文獻（列出 10 篇，另有其餘未列）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Phase 3 單臂試驗 (AGEHA) | J Thromb Haemost | 首個 Emicizumab 用於後天性血友病 A 的前瞻性、多中心、開放標籤 Phase 3 研究 |
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Phase 2 單臂試驗 (GTH-AHA-EMI) | Lancet Haematol | 檢驗 Emicizumab 能否在前 12 週預防出血並延後免疫抑制治療 |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Phase 3 最終分析 (AGEHA) | Thromb Haemost | 納入不適合免疫抑制治療的病人 (Cohort 2) 與長期預防資料 |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | 多中心真實世界世代研究 | Blood Adv | 美國 12 個血友病中心、62 位病人的仿單外使用，中位治療 10 週 |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | 世代研究 | Blood Adv | GTH-AHA-EMI 病人的 2 年追蹤，探討 Emicizumab 與延後免疫抑制的存活效益 |
| [38936699](https://pubmed.ncbi.nlm.nih.gov/38936699/) | 2024 | 比較性分析（類型待確認） | J Thromb Haemost | 比較 Emicizumab 與免疫抑制治療，評估能否減少早期積極免疫抑制的需求 |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | 共識建議 | Hamostaseologie | GTH-AHA 工作小組的 Emicizumab 使用建議 |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Review | J Thromb Haemost | 後天性血友病 A 在 Emicizumab 時代的敘述性回顧與處置方式 |
| [36795341](https://pubmed.ncbi.nlm.nih.gov/36795341/) | 2023 | Review | Blood Transfus | 探討 Emicizumab 用於後天性血友病 A 的優缺點 |
| [37276345](https://pubmed.ncbi.nlm.nih.gov/37276345/) | 2023 | 病例系列 | Haemophilia | Emicizumab 用於後天性血友病 A 的病例系列 |

## 安全性考量

- **血栓性微血管病變**：Emicizumab 與 aPCC（活化凝血酶原複合物）併用時有仿單警語，血栓風險需特別留意。這也是 TTP 預測不建議推進的原因之一。

其餘警語、禁忌症與藥物交互作用資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**（針對排名第 1 的偽性 von Willebrand 病）

**理由：**
- 只有模型分數，沒有任何臨床試驗或文獻。機轉上 FVIII 模擬功能也無法修復血小板 GPIb 缺陷，屬於 L5 證據。
- 本候選整體中，僅**後天性血友病 A** 值得優先評估（L2，Proceed with Guardrails）。

**若要推進需要：**
- 確認採用哪個預測適應症作為主要評估對象，建議改以後天性血友病 A 為主軸。
- 取得香港衞生署的仿單，補足警語、禁忌症與核准適應症。
- 取得 Emicizumab 的完整作用機轉資料 (DrugBank)。
- 後天性血友病 A 的推進條件：
  - 釐清仿單外使用的法規狀態。
  - 訂定併用 aPCC 等旁路製劑的血栓風險管控。
  - 制定是否併用免疫抑制治療的決策準則。
  - 補齊其餘未列出的文獻。
- 偽性 von Willebrand 病與其他血小板疾病：除非有新的機轉或臨床證據，否則不建議投入。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

