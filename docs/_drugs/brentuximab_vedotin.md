---
layout: default
title: Brentuximab Vedotin
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Brentuximab Vedotin：預測新適應症為濾泡性淋巴瘤 (Follicular Lymphoma)（證據等級 L5）。原適應症：何杰金氏淋巴瘤（Hodgkin lymphoma，含典型何杰金氏淋巴瘤）"
monitor_inn: "BRENTUXIMAB VEDOTIN"
predicted_indications: ["follicular lymphoma", "myeloid leukemia", "acute lymphoblastic/lymphocytic leukemia", "B-cell neoplasm", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "Richter syndrome", "mantle cell lymphoma", "ganglioneuroblastoma (disease)", "vertebral anomalies and variable endocrine and T-cell dysfunction"]
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Brentuximab Vedotin：從何杰金氏淋巴瘤到濾泡性淋巴瘤
{: .text-alpha }

## 一句話總結

Brentuximab Vedotin 是一種靶向 CD30 的抗體藥物複合體（ADC），原本用於何杰金氏淋巴瘤（Hodgkin lymphoma）治療。
TxGNN 模型預測它可能對**濾泡性淋巴瘤 (Follicular Lymphoma)** 有效，但目前僅有 **6 個相關臨床試驗**（其中 3 個撤回、2 個提前終止，僅 1 個仍在招募）和以綜述為主的文獻，證據仍屬早期。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 何杰金氏淋巴瘤（Hodgkin lymphoma，含典型何杰金氏淋巴瘤） |
| 預測新適應症 | 濾泡性淋巴瘤 (Follicular Lymphoma) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L2（依資料編製時的評估；但尚無已完成且有結果的 Phase 2/3 RCT，實際證據偏弱） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

> 說明：原適應症來自知識圖譜的適應症資料，香港許可證上未登載核准適應症文字。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 欄位未收錄）。根據已知資訊，Brentuximab Vedotin 是以 CD30 為標的的抗體藥物複合體，由抗 CD30 抗體連接 MMAE（一種微管抑制型細胞毒性藥物）組成，抗體結合 CD30 陽性細胞後將毒素送入細胞內。

何杰金氏淋巴瘤的 Reed-Sternberg 細胞高度表現 CD30，這是此藥療效的基礎。濾泡性淋巴瘤同屬淋巴系惡性腫瘤，但 CD30 表現變異大且通常偏低，因此理論基礎主要落在 CD30 陽性的亞群，或可能的旁觀者效應（bystander effect）。

臨床上已有與 rituximab、bendamustine 合併的 Phase 2 試驗被設計，但多數被撤回或提前終止，療效尚未被證實。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04587687](https://clinicaltrials.gov/study/NCT04587687) | Phase 2 | 招募中 | 23 | BV + bendamustine 用於復發/難治性濾泡性淋巴瘤，直接對應此適應症，尚無結果 |
| [NCT01805037](https://clinicaltrials.gov/study/NCT01805037) | Phase 1/2 | 提前終止 | 20 | BV + rituximab 作為 CD30+/EBV+ 淋巴瘤第一線治療，資料有限 |
| [NCT02594163](https://clinicaltrials.gov/study/NCT02594163) | Phase 2 | 提前終止 | 25 | 隨機試驗：rituximab + bendamustine 加或不加 BV，用於 CD30+ DLBCL，樣本過少 |
| [NCT04138875](https://clinicaltrials.gov/study/NCT04138875) | Phase 2 | 撤回 | 0 | 移植後淋巴增生異常的 RBvB 分層治療，未收案 |
| [NCT02623920](https://clinicaltrials.gov/study/NCT02623920) | Phase 2 | 撤回 | 0 | BV + bendamustine + rituximab 用於 CD30+ B 細胞 NHL，未收案 |
| [NCT04795869](https://clinicaltrials.gov/study/NCT04795869) | Phase 2 | 撤回 | 0 | BV + pembrolizumab 用於復發性周邊 T 細胞淋巴瘤，未收案 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38364196](https://pubmed.ncbi.nlm.nih.gov/38364196/) | 2024 | RCT | J Clin Oncol | Ro-CHOP 試驗最終分析（周邊 T 細胞淋巴瘤，非 BV 試驗） |
| [40758949](https://pubmed.ncbi.nlm.nih.gov/40758949/) | 2025 | Cohort | Blood Adv | LYSA Phase 2：BV 加 gemcitabine 用於復發/難治性周邊 T 細胞淋巴瘤 |
| [33320379](https://pubmed.ncbi.nlm.nih.gov/33320379/) | 2021 | Cohort | Eur J Haematol | BV 加 ICE 用於復發/難治性周邊 T 細胞淋巴瘤 |
| [35663281](https://pubmed.ncbi.nlm.nih.gov/35663281/) | 2022 | Review | Leuk Res Rep | 惰性非何杰金氏淋巴瘤（含濾泡性淋巴瘤）免疫治療回顧 |
| [38306597](https://pubmed.ncbi.nlm.nih.gov/38306597/) | 2024 | Review | Blood | 常見周邊 T 細胞淋巴瘤亞型的現行與新興治療 |
| [39644004](https://pubmed.ncbi.nlm.nih.gov/39644004/) | 2024 | Review | Hematology ASH Educ Program | BV 及新藥於周邊 T 細胞淋巴瘤的應用 |
| [32476657](https://pubmed.ncbi.nlm.nih.gov/32476657/) | 2020 | Case report | Gulf J Oncol | 一級濾泡性淋巴瘤轉化為 CD30+ 間變性大細胞淋巴瘤，BV 加高劑量 methotrexate 達完全緩解 |

> 說明：多數文獻聚焦於周邊 T 細胞淋巴瘤，並非濾泡性淋巴瘤本身，對此適應症屬間接證據。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63483 | ADCETRIS POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 50MG（廠商：Takeda Pharmaceuticals (Hong Kong) Limited） | 未登載 | 未登載 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗 CD30 抗體藥物複合體，攜帶 MMAE 微管抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 一般建議監測 CBC（含分類）、肝腎功能 |
| 處置防護 | 請參考原廠仿單，並依細胞毒性藥物處置規範操作 |

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 筆交互作用，以下為列出的中度等級項目範例：Acarbose、Albiglutide、Alogliptin、Metformin、Pioglitazone、Bupropion、Clarithromycin、Clotrimazole、Eliglustat 等；多為降血糖藥物，另有數種 CYP 相關藥物。

主要警語與禁忌症資料缺漏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 濾泡性淋巴瘤的 CD30 表現低且不一致，機轉依據薄弱；6 個相關試驗中 3 個撤回、2 個提前終止，唯一直接針對此適應症的 Phase 2（NCT04587687）仍在招募且尚無結果。
- 資料編製時雖給予 L2 分級，但並無已完成且有結果的 Phase 2/3 RCT 支持，且許可證與安全性資料不足。
- 同一份資料中，B 細胞腫瘤（CD30+ DLBCL）的證據相對較強，若要優先探索，可考慮該方向。

**若要推進需要：**
- 等待 NCT04587687 的結果
- 評估濾泡性淋巴瘤患者的 CD30 表現率，建立以 CD30 為基礎的篩選策略
- 補齊作用機轉資料（MOA）
- 取得香港原廠仿單的警語、禁忌症與核准適應症資料，完成安全性評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

