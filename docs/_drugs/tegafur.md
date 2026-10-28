---
layout: default
title: Tegafur
parent: 高證據等級 (L1-L2)
nav_order: 852
evidence_level: L1
indication_count: 10
monitor_inn: "TEGAFUR"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "cecum neuroendocrine tumor G1", "lipoma of colon", "cecal disease", "colon leiomyoma", "benign neoplasm of cecum", "rectosigmoid junction neoplasm", "colonic lymphangioma", "cavernous hemangioma of colon"]
last_modified_at: 2026-10-28
description: "Tegafur：預測新適應症為大腸腫瘤（證據等級 L1）。原適應症：胃癌"
---

# Tegafur
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

## Tegafur：從胃癌到大腸腫瘤
{: .text-alpha }

## 一句話總結

Tegafur 是 5-氟尿嘧啶（5-FU）的口服前驅藥，知識圖譜中記錄的原適應症為胃癌。
TxGNN 模型預測它可能對**大腸腫瘤 (colonic neoplasm)** 有效，
目前有 **17 個臨床試驗**和 **20 篇文獻**支持這個方向，其中包含多項已完成的 Phase 3 隨機對照試驗。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃癌（知識圖譜記錄；香港許可證資料未提供核准適應症文字） |
| 預測新適應症 | 大腸腫瘤 |
| TxGNN 預測分數 | 0.9990 |
| 證據等級 | L1 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 許可證數 | 6 張（有效 6 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。以下根據一般藥理知識說明：Tegafur 是 5-FU 的口服前驅藥，主要經肝臟 CYP2A6 轉換為 5-FU。5-FU 屬於氟嘧啶類抗代謝藥物，可抑制胸苷酸合成酶（thymidylate synthase），並嵌入 RNA/DNA。

這個機轉並不限於胃組織，因此直接適用於大腸直腸腺癌，而氟嘧啶本來就是大腸直腸癌的核心治療。與尿嘧啶合用（UFT）可抑制 DPD 對 5-FU 的分解；與 leucovorin 合用則可穩定 TS 抑制複合物。

需要注意的是，UFT/LV 用於大腸癌在多個地區已有臨床使用經驗，因此這更接近「適應症延伸」，而非全新的藥物再利用訊號。

## 臨床試驗證據

以下列出最相關的 10 個試驗（其餘試驗未列出）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00378716](https://clinicaltrials.gov/study/NCT00378716) | Phase 3 | 完成 | 1608 | UFT+LV 對比 5-FU+LV，用於第 II/III 期結腸癌術後輔助治療 |
| [NCT00152230](https://clinicaltrials.gov/study/NCT00152230) | Phase 3 | 完成 | 900 | 術後輔助 UFT 對比單純手術，用於 Dukes C 大腸直腸癌 |
| [NCT00392899](https://clinicaltrials.gov/study/NCT00392899) | Phase 3 | 完成 | 2025 | UFT 輔助化療對比觀察，用於第 II 期結腸癌 |
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Phase 3 | 完成 | 1535 | UFT+LV 對比 TS-1，用於第 III 期結腸癌輔助治療 |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Phase 3 | 狀態未知 | 1191 | SOX（S-1+oxaliplatin）對比 XELOX，用於第 III 期大腸直腸癌輔助治療 |
| [NCT00385970](https://clinicaltrials.gov/study/NCT00385970) | Phase 3 | 狀態未知 | 380 | UFT+PSK 對比 UFT+LV，用於第 IIB/III 期大腸直腸癌 |
| [NCT00209742](https://clinicaltrials.gov/study/NCT00209742) | Phase 3 | 狀態未知 | 340 | 比較三種 UFT 為基礎的術後方案，用於第 III 期大腸直腸癌 |
| [NCT00905047](https://clinicaltrials.gov/study/NCT00905047) | Phase 3 | 完成 | 89 | Xeloda 對比 UFT/亞葉酸的患者偏好交叉試驗，用於晚期或轉移性大腸直腸癌 |
| [NCT00004860](https://clinicaltrials.gov/study/NCT00004860) | Phase 2 | 完成 | 未提供 | UFT+leucovorin 用於 75 歲以上轉移性大腸直腸癌患者 |
| [NCT01225744](https://clinicaltrials.gov/study/NCT01225744) | Phase 2 | 完成 | 47 | cetuximab、irinotecan、oxaliplatin 加 UFT，用於轉移性大腸直腸癌第一線治療 |

註：多數試驗為含 tegafur 的組合方案（UFT 或 S-1），並非 tegafur 單一成分的試驗。

## 文獻證據

以下列出最相關的 10 篇（RCT 優先，其次為統合分析與回顧）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | RCT | Clin Colorectal Cancer | ACTS-CC 02：SOX 對比 UFT/LV，用於高風險第 III 期結腸癌輔助治療 |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | RCT | ESMO Open | ACTS-CC 02 五年更新：SOX 在無病存活期上未優於 UFT/LV |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | 世代研究與統合分析 | Medicine | 以台灣健保資料庫比較 UFT 與 5-FU 作為第 II/III 期結腸癌術後輔助治療 |
| [27056996](https://pubmed.ncbi.nlm.nih.gov/27056996/) | 2016 | RCT | Ann Oncol | ACTS-RC：S-1 對比 UFT，用於第 II/III 期直腸癌輔助治療 |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | RCT | Int J Clin Oncol | OK-432 與口服嘧啶類（含 UFT）不同組合用於大腸直腸癌輔助治療 |
| [10089948](https://pubmed.ncbi.nlm.nih.gov/10089948/) | 1999 | 統合分析 | Jpn J Clin Oncol | 口服氟嘧啶類作為大腸直腸癌術後輔助治療的個別病患資料統合分析 |
| [36676634](https://pubmed.ncbi.nlm.nih.gov/36676634/) | 2022 | 世代研究 | Medicina | UFT 作為第 IIA 期結腸癌術後輔助治療的效益 |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surg Today | UFT 作為多種實體瘤術後輔助化療的臨床證據與機轉 |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | 共識指引 | Clin Colorectal Cancer | 亞洲轉移性大腸直腸癌治療指引 |
| [16111469](https://pubmed.ncbi.nlm.nih.gov/16111469/) | 2005 | Review | Expert Rev Anticancer Ther | 結腸癌分期別化療選項 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60904 | UFUR CAP | 膠囊 | 資料未提供 |
| HK-48265 | UNITORAL CAP | 膠囊 | 資料未提供 |
| HK-61181 | TS-ONE 25 CAP | 膠囊 | 資料未提供 |
| HK-67976 | TEGO CAPSULES 20MG/5.8MG/19.6MG | 膠囊 | 資料未提供 |
| HK-67977 | TEGO CAPSULES 25MG/7.25MG/24.5MG | 膠囊 | 資料未提供 |

另有 HK-61182（TS-ONE 20 CAP），共 6 張有效許可證。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（氟嘧啶類抗代謝藥物，5-FU 前驅藥） |
| 骨髓抑制風險 | 中度（一般氟嘧啶類的已知風險；文獻亦有 UFT 引起溶血性貧血的個案報告） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類）、肝腎功能、電解質 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

請同時參考原廠仿單的警語與注意事項。

## 安全性考量

安全性資訊請參考原廠仿單。

另外，文獻中有與 UFT/S-1 相關的個案報告，包括溶血性貧血與 S-1 引起的高三酸甘油酯血症，臨床使用時可留意。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多項已完成的大型 Phase 3 RCT（如 NCT00378716、NCT00152230、NCT00392899、NCT00660894）直接在結腸癌／大腸直腸癌中研究含 tegafur 的方案，證據等級為 L1。
- 但多數為 UFT 或 S-1 組合方案，無法直接歸因於 tegafur 單一成分；香港許可證資料也未提供核准適應症文字，且作用機轉與安全性資料仍有缺口。

**若要推進需要：**
- 取得香港衛生署許可證的仿單，確認核准適應症、警語與禁忌
- 補齊 tegafur 的作用機轉資料（如 DrugBank）
- 釐清各許可證產品是單方或複方成分，以及與試驗方案的對應
- 建立血液學與肝腎功能監測及 DPD 缺乏等特定族群的安全性計畫

**其他預測適應症說明：** 排名 2–10 的預測（如盲腸絨毛狀腺瘤、結腸脂肪瘤、結腸血管瘤等）多為良性病變，缺乏直接證據，宜維持 Hold；「盲腸疾病」與「直腸乙狀結腸交界腫瘤」僅有間接的個案報告，建議併入大腸直腸癌一併評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

