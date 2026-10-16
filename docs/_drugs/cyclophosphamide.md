---
layout: default
title: Cyclophosphamide
parent: 高證據等級 (L1-L2)
nav_order: 234
evidence_level: L2
indication_count: 5
last_modified_at: 2026-10-14
description: "Cyclophosphamide：預測新適應症為骨髓性白血病 (Myeloid Leukemia)（證據等級 L2）。原適應症：蕈狀肉芽腫、多發性骨髓瘤、神經母細胞瘤、淋巴瘤、乳癌、視網膜母細胞瘤等"
monitor_inn: "CYCLOPHOSPHAMIDE"
predicted_indications: ["myeloid leukemia", "ganglioneuroblastoma (disease)", "vertebral anomalies and variable endocrine and T-cell dysfunction", "retroperitoneal neoplasm", "lymph node cancer"]
---

# Cyclophosphamide
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

# Cyclophosphamide：從淋巴瘤與乳癌等惡性腫瘤到骨髓性白血病

## 一句話總結

Cyclophosphamide 是烷化劑類細胞毒性藥物，原本用於蕈狀肉芽腫、多發性骨髓瘤、神經母細胞瘤、淋巴瘤、乳癌、視網膜母細胞瘤等癌症。
TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效，
目前有 **30 個臨床試驗**和 **20 篇文獻**支持這個方向，但多數是將它當作移植前預處理或移植後 GVHD 預防的一環，其單獨貢獻不易釐清。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 蕈狀肉芽腫、多發性骨髓瘤、神經母細胞瘤、淋巴瘤、乳癌、視網膜母細胞瘤等（香港許可證未登載適應症文字，此為知識圖譜所列適應症） |
| 預測新適應症 | 骨髓性白血病 (Myeloid Leukemia) |
| TxGNN 預測分數 | 99.47% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Cyclophosphamide 是烷化劑，具細胞毒性與淋巴細胞清除／免疫抑制作用。

在骨髓性白血病中，它主要用於兩種情境：
1. 作為異體造血幹細胞移植的預處理方案成分（如 busulfan-cyclophosphamide、cyclophosphamide/fludarabine）。
2. 作為移植後 cyclophosphamide（PTCy），選擇性清除具同種反應性的 T 細胞，預防單倍體相合及其他異體移植的移植物抗宿主病（GVHD）。

這與它原有的腫瘤與免疫抑制用途在機轉上相符。需要注意的是，多數試驗把它放在多藥或移植方案中，因此很難分離出 cyclophosphamide 本身的獨立貢獻。

---

## 臨床試驗證據

資料中共有 30 個相關試驗，以下列出與 cyclophosphamide 最相關的 10 個：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04473911](https://clinicaltrials.gov/study/NCT04473911) | Phase 1 | 完成 | 25 | 單倍體周邊血幹細胞移植，以 PTCy 為核心預防 GVHD，適用骨髓性惡性腫瘤 |
| [NCT00315705](https://clinicaltrials.gov/study/NCT00315705) | Phase 1/2 | 完成 | 50 | Clofarabine 併 etoposide、cyclophosphamide 用於兒童復發／難治急性白血病 |
| [NCT00003187](https://clinicaltrials.gov/study/NCT00003187) | Phase 2/3 | 完成 | 19 | 非親屬捐贈骨髓移植，比較傳統與去 T 細胞移植 |
| [NCT00390793](https://clinicaltrials.gov/study/NCT00390793) | Phase 2 | 完成 | 107 | Hyper-CVAD 併 dasatinib 用於 Ph+ ALL，結果受 dasatinib 干擾 |
| [NCT01350245](https://clinicaltrials.gov/study/NCT01350245) | Phase 2 | 完成 | 28 | 兩步驟單倍體異體移植用於血液惡性腫瘤 |
| [NCT04904588](https://clinicaltrials.gov/study/NCT04904588) | Phase 2 | 進行中（不招募） | 300 | HLA 不全相合非親屬捐贈移植併 PTCy 預防 GVHD |
| [NCT00309842](https://clinicaltrials.gov/study/NCT00309842) | Phase 2 | 完成 | 213 | 臍帶血移植，採 cyclophosphamide/fludarabine/TBI 清髓預處理 |
| [NCT05515029](https://clinicaltrials.gov/study/NCT05515029) | Phase 3 | 進行中（不招募） | 56 | PTCy 併 abatacept、vedolizumab 及鈣調神經磷酸酶抑制劑預防 GVHD（兒童與年輕成人） |
| [NCT02724163](https://clinicaltrials.gov/study/NCT02724163) | Phase 3 | 進行中（不招募） | 700 | 兒童 AML 國際隨機試驗，評估 gemtuzumab ozogamicin 與誘導化療 |
| [NCT07183878](https://clinicaltrials.gov/study/NCT07183878) | N/A | 招募中 | 138 | 隨機比較 Ven-BUCY 與標準 BUCY 預處理用於高風險 AML／MDS |

---

## 文獻證據

資料中的文獻以世代研究與回顧為主，未見隨機對照試驗：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36357773](https://pubmed.ncbi.nlm.nih.gov/36357773/) | 2023 | 系統性回顧／網絡統合分析 | Bone Marrow Transplant | 比較成人 AML 緩解期異體移植的清髓性預處理方案（含 Bu/Cy） |
| [14662323](https://pubmed.ncbi.nlm.nih.gov/14662323/) | 2003 | Review | Exp Hematol | 比較 Bu-Cy 與 TBI-Cy 預處理用於 AML 的研究，結果並不一致 |
| [38758817](https://pubmed.ncbi.nlm.nih.gov/38758817/) | 2024 | Cohort | Cancer | EBMT 報告：單倍體移植中 PTCy、ATG 及兩者合併預防 GVHD 的比較 |
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | Cohort | Future Oncol | 比較 BuCy 與 FluBu 預處理，FluBu 療效相近而毒性可能較低 |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Cohort | Am J Hematol | 165 位 AML 患者，Cy/Flu 非清髓移植與清髓移植存活結果比較 |
| [36842566](https://pubmed.ncbi.nlm.nih.gov/36842566/) | 2023 | Cohort | Transpl Immunol | PTCy 與早期混合嵌合現象，需在 GVHD 預防與復發風險間取得平衡 |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Cohort | Cytotherapy | 使用 PTCy 的單倍體移植治療 AML 之預後因子 |
| [41046309](https://pubmed.ncbi.nlm.nih.gov/41046309/) | 2026 | Cohort | Bone Marrow Transplant | AML 第一次緩解期，單一臍帶血移植與 PTCy 單倍體移植的登錄資料比較 |
| [42373850](https://pubmed.ncbi.nlm.nih.gov/42373850/) | 2026 | Cohort | Bone Marrow Transplant | ALWP/EBMT：次發性 AML 中單倍體與不全相合非親屬移植（均用 PTCy）比較 |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | 回溯研究 | Int J Mol Sci | 兒童 AML 在相合手足及非親屬移植後使用 PTCy 的經驗 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51711 | ENDOXAN TAB 50MG | — | — |
| HK-51308 | ENDOXAN FOR INJ 1G | — | — |
| HK-01327 | ENDOXAN 200 MG INJ | — | — |
| HK-50943 | CYCRAM FOR INJ 1G | — | — |

上述 4 張許可證皆為有效的單一成分製劑，目前資料未載明劑型與核准適應症文字。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（烷化劑） |
| 骨髓抑制風險 | 高（一般於高劑量預處理方案中特別明顯），詳細數據請參考原廠仿單 |
| 致吐性分級 | 中至高（依劑量而異） |
| 監測項目 | CBC（含分類）、肝腎功能、電解質、尿液檢查（出血性膀胱炎） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 筆交互作用，以下為部分範例（皆為 Moderate，除註明外）：
  - 抗黴菌藥：Amphotericin B（含脂質複合物、膽固醇硫酸酯、脂質體劑型）
  - 磺醯脲類降血糖藥：Chlorpropamide、Acetohexamide、Glimepiride、Glipizide、Glyburide、Tolazamide、Tolbutamide
  - 其他降血糖藥：Nateglinide、Repaglinide、Troglitazone
  - 其他：Bupropion、Aprepitant、Metronidazole、Nitisinone
  - Minor 等級：Levofloxacin、Ondansetron

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多項已完成的 Phase 2 及 Phase 2/3 試驗，並有大量移植相關世代研究支持 cyclophosphamide 於骨髓性白血病的預處理與 PTCy 用途，證據等級為 L2。
- 但絕大多數試驗是多藥或移植方案，cyclophosphamide 的獨立貢獻難以分離，且部分試驗規模很小。

**若要推進需要：**
- 取得作用機轉（MOA）資料以補強機轉分析
- 取得香港衛生署仿單的警語與禁忌症資料，並確認核准適應症文字（此項為完成安全性篩選的必要條件）
- 釐清各移植方案中 cyclophosphamide 的具體角色與劑量，優先分析 PTCy 相關試驗
- 針對移植情境擬定骨髓抑制、出血性膀胱炎及心臟毒性等的監測計畫

---

## 其他預測適應症（供參考）

| 排名 | 預測適應症 | 分數 | 證據等級 | 建議 |
|------|-----------|------|---------|------|
| 2 | 節細胞神經母細胞瘤 (Ganglioneuroblastoma) | 99.43% | L4 | Research Question |
| 3 | 椎骨異常合併內分泌及 T 細胞功能異常 | 99.38% | L5 | Hold |
| 4 | 腹膜後腫瘤 (Retroperitoneal neoplasm) | 99.37% | L4 | Research Question |
| 5 | 淋巴結癌 (Lymph node cancer) | 99.31% | L1 | Proceed with Guardrails |

淋巴結癌的 L1 證據主要來自淋巴結陽性乳癌的輔助化療 Phase 3 試驗（如 NCT00003782，n=5351），反映的是既有適應症的使用，並非真正的新適應症。椎骨異常合併 T 細胞功能異常一項目前僅有模型預測，無試驗與文獻，且免疫抑制劑對此類 T 細胞功能障礙可能不利，應暫緩。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

