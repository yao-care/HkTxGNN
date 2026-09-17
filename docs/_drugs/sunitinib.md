---
layout: default
title: Sunitinib
parent: 高證據等級 (L1-L2)
nav_order: 716
evidence_level: L2
indication_count: 5
---

# Sunitinib
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

# Sunitinib（DB01268）：老藥新用評估－脂肪肉瘤（Liposarcoma）

## 一句話總結

Sunitinib 目前在香港未上市，原始適應症資料付之闕如（僅能由證據內容推知其原用於腎細胞癌、GIST 等領域）。
TxGNN 模型預測它可能對**脂肪肉瘤 (Liposarcoma)** 有效，
目前有 **3 個臨床試驗**和 **9 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（香港未上市，無許可證核准適應症紀錄） |
| 預測新適應症 | 脂肪肉瘤 (Liposarcoma) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DG002：MOA 資料缺口）。但根據證據包內的機轉推論，Sunitinib 為多標靶酪胺酸激酶抑制劑（RTK inhibitor），標靶包括 VEGFR1-3、PDGFR-α/β、KIT、FLT3，作用機轉以抑制腫瘤血管新生為核心。

脂肪肉瘤（尤其黏液樣型伴 FUS-DDIT3 融合基因）具高度血管新生依賴性，部分亞型也表現 PDGFR，理論上對抗血管新生治療存在反應性。不過脂肪肉瘤並非單一分子靶點驅動的疾病，其機轉關聯屬於間接推論，而非直接標靶對應。

值得注意的是，兩個 Phase 2 完成試驗（NCT00400569、NCT00474994）均直接針對含脂肪肉瘤亞型的不可切除/轉移性軟組織肉瘤族群使用 sunitinib 治療，為此預測提供臨床層級的實證基礎，而非僅止於機轉推論。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Phase 2 | 已完成 | 48 | 開放性單一機構試驗，評估 sunitinib 用於不可切除/轉移性軟組織肉瘤（含脂肪肉瘤、平滑肌肉瘤、纖維肉瘤、MFH）之劑量與療效（相關性 A 級） |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Phase 2 | 已完成 | 53 | 多中心試驗，評估 sunitinib 連續給藥治療轉移性/局部晚期非 GIST 肉瘤（含脂肪肉瘤患者），機轉為阻斷腫瘤血管新生（相關性 A 級） |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Phase 2 | 已完成 | 131 | SARC024 傘型試驗，評估 **regorafenib**（非 sunitinib）於多種肉瘤亞型之療效，僅供肉瘤治療脈絡參考，藥物不符（相關性 C 級） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | RCT/Phase2 | Int J Cancer | Sunitinib 用於復發/難治軟組織肉瘤（平滑肌肉瘤、脂肪肉瘤、MFH）之 Phase 2 安全性與療效研究 |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Review | Cancers | 脂肪肉瘤的基因、表觀遺傳與轉錄體變異回顧，探討標靶治療選擇 |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Rev Anticancer Ther | 成人軟組織肉瘤新興療法回顧 |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magyar Onkologia | 依組織學亞型分類之軟組織肉瘤藥物治療回顧 |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | 依組織學/非組織學導向之軟組織肉瘤治療，提及 trabectedin 對黏液樣脂肪肉瘤具高度活性 |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Review/Protocol | BMC Cancer | REGOSARC 試驗計畫書，背景提及 sunitinib 於軟組織肉瘤之活性數據 |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Cohort/Genomic | Oncotarget | 骨外黏液樣軟骨肉瘤次世代定序分析，評估對 sunitinib 之潛在反應因子 |
| [38717131](https://pubmed.ncbi.nlm.nih.gov/38717131/) | 2024 | Cohort/Case series | Am J Surg Pathol | 黏液樣發炎性肌纖維母細胞肉瘤 25 例臨床病理分析（間接肉瘤分子標靶脈絡） |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Case Report | Anticancer Res | 重度預治療轉移性脂肪肉瘤患者使用 sunitinib 後獲得長期臨床效益之個案報告 |

---

## 香港上市資訊

目前無香港上市許可證（未上市，`total_licenses: 0`）。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多重酪胺酸激酶抑制劑，非傳統細胞毒性化療藥物） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。（DG001：TFDA/香港仿單警語與禁忌症資料為 Blocking 等級資料缺口，尚未取得）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
兩個 Phase 2 完成試驗直接於含脂肪肉瘤亞型的軟組織肉瘤族群測試 sunitinib，並有個案報告支持長期臨床效益；機轉上（抗血管新生 TKI）與脂肪肉瘤生物學具合理連結，證據等級達 L2，但尚不足以支持無保留推進。

**若要推進需要：**
- 補齊 TFDA/香港衛生署仿單警語與禁忌症資料（DG001，Blocking，阻斷 S1 安全性初評）
- 確認完整作用機轉資料（DG002）
- 因香港未上市，需評估藥證申請或專案進口／恩慈療法途徑
- 針對黏液樣脂肪肉瘤（FUS-DDIT3 融合）等特定亞型進行生物標記驗證，以強化分子層級的患者篩選依據

---

*附註：本證據包（candidate_id: TW-DB01268-multi）另評估 4 個較弱候選適應症——ovarian myxoid liposarcoma（L4/Research Question）、Xp11.2 易位相關腎細胞癌（L4/Research Question）、unclassified renal cell carcinoma（L2/Proceed with Guardrails，具 12 篇文獻及 5 個試驗，含多個非透明細胞 RCC 之隨機對照試驗如 ASPEN、ESPN）、以及 neuroblastoma 相關腎細胞癌（L5/Hold，因資料配對錯誤，證據等同無）。若欲評估 unclassified RCC 候選，建議另行產出獨立報告。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

