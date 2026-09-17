---
layout: default
title: Vilanterol
parent: 僅模型預測 (L5)
nav_order: 795
evidence_level: L5
indication_count: 5
---

# Vilanterol
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

# Vilanterol：邁向阻塞性肺病（Obstructive Lung Disease）適應症的老藥新用評估

## 一句話總結

Vilanterol（DrugBank ID: DB09082）目前在本 Evidence Pack 中缺乏原始核准適應症與作用機轉紀錄。
TxGNN 模型預測它可能對**阻塞性肺病 (Obstructive Lung Disease)** 有效，
目前有 **80+ 個臨床試驗**（含多個大型 Phase 3 RCT）和 **20 篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（原始適應症紀錄未提供，屬資料缺口） |
| 預測新適應症 | 阻塞性肺病 (Obstructive Lung Disease) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L1（≥2 個已完成的 Phase 3 RCT） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（Evidence Pack 標記為資料缺口 DG002），原始核准適應症也未提供對應紀錄。

不過從臨床試驗與文獻證據可以觀察到，Vilanterol 作為長效型 β2 受體促效劑 (LABA)，
在全球已被廣泛以複方形式（與 Fluticasone Furoate、Umeclidinium 等成分組合）
用於慢性阻塞性肺病 (COPD) 與氣喘的治療，累積了大量 Phase 3 等級的隨機對照試驗證據
（如 IMPACT、FULFIL、CAPTAIN、SUMMIT 等指標性試驗）。

這些試驗的治療族群與終點高度集中於「阻塞性肺病」的氣流限制、急性惡化與肺功能改善，
與 TxGNN 預測的新適應症具有直接的臨床一致性。換言之，此預測方向與該成分已被驗證的
臨床應用範疇高度吻合，機轉上的合理性可由既有大規模 RCT 佐證，但仍需補齊正式的 MOA
與原適應症紀錄以完善審查基礎。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01313676](https://clinicaltrials.gov/study/NCT01313676) | Phase 3 | 完成 | 16568 | FF/Vilanterol 對中度 COPD 合併心血管疾病風險患者存活率的影響（SUMMIT 試驗） |
| [NCT02924688](https://clinicaltrials.gov/study/NCT02924688) | Phase 3 | 完成 | 2436 | FF/UMEC/VI 三合一療法 vs FF/VI 雙合一於控制不佳氣喘患者之療效比較 |
| [NCT02345161](https://clinicaltrials.gov/study/NCT02345161) | Phase 3 | 完成 | 1811 | FF/UMEC/VI 每日一次 vs Budesonide/Formoterol 每日兩次於 COPD 之肺功能與健康狀態改善 |
| [NCT02105974](https://clinicaltrials.gov/study/NCT02105974) | Phase 3 | 完成 | 1621 | FF/VI 100/25mcg vs VI 25mcg 單方於 COPD 之肺功能貢獻度評估 |
| [NCT02729051](https://clinicaltrials.gov/study/NCT02729051) | Phase 3 | 完成 | 1055 | 「封閉式」三合一（FF/UMEC/VI）vs「開放式」三合一（FF/VI + UMEC）於 COPD 肺功能比較 |
| [NCT01686633](https://clinicaltrials.gov/study/NCT01686633) | Phase 3 | 完成 | 1040 | FF/VI 200/25mcg 與 100/25mcg 兩劑量及 FF 單方於持續性氣喘之療效比較 |
| [NCT03219255](https://clinicaltrials.gov/study/NCT03219255) | N/A | 完成 | 1047 | Relvar 100 Ellipta（FF/VI）於 COPD 長期臨床實務之特殊藥物使用調查 |
| [NCT01316913](https://clinicaltrials.gov/study/NCT01316913) | Phase 3 | 完成 | 872 | UMEC/VI 兩劑量 vs UMEC 單方 vs Tiotropium 於 COPD 之療效與安全性比較 |
| [NCT01822899](https://clinicaltrials.gov/study/NCT01822899) | Phase 3 | 完成 | 717 | UMEC/VI vs Fluticasone Propionate/Salmeterol 於 COPD 之療效與安全性比較 |
| [NCT03478696](https://clinicaltrials.gov/study/NCT03478696) | Phase 4 | 完成 | 732 | 單一吸入器三合一（FF/UMEC/VI）vs 多吸入器療法（Budesonide/Formoterol + Tiotropium）於 COPD 之肺功能與症狀比較 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29668352](https://pubmed.ncbi.nlm.nih.gov/29668352/) | 2018 | RCT | New England Journal of Medicine | IMPACT 試驗：COPD 患者單一吸入器三合一療法 vs 雙合一療法比較 |
| [28375647](https://pubmed.ncbi.nlm.nih.gov/28375647/) | 2017 | RCT | American Journal of Respiratory and Critical Care Medicine | FULFIL 試驗：COPD 患者每日一次三合一療法療效驗證 |
| [32918892](https://pubmed.ncbi.nlm.nih.gov/32918892/) | 2021 | RCT | The Lancet Respiratory Medicine | CAPTAIN 試驗：FF/UMEC/VI 三合一 vs FF/VI 於控制不佳氣喘之療效與安全性 |
| [29094315](https://pubmed.ncbi.nlm.nih.gov/29094315/) | 2017 | RCT | Advances in Therapy | UMEC/VI 與 Tiotropium/Olodaterol 於症狀性 COPD 之療效直接比較 |
| [35849317](https://pubmed.ncbi.nlm.nih.gov/35849317/) | 2022 | Meta-analysis | Advances in Therapy | FF/UMEC/VI 與其他 COPD 療法之網絡統合分析 |
| [39696097](https://pubmed.ncbi.nlm.nih.gov/39696097/) | 2024 | Systematic Review/Meta-analysis | BMC Pulmonary Medicine | UMEC/VI 與其他支氣管擴張劑於 COPD 治療之系統性回顧與統合分析 |
| [31389190](https://pubmed.ncbi.nlm.nih.gov/31389190/) | 2019 | Systematic Review | The Clinical Respiratory Journal | UMEC/VI 固定劑量複方於 COPD 之系統性回顧 |
| [32162970](https://pubmed.ncbi.nlm.nih.gov/32162970/) | 2020 | RCT (事後分析) | American Journal of Respiratory and Critical Care Medicine | FF/UMEC/VI 降低 COPD 患者全因死亡率（IMPACT 試驗事後分析） |
| [39797646](https://pubmed.ncbi.nlm.nih.gov/39797646/) | 2024 | Cohort Study | BMJ | 單一吸入器三合一療法於 COPD 之療效與安全性比較（新使用者世代研究） |
| [37213116](https://pubmed.ncbi.nlm.nih.gov/37213116/) | 2023 | Cohort Study | JAMA Internal Medicine | 複方吸入劑新使用者之 COPD 急性惡化與肺炎住院比較 |

## 香港上市資訊

Vilanterol 目前在香港**未上市**，無許可證資料。

## 安全性考量

安全性資訊請參考原廠仿單。目前缺乏香港仿單警語、禁忌症與藥物交互作用資料（資料缺口 DG001，嚴重度：Blocking），此為進入安全性初評 (S1) 前須補齊的關鍵項目。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 國際間已有多個大型已完成 Phase 3 RCT（如 IMPACT、FULFIL、CAPTAIN、SUMMIT）支持 Vilanterol 相關複方於阻塞性肺病的療效，證據等級達 L1。
- 然而香港仿單警語/禁忌症資料為 Blocking 等級缺口，且該藥目前未在香港上市（0 張許可證），在補齊安全性資料前不宜直接推進。

**若要推進需要：**
- 取得香港/原廠仿單之警語、禁忌症與藥物交互作用資料，完成 S1 安全性初評
- 補齊 Vilanterol 的詳細作用機轉 (MOA) 資料
- 確認原始核准適應症紀錄，釐清此候選是否為既有適應症之在地化上市申請，而非全新老藥新用假說
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

