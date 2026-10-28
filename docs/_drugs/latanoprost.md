---
layout: default
title: Latanoprost
parent: 僅模型預測 (L5)
nav_order: 513
evidence_level: L5
indication_count: 9
monitor_inn: "LATANOPROST"
predicted_indications: ["visceral calciphylaxis", "hypotrichosis simplex of the scalp", "arterial thoracic outlet syndrome", "venous thoracic outlet syndrome", "neurogenic thoracic outlet syndrome", "congenital hypotrichosis milia", "angiodysplasia of stomach", "blue toe syndrome", "lymphangiectasis"]
last_modified_at: 2026-10-23
description: "Latanoprost：預測新適應症為內臟鈣化防禦症 (Visceral Calciphylaxis)（證據等級 L5）。原適應症：開角型青光眼、高眼壓症"
---

# Latanoprost
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Latanoprost：從開角型青光眼到內臟鈣化防禦症（Visceral Calciphylaxis）
{: .text-alpha }

## 一句話總結

Latanoprost 是前列腺素 F2α 類似物，知識圖譜中記錄的原適應症為開角型青光眼與高眼壓症。
TxGNN 模型預測它可能對**內臟鈣化防禦症 (Visceral Calciphylaxis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 開角型青光眼、高眼壓症（來自知識圖譜記錄的關聯；香港許可證資料未提供適應症文字） |
| 預測新適應症 | 內臟鈣化防禦症 (Visceral Calciphylaxis) |
| TxGNN 預測分數 | 0.9983 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Latanoprost 屬於前列腺素 F2α 類似物，作用於 FP 受體，可促進葡萄膜鞏膜途徑的房水流出，進而降低眼壓。

在機轉上，FP 受體活化可能影響血管張力或血管重塑，因此理論上可與血管相關疾病產生連結。然而，鈣化防禦症的核心病理是血管鈣化與微血管血栓，目前沒有已建立的機轉依據說明 Latanoprost 能改善此狀況。

此外，Latanoprost 為眼用滴劑，全身暴露量極低。高分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。這是一個未經驗證的計算預測。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

以下為已列出的 20 張許可證（總數至少 20 張，清單可能不完整）。僅列出主要 5 張單方製劑：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-42158 | XALATAN EYE DROPS 50UG/ML | 眼用滴劑 | 資料未提供 |
| HK-64160 | XALAPRO EYE DROPS 0.005% W/V | 眼用滴劑 | 資料未提供 |
| HK-61876 | LATANOPROST OPHTHALMIC SOLUTION 0.005% W/V (BAUSCH & LOMB) | 眼用溶液 | 資料未提供 |
| HK-65985 | MONOPOST EYE DROPS 50MCG/ML | 眼用滴劑 | 資料未提供 |
| HK-68041 | LATANOPROST I&C PRESERVATIVE FREE EYE DROPS SOLUTION 50MCG/ML | 眼用滴劑（無防腐劑） | 資料未提供 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單文字）：葡萄膜炎、虹膜疾病、睫狀體疾病、全葡萄膜炎、黃斑部視網膜水腫、囊樣黃斑水腫、虹膜炎、結膜炎、急性傳染性結膜炎。
- **藥物交互作用**：資料庫查詢共 100 筆，已列出的項目包括 Calcitriol、Glimepiride、Doxycycline、Atropine、Metformin、Prednisone、Triamcinolone 等，但交互作用等級皆為未知，臨床意義需另行評估。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究 Latanoprost 於內臟鈣化防禦症，證據等級為 L5，僅有模型預測。
- 機轉上缺乏合理連結，且眼用劑型的全身暴露量低。

**若要推進需要：**
- 系統性檢索 PubMed 與試驗登記資料庫，確認是否有直接證據。
- 取得完整作用機轉資料，並分析 FP 受體與血管鈣化的關聯。
- 取得香港仿單的警語與禁忌資料。
- 評估給藥途徑是否可行（目前為眼用劑型，全身性使用的可行性未知）。
- 若要探索此藥物的新用途，可優先評估機轉上較合理的候選（如毛髮生長相關疾病），但同樣需要先取得外部證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

