---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 741
evidence_level: L5
indication_count: 5
---

# Ranibizumab
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

# Ranibizumab：從（原適應症資料未登載）到重度非增殖性糖尿病視網膜病變

## 一句話總結

Ranibizumab 是抗 VEGF 的 Fab 抗體片段，在香港以 Lucentis 眼內注射劑型上市，但資料中未登載原核准適應症。
TxGNN 模型預測它可能對**重度非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)** 有效，
目前有 **5 個相關臨床試驗**和 **20 篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未登載（香港許可證資料中無適應症文字） |
| 預測新適應症 | 重度非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1（依 Evidence Pack 評級，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Proceed with Guardrails |

> **等級說明：** 直接針對本適應症、以 ranibizumab 為藥物且已發表主要結果的 Phase 3 RCT 是 Pavilion（PMID 40048178）。其餘 Phase 3 多為間接證據（針對 DME，或所用抗 VEGF 藥物未確認），因此 L1 屬偏寬鬆的評級。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知藥理，ranibizumab 屬於抗 VEGF 的 Fab 抗體片段。VEGF 會促進糖尿病視網膜病變中的血管滲漏、視網膜無灌流與新生血管，患眼的玻璃體與血清 VEGF 濃度也會升高。

原適應症資料雖然缺漏，但它是眼內注射的抗 VEGF 藥物，用於糖尿病視網膜病變在機轉上直接且合理。RIDE/RISE 試驗的事後分析顯示，ranibizumab 治療可使糖尿病視網膜病變嚴重度出現改善。此預測主要依據同類藥物的已知藥理，而非該藥自身的 MOA 資料。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Phase 3 | 進行中（不再招募） | 174 | 以 ranibizumab 埋入式給藥系統 (PDS) 治療無中心型 DME 的糖尿病視網膜病變，與對照組比較療效與安全性 |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Phase 3 | 未知 | 118 | 玻璃體內注射 ranibizumab 與假注射比較，用於預防高風險糖尿病視網膜病變（標題未明確指出藥物） |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Phase 3 | 完成 | 399 | 玻璃體內抗 VEGF 預防高風險眼睛出現威脅視力的糖尿病視網膜病變（所用藥物未必是 ranibizumab，為間接證據） |
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Phase 3 | 完成 | 691 | Ranibizumab 或 triamcinolone 合併雷射治療 DME。藥物正確，但主要疾病是 DME 而非重度 NPDR |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Phase 4 | 完成 | 25 | 單中心、6 個月的 ranibizumab 先導研究，用於合併 NPDR 的黃斑部水腫，觀察微血管瘤變化與無灌流區 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | Pavilion 試驗：ranibizumab 埋入式給藥系統 vs 觀察，用於無黃斑部水腫的 NPDR，目標是減少注射頻率 |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | 系統性回顧 | Health Technol Assess | 比較抗 VEGF 與雷射光凝治療糖尿病視網膜病變 |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | 系統性回顧與經濟分析 | Health Technol Assess | 同一研究團隊的延伸分析，加入抗 VEGF 對比雷射的經濟評估 |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opin Biol Ther | 回顧 ranibizumab 治療糖尿病視網膜病變（含 DME）的證據 |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | RCT 事後分析（統合） | Ophthalmol Retina | 分析基線 DR 嚴重度與 ranibizumab 治療後 DME 緩解時間的關係 |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | RCT 事後分析 | Clin Ophthalmol | RIDE/RISE 試驗中，ranibizumab 使早期 DR 改善的預測因子 |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | RCT 事後分析 | BMJ Open Ophthalmol | RIDE/RISE 延伸期：減少給藥頻率對 DR 嚴重度量表分數的影響 |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | RCT 次要分析 | JAMA Ophthalmology | 比較 aflibercept、bevacizumab 與 ranibizumab 治療 2 年後 DR 的變化 |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | RCT 長期追蹤 | Retina | DRCR.net Protocol I 5 年報告：ranibizumab 治療 DME 期間 DR 嚴重度的變化 |
| [37278412](https://pubmed.ncbi.nlm.nih.gov/37278412/) | 2023 | 模擬模型研究 | BMJ Open Ophthalmol | 模擬主動以抗 VEGF 治療重度 NPDR，對比等到進展為 PDR 才治療的長期結果 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-65166 | LUCENTIS SOLUTION FOR INJECTION 2.3MG/0.23ML (VIAL+FILTER NEEDLE PACK) | 香港諾華藥品 (Novartis Pharmaceuticals (HK) Limited) |
| HK-68384 | LUCENTIS SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 10MG/ML | 香港諾華藥品 (Novartis Pharmaceuticals (HK) Limited) |
| HK-63860 | LUCENTIS SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 10MG/ML | 香港諾華藥品 (Novartis Pharmaceuticals (HK) Limited) |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 機轉直接合理，且已有針對 NPDR 的 Phase 3 RCT（Pavilion）發表，加上 RIDE/RISE 的 DR 嚴重度改善數據支持。
- 香港已有 3 張 Lucentis 許可證，但資料中未登載核准適應症，無法確認是否已涵蓋糖尿病視網膜病變。

**若要推進需要：**
- 取得香港衞生署的仿單，確認本地核准適應症、警語與禁忌症。
- 確認 NCT03452657 與 NCT02634333 實際使用的抗 VEGF 藥物。
- 補充 DrugBank 的作用機轉資料。
- 用藥時須留意眼內注射相關風險，如眼內炎和眼壓升高。抗 VEGF 的療效需要持續治療與追蹤。

**其他預測適應症（皆不建議推進）：**
- 第 2 名「第二型糖尿病相關白內障」為研究問題 (Research Question)，屬 L4。
- 第 3 至 5 名（未成熟白內障、顱縫早閉合併白內障、成熟白內障）皆為 Hold。
- 抗 VEGF 對水晶體混濁沒有已知療效，這些高分更可能源自知識圖譜中糖尿病眼病的鄰近關係。相關文獻只涉及白內障手術合併注射，用於治療已有的視網膜病變。

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

