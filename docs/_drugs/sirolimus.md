---
layout: default
title: Sirolimus
parent: 高證據等級 (L1-L2)
nav_order: 690
evidence_level: L2
indication_count: 5
---

# Sirolimus
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

# Sirolimus：從器官移植排斥預防到脂肪肉瘤 (Liposarcoma)

## 一句話總結

Sirolimus（DrugBank DB00877）是一種 mTOR 抑制劑，其文獻脈絡（如 PMID 16434506、20534289）顯示原本用於腎臟移植後免疫抑制與排斥預防。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，
目前有 **5 個臨床試驗**和 **12 篇文獻**支持這個方向，其中包含一項 sirolimus 本體用於黏液性脂肪肉瘤的單臂 Phase 2 試驗。

> ⚠️ 本 Evidence Pack 的 `original_indications` 欄位為空、`original_moa` 標記為 [Data Gap]，且香港未上市（無許可證資料），下方原適應症相關描述僅基於文獻脈絡推論，非正式核准資料。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地無核准適應症登記資料（香港未上市；文獻脈絡指向腎臟移植排斥預防） |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Research Question（研究假說階段） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（Evidence Pack 標記為 [Data Gap]）。但根據 sirolimus 的藥理類別（mTOR 抑制劑）與現有文獻證據，可推論其機轉關聯性：

去分化脂肪肉瘤（dedifferentiated liposarcoma, DDL）存在 Akt-mTOR 及 MAPK 路徑活化（PMID 26518767），mTOR 抑制劑（sirolimus 及其同類藥物 temsirolimus、everolimus/ridaforolimus）具明確分子標靶依據。MDM2/CDK4 擴增亦與 mTOR 路徑交互作用，這是此類脂肪肉瘤的常見分子特徵。

更直接的證據是，sirolimus 本體已在一項單臂 Phase 2 試驗（NCT02821507）中用於治療轉移性或無法切除的黏液性脂肪肉瘤與軟骨肉瘤，顯示藥廠與研究機構已認可其機轉合理性並付諸臨床測試。同類 mTOR 抑制劑 ridaforolimus（AP23573）也在晚期肉瘤（含脂肪肉瘤）的 Phase 2 試驗中獲得正向訊號（NCT00093080）。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | 已完成 | 70 | sirolimus 合併 cyclophosphamide 用於轉移性/無法切除黏液性脂肪肉瘤及軟骨肉瘤，直接相關（本體藥物） |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | 已完成 | 216 | ridaforolimus（sirolimus 類似物）用於晚期肉瘤（含脂肪肉瘤） |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | 進行中（未招募） | 48 | ribociclib 合併 everolimus 用於去分化脂肪肉瘤及平滑肌肉瘤 |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | 已完成 | 24 | Torisel（temsirolimus）合併脂質體 doxorubicin 用於軟組織及骨肉瘤 |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | 已完成 | 46 | cixutumumab 合併 temsirolimus 用於兒童復發/難治性肉瘤 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | RCT | Clin Cancer Res | Ribociclib+Everolimus 於去分化脂肪肉瘤及平滑肌肉瘤之 Phase 2 結果，CDK4 與 mTOR 雙標靶具協同效果 |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | 軟組織肉瘤新型治療藥物綜述 |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Review | Cancer Genomics Proteomics | Chloroquine 與 rapamycin 合併抑制自噬，用於高分化脂肪肉瘤治療 |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Cohort | Tumour Biology | 去分化脂肪肉瘤中 Akt-mTOR 與 MAPK 路徑活化之免疫組織化學分析 |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | Cohort | J Am Soc Nephrol | Sirolimus 早期停用 cyclosporine 後可降低成人腎臟移植患者癌症風險 |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | 晚期肉瘤新型標靶治療綜述 |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | 罕見結締組織腫瘤與肉瘤之標靶治療 |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | 臨床前 | Mol Cancer Ther | MLN0128（ATP 競爭性 mTOR 激酶抑制劑）於骨與軟組織肉瘤具抗腫瘤活性 |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | 臨床前 | In Vivo | Chloroquine 合併 rapamycin 於去分化脂肪肉瘤 PDOX 小鼠模型中抑制腫瘤生長 |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Cohort | Transplant Proc | 腎臟移植免疫抑制治療患者之癌症篩檢研究 |

---

## 香港上市資訊

目前無香港許可證登記資料（`taiwan_regulatory.market_status` = 未上市，`total_licenses` = 0）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 資料缺口提示：本 Evidence Pack 標記「HK 仿單警語/禁忌」為 **Blocking** 等級缺口（DG001），此項缺失使本候選**無法進入 S1 安全性初評階段**；「作用機轉 (MOA)」為 **High** 等級缺口（DG002），影響機轉關聯性分析的嚴謹度。

---

## 結論與下一步

**決策：Research Question（研究假說階段）**

**理由：**
- 已有 sirolimus 本體用於黏液性脂肪肉瘤的 Phase 2 試驗（NCT02821507）及同類藥物的多項 Phase 2 證據，機轉層面（mTOR 路徑活化）具合理性，對應證據等級 L2。
- 但香港無上市許可、無安全性仿單資料（Blocking 缺口），且 MOA 資料缺失，尚不足以支持進入正式安全性評估流程。

**若要推進需要：**
- 取得 sirolimus 完整 MOA 與 DrugBank 分類資料（DG002）
- 取得香港（或參考地區）仿單警語與禁忌症資料，解除 Blocking 缺口（DG001）
- 完成待分類文獻（多筆 `classification.study_type` 及 `relevance` 為 pending）之系統性分級
- 評估 sirolimus 現有劑型是否符合脂肪肉瘤治療所需給藥途徑
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

