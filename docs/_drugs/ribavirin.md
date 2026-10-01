---
layout: default
title: Ribavirin
parent: 僅模型預測 (L5)
nav_order: 753
evidence_level: L5
indication_count: 5
---

# Ribavirin
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

# Ribavirin：從抗病毒治療到慢性 B 型肝炎

## 一句話總結

Ribavirin 是一種核苷類似物抗病毒藥，香港有 1 張上市許可證，但許可證未載明適應症。
TxGNN 模型預測它可能對**慢性 B 型肝炎 (Chronic hepatitis B virus infection)** 有效。
目前檢索到 **50 個臨床試驗**和 **20 篇文獻**，但試驗幾乎都是 C 型肝炎研究，沒有直接證明 ribavirin 能治療 B 型肝炎。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明 |
| 預測新適應症 | 慢性 B 型肝炎 (Chronic hepatitis B virus infection) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L4（僅有間接證據，無直接 HBV 療效研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。Ribavirin 是 guanosine 類似物，主要對 HCV 等 RNA 病毒有活性。

B 型肝炎病毒是帶有反轉錄步驟的 DNA 病毒，ribavirin 對它沒有已確立的直接抗病毒作用。TxGNN 的高分最可能來自知識圖譜中「肝炎／干擾素合併療法」的鄰近關係，而不是機轉上的直接證據。

在 HBV/HCV 共同感染的病人中，ribavirin（合併 peginterferon）只作用於 HCV 部分。因此這個預測在機轉上缺乏支持，應視為待驗證的假說。

## 臨床試驗證據

共檢索到 50 個試驗。以下列出 10 個較相關者，**幾乎全是 HCV 試驗**。
- NCT02555943 是唯一涉及 HBV 的試驗。它研究的是 HCV/HBV 共同感染者在接受抗 HCV 藥物時的 HBV 再活化，並未測試 ribavirin 對 HBV 的療效。
- 其餘試驗的母群體皆為 HCV，不能作為 ribavirin 治療 HBV 的證據。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02555943](https://clinicaltrials.gov/study/NCT02555943) | Phase 2/3 | 完成 | 23 | 直接抗病毒藥治療 HCV/HBV 共同感染時，HBV 再活化的發生率與風險因子 |
| [NCT00215865](https://clinicaltrials.gov/study/NCT00215865) | Phase 3 | 完成 | 600 | PEG-IFN α-2b + ribavirin 用於先前治療失敗的慢性 C 肝，比較固定劑量與體重調整劑量 |
| [NCT00265395](https://clinicaltrials.gov/study/NCT00265395) | Phase 3 | 完成 | 1428 | 第 1 型 C 肝、病毒反應緩慢者，比較 72 週與 48 週 PEG-IFN + ribavirin |
| [NCT01598090](https://clinicaltrials.gov/study/NCT01598090) | Phase 3 | 完成 | 881 | Peginterferon lambda-1a 與 alfa-2a 分別合併 ribavirin 和 telaprevir，用於第 1 型 C 肝 |
| [NCT00940420](https://clinicaltrials.gov/study/NCT00940420) | Phase 4 | 完成 | 2695 | Pegasys + ribavirin 治療慢性 C 肝的安全性與耐受性 |
| [NCT00378599](https://clinicaltrials.gov/study/NCT00378599) | Phase 3 | 完成 | 125 | 肝移植後 C 肝復發者使用 PEG-IFN α-2b + ribavirin 的療效與安全性 |
| [NCT00215891](https://clinicaltrials.gov/study/NCT00215891) | Phase 3 | 完成 | 300 | HIV 合併 C 肝者使用 PEG-IFN α-2b + ribavirin，比較 48 週與 72 週 |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Phase 3 | 完成 | 102 | Sofosbuvir/velpatasvir ± ribavirin 用於 C 肝失代償性肝硬化 |
| [NCT01655966](https://clinicaltrials.gov/study/NCT01655966) | Phase 3 | 未知 | 80 | 在 PEG-IFN + ribavirin 之外加用維生素 D，用於第 4 型慢性 C 肝 |
| [NCT01854697](https://clinicaltrials.gov/study/NCT01854697) | Phase 3 | 完成 | 311 | ABT-450/r/ABT-267 + ABT-333 ± ribavirin，對比 telaprevir 組合，用於第 1 型 C 肝 |

## 文獻證據

共檢索到 20 篇，且均未被評定為直接支持。以下列出 10 篇較相關者，主要是 HBV/HCV 共同感染或兩種肝炎治療的綜述。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV 共同感染者肝病進展風險高。過去建議 PEG-IFN + ribavirin 用於 HCV RNA 陽性者 |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | HCV/HBV 雙重感染的治療與預後更新 |
| [19669238](https://pubmed.ncbi.nlm.nih.gov/19669238/) | 2009 | Review | Hepatol Int | 雙重感染中兩種病毒交互作用與長期預後仍待研究 |
| [18804888](https://pubmed.ncbi.nlm.nih.gov/18804888/) | 2008 | Review | J Hepatol | HBV 與 HCV 共同感染的治療仍是挑戰（無摘要） |
| [27433078](https://pubmed.ncbi.nlm.nih.gov/27433078/) | 2016 | Review | World J Gastroenterol | 回顧 HBV 與 HCV 的化學與免疫治療。IFN-α ± ribavirin 為早期治療基礎，後來由直接抗病毒藥取代 |
| [10832679](https://pubmed.ncbi.nlm.nih.gov/10832679/) | 2000 | 未分類 | J Gastroenterol | 標題探討 ribavirin 對慢性 B 肝是否真的有效（無摘要，僅依標題判斷） |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | 未分類 | Annu Rev Med | 慢性 B 肝與 C 肝的現行治療策略 |
| [10689413](https://pubmed.ncbi.nlm.nih.gov/10689413/) | 2000 | 未分類 | Postgrad Med | 慢性 B 肝與 C 肝的抗病毒治療，說明哪些病人適合哪些藥物 |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | 未分類 | Hepatology | 慢性 HBV 與 HCV 抗病毒治療的免疫學面向 |
| [26284971](https://pubmed.ncbi.nlm.nih.gov/26284971/) | 2015 | Review | Curr Opin Virol | IL28B 基因型與 PEG-IFN + ribavirin 對 HCV 療效的關聯，並討論其與 HBV 的關係 |

## 香港上市資訊

| 許可證號 | 品名 | 持證商 |
|---------|------|--------|
| HK-37449 | ROBAVIN CAP 100MG | JULIUS CHEN & COMPANY (HK) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有臨床試驗都是 HCV 研究，沒有一項測試 ribavirin 對 HBV 的療效，機轉上也沒有直接作用依據。
- TxGNN 的 99.86% 分數只代表知識圖譜上的關聯，且關鍵的許可證適應症與安全性資料缺失。

**若要推進需要：**
- 取得香港衛生署的仿單，確認核准適應症、警語與禁忌症
- 補齊 DrugBank 的作用機轉資料，重新評估機轉連結
- 檢索 ribavirin 對 HBV 的體外或臨床直接證據，並釐清 PMID 10832679 的結論
- 若要研究，須先排除 HCV/HBV 共同感染的混淆，確認療效是否來自 ribavirin 對 HBV 的作用
- 同一份預測清單中的另外 4 項預測（門靜脈血栓、肝肺症候群等）均無臨床試驗或有效文獻，列為 L5，不建議投入資源

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

