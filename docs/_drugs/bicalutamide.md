---
layout: default
title: Bicalutamide
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bicalutamide：預測新適應症為女性乳癌 (Female Breast Carcinoma)（證據等級 L5）。原適應症：資料未提供"
monitor_inn: "BICALUTAMIDE"
predicted_indications: ["hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "Ambras type hypertrichosis universalis congenita", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "leprosy", "multiple endocrine neoplasia", "pulmonary hypertension", "female breast carcinoma", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Bicalutamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Bicalutamide：從前列腺癌相關用途到女性乳癌
{: .text-alpha }

## 一句話總結

Bicalutamide 是一種非類固醇型雄激素受體（AR）拮抗劑，香港已有多張許可證上市。
TxGNN 模型的首位預測為**多毛症 (Hypertrichosis)**，但證據僅有 1 篇評論信件，並不充分。
證據最完整的是**女性乳癌 (Female Breast Carcinoma)**，目前有 **1 個 Phase 2 臨床試驗**和 **20 篇文獻**支持，因此本報告以乳癌作為主要評估對象。

> 備註：本資料中香港許可證未提供核准適應症文字，原適應症無法由許可證確認。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供（許可證無適應症文字） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma)（TxGNN 排名第 9；排名第 1 為多毛症，證據僅 L4） |
| TxGNN 預測分數 | 99.11% |
| 證據等級 | L2（依資料編譯時的評分；Phase 2 試驗尚未完成，嚴格依規則可能偏低） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Bicalutamide 是非類固醇型 AR 拮抗劑，透過阻斷雄激素受體訊號發揮作用。

部分乳癌依賴 AR 訊號，特別是 AR 陽性的三陰性乳癌（TNBC）、頂漿分泌型癌（apocrine）及管腔 AR 型（LAR）亞型。這些亞型缺乏雌激素受體、黃體素受體及 HER2，傳統內分泌與標靶治療難以使用，因此 AR 成為可能的治療標的。

前臨床研究顯示 Bicalutamide 可抑制 MDA-MB-231 細胞的增殖與侵襲，與薑黃素合用有療效，與 ERK 抑制劑共同標靶可經由 FOXC2 誘發鐵死亡，並可增強化療在發炎性乳癌細胞株的效果。不過，臨床上 Bicalutamide 併用芳香環轉化酶抑制劑於 ER+/AR+ 晚期乳癌的 Phase 2 單臂研究，並未顯示協同效果（6 個月臨床獲益率 16.7%，客觀反應率 0%，研究提前終止）。因此，需依 AR 表現篩選病人。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03650894](https://clinicaltrials.gov/study/NCT03650894) | Phase 2 | 進行中（不再招募） | 30 | Nivolumab + Bicalutamide + Ipilimumab 用於轉移性 HER2 陰性乳癌；單臂小型試驗，尚無結果，無法分離 Bicalutamide 的貢獻 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31434793](https://pubmed.ncbi.nlm.nih.gov/31434793/) | 2020 | Phase 2 單臂臨床研究 | The Oncologist | Bicalutamide + 芳香環轉化酶抑制劑用於 ER+/AR+ 晚期乳癌，未見協同效果，研究提前終止 |
| [40853613](https://pubmed.ncbi.nlm.nih.gov/40853613/) | 2025 | Review | Current Medical Science | 抗雄激素療法於 TNBC 的現況，探討與化療、免疫治療合併 |
| [29940524](https://pubmed.ncbi.nlm.nih.gov/29940524/) | 2018 | Review | Cancer Treatment Reviews | AR 是 TNBC（LAR 亞型）的潛在標的 |
| [32145961](https://pubmed.ncbi.nlm.nih.gov/32145961/) | 2020 | Review | Bulletin du Cancer | AR 陽性 TNBC 約占 TNBC 的 30%，預後並未較佳 |
| [24740738](https://pubmed.ncbi.nlm.nih.gov/24740738/) | 2014 | Review | J Mol Endocrinol | 重新檢視 AR 在乳癌的角色 |
| [32332626](https://pubmed.ncbi.nlm.nih.gov/32332626/) | 2020 | 前臨床 | Medicine | Bicalutamide 抑制 MDA-MB-231 細胞增殖與侵襲 |
| [31917699](https://pubmed.ncbi.nlm.nih.gov/31917699/) | 2020 | 前臨床 | Anti-Cancer Drugs | Bicalutamide 合併薑黃素對 AR 陽性 TNBC 有強療效 |
| [40974527](https://pubmed.ncbi.nlm.nih.gov/40974527/) | 2026 | 前臨床 | Sci China Life Sci | AR/ERK 共同標靶經 FOXC2 誘發 TNBC 鐵死亡 |
| [39063165](https://pubmed.ncbi.nlm.nih.gov/39063165/) | 2024 | 前臨床 | Int J Mol Sci | Bicalutamide 增強化療在人類與犬發炎性乳癌細胞株的效果 |
| [35027319](https://pubmed.ncbi.nlm.nih.gov/35027319/) | 2022 | Review | Clin Breast Cancer | 乳癌頂漿分泌型癌的分子與臨床特徵（ER 陰性、AR 陽性） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-41794 | CASODEX TAB 50MG | 錠劑 | 資料未提供 |
| HK-49624 | CASODEX TAB 150MG | 錠劑 | 資料未提供 |
| HK-68650 | HEXALIS TABLETS 50MG | 錠劑 | 資料未提供 |
| HK-68649 | HEXALIS TABLETS 150MG | 錠劑 | 資料未提供 |
| HK-59232 | BICALOX TAB 50MG | 錠劑 | 資料未提供 |

（共 11 張有效單方許可證，上表僅列 5 張。）

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶／內分泌治療（AR 拮抗劑），非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 低（但資料顯示貧血為知識圖譜中的禁忌疾病之一） |
| 致吐性分級 | 低 |
| 監測項目 | 肝功能、血糖、CBC |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **知識圖譜標示的禁忌／需謹慎疾病**（來自藥物－疾病關聯，非仿單原文）：肝病、膽囊疾病、藥物性肝損傷、高血糖、糖尿病、糖尿病酮酸中毒、貧血（含巨球性貧血）、間質性肺病。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 嚴重（Major）：Cisapride、Dolasetron
  - 中度（Moderate）：Famotidine、Loperamide、Aprepitant、Clarithromycin、Levofloxacin、Granisetron、Budesonide 等
  - 輕度（Minor）：Metronidazole

仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 乳癌是所有預測中證據最完整的一項，有 1 個 Phase 2 試驗及多篇前臨床與綜述文獻支持 AR 標的。但臨床證據仍薄弱，且 ER+/AR+ 的 Phase 2 單臂研究結果為陰性，效益可能僅限於特定亞型。
- 其餘預測（多毛症、先天畸形症候群、痲瘋病等）多為證據極少或機轉不明的圖譜預測，建議維持 Hold。

**若要推進需要：**
- 取得 Phase 2 試驗（NCT03650894）結果，並設計 AR 表現篩選的病人族群
- 補充作用機轉資料與香港仿單的警語、禁忌及核准適應症
- 針對肝功能、血糖及藥物交互作用（尤其 QT 延長相關藥物）制定監測計畫
- 評估單藥於 AR 陽性 TNBC 的療效，並與已知 AR 抑制劑（如 enzalutamide）比較
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

