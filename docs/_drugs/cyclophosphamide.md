---
layout: default
title: Cyclophosphamide
parent: 僅模型預測 (L5)
nav_order: 230
evidence_level: L5
indication_count: 5
---

# Cyclophosphamide
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

# Cyclophosphamide：從（香港登記資料未載明適應症）到骨髓性白血病

## 一句話總結

Cyclophosphamide 是烷化劑類抗癌藥，在香港有 4 張上市許可證，但登記資料沒有列出核准適應症。
TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效。
目前有 **50 個臨床試驗**和 **20 篇文獻**與此方向相關，但大多是把它當作移植前處理、移植後 GVHD 預防或 CAR-T 淋巴清除的一環，並非單獨評估它對白血病的療效。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明 |
| 預測新適應症 | 骨髓性白血病 (Myeloid Leukemia) |
| TxGNN 預測分數 | 99.47% |
| 證據等級 | L3（見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

證據等級說明：Evidence Pack 標示為 L2，但依判定規則，L2 需要 1 個已完成的 Phase 2/3 RCT。最直接的完成型 Phase 2 試驗 NCT01707004 是單臂試驗，不符合 RCT 條件。其餘證據以系統性回顧、網絡統合分析和世代研究為主，因此這裡判為 L3。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空）。根據一般藥理知識，Cyclophosphamide 是一種前驅藥，經肝臟活化後成為 DNA 烷化劑。它同時有細胞毒殺和淋巴清除（免疫抑制）作用。這些說明來自通用藥理，不是 Evidence Pack 提供的資料。

這兩種作用剛好對應它在骨髓性白血病（尤其是 AML）移植治療中的角色：

- 與 busulfan 合併的清髓性前處理（Bu/Cy）。
- 高劑量使用。
- 移植後 Cyclophosphamide（PTCy）預防 GVHD。

因此，這個預測比較像是印證既有的臨床用法，而不是全新的老藥新用。現有證據也沒有顯示它單獨用於白血病的療效。

## 臨床試驗證據

從 50 個相關試驗中挑選最相關的 10 個。多數試驗中 Cyclophosphamide 只是組成之一。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01707004](https://clinicaltrials.gov/study/NCT01707004) | Phase 2 | 完成 | 20 | Decitabine 加全身放射後接骨髓移植與高劑量 Cyclophosphamide，用於復發/難治型 AML；單臂試驗 |
| [NCT02724163](https://clinicaltrials.gov/study/NCT02724163) | Phase 3 | 招募中 | 700 | 兒童 AML 國際隨機試驗，比較誘導化療組合並找 gemtuzumab 劑量；未顯示 Cyclophosphamide 是受測變項 |
| [NCT02294552](https://clinicaltrials.gov/study/NCT02294552) | Phase 2 | 完成 | 200 | 高劑量移植後 Cyclophosphamide 預防異體移植後 GVHD |
| [NCT03246906](https://clinicaltrials.gov/study/NCT03246906) | Phase 2 | 終止 | 150 | 隨機比較 cyclosporine/sirolimus 合併 MMF 或 PTCy 預防 GVHD |
| [NCT04888741](https://clinicaltrials.gov/study/NCT04888741) | Phase 2 | 未知 | 400 | 非親緣移植中比較 Thymoglobulin 與含 PTCy 的 GVHD 預防 |
| [NCT02627573](https://clinicaltrials.gov/study/NCT02627573) | Phase 2 | 終止 | 32 | 隨機比較 PTCy 與 Thymoglobulin，對象為慢性骨髓增生性腫瘤和 MDS |
| [NCT02759822](https://clinicaltrials.gov/study/NCT02759822) | 不適用 | 未知 | 30 | 單倍體移植加 PTCy 治療急性白血病的前瞻性觀察世代 |
| [NCT02094794](https://clinicaltrials.gov/study/NCT02094794) | Phase 2 | 進行中（不招募） | 108 | 全骨髓與淋巴放射（TMLI）加 Cyclophosphamide 與 etoposide 作為高風險 ALL/AML 移植前處理 |
| [NCT00047060](https://clinicaltrials.gov/study/NCT00047060) | Phase 1/2 | 完成 | 5 | 血液幹細胞移植治療晚期蕈樣肉芽腫/Sézary 症候群；樣本極小 |
| [NCT00005804](https://clinicaltrials.gov/study/NCT00005804) | Phase 2 | 完成 | 未提供 | 非親緣骨髓移植治療血液惡性腫瘤；未確認 Cyclophosphamide 的角色 |

## 文獻證據

本次沒有 RCT 文獻，依「Review > 世代研究」排序，共列 10 篇。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | 系統性回顧/網絡統合分析 | Bone Marrow Transplant | 比較成人 AML 緩解期異體移植的清髓性前處理方案，Bu/Cy 為常用方案 |
| [28883081](https://pubmed.ncbi.nlm.nih.gov/28883081/) | 2017 | 專家立場聲明 | Haematologica | EBMT 對成人 AML 單倍體移植的立場聲明 |
| [32857869](https://pubmed.ncbi.nlm.nih.gov/32857869/) | 2020 | Review | Am J Hematol | 探討 PTCy 時代下 NK 細胞同種反應性在 AML 的角色 |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | 世代研究 | Future Oncol | 比較 BuCy 與 FluBu 前處理用於 AML 異體移植 |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | 世代研究 | Bone Marrow Transplant | EBMT 1,823 名 AML 病人使用 PTCy，依細胞遺傳/分子風險分析前處理強度的影響 |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | 世代研究 | Eur J Haematol | 65 歲以下 AML 使用 ATG 加 PTCy，比較清髓與減量前處理的存活 |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | 世代研究 | Int J Mol Sci | 兒童 AML 配對手足/非親緣移植使用 PTCy 的首批資料 |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | 比較研究 | Am J Hematol | 165 名 AML 病人比較清髓移植與 Cy/Flu 非清髓移植，存活結果無差異 |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | 病例系列 | Leuk Lymphoma | 27 名高白血球或白血球淤滯的 AML 病人使用高劑量 Cyclophosphamide（60 mg/kg）降低腫瘤負荷 |
| [29039989](https://pubmed.ncbi.nlm.nih.gov/29039989/) | 2017 | 病例系列 | Pediatr Hematol Oncol | 17 名復發/難治型兒童 AML 使用 clofarabine、Cyclophosphamide 與 etoposide，41% 有反應 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-51711 | ENDOXAN TAB 50MG | BAXTER HEALTHCARE LIMITED |
| HK-51308 | ENDOXAN FOR INJ 1G | BAXTER HEALTHCARE LIMITED |
| HK-01327 | ENDOXAN 200 MG INJ | BAXTER HEALTHCARE LIMITED |
| HK-50943 | CYCRAM FOR INJ 1G | HEALTHCARE PHARMASCIENCE LIMITED |

劑型欄位與核准適應症在登記資料中均為空白，需查閱衛生署仿單。

## 細胞毒性

以下為藥物類別的通用知識，Evidence Pack 未提供 toxicity 資料，實際內容請以原廠仿單為準。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（烷化劑，前驅藥） |
| 骨髓抑制風險 | 高（可造成嗜中性白血球減少、血小板減少） |
| 致吐性分級 | 中至高（隨劑量升高，高劑量偏高） |
| 監測項目 | CBC（含分類）、肝腎功能、尿液檢查（出血性膀胱炎）、電解質 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。警語、禁忌症都沒有可用資料，藥物交互作用查詢也無結果。

文獻提示：PMID [25612567](https://pubmed.ncbi.nlm.nih.gov/25612567/)（2015）報告 Cyclophosphamide 治療後早期發生次發性 AML，屬於治療相關骨髓腫瘤的風險。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Cyclophosphamide 已深入 AML 移植實務（Bu/Cy 前處理、PTCy），有系統性回顧、大型世代研究和多個 Phase 2 試驗支持。
- 但現有證據多屬組合方案的一部分，沒有單獨療效的隨機對照資料，證據等級為 L3。
- 香港仿單的警語與禁忌症尚缺，這是 Evidence Pack 標示的阻斷性缺口，安全性篩選前不宜再往前推。

**若要推進需要：**
- 取得衛生署仿單，補齊警語、禁忌症與核准適應症（DG001，阻斷性）。
- 補齊 DrugBank 作用機轉資料（DG002）。
- 明確界定使用情境（清髓前處理、PTCy 或淋巴清除），並針對各情境整理 Cyclophosphamide 特有的效果。
- 建立骨髓抑制、出血性膀胱炎與次發性惡性腫瘤的監測計畫。

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

