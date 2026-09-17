---
layout: default
title: Progesterone
parent: 中證據等級 (L3-L4)
nav_order: 619
evidence_level: L3
indication_count: 5
---

# Progesterone
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Progesterone：香港未上市藥物之續發性閉經 (Amenorrhea) 新適應症評估

## 一句話總結

Progesterone（DrugBank DB00396）目前在香港**未上市**，且原適應症與作用機轉資料均缺失。
TxGNN 模型預測它可能對**續發性閉經 (Amenorrhea)** 有效，目前有 **50 個臨床試驗**和 **18 篇文獻**與此關聯相關，
但多數試驗介入藥物並非 progesterone 本身，證據等級僅 **L3**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（未上市，無許可證記錄） |
| 預測新適應症 | 續發性閉經 (Amenorrhea) |
| TxGNN 預測分數 | 99.9996%（rank 24） |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 收錄的詳細作用機轉資料。根據已知藥理學知識，Progesterone 是下視丘－腦垂體－卵巢軸 (HPO axis) 調控月經週期的內源性關鍵黃體素，黃體期黃體素缺乏或撤退，正是續發性閉經的核心病生理機轉之一。

臨床上，口服微粒化 progesterone 進行的「progestin withdrawal test（黃體素撤退試驗）」是評估續發性閉經、判斷體內雌激素狀態是否足夠的標準診斷/治療方法。換句話說，這個 TxGNN 預測某種程度上是 progesterone 既有臨床用途的延伸，而非全新的「老藥新用」機會——evidence pack 的 `repurposing_rationale` 也明確標註了這一點。

需要注意的是：檢索到的 50 個臨床試驗中，多數（grade C 或 pending）介入藥物並非 progesterone 本身（例如 estradiol、romosozumab、goserelin、relugolix 等），僅 1 個試驗（NCT01185782, Phase 3）被評為 grade B 相關；文獻證據也以機轉綜述為主，缺乏直接證實 progesterone 治療續發性閉經療效的高品質 RCT。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01185782](https://clinicaltrials.gov/study/NCT01185782) | Phase 3 | 完成 | 300 | 黃體激素類製劑 vs 純化腦垂體促性腺激素治療閉經 I/無排卵週期；grade B，族群直接相關 |
| [NCT03309176](https://clinicaltrials.gov/study/NCT03309176) | Phase 4 | 完成 | 42 | 探討促排卵前是否需 progesterone 誘導之子宮內膜撤退性出血 |
| [NCT02744131](https://clinicaltrials.gov/study/NCT02744131) | N/A | 狀態未知 | 100 | OCP vs Metformin 治療 PCOS，可加用 progesterone 誘導閉經患者撤退性出血 |
| [NCT05312190](https://clinicaltrials.gov/study/NCT05312190) | N/A | 狀態未知 | 330 | 真氣補血口服液 vs Progesterone 膠囊治療月經失調 |
| [NCT03309709](https://clinicaltrials.gov/study/NCT03309709) | Phase 3 | 狀態未知 | 90 | 皮下注射 progesterone 治療停經前婦女子宮內膜息肉 |
| [NCT01942668](https://clinicaltrials.gov/study/NCT01942668) | Phase 3 | 完成 | 1845 | Estradiol + progesterone 併用治療停經後血管舒縮症狀，安全性資料量大 |
| [NCT01674426](https://clinicaltrials.gov/study/NCT01674426) | N/A | 完成 | 17 | 功能性下視丘性閉經病生理機轉研究；grade C，非 progesterone 介入 |
| [NCT06533865](https://clinicaltrials.gov/study/NCT06533865) | Phase 3 | 招募中 | 114 | Romosozumab 輔助雌激素替代治療功能性下視丘性閉經；grade C |
| [NCT00088153](https://clinicaltrials.gov/study/NCT00088153) | Phase 2/3 | 完成 | 110 | 厭食症骨密度與雌激素研究；grade C，族群相關但非 progesterone |
| [NCT03740204](https://clinicaltrials.gov/study/NCT03740204) | Phase 2 | 招募中 | 120 | 經皮雌二醇 + 週期性 progesterone 用於飲食障礙相關低雌激素青少年 |

> 註：evidence pack 共收錄 50 個相關臨床試驗，此處列出前 10 個最相關者；多數其餘試驗經初步標註為 grade C（介入藥物非 progesterone）或尚待分級（pending）。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38652231](https://pubmed.ncbi.nlm.nih.gov/38652231/) | 2024 | Review | Reviews in Endocrine & Metabolic Disorders | 口服微粒化 progesterone 於內分泌科的診斷與治療應用綜述 |
| [35525789](https://pubmed.ncbi.nlm.nih.gov/35525789/) | 2022 | Review | Curr Probl Pediatr Adolesc Health Care | 青少年及年輕女性閉經的病因與治療管理 |
| [8629565](https://pubmed.ncbi.nlm.nih.gov/8629565/) | 1996 | Review | American Family Physician | 閉經評估標準流程，含黃體素撤退試驗 |
| [22283375](https://pubmed.ncbi.nlm.nih.gov/22283375/) | 2012 | pending | Gynecological Endocrinology | 排卵之神經內分泌調控，HPO 軸失調導致無排卵/閉經 |
| [33716979](https://pubmed.ncbi.nlm.nih.gov/33716979/) | 2021 | Review | Frontiers in Endocrinology | 早發性卵巢功能不全 (POI) 病因、症狀與治療選項現況 |
| [28257537](https://pubmed.ncbi.nlm.nih.gov/28257537/) | 2017 | pending | Southern Medical Journal | 原發性卵巢功能不全現況概念，續發性閉經與激素替代治療 |
| [35463307](https://pubmed.ncbi.nlm.nih.gov/35463307/) | 2022 | pending | Frontiers in Oncology | 化療誘發閉經 (CIA) 之危險因子與預後意義統合分析 |
| [32233689](https://pubmed.ncbi.nlm.nih.gov/32233689/) | 2020 | pending | Climacteric | 停經後陰道出血臨床處置，閉經定義與雌/黃體素關聯 |
| [34569009](https://pubmed.ncbi.nlm.nih.gov/34569009/) | 2022 | pending | Clinical Pharmacokinetics | 選擇性黃體素受體調節劑 Vilaprisan 藥動學綜述 |
| [6232474](https://pubmed.ncbi.nlm.nih.gov/6232474/) | 1984 | pending | Obstetrics and Gynecology Annual | 多囊性卵巢疾病，閉經常見病因之一 |

> 註：evidence pack 共收錄 18 篇相關文獻，此處列出 10 篇最相關者。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠ 補充說明：evidence pack 標記 DG001（TFDA/香港仿單警語與禁忌，**Blocking** 等級）為資料缺口，目前**無法完成 S1 安全性初評**，須先取得官方仿單 PDF 解析後方可補齊。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- TxGNN 預測分數極高（99.9996%）且機轉合理，符合 progesterone 既有的黃體素撤退試驗臨床邏輯，但這代表的更可能是既有用途延伸而非全新老藥新用機會。
- 50 個臨床試驗中僅 1 個（NCT01185782）被評為 grade B 直接相關，其餘多數介入藥物非 progesterone 本身；文獻證據以機轉綜述為主，缺乏高品質 RCT 直接證實療效，故證據等級僅達 L3。
- 因藥物在香港未上市、且缺乏 TFDA/香港仿單警語資料（DG001, Blocking），**無法完成 S1 安全性初評**，須謹慎進行後續步驟。

**若要推進需要：**
- 補齊香港/TFDA 仿單警語與禁忌症資料（DG001，Blocking，解除 S1 安全性初評阻礙）
- 補齊 DrugBank 詳細作用機轉資料（DG002，High）
- 逐一複核 50 個臨床試驗中標記為 pending 的項目，確認真正以 progesterone 治療續發性閉經為介入設計的試驗數量
- 釐清此適應症是否應歸類為「既有用途延伸」而非「老藥新用候選」，據以調整後續資源投入優先序
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

