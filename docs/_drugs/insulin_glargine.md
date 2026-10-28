---
layout: default
title: Insulin Glargine
parent: 僅模型預測 (L5)
nav_order: 472
evidence_level: L5
indication_count: 10
monitor_inn: "INSULIN GLARGINE"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
last_modified_at: 2026-10-23
description: "Insulin Glargine：預測新適應症為自體免疫性卵巢炎 (Autoimmune Oophoritis)（證據等級 L5）。原適應症：第 2 型糖尿病、第 1 型糖尿病、糖尿病酮酸中毒"
---

# Insulin Glargine
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

## Insulin Glargine：從糖尿病到自體免疫性卵巢炎
{: .text-alpha }

## 一句話總結

Insulin Glargine（甘精胰島素）是長效基礎胰島素類似物，在知識圖譜中記錄的原有用途為第 1 型與第 2 型糖尿病及糖尿病酮酸中毒。
TxGNN 模型預測排名第一的新適應症為**自體免疫性卵巢炎 (Autoimmune Oophoritis)**，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第 2 型糖尿病、第 1 型糖尿病、糖尿病酮酸中毒（知識圖譜記錄的關聯；香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 自體免疫性卵巢炎 (Autoimmune Oophoritis) |
| TxGNN 預測分數 | 0.9988 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 7 張／共 7 張） |
| 許可證數 | 7 張（有效 7 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知甘精胰島素是長效基礎胰島素類似物，作用於胰島素受體，用於控制血糖。

自體免疫性卵巢炎是免疫介導的卵巢疾患。目前無法建立兩者之間的直接機轉關聯。模型的高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，例如自體免疫多內分泌症候群等共同的自體免疫內分泌關聯，而非生物學證據。

因此這個預測應視為假說層級的訊號，不宜解讀為有治療合理性。

**其他預測適應症摘要（前 10 名皆為 L5，唯一例外見下）：**

| 排名 | 疾病 | 分數 | 說明 |
|------|------|------|------|
| 2 | 硫胺素反應性功能障礙症候群 | 0.9961 | 糖尿病為其症狀之一，胰島素僅是症狀性血糖處置，並非真正的再利用 |
| 3 | 局部僵硬肢症候群 | 0.9960 | 與抗 GAD 自體免疫及第 1 型糖尿病共病有關，胰島素不處理神經病變 |
| 4 | 典型僵人症候群 | 0.9960 | 同上 |
| 5 | 類骨發育不良 (Opsismodysplasia) | 0.9959 | INPPL1 參與胰島素訊號，僅屬推測性連結 |
| 6 | 胰臟發育不全 | 0.9943 | 胰島素替代合理，但屬荷爾蒙補充而非新用途 |
| 7 | 藥物引起的局部脂肪營養不良 | 0.9942 | 為注射胰島素的已知不良反應，屬安全訊號而非適應症 |
| 8–10 | 離心性、壓力性、特發性局部脂肪營養不良 | 0.9938–0.9934 | 無機轉依據，注射胰島素反而可能造成局部脂肪萎縮 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對排名第一的自體免疫性卵巢炎，目前無相關文獻。

作為參考，排名第 6 的胰臟發育不全有 4 篇間接文獻，但均未直接研究該疾病：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | J Am Pharm Assoc | 回顧第 2 型糖尿病的胰島素治療與起始實務 |
| [19322513](https://pubmed.ncbi.nlm.nih.gov/19322513/) | 2009 | Review | Acta Diabetol | 內分泌疾病相關的續發性糖尿病與新治療方式 |
| [32871938](https://pubmed.ncbi.nlm.nih.gov/32871938/) | 2020 | Case report | Medicine | MODY5 病例以 GLP-1 受體促效劑治療 |
| [25818213](https://pubmed.ncbi.nlm.nih.gov/25818213/) | 2015 | 世代研究（獸醫） | J Vet Intern Med | 糖尿病貓的血清胰臟酵素與超音波追蹤 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56520 | LANTUS SOLOSTAR PRE-FILLED PEN INJ 100 UNITS/ML | 注射劑（預填充筆） | 資料未載明 |
| HK-64661 | TOUJEO 300 UNITS/ML SOLUTION FOR INJECTION IN PRE-FILLED PEN 450 UNITS/1.5ML | 注射劑（預填充筆） | 資料未載明 |
| HK-65078 | BASAGLAR KWIKPEN SOLUTION FOR INJECTION IN A PRE-FILLED PEN 300 UNITS/3ML | 注射劑（預填充筆） | 資料未載明 |
| HK-65079 | BASAGLAR SOLUTION FOR INJECTION IN A CARTRIDGE 300 UNITS/3ML | 注射劑（卡式瓶） | 資料未載明 |
| HK-50530 | LANTUS INJ 100 UNITS/ML | 注射劑 | 資料未載明 |

共 7 張有效許可證，以上列出前 5 張。

---

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為部分中度項目：
  - 擬交感神經藥物：Phenylephrine、Pseudoephedrine、Epinephrine、Salbutamol、Formoterol
  - 乙型阻斷劑：Acebutolol
  - 其他降血糖藥：Metformin、Pioglitazone、Alogliptin、Albiglutide
  - 其他：Hydrochlorothiazide、Acetazolamide、Doxycycline、Ethanol、Estradiol、Ethinylestradiol、Hydrocortisone、Alpelisib
  - 輕度項目例如外用 Hydrocortisone、外用 Alclometasone

其餘警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的自體免疫性卵巢炎沒有任何臨床試驗或文獻，也沒有合理的機轉連結，屬 L5 等級的模型預測。
- 前 10 名預測多半反映共病關聯（如僵人症候群、糖尿病）或不良反應關聯（如局部脂肪營養不良），並非真正的新治療用途。

**若要推進需要：**
- 釐清胰島素受體訊號與卵巢自體免疫之間是否有任何生物學連結
- 針對自體免疫性卵巢炎的文獻與試驗系統性檢索
- 作用機轉資料與香港仿單的警語、禁忌症
- 若有興趣，可優先評估胰臟發育不全，但其屬荷爾蒙替代，且目前僅有間接文獻，並無直接研究該疾病的證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

