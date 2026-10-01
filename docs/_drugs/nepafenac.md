---
layout: default
title: Nepafenac
parent: 高證據等級 (L1-L2)
nav_order: 602
evidence_level: L1
indication_count: 5
---

# Nepafenac
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

# Nepafenac：從白內障術後眼部發炎與疼痛到眼部疾病 (Eye Disease)

## 一句話總結

Nepafenac 是眼用非類固醇消炎藥 (NSAID)，文獻記載的核准用途是白內障術後的眼部發炎與疼痛。
TxGNN 模型預測它可能對**眼部疾病 (Eye Disease)** 有效，但這是範圍很廣的上位疾病名稱，證據大多來自已上市用途。
目前有 **41 個臨床試驗**和 **20 篇文獻**，其中多個已完成的 Phase 3 隨機對照試驗支持術後發炎與疼痛的用途。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 白內障術後眼部發炎與疼痛（依文獻；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 眼部疾病 (Eye Disease) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉欄位資料。從藥理特性來看，Nepafenac 是前驅藥 (prodrug)，經眼部組織水解酶轉換為 amfenac，後者抑制 COX-1 與 COX-2。前列腺素合成減少，可合理解釋它對術後眼部發炎、疼痛與黃斑部水腫的作用。前臨床與臨床資料也顯示，它經局部點眼後能到達眼後段。

「眼部疾病」是非特異性的上位疾病名稱。現有臨床證據大多反映已上市用途，也就是白內障術後的發炎與疼痛，而不是新適應症的驗證。由於原適應症與作用機轉的藥物層級欄位是空的，無法從本次輸入資料確認預測適應症與核准用途的重疊程度。若要延伸到標示外的用途，例如黃斑部水腫、雷射後或注射後的情境，需要針對個別適應症另行確認。

## 臨床試驗證據

共 41 個相關試驗，以下列出 10 個最相關者。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | 完成 | 2120 | Nepafenac 0.3% 用於預防與治療白內障術後眼部發炎與疼痛的安全性與療效 |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | 完成 | 881 | Nepafenac 0.3% 對照賦形劑，評估糖尿病患者白內障術後的臨床結果 |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | 完成 | 819 | 設計與上一項相同，同樣針對糖尿病患者白內障術後 |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | 完成 | 448 | Nepafenac 0.3% 學名藥與 Ilevro 的臨床等效性與安全性（雙盲、安慰劑對照） |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | 完成 | 260 | 中國成人白內障術後，Nepafenac 0.1% 對照安慰劑的安全性與療效 |
| [NCT00405730](https://clinicaltrials.gov/study/NCT00405730) | Phase 3 | 完成 | 227 | 歐洲研究，Nepafenac 0.1% 對照 ketorolac 與安慰劑，用於術後發炎與疼痛 |
| [NCT00939276](https://clinicaltrials.gov/study/NCT00939276) | Phase 3 | 已終止 | 175 | 評估 Nevanac 對糖尿病視網膜病變患者術後黃斑部水腫的效果；提前終止，結論力有限 |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Phase 2 | 完成 | 263 | 糖尿病視網膜病變患者白內障術後，評估 Nevanac 降低黃斑部水腫發生率 |
| [NCT01331005](https://clinicaltrials.gov/study/NCT01331005) | Phase 2 | 完成 | 125 | 局部 NSAID 對非中心性糖尿病黃斑部水腫黃斑體積的影響（對照安慰劑） |
| [NCT00818844](https://clinicaltrials.gov/study/NCT00818844) | Phase 4 | 完成 | 40 | 視網膜前膜手術後，Nepafenac 0.1% 對黃斑體積的影響（對照安慰劑） |

## 文獻證據

多數文獻摘要在輸入資料中被截斷，以下「主要發現」僅依可見的摘要與標題整理，不含未呈現的結果數據。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39936354](https://pubmed.ncbi.nlm.nih.gov/39936354/) | 2025 | 系統性回顧與統合分析 | Eur J Ophthalmol | 統合 RCT，評估在局部類固醇之外加用 Nepafenac 對中心黃斑厚度、黃斑體積與視力的影響 |
| [24345529](https://pubmed.ncbi.nlm.nih.gov/24345529/) | 2014 | Phase 3 試驗 | J Cataract Refract Surg | 評估每日一次 Nepafenac 0.3% 預防與治療白內障術後疼痛與發炎 |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmol Glaucoma | 雷射周邊虹膜切開術後，比較 Nepafenac 0.1% 與 prednisolone 1% 控制發炎 |
| [35196591](https://pubmed.ncbi.nlm.nih.gov/35196591/) | 2022 | RCT | Ophthalmol Glaucoma | 雷射虹膜切開術後，比較 Nepafenac 0.1% 與 bromfenac 0.09% 的安全性與療效 |
| [22795976](https://pubmed.ncbi.nlm.nih.gov/22795976/) | 2012 | 隨機對照研究 | J Cataract Refract Surg | 預防性使用 Nepafenac 或 ketorolac 對照安慰劑，評估術後黃斑體積 |
| [24345317](https://pubmed.ncbi.nlm.nih.gov/24345317/) | 2014 | 隨機前瞻研究 | Am J Ophthalmol | 評估 Nepafenac 0.1% 點眼對白內障眼睛眼壓的影響 |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | 回顧 Nepafenac 在白內障手術的角色：高眼部穿透性，副作用風險低 |
| [16466612](https://pubmed.ncbi.nlm.nih.gov/16466612/) | 2006 | Review／專家意見 | Curr Med Res Opin | 討論 Nepafenac 的眼部穿透與抑制視網膜發炎的臨床效用 |
| [17259381](https://pubmed.ncbi.nlm.nih.gov/17259381/) | 2007 | 動物研究 | Diabetes | 大鼠糖尿病模型中，局部 Nepafenac 抑制視網膜微血管病變 |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | 前臨床藥動學研究 | Exp Eye Res | 局部給藥後，Nepafenac 及其活性代謝物 amfenac 可分布至眼後段 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型／規格 | 廠商 |
|---------|------|-----------|------|
| HK-67972 | NEVANAC OPHTHALMIC SUSPENSION 0.1% W/V | 眼用懸液 0.1% w/v（依品名） | Novartis Pharmaceuticals (HK) Limited |
| HK-57847 | NEVANAC OPHTHALMIC SUSP 0.1%W/V | 眼用懸液 0.1% w/v（依品名） | Novartis Pharmaceuticals (HK) Limited |

## 安全性考量

安全性資訊請參考原廠仿單。本次未取得香港衛生署的仿單警語與禁忌資料，藥物交互作用查詢也無結果。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個已完成的 Phase 3 隨機對照試驗（樣本數達數百至兩千人），支持 Nepafenac 用於白內障術後發炎與疼痛，且已在香港上市。
- 但「眼部疾病」是非特異性上位詞，證據多反映已上市用途；新增適應症需逐項確認，安全性資料也尚未取得。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌（目前是阻斷性資料缺口）
- 補充 DrugBank 作用機轉資料，確認原適應症與預測適應症的重疊範圍
- 將「眼部疾病」拆解為具體適應症（如糖尿病患者術後黃斑部水腫），逐項評估證據
- 評估終止或小樣本試驗（如 NCT00939276）的結論限制，必要時等待更大型確認性試驗

**其他預測：** 視神經乳突炎 (optic papillitis)、頭皮單純性稀毛症、脂漏性角化症與 von Hippel 異常，證據為 L4–L5，僅有動物研究或模型預測，建議一律 Hold。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

