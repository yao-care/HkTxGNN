---
layout: default
title: Loxapine
parent: 高證據等級 (L1-L2)
nav_order: 466
evidence_level: L2
indication_count: 5
---

# Loxapine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Loxapine（DB00408）：TxGNN 預測用於雙相躁症

## 一句話總結

Loxapine 是傳統抗精神病藥物成分，目前尚未在香港取得藥品許可證。
TxGNN 模型預測它可能對**雙相躁症 (Manic Bipolar Affective Disorder)** 有效，
目前有 **0 個臨床試驗登記**和 **20 篇文獻**支持這個方向，其中包含 Phase III RCT 及系統性回顧統合分析。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（無結構化原適應症紀錄；文獻顯示其口服劑型傳統用於思覺失調症，吸入劑型已於美國/歐盟核准用於思覺失調症或雙相症之「急性激躁」） |
| 預測新適應症 | 雙相躁症 (Manic Bipolar Affective Disorder) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 完整的作用機轉資料（MOA 欄位為空）。根據文獻證據，Loxapine 為典型/非典型抗精神病藥，具 D2 多巴胺受體及 5-HT2A 血清素受體拮抗作用，此機轉可抑制精神運動性激躁與精神病症狀。

其吸入劑型（Adasuve）已於美國/歐盟核准用於思覺失調症及雙相情感障礙相關「急性激躁」的適應症，多篇文獻（含兩個 Phase III RCT：NCT00628589、NCT00721955）支持此用途的療效與安全性。

**需特別注意**：現有證據支持的是「雙相患者急性激躁之症狀控制」，並非「躁症/雙相情感障礙本身之核心治療」，兩者適應症範圍不可等同，推進時需明確界定目標族群與治療目的。

## 臨床試驗證據

目前無相關臨床試驗登記（ClinicalTrials.gov 與 ICTRP 皆查無結果；文獻中提及的 NCT00628589、NCT00721955、PLACID 試驗未在本 Evidence Pack 的試驗資料庫中單獨收錄，僅見於文獻引用）。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29724638](https://pubmed.ncbi.nlm.nih.gov/29724638/) | 2018 | RCT (PLACID study) | European Neuropsychopharmacology | 吸入 loxapine 與肌注 aripiprazole 治療思覺失調症/雙相 I 型急性激躁療效與安全性比較 |
| [22226343](https://pubmed.ncbi.nlm.nih.gov/22226343/) | 2012 | Review（2 個 Phase III RCT 二次分析） | International Journal of Clinical Practice | 以效果量重新檢視吸入 loxapine 治療激躁的療效 |
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | Systematic Review & Meta-analysis | Human Psychopharmacology | 系統性回顧思覺失調症/雙相症急性激躁之藥物治療 |
| [29163985](https://pubmed.ncbi.nlm.nih.gov/29163985/) | 2017 | Phase III RCT 事後分析 | BJPsych Open | 344 名思覺失調症及 314 名雙相 I 型患者的 PANSS-EC 反應分析（NCT00628589, NCT00721955） |
| [31496709](https://pubmed.ncbi.nlm.nih.gov/31496709/) | 2019 | Review | Neuropsychiatric Disease and Treatment | 吸入 loxapine 用於思覺失調症/雙相 I 型急性激躁之安全性、療效與患者接受度 |
| [27121764](https://pubmed.ncbi.nlm.nih.gov/27121764/) | 2016 | Review | Current Medical Research and Opinion | 吸入 loxapine 緊急治療思覺失調症或雙相症急性激躁 |
| [23740380](https://pubmed.ncbi.nlm.nih.gov/23740380/) | 2013 | Review | CNS Drugs | Loxapine 吸入粉劑（Adasuve）用於雙相症或思覺失調症急性激躁之療效回顧 |
| [28208695](https://pubmed.ncbi.nlm.nih.gov/28208695/) | 2017 | Clinical Review | International Journal of Molecular Sciences | 吸入 loxapine 治療精神疾病急性激躁之臨床回顧 |
| [35913401](https://pubmed.ncbi.nlm.nih.gov/35913401/) | 2022 | Review | Expert Review of Neurotherapeutics | 50 年 loxapine 用於思覺失調症等急性行為障礙非強制性鎮靜之經驗回顧 |
| [30721526](https://pubmed.ncbi.nlm.nih.gov/30721526/) | 2019 | Expert Review | Drugs in R&D | 吸入 loxapine 管理雙相症/思覺失調症急性激躁之專家評論 |

## 香港上市資訊

目前尚未在香港取得藥品許可證，無許可證資料可提供。

## 安全性考量

安全性資訊請參考原廠仿單（TFDA 仿單警語/禁忌症、藥物交互作用資料目前均缺失）。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
文獻證據包含 2 個 Phase III RCT（NCT00628589、NCT00721955）及後續統合分析，支持吸入劑型用於雙相症急性激躁具療效與安全性；但此為「症狀控制」而非「疾病核心治療」，且香港尚未上市，MOA 與安全性資料均缺失，須以防護機制推進。

**若要推進需要：**
- TFDA/香港衛生署仿單警語與禁忌症資料（DG001，Blocking）
- DrugBank 完整作用機轉資料（DG002，High）
- 釐清「雙相躁症核心治療」與「雙相症急性激躁症狀控制」之適應症範圍差異，避免適應症誤用
- 評估是否申請香港藥品許可證及所需劑型（吸入 vs 口服）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

