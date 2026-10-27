---
layout: default
title: Cobicistat
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Cobicistat：預測新適應症為猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)（證據等級 L5）。原適應症：HIV 感染、AIDS"
monitor_inn: "COBICISTAT"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Cobicistat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Cobicistat：從 HIV 感染到猿猴免疫缺陷病毒感染（模型預測）
{: .text-alpha }

## 一句話總結

Cobicistat 是一種藥物動力學增強劑，原本用於 HIV 感染與 AIDS 的抗病毒治療組合中。
TxGNN 模型預測它可能對**猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染、AIDS（取自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cobicistat 是一種以機轉為基礎的 CYP3A 抑制劑，用來提高其他抗反轉錄病毒藥物（如 darunavir、atazanavir、elvitegravir）的血中濃度，本身並無已知的抗病毒活性。

SIV 與 HIV 同屬慢病毒，親緣關係相近，模型的高分很可能反映its 與已核准 HIV 適應症在知識圖譜上的鄰近性。若 Cobicistat 對 SIV 有任何益處，也必須依賴與其併用的抗病毒藥物。

需要注意：SIV 感染是非人類靈長類的動物模型疾病，並非人類臨床適應症，因此不是有意義的人類藥物再利用目標。

另外，同一份預測還列出另外兩個候選，同樣只有模型預測、沒有任何證據支持：
- **貓後天免疫缺陷症候群 (Feline AIDS)**：分數同為 99.92%，屬獸醫領域疾病，與 SIV 分數完全相同，推測是圖譜鄰近節點造成的假象。
- **伴有共濟失調步態、無語言能力及皮質白質減少的神經發育障礙**：分數 99.91%，Cobicistat 的藥理（CYP3A 與轉運蛋白抑制）與此罕見遺傳疾病的病理沒有已知關聯，高分很可能是圖譜假象。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64960 | PREZCOBIX TABLETS 800MG/150MG | 錠劑 | 未載明 |
| HK-65912 | SYMTUZA TABLETS | 錠劑 | 未載明 |

兩張許可證均為有效的單方登記，持有者皆為 Johnson & Johnson (Hong Kong) Ltd.。

---

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用，以下列出部分例子（作為 CYP3A 抑制劑，併用藥物的暴露量可能上升）：
  - **嚴重 (Major)**：Loperamide、Triamcinolone、Cisapride、Budesonide
  - **中度 (Moderate)**：Hydrocortisone、Aprepitant、Betamethasone、Dexamethasone、Clarithromycin、Clotrimazole、Metoclopramide、Repaglinide、Fenfluramine
  - **輕微 (Minor)**：Prucalopride
- 長期使用的 CYP3A 抑制劑會帶來可觀的多重用藥負擔，若用於兒童神經科族群，風險更需謹慎評估。

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 三個預測適應症都只有模型分數，沒有臨床試驗或文獻（證據等級 L5）。
- SIV 與貓 AIDS 屬動物疾病，不是人類再利用目標；神經發育障礙則找不到機轉關聯。Cobicistat 本身也沒有抗病毒活性，在 HIV 領域已是既有用途。

**若要推進需要：**
- 補齊 Cobicistat 的作用機轉資料（MOA）。
- 取得香港衛生署仿單，確認警語、禁忌症與核准適應症。
- 若仍想探索，應先改用人類疾病為標的，重新篩選預測結果，並進行系統性文獻檢索。
- 對神經發育障礙一項，需先提出可驗證的機轉假說，再評估交互作用與安全負擔。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

