---
layout: default
title: Insulin Aspart
parent: 僅模型預測 (L5)
nav_order: 469
evidence_level: L5
indication_count: 8
monitor_inn: "INSULIN ASPART"
predicted_indications: ["autoimmune oophoritis", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy"]
last_modified_at: 2026-10-23
description: "Insulin Aspart：預測新適應症為自體免疫性卵巢炎 (autoimmune oophoritis)（證據等級 L5）。原適應症：糖尿病、糖尿病酮酸中毒"
---

# Insulin Aspart
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

## Insulin Aspart：從糖尿病到自體免疫性卵巢炎
{: .text-alpha }

## 一句話總結

Insulin Aspart 是速效型胰島素類似物，在知識圖譜中記錄的原適應症為糖尿病與糖尿病酮酸中毒。
TxGNN 模型預測它可能對**自體免疫性卵巢炎 (autoimmune oophoritis)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 糖尿病、糖尿病酮酸中毒（知識圖譜記錄的關聯；香港許可證資料未提供核准適應症文字） |
| 預測新適應症 | 自體免疫性卵巢炎 (autoimmune oophoritis) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 14 張／共 14 張） |
| 許可證數 | 14 張（有效 14 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Insulin Aspart 是胰島素類似物，一般用於控制血糖；其與預測新適應症的關聯，目前只能依推論。

可能的連結有兩點：胰島素訊號可能影響卵巢顆粒細胞功能，且自體免疫性內分泌疾病常與自體免疫性糖尿病並存。然而，Insulin Aspart 並無已知針對卵巢自體免疫的免疫調節作用，這個連結屬於推測，缺乏實證支持。

TxGNN 模型（深度學習）的分數雖高 (0.9992)，但該分數可能反映模型學到的相關疾病之間的相似性，並非生物學證據，不等於治療效果。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

資料顯示香港共有 14 張有效的單一成分許可證，皆為有效狀態。以下列出 5 張主要許可證（許可證資料未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-55341 | NOVORAPID FLEXPEN INJ 100U/ML | NOVO NORDISK HONG KONG LIMITED |
| HK-67493 | FIASP FLEXTOUCH SOLUTION FOR INJECTION IN PRE-FILLED PEN 100U/ML 3ML | NOVO NORDISK HONG KONG LIMITED |
| HK-68936 | KIRSTY SOLUTION FOR INJECTION IN PRE-FILLED PEN 300 UNITS/3ML | PRIMEDICA LIMITED |
| HK-68191 | NOVORAPID FLEXPEN SOLUTION FOR INJECTION IN PRE-FILLED PEN 100U/ML | NOVO NORDISK HONG KONG LIMITED |
| HK-60462 | NOVORAPID PENFILL SOLUTION FOR INJECTION 100U/ML | NOVO NORDISK HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測，沒有直接研究自體免疫性卵巢炎的臨床試驗或文獻，證據等級為 L5。
- Insulin Aspart 沒有已知的卵巢自體免疫調節機轉，目前不建議推進。

**若要推進需要：**
- 取得詳細的作用機轉資料，並釐清胰島素與卵巢自體免疫之間是否有生物學連結
- 先進行文獻系統性檢索與前臨床研究，確認是否有任何直接證據
- 取得香港許可證的仿單，完成警語、禁忌與交互作用的安全性評估

## 其他預測適應症備註

其餘預測候選目前均為 Hold，摘要如下：

| 預測適應症 | 預測分數 | 證據等級 | 備註 |
|-----------|---------|---------|------|
| 骨發育不良症 (opsismodysplasia) | 0.9959 | L5 | INPPL1 (SHIP2) 參與胰島素訊號，僅為路徑層面關聯，無證據顯示外源胰島素有益 |
| 硫胺素反應性功能障礙症候群 | 0.9957 | L5 | 該症候群含糖尿病表現，胰島素僅用於症狀性血糖控制，並非改變疾病本身 |
| 局部僵硬肢體症候群 | 0.9951 | L5 | 與抗 GAD 自體免疫及糖尿病相關，胰島素不處理神經免疫機轉 |
| 典型僵人症候群 | 0.9951 | L5 | 胰島素僅用於合併的糖尿病，無證據改變神經病程 |
| 胰臟發育不全 (pancreatic agenesis) | 0.9944 | L5 | 胰島素替代在生理上合理，但屬於荷爾蒙補充，與原糖尿病適應症一致，並非真正的藥物再利用。檢索到的兩篇文獻（胰島素自體免疫症候群病例報告、第二型糖尿病胰島素治療回顧）並未直接研究此疾病 |
| 藥物誘發局部脂肪營養不良 | 0.9935 | L5 | 注射部位脂肪營養不良是胰島素已知不良反應，藥物較可能是成因而非治療，安全性考量不支持再利用 |
| 離心性脂肪營養不良 | 0.9932 | L5 | 僅有理論性連結，無益處證據，且胰島素相關脂肪營養不良為已知不良反應 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

