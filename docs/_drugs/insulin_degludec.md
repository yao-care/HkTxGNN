---
layout: default
title: Insulin Degludec
parent: 高證據等級 (L1-L2)
nav_order: 462
evidence_level: L1
indication_count: 5
---

# Insulin Degludec
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Insulin Degludec：從基礎胰島素治療到第 1 型糖尿病

## 一句話總結

Insulin Degludec 是超長效基礎胰島素類似物，在香港已有上市產品。
TxGNN 模型預測它可能對**第 1 型糖尿病 (Type 1 Diabetes Mellitus)** 有效，目前有 **50 個臨床試驗**和 **20 篇文獻**支持這個方向。
第 1 型糖尿病其實是它既有的標示用途，因此這份預測較接近「既有適應症的再確認」，不是真正的老藥新用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未收錄適應症文字 |
| 預測新適應症 | 第 1 型糖尿病 (Type 1 Diabetes Mellitus) |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。就藥理特性而言，Insulin Degludec 是超長效基礎胰島素類似物，會與胰島素受體結合，補足第 1 型糖尿病患者缺乏的內源性胰島素。

第 1 型糖尿病的核心問題是胰島素絕對缺乏，因此基礎胰島素的作用是直接替代，不需要間接推論。文獻也指出，它在皮下注射後會由多聚體逐漸轉為單體，被緩慢而持續地吸收，作用時間超過 42 小時。

這個機轉與預測完全吻合，但適應症已是既有用途，所以要先確認香港仿單與核准範圍，再決定是否歸類為老藥新用候選。

## 臨床試驗證據

共 50 個試驗，以下列出與第 1 型糖尿病最相關的 10 個：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | 完成 | 350 | BEGIN Young 1：比較 Degludec 與 Detemir 用於 1 至未滿 18 歲兒童及青少年第 1 型糖尿病的療效與安全性 |
| [NCT00982228](https://clinicaltrials.gov/study/NCT00982228) | Phase 3 | 完成 | 629 | 第 1 型糖尿病基礎-餐時方案中，比較 Degludec 與 Glargine（各搭配 Aspart），為期 52 週並含延伸期 |
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Phase 3 | 完成 | 834 | 兒童及青少年第 1 型糖尿病，比較速效 Aspart 與 NovoRapid，皆搭配 Degludec 作為基礎胰島素 |
| [NCT00612040](https://clinicaltrials.gov/study/NCT00612040) | Phase 2 | 完成 | 178 | 比較兩種 Degludec 配方與 Glargine（皆搭配 Aspart），16 週 |
| [NCT03740919](https://clinicaltrials.gov/study/NCT03740919) | Phase 3 | 完成 | 751 | 兒童及青少年第 1 型糖尿病，比較 LY900014 與 Humalog（Degludec 的角色未明確說明） |
| [NCT06238778](https://clinicaltrials.gov/study/NCT06238778) | Phase 2 | 進行中（已停止招募） | 227 | 在使用 Degludec 的成人第 1 型糖尿病患者中，比較肝臟導向胰島素 (HDV-Insulin Lispro) 與單用 Lispro |
| [NCT03938740](https://clinicaltrials.gov/study/NCT03938740) | Phase 2 | 完成 | 61 | 探索性比較肝臟導向胰島素 Lispro 與 Degludec 的劑量演算法 |
| [NCT02536859](https://clinicaltrials.gov/study/NCT02536859) | Phase 1 | 完成 | 60 | 穩態下比較 Degludec 與 Glargine 300 U/mL 的藥效與藥動 |
| [NCT01704417](https://clinicaltrials.gov/study/NCT01704417) | Phase 1 | 完成 | 40 | 比較 Degludec 與 Glargine 在運動時對血糖的影響 |
| [NCT05069545](https://clinicaltrials.gov/study/NCT05069545) | N/A（觀察性） | 完成 | 411 | 真實世界中 NovoPen 6 搭配 Tresiba 與 Fiasp 的血糖控制 |

## 文獻證據

共 20 篇，以下列出優先的 10 篇（RCT 優先，其次為統合分析與回顧）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT：比較 Degludec 與 Detemir（皆搭配 Aspart）用於第 1 型糖尿病孕婦的非劣性試驗 |
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6：以每日一次 Degludec 為對照，評估每週一次 Icodec 在第 1 型糖尿病成人的療效與安全性 |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | Lancet | QWINT-5：以每日一次 Degludec 為對照，評估每週一次 Efsitora 在第 1 型糖尿病成人的非劣性 |
| [34643020](https://pubmed.ncbi.nlm.nih.gov/34643020/) | 2022 | RCT（交叉） | Diabetes Obes Metab | HypoDeg：比較 Degludec 與 Glargine U100 對易發生夜間嚴重低血糖之第 1 型糖尿病患者的影響 |
| [36516429](https://pubmed.ncbi.nlm.nih.gov/36516429/) | 2023 | RCT（交叉） | Diabetes Technol Ther | ULTRAFLEXI-1：比較 Glargine 300 U/mL 與 Degludec 100 U/mL 在自發性運動前後的低血糖時間 |
| [34763071](https://pubmed.ncbi.nlm.nih.gov/34763071/) | 2022 | RCT（交叉） | Endocr Pract | BIGLEAP：以連續血糖監測比較 Degludec 與 Aspart 經幫浦輸注在控制良好患者中的療效 |
| [36800034](https://pubmed.ncbi.nlm.nih.gov/36800034/) | 2023 | RCT | Eur J Pediatr | 比較 Degludec、Glargine 與 NPH 對學齡前幼童第 1 型糖尿病血糖變異度與目標範圍時間的影響 |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | 統合分析 | Clin Ther | 系統性回顧，比較 Degludec 與 Glargine、Detemir 的療效與耐受性 |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | 回顧（RCT 與觀察性資料） | Diabetes Metab | 對照試驗顯示 HbA1c 降幅與對照藥相當，空腹血糖控制較佳，夜間低血糖明顯減少 |
| [29477399](https://pubmed.ncbi.nlm.nih.gov/29477399/) | 2018 | 系統性回顧與網絡統合分析 | Value Health | 比較成人第 1 型糖尿病各種基礎胰島素方案的相對療效與安全性 |

## 香港上市資訊

共 8 張許可證，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-62700 | TRESIBA FLEXTOUCH 預填充筆注射液 100U/ML | NOVO NORDISK HONG KONG LIMITED |
| HK-67541 | TRESIBA FLEXTOUCH 預填充筆注射液 100U/ML | NOVO NORDISK HONG KONG LIMITED |
| HK-62699 | TRESIBA FLEXTOUCH 預填充筆注射液 200U/ML | NOVO NORDISK HONG KONG LIMITED |
| HK-68120 | XULTOPHY 預填充筆注射液 100 UNITS/ML + 3.6MG/ML（Degludec 與 Liraglutide 複方） | NOVO NORDISK HONG KONG LIMITED |
| HK-67704 | RYZODEG FLEXTOUCH 預填充筆注射液 100U/ML 70/30（Degludec 與 Aspart 複方） | NOVO NORDISK HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 第 1 型糖尿病有多個已完成的 Phase 3 隨機對照試驗（如 NCT01513473、NCT00982228、NCT02670915），並有多篇 RCT 與統合分析，證據等級為 L1。
- 這是既有適應症的再確認，不是新用途，而且香港仿單的警語與禁忌資料目前缺漏，因此需要加上防護條件。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症（此為阻斷性資料缺口），並確認各許可證核准的適應症文字。
- 補充 DrugBank 的作用機轉資料。
- 確認是否應歸類為老藥新用候選，或直接視為既有適應症。
- 其餘 4 個預測適應症（自體免疫性卵巢炎、Opsismodysplasia、硫胺素反應性功能障礙症候群、局部僵硬肢體症候群）沒有任何試驗或文獻，證據等級為 L5，建議 Hold。

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

