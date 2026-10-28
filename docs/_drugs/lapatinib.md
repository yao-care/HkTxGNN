---
layout: default
title: Lapatinib
parent: 僅模型預測 (L5)
nav_order: 510
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Lapatinib：預測新適應症為隆突性皮膚纖維肉瘤 (Dermatofibrosarcoma Protuberans)（證據等級 L5）。原適應症：HER2 陽性乳癌 (HER2 positive breast carcinoma)"
monitor_inn: "LAPATINIB"
predicted_indications: ["dermatofibrosarcoma protuberans"]
---

# Lapatinib
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

## Lapatinib：從 HER2 陽性乳癌到隆突性皮膚纖維肉瘤
{: .text-alpha }

## 一句話總結

Lapatinib 原本用於治療 HER2 陽性乳癌。
TxGNN 模型預測它可能對**隆突性皮膚纖維肉瘤 (Dermatofibrosarcoma Protuberans, DFSP)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測的假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HER2 陽性乳癌 (HER2 positive breast carcinoma) |
| 預測新適應症 | 隆突性皮膚纖維肉瘤 (Dermatofibrosarcoma Protuberans) |
| TxGNN 預測分數 | 0.9930 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Lapatinib 屬於 EGFR/HER2 雙重酪胺酸激酶抑制劑，其在 HER2 陽性乳癌中的療效已被證實。

然而，DFSP 的主要病因是 COL1A1-PDGFB 融合基因，會活化 PDGFRB 訊號，這也是 imatinib 對此病有效的基礎。依現有資料，EGFR/HER2 抑制與 DFSP 之間並沒有直接的機轉關聯。

若要建立關聯，只能推測可能經由下游 RTK/PI3K/MAPK 訊號的交互作用，且需要獨立驗證。因此，這項預測目前只能視為假說。

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
| HK-66822 | LAPATINIB TABLETS 250MG | 錠劑（依品名） | 資料未提供 |
| HK-67443 | TYKERB TABLETS 250MG | 錠劑（依品名） | 資料未提供 |
| HK-56194 | TYKERB TAB 250MG | 錠劑（依品名） | 資料未提供 |

---

## 細胞毒性

Lapatinib 為抗腫瘤藥物（標靶藥物，EGFR/HER2 酪胺酸激酶抑制劑）。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單；依下列知識圖譜禁忌疾病，建議留意肝功能、心功能與 QT 間期、電解質（鉀） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（來自模型知識圖譜，非仿單文字）：long QT 症候群、家族性 long QT 症候群、尖端扭轉型心室頻脈 (torsades de pointes)、肝衰竭、缺鉀症、間質性肺病、藥物性肝損傷、心衰竭。
- **藥物交互作用**：資料庫共查得 100 筆，以下為部分範例：
  - **嚴重 (Major)**：Loperamide、Clarithromycin
  - **中度 (Moderate)**：Famotidine、Ranitidine、Cimetidine、Omeprazole、Rabeprazole、Dexlansoprazole（制酸劑與氫離子幫浦抑制劑類）；Dexamethasone、Hydrocortisone、Betamethasone、Triamcinolone、Budesonide（類固醇類）；Aprepitant、Pioglitazone、Saxagliptin 等

仿單層級的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測分數（0.9930），沒有任何臨床試驗或文獻佐證，證據等級為 L5。
- Lapatinib 的 EGFR/HER2 抑制機轉與 DFSP 的 PDGFRB 驅動機轉缺乏直接關聯；DFSP 已有 imatinib 這類更合乎機轉的標靶治療。

**若要推進需要：**
- 取得完整的作用機轉 (MOA) 資料，並釐清 EGFR/HER2 與 DFSP 的潛在關聯。
- 進行文獻與臨床試驗的系統性檢索，並補充前臨床（細胞或動物模型）驗證。
- 取得香港仿單的警語與禁忌資料，完成安全性篩選（尤其是 QT 延長、肝毒性、心功能與間質性肺病風險）。
- 確認劑型與給藥途徑的相容性。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

