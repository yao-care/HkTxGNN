---
layout: default
title: Hyaluronidase
parent: 僅模型預測 (L5)
nav_order: 443
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Hyaluronidase：預測新適應症為糖尿病視網膜病變 (Diabetic Retinopathy)（證據等級 L5）。原適應症：許可證未載明"
monitor_inn: "Hyaluronidase"
predicted_indications: ["esotropia", "amenorrhea (disease)", "severe nonproliferative diabetic retinopathy", "renal tubular acidosis", "dermatitis", "diabetic retinopathy", "acrodermatitis chronica atrophicans", "diabetic cataract", "neonatal dermatomyositis", "non-syndromic esophageal malformation"]
---

# Hyaluronidase
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

# Hyaluronidase：從（原適應症資料缺漏）到糖尿病視網膜病變

## 一句話總結

Hyaluronidase（玻尿酸酶）是一種分解細胞外基質玻尿酸的酵素，在香港已有上市許可證，但許可證上未載明原適應症。
TxGNN 模型預測它可能對**糖尿病視網膜病變 (Diabetic Retinopathy)** 有效，其中最具實質證據的方向是玻璃體內注射。
目前有 **3 個臨床試驗**（含 2 個已完成的 Phase 3）和 **19 篇文獻**支持這個方向，但 Phase 3 試驗的目標是玻璃體出血，並非視網膜病變本身。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明 |
| 預測新適應症 | 糖尿病視網膜病變 (Diabetic Retinopathy) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L1（形式上符合，但適用性為間接，見下文） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold（需先檢視試驗完整結果） |

> 說明：TxGNN 排名第 1 的預測是斜視（esotropia，分數 99.89%），但其唯一文獻是白內障手術局部麻醉後複視的併發症報告，並無治療證據，因此不具推進價值。本報告改以證據最完整的「糖尿病視網膜病變」為主軸，另附其他預測的簡要評估。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Hyaluronidase 是能降解玻尿酸的酵素，用於玻璃體內時可發揮「藥物性玻璃體溶解」作用：使玻璃體凝膠液化、促進玻璃體後脫離，並協助清除玻璃體出血。

糖尿病視網膜病變的病程與玻璃體–視網膜界面密切相關。玻璃體牽引、出血以及血管新生訊號都可能推動疾病進展。前臨床研究（糖尿病大鼠、HIF-1α 路徑、視網膜內皮糖萼）支持這條機轉在生物學上的合理性。

不過需要留意：兩個 Phase 3 試驗針對的是**嚴重玻璃體出血**，而非視網膜病變進程本身，且該開發計畫最終並未取得糖尿病視網膜病變的核准適應症。因此這個預測的適用性屬於間接。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00198497](https://clinicaltrials.gov/study/NCT00198497) | Phase 3 | 完成 | 510 | 羊源 hyaluronidase（Vitrase）玻璃體內注射，評估清除嚴重玻璃體出血的安全性與療效 |
| [NCT00198510](https://clinicaltrials.gov/study/NCT00198510) | Phase 3 | 完成 | 750 | 同上之姊妹試驗，樣本數較大 |
| [NCT00198471](https://clinicaltrials.gov/study/NCT00198471) | Phase 2 | 完成 | 10 | 開放標籤，評估 Vitrase 在中重度非增殖性糖尿病視網膜病變誘發玻璃體後脫離；樣本小、無對照，僅能提供初步可行性 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20939804](https://pubmed.ncbi.nlm.nih.gov/20939804/) | 2011 | Review | Curr Pharm Biotechnol | 回顧藥物性玻璃體溶解；羊源 hyaluronidase 玻璃體內注射可有效清除玻璃體出血 |
| [17713597](https://pubmed.ncbi.nlm.nih.gov/17713597/) | 2007 | Review | Exp Diabetes Res | 糖尿病視網膜病變藥物治療現況與未來 |
| [19644368](https://pubmed.ncbi.nlm.nih.gov/19644368/) | 2009 | Review | Curr Opin Ophthalmol | 糖尿病視網膜病變治療典範的轉變 |
| [41789111](https://pubmed.ncbi.nlm.nih.gov/41789111/) | 2026 | 基礎/轉譯研究 | Front Immunol | 玻尿酸代謝失調驅動增殖性糖尿病視網膜病變的發炎與血管新生 |
| [23847321](https://pubmed.ncbi.nlm.nih.gov/23847321/) | 2013 | 動物研究 | Invest Ophthalmol Vis Sci | 酵素誘導玻璃體溶解可經 HIF-1α 路徑減緩病變進展 |
| [19050667](https://pubmed.ncbi.nlm.nih.gov/19050667/) | 2009 | 動物研究 | Retina | 糖尿病大鼠中 plasmin 與 hyaluronidase 誘導玻璃體後脫離的可行性 |
| [30445048](https://pubmed.ncbi.nlm.nih.gov/30445048/) | 2019 | 動物研究 | Exp Eye Res | 糖尿病與 hyaluronidase 對小鼠視網膜內皮糖萼的影響 |
| [12757408](https://pubmed.ncbi.nlm.nih.gov/12757408/) | 2003 | 藥物概述 | Drugs R D | Vitrase 的眼科注射劑型開發，目標為玻璃體出血與糖尿病視網膜病變 |
| [34293791](https://pubmed.ncbi.nlm.nih.gov/34293791/) | 2022 | 其他 | Ophthalmic Plast Reconstr Surg | 球後注射的 hyaluronidase 是否能到達玻璃體腔 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-35245 | HYALASE FOR INJ 1500IU | 未載明 | 未載明（製造商：LUEN CHEONG HONG LTD） |

---

## 安全性考量

- **藥物交互作用**：共查得 63 筆，目前列出的主要為輕微（Minor）等級，包括皮質類固醇（Hydrocortisone、Dexamethasone、Prednisolone 等）、抗組織胺（Chlorpheniramine、Cetirizine、Loratadine 等）、Lidocaine、Acetylsalicylic acid 及雌激素類（Estradiol、Ethinylestradiol 等）。
- **過敏風險**：文獻指出 hyaluronidase 注射可能引起過敏反應，且常被誤診。
- **眼內使用的需關注項目**：發炎與眼壓變化，需在審閱試驗完整結果時確認。

其餘警語與禁忌症資料不足，請參考原廠仿單。

---

## 其他預測適應症簡評

| 預測適應症 | TxGNN 分數 | 證據等級 | 評估 |
|-----------|-----------|---------|------|
| 斜視 (Esotropia) | 99.89% | L4 | 僅有麻醉後併發症報告，hyaluronidase 是可能的致病因子而非治療，無治療證據 |
| 閉經 | 99.83% | L5 | 僅有 1975 年內源性酵素活性研究，無外用治療證據 |
| 重度非增殖性糖尿病視網膜病變 | 99.79% | L3 | 僅有 n=10 開放標籤 Phase 2，可作為研究問題 |
| 腎小管酸中毒 | 99.76% | L5 | 無試驗與文獻，機轉上無合理連結 |
| 皮膚炎 | 99.73% | L4 | 文獻多為間接證據，且方向為抑制 hyaluronidase；過敏風險反向提示 |
| 慢性萎縮性肢端皮膚炎 | 99.58% | L5 | 無證據 |
| 糖尿病白內障 | 99.55% | L4 | 僅有麻醉輔助用途的間接文獻；1978 年研究顯示加入 hyaluronidase 組出現較多囊樣黃斑水腫 |
| 新生兒皮肌炎 | 99.51% | L5 | 無證據 |
| 非症候群性食道畸形 | 99.51% | L5 | 先天結構異常不太可能由基質降解酵素改善 |

---

## 結論與下一步

**決策：Hold**

**理由：**
- 糖尿病視網膜病變雖有 2 個已完成的 Phase 3 試驗（形式上符合 L1），但試驗針對玻璃體出血，開發計畫也未取得視網膜病變適應症，結果是否顯示明確療效尚不清楚；其餘預測多僅靠模型分數，缺乏實質證據。
- 本藥在香港的許可證缺少適應症與劑型資料，安全性資料（仿單警語、禁忌症）亦不完整，目前尚無法進入安全性篩選。

**若要推進需要：**
- 取得 NCT00198497、NCT00198510 的完整結果，並釐清開發中止的原因。
- 查閱香港衛生署仿單，補齊適應症、劑型、警語與禁忌症。
- 取得詳細的作用機轉資料（DrugBank）。
- 評估玻璃體內使用的安全性（發炎、眼壓、過敏）及與現有許可證劑型的給藥途徑相容性。
- 若考慮重度非增殖性糖尿病視網膜病變，需設計有對照組的臨床試驗。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

