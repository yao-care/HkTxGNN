---
layout: default
title: Galantamine
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 5
---

# Galantamine
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

# Galantamine：從阿茲海默症到錐體外及運動障礙疾病

## 一句話總結

Galantamine 是一種乙醯膽鹼酯酶抑制劑（AChEI），全球已核准用於阿茲海默症的症狀治療，但在香港尚未取得上市許可。
TxGNN 模型預測其可能對 **5 種運動障礙相關疾病**有效，其中以**錐體外及運動障礙疾病（Extrapyramidal and Movement Disease）**具最高實質證據，
目前有 **2 個臨床試驗**和 **4 篇文獻**（含 1 篇 2025 年系統性回顧）支持此方向，整體證據等級為 **L3**；其餘 4 項均為 L5，建議 Hold。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 阿茲海默症（全球已核准；香港未上市，無許可證資料） |
| 最高證據預測適應症 | 錐體外及運動障礙疾病（Extrapyramidal and Movement Disease） |
| TxGNN 預測分數 | 99.88%（Rank #3029） |
| 證據等級 | L3（系統性回顧 + 觀察性研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question（錐體外疾病）/ Hold（其餘 4 項） |

---

## 五項預測適應症總覽

| 排名 | 適應症 | TxGNN 分數 | 證據等級 | 決策 |
|------|--------|-----------|---------|------|
| 1 | 心因性運動障礙（Psychogenic Movement Disorders） | 99.90% | L5 | Hold |
| 2 | 慢性抽動症（Chronic Tic Disorder） | 99.89% | L5 | Hold |
| 3 | 原發性直立性震顫（Primary Orthostatic Tremor） | 99.89% | L5 | Hold |
| 4 | 良性顫抖發作（Benign Shuddering Attacks） | 99.88% | L5 | Hold |
| **5** | **錐體外及運動障礙疾病（Extrapyramidal and Movement Disease）** | **99.88%** | **L3** | **Research Question** |

---

## 為什麼這個預測合理？

**藥物作用機轉（通用藥理知識）**
目前 MOA 正式資料尚缺，根據已知藥理，Galantamine 為雙重作用膽鹼能藥物：同時具備可逆性乙醯膽鹼酯酶抑制（增加突觸間隙 ACh 濃度）和菸鹼型乙醯膽鹼受體（nAChR）正向異位性調節的能力。原適應症為阿茲海默症認知症狀的對症治療。

**與運動障礙的機轉關聯**
錐體外症候群（EPS）的核心病理涉及紋狀體多巴胺-膽鹼能平衡失調。Galantamine 提升 ACh 張力在不同病理情境下呈現**雙向效應**：在路易體失智症（DLB）等同時存在膽鹼能缺損與帕金森樣運動特徵的情境下，AChEI 具理論治療合理性；但在藥物誘發性 EPS 或膽鹼能過度活躍的情境下，可能產生拮抗或加重效應。

**TxGNN 圖譜效應說明**
5 項預測適應症均位於知識圖譜「神經系統運動障礙」類節點鄰域，高預測分數部分可能源自圖譜拓樸相似性（鄰近效應），而非真實因果關聯——這在 L5 的 4 項疾病上尤為明顯。僅錐體外及運動障礙疾病（L3）有足夠實質證據支撐進一步評估。

---

## 臨床試驗證據

以下試驗對應**錐體外及運動障礙疾病**（排名 5，最高證據等級適應症）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00176423](https://clinicaltrials.gov/study/NCT00176423) | Phase 4 | 完成 | 117 | 精神分裂症患者輔助 Galantamine 治療認知功能；研究情境中患者普遍使用抗精神病藥，EPS 為重要安全性背景因素，可提供間接安全性參考 |
| [NCT01012167](https://clinicaltrials.gov/study/NCT01012167) | Phase 2 | 完成 | 86 | 比較 Galantamine 與 Oxytocin 對精神分裂症陰性症狀及認知功能之療效；在抗精神病藥背景下提供 Galantamine 耐受性與潛在 EPS 交互作用的參考資料 |

> ⚠️ 注意：以上 2 項試驗的**主要終點均為精神分裂症認知功能**，並非直接治療錐體外症候群，與目標適應症為間接相關。

---

## 文獻證據

以下文獻對應**錐體外及運動障礙疾病**（排名 5）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40224553](https://pubmed.ncbi.nlm.nih.gov/40224553/) | 2025 | Systematic Review | Brain Circulation | 系統性回顧 AChEI 類（含 Galantamine）在阿茲海默症治療中誘發運動障礙的相關報告；此文獻提出**矛盾性安全訊號**，顯示 AChEI 本身可能誘發 EPS，需審慎解讀 |
| [14676467](https://pubmed.ncbi.nlm.nih.gov/14676467/) | 2004 | Expert Review | Dementia and Geriatric Cognitive Disorders | 路易體失智症（DLB）藥物治療期望綜述；DLB 兼具帕金森樣運動特徵與膽鹼能缺損，為 AChEI 最具理論支持的運動障礙適應情境 |
| [20701827](https://pubmed.ncbi.nlm.nih.gov/20701827/) | 2011 | Animal Study | Int J Neuropsychopharmacology | 動物模型中 Galantamine 輔助 Risperidone/Haloperidol 對抗精神病活性及 EPS 傾向的影響；探討 nAChR 在膽鹼能-多巴胺交互中的角色 |
| [17374745](https://pubmed.ncbi.nlm.nih.gov/17374745/) | 2007 | Animal Study | J Pharmacol Exp Ther | Galantamine 抑制 Cebus 猴 d-安非他命誘發精神病樣行為；提供 AChEI 在多巴胺相關神經迴路中的前臨床機轉依據 |

---

## 各適應症個別評估

### 1. 心因性運動障礙（Psychogenic Movement Disorders）

- **TxGNN 分數**：99.90%　**證據等級**：L5
- **機轉評估**：心因性運動障礙（FND）的病理機轉為皮質-紋狀體-視丘-皮質迴路的**功能性失調**，而非神經化學性缺損。Galantamine 增加膽鹼能張力的機轉與此無直接治療邏輯連結；無任何臨床或前臨床證據支持。
- **決策**：**Hold** — TxGNN 高分很可能源自圖譜鄰近效應，非真實因果關聯

---

### 2. 慢性抽動症（Chronic Tic Disorder）

- **TxGNN 分數**：99.89%　**證據等級**：L5
- **機轉評估**：抽動症核心機轉為紋狀體多巴胺過度活躍，一線治療為多巴胺 D2 拮抗劑（haloperidol、fluphenazine）及 VMAT2 抑制劑。AChEI 增強膽鹼能張力可能誘發或加重錐體外症狀。唯一相關文獻（PMID 7375270，1980 年兒童抽動症病因綜述）年代久遠且不涉及 Galantamine。
- **決策**：**Hold** — 機轉不支持，有加重風險

---

### 3. 原發性直立性震顫（Primary Orthostatic Tremor）

- **TxGNN 分數**：99.89%　**證據等級**：L5
- **機轉評估**：POT 為稀有病，13–18 Hz 高頻震顫病因不明，現無任何機轉假說連結膽鹼酯酶抑制與 POT 治療。完全無相關臨床試驗或文獻。
- **決策**：**Hold** — 稀有病且零支持證據

---

### 4. 良性顫抖發作（Benign Shuddering Attacks）

- **TxGNN 分數**：99.88%　**證據等級**：L5
- **機轉評估**：BSA 為嬰幼兒**自限性**運動現象，通常 6 歲前自然消退，無藥物介入的臨床必要性。此族群亦無 Galantamine 安全性資料。TxGNN 預測很可能因「運動障礙」節點圖譜相似性而錯誤遷移。
- **決策**：**Hold** — 自限性疾病，無介入必要，且嬰幼兒安全性資料缺如

---

### 5. 錐體外及運動障礙疾病（Extrapyramidal and Movement Disease）

- **TxGNN 分數**：99.88%　**證據等級**：L3
- **機轉評估**：機轉訊號為「混合/複雜」。路易體失智症相關 EPS 可能是最具潛力的子族群（膽鹼能缺損 + 多巴胺能失衡，AChEI 有治療理論依據）；藥物誘發性 EPS 則方向相反，AChEI 可能加重。2025 年系統性回顧（PMID 40224553）提出矛盾性安全訊號，需優先釐清。
- **決策**：**Research Question** — 需聚焦疾病亞型分析

---

## 安全性考量

> 安全性資訊請參考原廠仿單。

**特別注意**：2025 年系統性回顧（PMID 40224553）警示，AChEI 類藥物（包含 Galantamine）本身可能**誘發**運動障礙，此矛盾性安全訊號在評估 Galantamine 用於運動障礙適應症時屬關鍵風險因子，必須列入評估核心。

---

## 結論與下一步

**決策：Hold（整體）／Research Question（錐體外及運動障礙疾病亞型）**

**理由：**
5 項預測適應症中，4 項（L5）缺乏實質支持證據、機轉關聯薄弱或為不需治療的自限性疾病，應全面 Hold。第 5 項「錐體外及運動障礙疾病」雖具 L3 證據，但 2025 年系統性回顧揭示 AChEI 可能誘發而非治療運動障礙，訊號方向存在根本矛盾，需深度亞型分析後才能確立方向。

**若要推進錐體外/運動障礙方向需要：**

- 精讀 PMID 40224553 系統性回顧全文，釐清 AChEI 誘發 EPS 的具體藥物、劑量與條件
- 針對**路易體失智症相關運動特徵**進行專項文獻搜索（此為最具理論支持的子族群）
- 取得 Galantamine 完整 MOA 資料（DrugBank API，DG002）
- 補充香港仿單安全性警語與禁忌症（DG001）
- 確認香港是否有鄰近地區（如日本、韓國）的已核准適應症可供參考，以輔助市場准入評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

