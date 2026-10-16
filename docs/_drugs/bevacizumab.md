---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Bevacizumab：預測新適應症為會厭腫瘤 (Epiglottis Neoplasm)（證據等級 L5）。原適應症：腹膜癌、原發性腹膜漿液性癌、卵巢惡性上皮腫瘤、乳癌、大腸轉移性惡性腫瘤、神經膠母細胞瘤等"
---

# Bevacizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Bevacizumab：從卵巢／乳房／腦部腫瘤到會厭腫瘤

## 一句話總結

Bevacizumab 是抗血管內皮生長因子（VEGF）的單株抗體，原本用於腹膜癌、卵巢癌、乳癌、大腸轉移癌與神經膠母細胞瘤等癌症。
TxGNN 模型預測它可能對**會厭腫瘤 (Epiglottis Neoplasm)** 有效，但目前**沒有臨床試驗與文獻**直接支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 腹膜癌、原發性腹膜漿液性癌、卵巢惡性上皮腫瘤、乳癌、大腸轉移性惡性腫瘤、神經膠母細胞瘤等（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 會厭腫瘤 (Epiglottis Neoplasm) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Bevacizumab 是抗 VEGF-A 的單株抗體，可阻斷腫瘤血管新生。它在多種實體癌（卵巢、乳房、大腸、腦部）已有使用，機轉上可能也適用於頭頸部腫瘤。

會厭屬於頭頸部。頭頸部腫瘤同樣依賴血管新生，因此從抗血管生成的角度，這個預測有其合理性。不過這只是機轉上的推論，並沒有針對會厭腫瘤的試驗或文獻佐證。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67028 | MVASI 注射濃縮液 100mg/4ml（Amgen） | 輸注用濃縮液 | 資料中未載明 |
| HK-59450 | AVASTIN ROCHE 注射濃縮液 100mg/4ml（Roche） | 輸注用濃縮液 | 資料中未載明 |
| HK-67029 | MVASI 注射濃縮液 400mg/16ml（Amgen） | 輸注用濃縮液 | 資料中未載明 |
| HK-56638 | AVASTIN ROCHE 注射液 100mg/4ml（Roche） | 注射劑 | 資料中未載明 |
| HK-56637 | AVASTIN ROCHE 注射液 400mg/16ml（Roche） | 注射劑 | 資料中未載明 |

（全部共 6 張有效許可證，另有 HK-59449 AVASTIN ROCHE 400mg/16ml 輸注用濃縮液。）

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗 VEGF 單株抗體），非傳統細胞毒性藥物 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：已查得 22 項交互作用，主要包括：
  - **嚴重 (Major)**：Deferiprone、Samarium (153Sm) lexidronam、Panitumumab、Sunitinib、Thalidomide
  - **中度 (Moderate)**：多種雙磷酸鹽類（Alendronic acid、Risedronic acid、Etidronic acid、Ibandronate、Pamidronic acid、Tiludronic acid）、Filgrastim、Pegfilgrastim、Sargramostim、Palifermin、Idelalisib、Romosozumab、Radium Ra 223 dichloride、Strontium chloride Sr-89 等

警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 會厭腫瘤的預測分數雖高（99.90%），但沒有任何臨床試驗或文獻支持，證據等級僅 L5。
- 作用機轉與仿單安全性資料也尚未取得。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與核准適應症
- 補充 Bevacizumab 的作用機轉資料
- 搜尋頭頸部（含喉、會厭）腫瘤使用抗 VEGF 治療的臨床與文獻證據
- 確認會厭腫瘤的疾病定義（良性或惡性），並評估與既有適應症的相似性
- 若評估其他預測適應症，可優先看「囊性腫瘤 (Cystic Neoplasm)」（L3，有 Phase 3 試驗與系統性回顧），但其證據多與已核准的卵巢癌用途重疊，未必構成真正的再利用證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

