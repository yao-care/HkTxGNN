---
layout: default
title: Brigatinib
parent: 僅模型預測 (L5)
nav_order: 128
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Brigatinib：預測新適應症為牙齦纖維瘤病 (Fibromatosis, gingival)（證據等級 L5）。原適應症：非小細胞肺癌 (Non-small cell lung carcinoma)、肺癌"
monitor_inn: "BRIGATINIB"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung hilum carcinoma", "lung benign neoplasm", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "lung germ cell tumor", "pulmonary sulcus neoplasm", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
---

# Brigatinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Brigatinib：從非小細胞肺癌到牙齦纖維瘤病（預測）

## 一句話總結

Brigatinib 是一種激酶抑制劑，原本用於治療 ALK 陽性的非小細胞肺癌 (NSCLC)。
TxGNN 模型預測分數最高的新適應症是**牙齦纖維瘤病 (Gingival Fibromatosis)**，但目前**沒有任何臨床試驗或文獻**直接支持這項預測，屬於純模型預測。
在所有預測中，證據相對較多的方向是 **NF2 相關神經鞘瘤病**，但該方向目前只能算作需另行評估的研究線索。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 非小細胞肺癌 (Non-small cell lung carcinoma)、肺癌（取自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 牙齦纖維瘤病 (Fibromatosis, gingival) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，brigatinib 是一種以 ALK 為主要標靶的酪胺酸激酶抑制劑，亦會抑制 EGFR、FAK 等激酶，其在 ALK 陽性非小細胞肺癌中的療效已有 Phase 3 試驗 (ALTA-1L) 證實。

然而，ALK、EGFR、FAK 抑制與牙齦纖維瘤病之間，目前**找不到已知的機轉關聯**，也沒有相關臨床試驗或文獻。這個高分預測較可能反映知識圖譜中的網絡鄰近性，而非明確的生物學機制。因此這項預測應視為假說產生，而非可行動的再利用線索。

其他排名靠前的預測也有類似問題：

- **肺纖維瘤、肺錯構瘤、肺良性腫瘤**：分數高可能只是因為在知識圖譜中靠近肺部腫瘤節點。肺良性腫瘤所檢索到的文獻（如 ALTA-1L）談的都是原本的惡性適應症，並非真正的新適應症。
- **肺門癌、肺溝腫瘤**：若腫瘤為 ALK 陽性，可能與原適應症重疊，但沒有直接證據。
- **肺生殖細胞腫瘤**：僅有間接證據（神經母細胞瘤前臨床資料、嗜鉻細胞瘤與肺大細胞神經內分泌癌的個案報告），均限於 ALK 變異腫瘤。
- **遺傳性疾病（如交界型大疱性表皮鬆解症、VCP 相關肌病）**：機轉上看不出合理連結。

唯一值得另外追蹤的線索是 **NF2 相關神經鞘瘤病**：前臨床研究顯示 brigatinib 可透過抑制多種酪胺酸激酶（非 ALK）使 NF2 缺陷的腦膜瘤與神經鞘瘤縮小，2024 年也有針對進展性腫瘤患者的報告。不過這項線索是在排名第 10 的症候群標籤下被檢索出來的，該標籤本身並無直接證據，應視為獨立適應症另行評估。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對排名第 1 的預測（牙齦纖維瘤病），目前無相關文獻。

以下為其他預測項目中，與 brigatinib 較相關的文獻，供參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 | 對應預測 |
|------|-----|------|------|---------|---------|
| [38904277](https://pubmed.ncbi.nlm.nih.gov/38904277/) | 2024 | 小型臨床系列／個案報告 | N Engl J Med | 用於進展性 NF2 相關神經鞘瘤病患者 | NF2 相關神經鞘瘤病（歸於排名 10） |
| [34264955](https://pubmed.ncbi.nlm.nih.gov/34264955/) | 2021 | 前臨床 | PLoS One | 透過抑制多種酪胺酸激酶（非 ALK）使 NF2 缺陷腦膜瘤與神經鞘瘤縮小 | NF2 相關神經鞘瘤病 |
| [39395329](https://pubmed.ncbi.nlm.nih.gov/39395329/) | 2024 | 個案報告 | Respir Investig | EML4-ALK 陽性肺大細胞神經內分泌癌出現治療效果 | 肺生殖細胞腫瘤（間接） |
| [34371380](https://pubmed.ncbi.nlm.nih.gov/34371380/) | 2021 | 個案報告 | ESMO Open | ALK 突變的難治性轉移性嗜鉻細胞瘤出現持續緩解 | 肺生殖細胞腫瘤（間接） |
| [27049722](https://pubmed.ncbi.nlm.nih.gov/27049722/) | 2016 | 前臨床 | Oncotarget | 抑制 ALK 陽性神經母細胞瘤細胞、果蠅與小鼠的活性與生長 | 肺生殖細胞腫瘤（間接） |
| [30280657](https://pubmed.ncbi.nlm.nih.gov/30280657/) | 2018 | RCT (Phase 3) | N Engl J Med | 在未用過 ALK 抑制劑的 ALK 陽性 NSCLC 中，無惡化存活期優於 crizotinib（原適應症） | 原適應症 |
| [34537440](https://pubmed.ncbi.nlm.nih.gov/34537440/) | 2021 | RCT (Phase 3 最終結果) | J Thorac Oncol | ALTA-1L 最終分析確認療效與安全性（原適應症） | 原適應症 |
| [34987411](https://pubmed.ncbi.nlm.nih.gov/34987411/) | 2021 | 個案報告（不良事件） | Front Pharmacol | 肺腺癌患者使用後發生致命性腫瘤溶解症候群 | 安全性訊號 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66121 | ALUNBRIG TABLETS 90MG | 錠劑 | 許可證資料未載明 |
| HK-66119 | ALUNBRIG TABLETS 180MG | 錠劑 | 許可證資料未載明 |
| HK-66120 | ALUNBRIG TABLETS 30MG | 錠劑 | 許可證資料未載明 |

三張許可證皆為單一成分、有效狀態，持證商為 Takeda Pharmaceuticals (Hong Kong) Limited。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（酪胺酸激酶抑制劑，ALK 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為其中列出的主要項目：
  - **重度 (Major)**：Aprepitant、Dexamethasone、Clarithromycin
  - **中度 (Moderate)**：Acarbose、Famotidine、Ranitidine、Rabeprazole、Cimetidine、Metformin、Pioglitazone、Loperamide、Morphine、Cisapride、Clotrimazole 等；另有多種降血糖藥（如 Albiglutide、Alogliptin、Canagliflozin、Dapagliflozin、Chlorpropamide、Acetohexamide）
- **文獻中的安全性訊號**：有個案報告指出，在接受多種 ALK 抑制劑循序治療的肺腺癌患者中，brigatinib 曾引發致命性腫瘤溶解症候群 (PMID 34987411)。

主要警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第 1 的預測（牙齦纖維瘤病）僅有模型分數，沒有臨床試驗、文獻，也找不到合理的機轉連結。多數高分預測似乎反映知識圖譜中與肺腫瘤的鄰近性，並非真正的再利用訊號。
- 唯一較有前景的線索是 NF2 相關神經鞘瘤病，應作為獨立的研究問題，而非歸入本次預測的症候群。

**若要推進需要：**
- 取得 brigatinib 完整的作用機轉資料（MOA），以進行機轉關聯分析
- 取得香港仿單的警語與禁忌症資料，才能進行安全性篩選
- 針對 NF2 相關神經鞘瘤病另行建立評估，包括整理 2024 年 NEJM 報告的結果與安全性資料，並檢索相關臨床試驗
- 若要研究牙齦纖維瘤病，需先找出具體的生物學假說與前臨床證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

