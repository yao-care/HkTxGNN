---
layout: default
title: Orlistat
parent: 僅模型預測 (L5)
nav_order: 646
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Orlistat：預測新適應症為高維生素症 (Hypervitaminosis)（證據等級 L5）。原適應症：肥胖症（obesity disorder）、單基因肥胖（monogenic obesity）"
monitor_inn: "ORLISTAT"
predicted_indications: ["hypervitaminosis"]
---

# Orlistat
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Orlistat：從肥胖症到高維生素症
{: .text-alpha }

## 一句話總結

Orlistat 是胃腸道脂肪酶抑制劑，原本用於肥胖症（obesity disorder）與單基因肥胖（monogenic obesity）的治療。
TxGNN 模型預測它可能對**高維生素症 (Hypervitaminosis)** 有效，
但目前**沒有臨床試驗與文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肥胖症（obesity disorder）、單基因肥胖（monogenic obesity） |
| 預測新適應症 | 高維生素症 (Hypervitaminosis) |
| TxGNN 預測分數 | 0.9942 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 12 張／共 12 張） |
| 許可證數 | 12 張（有效 12 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。依一般藥理知識，Orlistat 是胃及胰臟脂肪酶抑制劑，可使膳食脂肪吸收減少約 30%。

脂溶性維生素（A、D、E、K）需隨膳食脂肪一同吸收，因此 Orlistat 會降低它們的吸收。對於脂溶性維生素過量所致的高維生素症，理論上減少腸道吸收可能略微降低體內維生素負荷，這是模型預測在生物學上的可能依據。

但需要注意：
- 這個效果正好是 Orlistat 平常的安全性疑慮（維生素缺乏，需額外補充），方向相反。
- 只影響脂溶性維生素，對水溶性維生素無效。
- 高維生素症的主要處置是停止維生素來源，Orlistat 的實用價值有限。
- 以上機轉為依一般知識推論，並非來自本報告彙整的資料。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67026 | ODISTAD 120 CAPSULES 120MG | 膠囊（品名標示） | 資料未提供 |
| HK-61889 | ZEROTEX CAPSULE 120MG | 膠囊（品名標示） | 資料未提供 |
| HK-44752 | XENICAL CAP 120MG | 膠囊（品名標示） | 資料未提供 |
| HK-67567 | OLILIO CAPSULES 60MG | 膠囊（品名標示） | 資料未提供 |
| HK-61430 | CUVARLIX CAP 120MG | 膠囊（品名標示） | 資料未提供 |

本藥共有 12 張有效單方許可證，上表僅列出 5 張主要許可證。

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（非仿單內容）：肝衰竭、原發性高草酸尿症、神經性厭食症、神經性暴食症、維生素缺乏症、膽汁淤積（含良性復發性肝內膽汁淤積、家族性肝內膽汁淤積）、藥物性肝損傷。
- **藥物交互作用**：共查得 100 筆交互作用，以下為部分範例：
  - 中度：Abacavir、Lamivudine、Acarbose、Albiglutide、Alogliptin、Metformin、Amiodarone、Atazanavir、Emtricitabine、Canagliflozin 等
  - 輕度：Cholecalciferol、Calcifediol、Calcitriol（皆為維生素 D 類，與本預測適應症相關，需特別留意）

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型（分數 0.9942），沒有任何臨床試驗或文獻佐證，證據等級為 L5。
- 機轉方向與 Orlistat 常見的維生素缺乏風險相反，且高維生素症的標準處置是移除來源，臨床價值不明確。另有 100 筆藥物交互作用，以及多項潛在禁忌疾病（尤其是肝臟與膽汁淤積相關），需審慎看待。

**若要推進需要：**
- 取得 Orlistat 的詳細作用機轉資料（MOA）
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選
- 進行文獻與臨床試驗檢索，確認是否有脂溶性維生素過量的相關研究
- 以前臨床或小規模研究驗證其降低脂溶性維生素負荷的幅度與臨床意義
- 評估與維生素 D 類藥物等交互作用的臨床影響
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

