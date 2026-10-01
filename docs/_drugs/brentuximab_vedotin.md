---
layout: default
title: Brentuximab Vedotin
parent: 僅模型預測 (L5)
nav_order: 124
evidence_level: L5
indication_count: 10
---

# Brentuximab Vedotin
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

# Brentuximab Vedotin：從 CD30 陽性淋巴瘤到濾泡性淋巴瘤

## 一句話總結

Brentuximab Vedotin（品牌 Adcetris）是靶向 CD30 的抗體藥物複合體（ADC），文獻描述其原本用於何杰金氏淋巴瘤與系統性間變性大細胞淋巴瘤。
TxGNN 模型預測它可能對**濾泡性淋巴瘤 (Follicular Lymphoma)** 有效，但直接證據很薄弱：僅有 **1 個進行中的小型 Phase 2 試驗**（23 人，尚無結果）和少數間接文獻。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明；文獻描述為何杰金氏淋巴瘤、系統性間變性大細胞淋巴瘤 (sALCL) |
| 預測新適應症 | 濾泡性淋巴瘤 (Follicular Lymphoma) |
| TxGNN 預測分數 | 99.89%（排名 2,812） |
| 證據等級 | L3（資料包標為 L2，但依判定規則，FL 試驗中沒有已完成的 RCT，故下修） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

DrugBank 的作用機轉欄位目前缺資料。依本次分析的機轉推論，Brentuximab Vedotin 由抗 CD30 抗體連結 MMAE（微管抑制劑）組成。抗體結合 CD30 陽性細胞後被內化，釋放 MMAE 殺死細胞。MMAE 還有旁觀者效應，可影響鄰近的腫瘤細胞。

濾泡性淋巴瘤是 B 細胞淋巴瘤，和已核准的何杰金氏淋巴瘤同屬淋巴系惡性腫瘤。但**濾泡性淋巴瘤的 CD30 表現通常偏低且不一致**，所以機轉契合度只是部分成立。最合理的應用對象是 CD30 陽性的轉化型或侵襲性亞群。

文獻中有一例濾泡性淋巴瘤轉化為 CD30 陽性 ALCL，使用本藥加高劑量 methotrexate 後達到完全緩解。這只是個案，不能推論到一般濾泡性淋巴瘤。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | 招募中 | 23 | BV 加 bendamustine 用於復發/難治性濾泡性淋巴瘤；直接對應本適應症，但樣本小、尚無結果 |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | 已終止 | 20 | BV 加 rituximab 用於 CD30+ 和/或 EBV+ 淋巴瘤的第一線治療；提前終止，FL 專屬訊號有限 |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | 已終止 | 25 | 隨機分組，比較 rituximab + bendamustine 加或不加 BV，對象為 CD30+ DLBCL；提前終止，統計檢定力不足 |
| [NCT02623920](https://clinicaltrials.gov/study/NCT02623920) | Phase 2 | 已撤回 | 0 | BV + bendamustine + rituximab 用於 CD30+ B 細胞 NHL；未收案，無證據價值 |
| [NCT04795869](https://clinicaltrials.gov/study/NCT04795869) | Phase 2 | 已撤回 | 0 | BV + pembrolizumab 用於復發性 PTCL；未收案，且非本適應症 |
| [NCT04138875](https://clinicaltrials.gov/study/NCT04138875) | Phase 2 | 已撤回 | 0 | RBvB 用於移植後淋巴增生疾患；未收案，且非本適應症 |

以上試驗沒有任何已完成且有結果的 FL 專屬試驗。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | 回顧 | Leukemia Research Reports | 惰性 NHL（含 FL）的免疫治療回顧；為 FL 相關的一般性背景資料 |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | 回顧 | Blood | 常見 PTCL 亞型的治療進展，CD30 陽性者可用 BV 加 CHP；非 FL |
| [39644004](https://pubmed.ncbi.nlm.nih.gov/39644004/) | 2024 | 回顧 | Hematology ASH Educ. Program | 說明 BV 已納入 PTCL 第一線方案；非 FL |
| [40517441](https://pubmed.ncbi.nlm.nih.gov/40517441/) | 2025 | 回顧 | Hematological Oncology | PTCL 亞型繁多、治療方向的展望；非 FL |
| [28967896](https://pubmed.ncbi.nlm.nih.gov/28967896/) | 2018 | 回顧 | Bone Marrow Transplantation | 淋巴瘤自體移植後的維持治療；提到 FL 使用 rituximab 維持治療 |
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | 臨床研究 (Phase 2) | Blood Advances | LYSA 研究：BV 加 gemcitabine 用於復發/難治性 CD30+ PTCL；非 FL |
| [34797505](https://pubmed.ncbi.nlm.nih.gov/34797505/) | 2022 | 回溯性真實世界研究 | Advances in Therapy | BV 加 CEP 用於未經治療的 PTCL 之短期療效與安全性；非 FL |
| [33320379](https://pubmed.ncbi.nlm.nih.gov/33320379/) | 2021 | 回溯性研究 | European Journal of Haematology | BV 加 ICE 用於復發/難治性 PTCL；非 FL |
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | 個案報告 | Gulf Journal of Oncology | 第 1 級 FL 轉化為 CD30+ ALCL，使用 BV 與高劑量 methotrexate 後完全緩解 |
| [38028985](https://pubmed.ncbi.nlm.nih.gov/38028985/) | 2023 | 個案報告 | Case Reports in Hematology | FL 轉化為 EBV+ DLBCL 與古典型何杰金氏淋巴瘤；說明轉化型 CD30+ 疾病的存在，未證實 BV 療效 |

這批文獻大多是 PTCL 相關，直接評估 BV 用於 FL 的研究幾乎沒有。沒有 RCT。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63483 | ADCETRIS POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 50MG（廠商：TAKEDA PHARMACEUTICALS (HONG KONG) LIMITED） | — | — |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗 CD30 抗體藥物複合體，payload 為 MMAE 微管抑制劑） |
| 骨髓抑制風險 | 中（依藥物類別判斷，常見嗜中性白血球減少）；本資料包無 toxicity 資料 |
| 致吐性分級 | 低（依藥物類別判斷） |
| 監測項目 | CBC（含分類）、肝功能、周邊神經病變評估、輸注反應 |
| 處置防護 | 屬於含細胞毒性成分的藥物，需依細胞毒性藥物處置規範操作 |

以上為依藥物類別的一般判斷，實際警語請參考原廠仿單。

---

## 安全性考量

安全性資訊請參考原廠仿單。本資料包沒有可用的警語、禁忌症資料，藥物交互作用查詢也無結果。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 只有一個 FL 專屬試驗（NCT04587687），為 23 人的招募中 Phase 2，尚無結果。其他相關試驗多數已終止或撤回。
- FL 的 CD30 表現偏低，機轉契合度有限，而香港仿單的安全性資料缺口屬於阻擋級。
- 同一份資料包中，「B 細胞腫瘤」的預測有 Phase 3 證據（何杰金氏淋巴瘤試驗），但那些屬於已確立的適應症，不能拿來支持 FL。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌症、核准適應症），補齊阻擋級的安全性缺口
- 追蹤 NCT04587687 的結果（預計完成日 2026-12）
- 取得 FL 檢體的 CD30 表現資料，界定可能受益的亞群（例如 CD30 陽性的轉化型）
- 補齊 DrugBank 的作用機轉資料
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

