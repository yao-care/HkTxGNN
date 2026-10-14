---
layout: default
title: Letrozole
parent: 高證據等級 (L1-L2)
nav_order: 521
evidence_level: L1
indication_count: 5
---

# Letrozole
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

# Letrozole：從（原適應症資料缺漏）到女性乳癌

## 一句話總結

Letrozole 是一種非類固醇芳香環轉化酶抑制劑，香港已有 12 張有效許可證，但本次彙整的資料未載明核准適應症。
TxGNN 模型預測它對**女性乳癌 (Female Breast Carcinoma)** 有效，目前有 **41 個臨床試驗**和 **20 篇文獻**支持。
需要注意：Letrozole 在乳癌中屬於已確立的標準治療，這項預測更接近資料完整性的缺口，而非真正的新用途發現。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症 |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 12 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏來自仿單或資料庫的詳細作用機轉資料。根據文獻彙整，Letrozole 是非類固醇芳香環轉化酶抑制劑，可阻斷雄激素轉換為雌激素，降低體內雌激素濃度，而雌激素正是驅動荷爾蒙受體陽性乳癌生長的因素。

這個機轉與乳癌直接相符。停經後婦女的雌激素主要來自芳香環轉化酶作用，因此抑制該酶能有效抑制 ER 陽性腫瘤。這是 Letrozole 已確立的作用方式，並非新發現的機轉連結。

TxGNN 預測分數很高，但本次資料未列出原適應症，因此無法評估「原適應症與新適應症的關聯性」。合理的解讀是：此預測反映的是已被證實的乳癌用途。

---

## 臨床試驗證據

本預測共有 41 項相關試驗，以下列出最相關的 10 項（依關聯性評級與規模挑選）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02941926](https://clinicaltrials.gov/study/NCT02941926) | Phase 3 | 完成 | 3246 | COMPLEEMENT-1：Ribociclib + Letrozole 用於 HR+/HER2- 晚期乳癌的安全性與療效 |
| [NCT02600923](https://clinicaltrials.gov/study/NCT02600923) | Phase 3 | 完成 | 131 | Palbociclib + Letrozole 用於停經後 HR+/HER2- 晚期乳癌 |
| [NCT01740427](https://clinicaltrials.gov/study/NCT01740427) | Phase 3 | 完成 | 666 | PALOMA-2：Palbociclib + Letrozole 對比安慰劑 + Letrozole，用於晚期乳癌第一線治療 |
| [NCT00433589](https://clinicaltrials.gov/study/NCT00433589) | Phase 3 | 完成 | 6600 | MINDACT：以 70 基因特徵選擇輔助化療對象，方案含 Letrozole |
| [NCT03425838](https://clinicaltrials.gov/study/NCT03425838) | Phase 3 | 進行中 | 1050 | SONIA：芳香環轉化酶抑制劑 + CDK4/6 抑制劑第一線與第二線的順序比較 |
| [NCT00908531](https://clinicaltrials.gov/study/NCT00908531) | Phase 3 | 終止 | 123 | 術前 4 個月 Letrozole 對比先手術，樣本數小、檢定力有限 |
| [NCT04272801](https://clinicaltrials.gov/study/NCT04272801) | Phase 2 | 進行中 | 84 | 老年女性早期乳癌術前內分泌治療窗口研究 |
| [NCT01439711](https://clinicaltrials.gov/study/NCT01439711) | Phase 2 | 完成 | 108 | 新輔助 Letrozole 用於 ER 陽性原位乳管癌 (DCIS) |
| [NCT02344550](https://clinicaltrials.gov/study/NCT02344550) | Phase 2 | 完成 | 137 | 卵巢抑制 + Letrozole + Everolimus，用於停經前轉移性乳癌 |
| [NCT00688909](https://clinicaltrials.gov/study/NCT00688909) | Phase 4 | 完成 | 261 | 對 Anastrozole 引起關節肌肉痛而不耐受者，改用 Letrozole 的風濕耐受性 |

另有數項試驗僅以 Letrozole 為輔助角色（如生育力保存、Everolimus 繼續治療），或已撤回、人數極少，參考價值有限。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35263519](https://pubmed.ncbi.nlm.nih.gov/35263519/) | 2022 | RCT | N Engl J Med | Ribociclib + Letrozole 在晚期乳癌的整體存活分析 |
| [29718092](https://pubmed.ncbi.nlm.nih.gov/29718092/) | 2018 | RCT | Ann Oncol | MONALEESA-2 更新結果：Ribociclib + Letrozole 第一線治療 HR+/HER2- 晚期乳癌 |
| [30632023](https://pubmed.ncbi.nlm.nih.gov/30632023/) | 2019 | RCT | Breast Cancer Res Treat | PALOMA-2 延長追蹤：Palbociclib + Letrozole 作為第一線治療 |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sci | Letrozole 的藥理、毒性與潛在治療效果 |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opin Drug Metab Toxicol | Letrozole 的藥效學、藥物動力學、臨床療效與安全性 |
| [17912633](https://pubmed.ncbi.nlm.nih.gov/17912633/) | 2007 | Review | Breast Cancer Res Treat | Letrozole 的研發歷程與作用機轉 |
| [19250202](https://pubmed.ncbi.nlm.nih.gov/19250202/) | 2009 | Review | Ann N Y Acad Sci | 芳香環轉化酶抑制劑與乳癌；動物模型中 Letrozole 抑制生長的時間較 Tamoxifen 長 |
| [15001182](https://pubmed.ncbi.nlm.nih.gov/15001182/) | 2004 | Review | Women's Health Issues | Letrozole 乳癌試驗的臨床意涵與待解問題 |
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | 臨床研究 | Comput Math Methods Med | Tamoxifen 與 Letrozole 序貫治療對比 Letrozole 單藥的療效、安全性與預後 |
| [27235140](https://pubmed.ncbi.nlm.nih.gov/27235140/) | 2016 | 前臨床 | Med Oncol | Letrozole 改變癌相關纖維母細胞功能，進而影響乳癌細胞生物學 |

---

## 香港上市資訊

本藥在香港共有 12 張有效單方許可證，以下列出 5 張（資料中劑型與核准適應症欄位皆空白）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-42537 | FEMARA TAB 2.5MG（Novartis） | 錠劑（2.5mg） | 資料未載明 |
| HK-65626 | LETROZOLE SANDOZ TABLETS 2.5MG | 錠劑（2.5mg） | 資料未載明 |
| HK-64679 | ACCORD LETROZOLE TABLETS 2.5MG | 錠劑（2.5mg） | 資料未載明 |
| HK-61004 | LETROZOLE-TEVA TAB 2.5MG | 錠劑（2.5mg） | 資料未載明 |
| HK-61622 | APO-LETROZOLE TABLETS 2.5MG | 錠劑（2.5mg） | 資料未載明 |

---

## 細胞毒性

Letrozole 為內分泌（荷爾蒙）治療藥物，並非傳統細胞毒性化療藥物，但用於抗腫瘤治療。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 內分泌治療（芳香環轉化酶抑制劑），非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 本次資料未提供；請參考原廠仿單 |
| 致吐性分級 | 本次資料未提供；請參考原廠仿單 |
| 監測項目 | 請參考原廠仿單；知識圖譜顯示與骨質疏鬆、肝功能異常相關，宜留意骨密度與肝功能 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（來自藥物－疾病關聯資料，非仿單文字）：肝衰竭、肝硬化、骨質疏鬆、停經後骨質疏鬆、高膽紅素血症、遺傳性高膽紅素血症、Gilbert 症候群、腦血管疾病。
- **藥物交互作用**：資料庫共記錄 100 筆，已列出的項目中僅 Aprepitant 為中度（Moderate），其餘多數分級為未知，例如 Calcitriol、Glimepiride、Lansoprazole、Granisetron、Famotidine、阿斯匹靈、Pantoprazole、Morphine、Metformin、Omeprazole 等。

仿單的警語與禁忌資料未能取得，完整安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多項已完成的 Phase 3 試驗（如 PALOMA-2、COMPLEEMENT-1）及多篇 RCT 文獻支持 Letrozole 用於 HR 陽性乳癌，證據等級為 L1，且香港已有 12 張有效許可證。
- 這屬於既有標準治療，並非新的再利用機會；原適應症與作用機轉資料缺漏，且仿單安全性資料尚未取得，因此需有防護條件。

**若要推進需要：**
- 取得並解析香港衛生署仿單，補齊核准適應症、警語與禁忌症（目前為阻擋性資料缺口）。
- 補充 DrugBank 的作用機轉資料。
- 針對知識圖譜標示的風險族群（肝功能異常、骨質疏鬆）制定監測計畫，並釐清藥物交互作用的分級。

**同時預測的其他適應症（僅供參考）：**
- **雌激素受體陽性乳癌**：與主預測同為 L1、Proceed with Guardrails，機轉直接吻合，屬標準治療。
- **乳頭癌**：L4、Hold，僅有病例報告，高分可能來自本體論的相近性。
- **雌激素受體陰性乳癌**：L4、Hold。Letrozole 依賴雌激素驅動，機轉上無依據，相關試驗皆針對 HR 陽性族群。
- **Ehrlich 腫瘤癌**：L5、Hold。為小鼠移植腫瘤模型，僅有奈米顆粒製劑的前臨床研究，並非人類適應症。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

