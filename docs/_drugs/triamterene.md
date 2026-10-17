---
layout: default
title: Triamterene
parent: 僅模型預測 (L5)
nav_order: 904
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Triamterene：預測新適應症為惡性腎血管性高血壓 (Malignant Renovascular Hypertension)（證據等級 L5）。原適應症：高血壓、充血性心臟衰竭"
monitor_inn: "TRIAMTERENE"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Triamterene：從高血壓到惡性腎血管性高血壓

## 一句話總結

Triamterene 是一種保鉀利尿劑，原本用於高血壓與充血性心臟衰竭。
TxGNN 模型預測它可能對**惡性腎血管性高血壓 (Malignant Renovascular Hypertension)** 有效，
但目前**沒有臨床試驗**，也**沒有直接相關的文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、充血性心臟衰竭（依知識圖譜資料；香港許可證未載明適應症文字） |
| 預測新適應症 | 惡性腎血管性高血壓 (Malignant Renovascular Hypertension) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Triamterene 是阻斷遠端腎elements 上皮鈉通道 (ENaC) 的保鉀利尿劑，已被核准用於高血壓，機轉上可能透過排鈉利尿作用，對高血壓相關疾病產生輔助效果。

惡性腎血管性高血壓主要由腎動脈狹窄造成腎素-血管收縮素系統過度活化所驅動。利尿劑或許能扮演次要的輔助角色，但這個關聯目前僅來自知識圖譜的預測，沒有任何試驗或文獻佐證。

此外，這類病人常合併腎功能受損，使用保鉀利尿劑有高血鉀風險，因此機轉上的合理性有限。

同批預測中的其他疾病（惡性高血壓性腎病、兩種肺高壓、Braddock 症候群）同樣只有模型分數，沒有臨床證據支持，其中惡性高血壓性腎病因腎功能受損，安全疑慮更明顯。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對首要預測（惡性腎血管性高血壓）目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-39897 | APO-TRIAZIDE TAB 50/25MG | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單內容，僅供參考）：肝衰竭、肝病、肝性腦病變、腎臟疾病、無尿症、腎結石、痛風、高尿酸相關疾病、糖尿病（第 1 型與第 2 型）、糖尿病酮酸中毒、酸中毒、乳酸中毒、胰臟炎、膽囊疾病、全身性紅斑狼瘡、副甲狀腺機能亢進、高血鈣、葉酸缺乏性貧血、新生兒黃疸等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 重大：Potassium citrate（併用有高血鉀風險）
  - 中度：Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide、Metformin、Bupropion、Morphine、Canagliflozin、Dapagliflozin、Bisacodyl、Dronabinol
  - 輕微：Famotidine、Ranitidine、Cimetidine、Doxycycline、Minocycline
- 此外，保鉀利尿劑用於腎功能受損者有高血鉀與急性腎損傷風險，而腎功能受損在惡性腎血管性高血壓中相當常見。

其餘警語與禁忌資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但僅屬模型推論，沒有臨床試驗與直接相關文獻（證據等級 L5）。
- 目標病人常有腎功能受損，使用保鉀利尿劑的高血鉀風險高，安全性疑慮大於潛在效益。

**若要推進需要：**
- 補齊作用機轉資料（MOA）
- 取得香港仿單的警語與禁忌資訊（目前為阻擋性缺口）
- 系統性搜尋腎血管性高血壓使用 triamterene 的臨床或觀察性研究
- 評估腎功能受損族群的安全性與血鉀監測方案
- 確認此許可證為含 hydrochlorothiazide 的複方製劑（品名為 APO-TRIAZIDE 50/25），再判斷後續證據是否可歸因於 triamterene
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

