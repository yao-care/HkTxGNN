---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 447
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Hydroxocobalamin：預測新適應症為食道靜脈曲張伴出血 (Esophageal varices with bleeding)（證據等級 L5）。原適應症：維生素 B12 缺乏、氰化物中毒、惡性貧血"
monitor_inn: "HYDROXOCOBALAMIN"
predicted_indications: ["esophageal varices with bleeding", "esophageal varices without bleeding"]
---

# Hydroxocobalamin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Hydroxocobalamin：從維生素 B12 缺乏到食道靜脈曲張
{: .text-alpha }

## 一句話總結

Hydroxocobalamin（羥鈷胺素）是維生素 B12 的一種形式，原本用於治療維生素 B12 缺乏、惡性貧血與氰化物中毒。
TxGNN 模型預測它可能對**食道靜脈曲張（伴出血／未出血）**有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 維生素 B12 缺乏、氰化物中毒、惡性貧血 |
| 預測新適應症 | 食道靜脈曲張伴出血 (Esophageal varices with bleeding)；食道靜脈曲張未出血 (Esophageal varices without bleeding) |
| TxGNN 預測分數 | 99.23% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Hydroxocobalamin 是鈷胺素（維生素 B12）的一種形式，用於矯正 B12 缺乏，並能結合氰化物以解毒。

這兩種作用與門脈高壓、靜脈曲張的病理生理或止血機制，**目前沒有已確立的關聯**。理論上，它可能清除一氧化氮而提高血管張力，但這只是推測，缺乏證據支持。而且這方向與治療目標相反：靜脈曲張治療要降低門脈壓，Hydroxocobalamin 已知可能使血壓上升。

兩個預測適應症的分數完全相同（99.23%），顯示模型可能是在疾病母概念層級做預測，而非捕捉到特定訊號。高分可能來自網路鄰近性的假象，例如與肝病或貧血的共同連結。因此，這個高分不應被視為療效的證據。

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
| HK-62101 | CYANOKIT POWDER FOR SOLUTION FOR INFUSION 5G | 未提供 | 未提供 |
| HK-18055 | HYCOBAL INJ 5MG/2ML | 未提供 | 未提供 |
| HK-18525 | HEPATOSWISS FOR IV INFUSION INJ | 未提供 | 未提供 |
| HK-18057 | HEPATOSWISS IM INJ | 未提供 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：高血壓相關疾病（hypertensive disorder、hypertension）。這來自知識圖譜的藥物－疾病關係，並非仿單內容。
- **藥物交互作用**：共查得 32 筆，以下僅列出已有分級者與部分代表：
  - 中度：Arsenic trioxide、Chloramphenicol、Iodide I-131、Iodide I-123
  - 分級未知：Omeprazole、Lansoprazole、Simvastatin、Prednisolone、Acetylsalicylic acid、Folic acid 等

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自圖模型，沒有臨床試驗或文獻支持（證據等級 L5），也找不到合理的機轉連結。
- Hydroxocobalamin 可能升高血壓，與靜脈曲張降低門脈壓的治療目標方向相反，且知識圖譜已將高血壓列為禁忌。

**若要推進需要：**
- 補齊作用機轉資料，並釐清是否存在與門脈高壓或止血相關的路徑
- 進行系統性文獻檢索，確認是否有任何臨床或前臨床證據
- 取得香港仿單的警語與禁忌資料，以進行安全性篩選
- 在有任何機轉或前臨床依據之前，不建議投入進一步開發資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

