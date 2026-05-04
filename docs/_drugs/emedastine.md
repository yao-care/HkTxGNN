---
layout: default
title: Emedastine
parent: 高證據等級 (L1-L2)
nav_order: 233
evidence_level: L2
indication_count: 2
---

# Emedastine
{: .fs-9 }

證據等級: **L2** | 預測適應症: **2** 個
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

# Emedastine：從過敏性結膜炎到過敏性蕁麻疹

## 一句話總結

Emedastine 是一種選擇性 H₁ 受體拮抗劑，主要用於過敏性結膜炎及過敏性鼻炎的治療，目前在香港尚未取得上市許可。TxGNN 模型預測它可能對**過敏性蕁麻疹 (Allergic Urticaria)** 有效，預測分數高達 99.96%，目前有 **4 篇文獻**（包含 1 個隨機雙盲多中心 RCT）支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏性結膜炎 / 過敏性鼻炎（文獻來源；香港無上市許可資料） |
| 預測新適應症 | 過敏性蕁麻疹 (Allergic Urticaria) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Emedastine 為第二代選擇性 H₁ 受體拮抗劑，具備高受體親和力、低鎮靜性及極低抗膽鹼活性。根據 Murota & Katayama（2009）的系統文獻回顧，emedastine difumarate 除已獲批用於過敏性結膜炎與過敏性鼻炎外，也在蕁麻疹、過敏性皮炎及皮膚搔癢等疾病中展現顯著療效，且心血管副作用優於部分同類藥物。

過敏性蕁麻疹的核心病理機轉為 IgE 介導的肥大細胞脫顆粒，導致組織胺大量釋放，進而活化皮膚 H₁ 受體，引發風疹塊（wheal）、紅斑（flare）與劇烈瘙癢。阻斷 H₁ 受體正是目前蕁麻疹一線藥物治療的基礎，emedastine 的作用機轉與此高度契合，屬於「同類藥理效應（class effect）」的直接延伸應用。

一項歐洲多中心隨機雙盲試驗（Pons-Guiraud et al., 2006）直接將 emedastine difumarate（2 mg 每日兩次）與 loratadine（10 mg 每日一次）在 192 名慢性特發性蕁麻疹患者中進行頭對頭比較，治療一週後 emedastine 組在皮膚受累控制（0–10% 範圍）的比例顯著高於 loratadine 組（57.1% vs. 38.2%，p=0.0019），進一步驗證了 TxGNN 預測的合理性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [17229605](https://pubmed.ncbi.nlm.nih.gov/17229605/) | 2006 | RCT（雙盲、主動對照、多中心） | European Journal of Dermatology | Emedastine 2 mg bid 對比 loratadine 10 mg qd 治療慢性特發性蕁麻疹（n=192）：第一週後 emedastine 組皮膚受累 0–10% 比例顯著較高（57.1% vs. 38.2%，p=0.0019），總症狀積分 0–1 分比例亦優於對照組（83.3% vs. 64.5%，p=0.0134） |
| [19558341](https://pubmed.ncbi.nlm.nih.gov/19558341/) | 2009 | Narrative Review | Expert Opinion on Pharmacotherapy | Emedastine difumarate 為選擇性 H₁ 拮抗劑，可改善過敏性鼻炎、結膜炎、蕁麻疹、過敏性皮炎及皮膚搔癢等多種過敏症狀，心血管副作用少，抗膽鹼活性低，在組織重塑抑制方面亦有潛力 |
| [24720119](https://pubmed.ncbi.nlm.nih.gov/24720119/) | 2013 | Guideline Analysis / Policy Review | Przeglad Lekarski | 分析波蘭蕁麻疹治療指引與上市許可文件（SPC）之差異，涉及抗組織胺藥物（含 emedastine）在蕁麻疹治療中的法規認定與實際處方證據之落差 |
| [14499249](https://pubmed.ncbi.nlm.nih.gov/14499249/) | 2003 | Animal Study（鼠模型） | Clinical Immunology | 在鼠接觸性過敏模型中，以 emedastine difumarate 作為比較藥物，評估抗組織胺藥物對皮膚嗜酸性球浸潤的影響，結果顯示 H₁ 拮抗劑對組織胺誘發的風疹有效，但對其他嗜酸性球驅動之皮膚病影響有限 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
TxGNN 模型給予 99.96% 的高預測分數，且有來自歐洲多中心 RCT 的直接人體試驗證據，顯示 emedastine 在慢性特發性蕁麻疹中的療效優於已廣泛使用的 loratadine，機轉關聯性明確。然而，emedastine 目前在香港無任何上市許可，完整安全性資料（MOA、警語、禁忌症）尚待補充，且需進一步釐清口服劑型的現有法規地位。

**若要推進需要：**
- 補充 DrugBank 完整安全性資訊（MOA、toxicity、DDI 資料）
- 調閱原廠仿單（Emadine® 等品牌）以了解警語、禁忌症及藥物交互作用
- 評估在香港申請口服劑型過敏性蕁麻疹適應症的可行性（emedastine 口服劑型在各市場許可狀態不一）
- 與第二代抗組織胺競品（bilastine、fexofenadine、cetirizine）進行市場定位分析，評估差異化優勢
- 就冷性蕁麻疹（cold urticaria，預測排名第 2，TxGNN 分數 99.82%）另行評估，作為潛在第二適應症候選
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

