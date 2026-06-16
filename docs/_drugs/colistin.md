---
layout: default
title: Colistin
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
---

# Colistin
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

# Colistin：從 MDR 革蘭氏陰性菌感染到感染後症候群預防

## 一句話總結

Colistin（多黏菌素 E，Polymyxin E）是多黏菌素類抗生素，長期作為多重耐藥（MDR）革蘭氏陰性菌感染的最後防線用藥，在香港目前無已登記的許可證。TxGNN 模型共預測 **10 個新適應症**，最具臨床意義的是**感染後症候群（Post-infectious Syndrome）預防**，由選擇性消化道去污染（SDD）方案的 **Phase 3 RCT（20,010 名 ICU 患者）**提供最強支持；**鼻竇炎**（MDR 革蘭氏陰性菌相關）亦有 **13 篇文獻**佐證。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症（國際已知） | MDR 革蘭氏陰性菌感染（CRAB、CRE、CRPA）最後防線用藥 |
| 最佳證據新適應症 | 感染後症候群 (Post-infectious Syndrome)（預防） |
| TxGNN 預測分數 | 99.91%（排名 #2,495） |
| 證據等級 | L2（Phase 3 RCT 間接支持） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 待補充）。根據已知資訊，Colistin 屬多黏菌素類（Polymyxin）抗生素，透過與革蘭氏陰性菌外膜的脂多糖（LPS）結合，破壞細菌細胞膜通透性導致菌體死亡。抗菌譜涵蓋 CRAB（碳青黴烯耐藥鮑氏不動桿菌）、CRE（碳青黴烯耐藥腸桿菌科）及 CRPA（碳青黴烯耐藥綠膿桿菌）。

在感染後症候群方向，TxGNN 的預測具有清晰的因果邏輯：選擇性消化道去污染（SDD）方案以口服 Colistin 為核心成分，透過消滅腸道 MDR 革蘭氏陰性菌定植，切斷細菌移行至下呼吸道的傳播路徑，從而預防 ICU 重症患者的院內感染及其衍生的感染後後遺症（如敗血症後器官損傷、菌血症後功能障礙）。此邏輯鏈在機制上成立，但需注意「感染後症候群」作為疾病標籤與臨床試驗實際研究的「現行感染治療」之間存在語意落差。

在鼻竇炎方向，Colistin 對 MDR P. aeruginosa 的抗生物膜活性，使其在囊腫纖維化（CF）相關慢性鼻竇炎中具有應用基礎。已有病例報告（PMID 19308657）證明靜脈 Colistin 成功治療 MDR 鼻竇炎，多項 CF 研究亦支持鼻腔霧化給藥的藥動學安全性。

---

## 各適應症預測總覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 建議決策 |
|------|--------|-----------|---------|---------|
| 1 | 感染後血管炎 (Postinfectious Vasculitis) | 99.91% | L5 | ❌ Hold |
| 2 | 後細菌性疾患 (Post-bacterial Disorder) | 99.91% | L3 | 🔬 Research Question |
| **3** | **感染後症候群 (Post-infectious Syndrome)** | **99.91%** | **L2** | **✅ Proceed with Guardrails** |
| 4 | 查加斯心肌病 (Chagas Cardiomyopathy) | 99.91% | L5 | ❌ Hold（強烈不合理） |
| 5 | 感染相關溶血性尿毒症候群 (HUS) | 99.90% | L5 | ❌ Hold（有主動傷害風險） |
| 6 | 感染性尿道狹窄 (Infective Urethral Stricture) | 99.90% | L5 | ❌ Hold |
| 7 | 副傷寒 (Paratyphoid Fever) | 99.51% | L4 | 🔬 Research Question |
| **8** | **鼻竇炎 (Sinusitis)** | **99.25%** | **L3** | **✅ Proceed with Guardrails** |
| 9 | 慢性鼻竇炎 (Chronic Rhinosinusitis) | 99.22% | L3 | 🔬 Research Question |
| 10 | 慢性篩竇炎 (Chronic Ethmoidal Sinusitis) | 99.20% | L4 | ❌ Hold |

---

## 臨床試驗證據（感染後症候群）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02389036](https://clinicaltrials.gov/study/NCT02389036) | Phase 3 | 完成 | 20,010 | SDD 方案（含口服 Colistin）預防 ICU 院內感染，交叉群集 RCT，迄今最大規模直接支持證據 |
| [NCT07004049](https://clinicaltrials.gov/study/NCT07004049) | Phase 4 | 招募中 | 600 | TREAT-GNB 平台試驗，自適應設計評估 MDR 革蘭氏陰性菌菌血症及下呼吸道感染多種治療策略 |
| [NCT06051513](https://clinicaltrials.gov/study/NCT06051513) | N/A | 招募中 | 404 | Colistimethate Sodium 注射液 vs 對照組治療 CRE 感染，直接針對 Colistin 的中國多中心 RCT |
| [NCT04882085](https://clinicaltrials.gov/study/NCT04882085) | Phase 4 | 完成 | 60 | CAZ-AVI vs 最佳可用治療（含 Colistin）治療碳青黴烯耐藥革蘭氏陰性菌感染，開放標籤多中心 RCT |
| [NCT01970371](https://clinicaltrials.gov/study/NCT01970371) | Phase 3 | 完成 | 69 | Plazomicin vs Colistin 治療 CRE 感染（BSI、HABP、VABP），直接評估 Colistin 療效的 Phase 3 RCT |
| [NCT03894046](https://clinicaltrials.gov/study/NCT03894046) | Phase 3 | 完成 | 207 | 舒巴坦-ETX2514 vs 含 Colistin 對照組治療鮑氏不動桿菌感染，Part B 含 Colistin 失敗族群 |
| [NCT01023087](https://clinicaltrials.gov/study/NCT01023087) | N/A | 完成 | 70 | Colistin（Polymyxin E）治療相關腎損傷發生率前瞻性研究，重要安全性基礎資料 |

---

## 臨床試驗證據（後細菌性疾患）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01631968](https://clinicaltrials.gov/study/NCT01631968) | N/A | 完成 | 2,948 | Colistin+紅黴素骨水泥 vs 標準骨水泥預防人工膝關節感染，直接使用 Colistin 預防術後細菌感染後遺症的最大規模 RCT |
| [NCT06488794](https://clinicaltrials.gov/study/NCT06488794) | Phase 2/3 | 尚未招募 | 400 | 霧化 Colistimethate Sodium 預防兒童呼吸器相關肺炎（VAP），設計嚴謹的安慰劑對照試驗 |
| [NCT01732250](https://clinicaltrials.gov/study/NCT01732250) | Phase 4 | 完成 | 406 | Colistin 單用 vs Colistin + Meropenem 治療 MDR 細菌感染，多中心開放標籤 RCT |
| [NCT06827756](https://clinicaltrials.gov/study/NCT06827756) | Phase 4 | 完成 | 90 | Norfloxacin vs Nitazoxanide vs Colistin 作為肝硬化腹水患者自發性細菌性腹膜炎（SBP）二次預防，直接比較三藥預防療效 |
| [NCT06440304](https://clinicaltrials.gov/study/NCT06440304) | Phase 4 | 招募中 | 108 | ICU 碳青黴烯耐藥鮑氏不動桿菌（CRAB）感染治療策略，Colistin 為主要比較臂之一 |

---

## 文獻證據（鼻竇炎）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19308657](https://pubmed.ncbi.nlm.nih.gov/19308657/) | 2009 | Case Report | Int J Hematol | AML 患者因 MBL 型 MDR P. aeruginosa 引起上顎竇炎及眶周蜂窩組織炎，靜脈 Colistin 成功治療，為直接使用案例 |
| [18575008](https://pubmed.ncbi.nlm.nih.gov/18575008/) | 2008 | Pilot RCT | Rhinology | 霧化 bacitracin/colimycin（Colistin）治療難治型慢性鼻竇炎（S. aureus），雙盲隨機交叉先導試驗 |
| [34296343](https://pubmed.ncbi.nlm.nih.gov/34296343/) | 2022 | Review | Eur Arch Otorhinolaryngol | CF 相關慢性鼻竇炎治療選項完整回顧，含 Colistin 局部用藥討論 |
| [25016384](https://pubmed.ncbi.nlm.nih.gov/25016384/) | 2014 | PK Study | J Antimicrob Chemother | CF 患者鼻腔霧化 Colistin 全身吸收量評估，建立鼻腔給藥安全性依據 |
| [27879058](https://pubmed.ncbi.nlm.nih.gov/27879058/) | 2017 | Cohort | Int Forum Allergy Rhinol | 原發性纖毛運動不良症患者鼻竇手術後改善肺部感染與肺功能，支持切斷 P. aeruginosa 鼻竇→肺傳播路徑的概念 |
| [2778857](https://pubmed.ncbi.nlm.nih.gov/2778857/) | 1989 | Cohort | Kaohsiung J Med Sci | 台灣 430 名慢性鼻竇炎患者 10 年菌相及抗生素敏感性分析，提供在地細菌生態背景 |

---

## 文獻證據（慢性鼻竇炎）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34296343](https://pubmed.ncbi.nlm.nih.gov/34296343/) | 2022 | Review | Eur Arch Otorhinolaryngol | CF 相關慢性鼻竇炎治療選項完整回顧，CF-CRS 幾乎 100% 盛行率，Colistin 局部應用具潛力 |
| [18575008](https://pubmed.ncbi.nlm.nih.gov/18575008/) | 2008 | Pilot Study | Rhinology | 霧化 Colistin 治療難治型慢性鼻竇炎雙盲交叉先導試驗 |
| [23406585](https://pubmed.ncbi.nlm.nih.gov/23406585/) | 2013 | Cohort | Am J Rhinol Allergy | CF 患者鼻竇手術加術後抗生素治療清除病原菌，驗證局部細菌根除可行性 |
| [27879058](https://pubmed.ncbi.nlm.nih.gov/27879058/) | 2017 | Cohort | Int Forum Allergy Rhinol | PCD 患者鼻竇手術改善肺部感染，鼻竇治療的系統性獲益佐證 |
| [41599109](https://pubmed.ncbi.nlm.nih.gov/41599109/) | 2025 | In Vitro | Pharmaceutics | Ceragenin 聯合 Ivacaftor 抑制鼻竇炎相關細菌生物膜（對照 Colistin 活性的基礎研究） |

---

## 香港上市資訊

Colistin 在香港**目前無已登記的藥品許可證**（共 0 張）。如需臨床使用，須透過特殊進口申請或醫院自購途徑取得，建議向香港衛生署藥品辦公室確認申請流程及儲備機制。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **重要提醒**：NCT01023087（前瞻性，70 名）直接研究 Colistin 治療相關腎損傷發生率，**腎毒性**為已知主要風險；另有神經毒性（神經肌肉阻斷）疑慮。任何推進計畫均需包含嚴密的腎功能監測方案。

---

## 不建議推進的適應症說明

| 適應症 | 停推原因 |
|--------|---------|
| 查加斯心肌病 | Colistin 對原蟲（克氏錐蟲）無任何已知活性，TxGNN 高分屬圖譜拓撲假陽性 |
| 感染相關溶血性尿毒症候群（HUS） | STEC-HUS 使用抗生素可能促進 Shiga 毒素大量釋放，加重病情，現行臨床指引建議避免 |

---

## 結論與下一步

**主要決策：Proceed with Guardrails（感染後症候群 / ICU 院內感染預防）**

**理由：**
SDD 方案中的口服 Colistin 已有 Phase 3 大型 RCT（NCT02389036，20,010 名 ICU 患者）支持，在預防院內感染及感染後後遺症方面機制邏輯清晰，且多項已完成的 Phase 3/4 試驗佐證 Colistin 在 MDR 感染治療鏈中的核心地位。

**次要決策：Proceed with Guardrails（鼻竇炎，MDR 革蘭氏陰性菌相關）**

適用範圍聚焦於 CF 或免疫缺陷患者中因 MDR P. aeruginosa 引起的難治型鼻竇炎，有直接成功案例報告及鼻腔霧化給藥的 PK 安全性佐證。

**若要推進需要：**
- 補充 Colistin 完整作用機轉資料（查詢 DrugBank API，DB00803）
- 確認香港特殊進口申請管道及藥事監管要求
- 制定腎功能監測計畫（建議每 2–3 天監測血清肌酐 SCr 及尿量）
- 「感染後症候群」需更精確的患者族群定義，建議聚焦 **ICU-SDD 預防情境**
- 鼻竇炎適應症建議設計 **CF 患者前瞻性觀察研究**，明訂霧化給藥的療效與安全終點
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

