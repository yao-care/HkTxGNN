---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 881
evidence_level: L5
indication_count: 5
---

# Trastuzumab
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

# Trastuzumab：從 HER2 陽性乳癌到黃體素受體陽性乳癌（HR+/HER2+ 亞群）

## 一句話總結

Trastuzumab（曲妥珠單抗）是靶向 HER2 的單株抗體，原本用於 HER2 陽性乳癌。
TxGNN 模型預測它可能對**黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer)** 有效，目前有 **36 個臨床試驗**和 **20 篇文獻**與這個方向相關。
需注意：這是既有適應症內的**受體亞群**，不是全新疾病。療效取決於 HER2 狀態，與 PR 狀態無關。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HER2 陽性乳癌（依證據包的機轉說明；香港許可證未載明適應症文字） |
| 預測新適應症 | 黃體素受體陽性乳癌 (Progesterone-receptor positive breast cancer)，實際適用範圍為 HR+/HER2+ |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L2（有已完成的 Phase 2/3 試驗，但多數為 HER2 陽性族群或藥物組合，缺少針對 PR 陽性的直接 Phase 3 證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Trastuzumab 結合 HER2 的細胞外區域，阻斷 HER2 訊號傳導，並透過抗體依賴性細胞毒殺作用 (ADCC) 殺傷腫瘤細胞。證據包中的原廠 MOA 欄位缺資料，以上機轉說明來自預測理由欄位。

HER2 陽性且黃體素受體陽性（HR+/HER2+）的腫瘤，本來就屬於 HER2 陽性乳癌的既有適用範圍。因此這個預測較準確的解讀，是 trastuzumab 在 HR+/HER2+ 亞群中的定位，也就是常與內分泌治療或 CDK4/6 抑制劑併用。它**不應延伸到 PR 陽性但 HER2 陰性**的乳癌，那種情況沒有機轉基礎。

目前已有多個試驗在 HR+/HER2+ 乳癌中測試 trastuzumab 搭配內分泌治療、CDK4/6 抑制劑或其他 HER2 藥物，顯示這個組合策略被臨床積極探索。

---

## 臨床試驗證據

從 36 個試驗中挑選與 HR+/HER2+ 最相關的 10 個：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | 進行中（不再招募） | 128 | 新輔助 lapatinib + trastuzumab，合併或不合併內分泌治療，用於 HER2 過度表現乳癌（尚無結果） |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | 未知 | 7 | 芳香環酶抑制劑 + pertuzumab/trastuzumab 新輔助治療 HR+/HER2+ 乳癌；人數很少，證據有限 |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | 招募中 | 30 | 術前 neratinib + 內分泌治療 + trastuzumab，用於 ER 陽性/HER2 陽性乳癌（尚無結果） |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | 完成 | 33 | Letrozole + trastuzumab，用於 ErbB2 陽性且 ER 和/或 PR 陽性的轉移性乳癌 |
| [NCT04334330](https://clinicaltrials.gov/study/NCT04334330) | Phase 2 | 未知 | 34 | Palbociclib + trastuzumab + pyrotinib + fulvestrant，用於 ER/PR 陽性、HER2 陽性乳癌腦轉移 |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Phase 1 | 完成 | 37 | Everolimus + letrozole + trastuzumab，用於荷爾蒙受體陽性/HER2 陽性的晚期乳癌與其他實體瘤，評估安全性與劑量 |
| [NCT00053339](https://clinicaltrials.gov/study/NCT00053339) | Phase 3 | 撤回 | 0 | Trastuzumab 加或不加 tamoxifen，用於 ER/PR 與 HER2 陽性的 IV 期乳癌；未執行，無證據產出 |
| [NCT00005970](https://clinicaltrials.gov/study/NCT00005970) | Phase 3 | 完成 | 3436 | AC 序貫 paclitaxel 加或不加 trastuzumab，用於 HER2 過度表現的輔助治療 |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | 完成 | 3270 | 化療單用 vs 化療 + trastuzumab 的輔助治療，用於淋巴結陽性或高風險乳癌 |
| [NCT00446030](https://clinicaltrials.gov/study/NCT00446030) | Phase 2 | 完成 | 127 | Docetaxel 為基礎的方案加 bevacizumab，主要評估心臟安全性；trastuzumab 的角色與 PR 亞群資料不明確 |

兩個已完成的大型 Phase 3 試驗（NCT00005970、NCT01275677）支持 trastuzumab 在乳癌輔助治療的角色，但並非針對 PR 陽性的分析。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT（Phase 2） | Lancet Oncol | monarcHER：abemaciclib + trastuzumab（加或不加 fulvestrant）對比 trastuzumab + 化療，用於 HR+/HER2+ 晚期乳癌 |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncol | WSG-TP-II：新輔助內分泌治療 + trastuzumab + pertuzumab 對比降階化療，用於 HR+/ERBB2+ 早期乳癌 |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT（Phase 2） | Lancet Oncol | NeoSphere 5 年分析：新輔助 pertuzumab + trastuzumab 用於 HER2 陽性乳癌，報告無惡化存活、無病存活與安全性 |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT（Phase 3） | Lancet Oncol | ExteNET：trastuzumab 為基礎的輔助治療後，使用 neratinib 12 個月 |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT（Phase 2） | Ann Oncol | WSG-ADAPT HER2+/HR-：trastuzumab + pertuzumab 加或不加 paclitaxel 的降階策略（HR 陰性族群，間接相關） |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | 多組學分析 | Theranostics | 分析 ER+/PR+/HER2+（三陽性）乳癌的分子特徵與對 trastuzumab 的反應性 |
| [34983437](https://pubmed.ncbi.nlm.nih.gov/34983437/) | 2022 | 回溯性研究 | BMC Cancer | Trastuzumab + fulvestrant 用於 HR+/HER2+ 晚期乳癌，單一機構經驗 |
| [40339592](https://pubmed.ncbi.nlm.nih.gov/40339592/) | 2025 | 單臂 Phase 2a | Lancet Oncol | Zanidatamab + palbociclib + fulvestrant 用於已治療過的 HR+/HER2+ 轉移性乳癌（不同的 HER2 藥物） |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | 治療指引 | J Clin Oncol | ASCO 晚期 HER2 陽性乳癌全身治療指引更新 |
| [39631485](https://pubmed.ncbi.nlm.nih.gov/39631485/) | 2024 | Review | Pharmacol Res | 乳癌標靶與細胞毒性抑制劑回顧，涵蓋 HER2、HR、ER、PR 狀態對治療的影響 |

---

## 香港上市資訊

目前共有 13 張許可證，以下列出 5 張主要許可證。證據包未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67312 | TRAZIMERA 凍晶注射粉劑 150mg | Pfizer Corporation Hong Kong Limited |
| HK-66513 | HERZUMA 凍晶注射粉劑 150mg | Celltrion Healthcare Hong Kong Limited |
| HK-64165 | HERCEPTIN 皮下注射液 600mg/5ml（僅供皮下注射） | Roche Hong Kong Limited |
| HK-50618 | HERCEPTIN 注射粉劑 150mg | Roche Hong Kong Limited |
| HK-66599 | KANJINTI 凍晶注射粉劑 150mg | Amgen Hong Kong Limited |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗 HER2 單株抗體） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Trastuzumab 在 HER2 陽性乳癌的療效已有大型 Phase 3 試驗支持，HR+/HER2+ 亞群也有多個 Phase 2 試驗與隨機試驗（如 monarcHER、WSG-TP-II）在探索併用策略。
- 這個預測屬於既有適應症的受體亞群。缺少針對 PR 陽性的直接 Phase 3 證據，且必須以 HER2 陽性為前提。

**若要推進需要：**
- 使用條件限定為 HER2 陽性，需先確認 HER2 狀態，不可延伸到 PR 陽性/HER2 陰性的乳癌。
- 取得香港衛生署仿單的警語與禁忌症（目前為阻擋性資料缺口，無法進入安全性篩選）。
- 補充 Phase 3 試驗中 HR+/HER2+ 亞群的分析，或等待 NCT00999804、NCT04886531 等進行中試驗的結果。
- 補齊許可證的劑型與核准適應症文字，確認香港現有適應症是否已涵蓋 HR+/HER2+。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

