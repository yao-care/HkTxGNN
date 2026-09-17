---
layout: default
title: Lenalidomide
parent: 高證據等級 (L1-L2)
nav_order: 444
evidence_level: L2
indication_count: 5
---

# Lenalidomide
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Lenalidomide：從多發性骨髓瘤／MDS(del5q) 到骨髓性白血病 (Myeloid Leukemia)

## 一句話總結

Lenalidomide 是一種 cereblon (CRBN) E3 ligase 調節劑，目前已核准用於多發性骨髓瘤與 del(5q) 骨髓增生不良症候群 (MDS)。
TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效，
目前有 **50 個臨床試驗**和 **20 篇文獻**支持這個方向，多數聚焦於 lenalidomide 併用 azacitidine 治療 AML/高風險 MDS。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 多發性骨髓瘤、MDS del(5q)（資料來自機轉關聯性敘述，非正式仿單摘錄） |
| 預測新適應症 | 骨髓性白血病 (Myeloid Leukemia) |
| TxGNN 預測分數 | 99.49% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Lenalidomide 是 cereblon (CRBN) E3 ligase 調節劑，透過降解 IKZF1/IKZF3 轉錄因子產生免疫調節與抗血管新生作用，目前已核准用於多發性骨髓瘤與 del(5q) MDS 的治療。

MDS 與急性骨髓性白血病 (AML) 同屬骨髓造血幹細胞的克隆性疾病，且 MDS 本身有相當比例會轉化為 AML（證據中 NCT02921815 即為專門監測 MDS 轉 AML 的上市後研究），兩者在細胞遺傳學異常（尤其是 del(5q) 亞群）上高度重疊。

機轉外推的合理性也反映在大量已完成的臨床試驗上：lenalidomide 與 azacitidine 併用治療 AML/高風險 MDS 已是被廣泛研究的組合療法（如 NCT00352001、NCT01743859、NCT03118466 等），且有系統性回顧/統合分析（PMID 31221030、30271212）評估其療效與安全性，顯示此適應症外推並非單純模型臆測，而有相當的臨床探索基礎。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00360672](https://clinicaltrials.gov/study/NCT00360672) | Phase 2 | 完成 | 27 | Lenalidomide 治療復發/難治性 AML 或 chromosome 5 異常之高風險 MDS，直接療效證據 |
| [NCT00352001](https://clinicaltrials.gov/study/NCT00352001) | Phase 1/2 | 完成 | 37 | Lenalidomide + Azacitidine 併用治療進展期 MDS，核心組合療法證據 |
| [NCT00957385](https://clinicaltrials.gov/study/NCT00957385) | Phase 2（隨機） | 完成 | 24 | Lenalidomide 用於 AML 緩解後維持治療，具對照設計 |
| [NCT01358734](https://clinicaltrials.gov/study/NCT01358734) | Phase 2（隨機） | 完成 | 88 | 比較高劑量 lenalidomide、azacitidine+lenalidomide 序貫療法與 azacitidine 單用於老年新診斷 AML |
| [NCT01029262](https://clinicaltrials.gov/study/NCT01029262) | Phase 3 | 完成 | 239 | Lenalidomide vs 安慰劑用於輸血依賴型低/中危 MDS 貧血，本組唯一已完成的 Phase 3 RCT |
| [NCT01743859](https://clinicaltrials.gov/study/NCT01743859) | Phase 2 | 完成 | 37 | Azacitidine 序貫 Lenalidomide 治療復發/難治性 AML 及高風險 MDS |
| [NCT03118466](https://clinicaltrials.gov/study/NCT03118466) | Phase 2 | 完成 | 41 | MEC 化療併用 Lenalidomide 治療復發/難治性 AML |
| [NCT02126553](https://clinicaltrials.gov/study/NCT02126553) | Phase 2 | 完成 | 29 | Lenalidomide 用於高風險 AML 緩解期維持治療 |
| [NCT00840931](https://clinicaltrials.gov/study/NCT00840931) | Phase 1 | 完成 | 22 | Lenalidomide + Bystander 疫苗免疫治療高風險 MDS，概念驗證研究 |
| [NCT01342692](https://clinicaltrials.gov/study/NCT01342692) | Phase 2（隨機） | 狀態未知 | 320 | 尋找與 Azacitidine 併用之最佳藥物（含 Lenalidomide）用於高風險 MDS，樣本數大但結果追蹤不明 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31221030](https://pubmed.ncbi.nlm.nih.gov/31221030/) | 2019 | 系統性回顧/統合分析 | Hematology (Amsterdam) | Azacitidine+Lenalidomide 治療 AML/MDS/CMML 之療效與不良反應統合分析 |
| [30271212](https://pubmed.ncbi.nlm.nih.gov/30271212/) | 2018 | 系統性回顧/統合分析 | Cancer Management and Research | Lenalidomide 治療 AML 療效與安全性統合分析，療效是否顯著仍有爭議 |
| [37288607](https://pubmed.ncbi.nlm.nih.gov/37288607/) | 2023 | Review | American Journal of Hematology | MDS 診斷、風險分層與治療 2023 年更新 |
| [35320468](https://pubmed.ncbi.nlm.nih.gov/35320468/) | 2022 | Review | Current Treatment Options in Oncology | MDS 治療新方法回顧 |
| [23316859](https://pubmed.ncbi.nlm.nih.gov/23316859/) | 2013 | Review | Expert Opinion on Investigational Drugs | Lenalidomide 作為 AML 新治療選項之回顧 |
| [23644421](https://pubmed.ncbi.nlm.nih.gov/23644421/) | 2013 | Cohort | Leukemia | Azacitidine+Lenalidomide 併用於 MDS/AML 之臨床應用評析 |
| [37259567](https://pubmed.ncbi.nlm.nih.gov/37259567/) | 2023 | Cohort | Haematologica | Azalena 試驗：Azacitidine+Lenalidomide+DLI 用於異體移植後 MDS/AML/CMML 復發 |
| [35512188](https://pubmed.ncbi.nlm.nih.gov/35512188/) | 2022 | Cohort/Mechanistic | Blood | Lenalidomide 與 TP53 突變治療相關骨髓腫瘤發生之關聯 |
| [34471239](https://pubmed.ncbi.nlm.nih.gov/34471239/) | 2021 | Cohort | Bone Marrow Transplantation | 移植後高風險 MDS/AML 患者 Lenalidomide 維持治療之安全性與耐受性 |
| [37435080](https://pubmed.ncbi.nlm.nih.gov/37435080/) | 2023 | Cohort | Frontiers in Immunology | Azacitidine+低劑量 Lenalidomide 作為異體移植後 AML 復發預防新方案 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶/免疫調節藥物（Cereblon E3 ligase 調節劑, IMiD），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 資料缺乏，請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 資料缺乏，請參考原廠仿單的警語與注意事項 |
| 監測項目 | 資料缺乏，請參考原廠仿單的警語與注意事項 |
| 處置防護 | 資料缺乏，請參考原廠仿單的警語與注意事項 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有 1 個完成的 Phase 3 RCT、多個完成的 Phase 2 試驗，以及 2 篇系統性回顧/統合分析支持 lenalidomide（尤其併用 azacitidine）於 AML/高風險 MDS 的療效訊號，機轉外推合理。
- 但香港未上市（0 張許可證）、且仿單警語/禁忌症資料完全缺失（DG001，Blocking），無法完成 S1 安全性初評，不能貿然推進。

**若要推進需要：**
- 取得完整仿單警語與禁忌症資料（DG001）
- 補充 DrugBank 完整 MOA 資料（DG002）
- 評估香港上市/引進管道
- 進一步檢視 NCT01029262（唯一完成之 Phase 3 RCT）及 azacitidine 併用試驗的最終療效數據，確認是否足以支持下一階段臨床評估
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

