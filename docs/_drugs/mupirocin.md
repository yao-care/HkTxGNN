---
layout: default
title: Mupirocin
parent: 中證據等級 (L3-L4)
nav_order: 511
evidence_level: L3
indication_count: 10
---

# Mupirocin
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Mupirocin：從皮膚抗菌用途到葡萄球菌燙傷樣皮膚症候群（SSSS）輔助治療

> 本評估涵蓋 TxGNN 對 Mupirocin 提出的 10 個候選適應症（candidate_id: TW-DB00410-multi）。多數候選僅為模型分數高但機轉不合理或全無實證，本報告聚焦於證據等級與決策階段最佳的候選——**葡萄球菌燙傷樣皮膚症候群 (SSSS)**，並附上完整候選總覽供對照。

## 一句話總結

Mupirocin 為外用（皮膚/鼻腔）抗金黃色葡萄球菌（含 MRSA）抗生素。TxGNN 模型對其提出 10 個候選新適應症，其中分數最高的「肋膜膿胸」在機轉與給藥途徑上皆不可行；相對地，**葡萄球菌燙傷樣皮膚症候群 (SSSS)** 雖 TxGNN 分數排名第 9，但有 **14 篇文獻**支持其作為輔助清除帶菌病灶的角色，是本組候選中證據最紮實者。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（正式核准適應症未記載；依再利用理由文字，Mupirocin 屬外用皮膚/鼻腔抗金黃色葡萄球菌抗生素） |
| 預測新適應症 | 葡萄球菌燙傷樣皮膚症候群 (Staphylococcal Scalded Skin Syndrome, SSSS) |
| TxGNN 預測分數 | 95.57%（排名第 9／10） |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold（研究優先） |

## 十大候選適應症總覽

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 | 備註 |
|------|------|-----------|---------|---------|------|------|
| 1 | 肋膜膿胸 (pleural empyema) | 99.49% | L5 | S0 | Hold | 外用劑型無法達胸腔深部感染，機轉不可行 |
| 2 | 點狀角膜結膜炎 | 99.10% | L5 | S0 | Hold | 無任何臨床/文獻證據 |
| 3 | 神經營養性角膜病變 | 98.48% | L5 | S0 | Hold | 非感染性病因，機轉無關聯 |
| 4 | 皮膚念珠菌病 | 98.27% | L3 | S1 | Research Question | 2 篇文獻，機轉為間接（清除續發性細菌感染） |
| 5 | 陰道分泌物 | 96.01% | L4 | S0 | Hold | 唯一相關試驗聚焦鼻腔/皮膚除菌，非陰道適應症 |
| 6 | 曝露性角膜炎 | 95.89% | L4 | S0 | Hold | 僅體外抗菌活性研究，無臨床療效資料 |
| 7 | 陰道白斑症 | 95.81% | L5 | S0 | Hold | 非感染性病灶，無實證 |
| 8 | non-human animal disease | 95.66% | L5 | S0 | Hold | 知識圖譜資料雜訊，建議排除 |
| **9** | **葡萄球菌燙傷樣皮膚症候群** | **95.57%** | **L3** | **S2** | **Research Question** | **14 篇文獻，決策階段最高** |
| 10 | 細菌性陰道炎 | 95.19% | L4 | S0 | Hold | 僅 1 篇 MRSA 陰道炎個案報告，非典型 BV 致病菌 |

## 為什麼這個預測合理？

Mupirocin 的正式作用機轉（MOA）欄位為資料缺口（DG002），但依證據包內多筆再利用理由描述，其藥理機轉為：透過抑制細菌異白胺酸-tRNA 合成酶（isoleucyl-tRNA synthetase）阻斷蛋白質合成，對 Gram 陽性球菌（含 MRSA）具高選擇性抗菌活性，臨床上常用於皮膚感染治療與鼻腔/皮膚金黃色葡萄球菌帶菌清除（decolonization）。

SSSS 由分泌外毒素（exfoliative toxin A/B）的金黃色葡萄球菌引起，臨床特徵是皮膚廣泛剝脫，但致病機轉是「毒素介導」而非局部組織的直接細菌侵犯。Mupirocin 的角色因此並非直接中和已釋出的外毒素，而是清除帶菌病灶（鼻腔、皮膚），減少毒素持續產生的來源，屬於輔助性、非典型的「新適應症」。

文獻中已有多筆探討 mupirocin 併用全身性抗生素治療 SSSS 的實務經驗（如 PMID 37404367 直接比較不同靜脈抗生素併用 2% mupirocin 藥膏的療效），顯示此用法在臨床上已有一定實作基礎，但均屬觀察性研究或病例系列，尚無隨機對照試驗驗證。

需特別指出：TxGNN 分數最高的候選「肋膜膿胸」（99.49%）機轉上不可行——Mupirocin 僅有外用劑型、全身生體可用率極低，無法治療胸腔內深部感染，說明本組候選不能單以模型分數排序，須以證據等級與決策階段綜合判斷。

## 臨床試驗證據

目前無相關臨床試驗登記（SSSS 適應症）。

> 補充：候選 #5「陰道分泌物」有 1 個間接相關試驗 [NCT07142408](https://clinicaltrials.gov/study/NCT07142408)（Phase 3，術前細菌 decolonization 對下肢術後感染率影響），但與 SSSS 或本報告主軸無直接關聯，僅供對照參考。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37404367](https://pubmed.ncbi.nlm.nih.gov/37404367/) | 2023 | Cohort | Clin Cosmet Investig Dermatol | 比較不同靜脈抗生素併用 2% mupirocin 藥膏治療兒童 SSSS 之療程、影響因子與費用 |
| [15482208](https://pubmed.ncbi.nlm.nih.gov/15482208/) | 2004 | Review | Expert Rev Anti Infect Ther | 回顧嬰兒膿疱瘡與 SSSS 的治療方式 |
| [16009455](https://pubmed.ncbi.nlm.nih.gov/16009455/) | 2005 | Cohort (outbreak) | J Hosp Infect | 新生兒單位 SSSS 院內群聚事件的流行病學調查與感染管制 |
| [9576389](https://pubmed.ncbi.nlm.nih.gov/9576389/) | 1998 | Cohort (molecular epi) | Pediatr Infect Dis J | 極低出生體重早產兒 SSSS 分子流行病學與感染控制策略 |
| [35901469](https://pubmed.ncbi.nlm.nih.gov/35901469/) | 2022 | Case Series | Adv Neonatal Care | 新生兒 SSSS 辨識與傷口照護病例系列 |
| [30418106](https://pubmed.ncbi.nlm.nih.gov/30418106/) | 2019 | Case Report/Series | J Med Microbiol | 新出現的產毒性、mupirocin/fusidic acid 具抗藥性 MSSA clone 引起之 SSSS |
| [28592549](https://pubmed.ncbi.nlm.nih.gov/28592549/) | 2017 | Case Report | J Clin Microbiol | 帶外毒素基因、對 mupirocin 及 fusidic acid 具抗藥性之金黃色葡萄球菌 clone 出現 |
| [31725120](https://pubmed.ncbi.nlm.nih.gov/31725120/) | 2020 | Case Series | Pediatr Infect Dis J | 休士頓地區 ST121 菌株引起 SSSS 病例增加之分子流行病學 |
| [27047925](https://pubmed.ncbi.nlm.nih.gov/27047925/) | 2014 | Case Report | Dermatopathology | 化療中成人發生 SSSS 之罕見病例 |
| [8435912](https://pubmed.ncbi.nlm.nih.gov/8435912/) | 1993 | Review | Dermatol Clin | 皮膚病中控制金黃色葡萄球菌之重要性，肯定外用 mupirocin 的臨床角色 |

## 香港上市資訊

目前未在香港上市，無許可證資料。

## 安全性考量

安全性資訊請參考原廠仿單。

> 注意：TFDA 仿單警語/禁忌資料為**阻斷級（Blocking）資料缺口**（DG001），目前無法完成 S1 安全性初評，此為推進本候選前必須補齊的項目。

## 結論與下一步

**決策：Hold（研究優先）**

**理由：**
- SSSS 候選雖具本組候選中最佳的證據等級（L3）與決策階段（S2），但現有文獻均為觀察性研究、病例系列或回顧，缺乏隨機對照試驗，且無任何臨床試驗登記直接驗證此適應症。
- 安全性資料為阻斷級缺口，且 Mupirocin 目前未在香港上市，缺乏在地法規與供應基礎。

**若要推進需要：**
- 補齊 TFDA/原廠仿單警語與禁忌症資料（DG001，阻斷級，必要項目）
- 取得正式 DrugBank MOA 與原始核准適應症資料（DG002）
- 針對 mupirocin 併用全身性抗生素治療 SSSS 之療效與安全性，規劃前瞻性對照研究
- 評估香港在地上市與供應可行性
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

