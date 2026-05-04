---
layout: default
title: Duloxetine
parent: 高證據等級 (L1-L2)
nav_order: 221
evidence_level: L2
indication_count: 10
---

# Duloxetine
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

# Duloxetine：從憂鬱症／焦慮症 到 強迫症

> **⚠️ 本報告為多適應症分析（Multi-Indication Pack）**，共包含 10 項 TxGNN 預測。以下以最具臨床推進價值的適應症**強迫症（OCD）**為主軸撰寫；其餘預測見「其他預測摘要」章節。

---

## 一句話總結

Duloxetine 是一種血清素-正腎上腺素再回收抑制劑（SNRI），已於美國、歐洲等多國核准用於重度憂鬱症、廣泛性焦慮症及多種疼痛相關適應症，台灣目前**尚未上市**。
TxGNN 模型共預測出 10 項潛在新適應症；其中**強迫症（Obsessive-Compulsive Disorder, OCD）**具有最高臨床再利用價值，
目前有 **5 個臨床試驗**和 **20 篇文獻**支持，證據等級達 **L2**，為本次分析中唯一達到「Proceed with Guardrails」門檻的候選適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 重度憂鬱症、廣泛性焦慮症、疼痛相關疾患（國際核准；台灣未上市） |
| 最優先預測適應症 | 強迫症（Obsessive-Compulsive Disorder, OCD） |
| TxGNN 預測分數 | 99.84%（全球知識圖譜排名 #3,897） |
| 證據等級 | L2 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Proceed with Guardrails** |

---

## 為什麼這個預測合理？

Duloxetine 是一種雙重機轉藥物（SNRI），透過同時抑制 SERT（血清素轉運體）和 NET（正腎上腺素轉運體），雙向提升突觸間 5-HT 與 NE 的濃度。目前缺乏台灣 TFDA 仿單 MOA 原文資料，但根據國際文獻（Muscatello et al., 2019），其核准適應症涵蓋重度憂鬱症（MDD）、廣泛性焦慮症（GAD）、糖尿病周邊神經病變疼痛、纖維肌痛症及慢性肌肉骨骼疼痛，機轉均圍繞單胺類神經傳導物質的調節。

強迫症（OCD）的病理生理核心為**血清素訊號系統異常**，及前額葉—紋狀體—視丘—皮質迴路（CSTC circuit）的過度活化。SSRIs 作為 OCD 第一線藥物已有充分科學共識，驗證了血清素系統在 OCD 中的核心地位。Duloxetine 的血清素再回收抑制成分（SERT 抑制 → 突觸間 5-HT ↑ → CSTC 迴路調節 → 強迫症狀改善）直接切入此機轉；其額外的正腎上腺素成分則被多篇文獻認為對 **SSRI 抵抗性 OCD** 具潛在增效作用（augmentation strategy），彌補了純 SSRI 治療反應率僅約 70% 的臨床缺口。

現有 1 項 Phase 4 完成試驗（NCT00464698）直接評估 Duloxetine 單藥治療 OCD 的療效，1 項雙盲 RCT（PMID 27811556）評估增效治療，機轉關聯性強，預測合理性高。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00464698](https://clinicaltrials.gov/study/NCT00464698) | Phase 4 | 已完成 | 20 | 直接評估 Duloxetine 治療 OCD 療效的核心試驗，為迄今最直接的試驗設計，n=20，提供 L2 核心證據 |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | 已完成 | 26 | OCD 藥物反應預測研究，Duloxetine 為備選用藥之一（前兩線藥物試用失敗者），含療效生物標記資料 |
| [NCT02476136](https://clinicaltrials.gov/study/NCT02476136) | N/A | 未知 | 8,800 | 焦慮疾患個別病患資料大型統合分析，評估抗憂鬱藥物初始嚴重度與療效關係，OCD 可能涵蓋其中，統計力強但 OCD 特異性待確認 |
| [NCT05930912](https://clinicaltrials.gov/study/NCT05930912) | N/A | 未知 | 1 | ASD 精神科處方觀察研究（n=1），與 OCD 直接關聯性低，不納入主要證據評估 |
| [NCT01944657](https://clinicaltrials.gov/study/NCT01944657) | N/A | 已撤回 | 0 | MDD 的 TMS vs 藥物研究，已撤回且研究對象非 OCD，不提供有效證據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27811556](https://pubmed.ncbi.nlm.nih.gov/27811556/) | 2016 | 雙盲 RCT（增效） | J Clin Psychopharmacol | Duloxetine 增效治療抵抗性 OCD 的雙盲對照試驗，提供最高等級直接證據 |
| [32982805](https://pubmed.ncbi.nlm.nih.gov/32982805/) | 2020 | Meta-Review | Front Psychiatry | 兒童青少年抗憂鬱藥物（含 OCD 適應症）療效、耐受性與自殺風險系統性回顧 |
| [28477500](https://pubmed.ncbi.nlm.nih.gov/28477500/) | 2017 | Meta-analysis | J Affect Disord | OCD 的抗憂鬱藥物與安慰劑反應統合分析，顯示 OCD 療效低於其他焦慮疾患，提示治療挑戰 |
| [24766145](https://pubmed.ncbi.nlm.nih.gov/24766145/) | 2014 | Systematic Review | Expert Opin Pharmacother | 雙盲研究系統性回顧，確認血清素性抗憂鬱藥（5-HT antidepressants）在 OCD 的核心角色 |
| [31749717](https://pubmed.ncbi.nlm.nih.gov/31749717/) | 2019 | Narrative Review | Front Psychiatry | Duloxetine 用於多種精神疾患（含 OCD）的系統性文獻回顧，彙整現有 off-label 使用證據 |
| [25637377](https://pubmed.ncbi.nlm.nih.gov/25637377/) | 2015 | Open-label trial | Int J Neuropsychopharmacol | 開放性試驗直接評估 Duloxetine 治療 OCD（DSM-IV）療效 |
| [39735048](https://pubmed.ncbi.nlm.nih.gov/39735048/) | 2024 | 病例報告 + CBT | Cureus | 超治療劑量 Duloxetine 合併 CBT 治療嚴重治療抵抗性 OCD 合併 MDD，患者達完全緩解 |
| [16669725](https://pubmed.ncbi.nlm.nih.gov/16669725/) | 2006 | Critical Review | J Clin Psychiatry | 批判性回顧 SNRI（venlafaxine、clomipramine）的抗強迫特性，為 Duloxetine 提供機轉類比支持 |
| [21779536](https://pubmed.ncbi.nlm.nih.gov/21779536/) | 2011 | Review | Innov Clin Neurosci | SNRI 作為 OCD 藥理替代方案的綜述，探討 SSRIs 以外的治療選項 |
| [18208931](https://pubmed.ncbi.nlm.nih.gov/18208931/) | 2008 | Case series | J Psychopharmacol | SRI 抵抗性 OCD 患者改用 Duloxetine 的案例系列，探討轉換策略療效 |

---

## 台灣上市資訊

Duloxetine 目前在台灣**尚未取得藥品許可證，無任何上市紀錄**。

如需臨床應用，須依衛生福利部相關法規申請專案進口（特殊管道申請），或待藥廠提出許可證申請。在此前提下，OCD 適應症的推進策略需同步規劃藥品取得路徑。

---

## 安全性考量

> 安全性資訊請參考原廠仿單。

台灣 TFDA 仿單警語、禁忌症及藥物交互作用資料目前尚未收集，為本報告的**阻塞性資料缺口（DG001）**，需優先補齊方能進入完整安全性初評（S1 階段）。

---

## 其他預測摘要

本次 TxGNN 多適應症分析共 10 項預測，完整概覽如下：

| 排名 | 適應症 | TxGNN 分數 | 全球排名 | 證據等級 | 建議 |
|------|--------|-----------|---------|---------|------|
| 1 | 嬰兒良性陣發性斜頸 | 99.85% | #3,733 | L5 | Hold |
| 2 | 廣場恐懼症（Agoraphobia） | 99.84% | #3,826 | L4 | Research Question |
| **3** | **強迫症（OCD）** ★ | **99.84%** | **#3,897** | **L2** | **Proceed with Guardrails** |
| 4 | 偏執型人格疾患 | 99.78% | #4,997 | L5 | Hold |
| 5 | 表演型人格疾患 | 99.78% | #4,998 | pending | pending |
| 6 | 類分裂型人格疾患 | 99.78% | #4,999 | L5 | Hold |
| 7 | 分裂型人格疾患 | 99.78% | #5,001 | L5 | Hold |
| 8 | Ohdo 症候群及變異型 | 99.69% | #6,343 | L5 | Hold |
| 9 | 木樣結膜炎 | 99.66% | #6,872 | L5 | Hold |
| 10 | 眼瞼縮短—智能障礙症候群（Ohdo 型） | 99.60% | #7,689 | L5 | Hold |

★ 唯一達到「Proceed with Guardrails」門檻的適應症

**補充說明：**
- **廣場恐懼症（排名 2）**：有 3 篇文獻（含 2009 年開放性試驗）支持 Duloxetine 用於共病恐慌症的療效，證據等級 L4，可列為次優先研究問題。
- **排名 4-10**：均為 L5（僅模型預測），機轉關聯性薄弱或屬遺傳性罕見疾病，現階段建議 Hold。

---

## 結論與下一步

**決策：Proceed with Guardrails**（針對強迫症適應症）

**理由：**
1 項 Phase 4 完成試驗及 1 項雙盲 RCT 直接針對 Duloxetine 治療 OCD 提供臨床數據，加上多篇系統性回顧及開放性研究，達到 L2 證據等級；SNRI 機轉與 OCD 血清素病理生理基礎具直接機轉關聯，學理支持充分，特別在 SSRI 抵抗性 OCD 的增效治療策略上具差異化定位。

**若要推進需要：**
- **【優先】** 補齊 TFDA 仿單警語、禁忌症及 DDI 資料（DG001，目前為阻塞性缺口，需解除方能進入 S1 安全性初評）
- **【優先】** 補充完整 MOA 文件資料（DG002），強化機轉合理性論述
- 評估台灣藥品取得路徑（專案進口申請或藥廠許可證申請可行性）
- 設計以「SSRI 治療失敗後二線 / 增效治療」為定位的臨床研究方案
- 考慮啟動 Phase 2 探索性試驗或真實世界數據收集，以台灣 OCD 患者族群為目標

---

*本報告結果僅供研究參考，不構成醫療建議。所有老藥新用候選適應症均需經過臨床驗證方可應用。*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

