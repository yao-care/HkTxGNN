---
layout: default
title: Irinotecan
parent: 高證據等級 (L1-L2)
nav_order: 412
evidence_level: L2
indication_count: 1
---

# Irinotecan
{: .fs-9 }

證據等級: **L2** | 預測適應症: **1** 個
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

# Irinotecan：從大腸直腸癌到乳癌

## 一句話總結

> Irinotecan（CPT-11）是拓撲異構酶 I（Topoisomerase I）抑制劑前驅藥，國際上原本核准用於大腸直腸癌治療（常與 5-FU/leucovorin 併用，即 FOLFIRI 療法）。TxGNN 模型預測它可能對**乳癌（Female Breast Carcinoma）**有效，目前有多個臨床試驗、**20 篇文獻**支持此方向，其活性代謝物 SN-38 更已透過抗體藥物複合體在乳癌領域證實 Phase 3 療效。

> ⚠️ 注意：Evidence Pack 中「原適應症」欄位（`drug.original_indications`、香港許可證資料）皆為空值，本藥物目前**未在香港上市**。上述「大腸直腸癌」為國際通用核准適應症之背景描述，非香港在地核准資料。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 大腸直腸癌（國際通用核准適應症，非香港在地資料） |
| 預測新適應症 | 乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.08% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Evidence Pack 中 `drug.original_moa` 欄位標示為資料缺口，但證據內容（`repurposing_rationale.mechanistic_link`）提供了機轉線索：Irinotecan 是拓撲異構酶 I（Topoisomerase I）抑制劑前驅藥，經 carboxylesterase 代謝為活性代謝物 **SN-38**。

SN-38 已透過抗體藥物複合體 **sacituzumab govitecan**（TROP-2 標靶抗體 + SN-38 payload）在 HR+/HER2− 及三陰性乳癌（TNBC）族群中，經 Phase 3 隨機對照試驗（TROPiCS-02）證實療效，驗證了拓撲異構酶 I 抑制在乳癌治療中的機轉可行性。

不過，這是 SN-38 以「標靶遞送」形式在乳癌中的證據，並非游離態 irinotecan 本身的直接療效證據。過去數十年多項 irinotecan 單藥 Phase II 單臂試驗顯示活性中等（緩解率約 15-25%），尚未取代既有標準治療，也從未進入 Phase 3 RCT 驗證其在乳癌的角色。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00072852](https://clinicaltrials.gov/study/NCT00072852) | Phase 2 | 完成 | 134 | Irinotecan 單藥治療 anthracycline/taxane/capecitabine 治療失敗後轉移性乳癌，比較兩種給藥排程 |
| [NCT03562390](https://clinicaltrials.gov/study/NCT03562390) | Phase 2 | 狀態未知 | 124 | Irinotecan 三線以上治療中國大陸轉移性乳癌患者的安全性與療效 |
| [NCT00083148](https://clinicaltrials.gov/study/NCT00083148) | Phase 1 | 完成 | 12 | Irinotecan 後續接續 capecitabine 治療晚期乳癌，劑量遞增試驗 |
| [NCT01770353](https://clinicaltrials.gov/study/NCT01770353) | Phase 1 | 完成 | 45 | 脂質體 irinotecan (MM-398/nal-IRI) 腫瘤藥物濃度與 MRI 影像預測反應之可行性研究 |
| [NCT00031681](https://clinicaltrials.gov/study/NCT00031681) | Phase 1 | 完成 | 41 | UCN-01 併用 irinotecan 治療三陰性復發性乳癌（2007 年起限收 TNBC） |
| [NCT05453825](https://clinicaltrials.gov/study/NCT05453825) | Phase 2 | 狀態未知 | 180 | Navicixizumab 單用或併用 paclitaxel/irinotecan，含 TNBC 族群 |
| [NCT03170960](https://clinicaltrials.gov/study/NCT03170960) | Phase 1 | 進行中（未招募） | 914 | Cabozantinib 併用 atezolizumab 治療多種實體腫瘤，含 TNBC 族群 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32223649](https://pubmed.ncbi.nlm.nih.gov/32223649/) | 2020 | RCT | Future Oncology | TROPiCS-02 Phase 3 研究：sacituzumab govitecan（SN-38 為 irinotecan 活性代謝物）治療 HR+/HER2− 轉移性乳癌 |
| [36027558](https://pubmed.ncbi.nlm.nih.gov/36027558/) | 2022 | RCT | J Clin Oncol | Sacituzumab govitecan 於 HR+/HER2− 轉移性乳癌之隨機對照試驗結果 |
| [30786188](https://pubmed.ncbi.nlm.nih.gov/30786188/) | 2019 | Cohort | NEJM | Sacituzumab govitecan-hziy 治療頑固性轉移性三陰性乳癌 |
| [28291390](https://pubmed.ncbi.nlm.nih.gov/28291390/) | 2017 | 單臂試驗 | J Clin Oncol | Sacituzumab govitecan（SN-38 複合體）於重度治療後轉移性 TNBC 之療效與安全性 |
| [41371050](https://pubmed.ncbi.nlm.nih.gov/41371050/) | 2026 | Phase 2 研究 | Eur J Cancer | PHENOMENAL 研究：脂質體 irinotecan (nal-IRI) 治療 HER2 陰性乳癌腦轉移患者 |
| [12800602](https://pubmed.ncbi.nlm.nih.gov/12800602/) | 2003 | Review | Oncology (Williston Park) | Mitomycin 與 irinotecan 併用治療晚期乳癌之機轉基礎（mitomycin 上調 topoisomerase I 表現） |
| [9726101](https://pubmed.ncbi.nlm.nih.gov/9726101/) | 1998 | Review | Oncology (Williston Park) | Irinotecan 於淋巴瘤、白血病及乳癌、胰臟癌等多種腫瘤之活性回顧 |
| [36302269](https://pubmed.ncbi.nlm.nih.gov/36302269/) | 2022 | Review | Breast (Edinburgh) | TROP-2 標靶抗體藥物複合體於轉移性乳癌之臨床開發回顧 |
| [39768216](https://pubmed.ncbi.nlm.nih.gov/39768216/) | 2024 | Review | Cells | Sacituzumab govitecan 治療頑固性三陰性乳癌之精準醫療新紀元 |
| [25944802](https://pubmed.ncbi.nlm.nih.gov/25944802/) | 2015 | Phase 1 試驗 | Clin Cancer Res | Anti-Trop-2/SN-38 複合體 sacituzumab govitecan 首次人體試驗，涵蓋乳癌等多種轉移性實體腫瘤 |

---

## 細胞毒性

**分類依據**：Irinotecan 為 camptothecin 衍生物、拓撲異構酶 I 抑制劑前驅藥（依證據內文 `repurposing_rationale.mechanistic_link` 及文獻 PMID 12800602 確認機轉），屬傳統細胞毒性化療藥物。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Topoisomerase I 抑制劑，Camptothecin 衍生物） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

> 安全性資訊請參考原廠仿單。

（Evidence Pack 標示 TFDA/HK 仿單警語與禁忌症資料缺口為 **Blocking** 等級，DDI 查詢無結果。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉上有 Phase 3 RCT（TROPiCS-02）支持 SN-38（irinotecan 活性代謝物）於乳癌的療效，但這是標靶遞送形式的證據，游離態 irinotecan 本身僅有 Phase 1/2 單臂試驗（部分狀態未知），未達 L1 等級。
- 該藥目前未在香港上市，且缺乏仿單警語、禁忌症等關鍵安全性資料（Blocking 等級缺口），無法進入安全性初評。

**若要推進需要：**
- 取得 TFDA/香港仿單完整警語與禁忌症資料，解除 DG001 阻塞
- 補齊 DrugBank MOA 完整資料（DG002）
- 評估游離態 irinotecan（非 ADC 形式）於乳癌之直接臨床證據是否足以支持後續試驗設計
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

