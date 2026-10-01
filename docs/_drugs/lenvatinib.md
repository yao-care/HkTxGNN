---
layout: default
title: Lenvatinib
parent: 中證據等級 (L3-L4)
nav_order: 510
evidence_level: L3
indication_count: 10
---

# Lenvatinib
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Lenvatinib：從多激酶抑制劑既有用途到脂肪肉瘤

## 一句話總結

Lenvatinib 是一種多激酶抑制劑，已在香港上市，但本次資料未提供其原適應症。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效。
目前有 **1 個已完成的臨床試驗**和 **4 篇文獻**，其中只有 1 個單臂 Phase Ib/II 試驗直接支持，且為 lenvatinib 併用 eribulin 的組合。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.51% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 尚未取得）。以下為一般藥理背景，並非來自本次資料集：Lenvatinib 是多激酶抑制劑，作用標的包括 VEGFR1-3、FGFR1-4、PDGFRα、RET、KIT，因此在肉瘤中具有抗血管新生的合理性。

支持這個預測的臨床訊號，來自 lenvatinib 併用 eribulin（微管抑制型化療藥）的 LEADER 研究。該研究在晚期脂肪肉瘤與平滑肌肉瘤中測試此組合。由於是併用療法，無法區分 lenvatinib 本身的貢獻。0.995 的 TxGNN 分數僅是模型預測，不能取代臨床證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03526679](https://clinicaltrials.gov/study/NCT03526679) | Phase 1/2 | 完成 | 30 | LEADER 研究：lenvatinib + eribulin 用於無法手術或轉移性脂肪細胞肉瘤與平滑肌肉瘤，為單臂試驗，無對照組 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36129471](https://pubmed.ncbi.nlm.nih.gov/36129471/) | 2022 | Phase Ib/II 單臂試驗 | Clin Cancer Res | LEADER 研究發表，評估 lenvatinib + eribulin 用於晚期脂肪肉瘤與平滑肌肉瘤的安全性與療效（摘要未提供具體數據） |
| [34326745](https://pubmed.ncbi.nlm.nih.gov/34326745/) | 2021 | Case report | Case Rep Oncol | 去分化脂肪肉瘤肺轉移個案，經標靶、手術、化療的綜合治療後腫瘤明顯縮小（摘要未載明是否使用 lenvatinib） |
| [39103896](https://pubmed.ncbi.nlm.nih.gov/39103896/) | 2024 | 前臨床／生物標記研究 | Exp Hematol Oncol | 探討 CDK4 作為軟組織肉瘤預後標記，以及抑制 CDK4 在去分化脂肪肉瘤序列治療中的協同效果，與 lenvatinib 無直接關聯 |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | 前臨床組合研究 | Anticancer Res | Eribulin 與不同機轉抗癌藥併用的廣譜前臨床抗腫瘤活性，說明併用 eribulin 的合理性 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 廠商 |
|---------|------|------|------|
| HK-64507 | LENVIMA CAPSULES 10MG | 膠囊（依品名） | EISAI (HONG KONG) COMPANY LIMITED |
| HK-64508 | LENVIMA CAPSULES 4MG | 膠囊（依品名） | EISAI (HONG KONG) COMPANY LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多激酶抑制劑） |
| 其他項目 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單。目前尚未取得香港衛生署仿單的警語與禁忌資料。

## 結論與下一步

**決策：Hold**

**理由：**
脂肪肉瘤目前只有 1 個單臂 Phase Ib/II 試驗（n=30），且為 lenvatinib 併用 eribulin，無隨機對照證據，也無法分離 lenvatinib 的單獨貢獻。此外，安全性與 MOA 資料都有缺口。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料（目前為阻斷性缺口）
- 補齊 DrugBank 作用機轉資料
- 取得 LEADER 研究的完整療效與安全性數據，並針對脂肪肉瘤亞型分析
- 尋找 lenvatinib 單藥或隨機對照的脂肪肉瘤證據

**補充：** 同一份資料中，預測排名第 7 的腎細胞癌 (renal carcinoma) 已有 Phase 3 CLEAR 試驗等 L1 證據，且 lenvatinib 已上市用於該適應症。該項較接近確認既有用途，而非新的老藥新用，可另行評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

