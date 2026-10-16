---
layout: default
title: Cetuximab
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Cetuximab：預測新適應症為軟骨樣錯構瘤 (Chondroid Hamartoma)（證據等級 L5）。原適應症：大腸直腸癌、頭頸部鱗狀細胞癌"
monitor_inn: "Cetuximab"
predicted_indications: ["chondroid hamartoma", "non-seminomatous lesion", "bronchial adenomas/carcinoids childhood", "ductal or ductular proliferation", "tumor of testis and paratestis", "odontogenic cyst", "thyroglossal duct cyst", "cystic neoplasm", "epiglottis neoplasm", "pre-malignant neoplasm"]
---

# Cetuximab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Cetuximab：從大腸直腸癌與頭頸部鱗狀細胞癌到囊性腫瘤（Cystic Neoplasm）

## 一句話總結

Cetuximab 是一種抗 EGFR 的單株抗體，原本用於大腸直腸癌與頭頸部鱗狀細胞癌。
TxGNN 模型預測分數最高的是軟骨樣錯構瘤 (chondroid hamartoma)，但該項目完全沒有證據支持。
在所有預測中，證據相對較多的是**囊性腫瘤 (Cystic Neoplasm)**，目前有 **4 個臨床試驗**和 **20 篇文獻**，其中僅 1 項 Phase 1/2 試驗直接相關，整體證據仍屬初步。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 大腸直腸癌、頭頸部鱗狀細胞癌（許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 軟骨樣錯構瘤 (Chondroid Hamartoma)（排名第 1）；本報告另評析證據較多的囊性腫瘤 (Cystic Neoplasm)（排名第 8） |
| TxGNN 預測分數 | 99.95%（軟骨樣錯構瘤）；99.95%（囊性腫瘤） |
| 證據等級 | 軟骨樣錯構瘤 L5；囊性腫瘤 L2（依資料系統評定，但實際僅為 Phase 1/2 試驗，不符合本報告 L2 的 Phase 2/3 RCT 標準，保守視為 L3–L4） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold（排名第 1 的預測）；囊性腫瘤列為研究問題，宜以 Hold 處理 |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cetuximab 是針對表皮生長因子受體 (EGFR) 的抗體，已證實可用於 EGFR 表現的轉移性大腸直腸癌，以及合併放射線治療的頭頸部鱗狀細胞癌。

排名第 1 的軟骨樣錯構瘤是良性病變，沒有任何臨床試驗或文獻，也找不到 EGFR 依賴機轉的依據，這個高分僅是模型預測，不宜解讀為有療效。

相對而言，囊性腫瘤的線索較具體：相關證據多來自腺樣囊性癌與唾液腺癌，這類腫瘤有 EGFR 過度表現，構成使用 EGFR 抗體的理由。不過唾液腺癌的 Phase II 研究（PMID 18804410）結果細節在現有資料中無法確認，歷史上此類腫瘤對 cetuximab 的反應也有限。此外，「囊性腫瘤」是廣義標籤，與腺樣囊性癌的對應關係為間接。

---

## 臨床試驗證據

以下為囊性腫瘤（排名第 8）的相關試驗；排名第 1 的軟骨樣錯構瘤無任何試驗。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01192087](https://clinicaltrials.gov/study/NCT01192087) | Phase 1/2 | 未知 | 49 | Cetuximab 合併 IMRT 與碳離子加強照射，用於腺樣囊性癌（直接相關），評估毒性與療效 |
| [NCT00397384](https://clinicaltrials.gov/study/NCT00397384) | Phase 1 | 完成 | 43 | Erlotinib 加 cetuximab 用於晚期消化道、頭頸部、肺與大腸直腸癌；與囊性腫瘤為間接關聯 |
| [NCT00101348](https://clinicaltrials.gov/study/NCT00101348) | Phase 1/2 | 完成 | 66 | Erlotinib、cetuximab 加或不加 bevacizumab 用於多種轉移性實體瘤；間接關聯 |
| [NCT01637194](https://clinicaltrials.gov/study/NCT01637194) | Phase 1 | 完成 | 12 | Cetuximab 加 everolimus 用於實體瘤的安全性研究；專一性有限 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18804410](https://pubmed.ncbi.nlm.nih.gov/18804410/) | 2009 | Phase II trial | Oral Oncology | Cetuximab 用於復發或轉移性唾液腺癌（30 例，其中 23 例為腺樣囊性癌），以臨床獲益率為指標 |
| [21234529](https://pubmed.ncbi.nlm.nih.gov/21234529/) | 2011 | Cohort | Strahlenther Onkol | 復發頭頸癌以 IMRT 再照射合併 cetuximab（無法使用鉑類者） |
| [30141310](https://pubmed.ncbi.nlm.nih.gov/30141310/) | 2018 | Cohort | Asian Pac J Cancer Prev | 轉移性大腸直腸癌使用 cetuximab 時，皮膚反應與原發部位為預後因子 |
| [39415301](https://pubmed.ncbi.nlm.nih.gov/39415301/) | 2024 | Case report | J Med Case Rep | 以劑量遞增法成功給予 cetuximab，處理嚴重輸注反應 |
| [32518035](https://pubmed.ncbi.nlm.nih.gov/32518035/) | 2020 | Case report | Oral Oncology | Cetuximab 單藥用於復發高惡性度黏液表皮樣癌 |
| [22246397](https://pubmed.ncbi.nlm.nih.gov/22246397/) | 2012 | 前臨床 | Oncol Rep | Cetuximab 抑制無 KRAS 突變的黏液性卵巢癌細胞生長 |
| [33939281](https://pubmed.ncbi.nlm.nih.gov/33939281/) | 2021 | 回溯比較 | Cancer Med | 轉移性大腸癌黏液性腺癌：bevacizumab 與 cetuximab 搭配化療的比較 |
| [21134823](https://pubmed.ncbi.nlm.nih.gov/21134823/) | 2010 | Review | Bull Cancer | 頭頸癌的分子標靶治療，cetuximab 為首批獲准藥物之一 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-57484 | ERBITUX SOLN FOR INFUSION 5MG/ML | 輸注溶液 | 資料中未載明 |

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗 EGFR 單株抗體） |
| 骨髓抑制風險 | 請參考原廠仿單 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 請參考原廠仿單的警語與注意事項（文獻提及輸注反應與皮膚反應為常見議題） |
| 處置防護 | 請參考原廠仿單 |

---

## 安全性考量

- **藥物交互作用**：共查得 20 筆紀錄，其中：
  - **重大 (Major)**：Aminolevulinic acid、Thalidomide
  - **中度 (Moderate)**：多種質子幫浦抑制劑（Omeprazole、Esomeprazole、Lansoprazole、Pantoprazole、Rabeprazole、Dexlansoprazole）；化療藥物（Fluorouracil、Capecitabine、Cisplatin、Carboplatin、Oxaliplatin）；以及 Idelalisib、Methoxsalen、Verteporfin、Omacetaxine 等
- **其他**：文獻顯示 KRAS 突變可能造成對抗 EGFR 抗體的抗藥性；輸注反應可能嚴重。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第 1 的軟骨樣錯構瘤為良性病變，僅有模型預測、無任何試驗或文獻，也沒有 EGFR 相關機轉依據。
- 證據較多的囊性腫瘤，直接相關的僅有 1 項未完成確認的 Phase 1/2 試驗與一項結果不明的 Phase II 研究，且標籤與腺樣囊性癌的對應是間接的，未達推進標準。

**若要推進需要：**
- 取得香港仿單的警語、禁忌症與核准適應症，完成安全性篩選
- 補充 DrugBank 的作用機轉資料
- 釐清「囊性腫瘤」標籤與腺樣囊性癌、唾液腺癌的對應關係，並取得 NCT01192087 與 PMID 18804410 的完整結果
- 評估 EGFR 表現與 KRAS 等生物標記的篩選策略
- 考慮與 DrugBank 等來源比對，確認 TxGNN 高分預測是否具實際轉譯價值
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

