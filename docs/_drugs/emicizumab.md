---
layout: default
title: Emicizumab
parent: 高證據等級 (L1-L2)
nav_order: 265
evidence_level: L1
indication_count: 10
---

# Emicizumab
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Emicizumab：從先天性血友病A到獲得性凝血因子缺乏症

## 一句話總結

Emicizumab 是一種雙特異性單株抗體，核准用於先天性血友病A（含/不含 FVIII 抑制劑）的預防性治療。TxGNN 模型針對 10 項稀有出血性疾病進行預測，其中**獲得性凝血因子缺乏症（Acquired Coagulation Factor Deficiency，代表性疾病為獲得性血友病A / AHA）**的再利用證據最為充分，目前有 **1 個觀察性世代研究**和 **20 篇文獻**支持，涵蓋 Phase II 及 Phase III 前瞻性多中心臨床試驗，共識指引已於 2024 年形成。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 先天性血友病A（含/不含 FVIII 抑制劑）預防出血 |
| 最高證據新適應症 | 獲得性凝血因子缺乏症 (Acquired Coagulation Factor Deficiency) |
| TxGNN 預測分數 | 99.90%（全球排名 #2678） |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 多適應症預測總覽

本次評估為多適應症（multi）報告，以下列出全部 10 項 TxGNN 預測結果：

| 排名 | 疾病 | TxGNN 分數 | 證據等級 | 建議 |
|------|------|-----------|---------|------|
| 1 | Pseudo-von Willebrand Disease | 99.99% | L5 | Hold |
| 2 | Primary Release Disorder of Platelets | 99.99% | L5 | Hold |
| 3 | Glanzmann Thrombasthenia | 99.98% | L4 | Research Question |
| 4 | Scott Syndrome | 99.92% | L5 | Hold |
| **5** | **Acquired Coagulation Factor Deficiency** | **99.90%** | **L1** | **Proceed with Guardrails** |
| 6 | Bleeding Diathesis due to Collagen Receptor Defect | 99.86% | L5 | Hold |
| 7 | Hemorrhagic Disorder due to Constitutional Thrombocytopenia | 99.85% | L5 | Hold |
| 8 | Thrombotic Thrombocytopenic Purpura ⚠️ | 99.61% | L5 | Hold |
| 9 | Fetal and Neonatal Alloimmune Thrombocytopenia | 99.52% | L5 | Hold |
| 10 | Flood Factor Deficiency | 99.40% | L5 | Hold |

> ⚠️ **TTP 安全警示（Rank 8）**：TTP 的核心病理為 ADAMTS13 缺乏導致 UL-vWF 蓄積，造成微血管血栓與血小板消耗，屬**過度凝血**病態。Emicizumab 促進凝血酶生成恐加重微血管血栓，機轉相悖，**不建議**作為研究方向。

---

## 為什麼這個預測合理？

### 作用機轉（針對最高證據適應症：AHA）

Emicizumab 是一種雙特異性 IgG4 單株抗體，能同時結合活化第IX凝血因子（FIXa）和第X凝血因子（FX），在空間上模擬活化 FVIII（FVIIIa）的輔因子功能，從而重建內源性 Xase 複合體（FIXa–FX），恢復凝血酶（thrombin）爆發生成能力。其核心優勢在於：**完全繞過 FVIII 依賴步驟**，即使在 FVIII 抗體完全抑制內源性 FVIII 的情況下，仍可維持有效止血。皮下注射給藥（每週/每兩週/每月一次）提供長效預防性保護。

### 原適應症與新適應症的關聯性

在**獲得性血友病A（AHA）**中，患者產生針對自身 FVIII 的自體免疫抗體，導致功能性 FVIII 完全喪失——這與 Emicizumab 在先天性血友病A（先天性 FVIII 基因缺陷）中的作用場景在**分子機轉層面完全相同**：目標步驟均為 FVIII 功能缺失所造成的凝血瀑布中斷。兩種疾病的差異僅在於 FVIII 喪失的原因（先天 vs. 自體免疫），而非 Emicizumab 的作用靶點。

### 其他預測的機轉關聯性分析

- **Glanzmann 血小板無力症（Rank 3）**：GPIIb/IIIa 缺乏屬初級止血障礙，Emicizumab 的次級凝血增強理論上可提升凝血酶爆發並穩定纖維蛋白網，類似 rFVIIa 已用於此症的旁路機制。現有資料為機轉類比層次，尚需臨床驗證（L4）。
- **Ranks 1、2、4、6、7、9**：均為初級止血障礙（血小板數量或功能問題），Emicizumab 作用於次級凝血途徑，機轉間接，且均缺乏任何臨床證據，維持 Hold。
- **Scott 症候群（Rank 4）**：TMEM16F 突變導致凝血複合體組裝效率不足，Emicizumab 旁路機制理論上有關聯，但全球病例不足 50 例，研究可行性極低。

---

## 臨床試驗證據

### 獲得性凝血因子缺乏症（Rank 5）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) | N/A（觀察性） | 招募中 | 3,000 | ATHN Transcends 自然史研究，廣泛收錄出血性疾病（含 AHA）之治療實踐；可提供 Emicizumab 真實世界使用的安全性與有效性背景資料，非介入性療效試驗 |

### Glanzmann 血小板無力症（Rank 3）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) | N/A（觀察性） | 招募中 | 3,000 | 同上：含 GT 患者之治療實踐自然史資料，提供疾病背景流行病學資訊 |

---

## 文獻證據

### 獲得性凝血因子缺乏症（Rank 5）—— 20 篇文獻，以下列出最相關 10 篇

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Phase III 前瞻性多中心 | J Thromb Haemost | AGEHA 研究：前瞻性評估 Emicizumab 預防 AHA 患者出血，確認有利的效益風險比 |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Phase III 最終分析 | Thromb Haemost | AGEHA 最終分析：納入免疫抑制不適用族群（Cohort 2）及長期預防性治療資料，效益持續確認 |
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Phase II 單臂開放性 | Lancet Haematol | GTH-AHA-EMI：Emicizumab 預防 AHA 出血並允許推遲免疫抑制，達到主要終點 |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | 前瞻性世代（2年追蹤） | Blood Adv | GTH-AHA-EMI 2年追蹤：推遲免疫抑制策略獲得持續存活優勢，感染相關死亡率降低 |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | 回顧性多中心世代 | Blood Adv | 美國 12 中心 62 例 AHA 真實世界資料：Emicizumab 有效控制出血，改善患者結局 |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | 共識指引 | Hamostaseologie | GTH-AHA 工作小組共識：正式建議 Emicizumab 用於 AHA 預防性出血管理的使用規範 |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | 敘述性回顧 | J Thromb Haemost | AHA 在 Emicizumab 時代的完整管理概覽：流行病學、診斷、治療策略 |
| [38936699](https://pubmed.ncbi.nlm.nih.gov/38936699/) | 2024 | 比較分析 | J Thromb Haemost | Emicizumab 對比傳統免疫抑制治療管理 AHA 的療效與安全性比較 |
| [36795341](https://pubmed.ncbi.nlm.nih.gov/36795341/) | 2023 | 回顧 | Blood Transfus | Emicizumab 在 AHA 的利弊分析：繞過抑制劑的機轉優勢與臨床考量 |
| [38562115](https://pubmed.ncbi.nlm.nih.gov/38562115/) | 2024 | 回顧 | Haemophilia | 獲得性出血性疾病（AHA、AVWS、慢性肝病）管理新進展，包含 Emicizumab 角色 |

### Glanzmann 血小板無力症（Rank 3）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37391649](https://pubmed.ncbi.nlm.nih.gov/37391649/) | 2024 | 回顧 | Ann Hematol | rFVIIa（NovoSeven）在血友病及稀有出血疾病（含 GT）的現況；rFVIIa 已核准用於 GT，提供 Emicizumab 旁路機制的間接類比基礎 |

---

## 安全性考量

目前 Evidence Pack 中香港安全性資料（仿單警語、禁忌）尚未取得，安全性資訊請參考原廠仿單。

> **根據臨床文獻摘要整理之 AHA 適應症特別注意事項（非正式仿單資料）：**
> - **TMA 禁忌合用**：Emicizumab 與活化凝血酶原複合物濃縮劑（aPCC，如 FEIBA）合用可能導致血栓性微血管病（TMA），應避免
> - **免疫抑制治療時序決策**：需血液科專家協同評估推遲免疫抑制的適當時機
> - **FVIII 活性干擾**：Emicizumab 存在時需使用特殊方法測定 FVIII 活性及抑制劑效價，常規一期法結果不可靠

---

## 結論與下一步

**決策：Proceed with Guardrails（針對獲得性凝血因子缺乏症 / AHA，Rank 5）**

**理由：**
獲得性血友病A（AHA）具備完整的 Phase II（GTH-AHA-EMI，*Lancet Haematol* 2023）及 Phase III（AGEHA，*J Thromb Haemost* 2023、最終分析 2025）前瞻性多中心研究支持，2024 年 GTH 共識指引已正式形成；Emicizumab 的 FIXa–FX 橋接機轉在 AHA 中機轉完全契合，屬高度合理且有充分人體證據支持的再利用路徑。

**若要推進需要：**

- [ ] **香港上市申請**：Emicizumab 目前在香港未上市，須向香港衛生署申請藥物進口許可證（Drug Import Licence）或評估優先審查途徑
- [ ] **完整安全性資料**：下載並解析原廠仿單 PDF，完善警語、禁忌及 DDI 評估（特別是 aPCC 合用禁忌的完整說明）
- [ ] **作用機轉補充**：透過 DrugBank API 取得完整 MOA 描述，完善機轉關聯性分析
- [ ] **TMA 風險管控計畫**：建立明確的 aPCC 禁忌合用管理規範及 TMA 早期偵測方案
- [ ] **Glanzmann 血小板無力症（Rank 3, L4）**：可啟動初步研究問題規劃（IIT 設計或案例報告系列），探索 Emicizumab 作為 rFVIIa 替代旁路治療的可行性

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用於臨床實踐。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

