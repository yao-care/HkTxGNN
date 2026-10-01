---
layout: default
title: Acetylcysteine
parent: 高證據等級 (L1-L2)
nav_order: 20
evidence_level: L2
indication_count: 10
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Acetylcysteine：從黏液溶解劑到血栓性疾病

## 一句話總結

Acetylcysteine（乙醯半胱胺酸，NAC）在香港以黏液溶解劑類產品上市。
TxGNN 模型預測它可能對**血栓性疾病 (Thrombotic disease)** 有效，目前有 **8 個臨床試驗**和 **20 篇文獻**支持這個方向。
證據集中在移植相關血栓性微血管病變 (TA-TMA) 與血栓性血小板減少性紫斑症 (TTP)，並非泛指所有血栓。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 血栓性疾病 (Thrombotic disease) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold（待補安全性資料後再評估是否轉為 Proceed with Guardrails） |

香港許可證資料未提供核准適應症文字，因此原適應症欄位省略。

## 為什麼這個預測合理？

DrugBank 的作用機轉資料目前缺漏。根據已有的預測依據，NAC 能還原雙硫鍵，縮小血管性血友病因子 (VWF) 多聚體的尺寸並降低其活性。它同時具有抗氧化與保護血管內皮的作用。

TTP 與 TA-TMA 的病理核心，都是 VWF 多聚體與血小板在微血管中形成血栓。因此 NAC 在機轉上有合理的切入點。小鼠與狒狒的 TTP 模型也支持這個方向（PMID 28011677）。

「血栓性疾病」是很廣的標籤。目前試驗涵蓋 TMA、TTP、移植後血栓預防，以及腎功能不全的血栓表型，尚無一般靜脈或動脈血栓的直接證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | 完成 | 170 | NAC 用於移植相關 TMA 的安全性與療效；未提供結果數據 |
| [NCT05907486](https://clinicaltrials.gov/study/NCT05907486) | Phase 3 | 未知 | 260 | NAC 預防異體造血幹細胞移植後血栓事件；完成與資料可靠性不明 |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | 進行中（不再招募） | 44 | 單臂多中心，NAC 治療 TA-TMA；結果待公布 |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | 完成 | 40 | 隨機雙盲交叉試驗，NAC 降低腎功能不全的血栓表型；終點為生物標記或表型，非臨床血栓事件 |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Early Phase 1 | 完成 | 3 | 疑似 TTP 併用血漿置換的 NAC 先導試驗；樣本極小，僅支持可行性 |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | 未知 | 44 | 高劑量 dexamethasone 併用 NAC 治療新診斷免疫性血小板低下症 (ITP)；ITP 屬出血性疾病，關聯性弱 |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | 未知 | 200 | atorvastatin、NAC 與 danazol 併用治療難治型 ITP；無法單獨評估 NAC 效果 |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Early Phase 1 | 完成 | 15 | atorvastatin 併用 NAC 提升 ITP 血小板數；非血栓適應症 |

另有 1 個再生不良性貧血移植後造血恢復試驗（NCT06518044），與血栓無關，未列入表格。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35940529](https://pubmed.ncbi.nlm.nih.gov/35940529/) | 2022 | RCT | Transplant Cell Ther | 隨機、安慰劑對照試驗，評估 NAC 預防 TA-TMA |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | 世代研究 | Ann Hematol | 回溯性研究 NAC 與後天性 TTP 住院死亡率的關聯；NAC 用於 TTP 仍有爭議 |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Review | Expert Rev Hematol | 整理 TTP 的老藥新用與新藥，NAC 為其中之一 |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | J Clin Med | TTP 的病理、診斷與處置 |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Review | Blood | TTP 綜述（背景資料） |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | 前臨床 | Blood | NAC 在小鼠與狒狒 TTP 模型的研究 |
| [21266777](https://pubmed.ncbi.nlm.nih.gov/21266777/) | 2011 | 前臨床 | J Clin Invest | NAC 縮小人類血漿與小鼠中 VWF 的尺寸並降低其活性 |
| [28961512](https://pubmed.ncbi.nlm.nih.gov/28961512/) | 2018 | 前臨床 | Redox Biol | NAC 減輕糖尿病模型的全身血小板活化與腦血管血栓 |
| [39737637](https://pubmed.ncbi.nlm.nih.gov/39737637/) | 2025 | 個案報告 | J Pediatr Hematol Oncol | 血漿置換併用 NAC，治療以急性腎衰竭表現的先天性 TTP |
| [30871975](https://pubmed.ncbi.nlm.nih.gov/30871975/) | 2019 | 機轉研究 | Biol Blood Marrow Transplant | TA-TMA 中循環 HO-1 與補體活化的機轉研究 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63073 | ADVANCE MUCOLYTIC POWDER 200MG/SACHET | 未提供 | 未提供 |
| HK-52560 | ACTEIN GRANULES 100MG | 未提供 | 未提供 |
| HK-65198 | AZEIN CAPSULES 200MG | 未提供 | 未提供 |
| HK-54293 | MICOSTEINE POWDER FOR ORAL SUSP 200MG/SACHET | 未提供 | 未提供 |
| HK-42254 | FLUIMUCIL INJ 300MG/3ML | 未提供 | 未提供 |

以上為 20 張許可證中的 5 張。品名沿用原文，資料中沒有中文品名。

## 安全性考量

安全性資訊請參考原廠仿單。香港衛生署仿單的警語與禁忌尚未取得，藥物交互作用查詢也無結果。

## 結論與下一步

**決策：Hold**

**理由：**
在 TA-TMA 與 TTP 上有 Phase 2/3 至 Phase 3 試驗，以及至少 1 篇隨機對照試驗，證據等級為 L2。但香港仿單的安全性資料缺漏，屬於阻擋性缺口，無法進入安全性篩選。現有證據也不足以外推到「血栓性疾病」全體。

**若要推進需要：**
- 取得並解析香港衛生署仿單的警語與禁忌症
- 從 DrugBank 補齊作用機轉資料
- 取得 NCT03252925、NCT07279610、NCT05907486 的結果，確認療效與安全性
- 將適應症收斂為 TA-TMA 或 TTP，而非泛稱血栓性疾病
- 釐清所需給藥途徑（注射或口服）與香港現有劑型是否相容

本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

