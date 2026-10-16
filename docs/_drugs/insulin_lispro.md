---
layout: default
title: Insulin Lispro
parent: 僅模型預測 (L5)
nav_order: 475
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Insulin Lispro：預測新適應症為自體免疫性卵巢炎 (Autoimmune Oophoritis)（證據等級 L5）。原適應症：第 2 型糖尿病、第 1 型糖尿病、糖尿病酮酸中毒"
monitor_inn: "INSULIN LISPRO"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia"]
---

# Insulin Lispro
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

# Insulin Lispro：從糖尿病到自體免疫性卵巢炎

## 一句話總結

Insulin Lispro 是速效型胰島素類似物，原本用於第 1 型與第 2 型糖尿病及糖尿病酮酸中毒的治療。
TxGNN 模型預測它可能對**自體免疫性卵巢炎 (Autoimmune Oophoritis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型的計算預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第 2 型糖尿病、第 1 型糖尿病、糖尿病酮酸中毒（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 自體免疫性卵巢炎 (Autoimmune Oophoritis) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Insulin Lispro 是胰島素類似物，在糖尿病中的血糖控制療效已被證實，但其機轉是否適用於自體免疫性卵巢炎，尚無資料可以確認。

一個可能但未經驗證的關聯是：胰島素訊號會影響卵巢功能與免疫調節，而自體免疫性卵巢炎常與第 1 型糖尿病、自體免疫性多腺體症候群等其他自體免疫內分泌疾病並存。不過，疾病並存只代表兩者有關聯，並不表示 Insulin Lispro 能治療卵巢炎。

原適應症（糖尿病）屬代謝性疾病，與新適應症的免疫性病因差異大。因此這個預測目前只能視為假說。

### 其他高分預測（供參考）

| 排名 | 預測疾病 | TxGNN 分數 | 評估 |
|------|---------|-----------|------|
| 2 | 硫胺素反應性功能障礙症候群 (Thiamine-responsive dysfunction syndrome) | 99.37% | 可能反映共同的糖尿病表型；胰島素僅是症狀性血糖控制 |
| 3 | 局部僵硬肢體症候群 (Focal stiff limb syndrome) | 99.36% | 可能來自抗 GAD 自體免疫的共同關聯，缺乏直接機轉證據 |
| 4 | 典型僵人症候群 (Classic stiff person syndrome) | 99.36% | 與第 1 型糖尿病共病；胰島素治療共病，不治療神經免疫疾病 |
| 5 | 奧普西斯骨發育不良 (Opsismodysplasia) | 99.34% | INPPL1 (SHIP2) 調控胰島素訊號，屬純假說性連結 |

以上 5 項預測皆為 L5 等級，建議決策皆為 Hold。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60381 | HUMALOG 100 U/ML KWIKPEN SOLUTION FOR INJECTION | 注射劑 | 未提供 |
| HK-42887 | HUMALOG INJ 3ML CARTRIDGE 100U/ML | 注射劑 | 未提供 |
| HK-42886 | HUMALOG INJ 100U/ML | 注射劑 | 未提供 |
| HK-60379 | HUMALOG MIX50 100 U/ML KWIKPEN SUSPENSION FOR INJECTION | 注射懸液劑 | 未提供 |
| HK-60380 | HUMALOG MIX25 100 U/ML KWIKPEN SUSPENSION FOR INJECTION | 注射懸液劑 | 未提供 |

以上 5 張許可證均為有效的單一成分製劑，持證商為 ELI LILLY ASIA, INC.。

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用，以下列出部分主要項目（多為中度）：
  - 擬交感神經藥物與支氣管擴張劑：Phenylephrine、Pseudoephedrine、Epinephrine、Salbutamol、Formoterol
  - 乙型阻斷劑與利尿劑：Acebutolol、Acetazolamide、Hydrochlorothiazide
  - 其他降血糖藥物：Metformin、Alogliptin、Albiglutide
  - 荷爾蒙與皮質類固醇：Estradiol、Ethinylestradiol、Levonorgestrel、Hydrocortisone
  - 其他：Doxycycline、Alpelisib、Ethanol

  局部用皮質類固醇（Hydrocortisone topical、Alclometasone topical）為輕度交互作用。

其餘警語與禁忌症資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.78%），但完全沒有臨床試驗或文獻支持，證據等級僅為 L5。
- 所提出的機轉連結來自疾病共病關係，而非藥理作用；胰島素在這些情況下最多是治療併發的糖尿病，而不是治療預測的疾病本身。

**若要推進需要：**
- 詳細的藥物作用機轉資料（MOA）
- 原廠仿單的警語與禁忌症資料（目前為阻斷性資料缺口）
- 針對自體免疫性卵巢炎的文獻回顧與前臨床機轉研究
- 評估給藥途徑與目標疾病是否相容
- 若前述研究顯示有生物學依據，再規劃探索性臨床研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

