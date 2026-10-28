---
layout: default
title: Mercaptopurine
parent: 高證據等級 (L1-L2)
nav_order: 565
evidence_level: L2
indication_count: 8
monitor_inn: "MERCAPTOPURINE"
predicted_indications: ["myeloid leukemia", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pulmonary blastoma", "Hodgkins lymphoma", "primary pulmonary lymphoma", "small cell lung carcinoma", "well-differentiated fetal adenocarcinoma of the lung"]
last_modified_at: 2026-10-23
description: "Mercaptopurine：預測新適應症為骨髓性白血病 (myeloid leukemia)（證據等級 L2）。原適應症：本地許可證資料未記載適應症"
---

# Mercaptopurine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **8** 個
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

## Mercaptopurine: 骨髓性白血病 (myeloid leukemia)
{: .text-alpha }

## 一句話總結

Mercaptopurine（6-MP）是一種嘌呤類抗代謝藥物，知識圖譜中記錄的原適應症為急性淋巴性白血病。
TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效，
目前資料中有 **15 個臨床試驗**和 **20 篇文獻**與此方向相關，但多數試驗中 6-MP 的角色無法單獨判斷。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 骨髓性白血病 (myeloid leukemia) |
| TxGNN 預測分數 | 0.9994 |
| 證據等級 | L2（見下方說明） |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 核准許可證數 | 2 張（有效 2 張） |
| 建議決策 | Proceed with Guardrails |

**證據等級說明：** 資料中有直接針對骨髓性白血病（AML）的研究，包括 Phase 3 試驗 NCT02521493（唐氏症 AML，進行中）、Phase 1 試驗 NCT05506332 與 NCT06199557（直接使用 6-MP 組合），以及 AML 的 6-MP 觀察性研究（PMID 26425037、27275453）。然而，沒有已完成且能明確歸因於 6-MP 的 Phase 2/3 RCT，因此 L2 的條件並未完全滿足；保守判斷應視為介於 L2 與 L3 之間，以下決策以此為前提。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫欄位缺漏）。根據文獻資訊，6-MP 是嘌呤類似物，其硫代鳥嘌呤核苷酸代謝物會嵌入 DNA/RNA 並抑制嘌呤從頭合成，對快速分裂的白血病母細胞具細胞毒性。

此機轉並不限於淋巴性白血病，在骨髓性白血病中同樣可能適用。口服 6-MP 加 methotrexate 的維持治療已用於急性前骨髓細胞白血病（APL）方案，兒童 AML 也曾測試類 ALL 的鞏固治療。不過 APL 本身已屬原適應症，所以此預測部分是原有用途的延伸；對非 APL 的 AML，證據較不充分。此預測分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病間相似性，並非生物學證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02521493](https://clinicaltrials.gov/study/NCT02521493) | Phase 3 | 進行中（不再招募） | 280 | 唐氏症兒童 AML／MDS 的風險分層化療；6-MP 是否為核心成分未明 |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | 招募中 | 10 | Venetoclax 加 6-MP 用於復發／難治 AML，規模很小 |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | 招募中 | 48 | 羥基脲＋丙戊酸，或 6-MP＋丙戊酸，用於不適合標準治療的 AML／高風險 MDS |
| [NCT00492856](https://clinicaltrials.gov/study/NCT00492856) | Phase 3 | 完成 | 105 | 低／中風險 APL 維持治療對比觀察（SWOG S0521） |
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | 完成 | 420 | APL 維持治療比較間歇 tretinoin 與 tretinoin＋6-MP＋methotrexate |
| [NCT00002701](https://clinicaltrials.gov/study/NCT00002701) | Phase 3 | 未知 | 750 | ATRA＋idarubicin，依微量殘存病灶隨機維持治療（APL） |
| [NCT00136084](https://clinicaltrials.gov/study/NCT00136084) | Phase 3 | 完成 | 238 | 新診斷 AML／MDS 兩種 cytarabine 劑量方案比較 |
| [NCT02688140](https://clinicaltrials.gov/study/NCT02688140) | Phase 3 | 完成 | 133 | 高風險 APL：ATO＋ATRA＋idarubicin 對比 AIDA |
| [NCT00482833](https://clinicaltrials.gov/study/NCT00482833) | Phase 3 | 完成 | 276 | 非高風險 APL：ATO＋ATRA 對比 AIDA |
| [NCT00866918](https://clinicaltrials.gov/study/NCT00866918) | Phase 3 | 完成 | 106 | 兒童 APL 於鞏固期使用三氧化二砷 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | 世代研究 | J Korean Med Sci | 不適合移植的 AML 病人使用口服 6-MP＋methotrexate 維持化療 |
| [27275453](https://pubmed.ncbi.nlm.nih.gov/27275453/) | 2016 | 前瞻性先導研究 | South Asian J Cancer | 老年 AML 使用口服 6-MP 的節拍式（metronomic）治療 |
| [38828002](https://pubmed.ncbi.nlm.nih.gov/38828002/) | 2024 | 世代研究 | Ther Adv Hematol | 兒童 AML 採雙重誘導與類 ALL 鞏固的強化化療（中國多中心） |
| [32459546](https://pubmed.ncbi.nlm.nih.gov/32459546/) | 2020 | 回溯性研究 | Pediatr Hematol Oncol | 幼年型骨髓單核球白血病（JMML）接受 cytarabine 與 6-MP 序貫治療的結果 |
| [31283407](https://pubmed.ncbi.nlm.nih.gov/31283407/) | 2019 | Phase 3 隨機研究 | J Clin Oncol | Interfant-06：嬰兒 ALL，比較骨髓性與淋巴性鞏固化療 |
| [22715121](https://pubmed.ncbi.nlm.nih.gov/22715121/) | 2012 | Phase 2 | Blood | APL 使用 ATRA、idarubicin 與靜脈三氧化二砷 |
| [3513537](https://pubmed.ncbi.nlm.nih.gov/3513537/) | 1986 | 臨床研究 | Am J Clin Oncol | 羥基脲與 6-MP 治療慢性顆粒球白血病 |
| [33183436](https://pubmed.ncbi.nlm.nih.gov/33183436/) | 2021 | Review | J Nanosci Nanotechnol | 6-MP 奈米藥物在白血病治療的應用 |
| [2676034](https://pubmed.ncbi.nlm.nih.gov/2676034/) | 1989 | Review | Blood Rev | 嘌呤代謝作為白血病化療標的 |
| [34442422](https://pubmed.ncbi.nlm.nih.gov/34442422/) | 2021 | Review | J Pers Med | NUDT15 多型性對硫嘌呤類治療的重要性 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-03770 | PURI-NETHOL TAB | 未載明（品名為錠劑） | 本報告所用資料未載明 |
| HK-65479 | ALLMERCAP MERCAPTOPURINE ORAL SUSPENSION 20MG/ML | 口服懸液劑（依品名） | 本報告所用資料未載明 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（嘌呤類抗代謝物） |
| 骨髓抑制風險 | 高（知識圖譜記錄嗜中性白血球減少、血小板減少、白血球減少、貧血、顆粒球缺乏等為禁忌關聯；另有文獻指出 NUDT15 與 TPMT 多型性可增加嚴重骨髓抑制風險） |
| 致吐性分級 | 低（依藥物類別判斷） |
| 監測項目 | CBC（含分類）、肝功能（膽紅素、轉胺酶）、腎功能、胰臟酵素；可考慮 TPMT／NUDT15 基因型檢測 |
| 處置防護 | 請依細胞毒性藥物處置規範操作；詳細要求請參考原廠仿單 |

## 安全性考量

- **禁忌症／風險關聯（來自知識圖譜，非仿單文字）**：腎臟疾病、胰臟炎、肝臟疾病、膽囊疾病、血小板減少、嗜中性白血球減少、顆粒球缺乏、貧血、巨球性貧血、高膽紅素血症、Gilbert 症候群、膽汁鬱積、白血球減少、肝脾 T 細胞淋巴瘤等。
- **藥物交互作用**（共查得 100 筆，以下為主要者）：
  - 中度：Mesalazine、Balsalazide、Olsalazine、Sulfasalazine、Naltrexone
  - 輕度：Levofloxacin
  - 其餘如 Prednisone、Omeprazole、Metformin 等為等級未知

香港仿單的警語與禁忌症資料未能取得，其他安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 6-MP 的機轉在骨髓性白血病上合理，且已有直接針對 AML 的小型前瞻性及觀察性研究，以及正在進行的 6-MP 組合 Phase 1/2 試驗。
- 但多數大型試驗無法歸因於 6-MP，APL 又屬原有關聯用途，對非 APL 的 AML 證據仍有限，因此只宜在嚴格監測下作為研究性方向推進。

**若要推進需要：**
- 取得香港仿單的警語、禁忌症與核准適應症文字
- 補充作用機轉資料
- 釐清 NCT02521493 與 NCT00136084 等試驗中 6-MP 的實際角色
- 追蹤 NCT05506332、NCT06199557 的結果
- 建立血液學監測與 TPMT／NUDT15 基因檢測計畫

---

**其他預測適應症（簡要）：** Hodgkin 淋巴瘤（L4，現有試驗皆為其他淋巴瘤或白血病，無直接證據，建議 Hold）；小細胞肺癌（僅有 1985 年單一藥物 Phase 2 研究，已非現行標準治療，建議 Hold）；慢性淋巴性白血病／小淋巴球淋巴瘤、肺母細胞瘤、原發性肺淋巴瘤、肺部高分化胎兒型腺癌等，目前無直接支持證據，僅為模型預測，建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

