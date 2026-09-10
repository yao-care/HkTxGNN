---
layout: default
title: Rosuvastatin
parent: 僅模型預測 (L5)
nav_order: 663
evidence_level: L5
indication_count: 5
---

# Rosuvastatin
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

# Rosuvastatin：從血脂異常到多項潛在新適應症

## 一句話總結

Rosuvastatin 是 HMG-CoA reductase 抑制劑（statin 類藥物），原本用於治療高膽固醇血症／血脂異常。
TxGNN 模型針對此藥物共預測出 **5 個候選新適應症**，證據強度差異很大：其中**家族性高膽固醇血症 (Familial Hypercholesterolemia)** 有 **24 個臨床試驗**與 **13 篇文獻**支持（多屬既有 statin 標準用法的延伸驗證），**HIV 感染合併心血管/發炎共病管理**則有 **21 個臨床試驗**與 **20 篇文獻**支持，屬於較具「老藥新用」意義的方向；其餘 3 項（CETP 缺乏症、CYP7A1 缺乏症、腦幹梗塞）證據薄弱，僅有零星文獻，缺乏臨床試驗支持。

⚠️ 本藥物**尚未在香港上市**（0 張許可證），且 TFDA/HK 仿單警語與禁忌症資料缺失（Blocking 等級缺口），無法完成 S1 安全性初評。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高膽固醇血症／血脂異常（statin 類藥物；香港無許可證，故無正式核准適應症文字） |
| TxGNN 排名第 1 候選適應症 | Cholesterol-Ester Transfer Protein (CETP) Deficiency |
| TxGNN 預測分數（Rank 1） | 99.54% |
| 證據等級（Rank 1） | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策（Rank 1） | Hold |

### 全部候選新適應症總覽

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|------|
| 1 | Cholesterol-ester transfer protein deficiency | 99.54% | L5 | S0 | Hold |
| 2 | Familial hypercholesterolemia | 99.54% | L1 | S3 | Proceed with Guardrails |
| 3 | Hypercholesterolemia due to cholesterol 7α-hydroxylase deficiency | 99.51% | L4 | S1 | Research Question |
| 4 | Brain stem infarction | 99.44% | L4 | S0 | Hold |
| 5 | HIV infectious disease（心血管/發炎共病管理） | 99.37% | L2 | S2 | Research Question |

---

## 為什麼這個預測合理？

**作用機轉**：目前缺乏正式登錄的 MOA 資料（DrugBank 查詢未返回結果）。根據本次收集之臨床證據反覆呈現的藥理基礎，rosuvastatin 屬 HMG-CoA reductase 抑制劑，透過抑制肝臟膽固醇合成、代償性上調 LDL 受體表現以降低 LDL-C；此外 statin 類藥物具多效性（pleiotropic）作用，包括抗發炎、內皮功能改善與免疫調節，這是多項候選適應症佐證資料的共同機轉基礎。

**逐一候選適應症解讀**：

- **家族性高膽固醇血症（Rank 2, L1）**：直接機轉——抑制 HMG-CoA reductase、上調 LDL 受體，正是 FH（LDL 受體缺陷/功能不足）的標準治療原理。此適應症已是 statin 類藥物既有臨床標準用法，非嚴格意義的「新」適應症，但可作為本平台之高信度陽性對照。
- **HIV 感染（Rank 5, L2）**：證據支持的是 rosuvastatin 作為 HIV 感染者「心血管風險／慢性發炎」輔助治療（降低血管發炎、抑制 T 細胞與單核球活化），**並非**抗病毒機轉。若將適應症標籤解讀為「治療 HIV 感染本身」則證據不支持；若解讀為「HIV 感染者心血管/發炎共病管理」則有中等強度證據。多筆列出的試驗實為抗病毒藥物與 rosuvastatin 的 PK/DDI 研究，非療效試驗，判讀時需注意。
- **CYP7A1 缺乏症（Rank 3, L4）**：間接機轉合理——此罕見病因膽酸合成受阻、喪失負回饋抑制，導致肝內膽固醇累積；rosuvastatin 理論上仍可獨立於膽酸路徑降低細胞內膽固醇並上調 LDL 受體，但無臨床試驗驗證實際反應性。
- **腦幹梗塞（Rank 4, L4）**：statin 之抗發炎、斑塊穩定化為缺血性中風次級預防的既有機轉基礎，但所提供文獻僅為外泌體合併療法之臨床前研究與生物標記相關性研究，並非直接療效證據，且無任何臨床試驗支持。
- **CETP 缺乏症（Rank 1, L5）**：機轉方向可能相反——此症特徵為 HDL-C 顯著升高、CETP 介導之膽固醇酯轉移受阻，與 statin 主要作用的 LDL 受體上調機轉無直接交集，無明確藥理學理由支持療效。

---

## 臨床試驗證據

### 家族性高膽固醇血症（L1，最強證據）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00654602](https://clinicaltrials.gov/study/NCT00654602) | Phase 3 | 完成 | 1500 | 大型開放性研究，確認 rosuvastatin 於 HeFH 降 LDL-C 療效與安全性 |
| [NCT00355615](https://clinicaltrials.gov/study/NCT00355615) | Phase 3 | 完成 | 173 | 兒童 HeFH 安慰劑對照 RCT，證實 rosuvastatin 降 LDL-C 療效 |
| [NCT01078675](https://clinicaltrials.gov/study/NCT01078675) | Phase 3 | 完成 | 315 | 兒童青少年 FH 族群 2 年安全性/療效追蹤 |
| [NCT02226198](https://clinicaltrials.gov/study/NCT02226198) | Phase 3 | 完成 | 20 | 兒童 HoFH 交叉試驗，確立療效、安全性、耐受性 |
| [NCT02434497](https://clinicaltrials.gov/study/NCT02434497) | Phase 3 | 完成 | 9 | HoFH 兒童青少年長期安全性擴展研究 |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | 完成 | 442 | 評估 rosuvastatin 對腎功能之影響於 HeFH 族群 |
| [NCT02748057](https://clinicaltrials.gov/study/NCT02748057) | Phase 3 | 完成 | 135 | Ezetimibe + Rosuvastatin 併用長期安全耐受性（日本患者） |
| [NCT06910098](https://clinicaltrials.gov/study/NCT06910098) | N/A | 完成 | 195 | 不同劑量 rosuvastatin 對 LDL、CPK、AST 之影響 |
| [NCT01623115](https://clinicaltrials.gov/study/NCT01623115) | Phase 3 | 完成 | 486 | Alirocumab 安慰劑對照 RCT 於 heFH（佐證性資料） |
| [NCT02107898](https://clinicaltrials.gov/study/NCT02107898) | Phase 3 | 完成 | 216 | Alirocumab 於 heFH 多中心 RCT（佐證性資料） |

### HIV 感染（心血管/發炎共病管理，L2）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01218802](https://clinicaltrials.gov/study/NCT01218802) | Phase 2 | 完成 | 147 | 安慰劑對照 RCT，評估 96 週 rosuvastatin 對心血管風險與骨質流失之調節 |
| [NCT03037372](https://clinicaltrials.gov/study/NCT03037372) | Phase 3 | 未知 | 320 | Atorvastatin vs rosuvastatin 等效性試驗，作為 HAART 輔助治療 |
| [NCT01813357](https://clinicaltrials.gov/study/NCT01813357) | Phase 4 | 完成 | 84 | 安慰劑對照 RCT，評估延緩中度心血管風險 HIV 患者之動脈粥狀硬化進展 |
| [NCT00673582](https://clinicaltrials.gov/study/NCT00673582) | Phase 4 | 終止 | 250 | 安慰劑對照 RCT，以頸動脈超音波評估抑制動脈粥狀硬化進展 |
| [NCT02234492](https://clinicaltrials.gov/study/NCT02234492) | Phase 4 | 完成 | 35 | 評估 rosuvastatin 對冠狀動脈血流儲備與神經認知功能之影響 |
| [NCT00117494](https://clinicaltrials.gov/study/NCT00117494) | Phase 4 | 完成 | 86 | Rosuvastatin vs pravastatin 於蛋白酶抑制劑相關血脂異常之療效安全性比較 |
| [NCT00908011](https://clinicaltrials.gov/study/NCT00908011) | N/A | 完成 | 43 | Ezetimibe 加成 rosuvastatin 治療 HIV 抗病毒相關高膽固醇血症 |
| [NCT00986999](https://clinicaltrials.gov/study/NCT00986999) | Phase 2/3 | 終止 | 7 | 低劑量 rosuvastatin 對內皮功能、氧化壓力、發炎指標之影響（樣本數小，證據力受限） |
| [NCT02841774](https://clinicaltrials.gov/study/NCT02841774) | Phase 2 | 完成 | 10 | HILLCLIMBER：急性冠心症後 HIV 患者，中劑量 vs 高劑量 statin 治療比較 |
| [NCT01881971](https://clinicaltrials.gov/study/NCT01881971) | Early Phase 1 | 完成 | 23 | 評估 statin 治療對 HIV 心肺異常進展之發炎抑制假說 |

### 其他候選適應症（證據不足以支持臨床試驗）

- **CETP 缺乏症、CYP7A1 缺乏症、腦幹梗塞**：目前無相關臨床試驗登記。

---

## 文獻證據

### 家族性高膽固醇血症

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE 血脂異常管理與心血管疾病預防指引 |
| [28838366](https://pubmed.ncbi.nlm.nih.gov/28838366/) | 2017 | Cohort | J Am Coll Cardiol | Rosuvastatin 於 HoFH 兒童之療效及與基因型之關聯 |
| [20223367](https://pubmed.ncbi.nlm.nih.gov/20223367/) | 2010 | Cohort | J Am Coll Cardiol | Rosuvastatin 治療兒童 FH 之療效與安全性 |
| [26988948](https://pubmed.ncbi.nlm.nih.gov/26988948/) | 2016 | Review | J Am Coll Cardiol | 改善 FH 患者監測與照護之綜述 |
| [28838367](https://pubmed.ncbi.nlm.nih.gov/28838367/) | 2017 | Review | J Am Coll Cardiol | HoFH 患者管理綜述 |
| [26687694](https://pubmed.ncbi.nlm.nih.gov/26687694/) | 2015 | pending | J Clin Lipidol | CHARON 研究：兒童青少年 FH 療效安全性結果 |
| [15256766](https://pubmed.ncbi.nlm.nih.gov/15256766/) | 2004 | pending | J Atheroscler Thromb | 日本 HeFH 患者 rosuvastatin 療效安全性 |
| [26387811](https://pubmed.ncbi.nlm.nih.gov/26387811/) | 2016 | pending | Eur J Clin Pharmacol | 兒童 HeFH 之 rosuvastatin 族群藥物動力學 |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | pending | Drugs | Rosuvastatin 綜合藥理與臨床療效回顧 |
| [34029164](https://pubmed.ncbi.nlm.nih.gov/34029164/) | 2021 | pending | Stem Cells Dev | FH 患者特異性 iPSC 世代與特徵化（機轉研究） |

### HIV 感染（心血管/發炎共病）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25514794](https://pubmed.ncbi.nlm.nih.gov/25514794/) | 2015 | RCT | J Acquir Immune Defic Syndr | Rosuvastatin 降低 HIV 感染者血管發炎及 T 細胞/單核球活化 |
| [32955957](https://pubmed.ncbi.nlm.nih.gov/32955957/) | 2021 | Cohort | Infect Dis (Lond) | Rosuvastatin 降低發炎指標並減緩代謝症候群 HIV 患者動脈粥狀硬化進展 |
| [40158388](https://pubmed.ncbi.nlm.nih.gov/40158388/) | 2025 | Mechanistic | EBioMedicine | Rosuvastatin 對 HIV 患者 CD8+ T 細胞記憶潛能與功能性之影響 |
| [29804227](https://pubmed.ncbi.nlm.nih.gov/29804227/) | 2018 | Review | Curr Infect Dis Rep | HIV 感染族群 statin 治療之效益與風險綜述 |
| [27192322](https://pubmed.ncbi.nlm.nih.gov/27192322/) | 2016 | Review | Expert Opin Pharmacother | HIV 相關代謝異常之藥物治療綜述 |
| [25015912](https://pubmed.ncbi.nlm.nih.gov/25015912/) | 2014 | pending | Clin Infect Dis | SATURN-HIV 試驗：rosuvastatin 保護腎功能並降低 cystatin C |
| [26477698](https://pubmed.ncbi.nlm.nih.gov/26477698/) | 2016 | pending | AIDS Res Hum Retroviruses | 96 週 rosuvastatin 對骨質、肌肉、脂肪之影響 |
| [29770749](https://pubmed.ncbi.nlm.nih.gov/29770749/) | 2018 | pending | HIV Clin Trials | Rosuvastatin 與 atorvastatin 於 HIV 合併慢性腎病及高血脂患者之腎功能保護 |
| [33620177](https://pubmed.ncbi.nlm.nih.gov/33620177/) | 2021 | pending | J Acquir Immune Defic Syndr | 週期性中斷 rosuvastatin 治療逆轉病毒潛伏並誘發 Gag 特異性 T 細胞反應（概念驗證） |
| [18991624](https://pubmed.ncbi.nlm.nih.gov/18991624/) | 2008 | pending | Curr HIV Res | Rosuvastatin、pravastatin、atorvastatin 治療蛋白酶抑制劑相關高膽固醇血症之比較 |

### 其他候選適應症

| 適應症 | PMID | 年份 | 類型 | 主要發現 |
|--------|------|-----|------|---------|
| CYP7A1 缺乏症 | [15583480](https://pubmed.ncbi.nlm.nih.gov/15583480/) | 2004 | 機轉研究 | HMG-CoA reductase 抑制對腎病症候群相關膽固醇調節酵素表現之影響 |
| 腦幹梗塞 | [31974756](https://pubmed.ncbi.nlm.nih.gov/31974756/) | 2020 | 臨床前/併用療法 | 骨髓幹細胞外泌體併用 rosuvastatin 於大鼠缺血性中風之神經保護 |
| 腦幹梗塞 | [36600882](https://pubmed.ncbi.nlm.nih.gov/36600882/) | 2022 | 生物標記相關性 | NT-proBNP 與幹細胞因子血漿濃度與 ESRD 透析患者心血管結局之關聯 |
| CETP 缺乏症 | [21122686](https://pubmed.ncbi.nlm.nih.gov/21122686/) | 2010 | 病例報告/綜述 | 伊拉克 Mandaean 家族完全性 Apo AI 缺乏症之案例與文獻回顧 |
| CETP 缺乏症 | [22798447](https://pubmed.ncbi.nlm.nih.gov/22798447/) | 2010 | 病例報告 | 中東阿拉伯男性之肝脂酶缺乏症臨床與生化特徵 |

---

## 香港上市資訊

目前**無香港許可證記錄**（`total_licenses = 0`，`licenses = []`）。Rosuvastatin 在本評估中屬「未上市」狀態，無法提取核准適應症文字、劑型或品名資訊。

---

## 安全性考量

安全性資訊尚未取得：主要警語、禁忌症與藥物交互作用資料均為缺口（DG001，Blocking 等級），已阻斷此藥物進入 S1 安全性初評。

> 安全性資訊請參考原廠仿單。建議優先向 TFDA/HK 或原廠取得正式仿單 PDF 以補齊警語與禁忌症資料。

---

## 結論與下一步

**決策：依候選適應症分層處理（整體：Hold，待補齊 Blocking 缺口）**

**理由：**
- **DG001（仿單警語/禁忌，Blocking）** 尚未補齊，任何候選適應症都無法完成 S1 安全性初評，故整體專案層級建議 **Hold**。
- 個別候選中，**家族性高膽固醇血症（L1, S3, Proceed with Guardrails）** 證據最強，但本質上是 statin 既有標準用法而非真正新適應症，可作陽性對照。
- **HIV 感染之心血管/發炎共病管理（L2, S2, Research Question）** 是本輪最具「老藥新用」意義的方向，有多個 Phase 2-4 試驗支持，值得列入下一階段研究議程，但需明確界定適應症範疇為「共病管理」而非「抗病毒治療」，避免誤讀。
- CETP 缺乏症（L5）、CYP7A1 缺乏症（L4）、腦幹梗塞（L4）證據薄弱或機轉方向存疑，建議 **Hold**，暫不投入資源。

**若要推進需要：**
- 取得 TFDA/HK 官方仿單，解析警語與禁忌症（解除 DG001 Blocking 缺口）
- 向 DrugBank API 查詢正式 MOA 資料（解除 DG002 缺口）
- 針對 HIV 共病管理候選，釐清適應症標籤定義（心血管/發炎風險管理 vs. 抗病毒治療），避免決策誤判
- 若考慮於香港申請新適應症或上市，需先確認藥品尚未取得任何香港許可證之現況
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

