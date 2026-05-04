---
layout: default
title: Adenosine
parent: 中證據等級 (L3-L4)
nav_order: 24
evidence_level: L4
indication_count: 2
---

# Adenosine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **2** 個
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

# Adenosine：從上心室性心搏過速到兒茶酚胺誘發性多型性室性心搏過速

## 一句話總結

Adenosine 是人體內源性嘌呤核苷，臨床上已廣泛用於終止上心室性心搏過速（SVT）的急性發作。TxGNN 模型預測它可能對**兒茶酚胺誘發性多型性室性心搏過速（Catecholaminergic Polymorphic Ventricular Tachycardia, CPVT）**有效，目前有 **1 個臨床試驗**（腺苷 A1 受體路徑間接驗證）和 **13 篇文獻**（含 1 篇直接病例報告）支持這個方向。

> ℹ️ **注意**：TxGNN 排名第 1 的預測（Obsolete Bundle Branch Block）因疾病本體術語已廢棄（MONDO retired term），評分被判定為知識圖譜殘留訊號（artifact），不具臨床意義，本報告以排名第 2 的 CPVT 為主要評估對象。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 上心室性心搏過速（SVT）（香港無上市許可，依通用醫學知識填入） |
| 預測新適應症 | 兒茶酚胺誘發性多型性室性心搏過速（CPVT） |
| TxGNN 預測分數 | 99.42% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

**Adenosine 的作用機轉**

Adenosine 透過激活腺苷 A1 受體（A1R），耦合 Gi 蛋白抑制腺苷酸環化酶（adenylyl cyclase），降低細胞內 cAMP 濃度，進而減弱蛋白激酶 A（PKA）活性。在心臟中，此機轉可快速抑制房室結（AV node）傳導，使其成為終止折返性 SVT 的標準急救用藥。

**CPVT 的致病路徑與腺苷的理論對抗機轉**

CPVT 的核心病理為 RyR2（心臟型 ryanodine receptor 2）功能增益突變，導致交感刺激（兒茶酚胺釋放）期間細胞內 Ca²⁺ 異常外漏，引發延遲後去極化（DAD）及致命性室性心搏過速。致病路徑可簡述如下：

> **兒茶酚胺 → β-AR → ↑cAMP → PKA 磷酸化 RyR2（Ser2808/Ser2814）→ DAD → 室速**

腺苷的訊號路徑恰好逆向而行：

> **A1R 激動 → Gi → ↓腺苷酸環化酶 → ↓cAMP → ↓PKA 活性 → ↓RyR2 過度磷酸化**

理論上，腺苷可藉由降低 cAMP/PKA 活性，對抗兒茶酚胺誘發的鈣離子失調，從而預防或終止 CPVT 發作。

**直接臨床佐證**

PMID 18313614（2008）提供最直接的臨床證據：一位 CPVT 患者在雙向性室性心搏過速（bidirectional VT）發作期間，靜脈注射 ATP（在體內迅速代謝為腺苷）後，心律成功終止並恢復正常。PMID 23747301（2013）的體外實驗進一步揭示，ATP 可與 CPVT 突變相關的 RyR2 中央結構域直接結合，從分子層面強化了機轉的合理性。此外，AGP100（選擇性 A1 腺苷受體激動劑）已進入 Phase 2a 臨床試驗（NCT07263139），顯示腺苷 A1R 路徑已受到業界認可，正式進入 CPVT 的臨床驗證階段。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07263139](https://clinicaltrials.gov/study/NCT07263139) | Phase 2a | 招募中 | 10 | 研究 AGP100（選擇性 A1 腺苷受體激動劑）用於 CPVT 患者的安全性、耐受性與初步臨床療效；AGP100 與腺苷共享 Gi/cAMP 下游訊號，屬腺苷 A1R 路徑在 CPVT 的首個 Phase 2 臨床驗證，預計 2027 年 6 月完成 |

> ⚠️ **注意**：此試驗的研究藥物為 AGP100，而非腺苷本身，屬路徑間接驗證（B 級相關性）。樣本數極小（n=10），目前仍在招募中，尚無公布結果。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case Report | Heart Rhythm | **直接佐證**：靜脈注射 ATP（代謝為腺苷）成功終止 CPVT 患者的雙向性室性心搏過速，為腺苷用於 CPVT 提供最直接的臨床案例 |
| [23747301](https://pubmed.ncbi.nlm.nih.gov/23747301/) | 2013 | In vitro mechanistic | Biochim Biophys Acta | ATP 與 CPVT 突變相關 RyR2 中央結構域直接結合，揭示腺苷核苷酸在 RyR2 分子層面的作用位點，強化機轉合理性 |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Translational/Animal | Cardiovascular Research | PDE2A/4B 基因療法透過改善 cAMP 細胞內區域分隔，有效防治心臟衰竭與心律不整，支持 ↓cAMP/PKA 路徑作為治療靶點的可行性 |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | In vitro organoid | J Physiol | 人類心臟-神經微組織模型揭示 CPVT 亦是交感神經元層面的疾病，強調腎上腺素能訊號路徑（腺苷作用的對立路徑）在 CPVT 中的核心角色 |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Clinical Review (多學會共識) | Europace | ESC/HRS/APHRS 等多學會共識聲明：心電生理藥物誘發試驗指引，包含 CPVT 診斷建議與腺苷相關藥物的使用規範 |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | Basic science | Communications Biology | TECRL 缺失導致心肌細胞粒線體功能異常，與 CPVT 部分表型相關，提示疾病異質性 |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Translational | Science Translational Medicine | SR Ca²⁺ 外漏（RyR2 路徑）是心律不整的關鍵機轉，選擇性 RyR2 穩定劑（rycal S36）可改善動物模型存活率 |
| [23858002](https://pubmed.ncbi.nlm.nih.gov/23858002/) | 2013 | Mechanistic | J General Physiology | Calsequestrin 對 RyR2 的腔內 Ca²⁺ 調控機制，在 CPVT 病理條件下功能異常 |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Observational/Case series | Heart Rhythm | RyR2 突變 CPVT 患者後起搏異常再極化現象；電生理研究（EPS）對 CPVT 診斷價值有限 |
| [18368865](https://pubmed.ncbi.nlm.nih.gov/18368865/) | 2007 | Clinical Review | J Assoc Physicians India | 結構正常心臟室性心搏過速（含 CPVT）的分類與治療邏輯；涵蓋腺苷反應性心律不整的診斷意義 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **特別提示**：Adenosine 在已知高度房室傳導阻斷、病竇症候群或嚴重低血壓患者中為禁忌。CPVT 患者在使用腺苷前，須先排除同時存在的傳導系統異常，且應在備有除顫器的監護環境下給藥。Adenosine 半衰期極短（＜10 秒），若考慮慢性 CPVT 管理需額外評估用藥策略。

---

## 結論與下一步

**決策：Hold**

**理由：**
Adenosine 對 CPVT 具有強力的機轉合理性（cAMP/PKA 路徑的鏡像對抗），且有 1 篇病例報告（PMID 18313614）提供直接臨床佐證，A1R 路徑亦已進入 Phase 2a 臨床驗證（AGP100）。然而，針對腺苷本身的直接臨床試驗缺失，現有資料僅達 L4 證據等級，且香港無上市許可，尚不具備直接推進條件。

**若要推進需要：**
- 補充 DrugBank 完整 MOA 資料，確認腺苷 A1R 路徑的藥理細節及已知交互作用
- 系統性文獻回顧：彙整所有 ATP/腺苷用於心室心律不整（尤其 CPVT）的個案報告與機轉研究
- 密切追蹤 NCT07263139（AGP100 Phase 2a）結果，評估 A1R 激動路徑在 CPVT 的臨床可行性與安全性
- 評估腺苷超短半衰期（＜10 秒）對慢性 CPVT 管理的根本限制，研究長效 A1R 激動劑或口服前體藥物（prodrug）的開發可能性
- 若追蹤 AGP100 結果正面，考慮設計針對腺苷（或 ATP）用於急性 CPVT 終止的 Proof-of-Concept 小型研究，並向相關藥監機構申請審查
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

