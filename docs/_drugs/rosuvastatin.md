---
layout: default
title: Rosuvastatin
parent: 高證據等級 (L1-L2)
nav_order: 788
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Rosuvastatin：預測新適應症為家族性高膽固醇血症 (Familial Hypercholesterolemia)（證據等級 L1）。原適應症：高三酸甘油脂血症、高脂蛋白血症、動脈粥樣硬化、腦梗塞、同型合子家族性高膽固醇血症等"
monitor_inn: "ROSUVASTATIN"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "familial hypercholesterolemia", "hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "brain stem infarction", "HIV infectious disease"]
---

# Rosuvastatin
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

# Rosuvastatin：從高脂血症與動脈硬化到家族性高膽固醇血症

## 一句話總結

Rosuvastatin（瑞舒伐他汀）是一種他汀類降血脂藥，原本用於高三酸甘油脂血症、高脂蛋白血症、動脈硬化及中風相關疾病的治療。
TxGNN 模型預測它可能對**家族性高膽固醇血症 (Familial Hypercholesterolemia)** 有效，
目前有 **12 個臨床試驗**和 **12 篇文獻**支持這個方向（部分為其他藥物的試驗，詳見下表）。
需要說明的是，此適應症與原適應症（同型合子家族性高膽固醇血症）高度重疊，較接近既有適應症的延伸，而非典型的藥物再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高三酸甘油脂血症、高脂蛋白血症、動脈粥樣硬化、腦梗塞、同型合子家族性高膽固醇血症等（來自知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 家族性高膽固醇血症 (Familial Hypercholesterolemia) |
| TxGNN 預測分數 | 99.54% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，rosuvastatin 為 HMG-CoA 還原酶抑制劑（他汀類），可降低肝臟膽固醇合成，並上調 LDL 受體，增加 LDL-C 的清除。

家族性高膽固醇血症的核心問題是 LDL 受體功能缺陷導致 LDL-C 嚴重升高，而 rosuvastatin 的降 LDL-C 機轉與此直接相關。原適應症中已包含同型合子家族性高膽固醇血症，因此本預測更像是適應症範圍的擴展（例如異型合子型或兒童族群），而非全新用途。

需注意，同型合子型患者的反應與 LDL 受體突變類型有關，異型合子與同型合子的療效可能不同。

---

## 臨床試驗證據

以下列出與 rosuvastatin 及家族性高膽固醇血症最相關的 10 個試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00355615](https://clinicaltrials.gov/study/NCT00355615) | Phase 3 | 完成 | 173 | 10–17 歲異型合子 FH 兒童，12 週雙盲安慰劑對照後接 40 週開放延伸，評估降 LDL-C 療效 |
| [NCT02226198](https://clinicaltrials.gov/study/NCT02226198) | Phase 3 | 完成 | 20 | 6–<18 歲同型合子 FH 兒童，雙盲安慰劑對照交叉試驗，評估療效與安全性 |
| [NCT02434497](https://clinicaltrials.gov/study/NCT02434497) | Phase 3 | 完成 | 9 | 同型合子 FH 兒童的開放label長期延伸試驗，評估長期安全性（樣本極小） |
| [NCT01078675](https://clinicaltrials.gov/study/NCT01078675) | Phase 3 | 完成 | 315 | 6–<18 歲 FH 兒童的 2 年開放試驗，評估療效、長期安全性與藥物動力學 |
| [NCT00654602](https://clinicaltrials.gov/study/NCT00654602) | Phase 3 | 完成 | 1500 | 48 週開放、非比較試驗，用於 IIa/IIb 型血脂異常（含異型合子 FH），評估達標率與安全性 |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | 完成 | 442 | 隨機開放試驗，比較 rosuvastatin 與 simvastatin 對腎臟的影響（6 週） |
| [NCT02748057](https://clinicaltrials.gov/study/NCT02748057) | Phase 3 | 完成 | 135 | 日本高膽固醇血症患者使用 ezetimibe + rosuvastatin 複方的 52 週長期安全性 |
| [NCT06910098](https://clinicaltrials.gov/study/NCT06910098) | N/A | 完成 | 195 | 不同 rosuvastatin 劑量對 LDL、CPK、AST 的影響（隨機對照） |
| [NCT07474649](https://clinicaltrials.gov/study/NCT07474649) | Phase 3 | 尚未招募 | 103 | bempedoic acid/ezetimibe/高強度他汀（atorvastatin 或 rosuvastatin）三合一療法對冠狀動脈斑塊的影響，rosuvastatin 非單一變項 |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | 完成 | 249 | alirocumab 用於異型合子 FH 的安慰劑對照試驗（非 rosuvastatin 試驗，屬同適應症的參考） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20223367](https://pubmed.ncbi.nlm.nih.gov/20223367/) | 2010 | RCT | J Am Coll Cardiol | 評估 rosuvastatin 用於 FH 兒童的療效與安全性 |
| [28838366](https://pubmed.ncbi.nlm.nih.gov/28838366/) | 2017 | Cohort | J Am Coll Cardiol | 同型合子 FH 兒童使用 rosuvastatin 的療效，並探討與基因突變的關聯 |
| [12269853](https://pubmed.ncbi.nlm.nih.gov/12269853/) | 2002 | Review | Drugs | 於 6–52 週試驗中，rosuvastatin 改善血脂的效果優於 atorvastatin、simvastatin 與 pravastatin |
| [15531000](https://pubmed.ncbi.nlm.nih.gov/15531000/) | 2004 | Review | Clin Ther | 回顧 rosuvastatin 用於高脂血症，適應症包含同型合子 FH |
| [26387811](https://pubmed.ncbi.nlm.nih.gov/26387811/) | 2016 | 藥動學研究 | Eur J Clin Pharmacol | 異型合子 FH 兒童的族群藥動學 |
| [36928267](https://pubmed.ncbi.nlm.nih.gov/36928267/) | 2023 | Cohort | J Atheroscler Thromb | 日本真實世界高風險 ASCVD 患者的 LDL-C 目標達成率 |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Guideline | Endocr Pract | AACE/ACE 血脂異常處置與心血管疾病預防指引 |
| [40254247](https://pubmed.ncbi.nlm.nih.gov/40254247/) | 2025 | 前臨床研究 | Toxicology | 以 FH 患者 iPSC 衍生骨骼肌細胞比較親脂性與親水性他汀的肌毒性 |
| [24849689](https://pubmed.ncbi.nlm.nih.gov/24849689/) | 2014 | 文獻回顧 | Consult Pharm | 他汀相關新發糖尿病的文獻回顧 |
| [20531065](https://pubmed.ncbi.nlm.nih.gov/20531065/) | 2010 | Case report | South Med J | 一名 65 歲患者使用 rosuvastatin 後發生嚴重血小板低下 |

---

## 香港上市資訊

香港共有 20 張有效單方許可證，以下列出 5 張代表性許可證（資料中未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65620 | ROSETOR 5 TABLETS 5MG | 錠劑（5mg） | 請參考原廠仿單 |
| HK-65073 | VICKROSTOR TABLETS 10MG | 錠劑（10mg） | 請參考原廠仿單 |
| HK-64427 | ROSUVASTATIN ALVOGEN TABLETS 20MG | 錠劑（20mg） | 請參考原廠仿單 |
| HK-61457 | APO-ROSUVASTATIN TABLET 20MG | 錠劑（20mg） | 請參考原廠仿單 |
| HK-61142 | ROSUVASTATIN SANDOZ TAB 10MG | 錠劑（10mg） | 請參考原廠仿單 |

---

## 安全性考量

- **知識圖譜標示之禁忌或需謹慎疾病**：肝臟疾病、膽囊疾病、甲狀腺功能低下（含黏液水腫、先天性甲狀腺功能低下）、肌病變、肌肉疾病、家族性週期性麻痺、藥物濫用/依賴、橫紋肌溶解症、蛋白尿等。（此為知識圖譜關聯，非仿單原文。）
- **藥物交互作用**：共查得 100 筆，其中較需注意的包括：
  - **嚴重 (Major)**：Fenofibrate、Atazanavir
  - **中度 (Moderate)**：Atorvastatin、Ezetimibe、Bempedoic acid、Amiodarone、Paclitaxel、Ethanol、Apalutamide 等
- **其他提示**：文獻提及他汀可能與罕見血小板低下、新發糖尿病及肌肉症狀相關；兒童使用時需注意劑量與安全性監測（CK、肝功能）。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個已完成的 Phase 3 試驗（包含兒童異型合子與同型合子 FH 的雙盲安慰劑對照試驗），且機轉與原適應症直接相關，證據等級為 L1。
- 此適應症與既有的同型合子 FH 適應症重疊，屬於適應症延伸，風險相對可控，但需有安全防護。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認各許可證的核准適應症、警語與禁忌（目前缺乏）
- 取得詳細的作用機轉資料（MOA）
- 建立兒童劑量與安全性監測計畫（CK、肝酵素）
- 完成 DDI 審查，特別是與 fenofibrate、atazanavir 的併用
- 依基因型（異型合子 vs 同型合子）釐清療效差異
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

