---
layout: default
title: Ruxolitinib
parent: 僅模型預測 (L5)
nav_order: 793
evidence_level: L5
indication_count: 10
monitor_inn: "RUXOLITINIB"
predicted_indications: ["uterine corpus perivascular epithelioid cell tumor", "benign PEComa", "lymphangiomyoma", "lymphangioleiomyomatosis", "liposarcoma", "familial rhabdoid tumor", "lung PEComa", "ovarian myxoid liposarcoma", "hemophagocytic syndrome associated with an infection", "acquired hemophagocytic lymphohistiocytosis associated with malignant disease"]
last_modified_at: 2026-10-28
description: "Ruxolitinib：預測新適應症為子宮體血管周上皮樣細胞腫瘤（證據等級 L5）。原適應症：香港許可證資料未載明核准適應症"
---

# Ruxolitinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Ruxolitinib：從骨髓增生性疾病到子宮體血管周上皮樣細胞腫瘤
{: .text-alpha }

## 一句話總結

Ruxolitinib 在知識圖譜中與骨髓纖維化、真性紅血球增多症等骨髓增生性疾病有關聯記錄，香港已有 5 張單一成分許可證。
TxGNN 模型預測它可能對**子宮體血管周上皮樣細胞腫瘤**有效，預測分數很高，但目前**沒有任何臨床試驗或文獻**直接支持，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症；知識圖譜記錄的關聯包括骨髓纖維化、真性紅血球增多症、骨髓增生性腫瘤、漿細胞瘤（這是圖譜關聯記錄，不等同核准適應症） |
| 預測新適應症 | 子宮體血管周上皮樣細胞腫瘤 |
| TxGNN 預測分數 | 0.9973 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ruxolitinib 是 JAK1/2 抑制劑，與骨髓增生性疾病在知識圖譜中有關聯記錄。

針對這個預測疾病，可能的連結是血管周上皮樣細胞腫瘤常見 TSC1/TSC2 缺失所致的 mTOR 路徑失調，並可能與 JAK-STAT 訊號有交互作用。這只是推測，所提供的資料中沒有任何研究支持，也無法確認 JAK 抑制能帶來療效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

下列許可證的核准適應症與劑型欄位在本報告所彙整的資料中皆未載明。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68437 | LUMIRIX CREAM 15MG/G | RXILIENT MEDICAL (HONG KONG) LIMITED |
| HK-61973 | JAKAVI TAB 5MG | NOVARTIS PHARMACEUTICALS (HK) LIMITED |
| HK-61972 | JAKAVI TAB 20MG | NOVARTIS PHARMACEUTICALS (HK) LIMITED |
| HK-61974 | JAKAVI TAB 15MG | NOVARTIS PHARMACEUTICALS (HK) LIMITED |
| HK-66148 | JAKAVI TABLETS 10MG | NOVARTIS PHARMACEUTICALS (HK) LIMITED |

## 細胞毒性

預測適應症為腫瘤，此處依標靶藥物類別簡要整理。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（JAK1/2 抑制劑），非傳統細胞毒性化療藥物 |
| 骨髓抑制風險 | 彙整資料提到需留意血球減少，詳細分級請參考原廠仿單 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 請參考原廠仿單（至少應包含血球計數） |
| 處置防護 | 請參考原廠仿單 |

## 安全性考量

- **藥物交互作用**：資料庫共記錄 100 筆，以下僅列出所取得的 20 筆中較重要者。
  - 嚴重（Major）：Clarithromycin、Cobicistat、Deferasirox、Deferiprone、Ibritumomab tiuxetan、Tositumomab、Tositumomab (I-131)、Samarium (153Sm) lexidronam
  - 中等（Moderate）：Dexamethasone、Rosuvastatin、Fenfluramine、Dexfenfluramine、Sibutramine、Troglitazone、Palifermin、Strontium chloride Sr-89

其他安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測只有模型分數，沒有任何直接研究，機轉連結也只是推測。
- 安全性警語與禁忌症資料缺漏，無法進入安全性篩選。

**若要推進需要：**
- 補齊 JAK 抑制與血管周上皮樣細胞腫瘤（含 mTOR 路徑）的機轉資料，以及完整作用機轉。
- 取得香港仿單的警語與禁忌症。
- 進行針對此疾病的臨床前或病例研究。

**其他候選適應症的參考：**
- 同一份預測清單中，**感染相關噬血症候群**（排名第 9）的證據相對充足。已有兒童與成人的 Ruxolitinib 治療研究、回溯性世代研究、病例報告，以及小鼠模型的機轉研究，證據等級為 L3。目前尚無法確認有 RCT。
- 若要優先評估，建議改以該適應症為主軸另行評估。
- 脂肪肉瘤（排名第 5）僅有 2 篇 JAK-STAT 的前臨床機轉研究，且未證實測試過 Ruxolitinib。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

