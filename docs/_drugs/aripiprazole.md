---
layout: default
title: Aripiprazole
parent: 高證據等級 (L1-L2)
nav_order: 60
evidence_level: L1
indication_count: 10
---

# Aripiprazole
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

# Aripiprazole：從精神分裂症到重度情感障礙

## 一句話總結

Aripiprazole 是第二代非典型抗精神病藥物，全球已核准用於精神分裂症及躁鬱症治療。
TxGNN 模型預測它可能對**重度情感障礙 (Major Affective Disorder)** 有效，
目前有**超過 30 個臨床試驗**和 **20 篇文獻**支持這個方向，FDA 亦已正式核准其作為重度憂鬱症輔助治療及躁鬱症 I 型維持治療。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 精神分裂症、躁鬱症（全球核准；香港衛生署無登記資料） |
| 預測新適應症 | 重度情感障礙 (Major Affective Disorder) |
| TxGNN 預測分數 | 99.62% |
| 證據等級 | L1 |
| 香港上市 | ✗ 無登記 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Aripiprazole 是多巴胺 D2/D3 受體**部分激動劑**，同時也是 5-HT1A 受體部分激動劑及 5-HT2A 受體拮抗劑。這種獨特的「穩定劑」機轉，讓它在多巴胺活性過高時發揮抑制作用、不足時又能補充，可雙向調節邊緣系統的多巴胺與血清素平衡，與傳統抗精神病藥物的純 D2 拮抗截然不同。

重度情感障礙（包含重度憂鬱症與躁鬱症）的核心病理假說，正是多巴胺能和血清素能系統的失調。Aripiprazole 的多受體調節特性直接針對此機轉：既可穩定躁症期的多巴胺過度活化，也能在憂鬱相中透過 5-HT1A 激動作用改善情緒低落，並輔助提升前額葉皮質的認知調控功能。

目前 FDA 及 EMA 已正式核准 Aripiprazole 用於 Bipolar I 型維持治療及重度憂鬱症（MDD）輔助治療（augmentation），多項大規模 Phase 3/4 試驗（VAST-D、NCT00095758/00095823 等）亦提供充分的 L1 等級臨床證據。TxGNN 預測結果高度符合已知臨床實踐，反映模型捕捉到藥物與疾病節點之間真實的生物學連結。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01421342](https://clinicaltrials.gov/study/NCT01421342) | Phase 3 | 完成 | 1522 | VA VAST-D 試驗：比較 Aripiprazole 增強 vs. Bupropion 增強 vs. 轉換 Bupropion 單藥治療 MDD（最大規模 TRD 增強策略頭對頭比較） |
| [NCT00261443](https://clinicaltrials.gov/study/NCT00261443) | Phase 4 | 完成 | 1270 | Aripiprazole 加上 Lithium/Valproate 治療 Bipolar I，評估對鋰鹽或丙戊酸部分無效的維持治療效果 |
| [NCT00277212](https://clinicaltrials.gov/study/NCT00277212) | Phase 4 | 完成 | 1169 | Aripiprazole + Lamotrigine 長期維持治療 Bipolar I 躁狂/混合發作後的穩定，雙盲大規模設計 |
| [NCT00095758](https://clinicaltrials.gov/study/NCT00095758) | Phase 3 | 完成 | 1200 | 隨機雙盲安慰劑對照，14 週評估 Aripiprazole 作為 MDD 輔助治療的安全性與療效 |
| [NCT00095823](https://clinicaltrials.gov/study/NCT00095823) | Phase 3 | 完成 | 1200 | 隨機雙盲安慰劑對照，14 週評估 Aripiprazole 輔助 MDD 治療療效，為 FDA 核准的關鍵試驗之一 |
| [NCT01567527](https://clinicaltrials.gov/study/NCT01567527) | Phase 3 | 完成 | 731 | Aripiprazole 長效針劑（IM depot）用於 Bipolar I 維持治療，評估首次任何情緒發作的時間 |
| [NCT00876343](https://clinicaltrials.gov/study/NCT00876343) | Phase 3 | 完成 | 586 | Aripiprazole 加上 SSRI/SNRI 輔助治療 MDD，安慰劑對照雙盲，評估療效與安全性 |
| [NCT02046564](https://clinicaltrials.gov/study/NCT02046564) | Phase 3 | 完成 | 412 | ASC-01（Aripiprazole/Sertraline 固定劑量複合錠）vs. Sertraline 單藥治療 Sertraline 反應不完全的 MDD 患者 |
| [NCT00110461](https://clinicaltrials.gov/study/NCT00110461) | Phase 3 | 完成 | 296 | 兒童及青少年 Bipolar I（躁狂/混合發作），兩種劑量 Aripiprazole 的安全性與療效評估 |
| [NCT01111539](https://clinicaltrials.gov/study/NCT01111539) | Phase 3 | 提前終止 | 211 | Aripiprazole/Escitalopram 組合治療 MDD（對 Escitalopram 反應不完全者），隨機雙盲設計，終止後仍有部分分析價值 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38669232](https://pubmed.ncbi.nlm.nih.gov/38669232/) | 2024 | 系統性回顧＋Meta 分析 | PLoS One | 目前最大規模的 RCT 統合分析：Aripiprazole 或 Bupropion 增強治療 TRD/MDD 療效與安全性優於安慰劑 |
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | 系統性回顧＋網絡 Meta 分析 | J Affect Disord | 成人 TRD 增強劑的網絡 Meta 分析，比較多種藥物療效及停藥率，Aripiprazole 屬一線增強選項 |
| [38219278](https://pubmed.ncbi.nlm.nih.gov/38219278/) | 2024 | 系統性回顧＋網絡 Meta 分析 | Neuropsychopharmacol Rep | 比較 Brexpiprazole vs. Aripiprazole vs. 安慰劑治療日本 MDD 患者的療效、耐受性與安全性 |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | 系統性回顧＋Meta 分析 | Psychol Med | 抗精神病藥物治療 MDD（單藥及輔助療法）的首次全面性 Meta 分析評估 |
| [34167174](https://pubmed.ncbi.nlm.nih.gov/34167174/) | 2021 | 系統性回顧＋Meta 分析 | Prim Care Companion CNS Disord | 長期（≥6 個月）Aripiprazole 增強治療 MDD 的緩解率與不良反應統合分析 |
| [37746943](https://pubmed.ncbi.nlm.nih.gov/37746943/) | 2023 | 系統性回顧＋網絡 Meta 分析 | Medicine | 4 種非典型抗精神病藥（含 Aripiprazole）增強治療 MDD 的比較有效性排名分析 |
| [37149344](https://pubmed.ncbi.nlm.nih.gov/37149344/) | 2023 | 回顧文獻 | Psychiatr Clin North Am | TRD 藥物治療回顧：Aripiprazole 為研究最充分的增強劑，緩解率優於安慰劑 |
| [36855876](https://pubmed.ncbi.nlm.nih.gov/36855876/) | 2023 | 回顧文獻 | Am J Psychiatry | 在快速演進的 TRD 治療格局中，非典型抗精神病藥物的定位與選擇建議 |
| [37815563](https://pubmed.ncbi.nlm.nih.gov/37815563/) | 2023 | 回顧文獻（JAMA） | JAMA | 躁鬱症診斷與治療全面回顧，涵蓋 Aripiprazole 用於 Bipolar I 維持治療的 Phase 4 證據 |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | 回顧文獻 | J Psychopharmacol | 比較第二代抗精神病藥（含 Aripiprazole）、Esketamine 及 Lithium 在 MDD 組合治療中的療效與耐受性 |

---

## 香港上市資訊

香港衛生署藥物辦公室資料庫目前無 Aripiprazole 的登記許可證紀錄（共 0 張）。

然而，Aripiprazole（品牌名 Abilify® 等）已在美國、歐盟、日本、台灣等主要市場廣泛上市，並核准用於精神分裂症、Bipolar I 型及 MDD 輔助治療。此資料缺口很可能反映本系統資料庫的收錄限制，而非該藥物在香港實際不可取得。

**建議行動**：向香港衛生署藥物辦公室（藥物查詢熱線）直接查詢正式登記狀態，或查閱 Drug Office 的 [香港中西藥物資料庫](https://www.drugoffice.gov.hk)。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Aripiprazole 用於重度情感障礙領域擁有多項大規模 Phase 3/4 雙盲隨機對照試驗（VAST-D n=1,522；兩個 Phase 3 各 n=1,200 等）及多篇系統性回顧/Meta 分析的 L1 等級最高證據支持，FDA 已正式核准其用於 MDD 輔助治療及 Bipolar I 維持治療，機轉合理性充分，具備直接推進的科學基礎。

**若要推進需要：**
- 確認香港衛生署對 Aripiprazole 的實際許可證狀態及可用品牌
- 補充完整安全性資料（TFDA/HK 仿單警語、禁忌症、主要藥物交互作用）
- 評估目標族群（成人 TRD、Bipolar I 維持、兒童青少年）的香港適用性及監管路徑
- 建立特殊族群（老年、孕婦、腎/肝功能不全）安全性監測計畫
- 補充作用機轉（MOA）詳細資料，以強化機轉關聯性分析報告

---

> ⚠️ **免責聲明**：本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過完整臨床驗證才能應用於臨床實踐。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

