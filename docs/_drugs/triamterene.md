---
layout: default
title: Triamterene
parent: 僅模型預測 (L5)
nav_order: 904
evidence_level: L5
indication_count: 5
monitor_inn: "TRIAMTERENE"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-28
description: "Triamterene：預測新適應症為惡性高血壓腎病變 (malignant hypertensive renal disease)（證據等級 L5）。原適應症：知識圖譜中記錄的關聯為高血壓、充血性心臟衰竭"
---

# Triamterene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Triamterene：從高血壓與充血性心臟衰竭到惡性高血壓腎病變
{: .text-alpha }

## 一句話總結

Triamterene 是一種保鉀利尿劑，知識圖譜中記錄的原適應症為高血壓與充血性心臟衰竭。
TxGNN 模型預測它可能對**惡性高血壓腎病變 (malignant hypertensive renal disease)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的關聯為高血壓、充血性心臟衰竭（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 惡性高血壓腎病變 (malignant hypertensive renal disease) |
| TxGNN 預測分數 | 0.9989 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 核准許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Triamterene 一般被歸類為保鉀利尿劑（透過阻斷上皮鈉通道 ENaC），可透過控制血壓與體液量間接影響高血壓相關疾病，但此機轉描述並非來自本報告所整理的資料欄位，需另行查證。

惡性高血壓腎病變是嚴重高血壓造成的腎臟損傷。此分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

此外，惡性高血壓合併腎功能受損時，保鉀利尿劑有高血鉀的風險，實際應用需非常謹慎。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

（備註：其他預測適應症中，肺高壓與慢性肺心症各有 2 篇文獻，但並未直接研究惡性高血壓腎病變，因此不計入本適應症的證據。）

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-39897 | APO-TRIAZIDE TAB 50/25MG | 未載明 | 未載明 |

此許可證的品名顯示為含 triamterene 與另一利尿成分的製劑，但資料中分類為單一成分；其內容不能用來說明單方 triamterene 的核准狀態。

## 安全性考量

- **知識圖譜中記錄的禁忌關聯（非仿單內容）**：肝衰竭、腎臟疾病、無尿、胰臟炎、肝病、膽囊疾病、全身性紅斑性狼瘡、糖尿病（第 1 型與第 2 型）、糖尿病酮酸中毒、高尿酸血症、痛風、副甲狀腺機能亢進、肝昏迷、肝性腦病變、新生兒黃疸、高鈣血症、腎鈣質沉著症、腎結石、急性尿酸腎病變、葉酸缺乏性貧血、酸中毒與乳酸中毒等。
- **藥物交互作用**：資料庫共查得 100 筆，以下為部分示例。
  - 重大：檸檬酸鉀（Potassium citrate），高血鉀風險。
  - 中度：Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide、Metformin、Bupropion、Morphine、Canagliflozin、Dapagliflozin、Bisacodyl 等。
  - 輕微：Famotidine、Ranitidine、Cimetidine、Doxycycline、Minocycline。

仿單的警語與禁忌資料未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究 triamterene 於惡性高血壓腎病變，證據等級僅為 L5（模型預測）。
- 該疾病常伴隨腎功能受損，而知識圖譜中腎臟疾病、無尿屬於禁忌關聯，加上高血鉀風險，安全疑慮明顯。

**若要推進需要：**
- 取得 triamterene 的作用機轉資料與香港仿單的警語、禁忌內容
- 針對惡性高血壓腎病變進行系統性文獻檢索，確認是否有直接研究
- 評估高血鉀與腎功能惡化風險，並釐清與既有高血壓適應症相比有何差異化價值
- 如有進一步研究計畫，先設計以腎功能與血鉀監測為核心的小型探索性研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

