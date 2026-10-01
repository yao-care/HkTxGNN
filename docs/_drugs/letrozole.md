---
layout: default
title: Letrozole
parent: 高證據等級 (L1-L2)
nav_order: 512
evidence_level: L1
indication_count: 5
---

# Letrozole
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Letrozole：從芳香環酶抑制劑（原適應症資料缺漏）到女性乳癌

## 一句話總結

Letrozole 是非類固醇類芳香環酶抑制劑，Evidence Pack 未登載原適應症。
TxGNN 模型預測它可能對**女性乳癌 (Female Breast Carcinoma)** 有效，目前有 **50 個以上的臨床試驗登記**和 **20 篇文獻**支持，其中包含多個已完成的 Phase 3 試驗。
不過這屬於既有的標準治療用途，並非全新的老藥新用訊號。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 女性乳癌 (Female Breast Carcinoma) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 12 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉欄位資料。根據已知資訊，Letrozole 是非類固醇類芳香環酶抑制劑，能減少雌激素合成，使依賴雌激素生長的乳癌細胞失去生長訊號。

乳癌中的荷爾蒙受體陽性（HR+）亞型依賴雌激素驅動，因此阻斷雌激素生成在機轉上合理。Letrozole 既可單獨使用，也是 CDK4/6 抑制劑（palbociclib、ribociclib、abemaciclib）合併療法中的內分泌治療基礎藥物。

需要注意的是，「女性乳癌」是較廣的上層疾病名稱，預期獲益主要集中在荷爾蒙受體陽性族群。在雌激素受體陰性乳癌中，預期獲益有限。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00004205](https://clinicaltrials.gov/study/NCT00004205) | Phase 3 | 完成 | 8028 | 比較 letrozole 與 tamoxifen 作為停經後 ER/PgR 陽性乳癌的輔助內分泌治療 |
| [NCT00073528](https://clinicaltrials.gov/study/NCT00073528) | Phase 3 | 完成 | 1286 | 雙盲安慰劑對照，lapatinib + letrozole 對比 letrozole，用於 HR+ 晚期或轉移性乳癌 |
| [NCT00330317](https://clinicaltrials.gov/study/NCT00330317) | Phase 3 | 完成 | 300 | 停經後 HR+ 原發性乳癌的術前 letrozole 治療，評估腫瘤縮小以利保乳手術 |
| [NCT00963729](https://clinicaltrials.gov/study/NCT00963729) | Phase 3 | 完成 | 756 | 停經後原發性乳癌，比較術前化療與 letrozole 內分泌治療 |
| [NCT03969121](https://clinicaltrials.gov/study/NCT03969121) | Phase 3 | 完成 | 141 | 術前荷爾蒙治療加 palbociclib 對比加安慰劑，用於 HR+/HER2- 乳癌（letrozole 的角色未於摘要中確認） |
| [NCT00107016](https://clinicaltrials.gov/study/NCT00107016) | Phase 2 | 完成 | 267 | 隨機、安慰劑對照，術前 letrozole 加 everolimus 用於停經後 ER+ 原發性乳癌 |
| [NCT04571437](https://clinicaltrials.gov/study/NCT04571437) | Phase 2 | 未知 | 204 | ER+/HER2- 晚期乳癌一線治療，letrozole 加或不加低劑量持續性 capecitabine |
| [NCT00908531](https://clinicaltrials.gov/study/NCT00908531) | Phase 3 | 提前終止 | 123 | 停經後可手術 HR+ 腫瘤，比較 4 個月 letrozole 術前治療與先手術 |
| [NCT05439499](https://clinicaltrials.gov/study/NCT05439499) | Phase 3 | 未知 | 434 | 雙盲安慰劑對照，FCN-437c 加 letrozole 或 anastrozole，用於 HR+/HER2- 晚期乳癌 |
| [NCT02400567](https://clinicaltrials.gov/study/NCT02400567) | Phase 2 | 完成 | 125 | 術前 letrozole + palbociclib 對比 FEC-docetaxel 化療，用於 Luminal 乳癌 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32683565](https://pubmed.ncbi.nlm.nih.gov/32683565/) | 2020 | RCT | Breast Cancer Res Treat | PALOMA-1 整體存活結果：palbociclib + letrozole 對比 letrozole 單用，一線 ER+/HER2- 晚期乳癌，無惡化存活期明顯延長（HR 0.488） |
| [31838010](https://pubmed.ncbi.nlm.nih.gov/31838010/) | 2020 | RCT | Lancet Oncol | CORALLEEN：ribociclib + letrozole 對比化療，用於停經後 Luminal B 早期乳癌的術前治療 |
| [16382061](https://pubmed.ncbi.nlm.nih.gov/16382061/) | 2005 | 臨床試驗（分類待確認） | N Engl J Med | 比較 letrozole 與 tamoxifen 作為停經後荷爾蒙受體陽性早期乳癌的輔助治療 |
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | 世代研究 | Comput Math Methods Med | 探討 tamoxifen 與 letrozole 序貫治療對比 letrozole 單用的療效、安全性與預後 |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sci | Letrozole 的藥理、毒性與潛在治療效果，涵蓋輔助、術前與轉移性 HR+ 乳癌 |
| [19445563](https://pubmed.ncbi.nlm.nih.gov/19445563/) | 2009 | Review | Expert Opin Pharmacother | 比較 anastrozole、letrozole、exemestane 用於早期乳癌，三者皆優於 tamoxifen |
| [18829517](https://pubmed.ncbi.nlm.nih.gov/18829517/) | 2008 | 臨床研究 | Clin Cancer Res | Letrozole 抑制乳癌組織與血漿雌激素的效果優於 anastrozole |
| [16500235](https://pubmed.ncbi.nlm.nih.gov/16500235/) | 2006 | Review | Breast | Letrozole 的研發歷程及其在晚期乳癌與術前治療的應用 |
| [17696797](https://pubmed.ncbi.nlm.nih.gov/17696797/) | 2007 | Review | Expert Opin Pharmacother | 第三代芳香環酶抑制劑改變乳癌荷爾蒙治療觀念，討論 letrozole 的現況與未來角色 |
| [20095792](https://pubmed.ncbi.nlm.nih.gov/20095792/) | 2010 | Review | Expert Opin Drug Metab Toxicol | 第三代芳香環酶抑制劑 letrozole 的藥效學、藥動學、臨床療效與安全性 |

---

## 香港上市資訊

許可證資料中未提供劑型與核准適應症內容。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68544 | LOTUSENZA TABLETS 2.5MG | LOTUS PHARMACEUTICAL HK LIMITED |
| HK-64679 | ACCORD LETROZOLE TABLETS 2.5MG | JACOBSON MARKETING LIMITED |
| HK-68767 | LETROZOLE TABLETS 2.5MG | NATURAL HEALTH RESOURCES COMPANY LIMITED |
| HK-65626 | LETROZOLE SANDOZ TABLETS 2.5MG | SANDOZ HONG KONG LIMITED |
| HK-58595 | LETROZOL FARMOZ TAB 2.5MG | TRENTON-BOMA LTD |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 內分泌治療（芳香環酶抑制劑），非傳統細胞毒性藥物 |

其他細胞毒性相關資料（骨髓抑制風險、監測項目、處置防護）：請參考原廠仿單的警語與注意事項。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
多個已完成的 Phase 3 隨機試驗（如 NCT00004205、NCT00073528、NCT00330317）和大量文獻，支持 letrozole 用於荷爾蒙受體陽性乳癌。這是既有的標準治療用途，證據等級 L1。「女性乳癌」是較廣的疾病名稱，且香港的核准適應症與安全性仿單資料尚未取得，因此需附帶限制條件推進。

**若要推進需要：**
- 取得香港衛生署仿單，確認警語、禁忌症與核准適應症（此為阻斷性缺口 DG001）
- 從 DrugBank 補齊作用機轉資料（DG002）
- 將適用範圍明確限定於荷爾蒙受體陽性（HR+）族群
- 確認各許可證的核准適應症是否已涵蓋乳癌

**同批預測的其他適應症（供參考）：**
- 雌激素受體陽性乳癌：同樣是 L1，屬標準治療，Proceed with Guardrails
- 雌激素受體陰性乳癌：證據等級 L4，機轉上預期獲益有限，Hold
- 乳頭癌：僅有間接證據，證據等級 L4，列為研究問題
- Ehrlich 腫瘤癌：僅有小鼠模型的前臨床研究，證據等級 L5，Hold

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

