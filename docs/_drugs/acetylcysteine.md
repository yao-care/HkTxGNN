---
layout: default
title: Acetylcysteine
parent: 高證據等級 (L1-L2)
nav_order: 20
evidence_level: L2
indication_count: 10
monitor_inn: "ACETYLCYSTEINE"
predicted_indications: ["thrombotic disease", "closed-angle glaucoma", "nasal cavity disease", "dry eye syndrome", "pharyngitis", "acute laryngopharyngitis", "tracheal disease", "transient ischemic attack (disease)", "laryngotracheitis", "angle-closure glaucoma"]
last_modified_at: 2026-10-28
description: "Acetylcysteine：預測新適應症為血栓性疾病 (thrombotic disease)（證據等級 L2）。原適應症：本地許可證資料未記載適應症"
---

# Acetylcysteine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Acetylcysteine：黏液溶解劑／抗氧化硫醇 → 血栓性疾病 (thrombotic disease)
{: .text-alpha }

## 一句話總結

Acetylcysteine 是一種含硫醇基的黏液溶解劑，具抗氧化活性。
TxGNN 模型預測它可能對**血栓性疾病 (thrombotic disease)** 有效，
目前有 **7 個臨床試驗**和 **20 篇文獻**列於此預測之下，但其中直接針對血栓性微血管病變（TA-TMA、TTP）的證據最為相關，多數結果尚未公開。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 血栓性疾病 (thrombotic disease) |
| TxGNN 預測分數 | 0.9996 |
| 證據等級 | L2 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。不過依據已整理的研究資料，Acetylcysteine 是一種硫醇化合物，可還原超大型 von Willebrand 因子 (VWF) 多聚體中的雙硫鍵，降低 VWF 與血小板的結合，進而減少微血栓形成。這一點獲得小鼠與狒狒 TTP 模型的前臨床研究支持。

此外，它具有抗氧化作用，可能減輕移植相關血栓性微血管病變 (TA-TMA) 中的內皮細胞損傷。

需要注意：訊號最強的是 TMA／TTP 類型的疾病，並非所有血栓性疾病。對於一般靜脈或動脈血栓，目前沒有直接證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | 已完成 | 170 | NAC 用於移植相關血栓性微血管病變 (TA-TMA)，安全性與療效評估；提供的資料未載明結果 |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | 進行中（不再招募） | 44 | 單臂試驗，NAC 治療 TA-TMA；尚無結果 |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | 已完成 | 40 | RENACTIF：隨機雙盲交叉試驗，NAC 用於降低腎功能不全患者的血栓表型 |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Early Phase 1 | 已完成 | 3 | 疑似 TTP 的先導研究，樣本過小，無法支持療效 |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | 未知 | 44 | 高劑量 dexamethasone 併用 NAC 治療新診斷免疫性血小板低下症 (ITP)，與血栓僅間接相關 |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Early Phase 1 | 已完成 | 15 | Atorvastatin 併用 NAC 於 ITP 的血小板數探索，間接相關 |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | 未知 | 200 | Atorvastatin、NAC 與 danazol 併用於類固醇抗藥或復發 ITP，併用設計干擾 NAC 效果判讀 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | 系統性回顧 | Journal of Clinical Medicine | NAC 治療 TTP 的系統性回顧與批判性評讀 |
| [42338865](https://pubmed.ncbi.nlm.nih.gov/42338865/) | 2026 | 系統性回顧 | Cureus | NAC 作為 TTP 輔助治療的系統性回顧 |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | 回溯性世代研究 | Annals of Hematology | 探討 NAC 與後天性 TTP 病患院內死亡率的關聯 |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | 前臨床（小鼠／狒狒） | Blood | NAC 在 TTP 動物模型中的作用 |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | 回顧 | Expert Review of Hematology | 整理 TTP 的再利用藥物與新藥，包括 NAC |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Review | Blood | TTP 的病理機轉與治療概述 |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | Journal of Clinical Medicine | TTP 的病理生理、診斷與處置 |
| [36410267](https://pubmed.ncbi.nlm.nih.gov/36410267/) | 2022 | Review | Journal of Infection and Public Health | NAC 於 COVID-19（含促血栓狀態）的證據現況 |

## 香港上市資訊

香港共有至少 20 張有效許可證（資料可能不完整），均為單一成分製劑。以下列出 5 張主要許可證，其核准適應症文字在本次資料中均未記載。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63073 | ADVANCE MUCOLYTIC POWDER 200MG/SACHET | 未記載 | 未記載 |
| HK-52560 | ACTEIN GRANULES 100MG | 未記載 | 未記載 |
| HK-65198 | AZEIN CAPSULES 200MG | 未記載 | 未記載 |
| HK-54293 | MICOSTEINE POWDER FOR ORAL SUSP 200MG/SACHET | 未記載 | 未記載 |
| HK-42254 | FLUIMUCIL INJ 300MG/3ML | 未記載 | 未記載 |

## 安全性考量

- **藥物交互作用**：資料庫共記錄 100 筆交互作用，等級多為「未知」。較具代表性者包括：Insulin human（吸入型，中度）、Activated charcoal（輕微）；另有 pantoprazole、omeprazole、metformin、morphine、doxycycline 等列為未知等級。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 個完成的 Phase 3 試驗（NCT03252925）與 1 個進行中的 Phase 2/3 試驗直接針對 TA-TMA，另有 TTP 的系統性回顧與動物模型支持，機轉合理。但已提供的資料未載明試驗結果，療效尚未確認，因此證據等級維持 L2。
- 證據集中在 TMA／TTP，不能外推到一般血栓性疾病。

**若要推進需要：**
- 取得 NCT03252925 與 NCT07279610 的實際結果，確認 TA-TMA 的療效與安全性
- 明確界定目標族群（TA-TMA 或 TTP），而非泛指血栓性疾病
- 補齊原廠仿單的警語、禁忌症與適應症資料，並確認靜脈注射劑型的用法與劑量
- 補充詳細作用機轉資料
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

