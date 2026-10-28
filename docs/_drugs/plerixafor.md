---
layout: default
title: Plerixafor
parent: 僅模型預測 (L5)
nav_order: 709
evidence_level: L5
indication_count: 6
monitor_inn: "PLERIXAFOR"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "bronchitis", "vulvar melanoma (disease)", "myeloid leukemia"]
last_modified_at: 2026-10-23
description: "Plerixafor：預測新適應症為CMM7（證據等級 L5）。原適應症：香港許可證文字未載明適應症"
---

# Plerixafor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Plerixafor：從漿細胞骨髓瘤到 CMM7
{: .text-alpha }

## 一句話總結

Plerixafor 是 CXCR4 拮抗劑，知識圖譜記錄它與**漿細胞骨髓瘤 (plasma cell myeloma)** 有關聯。
TxGNN 模型預測排名第一的新適應症是 **CMM7**，預測分數很高，但目前**沒有任何臨床試驗或文獻**直接支持，屬於純模型預測。
在其他預測中，**骨髓性白血病 (myeloid leukemia)** 有較多研究，詳見後文。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證文字未載明適應症；知識圖譜記錄的關聯為漿細胞骨髓瘤（此為知識圖譜關聯，不等同核准適應症） |
| 預測新適應症 | CMM7 |
| TxGNN 預測分數 | 0.9934 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Plerixafor 是 CXCR4 拮抗劑，也作用於 ACKR3，會阻斷 CXCR4 與 CXCL12 的結合。這一點來自藥理學資料，不是香港仿單。

就 CMM7 而言，現有資料無法建立機轉上的連結。高分只是計算模型的結果，這個疾病與藥物作用機轉的關聯性尚未評估，也沒有試驗或文獻佐證。因此不能把它視為臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-60176 | MOZOBIL INJ 20MG/ML | SANOFI HONG KONG LIMITED |
| HK-67839 | PLERIXAFOR SOLUTION FOR INJECTION 24MG/1.2ML | SINO PACIFIC PHARMA COMPANY LIMITED |

兩張許可證皆為有效狀態，但本報告所用資料未收錄劑型與核准適應症文字。

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：血小板低下症、腎功能受損、白血病。
- **藥理學資料庫的靶點資訊**：資料庫中列出的兩筆項目是藥理靶點 CXCR4 與 ACKR3，並非藥物交互作用。

其餘安全性資訊請參考原廠仿單。

## 其他預測適應症：骨髓性白血病（研究最多）

TxGNN 對骨髓性白血病的預測分數為 0.9902（整體第 6 順位），研究資料遠多於 CMM7。

**機轉：** Plerixafor 阻斷 CXCR4/CXCL12 (SDF-1) 軸。這條軸把白血病細胞固定在骨髓保護性微環境中。阻斷後，白血病細胞可能被動員到循環血中，並對化療或標靶藥物更敏感，例如 FLT3 突變 AML 合併 sorafenib。

**證據等級：L3。** 有針對白血病本身的 Phase 1/2 試驗和一篇系統性回顧，但沒有已完成的 Phase 3 RCT，也沒有隨機分組的療效比較，因此未達 L2。

### 代表性臨床試驗（共 25 項，列出 10 項）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00943943](https://clinicaltrials.gov/study/NCT00943943) | Phase 1 | 完成 | 33 | G-CSF + plerixafor + sorafenib 用於 FLT3 突變 AML，探討最大耐受劑量與安全性 |
| [NCT01435343](https://clinicaltrials.gov/study/NCT01435343) | Phase 1/2 | 完成 | 55 | 以 fludarabine、idarubicin、cytarabine、G-CSF 和 plerixafor 作為復發/難治 AML 的誘導治療 |
| [NCT01236144](https://clinicaltrials.gov/study/NCT01236144) | Phase 1/2 | 完成 | 113 | NCRI AML 試驗，評估 plerixafor 等藥物併用化療於高齡 AML 與高風險 MDS 的可行性 |
| [NCT00512252](https://clinicaltrials.gov/study/NCT00512252) | Phase 1/2 | 完成 | 52 | AMD3100 + MEC 用於復發/難治 AML，假設阻斷骨髓微環境可增強化療 |
| [NCT01352650](https://clinicaltrials.gov/study/NCT01352650) | Phase 1 | 完成 | 71 | Decitabine + plerixafor 用於 60 歲以上 AML |
| [NCT00990054](https://clinicaltrials.gov/study/NCT00990054) | Phase 1 | 完成 | 36 | Plerixafor 合併 7+3 方案，用於新診斷 AML |
| [NCT00906945](https://clinicaltrials.gov/study/NCT00906945) | Phase 1/2 | 完成 | 39 | Plerixafor + G-CSF 化療增敏，用於復發/難治 AML |
| [NCT01141543](https://clinicaltrials.gov/study/NCT01141543) | 未標示 | 完成 | 12 | 在清髓性預處理中以 plerixafor 動員白血病細胞 |
| [NCT01027923](https://clinicaltrials.gov/study/NCT01027923) | Phase 1 | 提前終止 | 6 | 靜脈注射 plerixafor 合併 MEC，樣本極少，證據有限 |
| [NCT06141304](https://clinicaltrials.gov/study/NCT06141304) | Phase 2 | 狀態未知 | 28 | Plerixafor + 供者淋巴球輸注，用於異體移植後復發的急性白血病，單臂、無結果 |

### 代表性文獻（共 20 篇，列出 8 篇）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32877869](https://pubmed.ncbi.nlm.nih.gov/32877869/) | 2020 | 系統性回顧 | Leukemia Research | 彙整 plerixafor 合併化療/移植治療急性白血病的前臨床與臨床研究，供設計確證性試驗參考 |
| [32697348](https://pubmed.ncbi.nlm.nih.gov/32697348/) | 2020 | Phase 1 | American Journal of Hematology | Sorafenib + G-CSF + plerixafor 用於復發/難治 FLT3-ITD AML，28 位患者 |
| [29724902](https://pubmed.ncbi.nlm.nih.gov/29724902/) | 2018 | Phase 1 | Haematologica | Plerixafor 合併 decitabine 用於高齡新診斷 AML，69 位患者 |
| [29392425](https://pubmed.ncbi.nlm.nih.gov/29392425/) | 2018 | Phase 1-2 | Annals of Hematology | PLERIFLAG 方案用於早期復發/難治 AML |
| [30654137](https://pubmed.ncbi.nlm.nih.gov/30654137/) | 2019 | Phase 1 報告 | Biol Blood Marrow Transplant | 評估清髓性預處理併用 plerixafor 的安全性與耐受性 |
| [39261603](https://pubmed.ncbi.nlm.nih.gov/39261603/) | 2024 | Review | Leukemia | CXCR4 作為 AML 治療標靶 |
| [29140182](https://pubmed.ncbi.nlm.nih.gov/29140182/) | 2018 | 前臨床 | Hematology | 阻斷 CXCR4 影響 AML 細胞與間質細胞共培養的化療敏感性 |
| [19657955](https://pubmed.ncbi.nlm.nih.gov/19657955/) | 2009 | 前臨床 | Leukemia & Lymphoma | Plerixafor 提高 BCR-ABL 陽性細胞對 imatinib 與 nilotinib 的敏感度 |

以上多為早期單臂研究，且摘要未提供療效結論，不能據此判斷療效。

## 結論與下一步

**決策：Hold**（針對 CMM7）

**理由：**
- CMM7 只有模型預測，沒有試驗或文獻，也缺乏作用機轉資料，只能列為 L5。
- 骨髓性白血病有明確機轉與多項早期臨床研究，但缺乏隨機對照療效證據，目前宜視為值得優先研究的問題，而不是可直接推進的適應症。

**若要推進需要：**
- 取得香港仿單，補齊核准適應症、警語與禁忌。
- 補充詳細的作用機轉資料。
- 釐清 CMM7 的疾病定義，並檢視其與 CXCR4 軸的生物學關聯。
- 針對骨髓性白血病，取得上述試驗的療效與安全性結果，並評估是否需要隨機對照試驗。
- 評估知識圖譜記錄的血小板低下、腎功能受損等風險。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

