---
layout: default
title: Nepafenac
parent: 高證據等級 (L1-L2)
nav_order: 612
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Nepafenac：預測新適應症為眼部疾病 (Eye Disease)（證據等級 L1）。原適應症：香港許可證資料未載明（依文獻與試驗，主要為白內障術後眼部發炎與疼痛）"
monitor_inn: "NEPAFENAC"
predicted_indications: ["eye disease", "optic papillitis", "hypotrichosis simplex of the scalp", "seborrheic keratosis", "von Hippel anomaly"]
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

# Nepafenac：從眼科術後發炎與疼痛到眼部疾病（Eye Disease）

## 一句話總結

Nepafenac 是一種外用非類固醇消炎藥（NSAID）前驅藥，已在香港以眼用懸浮液上市。
TxGNN 模型預測它可能對**眼部疾病 (Eye Disease)** 有效，
目前有 **40 個臨床試驗**和 **20 篇文獻**支持這個方向，其中多項為已完成的 Phase 3 試驗。
需要注意：此藥本身已用於眼科適應症，所以這個預測較接近對既有用途的確認，而非全新的藥物再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明（依文獻與試驗，主要為白內障術後眼部發炎與疼痛） |
| 預測新適應症 | 眼部疾病 (Eye Disease) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Nepafenac 是前驅藥，滴入眼睛後經眼組織水解酶轉換為活性代謝物 amfenac，後者抑制 COX-1 與 COX-2。前列腺素合成減少後，可降低眼部發炎、疼痛及血液－視網膜屏障的破壞。

這個機轉支持它用於白內障術後發炎與疼痛、預防囊樣黃斑部水腫（CME），以及視網膜相關的發炎性水腫。前臨床研究顯示，外用 nepafenac 可抑制糖尿病大鼠的視網膜微血管病變和眼部新生血管，並抑制兔子的發炎性視網膜水腫。

「眼部疾病」是很廣的類別，建議落實到具體情境：白內障術後發炎與疼痛、CME 預防，以及視網膜前膜手術後恢復。目前缺乏詳細的作用機轉資料欄位，上述機轉說明來自模型分析與文獻。

---

## 臨床試驗證據

目前共有 40 個相關試驗，以下列出最相關的 10 個（優先列出較大型、已完成的 Phase 3 與經評級的試驗）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | 完成 | 2120 | Nepafenac 0.3% 用於預防與治療白內障術後眼部發炎與疼痛 |
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | 完成 | 881 | Nepafenac 0.3% 對照載體，用於糖尿病患者白內障術後臨床結果 |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | 完成 | 819 | 與上項設計相同的平行試驗，評估糖尿病患者術後結果 |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | 完成 | 1342 | Nepafenac 0.3% 對 0.1% 與載體，用於白內障術後發炎與疼痛 |
| [NCT03499873](https://clinicaltrials.gov/study/NCT03499873) | Phase 3 | 完成 | 448 | 學名 nepafenac 0.3% 與 Ilevro 的臨床等效性試驗 |
| [NCT00333255](https://clinicaltrials.gov/study/NCT00333255) | Phase 3 | 完成 | 267 | Nevanac 0.1% 對照 Acular LS，用於白內障術後發炎 |
| [NCT00782717](https://clinicaltrials.gov/study/NCT00782717) | Phase 2 | 完成 | 263 | NEVANAC 0.1% 對照載體，用於糖尿病視網膜病變患者白內障術後黃斑部水腫 |
| [NCT01426854](https://clinicaltrials.gov/study/NCT01426854) | Phase 3 | 完成 | 260 | Nepafenac 0.1% 對照安慰劑，用於中國受試者白內障術後發炎與疼痛 |
| [NCT01021761](https://clinicaltrials.gov/study/NCT01021761) | Phase 4 | 完成 | 126 | 比較 Acuvail、Xibrom、Nevanac 對 PGE2 的抑制效果 |
| [NCT07736690](https://clinicaltrials.gov/study/NCT07736690) | Phase 4 | 完成 | 60 | 圍手術期外用 nepafenac 與視網膜前膜手術後的解剖與功能恢復 |

另有 NCT00405730（歐洲 Phase 3，n=227）、NCT00332774（Phase 3，n=149）及 NCT03025945（n=662，術後 CME 預防）等試驗。NCT00939276（Phase 3）與 NCT00801905（Phase 2）為提前終止，解讀時需留意。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39095467](https://pubmed.ncbi.nlm.nih.gov/39095467/) | 2024 | 系統性回顧／網絡統合分析 | Eye | 比較各種外用 NSAID 於白內障術後預防黃斑部增厚及對視力的影響 |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | RCT | Korean J Ophthalmol | Nepafenac 0.1% 與 prednisolone 1% 用於微切口白內障術後發炎控制的比較 |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology Glaucoma | Nepafenac 對 prednisolone 用於雷射周邊虹膜切開術後的安全性與療效 |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clin Exp Optom | Nepafenac 眼內穿透力高，可降低術後發炎、疼痛與 CME 風險，副作用少 |
| [25686158](https://pubmed.ncbi.nlm.nih.gov/25686158/) | 2015 | 系統性回顧 | Cochrane Database Syst Rev | 外用 NSAID 用於糖尿病性囊樣黃斑部水腫 |
| [26502088](https://pubmed.ncbi.nlm.nih.gov/26502088/) | 2016 | Review | Dev Ophthalmol | NSAID 於視網膜疾病的臨床應用 |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | 前臨床藥動學 | Exp Eye Res | Nepafenac 及 amfenac 可分布至眼後段 |
| [17259381](https://pubmed.ncbi.nlm.nih.gov/17259381/) | 2007 | 動物研究 | Diabetes | 外用 nepafenac 抑制糖尿病大鼠視網膜微血管病變 |
| [17964407](https://pubmed.ncbi.nlm.nih.gov/17964407/) | 2007 | 病例報告 | J Cataract Refract Surg | Nepafenac 相關角膜融解（安全性警訊） |
| [40243047](https://pubmed.ncbi.nlm.nih.gov/40243047/) | 2025 | 比較研究 | Indian J Ophthalmol | 假性剝落症候群患者白內障術後 nepafenac 0.1% 與 0.3% 的比較 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67972 | NEVANAC OPHTHALMIC SUSPENSION 0.1% W/V（Novartis） | 眼用懸浮液 | 資料未載明 |
| HK-57847 | NEVANAC OPHTHALMIC SUSP 0.1%W/V（Novartis） | 眼用懸浮液 | 資料未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自模型知識圖譜，並非仿單內容）：類風濕性關節炎、糖尿病、糖尿病酮酸中毒、凝血疾病、角膜炎、角結膜炎、乾眼症、乾眼病（xerophthalmia）、角膜潰瘍。
- **文獻中的安全訊號**：有 nepafenac 相關角膜融解的病例報告（患者有全身性移植物抗宿主病）。角膜表面已有病變的患者宜特別小心。

其他警語、禁忌與藥物交互作用，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 多項已完成的 Phase 3 試驗（含大型的白內障術後與糖尿病族群研究）及系統性回顧支持其眼科療效，證據等級為 L1。
- 但「眼部疾病」過於廣泛，且藥物已在香港上市，建議將推進範圍限定於具體情境，並注意角膜安全性。

**若要推進需要：**
- 明確定義目標適應症（白內障術後發炎／疼痛、CME 預防、視網膜前膜手術後恢復），而非籠統的「眼部疾病」。
- 取得香港仿單的核准適應症、警語與禁忌，確認與現行標示是否一致。
- 針對角膜炎、乾眼症、角膜潰瘍及糖尿病患者制定風險評估與監測計畫。
- 補充詳細的作用機轉資料。

---

### 其他預測適應症（供參考）

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----------|-----------|---------|------|
| 視神經乳頭炎 (Optic papillitis) | 99.84% | L4（僅一項兔子前臨床研究） | Hold |
| 頭皮單純性毛髮稀少症 | 99.84% | L5 | Hold |
| 脂漏性角化症 | 99.83% | L5 | Hold |
| von Hippel 異常 | 99.82% | L5 | Hold |

這四項皆缺乏直接的臨床證據，高分可能反映知識圖譜中的關聯，不建議推進。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

