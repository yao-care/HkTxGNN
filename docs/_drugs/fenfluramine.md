---
layout: default
title: Fenfluramine
parent: 僅模型預測 (L5)
nav_order: 368
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Fenfluramine：預測新適應症為16p11.2 近端微缺失症候群 (proximal 16p11.2 microdeletion syndrome)（證據等級 L5）。原適應症：肥胖症、單基因肥胖"
monitor_inn: "FENFLURAMINE"
predicted_indications: ["proximal 16p11.2 microdeletion syndrome", "hypervitaminosis", "obsolete hypertelorism (disease)", "frontorhiny"]
---

# Fenfluramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Fenfluramine：從肥胖症到 16p11.2 近端微缺失症候群

## 一句話總結

Fenfluramine 是一種血清素釋放劑，原本用於肥胖症（含單基因肥胖）的治療。
TxGNN 模型預測它可能對**16p11.2 近端微缺失症候群 (proximal 16p11.2 microdeletion syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測，屬於假說階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肥胖症、單基因肥胖（來自知識圖譜的適應症資料；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 16p11.2 近端微缺失症候群 (proximal 16p11.2 microdeletion syndrome) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（本報告彙整的資料中未收錄 MOA）。依藥理常識，fenfluramine 是血清素釋放劑，具有 5-HT2C／5-HT2A 促效作用，並可調節 sigma-1 受體。這些推論屬假說層級，並非來自本次彙整的臨床證據。

16p11.2 近端微缺失（涵蓋 SH2B1 基因）與肥胖有關，也常伴隨癲癇與自閉症譜系特徵。這與 fenfluramine 原本的抗肥胖用途，以及其在癲癇症候群（如 Dravet 與 Lennox-Gastaut 症候群）的應用有部分重疊，因此模型預測在機轉上有可能成立。

但必須強調：此關聯目前只有計算預測，沒有任何試驗或文獻佐證。此外，5-HT2B 促效作用相關的心臟瓣膜病變與肺高壓風險，是此藥物不容忽視的安全疑慮。

同一份預測清單中的其他候選（hypervitaminosis、obsolete hypertelorism、frontorhiny）皆未找到合理的機轉連結，高分很可能是知識圖譜結構造成的假象，不建議推進。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68504 | FINTEPLA ORAL SOLUTION 2.2MG/ML | 口服液劑（依品名） | 資料未載明 |

製造商／持證商：UCB Pharma (Hong Kong) Limited。

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物與疾病的關聯資料，並非仿單文字）：高血壓、肺動脈高壓、物質濫用／依賴、第 1 型與第 2 型糖尿病、糖尿病酮酸中毒、青光眼。
- **藥物交互作用**：已查詢到 100 筆，以下為部分範例。
  - **嚴重 (Major)**：Fentanyl、Dextromethorphan、Tramadol、Alfentanil、Almotriptan
  - **中度 (Moderate)**：Abciximab、Abiraterone、Acalabrutinib、Acarbose、Codeine、Dihydrocodeine、Formoterol、Ketorolac、Ibuprofen、Salbutamol、Ethanol、Alogliptin、Pioglitazone 等
  - 嚴重交互作用多為鴉片類與血清素相關藥物，需留意血清素症候群與中樞神經抑制風險。
- 其他警語與正式禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 模型分數雖高（99.93%），但沒有任何臨床試驗或文獻支持，證據等級僅為 L5。
- 仿單警語與 MOA 資料缺失，且該藥有心臟瓣膜病變與肺高壓的已知風險，目前不宜推進。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症資料
- 補充完整的作用機轉（MOA）資料
- 系統性檢索 16p11.2 微缺失症候群與 fenfluramine 的臨床前研究、病例報告及試驗登記
- 若有初步證據，需設計含心臟超音波追蹤的安全性監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

