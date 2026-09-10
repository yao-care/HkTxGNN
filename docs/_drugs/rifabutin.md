---
layout: default
title: Rifabutin
parent: 僅模型預測 (L5)
nav_order: 646
evidence_level: L5
indication_count: 5
---

# Rifabutin
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

# Rifabutin：從分枝桿菌感染治療到 HIV 感染症

## 一句話總結

Rifabutin 是 rifamycin 類抗生素，臨床上廣泛用於 HIV 感染合併分枝桿菌感染（結核病、MAC）病人的治療與預防。
TxGNN 模型預測它可能對**HIV 感染症 (HIV infectious disease)** 有效，
目前有 **39 個臨床試驗**和 **20 篇文獻**支持，但多數證據聚焦於藥物交互作用與共病治療，而非直接抗 HIV 病毒機轉（詳見下文說明）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無香港許可資料（未上市）；根據證據內容，臨床上多用於 HIV 合併分枝桿菌感染（結核病／MAC）之治療與預防 |
| 預測新適應症 | HIV infectious disease（HIV 感染症） |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L1（≥2 個已完成的 Phase 3 RCT） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 未提供）。根據臨床試驗與文獻，Rifabutin 廣泛用於 HIV 感染合併分枝桿菌感染（結核病、MAC）病人的治療與預防，尤其常見於與抗反轉錄病毒藥物（如蛋白酶抑制劑、NNRTI、INSTI）併用時的藥物動力學交互作用與劑量調整研究。

**重要說明**：仔細檢視證據內容後發現，39 個臨床試驗與 20 篇文獻中絕大多數的研究主題並非「Rifabutin 直接治療 HIV 病毒感染」，而是聚焦於：
1. Rifabutin 與抗反轉錄病毒藥物（dolutegravir、cabotegravir、darunavir/ritonavir、tenofovir alafenamide 等）之藥物動力學交互作用（DDI）
2. Rifabutin 用於 HIV 病人合併結核病／MAC 感染之治療與預防（取代 rifampicin，因其對 ART 酵素誘導作用較弱）
3. 安全性與劑量調整研究（含兒童族群）

因此，TxGNN 預測「HIV infectious disease」的高分，實質上反映的是 Rifabutin 在 HIV 臨床照護路徑中與 ART 藥物高度共現的關係，而非直接的抗 HIV 病毒藥理機轉。這是解讀此預測時的重要限制，建議將其定位為「HIV 合併分枝桿菌感染之輔助治療」而非「HIV 病毒感染之直接療法」。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00002122](https://clinicaltrials.gov/study/NCT00002122) | Phase 3 | 完成 | 720 | Azithromycin/Rifabutin 單獨及合併用於預防 HIV 病人 MAC 感染 |
| [NCT00001030](https://clinicaltrials.gov/study/NCT00001030) | Phase 3 | 完成 | 1100 | Clarithromycin vs Rifabutin vs 併用，預防 CD4≤100 病人 MAC 菌血症 |
| [NCT00001047](https://clinicaltrials.gov/study/NCT00001047) | Phase 3 | 完成 | 400 | Clarithromycin + ethambutol + rifabutin/clofazimine 治療 AIDS 病人瀰漫性 MAC |
| [NCT00002101](https://clinicaltrials.gov/study/NCT00002101) | Phase 3 | 完成 | 450 | Clarithromycin/ethambutol + rifabutin 兩劑量 vs 安慰劑，MAC 菌血症治療 |
| [NCT00023348](https://clinicaltrials.gov/study/NCT00023348) | Phase 2/3 | 完成 | 150 | HIV 相關結核病病人間歇性 isoniazid + rifabutin 藥物動力學研究 |
| [NCT03149848](https://clinicaltrials.gov/study/NCT03149848) | Phase 1 | 完成 | 15 | Rifabutin 對口服 cabotegravir（現代 ART 藥物）藥物動力學之影響 |
| [NCT02138084](https://clinicaltrials.gov/study/NCT02138084) | Phase 1 | 完成 | 102 | Rifabutin 與 BMS-626529（attachment inhibitor）之藥物交互作用 |
| [NCT01231542](https://clinicaltrials.gov/study/NCT01231542) | Phase 1 | 完成 | 27 | Rifampin 與 rifabutin 對 dolutegravir 藥物動力學之影響 |
| [NCT00651066](https://clinicaltrials.gov/study/NCT00651066) | Phase 2 | 完成 | 47 | 越南 HIV/TB 共病病人，Rifabutin 取代 rifampicin 之藥物動力學評估 |
| [NCT00640887](https://clinicaltrials.gov/study/NCT00640887) | Phase 2 | 完成 | 48 | 南非 HIV/TB 共病病人，Rifabutin 合併 ART 之藥物動力學評估 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25404581](https://pubmed.ncbi.nlm.nih.gov/25404581/) | 2014 | Systematic Review (Cochrane) | Evidence-based Child Health | Rifamycins（含 rifabutin）vs isoniazid 用於 HIV 陰性高風險族群 TB 預防 |
| [23828580](https://pubmed.ncbi.nlm.nih.gov/23828580/) | 2013 | Systematic Review (Cochrane) | Cochrane Database Syst Rev | 同上主題原始 Cochrane 回顧 |
| [28233512](https://pubmed.ncbi.nlm.nih.gov/28233512/) | 2017 | Review | Microbiology Spectrum | HIV 相關結核病之整體治療現況回顧 |
| [7736687](https://pubmed.ncbi.nlm.nih.gov/7736687/) | 1995 | Review | Clin Pharmacokinet | Rifabutin 臨床藥物動力學特性總論 |
| [26832753](https://pubmed.ncbi.nlm.nih.gov/26832753/) | 2016 | PK Pooled Analysis | J Antimicrob Chemother | Rifabutin 與 HIV 蛋白酶抑制劑之族群藥物動力學交互作用分析 |
| [36385424](https://pubmed.ncbi.nlm.nih.gov/36385424/) | 2023 | PK Model | Br J Clin Pharmacol | Rifabutin 與 dolutegravir 之藥物交互作用族群藥物動力學模型 |
| [32979587](https://pubmed.ncbi.nlm.nih.gov/32979587/) | 2020 | Retrospective | Int J Infect Dis | Tenofovir alafenamide 與 rifabutin 併用不影響 HIV-1 病毒抑制之回溯性研究 |
| [33294914](https://pubmed.ncbi.nlm.nih.gov/33294914/) | 2021 | Cohort | J Antimicrob Chemother | TB/HIV 共感染兒童接受 LPV/r 為主二線 ART 時 rifabutin 藥物動力學與安全性 |
| [31139825](https://pubmed.ncbi.nlm.nih.gov/31139825/) | 2019 | Cohort | J Antimicrob Chemother | HIV/TB 共感染兒童接受 LPV/r 為主 ART 時 rifabutin 安全性與療效 |
| [21406051](https://pubmed.ncbi.nlm.nih.gov/21406051/) | 2011 | Review | Infect Disord Drug Targets | HIV 大流行時代成人活動性結核病之治療現況與未來展望 |

---

## 香港上市資訊

Rifabutin 目前**未在香港上市**（`market_status: 未上市`，許可證數：0），無可列出之許可證資料。

---

## 安全性考量

⚠ **關鍵資料缺口（Blocking）**：本評估目前缺乏 TFDA／香港衛生署仿單之警語與禁忌症資料，**無法完成 S1 安全性初評**。需先取得仿單 PDF 並解析後，方可進行下一階段評估。

- **主要警語**：資料缺失，請參考原廠仿單。
- **禁忌症**：資料缺失，請參考原廠仿單。
- **藥物交互作用**：資料庫查無結果（`query_status: not_found`）；惟臨床試驗與文獻證據高度一致指出，Rifabutin 與多種抗反轉錄病毒藥物（PI、INSTI、NNRTI 及新型藥物如 cabotegravir、vesatolimod）存在具臨床意義之藥物動力學交互作用，實際使用時仍需個別評估劑量調整。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 雖符合 L1 證據等級（多個已完成 Phase 3 RCT），但這些試驗與文獻多聚焦於藥物交互作用及分枝桿菌合併感染治療，並非直接支持「治療 HIV 病毒感染」本身的療效，預測適應症與實際證據內容存在定位落差。
- 原廠仿單警語／禁忌症資料缺失為 **Blocking** 等級落差，無法完成 S1 安全性初評，依規範不應在此狀態下推進。
- 香港未上市，亦無許可證資料可供對照。

**若要推進需要：**
- 取得 TFDA／香港衛生署仿單完整警語與禁忌症資料（DG001，Blocking，需優先解決）
- 取得 DrugBank 完整作用機轉（MOA）資料（DG002）
- 釐清此預測之實際臨床定位：應理解為「HIV 合併分枝桿菌感染之輔助／共治療用藥」而非「HIV 病毒感染之直接療法」，並據此重新界定適應症敘述
- 補齊完整藥物交互作用資料庫查詢結果，特別是與現行 ART 標準療程（dolutegravir、cabotegravir 等 INSTI 類）之交互作用資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

