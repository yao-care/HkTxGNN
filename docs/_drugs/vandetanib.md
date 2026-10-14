---
layout: default
title: Vandetanib
parent: 僅模型預測 (L5)
nav_order: 926
evidence_level: L5
indication_count: 5
---

# Vandetanib
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

# Vandetanib：從甲狀腺癌到腎細胞癌

## 一句話總結

Vandetanib 是口服多標靶酪胺酸激酶抑制劑，原本用於甲狀腺癌（thyroid gland carcinoma）治療。
TxGNN 模型預測它可能對**腎細胞癌 (Renal Cell Carcinoma)** 有效，
目前有 **4 個臨床試驗**和 **5 篇文獻**與此方向相關，但多數試驗規模很小或提前終止，證據仍屬初步。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 甲狀腺癌 (thyroid gland carcinoma)（來自知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 腎細胞癌 (Renal Cell Carcinoma) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L4（僅有小型 Phase 2 試驗，無已完成且有結果的 RCT；以保守方式判定） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold（列為研究問題） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Vandetanib 是多標靶酪胺酸激酶抑制劑，作用標的包括 VEGFR2、EGFR 與 RET，其在甲狀腺癌（尤其是 RET 驅動的髓質癌）中的療效已被證實。

VEGFR 訊號是透明細胞腎細胞癌的核心驅動因子，特別是 VHL 缺失、HIF 驅動 VEGF 過度表現的腫瘤。遺傳性腎癌（如 VHL 病、HLRCC/SDH 相關腎癌）也顯示對血管新生與代謝重塑的依賴，因此抗血管新生抑制在機轉上合理。

不過，現有試驗規模小、數項提前終止，也沒有結果資料或 Phase 3 證據。整體而言，目前證據只支持「值得研究的問題」，尚不足以作為臨床建議。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Phase 2 | 完成 | 37 | Vandetanib 用於 VHL 病合併腎腫瘤；與腎細胞癌生物學直接相關，為最大的腎癌特異試驗，但未提供結果資料 |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Phase 1/2 | 終止 | 7 | Vandetanib 併用 metformin 於 HLRCC/SDH 相關或散發性乳突狀腎細胞癌；機轉合理但僅納入 7 人 |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Phase 2 | 終止 | 3 | Vandetanib 用於晚期透明細胞腎細胞癌；僅納入 3 人，幾乎無法評估療效 |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Phase 2 | 完成 | 82 | Carboplatin + gemcitabine 加或不加 vandetanib 用於晚期泌尿上皮癌；與腎細胞癌僅間接相關 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clin Exp Metastasis | 針對轉移性延胡索酸水合酶缺失型腎細胞癌的代謝與表觀遺傳重塑治療；尚無標準療法，多項 Phase 2 試驗評估標靶藥物組合 |
| [42107510](https://pubmed.ncbi.nlm.nih.gov/42107510/) | 2026 | Review | Pharmacol Res | FDA 核准的 RET 抑制劑在 RET 驅動甲狀腺癌與肺癌的應用，屬於原適應症的背景資料 |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets Ther | Nintedanib 於實體瘤的證據回顧，提及 vandetanib 等抗血管新生藥物 |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educ Book | 晚期甲狀腺癌的全身性治療；vandetanib 為 RET 抑制劑，已獲 FDA 核准用於髓質癌 |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | 前臨床（小鼠模型） | Mol Cancer Res | TFE3 Xp11.2 易位腎細胞癌小鼠模型，揭示新的治療標的；並非針對 vandetanib |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62087 | CAPRELSA TAB 300MG（Sanofi Hong Kong） | 錠劑 | 未提供 |
| HK-62086 | CAPRELSA TAB 100MG（Sanofi Hong Kong） | 錠劑 | 未提供 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多標靶酪胺酸激酶抑制劑，非傳統細胞毒性化療） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單；依下方安全性資料，建議至少關注心電圖 QT 間期、電解質（鉀、鈣）、甲狀腺功能、血壓與腎功能 |
| 處置防護 | 請參考原廠仿單 |

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎疾病**（來自藥物－疾病關聯，非仿單原文）：
  - 心血管：高血壓、長 QT 症候群（含家族性）、尖端扭轉型心室頻脈、充血性心衰竭／心衰竭
  - 內分泌與代謝：甲狀腺功能低下（含黏液水腫、先天性甲狀腺功能低下）、缺鉀、高血鈣、腎鈣質沉著症、磷代謝異常
  - 其他：腎功能不全、間質性肺病、腦缺血、短暫性腦缺血發作、後部可逆性腦病變症候群
- **藥物交互作用**：資料庫共記錄 100 筆，以下為部分範例：
  - 嚴重（Major）：Clarithromycin、Levofloxacin、Dolasetron、Palonosetron、Picosulfuric acid、Sodium sulfate、Polyethylene glycol（含電解質）。其中多數與 QT 延長或電解質紊亂風險相關，須特別留意。
  - 中度（Moderate）：Famotidine、Metformin、Loperamide、Dexamethasone、Bisacodyl、Lactitol
  - 輕微（Minor）：Ranitidine、Omeprazole、Rabeprazole、Lansoprazole、Dexlansoprazole、Metronidazole、Naloxegol

香港仿單的警語與禁忌尚未取得，詳細資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold（列為研究問題）**

**理由：**
- 腎細胞癌的 VEGF 依賴性提供合理的機轉依據，且已有數項腎癌特異的 Phase 2 試驗，但最直接相關的試驗不是提前終止（僅 3 與 7 人），就是沒有結果資料，缺乏 Phase 3 證據。
- 此藥有明確的心血管風險（QT 延長等）與大量交互作用，在療效證據薄弱的情況下，尚不足以推進臨床應用。

**若要推進需要：**
- 取得 NCT00566995（VHL 病腎腫瘤）的結果資料，評估客觀反應率與無惡化存活期
- 補齊香港仿單的警語與禁忌，完成安全性篩查
- 補充詳細的作用機轉資料（DrugBank）
- 與現有標準腎癌標靶藥物（如 sunitinib、pazopanib）比較其定位，並考慮針對 VHL 或 HLRCC 等特定亞群設計新試驗
- 制定 QT 間期、電解質與血壓的監測計畫

另外，排名第 2 至第 4 的預測（Xp11.2/TFE3 易位腎癌、伴神經母細胞瘤的腎癌、未分類腎癌）均無直接證據，分數可能源自上位腎細胞癌本體的繼承，建議暫不處理。第 5 名腎盂癌僅有一項間接相關的泌尿上皮癌試驗，同樣維持 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

