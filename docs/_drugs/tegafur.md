---
layout: default
title: Tegafur
parent: 高證據等級 (L1-L2)
nav_order: 837
evidence_level: L1
indication_count: 5
---

# Tegafur
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

# Tegafur：大腸腫瘤的預測與證據評估

## 一句話總結

Tegafur 是口服 5-FU 前驅藥，常與 uracil（UFT）或 gimeracil/oteracil（S-1）組成複方，用於消化道腫瘤化療。
TxGNN 模型預測它可能對**大腸腫瘤 (Colonic Neoplasm)** 有效，目前有 **28 個臨床試驗**和 **20 篇文獻**支持這個方向。
其中多項已完成的 Phase 3 試驗直接檢驗含 tegafur 的方案。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 大腸腫瘤 (Colonic Neoplasm) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Tegafur 是 5-FU 的口服前驅藥，主要經肝臟 CYP2A6 轉換為 5-FU。5-FU 會抑制胸苷酸合成酶（thymidylate synthase），也會嵌入 RNA 與 DNA，這是 5-FU 在大腸直腸癌中的既有細胞毒性機轉。目前缺乏 DrugBank 的詳細作用機轉資料，以上機轉說明來自已知藥理知識。

這項預測更可能是資料缺口，而不是真正的老藥新用。本次輸入中原適應症欄位為空，香港許可證也沒有核准適應症文字。但含 tegafur 的複方（UFT、S-1）早已用於大腸直腸癌，例如術後輔助化療。因此模型的高分與既有臨床實務一致。要把這視為新適應症主張前，應先核對香港衛生署的許可證標示。

## 臨床試驗證據

共檢索到 28 項相關試驗，其中 6 項為已完成的 Phase 3。以下列出最相關的 10 項。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | 完成 | 2025 | UFT 對比單純觀察，用於根除性切除後的 Stage II 結腸癌輔助治療 |
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | 完成 | 1608 | UFT+LV 對比 5-FU+LV，用於 Stage II/III 結腸癌 |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 完成 | 1535 | UFT+LV 對比 S-1，用於 Stage III 結腸癌輔助治療 |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | 完成 | 900 | UFT 對比單純手術，用於 Dukes C 大腸直腸癌（NSAS-CC） |
| [NCT01918852](https://clinicaltrials.gov/study/NCT01918852) | Phase 3 | 完成 | 161 | S-1 對比 capecitabine，用於轉移性大腸直腸癌第一線治療（SALTO） |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Phase 3 | 完成 | 89 | Xeloda 與 UFT+亞葉酸交叉試驗，以病人偏好為主要終點，僅供輔助參考 |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 狀態未知 | 1191 | SOX 對比 XELOX，用於 Stage III 大腸直腸癌輔助化療 |
| [NCT00209742](https://clinicaltrials.gov/study/NCT00209742) | Phase 3 | 狀態未知 | 340 | 比較 UFT+LV、UFT+LV/UFT、UFT+LV+PSK 三種術後方案，用於 Stage III 大腸直腸癌 |
| [NCT00497107](https://clinicaltrials.gov/study/NCT00497107) | Phase 3 | 狀態未知 | 300 | UFT/LV 對比 UFT/LV+PSK，用於 Stage III 大腸直腸癌，主要終點為 3 年無病存活 |
| [NCT00004860](https://clinicaltrials.gov/study/NCT00004860) | Phase 2 | 完成 | 未提供 | UFT+亞葉酸用於 75 歲以上轉移性大腸直腸癌，為單臂試驗 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT (Phase 3) | Clin Colorectal Cancer | ACTS-CC 02：驗證 SOX 對比 UFT/LV 用於高風險 Stage III 結腸癌輔助治療的優越性 |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT (Phase 3) | ESMO Open | ACTS-CC 02 的 5 年更新：SOX 在無病存活上未優於 UFT/LV |
| [16648506](https://pubmed.ncbi.nlm.nih.gov/16648506/) | 2006 | 隨機試驗 | J Clin Oncol | NSABP C-06：比較口服 UFT+LV 與靜脈 5-FU+LV 用於 Stage II/III 結腸癌的無病存活與整體存活 |
| [26347106](https://pubmed.ncbi.nlm.nih.gov/26347106/) | 2015 | RCT (Phase 3) | Ann Oncol | JFMC33-0502：探討 UFT/LV 輔助治療 Stage IIB/III 結腸癌的最適療程長度 |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | 比較 OK-432 與口服嘧啶類藥物（含 UFT）的不同組合，用於大腸直腸癌輔助治療 |
| [6402917](https://pubmed.ncbi.nlm.nih.gov/6402917/) | 1983 | 隨機比較研究 | Am J Clin Oncol | 口服 tegafur 對比靜脈 5-FU，用於轉移性大腸直腸癌 |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surg Today | UFT 用於肺、胃、大腸直腸及乳癌術後輔助化療的臨床證據與作用機轉 |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | 世代研究＋統合分析 | Medicine | 以台灣健保資料庫比較 UFT 與 5-FU 用於 Stage II/III 結腸癌輔助化療的無病存活與整體存活 |
| [35168560](https://pubmed.ncbi.nlm.nih.gov/35168560/) | 2022 | 前瞻性觀察研究 | BMC Cancer | JFMC46-1201：以傾向分數配對，比較 UFT/LV 與單純手術用於高風險 Stage II 結腸癌 |
| [38833114](https://pubmed.ncbi.nlm.nih.gov/38833114/) | 2024 | 前瞻性對照研究 | Int J Clin Oncol | JFMC46-1201 最終分析：納入 5 年整體存活與風險因子分析 |

## 香港上市資訊

共 6 張許可證，列出其中 5 張。資料中沒有劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-60904 | UFUR CAP | HIND WING CO LTD |
| HK-48265 | UNITORAL CAP | HEALTHCARE PHARMASCIENCE LIMITED |
| HK-61181 | TS-ONE 25 CAP | DKSH HONG KONG LIMITED |
| HK-67976 | TEGO CAPSULES 20MG/5.8MG/19.6MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-67977 | TEGO CAPSULES 25MG/7.25MG/24.5MG | LOTUS PHARMACEUTICAL HK LIMITED |

## 細胞毒性

以下為依藥物類別的一般判斷，並非來自 DrugBank 毒性資料。實際內容請以原廠仿單為準。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Fluoropyrimidine 類，5-FU 前驅藥） |
| 骨髓抑制風險 | 中度 |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類）、肝腎功能；用藥前可考慮 DPYD 基因型檢測 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 至少有 6 項已完成的 Phase 3 試驗與多篇 RCT 文獻，直接檢驗含 tegafur 的方案用於結腸或大腸直腸癌，證據等級為 L1。
- 目前缺少香港許可證的適應症與仿單安全資料，且這項預測可能只是既有適應症的重複，因此需設護欄。

**若要推進需要：**
- 取得香港衛生署的仿單與核准適應症，確認大腸直腸癌是否已在標示內，以判斷是否算新適應症。
- 補齊警語與禁忌症，並評估 DPD 缺乏與 CYP2A6 變異。
- 評估藥物交互作用，例如 warfarin、phenytoin。
- 補充 DrugBank 的作用機轉資料。
- 其他預測項目（盲腸絨毛腺瘤、盲腸神經內分泌腫瘤 G1、結腸脂肪瘤）缺乏臨床證據，且機轉上不合理，建議 Hold。
- 「盲腸疾病」僅有病例報告等間接證據，與大腸腫瘤重複，建議併入大腸腫瘤並改對應到更具體的疾病詞條。

> 本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

