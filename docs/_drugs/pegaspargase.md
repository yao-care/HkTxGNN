---
layout: default
title: Pegaspargase
parent: 高證據等級 (L1-L2)
nav_order: 670
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Pegaspargase：預測新適應症為前驅型淋巴母細胞淋巴瘤/白血病 (precursor lymphoblastic lymphoma/leukemia)（證據等級 L1）。原適應症：急性淋巴性白血病（ALL）"
---

# Pegaspargase
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Pegaspargase：從急性淋巴性白血病到前驅型淋巴母細胞淋巴瘤/白血病

## 一句話總結

Pegaspargase 是經聚乙二醇修飾的 L-天門冬醯胺酶，原本用於急性淋巴性白血病（ALL）的治療。
TxGNN 模型預測它可能對**前驅型淋巴母細胞淋巴瘤/白血病 (precursor lymphoblastic lymphoma/leukemia)** 有效，
目前有 **30 個臨床試驗**和 **20 篇文獻**支持這個方向。
需注意：這個預測與原適應症屬同一類疾病，較像是既有用途的再確認，而非真正的新用途。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性淋巴性白血病（ALL） |
| 預測新適應症 | 前驅型淋巴母細胞淋巴瘤/白血病 (precursor lymphoblastic lymphoma/leukemia) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

註：香港許可證資料中未載明核准適應症文字，原適應症係依知識圖譜的適應症資料列出。

---

## 為什麼這個預測合理？

Pegaspargase 是 PEG 化的 L-天門冬醯胺酶，能分解並耗竭血中的天門冬醯胺。淋巴母細胞的天門冬醯胺合成酶表現偏低，需依賴細胞外的天門冬醯胺，因此天門冬醯胺被耗竭後，蛋白質合成受抑制，白血病細胞走向死亡。

前驅型淋巴母細胞淋巴瘤/白血病與 ALL 本質上是同一類疾病（淋巴母細胞惡性腫瘤），臨床上常採用以 ALL 為基礎的相同方案治療。因此這項預測更像是對既有用途的確認，而非跨疾病的再利用。

目前缺乏 DrugBank 的詳細作用機轉欄位資料，上述機轉說明是依據已知的藥理學與本次整理的文獻內容。

---

## 臨床試驗證據

以下列出最相關的 10 個試驗（共 30 個登記）。多數試驗為多藥合併方案，pegaspargase 的單獨貢獻難以拆分。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00967057](https://clinicaltrials.gov/study/NCT00967057) | Phase 3 | 完成 | 470 | ALLR3 國際合作試驗，復發/難治型 ALL；pegaspargase 為方案骨幹之一 |
| [NCT00103285](https://clinicaltrials.gov/study/NCT00103285) | Phase 3 | 完成 | 5377 | 標準風險 B 前驅型 ALL 的大型隨機試驗，含天門冬醯胺酶的多藥方案 |
| [NCT05602194](https://clinicaltrials.gov/study/NCT05602194) | Phase 3 | 進行中（不再招募） | 440 | 以左旋肉鹼預防天門冬醯胺酶相關肝毒性，與安全防護直接相關 |
| [NCT02003222](https://clinicaltrials.gov/study/NCT02003222) | Phase 3 | 進行中（不再招募） | 488 | 新診斷 BCR-ABL 陰性 B 系 ALL 加入 blinatumomab；pegaspargase 在化療骨幹中 |
| [NCT00905034](https://clinicaltrials.gov/study/NCT00905034) | Phase 2 | 完成 | 37 | MOAD 方案（含 PEG 化天門冬醯胺酶）用於 ALL 挽救治療 |
| [NCT00890656](https://clinicaltrials.gov/study/NCT00890656) | Phase 2 | 完成 | 90 | 強化 hyper-CVAD 用於 ALL 挽救治療，單臂試驗 |
| [NCT01403415](https://clinicaltrials.gov/study/NCT01403415) | Phase 1 | 完成 | 13 | Temsirolimus 合併強化再誘導治療（含 pegaspargase）用於兒童復發 ALL/NHL |
| [NCT03643276](https://clinicaltrials.gov/study/NCT03643276) | Phase 3 | 招募中 | 5000 | AIEOP-BFM ALL 2017，兒童與青少年 ALL 國際合作方案 |
| [NCT03914625](https://clinicaltrials.gov/study/NCT03914625) | Phase 3 | 進行中（不再招募） | 6720 | 標準風險 B-ALL 或局限性 B 淋巴母細胞淋巴瘤，blinatumomab 合併含 pegaspargase 的化療 |
| [NCT01005914](https://clinicaltrials.gov/study/NCT01005914) | Phase 2 | 終止 | 11 | 在 hyper-CVAD 加入 PEG-天門冬醯胺酶用於成人新診斷 ALL，樣本很小 |

---

## 文獻證據

以下列出最相關的 10 篇（RCT 優先，其次為綜述與世代研究）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35271306](https://pubmed.ncbi.nlm.nih.gov/35271306/) | 2022 | RCT | J Clin Oncol | COG AALL1231：於新診斷 T-ALL/淋巴母細胞淋巴瘤測試 bortezomib |
| [32813610](https://pubmed.ncbi.nlm.nih.gov/32813610/) | 2020 | RCT | J Clin Oncol | COG AALL0434：於新診斷 T-ALL 測試 nelarabine |
| [27114587](https://pubmed.ncbi.nlm.nih.gov/27114587/) | 2016 | RCT | J Clin Oncol | AALL0232：地塞米松與高劑量甲氨蝶呤改善高風險 B-ALL 預後 |
| [40109190](https://pubmed.ncbi.nlm.nih.gov/40109190/) | 2025 | Review | Haematologica | 成人 ALL 使用天門冬醯胺酶/pegaspargase 不良事件的辨識、預防與處置專家共識 |
| [31030380](https://pubmed.ncbi.nlm.nih.gov/31030380/) | 2019 | Review | Drugs | Pegaspargase 於 ALL 的綜述；較原型 E. coli 天門冬醯胺酶循環時間更長 |
| [37276451](https://pubmed.ncbi.nlm.nih.gov/37276451/) | 2023 | Cohort | Blood Adv | GIMEMA LAL1913：成人 ALL 方案加入 pegaspargase 的風險導向治療 |
| [40858769](https://pubmed.ncbi.nlm.nih.gov/40858769/) | 2025 | Cohort | Ann Hematol | 55 歲以上 ALL 患者使用 pegaspargase 的耐受性次分析 |
| [40492422](https://pubmed.ncbi.nlm.nih.gov/40492422/) | 2025 | Cohort | Br J Haematol | CALGB 10403 方案整合 blinatumomab 鞏固治療的經驗 |
| [9161659](https://pubmed.ncbi.nlm.nih.gov/9161659/) | 1997 | Review | Ann Pharmacother | Pegaspargase 的化學、藥理、臨床活性與不良反應回顧 |
| [30823860](https://pubmed.ncbi.nlm.nih.gov/30823860/) | 2020 | Case report | J Oncol Pharm Pract | Pegaspargase 引起高三酸甘油酯血症的個案 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67823 | ONCASPAR POWDER FOR SOLUTION FOR INJECTION/INFUSION 3750 UNITS（廠商：SERVIER HONG KONG LIMITED） | 注射用粉劑（溶液用） | 未載明 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 酵素類抗腫瘤藥物（天門冬醯胺酶，PEG 化），並非傳統 DNA 損傷型細胞毒性藥物 |
| 骨髓抑制風險 | 請參考原廠仿單；本次資料未提供 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 肝功能、胰臟炎徵象（澱粉酶/脂肪酶）、血脂（三酸甘油酯）、血糖、凝血功能與血栓徵象、過敏反應 |
| 處置防護 | 請參考原廠仿單的處置規範 |

---

## 安全性考量

- **主要不良反應（依文獻）**：肝毒性、胰臟炎、血栓、高三酸甘油酯血症、高血糖、過敏反應。年長成人風險可能較高，55 歲以上與 40 歲以上族群已有專門的耐受性研究。
- **藥物交互作用**：資料庫共查得 100 筆交互作用，以下為部分中度（Moderate）項目：
  - 類固醇類：Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide
  - 降血糖藥：Metformin、Acarbose、Alogliptin、Canagliflozin、Dapagliflozin、Saxagliptin、Albiglutide、Dulaglutide、Chlorpropamide
  - 其他：Acetylsalicylic acid、Doxycycline、Tetracycline、Clarithromycin、Bupropion、Chenodeoxycholic acid

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多個已完成的 Phase 3 試驗（含 NCT00967057、NCT00103285），證據等級為 L1，且 pegaspargase 是 ALL 方案的標準組成。
- 此預測與原適應症屬同一疾病，應視為既有用途的確認而非新用途；其餘預測（慢性淋巴球性白血病、濾泡性淋巴瘤等）僅有模型分數，缺乏試驗與文獻，建議 Hold。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 補充作用機轉資料（DrugBank）
- 建立肝功能、胰臟炎、血栓、血脂、血糖與過敏反應的監測計畫，並對 55 歲以上族群評估劑量與耐受性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

