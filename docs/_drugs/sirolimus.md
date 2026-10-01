---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 802
evidence_level: L5
indication_count: 5
---

# Sirolimus
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

# Sirolimus：從器官移植免疫抑制到脂肪肉瘤

## 一句話總結

Sirolimus（Rapamycin，香港商品名 Rapamune）是 mTOR 抑制劑，常用於腎臟移植後的免疫抑制。香港許可證資料未列出核准適應症文字。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，目前有 **5 個臨床試驗**和 **12 篇文獻**。但這些試驗大多使用其他 rapalog 藥物（temsirolimus、everolimus、ridaforolimus），尚無 sirolimus 在脂肪肉瘤的直接療效數據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L4（Evidence Pack 標示 L2，但缺乏 RCT 且屬類別效應推論，依判定規則下修） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 尚未取得）。根據文獻，sirolimus 是 mTOR（哺乳動物雷帕黴素標靶蛋白）抑制劑，在實驗模型中能抑制而非促進腫瘤生長。

去分化脂肪肉瘤中已有研究證實 Akt-mTOR 與 MAPK 路徑被活化（PMID 26518767），因此抑制 mTOR 在機轉上有合理性。前臨床研究也顯示，rapamycin 合併 chloroquine（阻斷自噬）在去分化脂肪肉瘤的患者來源異種移植 (PDOX) 小鼠模型中能抑制腫瘤生長。

目前的臨床證據多為其他 rapalog 在混合肉瘤族群的單臂 Phase 2 或 Phase 1/2 試驗，不是 RCT。因此這個預測目前屬於類別效應的推論。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | 完成 | 70 | Sirolimus 合併 cyclophosphamide 用於轉移性或無法切除的黏液性脂肪肉瘤與軟骨肉瘤，單臂試驗，尚無可見的療效結果 |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | 完成 | 216 | Ridaforolimus（mTOR 抑制劑）用於晚期肉瘤，脂肪肉瘤可能為其中的亞群 |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | 進行中（不再招募） | 48 | Ribociclib 合併 everolimus 用於晚期去分化脂肪肉瘤與平滑肌肉瘤，疾病吻合但藥物非 sirolimus |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | 完成 | 24 | Temsirolimus 合併微脂體 doxorubicin 用於復發性軟組織與骨肉瘤 |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | 完成 | 46 | Cixutumumab 合併 temsirolimus 用於兒童復發或難治性實體瘤，族群為兒童，適用性低 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | RCT | J Am Soc Nephrol | 腎臟移植早期停用 cyclosporine 並改用 sirolimus，可降低癌症風險（結局為癌症風險，非肉瘤療效） |
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 試驗報告 | Clin Cancer Res | Ribociclib 合併 everolimus 用於去分化脂肪肉瘤與平滑肌肉瘤 |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | 前臨床／轉譯研究 | Tumour Biol | 99 例去分化脂肪肉瘤檢體顯示 Akt-mTOR 與 MAPK 路徑活化，並有 mTOR 抑制劑的體外抗腫瘤試驗 |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | 前臨床 | Cancer Genomics Proteomics | Chloroquine 合併 rapamycin 阻斷自噬，對高分化脂肪肉瘤有協同效果 |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | 前臨床 (PDOX) | In Vivo | Chloroquine 合併 rapamycin 在去分化脂肪肉瘤 PDOX 模型中抑制腫瘤生長 |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | 前臨床 | Mol Cancer Ther | ATP 競爭型 mTOR 激酶抑制劑 MLN0128 對骨與軟組織肉瘤有抗腫瘤活性；第一代 rapalog 的臨床效益有限 |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | 軟組織肉瘤新療法的進展回顧 |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | 晚期肉瘤標靶藥物的臨床試驗回顧 |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | 罕見結締組織腫瘤與肉瘤的標靶治療 |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | 世代研究／回顧 | Transplant Proc | 長期免疫抑制的腎臟移植患者之癌症篩檢 |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-50220 | RAPAMUNE TAB 1MG | PFIZER CORPORATION HONG KONG LIMITED |
| HK-61049 | RAPAMUNE TAB 0.5MG | PFIZER CORPORATION HONG KONG LIMITED |
| HK-67922 | RAPAMUNE ORAL SOLUTION 1MG/ML | PFIZER CORPORATION HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。目前尚未取得香港衛生署仿單的警語與禁忌資料，藥物交互作用查詢也無結果。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有 sirolimus 在脂肪肉瘤的直接療效數據，臨床證據來自其他 rapalog 的單臂 Phase 2 試驗，且混合了不同肉瘤亞型。
- 香港仿單的安全性資料缺漏，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌。
- 補充 DrugBank 的作用機轉資料。
- 取得 NCT02821507（sirolimus 合併 cyclophosphamide）的結果，並確認其中脂肪肉瘤亞群的療效。
- 檢視 NCT00093080 等試驗的脂肪肉瘤亞群分析。

**補充：**
同一份 Evidence Pack 中，**淋巴管平滑肌瘤病 (LAM，lymphangiomyoma)** 與**良性 PEComa** 的證據較強，兩者都有 TSC/mTORC1 的明確機轉。
- LAM 有 Phase 3 試驗 NCT00414648（MILES，sirolimus 用於 LAM），並有 NCT03150914 等 sirolimus 試驗。
- 良性 PEComa 有 everolimus 的 Phase 3 RCT（NCT00790400）。
- 兩者的評級均為 L2，建議決策為 Proceed with Guardrails，建議優先評估。

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

