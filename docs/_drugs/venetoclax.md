---
layout: default
title: Venetoclax
parent: 中證據等級 (L3-L4)
nav_order: 930
evidence_level: L4
indication_count: 5
---

# Venetoclax
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Venetoclax：從急性淋巴性白血病與 Richter 症候群到骨髓性白血病

## 一句話總結

Venetoclax 是一種口服 BCL-2 抑制劑，原本用於急性淋巴性白血病（acute lymphoblastic/lymphocytic leukemia）與 Richter 症候群。
TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效，目前有 **約 35 個相關臨床試驗**（含 3 個 Phase 3）和 **18 篇文獻**支持這個方向。

> 說明：模型共預測 5 個新適應症。本報告以排名第 1 的預測為主軸（見下方快速總覽），並在文末整理其餘預測的證據強弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性淋巴性白血病、Richter 症候群（來自知識圖譜；香港許可證未載明核准適應症文字） |
| 預測新適應症（排名第 1） | 前生發中心慢性淋巴球性白血病/小淋巴球淋巴瘤 (pregerminal center CLL/SLL) |
| TxGNN 預測分數 | 99.55% |
| 證據等級（排名第 1） | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

其他預測新適應症概況：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | 前生發中心 CLL/SLL | 99.55% | L4 | Hold |
| 2 | IGHV 突變型 CLL/SLL | 99.55% | L5 | Hold |
| 3 | 何杰金氏淋巴瘤 | 99.51% | L3 | 研究性問題 |
| 4 | 骨髓性白血病 | 99.47% | L1 | Proceed with Guardrails |
| 5 | BCR-ABL1 陽性慢性骨髓性白血病 | 99.36% | L2 | 研究性問題 |

以證據最完整的**骨髓性白血病（排名第 4）**而言，建議決策為 **Proceed with Guardrails**。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）欄位資料。根據文獻，venetoclax 是選擇性 BCL-2 抑制劑，可恢復惡性細胞的粒線體凋亡路徑。

CLL/SLL 細胞依賴 BCL-2 過度表現存活，因此機轉上合理。不過排名第 1、2 的項目屬於 CLL/SLL 的亞型，目前僅有一篇討論 B 細胞受體結構的文獻，屬間接生物學背景，沒有亞型專屬的臨床資料。

骨髓性白血病的機轉支持度較高：AML 母細胞與白血病幹細胞依賴 BCL-2 與粒線體凋亡啟動狀態，與去甲基化藥物（azacitidine、decitabine）併用時可干擾白血病幹細胞的氧化磷酸化。文獻也記載了抗藥機制（如 MCL-1 依賴、選殖演化）。對 BCR-ABL1 陽性 CML，BCL-2 同樣參與 TKI 治療下殘存祖細胞的存活，與 dasatinib、ponatinib 併用在機轉上合理。

---

## 臨床試驗證據

排名第 1、2 的預測無相關臨床試驗登記。以下列出證據最完整的**骨髓性白血病**之主要試驗（共 35 筆，列出相關性較高的 10 筆）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06852222](https://clinicaltrials.gov/study/NCT06852222) | Phase 3 | 招募中 | 600 | Bleximenib + venetoclax + azacitidine 對比安慰劑組，用於 NPM1/KMT2A 異常的新診斷 AML（尚無結果） |
| [NCT04708054](https://clinicaltrials.gov/study/NCT04708054) | Phase 2/3 | 招募中 | 324 | Venetoclax 加入分次 busulfan 方案，用於高風險 AML/MDS 移植 |
| [NCT05177731](https://clinicaltrials.gov/study/NCT05177731) | Phase 3 | 進行中（不招募） | 188 | Venetoclax + decitabine 對比傳統 7+3 誘導化療（年輕成人 AML） |
| [NCT07132684](https://clinicaltrials.gov/study/NCT07132684) | Phase 3 | 招募中 | 240 | VA 對比 D/IA 誘導方案（55–75 歲適合強化化療的 AML） |
| [NCT02250937](https://clinicaltrials.gov/study/NCT02250937) | Phase 2 | 進行中（不招募） | 116 | Venetoclax 搭配 busulfan、cladribine、fludarabine 移植前處置 |
| [NCT03471260](https://clinicaltrials.gov/study/NCT03471260) | Phase 1b/2 | 招募中 | 96 | Ivosidenib + venetoclax ± azacitidine，用於 IDH1 突變骨髓惡性腫瘤 |
| [NCT06696183](https://clinicaltrials.gov/study/NCT06696183) | Phase 2 | 招募中 | 60 | 序貫 gilteritinib + venetoclax + azacitidine（FLT3 突變 AML） |
| [NCT06429098](https://clinicaltrials.gov/study/NCT06429098) | Phase 2 | 進行中（不招募） | 40 | Venetoclax 為基礎的無 anthracycline 方案（CBFβ::MYH11 AML） |
| [NCT03844815](https://clinicaltrials.gov/study/NCT03844815) | Phase 1 | 進行中（不招募） | 26 | Venetoclax + 10 日 decitabine 方案的安全性與耐受性 |
| [NCT07228273](https://clinicaltrials.gov/study/NCT07228273) | Phase 2 | 招募中 | 102 | Venetoclax + FLAG-IDA 對比標準誘導／鞏固治療 |

補充：BCR-ABL1 陽性 CML 另有 [NCT02689440](https://clinicaltrials.gov/study/NCT02689440)（Phase 2，n=155，dasatinib + venetoclax，早期慢性期）與 [NCT04188405](https://clinicaltrials.gov/study/NCT04188405)（Phase 2，已完成，n=20，decitabine + venetoclax + ponatinib）。

---

## 文獻證據

骨髓性白血病相關文獻（列出 10 篇）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29339097](https://pubmed.ncbi.nlm.nih.gov/29339097/) | 2018 | Phase 1b | Lancet Oncol | Venetoclax 併用 decitabine 或 azacitidine 用於年長未治療 AML，顯示安全性與初步療效 |
| [35046058](https://pubmed.ncbi.nlm.nih.gov/35046058/) | 2022 | 亞組分析 | Clin Cancer Res | Venetoclax + azacitidine 用於 IDH1/2 突變、未治療的 AML |
| [39303729](https://pubmed.ncbi.nlm.nih.gov/39303729/) | 2024 | Phase 2 | Lancet Haematol | Decitabine + venetoclax + ponatinib 用於進展期 Ph+ 骨髓疾病 |
| [40913104](https://pubmed.ncbi.nlm.nih.gov/40913104/) | 2025 | 事後分析 | Leukemia | VIALE-A 等研究中，venetoclax + azacitidine 對比 azacitidine 單用，依年齡與風險分層 |
| [31932844](https://pubmed.ncbi.nlm.nih.gov/31932844/) | 2020 | 分子分析 | Blood | 年長 AML 接受 venetoclax 組合後，反應與治療失敗的分子模式 |
| [42035228](https://pubmed.ncbi.nlm.nih.gov/42035228/) | 2026 | Phase 2 | Am J Hematol | Cladribine + 低劑量 cytarabine + venetoclax 與 azacitidine + venetoclax 交替（n=190） |
| [28161120](https://pubmed.ncbi.nlm.nih.gov/28161120/) | 2017 | PK/DDI | Clin Ther | Venetoclax 與 posaconazole 交互作用及劑量調整 |
| [37925935](https://pubmed.ncbi.nlm.nih.gov/37925935/) | 2023 | Review | Biomed Pharmacother | Venetoclax 在成人 AML 的整體回顧 |
| [38866760](https://pubmed.ncbi.nlm.nih.gov/38866760/) | 2024 | Review | Cell Death Dis | Venetoclax 抗藥機制回顧 |
| [31048321](https://pubmed.ncbi.nlm.nih.gov/31048321/) | 2019 | 前臨床 | Cancer Discov | 靶向粒線體結構可使 AML 對 venetoclax 更敏感 |

排名第 1 的 CLL/SLL 亞型僅有一篇文獻：[35158929](https://pubmed.ncbi.nlm.nih.gov/35158929/)（2022，Cancers，回顧 CLL 腫瘤 B 細胞受體結構與功能，屬間接證據）。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65283 | VENCLEXTA TABLETS 50MG | — | 未提供 |
| HK-65285 | VENCLEXTA TABLETS 100MG | — | 未提供 |
| HK-65284 | VENCLEXTA TABLETS 10MG | — | 未提供 |

製造商均為 ABBVIE LIMITED，3 張皆為有效的單一成分許可證。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（選擇性 BCL-2 抑制劑），非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 文獻指出腫瘤溶解症候群與骨髓抑制為最常見的不良事件；與化療或去甲基化藥物併用時更需注意 |
| 監測項目 | CBC（含分類）、腫瘤溶解症候群相關檢驗（電解質、尿酸、腎功能） |

致吐性分級與處置防護請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **藥物交互作用**：已完成查詢，共 100 筆交互作用紀錄，以下為部分主要項目：
  - **Major**：Aprepitant、Dexamethasone、Clarithromycin、Eliglustat、Rolapitant、Fidaxomicin、Cobicistat、Deferiprone、Samarium (153Sm) lexidronam
  - **Moderate**：Alvimopan、Loperamide、Cimetidine、Naldemedine、Metreleptin、Miconazole、Rifaximin、Clotrimazole、Troglitazone、Deferasirox
  - **Minor**：Naloxegol
- 文獻佐證：posaconazole 等強效 CYP3A 抑制劑會提高 venetoclax 暴露量，需調整劑量（PMID 28161120）。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（排名第 1 的預測）；整體建議對骨髓性白血病（AML）方向 Proceed with Guardrails**

**理由：**
- 排名第 1、2 的 CLL/SLL 亞型僅有模型預測與一篇間接文獻，沒有亞型專屬的臨床資料，宜暫緩。
- 骨髓性白血病有多個 Phase 2/3 試驗、Phase 1b/2 研究及機轉文獻支持，但目前多為進行中或組合療法試驗，尚無已完成的 Phase 3 結果可直接歸功於 venetoclax，故需附帶防護措施。何杰金氏淋巴瘤與 CML 的證據多為間接或單臂組合研究，維持為研究性問題。

**若要推進需要：**
- 取得香港原廠仿單，確認核准適應症、警語與禁忌症
- 補充 DrugBank 的作用機轉資料
- 確認 Phase 3 試驗（如 NCT06852222、NCT05177731）的完成結果
- 制定 DDI 管理（強效 CYP3A 抑制劑需調整劑量）及腫瘤溶解症候群、骨髓抑制監測計畫
- 針對何杰金氏淋巴瘤，需確認試驗中是否有專屬的何杰金氏淋巴瘤族群
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

