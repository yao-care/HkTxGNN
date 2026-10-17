---
layout: default
title: Posaconazole
parent: 中證據等級 (L3-L4)
nav_order: 715
evidence_level: L4
indication_count: 1
last_modified_at: 2026-10-14
description: "Posaconazole：預測新適應症為肺囊蟲病 (Pneumocystosis)（證據等級 L4）。原適應症：香港許可證未提供核准適應症文字"
monitor_inn: "POSACONAZOLE"
predicted_indications: ["pneumocystosis"]
---

# Posaconazole
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Posaconazole：從侵襲性黴菌感染到肺囊蟲病（Pneumocystosis）

## 一句話總結

Posaconazole 是三唑類抗黴菌藥物，原本用於麴菌症、念珠菌症、組織漿菌症等多種黴菌感染。
TxGNN 模型預測它可能對**肺囊蟲病 (Pneumocystosis)** 有效，但目前**沒有直接評估 posaconazole 的臨床試驗**，文獻也僅為間接背景資料，證據屬於模型預測加機轉推論階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未提供核准適應症文字；知識圖譜列出的原適應症包括麴菌症、念珠菌症、口咽念珠菌症、組織漿菌症、球黴菌症、孢子絲菌症、鐮刀菌症、足菌腫等 |
| 預測新適應症 | 肺囊蟲病 (Pneumocystosis) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就一般藥理知識，posaconazole 是三唑類抗黴菌藥，抑制黴菌的羊毛固醇 14-α 去甲基酶（CYP51），阻斷麥角固醇合成，進而破壞黴菌細胞膜。

然而，肺囊蟲（*Pneumocystis jirovecii*）的細胞膜幾乎不含麥角固醇，而是以膽固醇為主。因此，azole 類藥物在此病原體上缺乏明確的作用標的，機轉上的支持其實很薄弱。

TxGNN 的高分（99.77%）較可能反映知識圖譜中「抗黴菌藥物與黴菌性肺部疾病」的類別關聯，而非經驗證的藥理機制。已知的文獻僅提到 posaconazole 可用於高風險血液腫瘤病人的黴菌預防，並未顯示它對肺囊蟲肺炎本身有效。此預測應視為待驗證的假說。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | 已完成 | 602 | 評估 rezafungin（非 posaconazole）預防異體造血幹細胞移植成人侵襲性黴菌感染；與本藥無直接關聯，僅提供抗黴菌預防領域的背景 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Med Wkly | 概述念珠菌、麴菌、隱球菌與肺囊蟲感染；提到 posaconazole 等黴菌預防使高風險血液腫瘤病人的侵襲性感染明顯減少 |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clin Pharmacokinet | 整理抗黴菌藥物在肺上皮襯液的穿透性（藥動學背景） |
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Guideline | Lancet Infect Dis | 英國醫學黴菌學會 2025 年嚴重黴菌病診斷建議更新 |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Guideline | Zhonghua Jie He He Hu Xi Za Zhi | 中國侵襲性肺部黴菌病診治指引（2025 版） |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transpl Infect Dis | 肝移植後急性 GVHD 的感染併發症回顧性世代研究 |

以上文獻皆未提供 posaconazole 治療肺囊蟲病的直接證據。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67802 | POSACON ORAL SUSPENSION 40MG/ML | 口服懸液劑 | 未提供 |
| HK-56439 | NOXAFIL ORAL SUSP 40MG/ML | 口服懸液劑 | 未提供 |
| HK-68771 | MOMETAMAX ULTRA EAR DROPS SUSPENSION FOR DOGS (VET) | 耳用滴劑（獸用） | 未提供 |

---

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用，以下列出部分主要項目：
  - **重大（Major）**：Loperamide、Triamcinolone、Budesonide
  - **中度（Moderate）**：Famotidine、Ranitidine、Cimetidine、Omeprazole、Rabeprazole、Hydrocortisone、Dexamethasone、Betamethasone、Aprepitant、Clarithromycin、Saxagliptin、Bisacodyl 等

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何直接評估 posaconazole 用於肺囊蟲病的臨床試驗或文獻，唯一的試驗是另一種藥物（rezafungin）。
- 肺囊蟲缺乏麥角固醇，與 azole 類藥物的作用機轉不符，高 TxGNN 分數可能僅反映類別關聯。

**若要推進需要：**
- 取得 posaconazole 的完整作用機轉資料，並驗證其對肺囊蟲的體外或動物模型活性
- 搜尋是否有 posaconazole 用於肺囊蟲病的病例報告或回溯性研究
- 取得香港衛生署核准仿單，補齊警語、禁忌與核准適應症
- 與現行標準治療（如 TMP-SMX）比較，評估潛在臨床定位
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

