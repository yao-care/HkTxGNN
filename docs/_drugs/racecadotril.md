---
layout: default
title: Racecadotril
parent: 僅模型預測 (L5)
nav_order: 751
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Racecadotril：預測新適應症為高澱粉酶血症 (Hyperamylasemia)（證據等級 L5）。原適應症：急性腹瀉"
monitor_inn: "Racecadotril"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder", "septicemic plague", "acute cystitis (disease)"]
---

# Racecadotril
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

# Racecadotril：從急性腹瀉到高澱粉酶血症

## 一句話總結

Racecadotril 是一種腸道抗分泌藥物，原本用於治療急性腹瀉。
TxGNN 模型預測它可能對**高澱粉酶血症 (Hyperamylasemia)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬於模型的圖譜推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性腹瀉 |
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia) |
| TxGNN 預測分數 | 97.72% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏經正式整理的作用機轉資料。就已知資訊，Racecadotril 是 thiorphan 的前驅藥物（prodrug），thiorphan 為腦啡肽酶（enkephalinase／neprilysin）抑制劑，可減少腸道的過度分泌，因此用於急性腹瀉。

然而，腸道分泌過多與血中澱粉酶升高之間，並沒有已知的機轉關聯。目前找不到 Racecadotril 或 thiorphan 與澱粉酶調節、胰臟酵素代謝相關的證據。

這個預測分數雖高，但僅來自知識圖譜中的相鄰關係，**不應視為有生物學依據的假說**。同一批預測中的其他疾病（如多株性高黏滯症候群、先天性無白蛋白血症、敗血性鼠疫、急性膀胱炎等）也同樣缺乏機轉支持，顯示這些結果較可能是圖譜結構造成的假象。

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
| HK-59223 | HIDRASEC CAP 100MG | 膠囊 | 資料未提供 |
| HK-59228 | HIDRASEC GRANULES FOR ORAL SUSPENSION 10MG/SACHET | 口服懸液用顆粒 | 資料未提供 |
| HK-59227 | HIDRASEC GRANULES FOR ORAL SUSPENSION 30MG/SACHET | 口服懸液用顆粒 | 資料未提供 |

三張許可證皆為單一成分製劑，狀態有效，持證商為 ABBOTT LAB LTD。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測，沒有任何臨床試驗、文獻或可信的機轉連結支持用於高澱粉酶血症，證據等級為 L5。
- 高澱粉酶血症通常是其他疾病（如胰臟炎等）的實驗室表現，而非獨立的治療標的，作為藥物再利用目標的價值有限。

**若要推進需要：**
- 補齊 Racecadotril 的作用機轉資料，並確認是否與澱粉酶或胰臟酵素代謝有任何關聯
- 進行系統性文獻回顧，確認是否有相關的前臨床或觀察性研究
- 取得香港仿單的核准適應症、警語與禁忌，以完成安全性篩選
- 在有任何機轉或實證線索之前，建議優先評估其他預測結果，或回頭檢視模型預測的合理性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

