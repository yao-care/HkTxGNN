---
layout: default
title: Insulin Human
parent: 僅模型預測 (L5)
nav_order: 474
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Insulin Human：預測新適應症為自體免疫性卵巢炎 (Autoimmune Oophoritis)（證據等級 L5）。原適應症：第 2 型糖尿病、第 1 型糖尿病、糖尿病酮酸中毒"
monitor_inn: "INSULIN HUMAN"
predicted_indications: ["autoimmune oophoritis", "classic stiff person syndrome", "focal stiff limb syndrome", "thiamine-responsive dysfunction syndrome", "opsismodysplasia"]
---

# Insulin Human
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

# 人類胰島素（Insulin Human）：從第 1 型與第 2 型糖尿病到自體免疫性卵巢炎

## 一句話總結

人類胰島素原本用於治療第 1 型與第 2 型糖尿病，以及糖尿病酮酸中毒。
TxGNN 模型預測它可能對**自體免疫性卵巢炎 (Autoimmune Oophoritis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第 2 型糖尿病、第 1 型糖尿病、糖尿病酮酸中毒 |
| 預測新適應症 | 自體免疫性卵巢炎 (Autoimmune Oophoritis) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 18 張 |
| 建議決策 | Hold |

註：香港許可證資料中未收錄核准適應症文字，上列原適應症取自知識圖譜的適應症關聯。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，胰島素是調節血糖的代謝荷爾蒙，其療效在糖尿病中已被證實，但沒有已知的免疫調節或卵巢保護作用，機轉上並無直接證據顯示它適用於自體免疫性卵巢炎。

這個預測較可能來自疾病網路的關聯：第 1 型糖尿病常與其他自體免疫內分泌疾病並存（多腺體自體免疫），模型可能因此將胰島素與自體免疫性卵巢炎連結。這是間接的關聯，不代表胰島素能治療該疾病。

整體而言，這是僅由計算得出的假說，需要實際研究驗證。

### 其他預測適應症（供參考）

| 排名 | 預測疾病 | 預測分數 | 評估 |
|------|---------|---------|------|
| 2 | 典型僵人症候群 (Classic Stiff Person Syndrome) | 99.81% | 可能來自抗 GAD65 自體免疫與糖尿病的共同關聯；胰島素只能處理併發的糖尿病，無法處理神經自體免疫 |
| 3 | 局限性僵肢症候群 (Focal Stiff Limb Syndrome) | 99.81% | 屬僵人症候群譜系，分數相同，推論同上 |
| 4 | 硫胺素反應性功能障礙症候群 (Thiamine-responsive Dysfunction Syndrome) | 99.80% | 此病常伴隨糖尿病，胰島素僅是治療糖尿病症狀，硫胺素仍是主要療法 |
| 5 | 類骨發育不全 (Opsismodysplasia) | 99.79% | INPPL1 (SHIP2) 調控胰島素/PI3K-AKT 訊號，僅為推測性連結，無證據顯示外源胰島素能矯正骨骼表型 |

以上均為 L5、建議 Hold。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 18 張有效的單一成分許可證，無已註銷者。以下列出 5 張主要許可證：

| 許可證號 | 品名 | 廠商 | 核准適應症 |
|---------|------|------|-----------|
| HK-60290 | ACTRAPID PENFILL INJ 100IU/ML (BRAZIL) | Novo Nordisk Hong Kong | 未收錄 |
| HK-63758 | ACTRAPID SOLUTION FOR INJECTION 100IU/ML | Novo Nordisk Hong Kong | 未收錄 |
| HK-39494 | HUMULIN R INSULIN INJ 100IU/ML-CARTRIDGE | Eli Lilly Asia | 未收錄 |
| HK-54859 | SCILIN R INJ 100 IU/ML (CARTRIDGE) | Keen Health | 未收錄 |
| HK-39509 | HUMULIN INSULIN 70/30 INJ (CARTRIDGE) | Eli Lilly Asia | 未收錄 |

其餘許可證涵蓋 Actrapid、Mixtard 30、Scilin 與 Humulin 系列的不同劑型與包裝。

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用，以下為部分中度項目：
  - 擬交感神經藥：Phenylephrine、Pseudoephedrine、Epinephrine、Salbutamol
  - 其他降血糖藥：Metformin、Pioglitazone、Alogliptin、Albiglutide
  - 其他：Acebutolol（β 阻斷劑）、Benazepril、Hydrochlorothiazide、Acetazolamide、Doxycycline、Ethanol、Hydrocortisone、Estradiol、Ethinylestradiol、Alpelisib
  - 輕度項目：外用 Hydrocortisone、外用 Alclometasone

  這些交互作用多與血糖控制改變有關，使用時需注意血糖監測。

警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 五個預測適應症皆僅有模型分數，沒有臨床試驗或文獻，證據等級為 L5。
- 預測多來自疾病網路的間接關聯（自體免疫共病、糖尿病併發），而非胰島素對這些疾病的直接作用。

**若要推進需要：**
- 取得並確認胰島素的作用機轉資料
- 系統性搜尋自體免疫性卵巢炎與胰島素相關的臨床或前臨床研究
- 釐清模型預測的來源，區分「治療該疾病」與「僅處理併發糖尿病」
- 取得香港衛生署的仿單，補齊警語與禁忌症資料
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

