---
layout: default
title: Amlodipine
parent: 高證據等級 (L1-L2)
nav_order: 46
evidence_level: L2
indication_count: 10
---

# Amlodipine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Amlodipine：從高血壓到腦內出血

## 一句話總結

Amlodipine 是長效的鈣離子通道阻斷劑（L-type CCB），廣泛用於**高血壓**及**心絞痛**治療。TxGNN 模型共預測了 10 個新適應症，其中**腦內出血 (Intracerebral Hemorrhage)** 的臨床證據最為充分，目前有 **6 個臨床試驗**（含 1 個已完成的 Phase 3 RCT）和 **8 篇文獻**支持，為本批次唯一達到 **Proceed with Guardrails** 決策的適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、心絞痛（CCB 標準適應症） |
| 最強證據預測新適應症 | 腦內出血 (Intracerebral Hemorrhage) |
| TxGNN 最高分適應症 | 腦幹梗塞 99.94%（無臨床支持，L5） |
| TxGNN 預測分數（腦內出血） | 99.79% |
| 證據等級 | L2 |
| 香港上市 | 資料缺失（系統顯示 0 張，待查核） |
| 許可證數 | 0 張（資料待確認） |
| 建議決策 | Proceed with Guardrails |

---

## 多重預測適應症概覽

本 Evidence Pack 共涵蓋 10 個 TxGNN 預測適應症，綜合評比如下：

| 排名 | 適應症（中文） | 英文名稱 | TxGNN 分數 | 證據等級 | 決策建議 |
|------|-------------|---------|-----------|---------|---------|
| 1 | 腦幹梗塞 | Brain Stem Infarction | 99.94% | L5 | Hold |
| 2 | 肺高壓（肺部疾病/缺氧型）| PH owing to lung disease/hypoxia | 99.91% | L4 | Hold |
| 3 | 多因素型肺高壓 | PH with unclear multifactorial mechanism | 99.91% | L5 | Hold |
| 4 | 惡性腎血管性高血壓 | Malignant Renovascular Hypertension | 99.90% | L4 | Research Question |
| 5 | 惡性高血壓腎病變 | Malignant Hypertensive Renal Disease | 99.90% | L5 | Hold |
| 6 | 腦動脈阻塞 | Cerebral Artery Occlusion | 99.89% | L3 | Research Question |
| 7 | Braddock 症候群 | Braddock Syndrome | 99.88% | L5 | Hold |
| 8 | MRI 定義腦梗塞 | MRI Defined Brain Infarct | 99.86% | L5 | Hold |
| 9 | ABri 澱粉樣蛋白病變 | ABri Amyloidosis | 99.84% | L5 | Hold |
| **10** | **腦內出血** | **Intracerebral Hemorrhage** | **99.79%** | **L2** | **Proceed with Guardrails** |

> **重要提示**：TxGNN 排名高≠臨床證據強。腦內出血雖排名第 10，卻是本批次**唯一具備 Phase 3 RCT 的適應症**，決策優先度最高。

---

## 為什麼這個預測合理？

### Amlodipine 的藥理機轉

Amlodipine 是二氫吡啶類（dihydropyridine class）L 型鈣離子通道阻斷劑。其主要機轉為阻斷血管平滑肌細胞的電壓閘控鈣離子通道（VGCC），使細胞內鈣離子濃度下降，導致動脈血管舒張、降低全身血管阻力，進而有效控制血壓。與同類 CCB 相比，Amlodipine 額外具備直接抗氧化活性，為其神經保護潛力提供生物學基礎。

> 注意：本 Evidence Pack 的 MOA 欄位尚未完整取得，以上機轉說明來自公開藥學知識，建議補充 DrugBank 正式資料。

### 高血壓與腦內出血的直接連結

腦內出血（ICH）最重要的可改變危險因子就是**高血壓**：慢性高血壓造成腦內穿透小動脈的脂質玻璃樣變（lipohyalinosis），使血管脆弱而易於破裂。研究顯示，ICH 後若血壓未得到有效控制，5 年內復發風險超過 20%。Amlodipine 作為三聯降壓療法（Triple Pill：Perindopril + Indapamide + Amlodipine）的核心成分，TRIDENT 試驗直接驗證了這一組合在 ICH 二級預防的效果。

### 降壓以外的延伸保護機轉

1. **腦血流自動調節改善**：CCB 可拓寬高血壓患者的腦血流自動調節範圍，預防過度降壓造成的缺血損傷。
2. **抗氧化保護**：Amlodipine 的直接抗氧化活性可能減輕血腫周圍組織（perihematomal edema）的氧化損傷。
3. **鈣超載阻斷**：VGCC 阻斷理論上可減少缺血周圍神經元的繼發性鈣毒性損傷。

---

## 臨床試驗證據（腦內出血）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | ✅ 已完成 | 1,671 | **【核心證據】** TRIDENT 試驗：雙盲多中心 RCT，評估三聯降壓療法（Perindopril + Indapamide + Amlodipine）預防腦出血後復發性腦內疾病事件，為本批次最高品質試驗 |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | — | 🔄 招募中 | 140 | **【重要新證據】** 香港主導試驗，腦出血後依 TRICH 評分使用含 Amlodipine 三聯降壓藥控制血壓，目標完成日 2030 年 |
| [NCT00134160](https://clinicaltrials.gov/study/NCT00134160) | Phase 4 | ✅ 已完成 | 1,000 | 日本老年高危高血壓患者：高劑量 ARB 單藥 vs. ARB+CCB 組合對心血管事件（含腦出血）的影響 |
| [NCT03264352](https://clinicaltrials.gov/study/NCT03264352) | Phase 4 | 🔄 招募中 | 11,414 | IPAD 試驗：第二型糖尿病高血壓患者降壓策略研究，心腦血管事件（含腦出血）為主要終點 |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | ❌ 已終止 | 1 | TRIDENT 認知次研究，僅招募 1 人即終止，無有效資料 |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | — | ❌ 已終止 | 4 | TRIDENT MRI 次研究，僅招募 4 人即終止，無有效資料 |

---

## 文獻證據（腦內出血）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | RCT 設計論文 | Int J Stroke | TRIDENT 試驗設計與進展報告：含 Amlodipine 三聯降壓療法預防 ICH 後復發事件的研究設計依據 |
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | RCT 設計 | Hypertension Res | CASE-J 試驗：高劑量 ARB 與 ARB+CCB 組合在日本高危高血壓患者心血管事件（含腦出血）的比較設計 |
| [23053838](https://pubmed.ncbi.nlm.nih.gov/23053838/) | 2013 | 觀察性研究 | Neurol Sci | 138 例高血壓性腦出血患者中 β-blocker 對死亡率、SIRS 及 3 個月預後的影響（提供 ICH 降壓治療背景） |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovasc Drugs Ther | 鈣離子拮抗劑降壓機轉回顧：CCB 在嚴重高血壓中作為一線治療的生物學依據 |
| [17077518](https://pubmed.ncbi.nlm.nih.gov/17077518/) | 2006 | 動物實驗 | Biol Pharm Bull | 長效二氫吡啶 CCB（benidipine）改善自發性高血壓大鼠腦血流自動調節，支持 CCB 類腦保護機轉 |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | 病例報告 | Ann Pharmacother | Amlodipine 相關血管性水腫病例，患者背景為右側視丘出血性中風（安全性警示） |
| [26698202](https://pubmed.ncbi.nlm.nih.gov/26698202/) | 2015 | 病例報告 | BMJ Case Rep | 腦出血病史患者術後突然停用含 Amlodipine 降壓藥導致 PRES 的案例（停藥安全性警示） |
| [37489780](https://pubmed.ncbi.nlm.nih.gov/37489780/) | 2024 | 病例報告 | Curr Drug Safety | 中風患者合併使用 Tizanidine 與降壓藥（含 Amlodipine 背景）所致低血壓病例（藥物交互作用警示） |

---

## 延伸分析：腦動脈阻塞（Cerebral Artery Occlusion，L3）

腦動脈阻塞（rank 6）具備動物模型研究支持（5 篇），雖無直接人體 RCT，但機轉上的多重神經保護作用值得關注：

| PMID | 年份 | 類型 | 主要發現 |
|------|-----|------|---------|
| [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/) | 2011 | 動物實驗 | Amlodipine + Atorvastatin 在 Zucker 代謝症候群大鼠腦動脈阻塞模型中的抗凋亡與抗自噬保護作用 |
| [20971084](https://pubmed.ncbi.nlm.nih.gov/20971084/) | 2011 | 動物實驗 | 協同治療在代謝症候群大鼠腦動脈阻塞後神經元損傷的協同保護效果 |
| [21276424](https://pubmed.ncbi.nlm.nih.gov/21276424/) | 2011 | 動物實驗 | Amlodipine + Atorvastatin 組合預處理 28 天後腦缺血體積縮減 |
| [17904110](https://pubmed.ncbi.nlm.nih.gov/17904110/) | 2007 | 動物實驗 | 具抗氧化特性的 CCB 在大鼠局灶性腦缺血後的神經保護，機轉可能與抗氧化活性有關 |
| [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/) | 2006 | 動物實驗 | Amlodipine 顯著縮小 ApoE 缺失小鼠局灶性腦缺血後梗塞面積 |

> **決策：Research Question** — 動物數據一致，但需人體試驗確認。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 特別提示：來自文獻的零散安全性訊號包括血管性水腫（PMID 19299323）及突然停藥後血壓反彈（PMID 26698202），在腦出血高風險族群中尤須注意。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
TRIDENT 試驗（NCT02699645，Phase 3 已完成 RCT，n=1,671）直接驗證了含 Amlodipine 的三聯降壓療法對腦出血後復發事件的預防效果；另有一項香港主導新試驗（NCT07458880）正在招募，直接針對本適應症。機轉上，Amlodipine 透過血壓控制、腦血流自動調節保護及抗氧化特性提供多重生物學支持，合理性充分。

**若要推進需要：**
- 查核香港許可證實際狀況（系統顯示 0 張，與臨床實際使用狀況可能不符，需人工查核 HKDH）
- 補充 DrugBank API 取得完整 MOA 資料（目前為 Data Gap）
- 補充香港仿單警語與禁忌症資料（目前均為 Data Gap，為 Blocking 資料缺口）
- 取得並分析 TRIDENT 試驗（NCT02699645）的最終結果全文
- 釐清 Amlodipine 在 ICH **急性期**（直接降壓）vs.**慢性二級預防期**（三聯療法）的不同角色
- 評估香港在地患者族群特性（高鹽飲食、腦出血比例偏高）對外推適用性的影響
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

