---
layout: default
title: Zanubrutinib
parent: 僅模型預測 (L5)
nav_order: 934
evidence_level: L5
indication_count: 5
---

# Zanubrutinib
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

# Zanubrutinib：從 B 細胞惡性腫瘤到骨髓性白血病

## 一句話總結

Zanubrutinib 是 BTK 抑制劑，香港已上市（品名 BRUKINSA），文獻中的臨床使用集中在 B 細胞惡性腫瘤（CLL/SLL、華氏巨球蛋白血症）。
TxGNN 模型預測它可能對**骨髓性白血病 (Myeloid Leukemia)** 有效，但目前**沒有任何以 zanubrutinib 治療骨髓性白血病的臨床試驗或文獻**。
所列的 2 個臨床試驗和 8 篇文獻都屬間接參考。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症；文獻顯示臨床使用為 CLL/SLL、華氏巨球蛋白血症等 B 細胞惡性腫瘤 |
| 預測新適應症 | 骨髓性白血病 (Myeloid Leukemia) |
| TxGNN 預測分數 | 99.65% |
| 證據等級 | L5（Evidence Pack 標示 L4，但供應資料中沒有骨髓性白血病的前臨床或臨床研究，故保守判定） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空）。依一般藥學知識，zanubrutinib 是共價結合的 BTK 抑制劑，對 BTK 的選擇性高於 ibrutinib 和 acalabrutinib。

有報告指出 BTK 在部分骨髓譜系細胞與 AML 母細胞中有表現，其他 BTK 抑制劑的前臨床研究也暗示它可能參與訊號傳遞。這只是假說，並非本次提供資料所證實。

**需要特別留意：** 0.996 的分數是知識圖譜模型的預測，不是臨床證據。所有 zanubrutinib 的臨床資料都來自淋巴系惡性腫瘤（CLL/SLL、WM），不是骨髓性白血病。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04477291](https://clinicaltrials.gov/study/NCT04477291) | Phase 1 | 已終止 | 45 | 測試 CG-806 (luxeptinib，另一種多激酶抑制劑) 用於復發/難治性 AML 或高風險 MDS；未測試 zanubrutinib |
| [NCT05665530](https://clinicaltrials.gov/study/NCT05665530) | Phase 1 | 完成 | 86 | 測試 CDK9 抑制劑 PRT2527 單用或併用 zanubrutinib/venetoclax，用於復發/難治性血液惡性腫瘤；zanubrutinib 只是併用藥物，未證實對骨髓性白血病有效 |

這兩個試驗與預測的相關性都低（C 級）。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39647999](https://pubmed.ncbi.nlm.nih.gov/39647999/) | 2025 | RCT | J Clin Oncol | SEQUOIA 三期試驗 5 年追蹤：zanubrutinib 對比 BR 用於初治 CLL/SLL |
| [40334067](https://pubmed.ncbi.nlm.nih.gov/40334067/) | 2025 | Cohort | Blood Adv | 對 ibrutinib/acalabrutinib 不耐受的 CLL/SLL 患者，zanubrutinib 耐受性佳且有效 |
| [40829104](https://pubmed.ncbi.nlm.nih.gov/40829104/) | 2026 | 合併分析 | Blood Adv | 跨試驗分析 del(17p)/TP53 突變 CLL/SLL 的療效與安全性 |
| [36400069](https://pubmed.ncbi.nlm.nih.gov/36400069/) | 2023 | Phase 2 單臂試驗 | Lancet Haematol | 對先前 BTK 抑制劑不耐受的 B 細胞惡性腫瘤，評估 zanubrutinib 的安全性與活性 |
| [36402930](https://pubmed.ncbi.nlm.nih.gov/36402930/) | 2023 | Review | Leukemia | BTK 抑制劑用於華氏巨球蛋白血症的治療管理 |
| [34959482](https://pubmed.ncbi.nlm.nih.gov/34959482/) | 2021 | Review | Pharmaceutics | 慢性白血病（CML、CLL）的 TKI 治療回顧 |
| [37150651](https://pubmed.ncbi.nlm.nih.gov/37150651/) | 2023 | Review | Clin Lymphoma Myeloma Leuk | BTK 抑制劑（含 zanubrutinib）相關 B 型肝炎病毒再活化 |
| [36325357](https://pubmed.ncbi.nlm.nih.gov/36325357/) | 2022 | Case report | Front Immunol | 華氏巨球蛋白血症合併 B-ALL 的罕見病例 |

以上文獻都不是針對骨髓性白血病，只支持 zanubrutinib 在淋巴系惡性腫瘤的療效與安全性。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67529 | BRUKINSA CAPSULES 80MG（廠商：BeOne Medicines (Hong Kong) Co., Limited） | 未載明 | 未載明 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（BTK 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單；文獻提示需留意 B 型肝炎病毒再活化（PMID 37150651） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 這項預測只有模型分數支持，沒有任何以 zanubrutinib 治療骨髓性白血病的研究。
- 現有臨床資料都來自淋巴系惡性腫瘤，機轉連結也只是假說。

**若要推進需要：**
- 取得 DrugBank 的作用機轉資料，釐清 BTK 在骨髓性白血病的生物學角色。
- 補做 zanubrutinib 在 AML 細胞株或初代檢體的前臨床研究。
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症。
- 檢索是否已有以 zanubrutinib 單用或併用治療骨髓性白血病的臨床試驗。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

