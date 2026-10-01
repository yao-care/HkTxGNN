---
layout: default
title: Itraconazole
parent: 僅模型預測 (L5)
nav_order: 484
evidence_level: L5
indication_count: 1
---

# Itraconazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Itraconazole：從抗真菌治療到肺囊蟲病 (Pneumocystosis)

## 一句話總結

Itraconazole 是一種 azole 類抗真菌藥，可抑制真菌的麥角固醇合成。
TxGNN 模型預測它可能對**肺囊蟲病 (Pneumocystosis)** 有效，但目前**沒有任何臨床試驗**，且**沒有文獻直接證實它對肺囊蟲病有效**。
19 篇文獻多為同一批免疫低下族群的感染症綜述或個案，機轉上也有疑慮，建議暫緩（Hold）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 肺囊蟲病 (Pneumocystosis) |
| TxGNN 預測分數 | 99.34% |
| 證據等級 | L4（僅有機轉層級的間接研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 19 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，DrugBank 端的 MOA 欄位尚未取得。根據已知資訊，itraconazole 抑制真菌的 CYP51（lanosterol 14-alpha-demethylase），阻斷麥角固醇合成，用於多種黴菌感染。

**這個預測的機轉基礎薄弱。**
- 肺囊蟲 (*Pneumocystis jirovecii*) 的細胞膜幾乎不含麥角固醇，主要依賴膽固醇等其他固醇，azole 類藥物的作用標的因此存疑。
- 2003 年一項研究選殖了 *P. carinii* 的 Erg11 基因，發現該菌對 azole 類藥物天生抗藥，部分潛在抗藥位點與抗 azole 的生物相同。
- 肺囊蟲病的標準一線預防與治療用藥屬於另一藥類，不是 itraconazole。

高分較可能來自圖譜上的共現關係。Itraconazole 常用於 HIV、器官移植、骨髓移植等免疫低下族群的其他黴菌感染，而這些族群也是肺囊蟲病的高風險群。文獻關聯多半反映這種共現，而不是療效證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

所有文獻的相關性審查狀態均為「待審」，下列摘要僅根據標題與摘要內容整理。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | RCT | HIV Medicine | 第三期雙盲安慰劑對照試驗，評估 itraconazole 預防 HIV 感染者的深部黴菌感染。終點不是肺囊蟲病，摘要未呈現結果 |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | 系統性原蟲感染（含 *P. carinii*）的治療與預防綜述，摘要未顯示與 itraconazole 的關聯 |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | 肺臟移植後感染的預防、辨識與治療進展 |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | 骨髓移植受者的感染預防與治療策略 |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | HIV 機會性感染的一級與二級預防 |
| [30429396](https://pubmed.ncbi.nlm.nih.gov/30429396/) | 2018 | Cohort | Indian Journal of Medical Microbiology | 比較免疫正常與免疫低下宿主的呼吸道黴菌病原分布，並分析與 CD4 細胞數的關係 |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplantation Proceedings | 腎臟移植後侵襲性黴菌感染的單中心經驗 |
| [12606318](https://pubmed.ncbi.nlm.nih.gov/12606318/) | 2003 | 機轉研究 | Am J Respir Cell Mol Biol | 選殖 *P. carinii* 的 Erg11（azole 標的酵素），指出該菌對 azole 類天生抗藥，不利於此預測 |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report | Frontiers in Immunology | STAT1 突變患童同時感染 *T. marneffei* 與 *P. jirovecii* 的個案 |
| [8967681](https://pubmed.ncbi.nlm.nih.gov/8967681/) | 1996 | Case report | Annals of Internal Medicine | rifabutin 預防用藥合併 itraconazole 治療相關的葡萄膜炎（安全性訊號，非療效） |

---

## 香港上市資訊

香港共有 19 張許可證，以下列出 5 張。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-54674 | ITRANSTAD CAP 100MG | HONG KONG MEDICAL SUPPLIES LTD |
| HK-63889 | ITRAZOL ORAL SOLUTION 10MG/ML | HIND WING CO LTD |
| HK-50434 | CANDITRAL CAP 100MG | SB PHARMA LIMITED |
| HK-50868 | ITRACON CAP 100MG | HEALTH ALLIANCE INTERNATIONAL CO LTD |
| HK-51056 | SPORANOX CAP 100MG | JOHNSON & JOHNSON (HONG KONG) LTD. |

---

## 安全性考量

安全性資訊請參考原廠仿單。

文獻中另有 itraconazole 與 rifabutin 併用時出現葡萄膜炎的個案報告（1996），僅作為交互作用的參考訊號。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻也沒有直接證明 itraconazole 對肺囊蟲病有效，證據等級僅為 L4。
- 肺囊蟲缺乏麥角固醇、對 azole 天生抗藥，機轉上不支持此預測。99.34% 的高分應視為圖譜共現的結果，不應當成療效訊號。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症（目前是阻斷性資料缺口，無法進入安全性篩選）。
- 從 DrugBank 補齊作用機轉資料。
- 人工審查 19 篇文獻的相關性，確認是否有直接以 itraconazole 治療或預防肺囊蟲病的研究。
- 與標準一線用藥比較，說明 itraconazole 的潛在定位；若無明確優勢，建議不再推進。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

