---
layout: default
title: Irinotecan
parent: 中證據等級 (L3-L4)
nav_order: 484
evidence_level: L3
indication_count: 1
last_modified_at: 2026-10-14
description: "Irinotecan：預測新適應症為女性乳癌 (Female Breast Carcinoma)（證據等級 L3）。原適應症：結腸癌轉移、胰腺癌"
monitor_inn: "IRINOTECAN"
predicted_indications: ["female breast carcinoma"]
---

# Irinotecan
{: .fs-9 }

證據等級: **L3** | 預測適應症: **1** 個
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

## Irinotecan：從大腸癌轉移與胰腺癌到女性乳癌
{: .text-alpha }

## 一句話總結

Irinotecan（伊立替康）是拓樸異構酶 I 抑制劑類的化療藥物，原本用於結腸癌轉移與胰腺癌。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，
目前有 **9 個臨床試驗**和 **20 篇文獻**與此方向相關，但多數為間接證據（如 SN-38 抗體藥物複合體、混合實體瘤的早期試驗）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 結腸癌轉移、胰腺癌（來自 TxGNN 知識圖譜；香港許可證未提供適應症文字） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.08% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 16 張 |
| 建議決策 | Hold（列為研究問題，待補強證據） |

---

## 為什麼這個預測合理？

Irinotecan 是 SN-38 的前驅藥物，SN-38 為拓樸異構酶 I 抑制劑，可造成 DNA 損傷並誘導快速分裂細胞凋亡。目前缺乏 DrugBank 的詳細作用機轉資料，以上機轉是根據已知藥理推論，而非直接取自資料庫。

間接證據來自 sacituzumab govitecan（抗 Trop-2 抗體連接 SN-38）。其 Phase III 試驗 TROPiCS-02 針對 HR+/HER2- 轉移性乳癌，顯示 SN-38 作為載荷在乳癌中具活性。但這**並不能證明 irinotecan 本身**對乳癌有效。

另有一篇 2003 年的文獻指出，irinotecan 與 mitomycin 在乳癌中單藥活性有限（marginal activity），但臨床前研究顯示兩者循序使用可能有協同作用。TxGNN 的高分是計算預測，不等同臨床證據。

---

## 臨床試驗證據

以下為與乳癌相關性較高的試驗（未列出相關性低、無實際資料者，如已撤回的 NCT05238831）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00083148](https://clinicaltrials.gov/study/NCT00083148) | Phase 1 | 完成 | 12 | Irinotecan 後接 capecitabine 用於晚期乳癌；直接針對目標疾病，但規模小，僅提供安全性與可行性資訊 |
| [NCT00031681](https://clinicaltrials.gov/study/NCT00031681) | Phase 1 | 完成 | 41 | UCN-01 併用 irinotecan，用於抗藥性實體瘤及三陰性乳癌；僅早期安全性資料 |
| [NCT00004095](https://clinicaltrials.gov/study/NCT00004095) | Phase 1 | 完成 | 38 | Irinotecan 併用 gemcitabine 於混合實體瘤；非乳癌特異 |
| [NCT03678883](https://clinicaltrials.gov/study/NCT03678883) | Phase 2 | 進行中（不招募） | 350 | 9-ING-41（GSK-3β 抑制劑）單用或併用化療；irinotecan 的乳癌貢獻不明確 |
| [NCT05453825](https://clinicaltrials.gov/study/NCT05453825) | Phase 2 | 未知 | 180 | Navicixizumab 單用或併用 paclitaxel/irinotecan，含三陰性乳癌組；irinotecan 非核心 |
| [NCT02419495](https://clinicaltrials.gov/study/NCT02419495) | Phase 1 | 終止 | 221 | Selinexor 併用多種標準化療；irinotecan 貢獻不明 |
| [NCT06840886](https://clinicaltrials.gov/study/NCT06840886) | Phase 1 | 招募中 | 426 | PHST001 於晚期實體瘤；irinotecan 角色不明 |
| [NCT06769425](https://clinicaltrials.gov/study/NCT06769425) | Phase 1 | 招募中 | 157 | HS-10502（PARP1 抑制劑）組合治療；irinotecan 角色不明 |

目前沒有已完成的 Phase 2/3 試驗直接評估 irinotecan 於乳癌的療效。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32223649](https://pubmed.ncbi.nlm.nih.gov/32223649/) | 2020 | Phase III 試驗設計 | Future Oncology | TROPiCS-02：sacituzumab govitecan（SN-38 載荷）用於 HR+/HER2- 轉移性乳癌 |
| [25944802](https://pubmed.ncbi.nlm.nih.gov/25944802/) | 2015 | Phase 1 | Clin Cancer Res | Sacituzumab govitecan 首次人體試驗，用於多種轉移性實體瘤 |
| [41371050](https://pubmed.ncbi.nlm.nih.gov/41371050/) | 2026 | Phase 2 | Eur J Cancer | PHENOMENAL：脂質體 irinotecan 用於 HER2 陰性乳癌合併腦轉移（該脂質體劑型可穿越血腦屏障） |
| [40877204](https://pubmed.ncbi.nlm.nih.gov/40877204/) | 2025 | 臨床研究 | Cancer Reports | Etirinotecan pegol 用於肺癌或乳癌的活動性腦轉移 |
| [40749148](https://pubmed.ncbi.nlm.nih.gov/40749148/) | 2025 | 早期臨床 | J Clin Oncol | DEP-SN38 於晚期實體瘤的安全性、耐受性與初步療效 |
| [12800602](https://pubmed.ncbi.nlm.nih.gov/12800602/) | 2003 | 回顧 | Oncology (Williston Park) | Mitomycin 與 irinotecan 單藥於乳癌活性有限，但循序使用具臨床前協同作用 |
| [9726101](https://pubmed.ncbi.nlm.nih.gov/9726101/) | 1998 | 回顧 | Oncology (Williston Park) | Irinotecan 在淋巴瘤、白血病及乳癌、胰臟癌、卵巢癌、小細胞肺癌等的活性概述 |
| [26101915](https://pubmed.ncbi.nlm.nih.gov/26101915/) | 2015 | 臨床前 | Oncotarget | Trop-2 為 SN-38 抗體藥物複合體的新標靶 |
| [28558150](https://pubmed.ncbi.nlm.nih.gov/28558150/) | 2017 | 回顧／臨床前 | Cancer | Sacituzumab govitecan 於多種上皮癌的安全性與藥動學 |
| [40244130](https://pubmed.ncbi.nlm.nih.gov/40244130/) | 2025 | 臨床前 | Int J Mol Sci | PD-L1 標靶奈米粒子（含 SN38）用於三陰性乳癌模型 |

文獻中多數屬於間接證據：以 SN-38 為載荷的藥物，或其他劑型（脂質體、聚乙二醇化）的研究，並非傳統 irinotecan 本身。

---

## 香港上市資訊

香港共有 16 張有效許可證，皆為單方注射濃縮液。以下列出 5 張主要許可證，許可證資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-42884 | CAMPTO CONC FOR INFUSION 20MG/ML（Pfizer） | 輸注用濃縮液 | 未提供 |
| HK-67985 | ONIVYDE PEGYLATED LIPOSOMAL CONCENTRATE FOR DISPERSION FOR INFUSION 43MG/10ML（Servier） | 脂質體輸注濃縮液 | 未提供 |
| HK-65294 | DBL IRINOTECAN CONCENTRATE FOR SOLUTION FOR INFUSION 40MG/2ML（Pfizer） | 輸注用濃縮液 | 未提供 |
| HK-58691 | IRINOTESIN CONCENTRATE FOR INF 100MG/5ML（Teva） | 輸注用濃縮液 | 未提供 |
| HK-68057 | IRINOCAN 100 CONCENTRATE FOR SOLUTION FOR INFUSION 100MG/5ML（Jacobson） | 輸注用濃縮液 | 未提供 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（拓樸異構酶 I 抑制劑） |
| 骨髓抑制風險 | 高（知識圖譜顯示與嗜中性白血球減少、血小板減少、貧血相關的禁忌關聯） |
| 致吐性分級 | 中度（依藥物類別判斷） |
| 監測項目 | CBC（含分類）、肝功能（含膽紅素）、腎功能、電解質、腹瀉狀況 |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

詳細警語與注意事項請參考原廠仿單。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病關聯**（來自 TxGNN 知識圖譜，非仿單文字）：腎臟疾病、胰臟炎、肝臟疾病、膽囊疾病、血小板減少、嗜中性白血球減少、顆粒球缺乏症、貧血、腸阻塞、腸道阻塞、高膽紅素血症（含 Gilbert 症候群）、間質性肺病、腹瀉性疾病。
- **藥物交互作用**：資料庫共有 100 筆紀錄，以下為部分重點：
  - **重大 (Major)**：Clarithromycin
  - **中度 (Moderate)**：Aprepitant、Dexamethasone、Cimetidine、Miconazole、Eluxadoline、Metreleptin，以及多種瀉劑與滲透性藥物（Bisacodyl、Picosulfuric acid、Magnesium sulfate/citrate/hydroxide、Castor oil、Glycerin、Lactitol、Lactulose、Mannitol、Mineral oil、Phenolphthalein）
  - **輕微 (Minor)**：Levofloxacin

香港仿單的警語與禁忌資料尚未取得，請以原廠仿單為準。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前證據屬 L3：直接評估 irinotecan 於乳癌的試驗僅有小型 Phase 1，其餘多為 SN-38 載荷藥物或脂質體等不同劑型的間接證據。TxGNN 分數高（99.08%）屬計算預測，非臨床證據。
- 既有文獻甚至指出 irinotecan 在乳癌的單藥活性有限，且藥物本身的骨髓抑制與腹瀉風險較高，需要更強的直接證據。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症，完成安全性篩選
- 補充 DrugBank 的作用機轉資料
- 釐清脂質體 irinotecan（如 PHENOMENAL 研究）、etirinotecan pegol 等劑型的結果能否外推到一般 irinotecan 製劑
- 針對特定亞型（如三陰性乳癌、HER2 陰性合併腦轉移）設計或尋找 Phase 2 以上、直接使用 irinotecan 的試驗
- 評估 UGT1A1 基因型檢測（藥物基因體學）以管理毒性風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

