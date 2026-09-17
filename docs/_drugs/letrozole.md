---
layout: default
title: Letrozole
parent: 僅模型預測 (L5)
nav_order: 447
evidence_level: L5
indication_count: 5
---

# Letrozole
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

# Letrozole：原適應症資料缺失，預測與女性乳癌（Female Breast Carcinoma）高度相關

## 一句話總結

Letrozole（DrugBank ID: DB01006）目前香港未上市、無許可證登記，且原始適應症與作用機轉資料均缺失。TxGNN 模型預測它與**女性乳癌 (Female Breast Carcinoma)** 高度相關（預測分數 99.98%），目前有 **50+ 個臨床試驗**（含多個大型 Phase 3 RCT）和 **20 篇文獻**支持——但值得注意的是，多筆試驗摘要本身已顯示 letrozole 是芳香酶抑制劑，早已用於荷爾蒙敏感型乳癌治療，此預測較接近「證實既有用途」而非全新機轉發現。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料庫未收錄（`original_indications` 為空、香港無許可證記錄） |
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.98%（rank 817） |
| 證據等級 | L1（≥2 個已完成的 Phase 3 RCT，含 n=8,028 大型試驗） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉（MOA）資料庫記錄。但根據所收集臨床試驗的摘要文字，letrozole 被多筆試驗描述為「芳香酶抑制劑 (aromatase inhibitor)」，用於降低體內雌激素生成，適用於荷爾蒙敏感型（ER/PR 陽性）乳癌患者（例如 NCT03901170、NCT02095184 的摘要說明）。

由於原始核准適應症資料在本證據包中同樣缺失（`original_indications` 為空），無法比較「原適應症」與「新適應症」之間的機轉延伸關係。不過從證據強度來看，letrozole 在乳癌治療上已有極大量且長期累積的 Phase 3 隨機對照試驗證據（如 n=8,028 的大型輔助治療試驗、NEJM 發表的 letrozole vs tamoxifen 比較研究），顯示此預測更可能反映 letrozole 作為乳癌標準治療藥物的既定角色，而非探索性的老藥新用假說。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00004205](https://clinicaltrials.gov/study/NCT00004205) | Phase 3 | 完成 | 8028 | Letrozole 作為輔助內分泌治療用於停經後 ER/PgR 陽性乳癌，比較 letrozole 與 tamoxifen 療效 |
| [NCT00073528](https://clinicaltrials.gov/study/NCT00073528) | Phase 3 | 完成 | 1286 | Lapatinib+letrozole vs letrozole 用於 ER/PR 陽性晚期或轉移性乳癌 |
| [NCT00330317](https://clinicaltrials.gov/study/NCT00330317) | Phase 3 | 完成 | 300 | 新輔助 letrozole 治療用於腫瘤縮小以利保乳手術 |
| [NCT03969121](https://clinicaltrials.gov/study/NCT03969121) | Phase 3 | 完成 | 141 | 新輔助荷爾蒙治療 + palbociclib vs 安慰劑，用於可手術之 HR+/HER2- 乳癌 |
| [NCT00908531](https://clinicaltrials.gov/study/NCT00908531) | Phase 3 | 終止 | 123 | 比較 letrozole 內分泌治療優先 vs 手術優先，用於可手術荷爾蒙受體陽性腫瘤 |
| [NCT05439499](https://clinicaltrials.gov/study/NCT05439499) | Phase 3 | 未知 | 434 | FCN-437c 併用 letrozole/anastrozole ± goserelin vs 安慰劑，用於 HR+/HER2- 晚期乳癌 |
| [NCT04095364](https://clinicaltrials.gov/study/NCT04095364) | Phase 3 | 進行中 | 450 | Paclitaxel/carboplatin/letrozole 維持治療 vs letrozole 單藥，用於低惡性度漿液性卵巢/腹膜癌 |
| [NCT03820830](https://clinicaltrials.gov/study/NCT03820830) | Phase 3 | 進行中 | 405 | 輔助 palbociclib+內分泌治療 vs 內分泌治療單獨，用於局部區域復發乳癌 |
| [NCT06223698](https://clinicaltrials.gov/study/NCT06223698) | Phase 3 | 尚未招募 | 3832 | 延長輔助內分泌治療策略比較（tamoxifen 續用 vs 轉換為芳香酶抑制劑） |
| [NCT04571437](https://clinicaltrials.gov/study/NCT04571437) | Phase 2 | 未知 | 204 | Letrozole ± metronomic capecitabine 一線治療 ER+/HER2- 晚期乳癌 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16382061](https://pubmed.ncbi.nlm.nih.gov/16382061/) | 2005 | RCT | NEJM | Letrozole 對比 tamoxifen 用於停經後早期乳癌之輔助治療比較 |
| [32683565](https://pubmed.ncbi.nlm.nih.gov/32683565/) | 2020 | RCT | Breast Cancer Res Treat | PALOMA-1 總存活率結果：palbociclib+letrozole vs letrozole 單藥 |
| [31838010](https://pubmed.ncbi.nlm.nih.gov/31838010/) | 2020 | RCT | Lancet Oncology | CORALLEEN 試驗：新輔助 ribociclib+letrozole vs 化療，用於 Luminal B 乳癌 |
| [18829517](https://pubmed.ncbi.nlm.nih.gov/18829517/) | 2008 | 比較研究 | Clin Cancer Res | Letrozole 抑制乳癌組織與血漿雌激素濃度優於 anastrozole |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opin Drug Metab Toxicol | Letrozole 藥效學、藥動學及臨床療效與安全性回顧 |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sciences | Letrozole 藥理學、毒性與潛在治療效果總論 |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Review | Expert Opin Pharmacother | Anastrozole、letrozole、exemestane 於早期乳癌治療之比較回顧 |
| [16500235](https://pubmed.ncbi.nlm.nih.gov/16500235/) | 2006 | Review | Breast (Edinburgh) | Letrozole 於晚期乳癌及新輔助治療之發展回顧 |
| [17696797](https://pubmed.ncbi.nlm.nih.gov/17696797/) | 2007 | Review | Expert Opin Pharmacother | Letrozole 於乳癌治療的現況與未來角色 |
| [35378469](https://pubmed.ncbi.nlm.nih.gov/35378469/) | 2022 | 世代研究 | Curr Probl Cancer | Palbociclib+letrozole 用於荷爾蒙受體陽性晚期乳癌之預測反應與預後因子 |

---

## 香港上市資訊

目前無許可證登記（未上市；`total_licenses = 0`）。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶/內分泌治療（芳香酶抑制劑，非傳統細胞毒性化療藥物）——依多筆臨床試驗摘要描述所判斷 |
| 骨髓抑制風險 | 缺乏毒性資料，請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 缺乏毒性資料，請參考原廠仿單的警語與注意事項 |
| 監測項目 | 缺乏毒性資料，請參考原廠仿單的警語與注意事項 |
| 處置防護 | 缺乏毒性資料，請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。（`key_warnings`、`contraindications`、DDI 查詢均無資料，且 TFDA/仿單警語缺失已被標記為 Blocking 資料缺口 DG001。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然臨床試驗與文獻證據等級達 L1（多個已完成 Phase 3 RCT，含大型 n=8,028 試驗），但「TFDA 仿單警語/禁忌」資料缺口被明確標記為 **Blocking**，依規範無法進入 S1 安全性初評。
- 藥物在香港無許可證、無上市紀錄，且原始適應症與 MOA 資料均缺失，難以評估此預測相對於既有用途的「新穎性」。

**若要推進需要：**
- 取得 letrozole 完整仿單（警語、禁忌症、DDI）以解除 DG001 阻斷項
- 補齊 DrugBank MOA 與藥物分類資料（DG002），釐清此預測是否代表真正新適應症或僅為既有用途確認
- 確認香港藥物註冊狀態與潛在上市路徑
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

