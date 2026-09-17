---
layout: default
title: Trastuzumab
parent: 高證據等級 (L1-L2)
nav_order: 763
evidence_level: L1
indication_count: 5
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Trastuzumab：從 HER2 陽性乳癌到黃體素受體陽性乳癌

## 一句話總結

Trastuzumab（曲妥珠單抗）是抗 HER2 人類化單株抗體，臨床上已廣泛用於 HER2 過度表現的乳癌治療。
TxGNN 模型預測它可能對**黃體素受體陽性乳癌 (Progesterone-Receptor Positive Breast Cancer)** 有效，
目前有 **超過 30 個臨床試驗**（含多個 Phase 3 RCT）和 **20 篇文獻**支持這個方向，證據等級達 **L1**。

> ⚠️ 本 Evidence Pack 缺乏 TFDA/香港仿單警語（Blocking）與詳細 MOA 敘述（High），下方標示處請留意。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料庫未提供許可證資料（Data Gap）；依公開藥理知識，Trastuzumab 原用於 HER2 過度表現之乳癌 |
| 預測新適應症 | 黃體素受體陽性乳癌 (Progesterone-Receptor Positive Breast Cancer) |
| TxGNN 預測分數 | 99.90%（rank 2589） |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前 Evidence Pack 中缺乏詳細的作用機轉描述（`original_moa: [Data Gap]`）。但依據臨床廣泛共識與本次證據集中的多筆試驗／文獻交叉驗證，Trastuzumab 為抗 HER2 人類化單株抗體，其臨床適應症本即涵蓋 HER2 過度表現的乳癌，並不特別區分 HR（ER/PR）狀態。

TxGNN 預測的「黃體素受體陽性乳癌」實際上屬於 HER2 陽性乳癌下的一個分子亞群（HR+/HER2+，即所謂三陽性乳癌）。這類病人在臨床實務上長期同時接受抗 HER2 治療與內分泌治療，因此並非機轉上的全新延伸，而是既有適應症的族群細分。這也解釋了為何本候選能同時匹配大量 Phase 2/3 RCT（如 TBCRC023、NEOADAPT、monarcHER、WSG-ADAPT、WSG-TP-II），證據基礎相對紮實。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00999804](https://clinicaltrials.gov/study/NCT00999804) | Phase 2 | 進行中(未招募) | 128 | TBCRC023：Lapatinib+Trastuzumab neoadjuvant，含 HR 亞群分析（12週 vs 24週） |
| [NCT05802225](https://clinicaltrials.gov/study/NCT05802225) | Phase 3 | 進行中(未招募) | 398 | BCD-178 vs Perjeta，HER2+/ER-PR- 族群 neoadjuvant 雙標靶療法 |
| [NCT02689921](https://clinicaltrials.gov/study/NCT02689921) | Phase 2 | 狀態未知 | 7 | NEOADAPT：內分泌療法合併 Pertuzumab/Trastuzumab，無化療，針對 HR+/HER2+ |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | 招募中 | 30 | Neratinib+芳香酶抑制劑+Trastuzumab，針對 ER+/HER2+ 早期乳癌 |
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | 完成 | 33 | Letrozole+Trastuzumab，直接針對 ER 和/或 PR 陽性、HER2 陽性轉移性乳癌 |
| [NCT00446030](https://clinicaltrials.gov/study/NCT00446030) | Phase 2 | 完成 | 127 | Docetaxel 為基礎方案 ± Bevacizumab/Trastuzumab，評估心臟安全性 |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | 完成 | 3270 | 大型輔助治療 RCT：化療 ± Trastuzumab，HER2-low 高風險族群 |
| [NCT00005970](https://clinicaltrials.gov/study/NCT00005970) | Phase 3 | 完成 | 3436 | AC→Paclitaxel ± Trastuzumab 輔助治療，HER2 過度表現族群 |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | 完成 | 652 | Taxane+Lapatinib vs Taxane+Trastuzumab，HER2+ 轉移性乳癌一線治療 |
| [NCT01785420](https://clinicaltrials.gov/study/NCT01785420) | Phase 3 | 招募中 | 1100 | 雙盲安慰劑對照，Trastuzumab 術前短期治療 HER2+ 可手術乳癌 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | RCT (5年追蹤) | Lancet Oncology | NeoSphere：Pertuzumab+Trastuzumab neoadjuvant，5年 PFS/DFS 與安全性數據 |
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | RCT | Lancet Oncology | monarcHER：Abemaciclib+Trastuzumab±Fulvestrant vs 化療+Trastuzumab，HR+/HER2+ 晚期乳癌 |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | RCT | Lancet Oncology | ExteNET：Trastuzumab 輔助治療後接續 Neratinib，HER2+ 早期乳癌 |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | RCT | Annals of Oncology | WSG-ADAPT：HER2+/HR- neoadjuvant 雙標靶去化療策略 |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncology | WSG-TP-II：內分泌療法+雙標靶 vs 降階化療，HR+/HER2+ 早期乳癌 |
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | 多體學分析 | Theranostics | 直接分析 ER+/PR+/HER2+（三陽性）乳癌之分子特徵與 Trastuzumab 反應性 |
| [34983437](https://pubmed.ncbi.nlm.nih.gov/34983437/) | 2022 | 回顧性單中心研究 | BMC Cancer | Trastuzumab+Fulvestrant 合併療法用於 HR+/HER2+ 晚期乳癌 |
| [15894097](https://pubmed.ncbi.nlm.nih.gov/15894097/) | 2005 | Meta-analysis (EBCTCG) | Lancet | 早期乳癌化療與荷爾蒙治療對復發及15年存活率之總體分析 |
| [26253814](https://pubmed.ncbi.nlm.nih.gov/26253814/) | 2015 | Review | Breast (Edinburgh) | 乳癌內在分子亞型（含 Luminal、HER2-enriched）之臨床意義 |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | 指引更新 | J Clin Oncol | ASCO 指引：HER2 陽性晚期乳癌全身性治療更新 |

---

## 細胞毒性

Trastuzumab 屬於抗腫瘤用藥（標靶治療類別），故列出以下資訊：

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（Anti-HER2 人類化單株抗體，非傳統細胞毒性化療藥物） |
| 骨髓抑制風險 | Data Gap — 單獨使用骨髓抑制風險通常較低，但常與化療併用，實際風險請參考仿單 |
| 致吐性分級 | Data Gap — 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 建議監測心臟功能（LVEF），單株抗體類藥物常見心臟毒性關注點；其餘依仿單規範 |
| 處置防護 | 屬生物製劑注射劑型，非傳統小分子細胞毒性藥物處置規範對象，仍請依機構 SOP 處理 |

---

## 安全性考量

安全性資訊請參考原廠仿單。（`key_warnings`、`contraindications`、`DDI` 均為 Data Gap，屬本評估之 Blocking 缺口，見下方結論）

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 黃體素受體陽性乳癌屬 HER2 陽性乳癌下既有適應症的分子亞群，機轉上並非全新延伸，且有多個直接對應的 Phase 2/3 RCT（TBCRC023、NEOADAPT、monarcHER、WSG-ADAPT、WSG-TP-II）與三陽性乳癌專屬分子分析文獻（PMID 31410192）支持，證據等級達 L1。
- 但本藥物目前未於香港上市（0 張許可證），且缺乏 TFDA/香港仿單警語資料（Blocking），無法完成完整安全性初評。

**若要推進需要：**
- 補齊 TFDA/香港仿單之警語、禁忌症與 DDI 資料（DG001，Blocking，需下載並解析仿單 PDF）
- 補充 DrugBank MOA 詳細描述以強化機轉關聯性分析（DG002，High）
- 若考慮於香港申請適應症擴充，需先確認藥品上市/引進計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

