---
layout: default
title: Insulin Glulisine
parent: 僅模型預測 (L5)
nav_order: 473
evidence_level: L5
indication_count: 9
monitor_inn: "INSULIN GLULISINE"
predicted_indications: ["thiamine-responsive dysfunction syndrome", "opsismodysplasia", "focal stiff limb syndrome", "classic stiff person syndrome", "autoimmune oophoritis", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
last_modified_at: 2026-10-23
description: "Insulin Glulisine：預測新適應症為硫胺素反應性功能障礙症候群（證據等級 L5）。原適應症：知識圖譜記錄：糖尿病、糖尿病酮酸中毒"
---

# Insulin Glulisine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Insulin Glulisine：從糖尿病到硫胺素反應性功能障礙症候群
{: .text-alpha }

## 一句話總結

Insulin Glulisine 是速效胰島素類似物，知識圖譜中記錄的相關疾病為糖尿病與糖尿病酮酸中毒。
TxGNN 模型預測它可能對**硫胺素反應性功能障礙症候群 (thiamine-responsive dysfunction syndrome)** 有關聯，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測，且關聯可能來自糖尿病共病。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄：糖尿病、糖尿病酮酸中毒（香港許可證未載明核准適應症文字） |
| 預測新適應症 | 硫胺素反應性功能障礙症候群 |
| TxGNN 預測分數 | 0.9947 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Insulin Glulisine 屬於速效胰島素類似物，在糖尿病血糖控制上被使用，但本報告所整理的資料並未提供其作用機轉細節。

硫胺素反應性巨母細胞性貧血 (TRMA，SLC19A2 突變) 常合併糖尿病，因此胰島素本來就被用於處理其糖尿病部分。這屬於症狀性的支持照護，並非針對硫胺素運輸缺陷的再利用。TxGNN 模型（深度學習）的高分可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56757 | APIDRA SOLOSTAR SOLUTION FOR INJ 100 UNITS/ML (PRE-FILLED PEN) | 預充填注射筆（注射液） | 許可證資料未載明 |

## 安全性考量

- **藥物交互作用**：共查得 100 項交互作用，以下為部分列出（多為中度）：
  - 中度：Phenylephrine、Acebutolol、Acetazolamide、Formoterol、Pseudoephedrine、Doxycycline、Epinephrine、Ethinylestradiol、Hydrocortisone、Albiglutide、Salbutamol、Ethanol、Hydrochlorothiazide、Alogliptin、Metformin、Pioglitazone、Estradiol、Alpelisib
  - 輕微：Hydrocortisone（外用）、Alclometasone（外用）

其他警語與禁忌請參考原廠仿單。

## 其他排名較前的預測（供參考）

所有預測皆無臨床試驗與文獻支持，以下為各項的重點判讀：

| 排名 | 預測疾病 | 分數 | 證據等級 | 判讀 |
|------|---------|------|---------|------|
| 2 | Opsismodysplasia | 0.9946 | L5 | INPPL1 (SHIP2) 為胰島素訊號負調控因子，僅有理論連結，無證據 |
| 3 | 局部僵硬肢症候群 | 0.9946 | L5 | 可能源自 GAD 自體免疫與第一型糖尿病的共病關聯 |
| 4 | 典型僵人症候群 | 0.9946 | L5 | 胰島素僅治療共病糖尿病，對神經症狀無已知效果 |
| 5 | 自體免疫卵巢炎 | 0.9937 | L5 | 共病驅動的關聯，無證據顯示可調節卵巢自體免疫 |
| 6 | 胰臟發育不全 | 0.9917 | L5 | 胰島素替代為標準照護，合理但屬於荷爾蒙替代；速效類似物在新生兒未被專門研究，且未見直接研究 |
| 7 | 藥物誘發局部脂肪失養症 | 0.9915 | L5 | 胰島素本身可造成注射部位脂肪失養，應視為安全性訊號 |
| 8 | 離心性脂肪失養症 | 0.9911 | L5 | 理論依據薄弱，且胰島素相關脂肪萎縮為已知不良反應 |
| 9 | 壓力誘發局部脂肪萎縮 | 0.9910 | L5 | 注射本身可致脂肪萎縮，無支持證據 |

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究此預測疾病，證據等級為 L5。
- 預測分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據；胰島素僅是對合併的糖尿病做支持性處置，並非治療硫胺素運輸缺陷本身。

**若要推進需要：**
- 補齊作用機轉資料與原廠仿單的警語、禁忌資料
- 針對 TRMA 合併糖尿病族群進行文獻回顧，釐清速效胰島素類似物的實際使用情形
- 若考慮胰臟發育不全，可另行評估新生兒速效類似物的使用資料
- 脂肪失養類預測應改列為安全性訊號，而非再利用候選
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

