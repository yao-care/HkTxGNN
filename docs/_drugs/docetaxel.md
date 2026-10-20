---
layout: default
title: Docetaxel
parent: 高證據等級 (L1-L2)
nav_order: 288
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Docetaxel：預測新適應症為女性乳癌 (Female Breast Carcinoma)（證據等級 L1）。原適應症：非小細胞肺癌、前列腺癌、頭頸癌、胃癌、乳癌等"
monitor_inn: "DOCETAXEL"
predicted_indications: ["Ewing sarcoma", "well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "pulmonary blastoma", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma"]
---

# Docetaxel
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

# Docetaxel：從多種實體腫瘤到女性乳癌

## 一句話總結

Docetaxel（歐洲紫杉醇類藥物）原本用於非小細胞肺癌、前列腺癌、頭頸癌、胃癌與乳癌等治療。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，
目前有 **40 個臨床試驗**和 **20 篇文獻**支持這個方向。
需要說明的是，乳癌本身已是 docetaxel 的既有適應症，因此這項預測更接近對既有用途的驗證，而非真正的新用途。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌、前列腺癌、頭頸癌、胃癌、乳癌等（香港許可證未提供適應症文字，此處依知識圖譜適應症關聯） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，docetaxel 是一種微管穩定型紫杉烷類藥物，能造成有絲分裂停滯並誘導快速分裂細胞凋亡。

乳癌已是 docetaxel 的既有適應症，因此高預測分數與其已確立的機轉和臨床用途一致。文獻中也有綜述指出，docetaxel 最初即是為乳癌開發，並在肺癌等其他腫瘤展現高度活性。

其他排名較前的預測疾病（如 Ewing 肉瘤、橫紋肌肉瘤）多半是以 gemcitabine 併用的方式使用，效果有限；肺部罕見腫瘤則僅有個案報告，證據明顯弱於乳癌。

---

## 臨床試驗證據

資料共列出 40 個與乳癌相關的試驗，以下依相關性挑選 10 個：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00021255](https://clinicaltrials.gov/study/NCT00021255) | Phase 3 | 完成 | 3222 | 輔助治療 HER2 陽性乳癌：AC-T、AC-TH 與 TCH（docetaxel + carboplatin + trastuzumab）比較 |
| [NCT00003782](https://clinicaltrials.gov/study/NCT00003782) | Phase 3 | 完成 | 5351 | 腋下淋巴結陽性乳癌輔助治療：AC-T、AT、ATC 三組比較 |
| [NCT00003519](https://clinicaltrials.gov/study/NCT00003519) | Phase 3 | 完成 | 2778 | 輔助治療：Adriamycin/Taxotere 對比 Adriamycin/Cytoxan |
| [NCT00002707](https://clinicaltrials.gov/study/NCT00002707) | Phase 3 | 完成 | 2411 | 術前 AC 加或不加 docetaxel（術前或術後）用於可手術乳癌 |
| [NCT00333775](https://clinicaltrials.gov/study/NCT00333775) | Phase 3 | 完成 | 736 | Bevacizumab 併用 docetaxel 對比 docetaxel 加安慰劑，用於 HER2 陰性轉移性乳癌第一線 |
| [NCT00887536](https://clinicaltrials.gov/study/NCT00887536) | Phase 3 | 完成 | 1613 | TC 加 bevacizumab 對比 TC 單獨及 TAC，用於高風險 HER2 陰性乳癌 |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | 完成 | 652 | 紫杉烷化療併用 lapatinib 或 trastuzumab，用於 HER2 陽性轉移性乳癌第一線 |
| [NCT03588091](https://clinicaltrials.gov/study/NCT03588091) | Phase 3 | 完成 | 355 | 新輔助 pyrotinib + trastuzumab + docetaxel 對比安慰劑組合 |
| [NCT00431080](https://clinicaltrials.gov/study/NCT00431080) | Phase 3 | 完成 | 478 | 劑量密集 FE75C 後接 docetaxel 對比 paclitaxel，用於淋巴結陽性乳癌輔助治療 |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Phase 2 | 完成 | 148 | 隨機比較 carboplatin 與 docetaxel，用於遺傳性轉移性乳癌 |

> 註：Phase 3 試驗多數以 docetaxel 為組合療程的一部分，無法單獨區分 docetaxel 的貢獻，部分試驗亦主要評估併用藥物。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | ABC 系列輔助試驗：比較 TC（docetaxel + cyclophosphamide）與含紫杉烷的 AC 方案用於早期乳癌 |
| [10791395](https://pubmed.ncbi.nlm.nih.gov/10791395/) | 2000 | Review | Lancet | 紫杉烷類為晚期乳癌、肺癌、卵巢癌的實證治療選項 |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug Ther Bull | Paclitaxel 與 docetaxel 在乳癌與卵巢癌的評估 |
| [18624687](https://pubmed.ncbi.nlm.nih.gov/18624687/) | 2008 | Review | Expert Opin Drug Metab Toxicol | Docetaxel 開發經驗：藥理、藥動與藥物基因體學 |
| [12868800](https://pubmed.ncbi.nlm.nih.gov/12868800/) | 2003 | Review | Breast Cancer Res Treat | Docetaxel 與 anthracycline 併用於轉移性乳癌，兩者活性高且毒性不重疊 |
| [9364543](https://pubmed.ncbi.nlm.nih.gov/9364543/) | 1997 | 臨床研究 | Oncology (Williston Park) | Docetaxel 併用 vinorelbine 用於轉移性乳癌與非小細胞肺癌 |
| [20514452](https://pubmed.ncbi.nlm.nih.gov/20514452/) | 2010 | Cohort | Oncol Rep | 第 8 號染色體基因組變化可預測含紫杉烷新輔助化療的反應 |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Phase II | Oncology | 每週 docetaxel + gemcitabine 用於轉移性乳癌第一線 |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | 臨床研究 | Cancer | Capecitabine 併用 docetaxel 與 epirubicin 用於晚期乳癌第一線 |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | 回溯性研究 | Anti-cancer Drugs | 輔助 docetaxel 化療與乳癌相關淋巴水腫的關聯 |

---

## 香港上市資訊

共 20 張有效許可證（皆為單方），以下列出 5 張主要許可證。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-41354 | TAXOTERE CONC FOR INF. 80MG/2ML (VIAL)（Sanofi） | 注射濃縮液 | 資料未提供 |
| HK-41353 | TAXOTERE CONC FOR INF 20MG/0.5ML (VIAL)（Sanofi） | 注射濃縮液 | 資料未提供 |
| HK-64613 | ACCORD DOCETAXEL 20MG/1ML（I & C） | 注射濃縮液 | 資料未提供 |
| HK-68552 | DAXOTEL 80MG/4ML（Fresenius Kabi） | 注射濃縮液 | 資料未提供 |
| HK-62664 | DOCETAXEL ACTAVIS 80MG/2ML（Teva） | 注射濃縮液 | 資料未提供 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（紫杉烷類，微管穩定劑） |
| 骨髓抑制風險 | 高（知識圖譜顯示與嗜中性白血球低下、血小板低下、貧血、粒線球缺乏等相關） |
| 致吐性分級 | 低至中度（依藥物類別判斷） |
| 監測項目 | CBC（含分類）、肝功能與膽紅素、周邊神經症狀、體液滯留 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

具體警語與劑量調整請參考原廠仿單。

---

## 安全性考量

- **知識圖譜標示的禁忌或高風險情況**（非仿單原文）：肝臟疾病、膽囊疾病、血小板低下、嗜中性白血球低下、粒線球缺乏、周邊神經疾病／神經病變、貧血、高膽紅素血症（含 Gilbert 症候群）、腹瀉性疾病、肺水腫、口腔炎、運動神經炎、心包填塞。
- **藥物交互作用**（共 100 筆，以下為主要項目）：
  - **重大**：Clarithromycin
  - **中度**：Aprepitant、Metronidazole、Cimetidine、Eliglustat、Miconazole、Rolapitant、Rosuvastatin、Simvastatin、Tinidazole、Troglitazone
  - **輕度**：Dexamethasone、Levofloxacin、Prednisolone、Prednisone

仿單層級的警語與禁忌尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 多個大型 Phase 3 試驗（含 NCT00021255、NCT00003782、NCT00333775 等）已將 docetaxel 納入乳癌輔助或轉移性治療方案，證據等級為 L1，且香港已有 20 張有效許可證。
- 乳癌屬既有用途，並非真正的藥物再利用；同時 docetaxel 骨髓抑制與神經毒性風險明確，需以護欄方式管理。

**若要推進需要：**
- 取得香港衛生署仿單的警語、禁忌與核准適應症文字
- 補充詳細的作用機轉資料（MOA）
- 若關注真正的再利用方向，可另行評估 Ewing 肉瘤（L2，docetaxel 多與 gemcitabine 併用）與橫紋肌肉瘤（L2），但其療效有限，屬研究性議題
- 針對骨髓抑制與周邊神經病變建立監測計畫，並檢視與 CYP3A4 抑制劑（如 clarithromycin）的併用
- 其餘預測（肺部罕見腫瘤、原發性肺淋巴瘤及多個橫紋肌肉瘤亞型）證據僅限個案報告或無資料，建議暫緩（Hold）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

