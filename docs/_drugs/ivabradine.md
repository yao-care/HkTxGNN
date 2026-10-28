---
layout: default
title: Ivabradine
parent: 僅模型預測 (L5)
nav_order: 493
evidence_level: L5
indication_count: 6
monitor_inn: "IVABRADINE"
predicted_indications: ["hypertrichosis (disease)", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "nephrogenic syndrome of inappropriate antidiuresis"]
last_modified_at: 2026-10-28
description: "Ivabradine：預測新適應症為多毛症 (Hypertrichosis)（證據等級 L5）。原適應症：許可證資料中未載明核准適應症"
---

# Ivabradine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Ivabradine：從原適應症資料缺漏到毛髮過多症（hypertrichosis）
{: .text-alpha }

## 一句話總結

Ivabradine 是一種 HCN 通道（If 電流）抑制劑，在香港已有 10 張有效許可證，但本報告所整理的資料中沒有記載其核准適應症文字。
TxGNN 模型預測它可能對**多毛症 (Hypertrichosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料中未載明核准適應症 |
| 預測新適應症 | 多毛症 (Hypertrichosis) |
| TxGNN 預測分數 | 0.9979 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 10 張／共 10 張） |
| 許可證數 | 10 張（有效 10 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏經本報告資料確認的詳細作用機轉。已知 Ivabradine 為選擇性 HCN 通道（If 電流）抑制劑，作用於竇房結以降低心率。

毛髮過多症與 Ivabradine 的唯一連結，是 TxGNN 模型（深度學習）的計算預測（分數 0.9979）。HCN 通道雖可能在毛囊相關組織表現，但這屬於推測，缺乏資料支持。此分數來自 TxGNN 模型（深度學習），可能反映模型在相關疾病之間學到的相似性，而非生物學證據；高分較可能反映與遺傳性症候群的相似性，而非藥理學上的合理性。因此，這個預測目前**不具備可說明的機轉依據**。

其他排名靠前的預測（皆為 L5、無任何試驗或文獻）：

| 排名 | 預測疾病 | TxGNN 分數 | 說明 |
|------|---------|-----------|------|
| 2 | Ambras 型先天性全身性多毛症 | 0.9972 | 與 TRPS1 調控異常相關，與 HCN 抑制無已知關聯 |
| 3 | 伴有牙齒／牙周異常的畸形症候群 | 0.9972 | 類別過於異質，無法作為單一標的評估 |
| 4 | 以 Dandy-Walker 畸形為主要特徵的症候群 | 0.9970 | 結構性先天缺陷，降心率機轉不預期能矯正 |
| 5 | 孤立性遺傳性毛幹異常 | 0.9969 | 多為結構或角蛋白缺陷，無 HCN 關聯 |
| 6 | 腎因性抗利尿激素不當分泌症候群 | 0.9908 | 與 AVPR2 活化突變相關，Ivabradine 不作用於此路徑 |

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

下列 10 張許可證均為單一成分製劑、狀態有效。資料中未載明劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-55438 | CORALAN TAB 7.5MG | SERVIER HONG KONG LIMITED |
| HK-55439 | CORALAN TAB 5MG | SERVIER HONG KONG LIMITED |
| HK-68232 | IVACORD 5 TABLETS 5MG | JACOBSON MARKETING LIMITED |
| HK-68233 | IVACORD 7.5 TABLETS 7.5MG | JACOBSON MARKETING LIMITED |
| HK-68712 | IVABRADINE TABLETS 5MG | CHEMILL PHARMA LIMITED |

另有 5 張許可證（HK-68713、HK-68765、HK-68766、HK-68861、HK-68862），分別由 Chemill Pharma、SB Pharma 與 Sandoz Hong Kong 持有，此處僅列出前 5 張主要許可證。

## 安全性考量

- **藥物交互作用**：資料庫共記錄 100 筆交互作用，以下為部分範例。
  - **嚴重 (Major)**：Aprepitant、Clarithromycin、Dolasetron、Palonosetron、Cisapride、Clotrimazole、Granisetron、Levofloxacin、Ondansetron、Papaverine、Cobicistat
  - **中度 (Moderate)**：Famotidine、Ranitidine、Dexamethasone、Cimetidine、Metreleptin、Miconazole、Nizatidine、Troglitazone

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型計算，沒有任何臨床試驗或文獻直接研究 Ivabradine 用於多毛症，證據等級為 L5。
- 作用機轉（降低心率的 HCN 抑制）與多毛症缺乏可辨識的生物學關聯，且六個預測疾病多為罕見遺傳或先天性疾病，不易進行臨床研究。

**若要推進需要：**
- 補齊香港許可證的核准適應症與仿單警語、禁忌症
- 取得詳細的作用機轉資料，並以實驗或文獻檢驗 HCN 通道與毛囊生物學的關聯
- 進行前臨床研究（如毛囊模型），再評估是否有進一步開發的價值
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

