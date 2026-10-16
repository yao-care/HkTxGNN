---
layout: default
title: Iopromide
parent: 僅模型預測 (L5)
nav_order: 479
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Iopromide：預測新適應症為退化性關節炎易感性 (osteoarthritis susceptibility)（證據等級 L5）。原適應症：許可證未載明核准適應症（一般為放射影像造影劑）"
monitor_inn: "Iopromide"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "alopecia", "myosclerosis", "hemoglobinopathy", "pseudoachondroplasia"]
---

# Iopromide
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

# Iopromide：從影像診斷造影到退化性關節炎（預測）

## 一句話總結

Iopromide 是含碘的非離子型放射造影劑，在香港以 Ultravist 品名上市，用於影像診斷。
TxGNN 模型預測它可能對**退化性關節炎易感性 (osteoarthritis susceptibility)** 有效，但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明核准適應症（一般為放射影像造影劑） |
| 預測新適應症 | 退化性關節炎易感性 (osteoarthritis susceptibility) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Iopromide 是碘化非離子型造影劑，其作用在於吸收 X 光以增強影像對比，並非藥理上調控疾病路徑。

排名第一的預測（骨關節炎易感性）涉及遺傳易感性，而 Iopromide 對關節組織或相關遺傳路徑沒有已知的藥理作用。排名第二的骨關節炎，可能是因為造影劑被用於關節攝影（arthrography）這類診斷用途，使知識圖譜中出現關聯；但診斷用途不等於疾病修飾療效。

因此，0.996 的高分應解讀為知識圖譜上的鄰近關係，而非具生物學依據的療效訊號。其他前 10 名預測（類風濕性關節炎、短軀幹症 brachyolmia、Hunter-Thompson 型肢中發育不良、禿髮、血紅素病變、假性軟骨發育不全等）同樣沒有機轉依據或實證支持。

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
| HK-43949 | ULTRAVIST 370 INJ 370MGI/ML | 注射劑 | 資料未載明 |
| HK-43948 | ULTRAVIST 300 INJ 300MGI/ML | 注射劑 | 資料未載明 |

兩張許可證皆為單方、有效，持證商為 Bayer Healthcare Limited。

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 筆交互作用，其中多筆為重大（Major）等級，主要例子包括：
  - Metformin（與含碘造影劑併用需留意腎功能與乳酸中毒風險）
  - Amphotericin B（含脂質複合物、膽固醇硫酸酯、脂質體劑型）
  - Mesalazine、Balsalazide、Olsalazine、Sulfasalazine
  - Vancomycin
  - 胺基糖苷類／多黏菌素：Kanamycin、Neomycin、Streptomycin、Polymyxin B
  - 中度等級：Mannitol

主要警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.57%），但沒有任何臨床試驗或文獻佐證，也找不到合理的作用機轉，證據等級僅為 L5。
- Iopromide 是診斷用造影劑，預測的疾病（關節炎、骨骼發育不良、禿髮、血紅素病變等）與其藥理特性不相符，應視為圖譜關聯造成的假陽性可能性較高。

**若要推進需要：**
- 取得 Iopromide 的作用機轉資料，並說明其如何與任何預測疾病建立生物學關聯
- 取得香港仿單的核准適應症、警語與禁忌症
- 進行系統性文獻與試驗檢索，確認是否有任何關節疾病相關的治療性研究
- 若仍有意探索，需先有前臨床研究支持，並評估關節內給藥的可行性與安全性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

