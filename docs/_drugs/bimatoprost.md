---
layout: default
title: Bimatoprost
parent: 僅模型預測 (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
---

# Bimatoprost
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

# Bimatoprost：從青光眼到含牙齒/牙周成分的畸形症候群

## 一句話總結

Bimatoprost 是一種合成前列腺素 F2α 類似物（prostamide），原本核准用於治療**眼壓過高及開角型青光眼**，並另有 FDA 核准的睫毛生長適應症（Latisse™）。
TxGNN 模型預測它可能對**含牙齒/牙周成分的畸形症候群（malformation syndrome with odontal and/or periodontal component）** 有效，
目前有 **0 個臨床試驗**及 **20 篇文獻**支持，但需注意這 20 篇均為**牙周炎一般性研究，並非 Bimatoprost 直接應用的證據**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 眼壓過高／開角型青光眼（根據文獻推斷） |
| 預測新適應症 | 含牙齒/牙周成分的畸形症候群（malformation syndrome with odontal and/or periodontal component） |
| TxGNN 預測分數 | 99.997% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Bimatoprost 屬於前列腺素類似物（prostamide F2α analog），其核心藥理機制為結合 FP 前列腺素受體，調節前列腺素相關訊號路徑以降低眼壓。目前缺乏詳細的完整 MOA 資料，但根據現有文獻，前列腺素路徑調節是其主要藥理基礎。

前列腺素（尤其是 PGE2）在牙周組織的慢性炎症與骨質破壞過程中扮演關鍵介質角色，牙周炎病理進程中前列腺素濃度顯著升高，骨吸收與組織破壞均與此訊號路徑密切相關。TxGNN 模型可能基於此分子層面的路徑關聯，預測前列腺素受體調節劑（如 Bimatoprost）對含牙周成分的畸形症候群具有潛在效益。

然而，此連結目前仍屬純理論假設。現有系統蒐集到的 20 篇文獻均為牙周炎（periodontitis）一般性治療研究，論文標題與摘要均未涉及 Bimatoprost，無法作為支持此適應症的直接證據。從知識圖譜的網路距離而言，這是一個間接且尚未被研究驗證的預測。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

> ⚠️ **重要說明**：以下文獻為系統以「Bimatoprost + 牙周相關疾病」關鍵字搜尋所得，論文內容均為**牙周炎一般性研究**，並非 Bimatoprost 用於此適應症的直接應用研究，僅作為疾病背景參考。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [35688447](https://pubmed.ncbi.nlm.nih.gov/35688447/) | 2022 | Guideline | J Clin Periodontol | Stage IV 牙周炎治療的 EFP S3 臨床實務指引，涵蓋嚴重牙周喪失的處置建議 |
| [37435999](https://pubmed.ncbi.nlm.nih.gov/37435999/) | 2023 | Review | Periodontology 2000 | 再生牙周手術（針對骨內缺損和根分叉缺損）的併發症及治療失誤分析 |
| [35420698](https://pubmed.ncbi.nlm.nih.gov/35420698/) | 2022 | Systematic Review | Cochrane | 牙周治療對糖尿病患者血糖控制效果的 Cochrane 系統性回顧 |
| [39233377](https://pubmed.ncbi.nlm.nih.gov/39233377/) | 2024 | Review | Periodontology 2000 | 睡眠障礙（阻塞性睡眠呼吸中止）為牙周健康新興風險因子的文獻回顧 |
| [38907216](https://pubmed.ncbi.nlm.nih.gov/38907216/) | 2024 | Review | J Nanobiotechnology | 生物材料介導的巨噬細胞免疫療法應用於牙周炎治療的研究現況 |
| [38362600](https://pubmed.ncbi.nlm.nih.gov/38362600/) | 2024 | Clinical Study | J Dental Research | 牙周炎（Stage III/IV，n=47）患者治療前後口腔與腸道菌群的縱向變化 |
| [36883660](https://pubmed.ncbi.nlm.nih.gov/36883660/) | 2023 | Review | J Dental Research | 牙齦纖維母細胞在牙周炎中作為非典型先天免疫細胞的病理調節角色 |
| [22057194](https://pubmed.ncbi.nlm.nih.gov/22057194/) | 2012 | Review | Diabetologia | 牙周炎與糖尿病的雙向關係；糖尿病使牙周炎風險增加約三倍 |
| [29291254](https://pubmed.ncbi.nlm.nih.gov/29291254/) | 2018 | Systematic Review | Cochrane | 支持性牙周治療（SPT）維持已治療成年患者牙齒的長期效果 |
| [20599785](https://pubmed.ncbi.nlm.nih.gov/20599785/) | 2010 | Review | Biochem Pharmacol | 補體系統過度活化或失調在牙周炎免疫病理機制中的角色 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然 TxGNN 給出高達 99.997% 的預測分數，但前列腺素路徑與牙周組織的關聯屬分子網路推斷，現有 20 篇文獻均為一般牙周炎治療研究，與 Bimatoprost 無直接關聯，實際臨床可行性未知，尚不具備進入開發流程的最低證據門檻（L5）。
- ⚡ **關鍵提示**：在本次預測清單中，Bimatoprost 用於**脫髮（alopecia，Rank 8）** 已有 **11 個臨床試驗**（含多項已完成的 Phase 2 研究）及 **20 篇直接相關文獻**，機轉合理且前列腺素誘導睫毛/毛髮生長的副作用已獲 FDA 認可（Latisse™），若要探索老藥新用，強烈建議優先評估脫髮適應症。

**若要推進需要：**
- 補充 Bimatoprost 完整作用機轉資料（DrugBank MOA 查詢）
- 前列腺素 FP 受體在牙周組織中表達與功能的前臨床研究
- 香港衛生署批准的仿單安全性資料（主要警語、禁忌症）
- 動物模型驗證 Bimatoprost 對牙周骨質破壞的影響
- 若優先資源有限，建議轉向評估**脫髮（Rank 8）**——已有充分臨床證據支持，進入門檻顯著較低
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

