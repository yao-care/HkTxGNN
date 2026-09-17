---
layout: default
title: Insulin Degludec
parent: 僅模型預測 (L5)
nav_order: 399
evidence_level: L5
indication_count: 5
---

# Insulin Degludec
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

# Insulin Degludec：從資料缺口的「原適應症」到 TxGNN 預測的「第一型糖尿病」

## 一句話總結

> Insulin Degludec（DB09564）是超長效基礎胰島素類似物，但本次 Evidence Pack 中原適應症與作用機轉資料均為缺口，香港亦未上市登記。
> TxGNN 模型將其最高分預測指向**第一型糖尿病 (Type 1 Diabetes Mellitus)**，
> 目前有 **50+ 個臨床試驗**（含多個 Phase 3 RCT）與 **20 篇文獻**支持——但需特別提醒：這極可能是「已知適應症因資料缺口而被誤判為新機會」，而非真正的老藥新用發現。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（原廠核准適應症未收錄；胰島素類藥物臨床上本即用於糖尿病治療） |
| 預測新適應症 | 第一型糖尿病 (Type 1 Diabetes Mellitus) |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L1（≥2 個已完成 Phase 3 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails（附重大保留說明，見下方） |

---

## 為什麼這個預測合理？——重要保留說明

目前缺乏詳細的作用機轉資料，`original_moa` 與香港許可證資訊皆為資料缺口。

根據 Evidence Pack 中的機轉關聯分析：Insulin Degludec 是超長效基礎胰島素類似物，藥理上直接作用於胰島素受體以調控血糖。**這代表第一型糖尿病本來就是這個藥物已知、核准的適應症，而非 TxGNN 新發現的老藥新用機會。** TxGNN 給出的高分（99.44%）反映的是知識圖譜中既有的藥理關係，而 `original_indications` 欄位為空，是因為本次資料來源（DrugBank/香港藥政）未收錄該藥的原始適應症清單，屬於資料缺口，並非藥物本身無此適應症。

**建議**：此候選應標註為「已知適應症、資料缺口待修正」，而非全新的老藥新用機會；下方所列臨床試驗與文獻證據應理解為「支持既有適應症的療效安全性資料」，而非「發現新用途」的證據。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01513473](https://clinicaltrials.gov/study/NCT01513473) | Phase 3 | 完成 | 350 | BEGIN Young 1：兒童青少年 T1D 中 degludec vs detemir 療效安全性比較（26 週+26 週延伸） |
| [NCT02030600](https://clinicaltrials.gov/study/NCT02030600) | Phase 3 | 完成 | 721 | SWITCH 2：雙盲交叉試驗比較 degludec 與 glargine 安全性與療效 |
| [NCT02670915](https://clinicaltrials.gov/study/NCT02670915) | Phase 3 | 完成 | 834 | 兒童青少年 T1D 中 faster aspart 併用 degludec 之直接對照試驗 |
| [NCT00982228](https://clinicaltrials.gov/study/NCT00982228) | Phase 3 | 完成 | 629 | BEGIN: BB T1 LONG/T1：degludec 對比 glargine（皆併用 aspart）之基礎-餐時療法比較，degludec 核准之關鍵試驗之一 |
| [NCT01773798](https://clinicaltrials.gov/study/NCT01773798) | Phase 1 | 完成 | 33 | Degludec/aspart 複方於 T1D 患者之 PK/PD 特性研究 |
| [NCT03938740](https://clinicaltrials.gov/study/NCT03938740) | Phase 2 | 完成 | 61 | 探索性胰島素劑量演算法比較（HDV-lispro vs degludec） |
| [NCT04196231](https://clinicaltrials.gov/study/NCT04196231) | Phase 4 | 完成 | 258 | 合併療法（基礎胰島素+GLP-1RA/SGLT-2i）血糖控制持久性比較 |
| [NCT06199505](https://clinicaltrials.gov/study/NCT06199505) | Phase 2 | 完成 | 153 | 新藥 GZR101 對比 degludec/aspart 於 T2D 之療效安全性 |
| [NCT02392117](https://clinicaltrials.gov/study/NCT02392117) | N/A | 完成 | 1262 | Tresiba® 於真實世界 T1D/T2D 族群之安全性與有效性前瞻性觀察研究 |
| [NCT01984372](https://clinicaltrials.gov/study/NCT01984372) | N/A | 完成 | 6163 | Tresiba® 長期治療上市後安全性監測（PMS），亞洲多中心 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37863084](https://pubmed.ncbi.nlm.nih.gov/37863084/) | 2023 | RCT | Lancet | ONWARDS 6：每週一次 icodec 與每日一次 degludec 於 T1D 基礎-餐時療法比較 |
| [36623517](https://pubmed.ncbi.nlm.nih.gov/36623517/) | 2023 | RCT | Lancet Diabetes Endocrinol | EXPECT：degludec vs detemir（併用 aspart）用於 T1D 孕婦之非劣效性試驗 |
| [39270686](https://pubmed.ncbi.nlm.nih.gov/39270686/) | 2024 | RCT | Lancet | QWINT-5：每週一次 efsitora 與每日一次 degludec 於成人 T1D 之非劣效性試驗 |
| [34643020](https://pubmed.ncbi.nlm.nih.gov/34643020/) | 2022 | RCT | Diabetes Obes Metab | HypoDeg：degludec vs glargine U100 降低夜間低血糖風險之交叉試驗 |
| [34763071](https://pubmed.ncbi.nlm.nih.gov/34763071/) | 2022 | RCT | Endocr Pract | BIGLEAP：degludec 與 aspart 幫浦療法血糖控制比較之交叉試驗 |
| [36516429](https://pubmed.ncbi.nlm.nih.gov/36516429/) | 2023 | RCT | Diabetes Technol Ther | ULTRAFLEXI-1：glargine U300 與 degludec U100 於運動前後低血糖比較之交叉試驗 |
| [36763996](https://pubmed.ncbi.nlm.nih.gov/36763996/) | 2022 | Meta-analysis | Clin Ther | Degludec 與其他長效基礎胰島素於 T1D/T2D 療效耐受性之系統性回顧統合分析 |
| [35476308](https://pubmed.ncbi.nlm.nih.gov/35476308/) | 2022 | Systematic Review | Int J Clin Pharm | Degludec U100 vs Glargine U300 於 T1D 安全性、療效與成本效益之系統性回顧與間接比較 |
| [31055056](https://pubmed.ncbi.nlm.nih.gov/31055056/) | 2020 | Review | Diabetes Metab | 基於隨機與觀察性試驗之 degludec 於 T1D/T2D 現況回顧 |
| [23620200](https://pubmed.ncbi.nlm.nih.gov/23620200/) | 2013 | Review | Drugs | Degludec 與 degludec/aspart 於糖尿病治療應用之回顧 |

---

## 香港上市資訊

此藥物目前**未於香港上市**，無許可證登記資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 雖有多個 Phase 3 RCT（含大型真實世界 PMS 研究，n 最高達 6163）支持 degludec 於 T1D 之療效安全性，證據等級達 L1，但機轉分析顯示這**極可能是既有已核准適應症、因資料缺口被誤判為新候選**，而非真正的老藥新用發現，不應以「新機會」規格推進。
- 香港未上市、無許可證與安全性仿單資料，且原廠 MOA 資料缺失（DG002, High）、TFDA/香港仿單警語禁忌資料缺失（DG001, Blocking），現階段無法完成 S1 安全性初評。

**若要推進需要：**
- 確認並修正 `original_indications` 欄位（查證 DrugBank/原廠仿單，確認第一型糖尿病是否本為核准適應症）
- 取得香港藥品仿單警語與禁忌（DG001，Blocking，來源：香港衛生署/原廠仿單 PDF 解析）
- 取得完整作用機轉資料（DG002，High，來源：DrugBank API）
- 若確認為已知適應症，應將此候選自「老藥新用」清單中移除或重新分類
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

