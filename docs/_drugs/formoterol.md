---
layout: default
title: Formoterol
parent: 僅模型預測 (L5)
nav_order: 391
evidence_level: L5
indication_count: 6
---

# Formoterol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Formoterol：從氣喘／慢性阻塞性肺病（COPD）到呼吸道畸形

## 一句話總結

Formoterol 是長效 β2 腎上腺素受器促效劑，香港上市的相關產品（如 Foster、Symbicort、Duaklir）主要用於氣喘與 COPD 的支氣管擴張治療。
TxGNN 模型預測它可能對**呼吸道畸形 (Respiratory Malformation)** 有效，分數很高，但目前**沒有任何針對此適應症的臨床試驗或文獻**。檢索到的 25 個試驗和 10 篇文獻都是氣喘與 COPD 研究，只是關鍵字相符，這個預測應視為模型的關聯性假象。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 呼吸道畸形 (Respiratory Malformation) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5（無直接研究支持；證據包標示為 L4，但未見前臨床或機轉研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Formoterol 是長效 β2 促效劑，作用是放鬆支氣管平滑肌，改善氣流阻塞，在氣喘與 COPD 中的療效已被證實。

但呼吸道畸形是發育過程中的結構性缺陷，支氣管擴張劑只能緩解症狀，無法矯正結構異常。因此機轉上沒有直接關聯。

0.999 的高分較可能反映知識圖譜中，Formoterol 與阻塞性呼吸道表型距離很近，而不是真實的治療訊號。此預測的合理性偏低。

## 臨床試驗證據

以下試驗都是氣喘或 COPD 研究，沒有一個針對呼吸道畸形。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03324607](https://clinicaltrials.gov/study/NCT03324607) | Phase 2/3 | 完成 | 20 | Glycopyrrolate/Formoterol 用於 COPD，以 129Xe MRI 評估通氣與氣體交換異常；針對後天疾病，與先天畸形無關 |
| [NCT03453112](https://clinicaltrials.gov/study/NCT03453112) | Phase 3 | 完成 | 494 | Foster NEXThaler 對比 pMDI 用於控制良好的氣喘，非劣性試驗；族群與呼吸道畸形無關 |
| [NCT00861926](https://clinicaltrials.gov/study/NCT00861926) | Phase 3 | 完成 | 1714 | Foster 維持與緩解治療 (MART) 對比固定劑量加 Salbutamol，用於氣喘；族群不符 |
| [NCT00130351](https://clinicaltrials.gov/study/NCT00130351) | Phase 3 | 完成 | 155 | Formoterol 新型吸入裝置的患者使用性評估（氣喘） |
| [NCT01577082](https://clinicaltrials.gov/study/NCT01577082) | Phase 3 | 完成 | 542 | CHF 1535（BDP/Formoterol）對比 BDP，用於控制不佳的成人氣喘 |
| [NCT03888131](https://clinicaltrials.gov/study/NCT03888131) | Phase 3 | 完成 | 750 | BDP/Formoterol 對比 Symbicort，用於 COPD 的肺功能非劣性試驗 |
| [NCT03197818](https://clinicaltrials.gov/study/NCT03197818) | Phase 3 | 完成 | 708 | BDP/Formoterol/Glycopyrronium 三合一對比 Symbicort，用於 COPD |
| [NCT02345161](https://clinicaltrials.gov/study/NCT02345161) | Phase 3 | 完成 | 1811 | FF/UMEC/VI 對比 Budesonide/Formoterol，用於 COPD，為期 24 週 |
| [NCT01245569](https://clinicaltrials.gov/study/NCT01245569) | Phase 3 | 完成 | 419 | Foster 對比 Seretide，用於 COPD |
| [NCT00931385](https://clinicaltrials.gov/study/NCT00931385) | Phase 3 | 完成 | 99 | BI 1744 CL 與 Foradil（Formoterol）在 COPD 的 24 小時 FEV1 曲線比較 |

## 文獻證據

以下文獻同樣與呼吸道畸形無關，僅列出檢索結果。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22541245](https://pubmed.ncbi.nlm.nih.gov/22541245/) | 2012 | RCT | J Allergy Clin Immunol | Budesonide/Formoterol pMDI 用於非裔美國氣喘患者的長期安全性 |
| [35115339](https://pubmed.ncbi.nlm.nih.gov/35115339/) | 2022 | RCT（交叉試驗） | Eur Respir J | 成人氣喘重複給藥時，Budesonide/Formoterol 與 Salbutamol 的支氣管擴張與副作用比較 |
| [40840693](https://pubmed.ncbi.nlm.nih.gov/40840693/) | 2026 | 系統性回顧／統合分析 | J Am Pharm Assoc | BGF 對比 GFF 用於 COPD 的安全性與療效 |
| [20528601](https://pubmed.ncbi.nlm.nih.gov/20528601/) | 2010 | Review | J Asthma | Symbicort pMDI 用於持續性氣喘的療效與安全性回顧 |
| [24842803](https://pubmed.ncbi.nlm.nih.gov/24842803/) | 2014 | Review | Prog Neuropsychopharmacol Biol Psychiatry | 唐氏症認知功能障礙的神經傳導物質治療策略；與 Formoterol 關聯薄弱 |
| [35034195](https://pubmed.ncbi.nlm.nih.gov/35034195/) | 2022 | 臨床生理學研究 | Eur J Appl Physiol | COPD 睡眠期間呼吸力學異常的代償反應 |
| [30662579](https://pubmed.ncbi.nlm.nih.gov/30662579/) | 2018 | 世代研究 | Can Respir J | 妊娠氣喘婦女的吸入器使用錯誤與母胎結果 |
| [14738234](https://pubmed.ncbi.nlm.nih.gov/14738234/) | 2004 | 臨床研究 | Eur Respir J | Formoterol 可對抗氣喘患者的血小板活化因子 (PAF) 誘發效應 |
| [37691104](https://pubmed.ncbi.nlm.nih.gov/37691104/) | 2023 | Case report | J Med Case Rep | 長新冠患者的小氣道疾病三年追蹤 |
| [41686546](https://pubmed.ncbi.nlm.nih.gov/41686546/) | 2026 | Case report | Medicine | 肺癌術後患者的 Schizophyllum commune 相關過敏性支氣管肺黴菌症 |

## 香港上市資訊

香港共有 13 張 Formoterol 相關許可證，以下列出 5 張。資料未提供劑型與核准適應症。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61392 | FOSTER PRESSURISED INHALATION SOLUTION 100/6 MICROGRAMS PER ACTUATION | — | — |
| HK-62090 | FLUTIFORM 250 MICROGRAM/10 MICROGRAM PER ACTUATION PRESSURISED INHALATION SUSPENSION | — | — |
| HK-64503 | DUAKLIR GENUAIR INHALATION POWDER 340 MCG/12 MCG | — | — |
| HK-60618 | VANNAIR PRESSURIZED METERED-DOSE INHALER 80/4.5MCG/DOSE | — | — |
| HK-49176 | SYMBICORT TURBUHALER 160/4.5MCG/DOSE | — | — |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 呼吸道畸形是結構性發育缺陷，β2 促效劑無法矯正，機轉上找不到合理連結。
- 0.999 的分數應視為知識圖譜的關聯性假象。所有檢索到的試驗與文獻都是氣喘或 COPD，沒有直接證據。

**若要推進需要：**
- 找出針對呼吸道畸形（如先天性肺氣道畸形）的 Formoterol 研究，或提出可檢驗的機轉假說。
- 取得香港衛生署仿單的警語與禁忌資料，並補齊 DrugBank 作用機轉資料。

**其他預測適應症的參考：**
- 支氣管炎、阻塞性肺病與氣喘的證據較強（L1，建議 Proceed with Guardrails）。
- 這三者屬於現有的氣喘與 COPD 適應症範圍，不是新的老藥新用機會。
- 大部分證據來自固定劑量複方（如 Budesonide/Formoterol），無法單獨歸因於 Formoterol。
- 使用時需注意心血管監測。氣喘不可單用 LABA，需併用吸入型類固醇。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

