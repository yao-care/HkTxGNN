---
layout: default
title: Pimecrolimus
parent: 高證據等級 (L1-L2)
nav_order: 585
evidence_level: L2
indication_count: 4
---

# Pimecrolimus
{: .fs-9 }

證據等級: **L2** | 預測適應症: **4** 個
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

# Pimecrolimus：從異位性皮膚炎到脂漏性皮膚炎

## 一句話總結

Pimecrolimus（DB00337）是外用 calcineurin 抑制劑，目前臨床上已用於異位性皮膚炎的治療。
TxGNN 模型預測它可能對**脂漏性皮膚炎 (Seborrheic Dermatitis)** 有效，
目前有 **1 個直接針對此適應症的臨床試驗**、外加同一機轉延伸的多項比較試驗，以及 **18 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 異位性皮膚炎（依臨床試驗資料庫記載為 Elidel® 已核准適應症；本地無許可證資料佐證） |
| 預測新適應症 | 脂漏性皮膚炎 (Seborrheic Dermatitis) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Pimecrolimus 是 ascomycin 衍生的非類固醇 calcineurin 抑制劑，選擇性作用於 T 細胞與肥大細胞：抑制 T 細胞增生，減少 IL-2、IL-4、interferon-gamma、TNF-α 等發炎細胞激素的產生與釋放，同時抑制肥大細胞去顆粒化。此機轉正是它被用於異位性皮膚炎的核心理由（文獻 PMID 16033622）。

脂漏性皮膚炎的病理牽涉 *Malassezia* 誘發的局部 T 細胞/發炎反應，與異位性皮膚炎的免疫路徑有重疊。calcineurin 抑制可壓制這條發炎級聯，因此機轉外推具有合理性——這不只是圖譜關聯，而是有藥理基礎支持的推論。

更重要的是，這個方向已有多個獨立 RCT 佐證，包括與 sertaconazole 之頭對頭比較試驗，以及至少 2 篇針對 RCT 的系統性回顧，顯示 pimecrolimus 1% cream 在脂漏性皮膚炎的療效與耐受性與現行療法（皮質類固醇、抗黴菌劑）相當，證據強度已超越單純模型預測。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00403559](https://clinicaltrials.gov/study/NCT00403559) | Phase 2 | 完成 | 113 | 4 週雙盲、主動對照試驗，探索 Elidel（pimecrolimus）用於脂漏性皮膚炎之療效 |

> 註：此為直接以「seborrheic dermatitis」為目標登記的試驗；文獻中另有多項與 ketoconazole、sertaconazole 之頭對頭比較試驗未在 ClinicalTrials.gov 單獨登記為此適應症，詳見下方文獻證據。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23715821](https://pubmed.ncbi.nlm.nih.gov/23715821/) | 2013 | RCT（對照 sertaconazole） | Irish J Med Sci | Sertaconazole 2% 與 pimecrolimus 1% 治療脂漏性皮膚炎之療效比較 |
| [34910320](https://pubmed.ncbi.nlm.nih.gov/34910320/) | 2022 | RCT（對照 sertaconazole） | Clin Exp Dermatol | 隨機盲性試驗，pimecrolimus 1% vs sertaconazole 2% 治療顏面脂漏性皮膚炎，療效與安全性相當 |
| [22142161](https://pubmed.ncbi.nlm.nih.gov/22142161/) | 2012 | 系統性回顧（RCT） | Expert Rev Clin Pharmacol | Pimecrolimus 1% cream 為耐受性良好且有效的脂漏性皮膚炎治療選項，療效與皮質類固醇/抗黴菌劑相當 |
| [36072203](https://pubmed.ncbi.nlm.nih.gov/36072203/) | 2022 | 系統性回顧（RCT） | Cureus | 針對顏面脂漏性皮膚炎，回顧 calcineurin 抑制劑等四類藥物之療效與安全性 |
| [18677657](https://pubmed.ncbi.nlm.nih.gov/18677657/) | 2009 | RCT（對照 ketoconazole） | J Dermatolog Treat | 開放性隨機比較研究：pimecrolimus 1% cream 與 ketoconazole 2% cream 治療脂漏性皮膚炎 |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | 系統性回顧 | Am J Clin Dermatol | 顏面脂漏性皮膚炎外用治療系統性回顧，涵蓋抗黴菌、角質溶解、皮質類固醇三大類藥物 |
| [20000875](https://pubmed.ncbi.nlm.nih.gov/20000875/) | 2010 | 開放性研究 | Am J Clin Dermatol | Pimecrolimus 1% cream 對難治型顏面脂漏性皮膚炎為有效且耐受性良好之治療 |
| [16033622](https://pubmed.ncbi.nlm.nih.gov/16033622/) | 2005 | Review | Int J Clin Pract | 說明 pimecrolimus 之 T 細胞/肥大細胞作用機轉，並回顧其於異位性皮膚炎以外之應用 |
| [23441238](https://pubmed.ncbi.nlm.nih.gov/23441238/) | 2013 | Review | J Clin Aesthet Dermatol | Pimecrolimus 為長期使用之安全替代方案，可避免外用皮質類固醇長期副作用 |
| [15700745](https://pubmed.ncbi.nlm.nih.gov/15700745/) | 2004 | 臨床研究 | Drugs Exp Clin Res | Pimecrolimus 1% cream 用於顏面及軀幹脂漏性皮膚炎之療效、耐受性與安全性評估 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
已有多個獨立 RCT（含與 sertaconazole、ketoconazole 之頭對頭比較）及至少 2 篇系統性回顧支持 pimecrolimus 用於脂漏性皮膚炎，機轉外推合理，證據等級達 L2；但本地（香港）尚未上市、無許可證與仿單資料，安全性初評無法完成。

**若要推進需要：**
- 補齊仿單警語與禁忌資料（Blocking：目前無法進入 S1 安全性初評）
- 補齊完整作用機轉（MOA）正式來源資料，取代目前僅能引用文獻推論
- 評估本地（香港）上市/許可證申請可行性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

