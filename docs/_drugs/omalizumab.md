---
layout: default
title: Omalizumab
parent: 高證據等級 (L1-L2)
nav_order: 544
evidence_level: L2
indication_count: 5
---

# Omalizumab
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Omalizumab：從過敏性氣喘到異位性濕疹等多項預測新適應症

## 一句話總結

Omalizumab（DrugBank DB00043）是抗 IgE 單株抗體，依文獻脈絡原用於過敏性氣喘與慢性自發性蕁麻疹（正式核准適應症資料缺失，見 DG001）。TxGNN 模型針對此藥物提出 **5 個候選新適應症**，證據品質落差很大：**異位性濕疹**有 1 個完成的 Phase 4 兒童 RCT（n=62）與 20 篇文獻支持，是目前最具潛力的方向；其餘候選（支氣管炎、阻塞性肺病、皮膚炎、支氣管腫瘤）多屬機轉薄弱或疑似關鍵字混淆（bronchitis/bronchial 詞根與 asthma 大量共現）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏性氣喘、慢性自發性蕁麻疹（依文獻脈絡整理；正式核准適應症文字缺失，見 DG001） |
| 預測新適應症（最具潛力） | 異位性濕疹 (Atopic Eczema) |
| TxGNN 預測分數 | 99.97%（rank 978） |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Research Question（見下方各候選詳情，藥物層級整體為 Hold） |

### 候選適應症總覽（5 項）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|-----|-----------|-----------|---------|---------|------|
| 1 | 支氣管炎 (Bronchitis) | 99.999% | L4 | S0 | Hold |
| 2 | 異位性濕疹 (Atopic Eczema) | 99.97% | L2 | S2 | Research Question |
| 3 | 阻塞性肺病 (Obstructive Lung Disease) | 99.97% | L3 | S1 | Research Question |
| 4 | 皮膚炎 (Dermatitis) | 99.97% | L2 | S2 | Research Question |
| 5 | 支氣管腫瘤 (Bronchial Neoplasm) | 99.95% | L5 | S0 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Omalizumab 詳細的作用機轉資料（DG002，High severity）。根據證據包內文獻記載，Omalizumab 是重組人化抗 IgE 單株抗體，結合游離 IgE 的恆定區（Cε3 domain），阻斷 IgE 與肥大細胞、嗜鹼性球上高親和力受體（FcεRI）的結合，進而降低過敏發炎反應，目前廣泛用於過敏性氣喘與慢性自發性蕁麻疹。

**異位性濕疹（排名 2）**：部分濕疹病人有血清 IgE 顯著升高與過敏原致敏現象，anti-IgE 阻斷肥大細胞活化的機轉具生物學合理性，且已有 Phase 4 完成的兒童重度濕疹 RCT（NCT02300701）直接驗證，是 5 項候選中機轉與實證最一致的方向。惟濕疹的屏障失能與 Th2/Th17 混合發炎機轉較氣喘複雜，療效不如氣喘穩定。

**皮膚炎（排名 4）**與異位性濕疹共用幾乎同一組核心試驗與文獻，屬同一訊號的重複呈現；但出現一則矛盾安全性報告（PMID 37988298：Omalizumab 誘發皮膚炎、改以 Dupilumab 治療），顯示因果方向需要進一步釐清（是治療效果還是藥物不良反應）。

**阻塞性肺病（排名 3）**：COPD 中具過敏原致敏／嗜酸性球表現型的亞群與氣喘重疊（asthma-COPD overlap, ACO），anti-IgE 在此亞群有理論基礎，且有一項正在招募的 Phase 2 專門試驗（NCT07059091）；但典型吸菸相關、非過敏性 COPD 缺乏機轉支持。

**支氣管炎（排名 1）與支氣管腫瘤（排名 5）**：兩者證據薄弱，很可能是知識圖譜/文字檢索的關鍵字混淆所致——「bronchitis」「bronchial」與「asthma」「bronchial asthma」詞根高度共現，檢索回來的試驗實際受試族群幾乎全是氣喘患者，機轉上（感染/刺激性氣道發炎 vs. IgE 過敏機轉；IgE 與肺腫瘤免疫監視）均無直接支持，儘管 TxGNN 分數是 5 項中最高。

---

## 臨床試驗證據

### 異位性濕疹（最具潛力）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02300701](https://clinicaltrials.gov/study/NCT02300701) | Phase 4 | 完成 | 62 | 評估 Omalizumab 用於重度頑固性小兒異位性濕疹的療效（Grade A，最直接證據） |
| [NCT00822783](https://clinicaltrials.gov/study/NCT00822783) | Phase 4 | 完成 | N/A | 探索 IgE 介導樹突細胞抗原呈現機轉變化（Grade B） |
| [NCT01179529](https://clinicaltrials.gov/study/NCT01179529) | Phase 2 | 完成 | N/A | 單臂研究，尋找治療反應變異性的生物標記（Grade B） |
| [NCT01678092](https://clinicaltrials.gov/study/NCT01678092) | Phase 1 | 完成 | 8 | 依產品標籤劑量在異位性皮膚炎患者中的單中心研究 |
| [NCT01995747](https://clinicaltrials.gov/study/NCT01995747) | N/A | 完成 | 52 | 異位性皮膚炎患者 PBMC 中 IgE 產生機轉研究 |
| [NCT04060550](https://clinicaltrials.gov/study/NCT04060550) | N/A | 未知 | 36 | 濕疹合併疱疹感染患者中 IgE 對抗病毒先天免疫反應的影響 |
| [NCT05674695](https://clinicaltrials.gov/study/NCT05674695) | N/A | 招募中 | 2500 | 西班牙異位性濕疹系統性治療登記研究 |
| [NCT07021495](https://clinicaltrials.gov/study/NCT07021495) | N/A | 招募中 | 840 | 六種慢性免疫發炎性皮膚病（含 AD）生物標記真實世界研究 |

### 皮膚炎（與異位性濕疹同源信號）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02300701](https://clinicaltrials.gov/study/NCT02300701) | Phase 4 | 完成 | 62 | 同上，兒童重度濕疹（Grade A） |
| [NCT00260702](https://clinicaltrials.gov/study/NCT00260702) | Phase 1 | 完成 | 1 | Job's 症候群（高 IgE 症候群）先導研究，n=1，罕見病（Grade C） |

### 阻塞性肺病

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07059091](https://clinicaltrials.gov/study/NCT07059091) | Phase 2 | 招募中 | 334 | 針對過敏原致敏且暴露之 COPD 病人設計，直接對應此適應症但尚無結果（Grade A） |
| [NCT00851370](https://clinicaltrials.gov/study/NCT00851370) | Phase 2 | 已撤回 | 0 | COPD 合併高 IgE 探索性研究，已 WITHDRAWN 無可用結果（Grade B） |
| [NCT02293265](https://clinicaltrials.gov/study/NCT02293265) | Phase 3 | 完成 | 767 | 重度氣喘橫斷面研究，非 COPD 特異性（Grade C） |

其餘 47 個檢索到的試驗絕大多數是過敏性氣喘生物製劑研究，與典型 COPD 無直接關聯，故不逐一列出。

### 支氣管炎

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Phase 2/3 | 完成 | 11 | 氣喘合併嗜酸性球性支氣管炎的類固醇減量試驗，適應症核心仍為氣喘（Grade C） |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Phase 2b | 完成 | 382 | 慢性自發性蕁麻疹劑量探索試驗，與支氣管炎無直接關聯（Grade C） |

### 支氣管腫瘤

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06869382](https://clinicaltrials.gov/study/NCT06869382) | Phase 4 | 完成 | 26 | 過敏性氣喘轉錄體表現研究，非腫瘤終點（Grade C） |
| [NCT04680117](https://clinicaltrials.gov/study/NCT04680117) | N/A | 未知 | 150 | 重度小兒氣喘內表型研究，與支氣管腫瘤無關（Grade C） |

---

## 文獻證據

### 異位性濕疹 / 皮膚炎

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35980214](https://pubmed.ncbi.nlm.nih.gov/35980214/) | 2022 | Guideline | JEADV | EuroGuiDerm 異位性濕疹系統性治療指引 |
| [38812522](https://pubmed.ncbi.nlm.nih.gov/38812522/) | 2024 | Review | Front Immunol | 兒童/青少年中重度異位性皮膚炎系統性治療有效性與安全性回顧 |
| [30717578](https://pubmed.ncbi.nlm.nih.gov/30717578/) | 2019 | Review | G Ital Dermatol Venereol | Omalizumab 用於異位性皮膚炎的正反證據回顧 |
| [27337170](https://pubmed.ncbi.nlm.nih.gov/27337170/) | 2017 | Case series + Systematic review | Int J Dermatol | 9 例異位性皮膚炎病例系列及系統性文獻回顧 |
| [27543070](https://pubmed.ncbi.nlm.nih.gov/27543070/) | 2016 | Systematic review/Meta-analysis | J Allergy Clin Immunol | Omalizumab 用於異位性皮膚炎的療效系統性回顧與統合分析 |
| [33074565](https://pubmed.ncbi.nlm.nih.gov/33074565/) | 2021 | Systematic review | Allergy | 中重度 AD 系統性治療的系統性回顧與統合分析（EAACI 指引資源） |
| [37988298](https://pubmed.ncbi.nlm.nih.gov/37988298/) | 2023 | Case report | Cutis | ⚠️ Omalizumab 誘發異位性皮膚炎，改以 Dupilumab 治療（矛盾安全性訊號） |
| [31998003](https://pubmed.ncbi.nlm.nih.gov/31998003/) | 2019 | pending | Postepy Dermatol Alergol | 土耳其東南部 Omalizumab 用於慢性蕁麻疹與異位性皮膚炎之使用數據 |

### 阻塞性肺病

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36740144](https://pubmed.ncbi.nlm.nih.gov/36740144/) | 2023 | Target trial emulation (Cohort) | J Allergy Clin Immunol | Omalizumab、Mepolizumab、Dupilumab 於氣喘的比較效果研究 |
| [36581073](https://pubmed.ncbi.nlm.nih.gov/36581073/) | 2023 | Systematic review/Meta-analysis | J Allergy Clin Immunol Pract | Omalizumab 用於難治性過敏性支氣管肺麴菌病的系統性回顧與統合分析 |
| [33160970](https://pubmed.ncbi.nlm.nih.gov/33160970/) | 2021 | pending | J Allergy Clin Immunol | Omalizumab 於「非 IgE 介導」疾病中的角色探討 |

### 支氣管炎

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case report | J Investig Allergol Clin Immunol | 塑型性支氣管炎（plastic bronchitis）罕見個案，非治療適應症 |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | pending | Expert Opin Pharmacother | 吸菸相關氣道疾病（含慢性支氣管炎）合併氣喘的治療挑戰 |

### 支氣管腫瘤

僅 1 篇文獻（[20955114](https://pubmed.ncbi.nlm.nih.gov/20955114/)，2010，Review，兒童氣喘用藥回顧），與肺部腫瘤無直接關聯。

---

## 香港上市資訊

目前無香港上市許可證資訊（`market_status: 未上市`，`total_licenses: 0`）。

---

## 安全性考量

安全性資訊請參考原廠仿單。目前查無 TFDA/藥物安全警語、禁忌症及藥物交互作用資料（DG001，Blocking severity：此缺口導致無法進入 S1 安全性初評）。唯一相關訊號來自文獻 [PMID 37988298](https://pubmed.ncbi.nlm.nih.gov/37988298/)：個案報告顯示 Omalizumab 治療期間誘發異位性皮膚炎，需列入濕疹/皮膚炎候選適應症的鑑別考量。

---

## 結論與下一步

**決策：Hold（異位性濕疹方向可維持 Research Question，其餘候選維持 Hold）**

**理由：**
- 5 項候選中，僅「異位性濕疹」具備 L2 等級實證（1 個完成的 Phase 4 兒童 RCT + 系統性回顧/統合分析文獻），機轉合理，值得列為研究問題持續追蹤。
- 「支氣管炎」「支氣管腫瘤」證據等級為 L4/L5，且評估認為極可能是關鍵字混淆造成的雜訊，不建議投入資源。
- 「阻塞性肺病」僅在 ACO（氣喘-COPD 重疊）亞群有理論基礎，關鍵試驗（NCT07059091）尚在招募中無結果。
- 藥物層級的仿單警語/禁忌症資料缺失（DG001，Blocking），在此資料補齊前，任一候選皆無法進入 S1 安全性初評階段。

**若要推進需要：**
- 補齊 TFDA/原廠仿單警語與禁忌症資料（DG001，最高優先）
- 補齊 DrugBank 作用機轉（MOA）詳細資料（DG002）
- 待 NCT07059091（COPD-OMA）試驗完成，重新評估阻塞性肺病候選
- 針對「皮膚炎誘發」矛盾安全性訊號（PMID 37988298）進行文獻覆核，釐清因果方向
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

