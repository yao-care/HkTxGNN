---
layout: default
title: Polatuzumab Vedotin
parent: 僅模型預測 (L5)
nav_order: 710
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Polatuzumab Vedotin：預測新適應症為HER2 陽性乳癌 (HER2 positive breast carcinoma)（證據等級 L5）。原適應症：資料未載明"
---

# Polatuzumab Vedotin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Polatuzumab Vedotin：從原適應症（資料未載明）到 HER2 陽性乳癌

## 一句話總結

Polatuzumab vedotin 是一種抗體藥物複合體（ADC），在香港已由羅氏（Roche）取得上市許可，但本次整理的資料未載明其核准適應症。
TxGNN 模型預測它可能對 **HER2 陽性乳癌 (HER2 positive breast carcinoma)** 有效。
目前**沒有臨床試驗和文獻**支持這個方向，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | HER2 陽性乳癌 (HER2 positive breast carcinoma) |
| TxGNN 預測分數 | 99.34% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，Polatuzumab vedotin 是一種靶向 CD79b 的抗體藥物複合體，攜帶破壞微管的 MMAE（monomethyl auristatin E）作為細胞毒性藥物。

CD79b 是 B 細胞受體的組成成分，主要表現於 B 細胞惡性腫瘤，並非 HER2 陽性乳癌的已知靶點。兩者之間唯一可能的連結，是 MMAE 對增生中細胞的一般細胞毒性作用，但這並非特定於此腫瘤類型。

TxGNN 分數雖高（99.34%），但僅是模型預測。現有資料中沒有任何機轉或生物學證據支持 CD79b 與 HER2 陽性乳癌有關，也無法與已整理的標靶資料交叉驗證。因此，這個預測的合理性目前**偏低**，需要進一步的生物學驗證。

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
| HK-66664 | POLIVY POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 140MG | 未載明 | 未載明 |
| HK-67107 | POLIVY POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 30MG | 未載明 | 未載明 |

兩張許可證皆為單一成分製劑，狀態有效，持有者為 ROCHE HONG KONG LIMITED。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗體藥物複合體（ADC），攜帶微管抑制劑 MMAE |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項（一般建議包含 CBC 與肝腎功能） |
| 處置防護 | 請參考原廠仿單；ADC 含細胞毒性成分，一般應依細胞毒性藥物處置規範操作 |

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下列出部分主要項目：
  - **嚴重 (Major)**：Clarithromycin、Cobicistat、Deferiprone、Samarium (153Sm) lexidronam
  - **中度 (Moderate)**：Aprepitant、Cimetidine、Naltrexone、Metronidazole、Miconazole、Rosuvastatin、Simvastatin、Tinidazole、Ticagrelor、Chloroquine、Hydroxychloroquine 等

其他警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測（證據等級 L5），沒有任何臨床試驗或文獻支持。
- 藥物靶點 CD79b 與 HER2 陽性乳癌之間缺乏已知的生物學連結，且作用機轉與原適應症資料皆不完整。

**若要推進需要：**
- 補齊 DrugBank 的作用機轉資料，以及香港許可證的核准適應症與仿單內容
- 評估 CD79b 在 HER2 陽性乳癌中是否表現（組織或細胞株層級的前臨床研究）
- 進行文獻與臨床試驗的系統性檢索，確認是否有尚未納入的證據
- 與現有 HER2 標靶 ADC 比較，釐清此預測相對於既有療法的價值
- 補齊安全性資料後，再進入安全性篩選
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

