---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 552
evidence_level: L5
indication_count: 9
monitor_inn: "MANNITOL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "central core myopathy"]
last_modified_at: 2026-10-23
description: "Mannitol：預測新適應症為腎因性抗利尿不適當症候群 (NSIAD)（證據等級 L5）。原適應症：知識圖譜記錄的相關用途：充血性心衰竭、腦水腫、眼壓過高、假性腦瘤、顱內高壓、囊性纖維化"
---

# Mannitol
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

## Mannitol：從腦水腫與顱內高壓到腎因性抗利尿不適當症候群
{: .text-alpha }

## 一句話總結

Mannitol（甘露醇）是一種滲透性利尿劑，知識圖譜中記錄的相關用途包括腦水腫、顱內高壓、眼壓過高等。
TxGNN 模型預測它可能對**腎因性抗利尿不適當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇**一般性的低血鈉評估綜述，且該文並未評估甘露醇，因此證據非常薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的相關用途：充血性心衰竭、腦水腫、眼壓過高、假性腦瘤、顱內高壓、囊性纖維化（香港許可證未提供核准適應症文字，故無法確認核准範圍） |
| 預測新適應症 | 腎因性抗利尿不適當症候群 (NSIAD) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 核准許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知甘露醇屬於滲透性利尿劑，理論上，滲透負荷可能促進自由水排出，這是此預測唯一可能的機轉連結。

NSIAD 是 V2 受體功能增強所造成的水分滯留與低血鈉。然而甘露醇也可能透過水分位移效應使低血鈉惡化，因此這個連結只是推測，安全方向也不確定。TxGNN 模型（深度學習）的高分可能反映模型學到的相關疾病之間的相似性，不是生物學證據，不能視為療效證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | 說明低血鈉評估的十大常見陷阱，強調診斷病因與避免治療不足或過度矯正；並未評估甘露醇 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-21527 | OSMITROL (MANNITOL) INJ 20% "VIAFLEX" | 未提供 | 未提供 |
| HK-28237 | OSMOFUNDIN IV INFUSION 20% | 未提供 | 未提供 |
| HK-43086 | NEUROLITE FOR INJ WITH BUFFER VIAL | 未提供 | 未提供 |

---

## 安全性考量

- **知識圖譜中記錄的禁忌關聯（非仿單文字）**：肝衰竭、肝病、肝性腦病變／肝昏迷、無尿、腎功能受損、肺水腫、顱內出血、血小板低下、嗜中性白血球低下、顆粒球缺乏、貧血、紫質症、睡眠呼吸中止症、物質濫用／依賴等。
- **藥物交互作用**：資料庫共查得 100 筆，以下為部分例子：
  - 重大：Amikacin
  - 中度：Lamivudine、Formoterol、Salbutamol、Captopril、Benazepril、Carbamazepine、Citalopram、Dapagliflozin、Canagliflozin 等
  - 輕微：Doxycycline
- **與此預測相關的特別疑慮**：甘露醇的滲透利尿作用可能加重水分與電解質失衡，用於 NSIAD 的安全性方向不明。

完整警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，唯一的文獻是未評估甘露醇的一般性低血鈉綜述，沒有直接研究此疾病的證據，故證據等級為 L5。
- 機轉上屬推測，且甘露醇可能使低血鈉惡化，安全性方向不明。

**若要推進需要：**
- 取得甘露醇的作用機轉資料與香港仿單中的警語、禁忌。
- 進行針對 NSIAD 的機轉與安全性文獻回顧，並評估對血鈉與水分平衡的影響。
- 若仍有價值，先以前臨床或小型探索性研究驗證，再考慮臨床試驗。

---

### 附註：其他預測適應症的簡要觀察

| 預測適應症 | TxGNN 分數 | 證據 | 觀察 |
|-----------|-----------|------|------|
| 急性肺心病 | 0.9988 | 6 篇間接文獻（含 1977 年高張甘露醇用於 ARDS 的小型臨床研究） | 沒有直接研究此疾病的文獻；甘露醇也可能因容積擴張引發肺水腫（1976 年病例），證據應視為 L5 |
| 運動誘發惡性高熱 | 0.9986 | 無 | 無合理機轉 |
| 家族性週期性麻痺 | 0.9975 | 2 篇文獻 | 僅為病例報告與處置綜述，甘露醇至多作為輔助用途 |
| 低血鉀週期性麻痺 | 0.9972 | 3 篇文獻 | 同上，無對照試驗，不直接治療疾病本身 |
| 腎因性尿崩症 | 0.9970 | 1 篇不相關病例報告 | 甘露醇預期會加重自由水流失，具安全疑慮 |
| 先天性多核心肌病、多小核心病、中央軸空肌病 | 0.9969–0.9971 | 無 | 僅為 TxGNN 模型（深度學習）從相關疾病學到的相似性，不是生物學證據，無支持證據 |

整體而言，上述預測目前都沒有直接研究該疾病的證據，皆建議維持 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

