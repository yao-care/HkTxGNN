---
layout: default
title: Ezetimibe
parent: 高證據等級 (L1-L2)
nav_order: 304
evidence_level: L1
indication_count: 4
---

# Ezetimibe
{: .fs-9 }

證據等級: **L1** | 預測適應症: **4** 個
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

# Ezetimibe：從高膽固醇血症到高脂蛋白血症

## 一句話總結

Ezetimibe 是一種選擇性腸道膽固醇吸收抑制劑，已在全球廣泛用於高膽固醇血症及心血管疾病預防，但目前在香港尚未取得上市許可。TxGNN 模型預測它對**高脂蛋白血症 (Hyperlipoproteinemia)** 及**家族性高膽固醇血症 (Familial Hypercholesterolemia)** 均具有高度療效，預測分數分別達 **99.63%** 與 **99.38%**，有超過 **47 個臨床試驗**及 **39 篇文獻**支持這一方向，其中包含多個已完成的大型 Phase 3 RCT。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 全球已核准用途 | 高膽固醇血症（香港尚未上市） |
| 預測新適應症（第 1 位） | 高脂蛋白血症 (Hyperlipoproteinemia) |
| TxGNN 預測分數（第 1 位） | 99.63% |
| 預測新適應症（第 2 位） | 家族性高膽固醇血症 (Familial Hypercholesterolemia) |
| TxGNN 預測分數（第 2 位） | 99.38% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Ezetimibe 的核心作用機轉是選擇性抑制腸道刷狀緣的 **NPC1L1（Niemann-Pick C1-Like 1）蛋白**，阻斷來自飲食及膽汁的膽固醇在小腸的主動吸收通道。此一機轉可使循環 LDL-C 降低 15–20%，同時代償性上調肝臟 LDL 受體表達，進一步增強血漿膽固醇清除效率。這是針對高脂蛋白血症（尤其是 LDL 過高亞型）的直接治療機轉。

高脂蛋白血症（Hyperlipoproteinemia）為一類以血漿脂蛋白升高為特徵的代謝疾病群，家族性高膽固醇血症（Familial Hypercholesterolemia, FH）是其中因 *LDLR*、*APOB* 或 *PCSK9* 基因突變、導致 LDL 受體功能缺損的最常見單基因亞型。Ezetimibe 對這兩個適應症的機轉關聯性極強：它與 statin 構成互補的雙重降脂途徑—statin 抑制 HMG-CoA 還原酶減少膽固醇合成，ezetimibe 抑制腸道吸收減少外源輸入，兩者協同可使 LDL-C 在 statin 基礎上額外再降 10–20%。即使對 statin 效果有限的純合子 FH（HoFH）患者，ezetimibe 仍有輔助降脂的臨床價值。

全球已有多個里程碑式 Phase 3 RCT 確立其療效：IMPROVE-IT（n=18,144）證實 ezetimibe 加入 simvastatin 可顯著降低心血管事件；SHARP（n=9,270）於慢性腎臟病患者同樣確立療效；2025 年 TANDEM 試驗（PMID 40347969）進一步驗證 ezetimibe 與 obicetrapib 固定劑量組合的加成降脂效益。TxGNN 的高分預測高度吻合這些既有臨床實證。

---

## 臨床試驗證據

### ▸ 高脂蛋白血症 (Hyperlipoproteinemia)

目前無以「高脂蛋白血症」為主要登記適應症的直接臨床試驗記錄。家族性高膽固醇血症屬高脂蛋白血症最重要的亞型，下方 FH 試驗提供直接支持。

### ▸ 家族性高膽固醇血症 (Familial Hypercholesterolemia)

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00704444](https://clinicaltrials.gov/study/NCT00704444) | N/A | 完成 | 11,332 | 日本最大規模指定藥物使用調查：Zetia（ezetimibe）12 週單藥或聯合療法安全性與療效，真實世界最大直接 ezetimibe 資料 |
| [NCT03867318](https://clinicaltrials.gov/study/NCT03867318) | Phase 3 | 完成 | 621 | Ezetimibe 10mg 加入 atorvastatin 治療 HeFH 或多重心血管風險因素患者，評估療效與安全性 |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | 完成 | 720 | ENHANCE 試驗：ezetimibe + simvastatin vs. simvastatin 單藥，評估 HeFH 患者頸動脈內中膜厚度（CIMT）進展 |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | 完成 | 248 | Ezetimibe + simvastatin 在 10–17 歲 HeFH 青少年的療效與安全性 |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | 完成 | 50 | Ezetimibe 10mg 加入 atorvastatin 或 simvastatin 治療純合子 FH（HoFH）的療效與安全性 |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | 完成 | 44 | Ezetimibe 加入 atorvastatin 或 simvastatin 治療 HoFH 的長期安全性與耐受性（24 個月延伸研究） |
| [NCT06005597](https://clinicaltrials.gov/study/NCT06005597) | Phase 3 | 完成 | 407 | Obicetrapib 10mg + ezetimibe 10mg 固定劑量組合於 HeFH 和/或 ASCVD 患者，加入最大耐受降脂療法 |
| [NCT02748057](https://clinicaltrials.gov/study/NCT02748057) | Phase 3 | 完成 | 135 | Ezetimibe 10mg + Rosuvastatin 聯合用於日本高膽固醇血症患者長期安全性（52 週） |
| [NCT01730040](https://clinicaltrials.gov/study/NCT01730040) | Phase 3 | 完成 | 355 | Alirocumab vs. ezetimibe 加入 atorvastatin，HeFH 及高心血管風險患者頭對頭比較 |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | 終止 | 49 | Ezetimibe 10mg/day 全球治療用途研究（HoFH 族群），因計畫原因終止，仍提供 HoFH 直接用藥資料 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | Phase 3 RCT | *Lancet* | TANDEM 試驗：obicetrapib + ezetimibe 固定劑量組合顯著降低 LDL-C，確立 ezetimibe 在新型聯合療法中的核心地位 |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | Phase 3 RCT | *JAMA* | Enlicitide（口服 PCSK9i）於 HeFH，以 ezetimibe 作為背景標準治療，支持 ezetimibe 在 FH 管理的基石角色 |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | Phase 3 RCT | *Circulation* | ORION-5：inclisiran 治療 HoFH，ezetimibe 作為允許背景療法，確認聯合使用安全性 |
| [31357887](https://pubmed.ncbi.nlm.nih.gov/31357887/) | 2020 | Phase 3 RCT | *Eur J Prev Cardiology* | Bempedoic acid + ezetimibe 固定劑量組合，在最大耐受 statin 基礎上進一步降低高心血管風險高膽固醇血症患者的 LDL-C |
| [35593194](https://pubmed.ncbi.nlm.nih.gov/35593194/) | 2022 | Systematic Review | *J Cardiovasc Pharmacol Ther* | PCSK9 抑制劑全面評述，ezetimibe 作為標準對比及聯用背景，提供療效比較數據 |
| [38599725](https://pubmed.ncbi.nlm.nih.gov/38599725/) | 2024 | Review | *Indian Heart J* | FH 2024 更新：ezetimibe 在現行指南中的治療地位及其與新型藥物的協同使用 |
| [37762244](https://pubmed.ncbi.nlm.nih.gov/37762244/) | 2023 | Review | *Int J Mol Sci* | 餐後高脂血症病理機轉與治療，包含 ezetimibe 透過 NPC1L1 抑制影響脂蛋白代謝的機轉討論 |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | *Nat Rev Disease Primers* | 家族性高膽固醇血症 Primer：遺傳機轉、診斷標準與治療策略（含 ezetimibe 聯合療法） |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Clinical Guidance | *European Heart J* | EAS 共識聲明：FH 診斷不足與治療建議，確立 ezetimibe 為 statin 不耐或達標不足患者的標準二線選擇 |
| [21127699](https://pubmed.ncbi.nlm.nih.gov/21127699/) | 2010 | Review | *Vasc Health Risk Manag* | Statin + ezetimibe 聯合療法用於 FH：多項研究短中期有效且安全，現已成為 HeFH 成人及兒童的標準治療方案 |

---

## 香港上市資訊

Ezetimibe 目前在香港**尚未取得藥品許可證**，無本地上市記錄。

> 備註：Ezetimibe（品牌名 Zetia®、Ezetrol®）已在美國 FDA、歐盟 EMA、日本 PMDA、台灣 TFDA 等多個主要市場取得高膽固醇血症或混合性高脂血症的核准適應症，香港市場的引入需另行向衛生署藥劑業及毒藥監管局申請藥品登記。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **資料缺口提示**：本報告安全性資料（TFDA 仿單警語、禁忌症及藥物交互作用）均待補充（Data Gap DG001、DG002），建議優先查閱原廠仿單 PDF 及 DrugBank 資料庫，取得完整安全性資訊後方可進行正式評估。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Ezetimibe 在高脂蛋白血症及家族性高膽固醇血症的療效已獲全球多個大型 Phase 3 RCT 確立（IMPROVE-IT n=18,144；SHARP n=9,270；ENHANCE n=720 等），TxGNN 預測分數（第 1 位 99.63%、第 2 位 99.38%）與現有臨床實證高度吻合，證據等級達 L1。香港雖尚無本地許可，但科學依據與臨床需求均充分，具備推進評估的條件。

**附注（其他預測適應症）：**
- 排名第 3：CYP7A1 缺乏性高膽固醇血症（L4）—機轉上有間接合理性，但無直接臨床試驗，建議列為**研究問題（Research Question）**，暫不投入資源。
- 排名第 4：CETP 缺乏症（L4）—機轉邏輯存在根本性問題（CETP 缺乏患者表現為 LDL 偏低而非升高，ezetimibe 降 LDL 機轉於此族群缺乏治療依據），**建議排除（Hold）**。

**若要推進需要：**
- 向香港衛生署藥劑業及毒藥監管局提交藥品登記申請，評估是否可引用境外 RCT 資料免除或縮減橋接試驗要求
- 補充完整安全性資料：TFDA 仿單警語、禁忌症及主要藥物交互作用（DDI）清單（修復 DG001）
- 補充詳細作用機轉（MOA）文獻資料（修復 DG002），以強化機轉關聯性分析
- 確認香港本地目標族群規模：HeFH 患者（估計盛行率 1:250）、他汀耐受性不良患者及高心血管風險族群
- 評估與現有降脂藥物（statin、PCSK9 抑制劑）的市場定位及聯合使用策略
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

