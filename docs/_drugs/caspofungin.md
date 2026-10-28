---
layout: default
title: Caspofungin
parent: 僅模型預測 (L5)
nav_order: 168
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Caspofungin：預測新適應症為胃泌素分泌異常 (Gastrin Secretion Abnormality)（證據等級 L5）。原適應症：食道念珠菌症、念珠菌血症"
monitor_inn: "CASPOFUNGIN"
predicted_indications: ["gastrin secretion abnormality"]
---

# Caspofungin
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

## Caspofungin：從食道念珠菌症與念珠菌血症到胃泌素分泌異常
{: .text-alpha }

## 一句話總結

Caspofungin 是一種抗黴菌藥物，原本用於治療食道念珠菌症 (esophageal candidiasis) 與念珠菌血症 (candidemia)。
TxGNN 模型預測它可能對**胃泌素分泌異常 (Gastrin Secretion Abnormality)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 食道念珠菌症、念珠菌血症 |
| 預測新適應症 | 胃泌素分泌異常 (Gastrin Secretion Abnormality) |
| TxGNN 預測分數 | 0.9944 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的藥理知識，Caspofungin 屬於 echinocandin 類抗黴菌藥物，作用是抑制黴菌細胞壁的 β-(1,3)-D-glucan 合成酶。這個標的在哺乳動物細胞中並不存在。

就目前資料而言，**找不到**連結 Caspofungin 與胃泌素調控（如 G 細胞功能、CCK2 受體訊號或胃酸分泌）的已知機轉。原適應症（食道念珠菌症）屬於消化道感染，而新適應症屬於胃腸內分泌異常，兩者在病理上並無明確關聯。

0.9944 的預測分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。解讀時應保守。

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
| HK-66617 | CASPOVITAE POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 70MG | 未提供 | 未提供 |
| HK-66616 | CASPOVITAE POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 50MG | 未提供 | 未提供 |

兩張許可證皆為單方、有效狀態，持證商為 HONG KONG MEDICAL SUPPLIES LTD。

---

## 安全性考量

- **知識圖譜標示的相關疾病風險**（來自藥物－疾病禁忌關聯，非仿單內容）：肝臟疾病、膽囊疾病、鉀缺乏症。
- **藥物交互作用**：共查得 81 筆交互作用，主要包括：
  - **重大 (Major)**：Dexamethasone
  - **中度 (Moderate)**：Naltrexone
  - 另有多筆等級未明的交互作用，例如 Amphotericin B、Vancomycin、Simvastatin、Prednisone、Hydrocortisone、Prednisolone、Potassium chloride 等。

其餘警語與禁忌症資料不足，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有模型預測（L5），沒有臨床試驗或文獻佐證。
- 缺乏機轉依據，Caspofungin 的作用標的不存在於哺乳動物細胞，預測分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

**若要推進需要：**
- 補齊香港衛生署仿單中的警語與禁忌症資料，完成安全性篩查。
- 補充 DrugBank 的作用機轉資料，並評估是否存在任何生物學上的合理連結。
- 以文獻或前臨床研究，檢驗 Caspofungin 與胃泌素調控之間是否有關聯。
- 確認給藥途徑的相容性（Caspofungin 為靜脈輸注劑型）與目標疾病的臨床需求。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

