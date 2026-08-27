---
layout: default
title: Prednisolone
parent: 中證據等級 (L3-L4)
nav_order: 410
evidence_level: L3
indication_count: 5
---

# Prednisolone
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Prednisolone：從全身性抗發炎/免疫抑制治療到圓禿 (Alopecia Areata)

## 一句話總結

Prednisolone 是廣泛使用的全身性皮質類固醇，具有抗發炎與免疫抑制作用（本次 Evidence Pack 未含香港許可證登記資料，故無法列出特定原適應症）。
TxGNN 模型預測它可能對**圓禿 (Alopecia Areata)** 有效，
資料庫中共檢索到 **18 個相關臨床試驗**與 **20 篇文獻**，其中多數試驗因藥物或適應症不直接相關而評為低相關性，實際具參考價值者已篩選列出如下。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無登記資料（香港未上市，本次 Evidence Pack 未提供原適應症紀錄） |
| 預測新適應症 | 圓禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 詳細作用機轉資料（此為已知的高優先資料缺口 DG002）。根據臨床藥理學已知資訊，Prednisolone 為全身性皮質類固醇（glucocorticoid），具有廣泛的抗發炎與免疫抑制作用。

圓禿 (Alopecia Areata) 是一種由 T 細胞介導、攻擊毛囊周圍組織所導致的自體免疫性落髮疾病。皮質類固醇（含 prednisolone）能抑制 T 細胞活化與局部發炎反應，幫助毛囊恢復「免疫豁免」狀態，進而促進毛髮再生。

值得注意的是，這並非全新的藥理假說，而是對既有臨床用藥的證據再確認——口服脈衝式類固醇療法（如 methylprednisolone、prednisolone）目前已是中重度、難治性圓禿的標準或次線治療選項之一，機轉關聯明確。

---

## 臨床試驗證據

資料庫共檢索到 18 個相關試驗登記，但多數（如多項 systemic lupus erythematosus 相關的 JAK 抑制劑試驗）與圓禿或 prednisolone 無直接關聯，評為低相關性（Grade C）而未列入下表。以下為與圓禿治療直接相關的試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | 已完成 | 42 | 口服大劑量脈衝 methylprednisolone（同屬皮質類固醇）治療難治性重度圓禿，為與 prednisolone 機轉一致、最直接支持療效的試驗（相關性 A） |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A（觀察性） | 已完成 | 296 | 評估 Tofacitinib（合併或未合併 prednisolone）於落髮症患者之安全性與療效 |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | N/A | 未知 | 20 | 比較 DERMOJET 與傳統針筒進行病灶內類固醇注射於圓禿之給藥技術，非療效型 RCT（相關性 B） |

---

## 文獻證據

共檢索到 20 篇相關文獻，以下列出證據等級最高（系統性回顧、RCT、世代研究優先）之 10 篇：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network Meta-analysis | Cochrane Database Syst Rev | 比較各類圓禿治療（含免疫抑制劑、生髮刺激劑、接觸性免疫療法）之相對療效 |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | 回顧皮質類固醇脈衝療法於圓禿之療效、復發率、副作用與預後因子 |
| [30191561](https://pubmed.ncbi.nlm.nih.gov/30191561/) | 2019 | Systematic Review | Australas J Dermatol | 系統性回顧 1946–2018 年圓禿全身性治療（含 RCT）之證據 |
| [15692475](https://pubmed.ncbi.nlm.nih.gov/15692475/) | 2005 | RCT | J Am Acad Dermatol | 安慰劑對照之口服脈衝 prednisolone 治療圓禿研究 |
| [21572877](https://pubmed.ncbi.nlm.nih.gov/21572877/) | 2009 | Cohort | Dermato-endocrinology | 中劑量 prednisolone 脈衝療法於圓禿早期病灶有效，但副作用可能導致停藥 |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Retrospective Cohort | Dermatol Ther | Methylprednisolone 併用 methotrexate 治療廣泛型圓禿，療效未顯著優於單用 |
| [28140540](https://pubmed.ncbi.nlm.nih.gov/28140540/) | 2017 | Case Series/Cohort | JDDG | 序貫高劑量後低劑量全身性類固醇治療重度兒童圓禿，緩解快但停藥後易復發 |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatr Dermatol | 回顧兒童脈衝劑量皮質類固醇治療圓禿之劑量方案與副作用 |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Review | J Dermatolog Treat | 無法使用 JAK 抑制劑時，dexamethasone 口服迷你脈衝療法可達重度圓禿長期緩解 |
| [30294905](https://pubmed.ncbi.nlm.nih.gov/30294905/) | 2019 | Mechanistic Study | J Cosmet Dermatol | 口服脈衝類固醇治療圓禿可能透過降低血清與組織 TNF-α 濃度發揮作用 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 提醒：TFDA 仿單警語與禁忌資料目前為**阻斷性（Blocking）資料缺口**（DG001），在補齊前無法進入 S1 安全性初評階段。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 圓禿的自體免疫機轉與皮質類固醇的抗發炎/免疫抑制作用高度吻合，且已有系統性回顧、世代研究與一篇安慰劑對照研究支持口服脈衝 prednisolone/methylprednisolone 之療效（證據等級 L3），屬於既有用藥的證據再確認而非全新假說。
- 但缺乏正式 Phase 2/3 RCT，且藥物安全性資料（仿單警語、禁忌、DDI）尚未補齊，須以防護措施（Guardrails）方式推進。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，阻斷性缺口，優先處理）
- 取得 DrugBank 詳細作用機轉資料以強化機轉關聯性分析（DG002）
- 若考慮於香港推動此適應症，需確認當地藥物許可證與核准適應症範圍（目前查無登記資料）
- 建議規劃小規模前瞻性研究或至少回顧性世代研究，以強化 L3 → L2 的證據等級
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

