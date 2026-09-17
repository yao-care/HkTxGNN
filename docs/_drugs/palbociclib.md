---
layout: default
title: Palbociclib
parent: 僅模型預測 (L5)
nav_order: 553
evidence_level: L5
indication_count: 10
---

# Palbociclib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Palbociclib：從乳癌到多項潛在新適應症評估

## 一句話總結

Palbociclib 是 CDK4/6 選擇性抑制劑，原用於 HR+/HER2- 晚期乳癌治療（阻斷 Rb 磷酸化以抑制細胞週期進展）。TxGNN 模型針對此藥物產出 **10 個候選新適應症**，經逐一比對臨床試驗與文獻後，僅**骨髓性白血病（Myeloid Leukemia）**有實質支持（**L2**，5 個臨床試驗＋多篇轉譯研究），**類風濕性關節炎**有初步機轉訊號但僅個案報告等級（L4），**血栓性疾病**的既有證據方向與治療假說**相反**（顯示為風險訊號而非療效訊號），其餘 7 項預測目前完全缺乏臨床或文獻佐證（L5）。本藥物香港未上市，無許可證資料。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 乳癌（HR+/HER2- 晚期乳癌，取自文獻與試驗上下文） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 預測新適應症總數 | 10 項（TxGNN rank 9612–18650） |
| 最具證據之候選 | 骨髓性白血病 (Myeloid Leukemia)，L2，Proceed with Guardrails |
| 需留意之負向訊號 | 血栓性疾病（thrombotic disease）——證據指向風險而非療效 |

### 10 項預測總覽（依證據強度排序）

| 排名(TxGNN) | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|---|---|---|---|---|---|
| 6 | 骨髓性白血病 (Myeloid Leukemia) | 98.94% | L2 | S2 | **Proceed with Guardrails** |
| 2 | 類風濕性關節炎 (Rheumatoid Arthritis) | 99.36% | L4 | S1 | Research Question |
| 3 | 血栓性疾病 (Thrombotic Disease) | 99.32% | L4 | S0 | **Hold（負向訊號）** |
| 7 | 多發性內分泌腫瘤 (MEN) | 98.86% | L5 | S0 | Hold（試驗比對為假陽性） |
| 1 | 甲狀腺機能亢進 (Hyperthyroidism) | 99.44% | L5 | S0 | Hold |
| 4 | 甲狀腺荷爾蒙受體 β 突變抗性 | 99.30% | L5 | S0 | Hold |
| 5 | 短指併指症候群 | 98.996% | L5 | S0 | Hold |
| 8 | 缺損性小眼球-肢近端發育不良症候群 | 98.85% | L5 | S0 | Hold |
| 9 | 高甲狀腺素血症 | 98.78% | L5 | S0 | Hold |
| 10 | 變異型心絞痛 (Prinzmetal Angina) | 98.75% | L5 | S0 | Hold |

---

## 為什麼這個預測合理？（以骨髓性白血病為主軸）

Palbociclib 為 CDK4/6 選擇性抑制劑，阻斷 Rb 蛋白磷酸化，使細胞停滯於 G1-S 期。急性骨髓性白血病（AML）芽細胞，尤其 **MLL(KMT2A)-rearranged** 及 **t(8;21)** 亞型，對 CDK6 依賴性高，這些亞型的細胞增生高度仰賴 CDK4/6 路徑，因此在機轉上具有合理的抗腫瘤基礎。

多篇轉譯研究顯示 palbociclib 可與現有 AML 治療藥物產生協同效應：與 venetoclax（BCL2 抑制劑）＋azacitidine 併用可提升療效並**克服 venetoclax 抗藥性**；與 CPX-351（微脂體化療）併用已完成 Phase 1/2 試驗。目前已有 5 個註冊臨床試驗，其中 3 個評級為「高度相關（A級）」，1 個已完成（NCT03844997），顯示此方向已從機轉假說進入臨床驗證階段。

相對地，類風濕性關節炎僅有 1 篇個案報告（乳癌患者用藥期間關節炎症狀改善）搭配動物模型機轉研究支持，屬偶然臨床訊號，尚無專門設計之臨床試驗；血栓性疾病則證據方向相反——多篇 FAERS 藥物不良反應通報分析顯示 CDK4/6 抑制劑與血栓栓塞事件呈**正相關**（即致栓風險而非治療效果），列出的兩個臨床試驗也非以血栓疾病為治療標的。

---

## 分項證據：骨髓性白血病（Myeloid Leukemia）— L2, Proceed with Guardrails

### 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03844997](https://clinicaltrials.gov/study/NCT03844997) | Phase 1/2 | 已完成 | 35 | CPX-351＋Palbociclib 治療 AML 之安全性與緩解率（ORR/CR/CRi），為目前主要證據支柱 |
| [NCT02310243](https://clinicaltrials.gov/study/NCT02310243) | Phase 1b/2a | 狀態未知 | 50 | Palbociclib 用於 MLL-rearranged 急性白血病，需查證後續結果 |
| [NCT05627232](https://clinicaltrials.gov/study/NCT05627232) | Phase 1 | 招募中 | 24 | Palbociclib 前導治療續以 CPX-351 治療復發/難治型 AML |
| [NCT03132454](https://clinicaltrials.gov/study/NCT03132454) | Phase 1 | 進行中（未招募） | 32 | Palbociclib 單獨或併用 sorafenib/decitabine/dexamethasone 治療復發/難治型白血病 |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | 已終止 (n=2) | 2 | 多癌別分子導向 basket trial，AML 專一性較低，證據力有限 |

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41468895](https://pubmed.ncbi.nlm.nih.gov/41468895/) | 2026 | Translational | Cell Reports Medicine | CDK4/6 抑制克服 venetoclax 抗藥機轉，302 例患者樣本分析＋PDX 模型顯示協同活性 |
| [36076608](https://pubmed.ncbi.nlm.nih.gov/36076608/) | 2022 | Preclinical/Translational | Biomed Pharmacother | Palbociclib 提升 Venetoclax+Azacitidine 治療 AML 之療效 |
| [38430306](https://pubmed.ncbi.nlm.nih.gov/38430306/) | 2024 | Case Report | Cancer Chemother Pharmacol | Palbociclib＋Venetoclax＋Azacitidine 成功治療復發難治型治療相關 AML |
| [33068248](https://pubmed.ncbi.nlm.nih.gov/33068248/) | 2021 | Preclinical | Int J Hematol | CDK4/6 抑制併用自噬抑制在 t(8;21) AML 細胞誘發協同凋亡 |
| [40482924](https://pubmed.ncbi.nlm.nih.gov/40482924/) | 2025 | Preclinical | J Control Release | 抗體導向 FLT3/CDK4/6 雙標靶藥物遞送治療 AML |
| [27323399](https://pubmed.ncbi.nlm.nih.gov/27323399/) | 2016 | Mechanistic | Oncotarget | FLT3-ITD 訊號經由 HCK 誘導 CDK6 過度表現，AML 對 CDK6 具依賴性 |
| [30381403](https://pubmed.ncbi.nlm.nih.gov/30381403/) | 2018 | Genomic | Blood Advances | MLL-rearranged AML 中 CCND3（CDK4/6 上游）反覆突變 |
| [34430715](https://pubmed.ncbi.nlm.nih.gov/34430715/) | 2021 | Preclinical (xenograft) | Biochem Biophys Rep | CDK4/6＋自噬雙標靶療法於 t(8;21) AML 小鼠異種移植模型有效 |
| [34958208](https://pubmed.ncbi.nlm.nih.gov/34958208/) | 2022 | Drug Discovery | J Med Chem | 開發 CDK6/PIM1 雙重抑制劑用於 AML 治療 |
| [38890447](https://pubmed.ncbi.nlm.nih.gov/38890447/) | 2024 | Preclinical | Leukemia | NUP98 重排白血病依賴 CDK6/FLT3，Menin＋激酶抑制劑併用具療效 |

---

## 分項證據：類風濕性關節炎（Rheumatoid Arthritis）— L4, Research Question

無相關臨床試驗登記。

### 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39940918](https://pubmed.ncbi.nlm.nih.gov/39940918/) | 2025 | Preclinical (動物模型) | Int J Mol Sci | SPACIA1/SAAL1 上調 CDK6（非 CDK4）驅動關節炎小鼠滑膜增生 |
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Cohort | The Oncologist | HR+/HER2- 乳癌患者使用 CDK4/6 抑制劑期間自體免疫疾病盛行率之觀察研究 |
| [33587021](https://pubmed.ncbi.nlm.nih.gov/33587021/) | 2021 | Case Report | Mod Rheumatol Case Rep | 乳癌患者接受 palbociclib 治療期間類風濕性關節炎症狀改善之個案 |
| [25165034](https://pubmed.ncbi.nlm.nih.gov/25165034/) | 2016 | Preclinical (動物模型) | Ann Rheum Dis | CDK 抑制劑併用細胞激素阻斷可減緩關節炎動物模型病程，且不增加免疫抑制 |

---

## 分項證據：血栓性疾病（Thrombotic Disease）— L4, **Hold（負向訊號，非治療方向）**

⚠️ 此候選之現有證據方向與治療假說**相反**：多篇 FAERS 藥物不良反應通報分析顯示 CDK4/6 抑制劑（含 palbociclib）與血栓栓塞事件呈正相關，屬**已知安全性風險訊號**，而非治療效果訊號。

### 臨床試驗證據（皆非以血栓疾病為治療標的）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05468697](https://clinicaltrials.gov/study/NCT05468697) | Phase 1/2 | 進行中（未招募） | 60 | Belzutifan＋Palbociclib 治療腎細胞癌，非血栓適應症 |
| [NCT05371275](https://clinicaltrials.gov/study/NCT05371275) | Phase 2 | 已撤回 (n=0) | 0 | Palbociclib 用於 COVID-19 住院病人以預防血栓性發炎，已撤回 |

### 文獻證據（安全性風險訊號為主）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36794339](https://pubmed.ncbi.nlm.nih.gov/36794339/) | 2023 | Real-world Pharmacovigilance | Expert Opin Drug Saf | CDK4/6 抑制劑與血栓栓塞事件之真實世界藥物警戒研究＋系統性回顧 |
| [39123221](https://pubmed.ncbi.nlm.nih.gov/39123221/) | 2024 | Pharmacovigilance (FAERS) | BMC Pharmacol Toxicol | 三種 CDK4/6 抑制劑不良事件比較分析 |
| [39083396](https://pubmed.ncbi.nlm.nih.gov/39083396/) | 2025 | Pharmacovigilance (FAERS) | Expert Opin Drug Saf | FAERS 不成比例分析評估 CDK4/6 抑制劑相關不良事件 |
| [41496429](https://pubmed.ncbi.nlm.nih.gov/41496429/) | 2026 | Pharmacovigilance (FAERS) | Breast | 高齡女性 CDK4/6 抑制劑毒性之年齡分層分析 |
| [35300061](https://pubmed.ncbi.nlm.nih.gov/35300061/) | 2022 | Cohort (real-world) | Cancer Manag Res | Ribociclib 併用內分泌治療之血栓栓塞事件真實世界資料 |
| [37994878](https://pubmed.ncbi.nlm.nih.gov/37994878/) | 2023 | Review | Expert Opin Drug Saf | CDK4/6 抑制劑之間質性肺病與骨髓抑制等安全性回顧 |
| [38390439](https://pubmed.ncbi.nlm.nih.gov/38390439/) | 2024 | Case Report | SAGE Open Med Case Rep | Ribociclib 治療期間發生腦靜脈竇栓塞個案 |
| [39302147](https://pubmed.ncbi.nlm.nih.gov/39302147/) | 2025 | Preclinical | Cardiovasc Res | dsDNA 經 cGAS 路徑增強血小板活化與血栓形成（機轉研究，非藥物特異） |
| [27098250](https://pubmed.ncbi.nlm.nih.gov/27098250/) | 2016 | Preclinical (動物模型) | Circ Cardiovasc Genet | CDKN2A 缺失小鼠巨核細胞生成與血小板活性增強 |

---

## 其他候選簡述

- **多發性內分泌腫瘤 (MEN)**：TxGNN 比對出 26 個臨床試驗，但檢視後皆為 palbociclib 併用內分泌治療之**乳癌**試驗，非針對 MEN（MEN1/RET 基因突變症候群）設計，屬檢索假陽性，無實質支持證據。
- **甲狀腺機能亢進、甲狀腺荷爾蒙受體 β 突變抗性、短指併指症候群、缺損性小眼球-肢近端發育不良症候群、高甲狀腺素血症、變異型心絞痛**：以上 6 項**無任何臨床試驗或文獻登記**，僅為 TxGNN 知識圖譜嵌入之高分預測，機轉上與 CDK4/6 路徑無已知關聯，建議 Hold。

---

## 香港上市資訊

Palbociclib 目前**未於香港上市**，無許可證登記資料。

---

## 細胞毒性

Palbociclib 原適應症為乳癌，屬抗腫瘤藥物。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（CDK4/6 選擇性抑制劑，非傳統細胞毒性化療藥物） |
| 骨髓抑制風險 | 高（文獻回顧列為 CDK4/6 抑制劑常見不良事件之一，中性球低下為典型劑量限制毒性） |
| 血栓栓塞風險 | 中度（多篇 FAERS 藥物警戒分析顯示與血栓栓塞事件呈正相關，見上方「血栓性疾病」章節） |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | CBC（含分類）、血栓栓塞相關症狀監測；如用於 AML 適應症研究，另需監測腫瘤溶解症候群相關指標 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單（TFDA 仿單警語/禁忌資料尚未取得，列為 Blocking 等級資料缺口）。文獻層面已知的風險訊號請見上方「血栓性疾病」與「細胞毒性」章節。

---

## 結論與下一步

**決策：分適應症處理**

| 適應症 | 決策 |
|---|---|
| 骨髓性白血病 | **Proceed with Guardrails** |
| 類風濕性關節炎 | Research Question（值得追蹤，不建議直接推進） |
| 血栓性疾病 | **Hold**（證據方向相反，應視為安全性警訊而非療效方向） |
| 其他 7 項 | Hold（證據不足） |

**理由：**
骨髓性白血病方向已有 1 個完成之 Phase 1/2 試驗與多篇機轉／轉譯研究支持，CDK6 依賴性在 MLL-rearranged、t(8;21) 亞型有明確生物學基礎；其餘候選證據不足或方向相反，不建議投入資源。

**若要推進骨髓性白血病方向需要：**
- 補齊 TFDA/仿單安全性資料（目前為 Blocking 缺口，無法進入 S1 安全性初評）
- 補齊完整 MOA 與 DDI 資料
- 查證 NCT02310243（狀態未知）之最終結果
- 針對 MLL-rearranged／t(8;21) 亞型設計專一性 Phase 2 試驗，並將血栓栓塞風險納入安全性監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

