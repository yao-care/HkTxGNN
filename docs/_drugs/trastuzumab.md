---
layout: default
title: Trastuzumab
parent: 高證據等級 (L1-L2)
nav_order: 896
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Trastuzumab：預測新適應症為黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer)（證據等級 L1）。原適應症：HER2 陽性乳癌"
monitor_inn: "TRASTUZUMAB"
predicted_indications: ["malignant cutaneous granular cell skin tumor"]
---

# Trastuzumab
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Trastuzumab：從 HER2 陽性乳癌到黃體素受體陽性乳癌

## 一句話總結

Trastuzumab 是一種抗 HER2 的單株抗體，原本用於 HER2 陽性乳癌的治療。
TxGNN 模型預測它可能對**黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer)** 有效，
目前有 **13 個臨床試驗**和 **20 篇文獻**列於此方向。但此適應症大部分屬於原適應症的子群（HR+/HER2+），並非全新的藥物再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HER2 陽性乳癌 |
| 預測新適應症 | 黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Trastuzumab 靶向 HER2，已獲核准用於 HER2 陽性乳癌，其療效取決於 HER2 狀態，而非黃體素受體 (PR) 狀態。

相當大比例的 HER2 陽性腫瘤同時為 PR 陽性（HR+/HER2+），因此這個預測適應症在很大程度上是原核准適應症的一個亞型，而不是真正的新用途。TxGNN 的高分 (0.999) 反映的正是這種與原適應症的重疊。

需要注意的是，對 HER2 陰性的 PR 陽性乳癌，預期 trastuzumab 不會有效。HER2-low 的情境中，有效的是 trastuzumab deruxtecan 這種抗體藥物複合體，其作用機轉不同（藥物載荷傳遞與旁觀者效應）。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | 完成 | 3270 | 輔助化療加或不加 trastuzumab 用於乳癌，涵蓋 HR+/HER2+ 族群，為最直接的高階證據 |
| [NCT00194779](https://clinicaltrials.gov/study/NCT00194779) | Phase 2 | 完成 | 50 | 新輔助化療後接含 trastuzumab 方案，用於 HER2 陽性乳癌，規模小 |
| [NCT01750073](https://clinicaltrials.gov/study/NCT01750073) | Phase 2 | 完成 | 92 | 新輔助化療加或不加 trastuzumab |
| [NCT02260531](https://clinicaltrials.gov/study/NCT02260531) | Phase 2 | 完成 | 36 | Cabozantinib 單用或併用 trastuzumab，用於乳癌腦轉移 |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | 完成 | 33 | Letrozole 併用 trastuzumab，用於 ER/PR 陽性且 HER2 陽性的轉移性乳癌 |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | 招募中 | 30 | 術前 neratinib、芳香環酶抑制劑併用 trastuzumab，用於 ER 陽性/HER2 陽性癌症 |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Phase 1 | 完成 | 37 | Everolimus、letrozole 併用 trastuzumab，用於 HR 陽性/HER2 陽性晚期乳癌 |
| [NCT04334330](https://clinicaltrials.gov/study/NCT04334330) | Phase 2 | 狀態未知 | 34 | Palbociclib、trastuzumab、pyrotinib 與 fulvestrant 併用，用於 ER/PR 陽性、HER2 陽性腦轉移；組合療法難以單獨判斷 trastuzumab 效果 |
| [NCT00053339](https://clinicaltrials.gov/study/NCT00053339) | Phase 3 | 撤回 | 0 | Trastuzumab 加或不加 tamoxifen，主題直接相關，但未收案，無法提供證據 |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | 完成 | 517 | QL1209/pertuzumab 併用 trastuzumab 與 docetaxel，對象為 ER/PR 陰性族群，與此適應症關聯有限 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT (Phase 2) | Lancet Oncol | monarcHER：abemaciclib 併用 trastuzumab（加或不加 fulvestrant）用於 HR+/HER2+ 晚期乳癌，對照 trastuzumab 加標準化療 |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT (Phase 2) 追蹤 | Lancet Oncol | NeoSphere 5 年分析：新輔助 pertuzumab 加 trastuzumab 的無惡化存活、無病存活與安全性 |
| [29117498](https://pubmed.ncbi.nlm.nih.gov/29117498/) | 2017 | 統合分析 | N Engl J Med | ER 陽性早期乳癌停止內分泌治療後 20 年復發風險 |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | 統合分析 | Lancet | 早期乳癌化療與荷爾蒙治療對復發及 15 年存活的影響 |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | Phase 2 試驗 | Ann Oncol | WSG-ADAPT：trastuzumab 加 pertuzumab 雙重阻斷（±紫杉醇）12 週新輔助降階治療，針對 HER2+/HR− |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | 多組學研究 | Theranostics | ER+/PR+/HER2+ 三陽性乳癌的分子特徵與對 trastuzumab 的反應性 |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | 治療指引 | J Clin Oncol | ASCO 晚期 HER2 陽性乳癌全身治療指引更新 |
| [21151204](https://pubmed.ncbi.nlm.nih.gov/21151204/) | 2011 | Review | Nat Rev Clin Oncol | HER2 與荷爾蒙受體雙陽性乳癌：芳香環酶抑制劑加抗 HER2 治療策略 |
| [26253814](https://pubmed.ncbi.nlm.nih.gov/26253814/) | 2015 | Review | Breast | 乳癌內在分子亞型的臨床意涵 |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacol Res | 乳癌標靶與細胞毒性抑制劑，依 HER2/HR 狀態分層 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-50618 | HERCEPTIN POWDER FOR INJ 150MG（Roche） | — | — |
| HK-64165 | HERCEPTIN SOLUTION FOR INJECTION 600MG/5ML（皮下注射，Roche） | — | — |
| HK-67312 | TRAZIMERA POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 150MG（Pfizer） | — | — |
| HK-66513 | HERZUMA POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 150MG（Celltrion） | — | — |
| HK-66599 | KANJINTI POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 150MG（Amgen） | — | — |

共 13 張有效許可證，皆為單方製劑，無已註銷者。其他包括 Herceptin 440 mg、Kanjinti 420 mg、Herzuma 420 mg、Trazimera 420 mg，以及 Phesgo 皮下注射劑（兩種規格）。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗 HER2 單株抗體） |
| 骨髓抑制風險 | 單用相對較低，但與化療併用時需留意血球變化 |
| 致吐性分級 | 低 |
| 監測項目 | 心臟功能（左心室射出分率，LVEF）、CBC |
| 處置防護 | 請依機構的注射用生物製劑處置規範，並參考原廠仿單 |

文獻指出 trastuzumab 相關心臟毒性是重要議題（見 PMID 17687157、27038641），用藥前後應進行心臟評估。

---

## 安全性考量

- **藥物交互作用**：已查詢到 94 筆交互作用，以下為部分主要項目：
  - 重度：Deferiprone、Samarium (153Sm) lexidronam、Adalimumab、Baricitinib
  - 中度：Paclitaxel、Warfarin、Dicoumarol、Zidovudine、Chloramphenicol、Roflumilast、Palifermin、Alemtuzumab、Azathioprine 等

其他警語與禁忌症，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Trastuzumab 在 HER2 陽性乳癌的療效已有大型 Phase 3 試驗及多篇 RCT 支持，PR 陽性的 HER2 陽性腫瘤屬於已核准適應症的子群。
- 高 TxGNN 分數反映的是與原適應症的重疊，並非新的再利用訊號。療效取決於 HER2 狀態，對 HER2 陰性的 PR 陽性乳癌不應預期有效。

**若要推進需要：**
- 以 HER2 狀態作為使用前提，明確限定於 HR+/HER2+ 族群。
- 補充作用機轉資料與香港核准適應症文字及仿單的警語、禁忌症。
- 建立心臟功能監測計畫。
- 針對 HR+/HER2+ 子群取得更直接的證據。目前最直接的 Phase 3（NCT00053339）已撤回。

**其他預測適應症的簡要評估：**
- 「正常乳腺樣亞型乳癌」：缺乏 HER2 相關機轉依據，唯一試驗尚未開始收案且使用不同分子，建議 **Hold**。
- 「PR 陰性乳癌」：與 PR 陽性相同，HER2 陽性者已涵蓋於原適應症；三陰性乳癌缺乏標靶，不預期有效。
- 「Luminal A 或 B 乳腺腫瘤」：僅 HER2 陽性的 luminal B 子集適用，已涵蓋於原適應症。
- 「惡性皮膚顆粒細胞瘤」：無任何試驗或文獻，僅為模型預測，建議 **Hold**。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

