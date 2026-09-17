---
layout: default
title: Itraconazole
parent: 中證據等級 (L3-L4)
nav_order: 420
evidence_level: L4
indication_count: 1
---

# Itraconazole
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Itraconazole：從黴菌感染到肺囊蟲病 (Pneumocystosis)

## 一句話總結

Itraconazole 是三唑類抗黴菌藥，原用於全身性黴菌感染的治療與預防。
TxGNN 模型預測它可能對**肺囊蟲病 (Pneumocystosis)** 有效，
目前有 **0 個臨床試驗**，僅有 **20 篇文獻**（多為間接相關的伺機性感染文獻）支持，且機轉關聯性存疑。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無正式核准適應症資料；依藥物類別推斷為全身性黴菌感染（三唑類抗黴菌藥） |
| 預測新適應症 | 肺囊蟲病 (Pneumocystosis) |
| TxGNN 預測分數 | 99.34%（排名第 11034） |
| 證據等級 | L4 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Itraconazole 為三唑類抗黴菌藥，作用機轉是抑制真菌的 CYP51（lanosterol 14α-demethylase），阻斷 ergosterol（麥角固醇）合成，進而破壞真菌細胞膜完整性。

然而 *Pneumocystis jirovecii*（引起肺囊蟲病的病原體）在分類上屬於非典型真菌，其細胞膜主要以 cholesterol 構成，幾乎不含 ergosterol。這代表唑類抗黴菌藥的藥理標靶在此病原體上基礎薄弱，機轉關聯性偏低。實際上有文獻（PMID 12606318）指出 *Pneumocystis carinii* 對唑類抗黴菌藥存在天然抗性。

因此 TxGNN 給出的高分（0.993）與機轉分析並不一致，較可能是模型從「伺機性感染」（HIV/器官移植/免疫低下族群中黴菌感染與肺囊蟲病常同時出現）的共現模式中間接學習到的關聯，而非真正的藥理標靶匹配。正式的 DrugBank MOA 記錄目前仍缺失（見 Data Gap DG002），上述機轉分析僅供參考，尚待正式來源確認。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | 隨機雙盲安慰劑對照試驗：itraconazole 膠囊用於預防 HIV 感染者深部黴菌感染 |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | HIV 患者伺機性感染（含肺囊蟲肺炎）之初級與次級預防策略回顧 |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Cohort | Indian J Med Microbiol | 比較免疫功能正常與低下族群呼吸道黴菌病原譜及其與 CD4 細胞數的相關性 |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplantation Proceedings | 腎臟移植患者侵襲性黴菌感染單中心經驗 |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | 機轉研究 | Am J Respir Cell Mol Biol | 鑑定 *Pneumocystis carinii* 的 lanosterol 14α-demethylase，指出其對唑類抗黴菌藥具天然抗性 |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | 全身性原蟲/伺機性感染（含 *Pneumocystis carinii*）治療與預防藥物總論 |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | 肺移植後感染（含黴菌與肺囊蟲）之預防與治療回顧 |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Curr Clin Top Infect Dis | 骨髓移植患者感染預防與治療回顧 |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case Report | Frontiers in Immunology | STAT1 突變兒童併發馬爾尼菲籃狀菌與肺囊蟲共感染病例 |
| [8967681](https://pubmed.ncbi.nlm.nih.gov/8967681/) | 1996 | Case Report | Annals of Internal Medicine | Rifabutin 預防合併 itraconazole 治療引發葡萄膜炎的不良事件病例 |

---

## 香港上市資訊

Itraconazole 目前**未於香港上市**，查無許可證資料。

---

## 安全性考量

目前查無主要警語、禁忌症或藥物交互作用資料（Data Gap DG001，屬 Blocking 等級，影響安全性初評），且因未於香港上市而無本地仿單可參考，建議查詢原廠（如美國/歐盟）核准仿單以取得完整安全性資訊。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉分析顯示唑類抗黴菌藥對 *Pneumocystis jirovecii*（缺乏 ergosterol 細胞膜）的藥理標靶基礎薄弱，與 TxGNN 高分不一致，需視為模型對感染共現模式的間接學習結果。
- 無任何直接測試 itraconazole 治療/預防肺囊蟲病的臨床試驗，僅有間接相關文獻，證據等級僅達 L4；安全性資料（DG001，Blocking）缺失，無法進入 S1 安全性初評。

**若要推進需要：**
- 補齊 TFDA/原廠仿單警語與禁忌症資料（DG001，Blocking）
- 透過 DrugBank API 或原廠資料正式確認作用機轉（DG002）
- 尋求體外/動物實驗證據，確認 itraconazole 對 *Pneumocystis* 是否存在非 ERG11 依賴的替代作用機制
- 若無法補強機轉合理性，建議將此候選降低優先序或排除
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

