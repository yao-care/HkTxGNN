---
layout: default
title: Revefenacin
parent: 僅模型預測 (L5)
nav_order: 767
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Revefenacin：預測新適應症為支氣管炎 (Bronchitis)（證據等級 L5）。原適應症：慢性阻塞性肺病 (COPD)"
monitor_inn: "REVEFENACIN"
predicted_indications: ["bronchitis"]
---

# Revefenacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Revefenacin：從慢性阻塞性肺病 (COPD) 到支氣管炎
{: .text-alpha }

## 一句話總結

Revefenacin 是一種肺部選擇性的長效型蕈毒鹼拮抗劑 (LAMA)，原本用於慢性阻塞性肺病 (COPD) 的維持治療。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，但目前僅有 **1 個間接相關的臨床試驗**，且**沒有直接針對支氣管炎的文獻**。
另一個預測方向「阻塞性肺病」實質上等同於原適應症，不屬於真正的再利用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性阻塞性肺病 (COPD)（香港許可證未載明適應症文字，此處依知識圖譜資料） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.61% |
| 證據等級 | L2（依資料編製時的評等；實際上僅有 COPD 族群的試驗，並無支氣管炎專屬試驗，直接證據偏弱） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold（列為研究問題） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥物類別推論，Revefenacin 是一種肺部選擇性的長效蕈毒鹼拮抗劑，透過阻斷呼吸道平滑肌與黏膜下腺體上的 M3 受體，產生支氣管擴張，並可能減少由膽鹼激導的黏液分泌。

慢性支氣管炎是 COPD 的主要表型之一，兩者在臨床上高度重疊。因此機轉上，減少黏液分泌與緩解氣道收縮，可能有助於改善支氣管炎症狀。

需要注意的是，TxGNN 的高分 (0.996) 很可能反映的是慢性支氣管炎與已核准 COPD 適應症之間的重疊，而不是獨立的證據。目前連結到的試驗收錄的都是 COPD 患者，並未單獨檢驗支氣管炎。

## 臨床試驗證據

以下為與「支氣管炎」預測直接連結的試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01704404](https://clinicaltrials.gov/study/NCT01704404) | Phase 2 | 完成 | 62 | 在 COPD 患者中評估 7 天多次給藥的藥效、安全性與藥動學；無支氣管炎專屬療效指標，相關性屬間接 |

此外，在「阻塞性肺病」這個預測方向（本質上就是原適應症 COPD）下，另有多個試驗，包括：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02512510](https://clinicaltrials.gov/study/NCT02512510) | Phase 3 | 完成 | 611 | 12 週安慰劑對照試驗，為支持 COPD 適應症的關鍵療效與安全性試驗 |
| [NCT02459080](https://clinicaltrials.gov/study/NCT02459080) | Phase 3 | 完成 | 619 | 12 週安慰劑對照的重複試驗，評估 COPD 療效與安全性 |
| [NCT02518139](https://clinicaltrials.gov/study/NCT02518139) | Phase 3 | 完成 | 1060 | 52 週、與 tiotropium 對照的安全性與耐受性試驗 |
| [NCT05046795](https://clinicaltrials.gov/study/NCT05046795) | Phase 3 | 完成 | 258 | 中國族群、12 週安慰劑對照試驗 |
| [NCT03095456](https://clinicaltrials.gov/study/NCT03095456) | Phase 3 | 完成 | 207 | 與 Spiriva HandiHaler 比較，用於低吸氣流速的 COPD 患者 |
| [NCT05165485](https://clinicaltrials.gov/study/NCT05165485) | Phase 4 | 完成 | 404 | 與 tiotropium 比較，用於重度至極重度 COPD 且吸氣流速不足者 |
| [NCT02040792](https://clinicaltrials.gov/study/NCT02040792) | Phase 2 | 完成 | 355 | 28 天劑量範圍試驗，支持劑量選擇 |
| [NCT02109172](https://clinicaltrials.gov/study/NCT02109172) | Phase 2 | 完成 | 64 | 每日一次與兩次給藥的交叉試驗 |
| [NCT04315558](https://clinicaltrials.gov/study/NCT04315558) | Phase 2 | 完成 | 21 | RARICO：COPD 急性呼吸衰竭的探索性研究，樣本小 |
| [NCT03573817](https://clinicaltrials.gov/study/NCT03573817) | Phase 3 | 完成 | 122 | 與 formoterol 序貫或合併給藥的 42 天安全性與耐受性研究 |

## 文獻證據

目前無與支氣管炎直接相關的文獻。

以下為 COPD 方向（原適應症）的代表性文獻，僅供參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32106777](https://pubmed.ncbi.nlm.nih.gov/32106777/) | 2020 | RCT（亞組分析） | Ther Adv Respir Dis | 評估併用 ICS/LABA 或 LABA 的 COPD 患者使用 revefenacin 的療效與安全性 |
| [36681255](https://pubmed.ncbi.nlm.nih.gov/36681255/) | 2023 | RCT（事後分析） | Respir Med | 175 μg 每日一次改善 COPD 患者的健康狀態 |
| [34875569](https://pubmed.ncbi.nlm.nih.gov/34875569/) | 2022 | 統合分析 | Heart Lung | 核准劑量下的安全性評估 |
| [31150963](https://pubmed.ncbi.nlm.nih.gov/31150963/) | 2019 | 52 週 Phase 3 安全性分析 | Respir Med | 88 μg 與 175 μg 在中度至極重度 COPD 的安全性與耐受性 |
| [31152911](https://pubmed.ncbi.nlm.nih.gov/31152911/) | 2019 | Phase 3 心血管安全性分析 | Pulm Pharmacol Ther | 未見臨床上有意義的心電圖變化 |
| [30560478](https://pubmed.ncbi.nlm.nih.gov/30560478/) | 2019 | Review | Drugs | Revefenacin 首次全球核准的藥物概述 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68082 | YUPELRI INHALATION SOLUTION 175MCG/3ML | 吸入溶液 | 資料未載明 |

製造商（持證商）：VIATRIS HEALTHCARE HONG KONG LIMITED。

## 安全性考量

- **藥物交互作用**：資料庫共記錄 100 筆交互作用，以下為其中屬中度 (Moderate) 者的主要例子，多為其他抗膽鹼藥物，併用可能加重抗膽鹼作用：
  - Hyoscyamine、Atropine、Glycopyrronium、Scopolamine、Dicyclomine、Trospium
  - 其他中度交互作用藥物包括 Cobicistat、Promethazine、Eltrombopag、Abiraterone、Obeticholic acid 等
- **使用上的注意事項**（依藥物類別推論，非仿單原文）：需留意抗膽鹼不良反應，如尿滯留、窄角性青光眼，以及矛盾性支氣管痙攣。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold（列為研究問題）**

**理由：**
- 支氣管炎的預測分數雖高，但很可能只是反映它與已核准的 COPD 適應症重疊；目前沒有任何支氣管炎專屬的試驗或文獻。
- COPD 方向有多個 Phase 3 試驗支持，但那是既有適應症，並非新的再利用發現。

**若要推進需要：**
- 釐清目標族群：是「慢性支氣管炎表型的 COPD」（已在標示範圍內）還是「非 COPD 的支氣管炎」（需另行取得證據）
- 取得詳細的作用機轉資料，特別是黏液分泌調控方面
- 針對支氣管炎（尤其是慢性支氣管炎、黏液過度分泌）設計探索性研究，並以痰量、咳嗽、急性惡化次數為終點
- 取得香港原廠仿單，確認核准適應症、警語與禁忌症
- 不建議直接外推到氣喘等其他阻塞性疾病，需有獨立證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

