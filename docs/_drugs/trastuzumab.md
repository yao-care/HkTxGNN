---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 896
evidence_level: L5
indication_count: 6
monitor_inn: "TRASTUZUMAB"
predicted_indications: ["malignant cutaneous granular cell skin tumor", "ectomesenchymoma", "human herpesvirus 8-related tumor", "middle ear neuroendocrine tumor", "kidney pelvis sarcomatoid transitional cell carcinoma", "prostatic urethra urothelial carcinoma"]
last_modified_at: 2026-10-28
description: "Trastuzumab：預測新適應症為惡性皮膚顆粒細胞瘤 (malignant cutaneous granular cell skin tumor)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Trastuzumab
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

## Trastuzumab: 惡性皮膚顆粒細胞瘤 (malignant cutaneous granular cell skin tumor)
{: .text-alpha }

## 一句話總結

Trastuzumab 是一種針對 HER2 的藥物，在知識圖譜中記錄的原適應症為 HER2 陽性乳癌。
TxGNN 模型預測它可能對**惡性皮膚顆粒細胞瘤 (malignant cutaneous granular cell skin tumor)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 惡性皮膚顆粒細胞瘤 (malignant cutaneous granular cell skin tumor) |
| TxGNN 預測分數 | 0.9948 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 13 張／共 13 張） |
| 許可證數 | 13 張（有效 13 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Trastuzumab 是靶向 HER2（ERBB2）的單株抗體，在 HER2 陽性乳癌中的角色已被知識圖譜記錄，但尚無資料說明它如何作用於這個新適應症。

惡性皮膚顆粒細胞瘤是罕見腫瘤，目前沒有已確立的 HER2 依賴性。這個預測僅來自 TxGNN 的高分（0.9948），沒有任何臨床或文獻資料佐證。若要建立合理的機轉依據，必須先確認該腫瘤是否有 HER2 表現或擴增。

其他排名較前的預測（如 ectomesenchymoma、HHV-8 相關腫瘤、中耳神經內分泌腫瘤）同樣缺乏 HER2 相關證據。排名較後的泌尿上皮癌（腎盂肉瘤樣移行細胞癌、前列腺尿道泌尿上皮癌）因部分泌尿上皮癌有 HER2 過度表現，生物學上相對較有討論空間，但目前同樣沒有試驗或文獻支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

以下列出 5 張主要許可證，其核准適應症文字在資料中未提供：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-64165 | HERCEPTIN 皮下注射液 600MG/5ML | 羅氏（Roche） |
| HK-50618 | HERCEPTIN 注射用粉末 150MG | 羅氏（Roche） |
| HK-67312 | TRAZIMERA 輸注濃縮液用粉末 150MG | 輝瑞（Pfizer） |
| HK-66513 | HERZUMA 輸注濃縮液用粉末 150MG | Celltrion |
| HK-66599 | KANJINTI 輸注濃縮液用粉末 150MG | 安進（Amgen） |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗 HER2 單株抗體） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：資料共收錄 94 筆交互作用。其中列為嚴重（Major）的包括 Deferiprone、Samarium (153Sm) lexidronam、Adalimumab、Baricitinib；列為中度（Moderate）的包括 Warfarin、Dicoumarol、Paclitaxel、Zidovudine、Azathioprine、Alemtuzumab 等。以上僅為部分清單。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅有模型分數支持，沒有任何直接研究該疾病的臨床試驗或文獻，證據等級為 L5。
- 惡性皮膚顆粒細胞瘤沒有已知的 HER2 依賴性，機轉依據不足。

**若要推進需要：**
- 檢測該腫瘤檢體的 HER2 表現或擴增狀態
- 針對此疾病與 HER2 靶向治療進行系統性文獻與試驗檢索
- 取得 Trastuzumab 的作用機轉資料與完整原廠仿單（警語、禁忌症）
- 若 HER2 證據不足，可改為優先評估泌尿上皮癌類（如腎盂肉瘤樣移行細胞癌、前列腺尿道泌尿上皮癌）作為較合理的研究問題
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

