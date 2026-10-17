---
layout: default
title: Ribavirin
parent: 僅模型預測 (L5)
nav_order: 768
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ribavirin：預測新適應症為慢性 B 型肝炎病毒感染 (chronic hepatitis B virus infection)（證據等級 L5）。原適應症：慢性 C 型肝炎、C 型肝炎病毒感染、呼吸道融合病毒感染"
monitor_inn: "RIBAVIRIN"
predicted_indications: ["primitive portal vein thrombosis", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "hepatoportal sclerosis"]
---

# Ribavirin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ribavirin：從慢性 C 型肝炎到慢性 B 型肝炎

## 一句話總結

Ribavirin 是一種核苷類似物抗病毒藥，原本用於慢性 C 型肝炎與呼吸道融合病毒感染。
TxGNN 模型預測它可能對**慢性 B 型肝炎病毒感染 (chronic hepatitis B virus infection)** 有效，
目前有 **14 個臨床試驗**和 **20 篇文獻**與此方向相關，但多數屬於 C 型肝炎研究或間接證據，直接證據有限。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性 C 型肝炎、C 型肝炎病毒感染、呼吸道融合病毒感染（香港許可證未載明適應症文字） |
| 預測新適應症 | 慢性 B 型肝炎病毒感染 (chronic hepatitis B virus infection) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L2（僅 1 個已完成的 Phase 3 試驗直接針對 B 型肝炎，其餘 B 型肝炎相關試驗為小型先導或狀態未知） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

> 註：資料中系統給定的證據等級為 L1，但依本報告的判定規則，直接針對 B 型肝炎且已完成的 Phase 3 試驗僅 NCT00114361 一項，因此本報告評為 L2。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。就已知資訊，Ribavirin 是鳥苷核苷類似物，具廣譜抗病毒活性，可能的作用包括抑制 IMPDH、耗竭 GTP 池及免疫調節。

Ribavirin 對 B 型肝炎病毒的直接抗病毒作用較弱。較合理的角色是作為 peginterferon 的免疫調節輔助（增強 Th1 反應、調節干擾素刺激基因）。目前 B 型肝炎的標準治療仍是核苷(酸)類似物（如 entecavir、tenofovir），Ribavirin 並無既定的單用或常規加用角色。

此外，許多相關試驗收錄的是 C 型肝炎或 B/C 型共同感染患者，很難分離出 Ribavirin 對 B 型肝炎的單獨貢獻。

## 臨床試驗證據

以下列出與 B 型肝炎關聯較高的試驗（共 14 個，此處列 10 個）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | 完成 | 138 | PEG-IFN 加 Ribavirin 對比 PEG-IFN 單用，用於 HBeAg 陰性慢性 B 型肝炎（PARC 試驗），直接相關 |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | 完成 | 120 | 干擾素 alpha-2b 加 Ribavirin 用於慢性肝炎的先導研究 |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Phase 3 | 未知 | 24 | 探討 Ribavirin 的免疫調節作用，與 B 型肝炎核苷類似物併用的先導試驗 |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | 未知 | 320 | Peginterferon 加 Ribavirin 用於 C 型/B 型肝炎共同感染 |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Phase 4 | 未知 | 20 | Peginterferon alfa-2b 加 Ribavirin 用於 B 型合併 D 型肝炎的先導研究 |
| [NCT02219477](https://clinicaltrials.gov/study/NCT02219477) | Phase 3 | 完成 | 36 | 直接作用抗病毒藥加 Ribavirin 用於 C 型肝炎失代償性肝硬化，對 B 型肝炎為間接證據 |
| [NCT01447420](https://clinicaltrials.gov/study/NCT01447420) | Phase 4 | 完成 | 129 | IL-28B 表現與 C 型肝炎持續病毒學反應，與 B 型肝炎關聯低 |
| [NCT01195181](https://clinicaltrials.gov/study/NCT01195181) | Phase 4 | 完成 | 506 | C 型肝炎監測與照護改善計畫，非 Ribavirin 對 B 型肝炎的療效試驗 |
| [NCT01795911](https://clinicaltrials.gov/study/NCT01795911) | Phase 2 | 完成 | 165 | Peginterferon lambda 合併 Ribavirin 用於 C 型肝炎，B 型肝炎為間接證據 |
| [NCT03186313](https://clinicaltrials.gov/study/NCT03186313) | Phase 3 | 完成 | 72 | Sofosbuvir、Daclatasvir 加 Ribavirin 複方用於埃及 C 型肝炎基因型 4 |

## 文獻證據

文獻多為綜述，未檢索到針對 Ribavirin 治療 B 型肝炎的 RCT。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | C 型/B 型肝炎共同感染的處置，HCV RNA 陽性者曾建議 pegIFN 加 Ribavirin |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | 雙重 HCV/HBV 感染的治療與預後更新 |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Review | Hepatology | B 型/C 型肝炎抗病毒治療的免疫學層面 |
| [25232239](https://pubmed.ncbi.nlm.nih.gov/25232239/) | 2014 | Review | World J Gastroenterol | IL28B 基因多型性與 B 型肝炎感染 |
| [24379612](https://pubmed.ncbi.nlm.nih.gov/24379612/) | 2013 | Review | World J Gastroenterol | 慢性 B 型/C 型肝炎的肝癌預防 |
| [16838649](https://pubmed.ncbi.nlm.nih.gov/16838649/) | 2006 | Review | Nihon Rinsho | HCV-HBV 重複感染 |
| [17009938](https://pubmed.ncbi.nlm.nih.gov/17009938/) | 2006 | Review | Expert Rev Anti Infect Ther | 兒童慢性 B 型/C 型肝炎的治療選擇 |
| [29415584](https://pubmed.ncbi.nlm.nih.gov/29415584/) | 2018 | Review | Expert Rev Anti Infect Ther | 血液病患者慢性病毒性肝炎的處置 |
| [11929032](https://pubmed.ncbi.nlm.nih.gov/11929032/) | 2002 | Review | Indian J Pediatr | B 型/C 型肝炎感染的處置 |
| [11005078](https://pubmed.ncbi.nlm.nih.gov/11005078/) | 2000 | Review | J R Coll Physicians Lond | 病毒性肝炎概述 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-37449 | ROBAVIN CAP 100MG | 未記載 | 未記載 |

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物與疾病關聯資料，並非仿單原文）：慢性阻塞性肺病、肝硬化、氣喘、類肉瘤病、鐮刀型貧血、心肌梗塞、冠狀動脈疾病、動脈粥樣硬化、各類貧血（含溶血性貧血）、全血球低下、間質性肺病、腎功能不全、胰臟炎、自體免疫性肝炎、牙周炎等。其中貧血／溶血與心血管疾病是 Ribavirin 臨床上需特別留意的面向。
- **藥物交互作用**：資料庫共收錄 100 筆交互作用，但嚴重程度皆標示為「未知」，例如 Calcitriol、Pantoprazole、Glimepiride、Metformin、Prednisone、Amphotericin B 等，無法據此評估風險高低。
- 與干擾素合併使用時，需留意肺部不良反應（見肝肺症候群項下的個案報告）。

其餘警語與禁忌症請參考原廠仿單。

## 其他預測適應症

其餘四項預測（原發性門靜脈血栓、肝肺症候群、早發家族性非肝硬化門脈高壓、肝門脈硬化症）均無臨床試驗，亦無支持的作用機轉，僅為圖譜近鄰所致的預測，且 Ribavirin 引起溶血反而可能是疑慮。這些方向皆建議 **Hold**。

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一直接針對 B 型肝炎且已完成的 Phase 3 試驗（PARC，NCT00114361）顯示的結果在資料中並未提供，其餘多為 C 型肝炎的間接證據或小型先導研究。
- Ribavirin 直接抗 B 型肝炎活性弱，標準治療（entecavir、tenofovir）已相當有效，且 Ribavirin 有溶血等安全性疑慮，難以支持推進。

**若要推進需要：**
- 取得 PARC 試驗（NCT00114361）的完整結果，確認 Ribavirin 相對於 PEG-IFN 單用的增益
- 追蹤 NCT03759782（Ribavirin 加核苷類似物）的結果
- 補齊作用機轉資料與香港仿單的警語及禁忌症
- 與現行標準治療比較，並規劃貧血／溶血的監測方案
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

