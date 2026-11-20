---
layout: default
title: Calcium Glycerophosphate
parent: 僅模型預測 (L5)
nav_order: 148
evidence_level: L5
indication_count: 4
monitor_inn: "CALCIUM GLYCEROPHOSPHATE"
predicted_indications: ["calcium-alkali syndrome", "primary bone dysplasia with defective bone mineralization", "potassium deficiency disease", "hypophosphatemia (disease)"]
last_modified_at: 2026-10-28
description: "Calcium Glycerophosphate：預測新適應症為鈣鹼症候群 (calcium-alkali syndrome)（證據等級 L5）。香港藥劑製品註冊：2 張（有效 2 張）"
---

# Calcium Glycerophosphate
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

## Calcium Glycerophosphate：鈣與有機磷補充劑 → 鈣鹼症候群 (calcium-alkali syndrome)
{: .text-alpha }

## 一句話總結

Calcium Glycerophosphate（甘油磷酸鈣）是一種同時提供鈣與有機磷的礦物質補充成分。
TxGNN 模型預測它可能與**鈣鹼症候群 (calcium-alkali syndrome)** 相關，但目前**沒有任何臨床試驗或文獻**直接支持這個預測，僅為模型推測，且可能是偽陽性。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 鈣鹼症候群 (calcium-alkali syndrome) |
| TxGNN 預測分數 | 0.9995 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Calcium Glycerophosphate 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「甘油磷酸鈉（sodium glycerophosphate）是一種有機磷酸鹽，可作為磷的來源。以有機及無機磷酸鹽形式存在的磷在所有器官及組織中具有多種生化功能，包括在核酸結構、能量儲存與傳遞、細胞訊息傳遞、細胞膜組成與結構、酸鹼平衡、礦物質恆定及骨骼礦化方面扮演關鍵角色。」英文原文："Sodium glycerophosphate, an organic phosphate salt, functions as a source of phosphorus. Phosphorus in the form of organic and inorganic phosphate has a variety of biochemical functions in all organs and tissues, including critical roles in nucleic acid structure, energy storage and transfer, cell signaling, cell membrane composition and structure, acid-base balance, mineral homeostasis, and bone mineralization."（[DailyMed: Glycophos (sodium glycerophosphate) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e887e473-f1a7-40f1-bd6e-c99e7db7420d)，版本日期 2026-10-08；查閱日期 2026-11-19）。根據已知資訊，甘油磷酸鈣是鈣與有機磷酸鹽的來源，水解後可釋出無機磷，常作為鈣、磷的補充劑。

鈣鹼症候群是因攝取過量的鈣與可吸收的鹼性物質，導致高血鈣、代謝性鹼中毒與腎功能受損。由於甘油磷酸鈣本身是鈣補充劑，理論上較可能**促成**這個疾病，而非治療它。模型給出高分，較可能反映的是網路上與高血鈣等相近概念的距離，而不是真正的治療關係。

因此，這項預測較應視為**潛在的安全性警訊**，而不是值得推進的再利用機會，很可能是偽陽性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-52479 | AMINOLEBAN EN POWDER | 未記載 | 未記載 |
| HK-54177 | AMINOLEBAN ORAL POWDER | 未記載 | 未記載 |

## 安全性考量

- **藥物交互作用**：資料庫共記錄 7 項中度交互作用，包括 Calcitriol（外用）、Calcipotriol（外用）、Levofloxacin、Deferiprone、Tolevamer、Eltrombopag、Estramustine。其中與維生素 D 類似物併用可能增加血鈣上升的風險，而與 Levofloxacin 等藥物則可能因鈣的螯合作用影響吸收，使用時需留意。

其餘警語與禁忌症資料不足，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何直接研究支持，證據等級為 L5。
- 藥物本身供應鈣，機轉上可能加重鈣鹼症候群而非改善，存在安全疑慮。

**若要推進需要：**
- 先釐清此預測是否只是模型的關聯假象（偽陽性）
- 取得詳細的作用機轉資料
- 取得香港仿單的警語與禁忌症資料，完成安全性篩檢
- 若要探索此方向，需先有直接針對鈣鹼症候群的機轉或臨床研究證據

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Glycophos (sodium glycerophosphate) prescribing information, Fresenius Kabi USA, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e887e473-f1a7-40f1-bd6e-c99e7db7420d) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

