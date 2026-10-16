---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 376
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Filgrastim：預測新適應症為血小板釋放障礙 (Primary release disorder of platelets)（證據等級 L5）。原適應症：體質性嗜中性白血球低下症、嚴重先天性嗜中性白血球低下症、週期性造血異常、慢性家族性嗜中性白血球低下症"
monitor_inn: "FILGRASTIM"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia"]
---

# Filgrastim
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

# Filgrastim：從先天性嗜中性白血球低下症到血小板釋放障礙

## 一句話總結

Filgrastim 是重組 G-CSF（顆粒球群落刺激因子）類似物，原本用於治療體質性及嚴重先天性嗜中性白血球低下症等疾病。
TxGNN 模型預測它可能對**血小板釋放障礙 (Primary release disorder of platelets)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 體質性嗜中性白血球低下症、嚴重先天性嗜中性白血球低下症、週期性造血異常、慢性家族性嗜中性白血球低下症（來自知識圖譜，非仿單） |
| 預測新適應症 | 血小板釋放障礙 (Primary release disorder of platelets) |
| TxGNN 預測分數 | 99.998% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Filgrastim 是重組 G-CSF 類似物，透過 G-CSF 受體作用於嗜中性白血球譜系，促進其增生與分化，這也是它用於嗜中性白血球低下症的基礎。

血小板釋放障礙屬於血小板功能的質性缺陷，與 G-CSF 訊號之間**沒有已確立的直接機轉連結**。0.99998 的高分是圖譜模型的運算結果，可能來自血液學領域中相近的網路節點，而非生物學上的理由。

其他排名前列的預測也有類似情形：

| 排名 | 預測疾病 | 分數 | 機轉評估 |
|------|---------|------|---------|
| 2 | 假性血管性血友病 (Pseudo-von Willebrand disease) | 99.997% | 病因為血小板 GPIb-alpha 功能增強，G-CSF 無已知作用 |
| 3 | Glanzmann 血小板無力症 | 99.996% | 為整合素 αIIbβ3 缺陷，Filgrastim 無法矯正 |
| 4 | Scott 症候群 | 99.956% | 為 TMEM16F/ANO6 缺陷，與 G-CSF 訊號無已知關聯 |
| 5 | 體質性血小板低下所致出血性疾病 | 99.911% | 五項預測中生物學上最相近（共同的造血背景），但 Filgrastim 並無已知的血小板生成作用 |

這五項預測均無臨床試驗或文獻支持。

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
| HK-45427 | NEUPOGEN PRE-FILLED SYRINGE 0.3MG/0.5ML（Amgen） | 預充填注射劑 | 未提供 |
| HK-60951 | NIVESTIM 300MCG/0.5ML 預充填注射劑（Pfizer） | 預充填注射劑 | 未提供 |
| HK-64300 | ZARZIO 48MU/0.5ML 預充填注射劑（Sandoz） | 預充填注射劑 | 未提供 |
| HK-35878 | NEUPOGEN INJ 0.3MG/ML（Amgen） | 注射劑 | 未提供 |
| HK-68517 | ACCOFIL 30MU/0.5ML 預充填注射劑（Jacobson Marketing） | 預充填注射劑 | 未提供 |

以上列出 5 張主要許可證，共 8 張，均為有效的單一成分製劑。

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為部分中度（Moderate）交互作用藥物：
  - 放射性藥物與放射免疫治療：Iobenguane (I-131)、Fludeoxyglucose (18F)、Ibritumomab tiuxetan、Tositumomab (I-131)、Tositumomab
  - 化療及抗腫瘤藥物：Paclitaxel、Mercaptopurine、Trimetrexate、Abemaciclib、Azacitidine、Bendamustine、Arsenic trioxide
  - 其他：Levamisole、Aldesleukin、Alemtuzumab、Acalabrutinib

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 五項預測均僅有模型分數，沒有臨床試驗與文獻，證據等級為 L5。
- 預測疾病的病理（血小板功能或生成缺陷）與 G-CSF 作用於嗜中性白血球的機轉缺乏已知連結，生物學合理性不足。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並進行機轉連結分析。
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選。
- 進行系統性文獻檢索，確認是否有 G-CSF 與血小板疾病的前臨床或病例資料。
- 若要優先驗證，可從「體質性血小板低下所致出血性疾病」著手，因其機轉相近程度相對較高。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

