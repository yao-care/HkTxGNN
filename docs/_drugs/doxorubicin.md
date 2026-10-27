---
layout: default
title: Doxorubicin
parent: 高證據等級 (L1-L2)
nav_order: 298
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Doxorubicin：預測新適應症為尤因氏肉瘤 (Ewing Sarcoma)（證據等級 L1）。原適應症：急性淋巴性白血病、何杰金氏淋巴瘤、非何杰金氏淋巴瘤、被套細胞淋巴瘤、蘭格漢斯細胞組織球增生症等"
monitor_inn: "Doxorubicin"
predicted_indications: ["Ewing sarcoma", "well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "monocytic leukemia", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "parameningeal embryonal rhabdomyosarcoma", "rhabdomyosarcoma (disease)", "ganglioneuroblastoma (disease)"]
---

# Doxorubicin
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

## Doxorubicin：從淋巴瘤與白血病到尤因氏肉瘤 (Ewing Sarcoma)
{: .text-alpha }

## 一句話總結

Doxorubicin（小紅莓，一種蒽環類化療藥）原本用於急性淋巴性白血病、何杰金氏與非何杰金氏淋巴瘤等血液腫瘤。
TxGNN 模型預測它可能對**尤因氏肉瘤 (Ewing Sarcoma)** 有效，
目前有 **28 筆臨床試驗**（其中數項為 Phase 3）和 **20 篇文獻**支持這個方向。
需要說明的是，尤因氏肉瘤的標準多藥方案（VDC/IE、VAC）本來就含有 doxorubicin，所以這比較像是對既有臨床用法的印證，而不是全新的再利用發現。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性淋巴性白血病、何杰金氏淋巴瘤、非何杰金氏淋巴瘤、被套細胞淋巴瘤、蘭格漢斯細胞組織球增生症等（香港許可證未登載適應症文字，此處依知識圖譜資料） |
| 預測新適應症 | 尤因氏肉瘤 (Ewing Sarcoma) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未收錄）。依一般藥理知識，doxorubicin 是拓撲異構酶 II 抑制劑，同時會嵌入 DNA，使快速增生的腫瘤細胞發生 DNA 損傷。

原適應症（白血病、淋巴瘤）和尤因氏肉瘤都是快速增生的惡性腫瘤，對 DNA 損傷型化療敏感。Doxorubicin 是尤因氏肉瘤標準多藥方案（VDC/IE 或 VAC/VAI）的骨幹之一，與模型給出的高分預測一致。

另外，此預測清單中的其他項目（如橫紋肌肉瘤、軟組織肉瘤、肺母細胞瘤）也顯示 doxorubicin 在肉瘤類疾病中有廣泛的使用基礎。

---

## 臨床試驗證據

資料中共有 28 筆相關試驗，以下列出最相關的 10 筆（優先選擇相關度高的完成型 Phase 2/3 試驗）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | 完成 | 587 | 以間隔壓縮方式強化化療，用於尤因氏肉瘤及相關腫瘤 |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | 完成 | 642 | 在標準五藥方案（含 doxorubicin）加上 VTC，用於非轉移性尤因氏肉瘤 |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | 完成 | 278 | 非轉移性尤因氏肉瘤的劑量強化與標準治療比較 |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | 進行中（不招募） | 312 | 化療加 ganitumab（IGF-1R 抗體）用於轉移性尤因氏肉瘤 |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | 未知 | 1200 | EURO-E.W.I.N.G.99，歐洲尤因氏腫瘤合作研究 |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | 完成 | 未提供 | 含 doxorubicin 的多藥化療後接手術及放療，用於周邊原始神經外胚層腫瘤／尤因氏肉瘤 |
| [NCT00003667](https://clinicaltrials.gov/study/NCT00003667) | Phase 2 | 完成 | 未提供 | VAC 加 dexrazoxane，併用或不併用 ImmTher，用於高風險尤因氏肉瘤 |
| [NCT00038142](https://clinicaltrials.gov/study/NCT00038142) | Phase 2 | 提前終止 | 46 | 同上方案的隨機試驗，因提前終止資訊有限 |
| [NCT00002643](https://clinicaltrials.gov/study/NCT00002643) | Phase 2 | 完成 | 130 | 診斷時已轉移之尤因氏腫瘤的強化治療併用生長因子支持 |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | 完成 | 24 | 脂質體 doxorubicin 加 temsirolimus，用於復發性軟組織及骨肉瘤（非尤因氏專屬） |

注意：多數試驗是多藥方案，doxorubicin 的單獨貢獻無法從中分離。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | 在標準化療加入 ifosfamide 與 etoposide，評估對新診斷尤因氏肉瘤／骨 PNET 存活的影響 |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT | Lancet | EE2012：比較歐美兩種標準化療方案的開放性 Phase 3 試驗 |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT | J Clin Oncol | 間隔壓縮化療加 ganitumab 用於新診斷轉移性尤因氏肉瘤 |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | 間隔壓縮化療用於局部性尤因氏肉瘤 |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT（試驗設計） | Trials | EURO EWING 2012 試驗方案 |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Review | Cancer | 國家尤因氏肉瘤腫瘤委員會的治療共識建議 |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | 尤因氏肉瘤現行處置與國際合作方向 |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | 引入化療後局部性病患存活率由約 10% 提升至約 75% |
| [25993235](https://pubmed.ncbi.nlm.nih.gov/25993235/) | 2015 | Review | ASCO Educ Book | 骨肉瘤與尤因氏肉瘤的全身性治療 |
| [37651654](https://pubmed.ncbi.nlm.nih.gov/37651654/) | 2023 | 長期追蹤 | J Clin Oncol | AEWS0031 間隔壓縮化療的長期結果 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52946 | DOXORUBICIN-TEVA INJ 2MG/ML | 注射劑 | 未登載 |
| HK-40874 | DOXORUBICIN-EBEWE INJ 10MG/5ML VIAL | 注射劑（小瓶） | 未登載 |
| HK-37493 | DOXORUBICIN-EBEWE INJ 50MG/25ML (VIAL) | 注射劑（小瓶） | 未登載 |
| HK-67505 | DOXORUBICIN HYDROCHLORIDE LIPOSOME CONCENTRATE FOR SOLUTION FOR INFUSION 20MG/10ML | 脂質體輸注濃縮液 | 未登載 |
| HK-66647 | CAELYX CONCENTRATE FOR SOLUTION FOR INFUSION 20MG/10ML | 脂質體輸注濃縮液 | 未登載 |

另有 HK-68965、HK-68964（DOXOCCORD LP，脂質體劑型）共 7 張有效單一成分許可證，全數有效、無已註銷。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（蒽環類，拓撲異構酶 II 抑制劑） |
| 骨髓抑制風險 | 高（知識圖譜標示與嗜中性白血球低下、白血球低下、血小板低下、貧血相關） |
| 致吐性分級 | 中至高（依藥物類別判斷，請以原廠仿單為準） |
| 監測項目 | CBC（含分類）、肝功能與膽紅素、心臟功能（左心室射血分率） |
| 處置防護 | 需依細胞毒性藥物處置規範操作 |

---

## 安全性考量

- **禁忌症（來自知識圖譜，非仿單文字）**：肝衰竭或肝病、血小板低下、嗜中性白血球低下、白血球低下、顆粒球缺乏症、貧血、心臟病、心肌病變、充血性心衰竭、心臟傳導疾病、猝發性心臟停止、高膽紅素血症、感染性疾病等。
- **藥物交互作用**：共查得 100 筆，以下為主要者：
  - **嚴重 (Major)**：Dolasetron、Cisapride、Papaverine
  - **中度 (Moderate)**：Aprepitant、Ondansetron、Granisetron、Palonosetron、Dexamethasone、Clarithromycin、Levofloxacin、Famotidine 等

香港仿單的警語與禁忌症資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 多項 Phase 3 隨機試驗與多篇 RCT 文獻均以含 doxorubicin 的多藥方案治療尤因氏肉瘤，臨床使用基礎充分，故證據等級為 L1。
- 這些證據多為多藥方案，無法單獨評估 doxorubicin 貢獻，且藥物具高度心臟與骨髓毒性，因此需附加防護措施。

**若要推進需要：**
- 補齊作用機轉資料（MOA）。
- 取得香港仿單的警語、禁忌症與核准適應症文字，確認尤因氏肉瘤是否在本地許可範圍。
- 制定心臟毒性（累積劑量、心功能監測，必要時考慮 dexrazoxane）與血液學監測計畫。
- 評估各劑型（傳統與脂質體）在尤因氏肉瘤的適用性。

**其他預測適應症補充（僅供參考）：**
- 橫紋肌肉瘤（rank 9）：證據等級 L1，但試驗多為混合軟組織肉瘤設計，建議 Proceed with Guardrails。
- 肺母細胞瘤（rank 4）：L3，建議列為研究問題。
- 原發性肺淋巴瘤（rank 3）：L4，建議列為研究問題。
- 其餘（肺胎兒型腺癌、BCR-ABL1 陽性慢性骨髓性白血病、單核球白血病、陰道葡萄狀胚胎型橫紋肌肉瘤、顱旁胚胎型橫紋肌肉瘤、神經節母細胞瘤）：僅有模型預測或個案報告，建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

