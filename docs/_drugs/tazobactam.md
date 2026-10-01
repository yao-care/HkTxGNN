---
layout: default
title: Tazobactam
parent: 高證據等級 (L1-L2)
nav_order: 836
evidence_level: L1
indication_count: 2
---

# Tazobactam
{: .fs-9 }

證據等級: **L1** | 預測適應症: **2** 個
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

# Tazobactam：從（原適應症資料缺漏）到肺炎

## 一句話總結

Tazobactam 是 β-內醯胺酶抑制劑，只以固定複方（如 piperacillin/tazobactam、ceftolozane/tazobactam）使用。
TxGNN 模型預測它可能對**肺炎 (Pneumonia)** 有效，目前有 **43 個臨床試驗**和 **20 篇文獻**支持這個方向。
但肺炎其實是 tazobactam 複方已確立的適應症，較像「既有用途的確認」，而非真正的新用途。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺漏（香港許可證未收錄核准適應症文字） |
| 預測新適應症 | 肺炎 (Pneumonia) |
| TxGNN 預測分數 | 99.46% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 14 張 |
| 建議決策 | Proceed with Guardrails |

> 另有第 2 順位預測：泌尿道感染 (urinary tract infection)，分數 99.12%，同為 L1、Proceed with Guardrails（見文末補充）。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 未取得）。根據已知資訊，tazobactam 是 β-內醯胺酶抑制劑，用來保護搭配的 β-內醯胺類抗生素（piperacillin 或 ceftolozane）不被細菌的 β-內醯胺酶水解。

醫院內感染性肺炎與呼吸器相關肺炎，常由產 β-內醯胺酶的革蘭氏陰性菌引起。Tazobactam 能恢復夥伴抗生素對這些菌的活性，因此機轉上直接且合理。

需要注意：原適應症欄位為空是資料缺漏，不是真正的再利用訊號。多個 Phase 3 試驗中，piperacillin/tazobactam 只是對照組，而非受試的新藥。

## 臨床試驗證據

以下列出相關性最高的試驗（依 Phase 3 完成且直接相關者優先）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Phase 3 | 完成 | 726 | Ceftolozane/tazobactam vs meropenem，用於呼吸器相關／院內肺炎，主要指標為第 28 天全因死亡率（ASPECT-NP） |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Phase 3 | 完成 | 537 | Imipenem/relebactam vs piperacillin/tazobactam（對照組）用於 HABP/VABP |
| [NCT03583333](https://clinicaltrials.gov/study/NCT03583333) | Phase 3 | 完成 | 274 | 同上設計的多國試驗，piperacillin/tazobactam 為對照組 |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Phase 3 | 完成 | 460 | Levofloxacin vs piperacillin/tazobactam，用於輕中度院內肺炎 |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Phase 3 | 提前終止 | 4 | Ceftolozane/tazobactam vs piperacillin/tazobactam 用於呼吸器相關肺炎，收案過少 |
| [NCT03006679](https://clinicaltrials.gov/study/NCT03006679) | Phase 3 | 撤回 | 0 | Meropenem-vaborbactam vs piperacillin/tazobactam（TANGO III），未收案 |
| [NCT02735707](https://clinicaltrials.gov/study/NCT02735707) | Phase 3 | 招募中 | 20000 | REMAP-CAP 適應性平台試驗，社區型肺炎；是否含 piperacillin/tazobactam 未能從資料確認 |
| [NCT01796717](https://clinicaltrials.gov/study/NCT01796717) | Phase 2/3 | 未知 | 50 | Piperacillin/tazobactam 延長輸注 vs 一般輸注，用於院內肺炎 |
| [NCT06977347](https://clinicaltrials.gov/study/NCT06977347) | N/A | 尚未招募 | 100 | 重症社區型肺炎：piperacillin/tazobactam 單用 vs 併用氟喹諾酮 |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | N/A | 招募中 | 42 | 模型導向劑量 vs 經驗劑量，用於老年肺炎 |

另有多項為藥物動力學、劑量監測或診斷策略研究，與療效的關聯較間接，此處不逐一列出。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | Ceftolozane-tazobactam vs meropenem 用於革蘭氏陰性院內肺炎的 Phase 3 非劣性試驗（ASPECT-NP） |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | Imipenem/relebactam vs piperacillin/tazobactam 用於 HABP/VABP（RESTORE-IMI 2） |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Imipenem/relebactam vs piperacillin/tazobactam 的 Phase 3 非劣性試驗，針對 HABP/VABP |
| [30208454](https://pubmed.ncbi.nlm.nih.gov/30208454/) | 2018 | RCT | JAMA | 針對產 ESBL 的血流感染，piperacillin-tazobactam 對比 meropenem（MERINO）；非肺炎，但為重要的警示證據 |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | 系統性回顧 | Clin Microbiol Infect | 非呼吸器相關院內肺炎經驗性抗生素的網絡統合分析 |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | 系統性回顧 | Int J Antimicrob Agents | 新型 β-內醯胺類及抑制劑複方治療碳青黴烯抗藥菌肺炎的 PK/PD |
| [39701120](https://pubmed.ncbi.nlm.nih.gov/39701120/) | 2025 | 世代研究 | Lancet Infect Dis | Ceftazidime-avibactam vs ceftolozane-tazobactam 治療多重抗藥綠膿桿菌感染（CACTUS） |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | 世代研究 | Clin Infect Dis | 綠膿桿菌菌血症或肺炎中，ceftolozane-tazobactam 的抗藥性產生率低於 ceftazidime-avibactam（10% vs 40%） |
| [32662691](https://pubmed.ncbi.nlm.nih.gov/32662691/) | 2020 | Review | Expert Rev Anti Infect Ther | Ceftolozane/tazobactam 用於院內肺炎的回顧 |
| [41305690](https://pubmed.ncbi.nlm.nih.gov/41305690/) | 2025 | 個案報告 | Medicine | Piperacillin-tazobactam 引發噬血球性淋巴組織球增生症（HLH），並造成降鈣素原升高的診斷困難 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66929 | PIPERACILLIN AND TAZOBACTAM POWDER FOR SOLUTION FOR INFUSION 4.5G | 未載明 | 資料未提供 |
| HK-65419 | PIPERACILLIN/TAZOBACTAM KABI POWDER FOR SOLUTION FOR INFUSION 4G/0.5G | 未載明 | 資料未提供 |
| HK-65156 | ZERBAXA POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 1G/0.5G | 未載明 | 資料未提供 |
| HK-60314 | PYBACTAM 4.5G POWDER FOR SOLN FOR INJ/INF | 未載明 | 資料未提供 |
| HK-52054 | TAZOBACTAM/PIPERACILLIN SOD F/ INJ 2.25G (ZHUHAI UNITED LAB) | 未載明 | 資料未提供 |

香港共 14 張許可證，上表為其中 5 張。

## 安全性考量

安全性資訊請參考原廠仿單。目前未取得香港衛生署仿單的警語與禁忌資料，藥物交互作用查詢也無結果。

文獻中有兩項值得留意的訊號：
- piperacillin-tazobactam 有引發 HLH 的個案報告（PMID 41305690）。
- 腎功能不全時，含 tazobactam 的複方需留意劑量調整（PMID 30219824）。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個已完成的 Phase 3 RCT，包括 ceftolozane/tazobactam 的 ASPECT-NP，支持 tazobactam 複方用於院內及呼吸器相關肺炎，證據等級為 L1。
- Tazobactam 只以固定複方使用，療效無法單獨歸因於它。多項 Phase 3 試驗中它也只是對照組。肺炎屬既有適應症，不是新的再利用發現。

**若要推進需要：**
- 取得香港衛生署仿單，補齊適應症、警語與禁忌。
- 補齊 DrugBank 的作用機轉資料。
- 依夥伴抗生素與本地抗藥性資料評估適用性。
- 確認 NCT02735707（REMAP-CAP）是否含 piperacillin/tazobactam 組別。

## 補充：第 2 順位預測（泌尿道感染）

| 項目 | 內容 |
|------|------|
| TxGNN 預測分數 | 99.12% |
| 證據等級 | L1 |
| 建議決策 | Proceed with Guardrails |

- **臨床試驗**：[NCT03687255](https://clinicaltrials.gov/study/NCT03687255)（Phase 3，完成，1043 人，cefepime-AAI101 vs piperacillin/tazobactam 用於複雜性泌尿道感染）。[NCT03891433](https://clinicaltrials.gov/study/NCT03891433)（Phase 4，暫停，198 人，piperacillin/tazobactam vs 碳青黴烯，用於產 ESBL 的非菌血症泌尿道感染）。
- **文獻**：PMID [36194218](https://pubmed.ncbi.nlm.nih.gov/36194218/)（JAMA 2022）、[28592240](https://pubmed.ncbi.nlm.nih.gov/28592240/)（BMC Infect Dis 2017）、[29486041](https://pubmed.ncbi.nlm.nih.gov/29486041/)（JAMA 2018）。
- **注意事項**：MERINO 試驗（PMID 30208454）顯示，對產 ESBL 的大腸桿菌與克雷伯氏菌血流感染，piperacillin-tazobactam 表現不如 meropenem，需特別留意。此外，複雜性泌尿道感染同樣是既有適應症，不是新發現。

> 本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

