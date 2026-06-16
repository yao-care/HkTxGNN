---
layout: default
title: Entrectinib
parent: 中證據等級 (L3-L4)
nav_order: 272
evidence_level: L4
indication_count: 10
---

# Entrectinib
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Entrectinib：從 NTRK/ROS1/ALK 融合陽性實體瘤到多發性內分泌腫瘤

## 一句話總結

Entrectinib 是獲 FDA 核准的選擇性酪胺酸激酶抑制劑，靶向 NTRK1/2/3、ROS1 及 ALK 融合陽性實體瘤。
TxGNN 模型預測它可能對**多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)** 有效，
目前有 **2 個臨床試驗**和 **1 篇文獻**支持，但關聯性有限，疑似系統誤分類。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | NTRK/ROS1/ALK 融合陽性實體瘤（FDA 核准，香港未登記） |
| 預測新適應症 | 多發性內分泌腫瘤 (Multiple Endocrine Neoplasia) |
| TxGNN 預測分數 | 98.58% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question |

---

## 為什麼這個預測合理？

目前缺乏正式的作用機轉文件（MOA 為 Data Gap）。根據本證據包中的臨床試驗與文獻資料，Entrectinib 是針對神經營養酪胺酸激酶受體（NTRK1、NTRK2、NTRK3）、ROS1 及 ALK 的口服選擇性小分子抑制劑，透過競爭性占據 ATP 結合口袋，阻斷融合蛋白的持續活化訊號，進而抑制腫瘤細胞增生與轉移。

多發性內分泌腫瘤（MEN）在機轉上以 **RET 原癌基因突變**為主要驅動力，尤其是 MEN2A 和 MEN2B。Entrectinib 的主要靶點（NTRK/ROS1/ALK）與 RET 屬於不同激酶家族。雖然部分廣譜 TKI 對 RET 具有微弱的脫靶活性，但 RET 並非 Entrectinib 的設計靶點，專一性 RET 抑制劑為 selpercatinib 與 pralsetinib。

系統評估顯示，本次查詢返回的 2 項臨床試驗（ROSALINE 乳癌試驗、SMMART 籃型試驗）均非針對 MEN 設計，極可能是資料庫標籤誤分類。唯一相關文獻（PMID 38438731）探討的是 selpercatinib 在 RET 驅動癌症中的抗藥機轉，為間接機轉研究，並非 Entrectinib 直接用於 MEN 的療效證據。

---

## 臨床試驗證據

> ⚠️ **注意：以下試驗均非針對多發性內分泌腫瘤設計，疑為資料庫誤分類，請勿直接引用為 MEN 適應症的支持證據。**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04551495](https://clinicaltrials.gov/study/NCT04551495) | Phase 2 | 停止新入組 | 65 | ROSALINE 試驗：Entrectinib 聯合內分泌治療針對 ROS1 陽性浸潤性小葉乳癌（ILC），非 MEN 設計；與乳癌適應症高度相關 |
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | 已終止 | 2 | SMMART PRIME 籃型試驗，已提早終止，僅招募 2 名受試者，無統計意義數據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | 機轉/轉譯研究 | NPJ Precision Oncology | 探討甲狀腺髓樣癌患者接受 selpercatinib 治療後的 RET 脫靶抗藥機轉，提示 RET 通路具可介入性，但無 Entrectinib 直接療效數據 |

---

## 香港上市資訊

Entrectinib 目前在香港**尚未上市**，無任何藥品許可證登記。如需取得本藥，須透過特別審批途徑（如未經註冊藥物申請）。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（TRK/ROS1/ALK 選擇性酪胺酸激酶抑制劑，非傳統細胞毒性化療） |
| 骨髓抑制風險 | 中度（臨床試驗中可見貧血、嗜中性白血球減少、血小板減少） |
| 致吐性分級 | 低至中度（口服 TKI 典型致吐等級） |
| 監測項目 | CBC（含分類計數）、肝功能（ALT/AST）、QTc 間期、體重、中樞神經系統症狀評估 |
| 處置防護 | 請參考原廠仿單的警語與注意事項；一般口服抗癌藥物防護原則適用 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 注意：第 3、5 號預測適應症的證據評估發現，**血小板減少症**與**肺動脈高壓**（PTTM 相關）均出現於 Entrectinib 治療的**不良反應報告**中（PMID 41002576），而非治療目標，使用時應列為安全性監測訊號。

---

## 結論與下一步

**決策：Research Question**

**理由：**
TxGNN 預測分數達 98.58%，但機轉支持薄弱——MEN 的主要驅動基因為 RET，而非 Entrectinib 的核心靶點 NTRK/ROS1/ALK。列出的 2 項臨床試驗均非針對 MEN 設計，疑似資料庫誤分類；唯一文獻亦屬間接機轉研究。在任何前臨床數據出現前，此預測不具推進臨床的基礎。

**若要推進需要：**
- 確認 Entrectinib 對 RET 突變型（MEN2A/2B 相關 RET 突變）的 IC₅₀ 數據，評估脫靶抑制是否具臨床意義
- 在 MEN 相關細胞株（如 MTC TT 細胞）或小鼠模型進行前臨床活性測試
- 排除資料庫誤分類：確認 NCT04551495 及 NCT03878524 是否確有 MEN 患者入組亞組

---

## ⚡ 補充：本次預測中更具潛力的候選適應症

在本次 10 項 TxGNN 預測中，以下適應症具有明顯更強的臨床證據，建議優先評估：

| 排名 | 適應症 | 預測分數 | 證據等級 | 建議決策 | 關鍵亮點 |
|------|--------|---------|---------|---------|---------|
| **#8** | **女性乳癌 (Female Breast Carcinoma)** | **97.76%** | **L2** | **Proceed with Guardrails** | Entrectinib 已獲 FDA 核准用於 NTRK fusion 陽性實體瘤（含乳癌亞型）；STARTRK-2（NCT02568267，534 名受試者）為核心樞軸試驗；ROSALINE 試驗（NCT04551495）專門針對 ROS1 陽性 ILC；ETV6-NTRK3 融合基因出現於 ~90% 的乳腺分泌型癌 |

> **女性乳癌適應症守護條件**：必須以 NGS 或 FISH 確認 NTRK1/2/3、ROS1 或 ALK 融合基因陽性，不建議用於未篩選族群。香港未上市為地區核准問題，非療效缺乏，可透過未經註冊藥物途徑申請。

> ⚠️ 以下預測疑為「反向關聯」（不良反應誤判為治療目標），建議作為**安全性監測訊號**而非再利用候選：血小板減少症（#3, #6, #7, #9）、肺動脈高壓（#5）。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

