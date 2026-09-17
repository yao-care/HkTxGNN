---
layout: default
title: Potassium Chloride
parent: 中證據等級 (L3-L4)
nav_order: 604
evidence_level: L4
indication_count: 1
---

# Potassium Chloride
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Potassium Chloride（氯化鉀）：原適應症資料缺失 → 腎小管性酸中毒（Renal Tubular Acidosis）

## 一句話總結

Potassium Chloride（DrugBank ID: DB00761）目前缺乏原適應症與作用機轉資料，且尚未在香港取得上市許可證。TxGNN 模型預測它可能對**腎小管性酸中毒（Renal Tubular Acidosis, RTA）**有效，目前有 **9 個相關臨床試驗**和 **19 篇文獻**，但均未直接針對「KCl 用於 RTA」進行介入性研究，證據屬機轉合理但間接。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（DrugBank 原始適應症與 MOA 均缺失） |
| 預測新適應症 | 腎小管性酸中毒 (Renal Tubular Acidosis) |
| TxGNN 預測分數 | 99.87%（Rank 3352） |
| 證據等級 | L4 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 Potassium Chloride 詳細的作用機轉（MOA）資料，也沒有記錄到的原始核准適應症，這是本項預測的一個重要限制。

不過根據證據包中的機轉關聯分析：RTA（尤其遠端型/第 I 型及部分近端型）常伴隨慢性尿鉀流失導致低血鉀，臨床上鉀離子補充是糾正低血鉀的標準支持性治療。但需注意，單純 KCl 只補鉀、不糾正酸血症，且其氯離子負荷可能加重 RTA 常見的高氯性代謝性酸血症——臨床指引在 RTA 情境下多優先選用檸檬酸鉀（同時提供鹼化前驅物）而非 KCl。

因此，這個預測在機轉方向上具合理性（鉀離子補充確實是 RTA 支持性治療的一環），但缺乏針對 KCl 本身在 RTA 族群的直接介入性試驗證據，屬於「機轉合理、證據間接」的類型，需要謹慎解讀。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00120731](https://clinicaltrials.gov/study/NCT00120731) | N/A | WITHDRAWN | 0 | 檸檬酸鉀用於兒童特發性高鈣尿症之尿液化學與酸鹼效應研究；試驗已撤回，enrollment 為 0 |
| [NCT03354507](https://clinicaltrials.gov/study/NCT03354507) | N/A | UNKNOWN | 40 | 碳酸氫鈉鹼化療法用於 Topiramate 誘發之腎小管性酸中毒（試驗性研究） |
| [NCT03644706](https://clinicaltrials.gov/study/NCT03644706) | Phase 3 | TERMINATED | 3 | ADV7103 用於預防遠端 RTA 患者代謝性酸中毒惡化，因入組不足而終止 |
| [NCT06750172](https://clinicaltrials.gov/study/NCT06750172) | N/A | RECRUITING | 33 | 原發性醛固酮症診斷方法學比較（尿液醛固酮檢測），非治療性介入 |
| [NCT07273838](https://clinicaltrials.gov/study/NCT07273838) | Phase 2 | RECRUITING | 130 | SGLT2 抑制劑用於急性心腎症候群，機轉與 KCl 補充無關 |
| [NCT01834768](https://clinicaltrials.gov/study/NCT01834768) | Phase 2 | UNKNOWN | 31 | Eplerenone 用於環孢素治療之移植病人安全性研究，機轉為保鉀非補鉀 |
| [NCT01843309](https://clinicaltrials.gov/study/NCT01843309) | Phase 4 | TERMINATED | 36 | Spironolactone 預防 Amphotericin B 相關電解質異常 |
| [NCT01894594](https://clinicaltrials.gov/study/NCT01894594) | Phase 1 | TERMINATED | 7 | 鹼性療法用於鎌狀細胞病之酸鹼平衡評估 |
| [NCT06867471](https://clinicaltrials.gov/study/NCT06867471) | N/A | RECRUITING | 43 | 外源性酮症對慢性腎病及多囊腎患者蛋白尿與腎功能之效應 |

**註**：以上試驗多為間接相關（RTA 或酸鹼平衡治療情境），尚無直接評估 Potassium Chloride 於 RTA 適應症之介入性試驗。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17297212](https://pubmed.ncbi.nlm.nih.gov/17297212/) | 2007 | Review | Acta Med Indones | 低血鉀病因與處置綜述，涵蓋腎性/腎外性鉀流失機轉 |
| [33459628](https://pubmed.ncbi.nlm.nih.gov/33459628/) | 2021 | Review | Arch Esp Urol | 腎小管性酸中毒診斷與治療綜述，含遠端型 RTA 致低血鉀與腎結石機轉 |
| [8694660](https://pubmed.ncbi.nlm.nih.gov/8694660/) | 1996 | Review | Arch Intern Med | RTA 病理生理與診斷方法之經典綜述 |
| [37081692](https://pubmed.ncbi.nlm.nih.gov/37081692/) | 2023 | Review | Endocrine Journal | 將假性醛固酮低下症第二型重新分類為第四型 RTA 之文獻回顧 |
| [38445406](https://pubmed.ncbi.nlm.nih.gov/38445406/) | 2023 | Cohort | La Tunisie Medicale | 突尼西亞遠端 RTA 病人之基因型-表現型關聯研究 |
| [783200](https://pubmed.ncbi.nlm.nih.gov/783200/) | 1976 | Cohort/Physiology | J Clin Invest | 以碳酸氫鉀矯正典型（第一型）RTA 酸血症後，鈉氯保留能力受損之研究 |
| [14048071](https://pubmed.ncbi.nlm.nih.gov/14048071/) | 1963 | Review | Med Bulletin (Ann Arbor) | 腎小管性酸中毒之早期綜述文獻 |
| [34748193](https://pubmed.ncbi.nlm.nih.gov/34748193/) | 2022 | Case Report | J Nephrol | 妊娠期遠端 RTA 合併低血鉀性週期性麻痺病例報告 |
| [40288831](https://pubmed.ncbi.nlm.nih.gov/40288831/) | 2025 | Case Report | Nefrologia | 原發性 RTA 妊娠期病例報告及周產期預後文獻回顧 |
| [28509102](https://pubmed.ncbi.nlm.nih.gov/28509102/) | 2015 | Case Report | CEN Case Reports | 小兒 Sjogren 症候群合併遠端 RTA 及自體免疫甲狀腺低能症之罕見病例 |

## 香港上市資訊

目前無香港上市許可證資料（藥物狀態：未上市）。

## 安全性考量

安全性資訊請參考原廠仿單。

**額外提醒**：證據包標示一項 Blocking 等級資料缺口——尚缺 TFDA/HK 官方仿單警語與禁忌症資料，此缺口目前阻擋本案進入 S1 安全性初評，需優先補齊後方可進行下一步安全性審查。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- TxGNN 預測分數高（99.87%），且鉀離子補充在 RTA 支持性治療中有機轉合理性，但目前無任何研究直接評估 KCl（相對於檸檬酸鉀等鹼化鉀鹽）用於 RTA 的療效與安全性，證據等級僅達 L4。

**若要推進需要：**
- 補齊 TFDA/HK 官方仿單警語與禁忌症資料（Blocking 缺口，DG001）
- 取得 Potassium Chloride 之詳細作用機轉（MOA）資料（DG002）
- 補充原始核准適應症資料，以利與 RTA 適應症進行機轉比對
- 評估是否應以「同類鉀鹽/鹼化療法」（如檸檬酸鉀）作為更貼近的機轉對照組，釐清單純氯化鉀補充在 RTA 中的角色與風險（尤其高氯性酸中毒加重疑慮）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

