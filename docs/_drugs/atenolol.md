---
layout: default
title: Atenolol
parent: 僅模型預測 (L5)
nav_order: 78
evidence_level: L5
indication_count: 5
monitor_inn: "ATENOLOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-28
description: "Atenolol：預測新適應症為惡性高血壓腎病變（證據等級 L5）。原適應症：知識圖譜記錄：高血壓、心肌梗塞等"
---

# Atenolol
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

## Atenolol：從高血壓到惡性高血壓腎病變
{: .text-alpha }

## 一句話總結

Atenolol 是 β1 選擇性受體阻斷劑，知識圖譜中記錄的使用範圍包含高血壓與心肌梗塞。
TxGNN 模型預測它可能對**惡性高血壓腎病變 (malignant hypertensive renal disease)** 有效，
但目前**沒有臨床試驗，也沒有直接研究此疾病的文獻**，證據僅來自模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄：高血壓、心肌梗塞等（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 惡性高血壓腎病變 |
| TxGNN 預測分數 | 0.9985 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 核准數 | 至少 20 張單方許可證（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Atenolol 屬於 β1 選擇性阻斷劑，一般認為可降低血壓並減少腎素釋放，這在機轉上與高血壓造成的腎臟損傷有一定關聯。

惡性高血壓腎病變與高血壓本身高度相關，因此模型給出高分並不意外。這個預測較可能是既有高血壓用途的延伸，而不是獨立的新用途訊號。

需要留意的是，惡性高血壓屬於緊急狀況，臨床上通常使用可精準調整劑量的靜脈藥物處理，而不是口服 atenolol。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

下列為資料中列出的 20 張單方許可證（總數至少 20 張，清單可能不完整），此處列出 5 張。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-17873 | TENORMIN TAB 50MG | PRUDENTLINK LIMITED |
| HK-06812 | TENORMIN TAB 100MG | PRUDENTLINK LIMITED |
| HK-45490 | NORMATEN TAB 50MG | FP HEALTHCARE LIMITED |
| HK-34859 | NOTEN TAB 50MG | VIATRIS HEALTHCARE HONG KONG LIMITED |
| HK-61154 | DEMITENS ORAL SOLUTION 25MG/5ML | SINO-ASIA PHARMACEUTICAL SUPPLIES LTD |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：氣喘（含內因性、過敏性）、房室傳導阻滯、雷諾氏病、第 1 型與第 2 型糖尿病及糖尿病酮酸中毒、肝衰竭、胰臟炎、全身性紅斑性狼瘡、乾癬、痛風、過敏性休克、無尿等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 中度：Epinephrine、Hydrocortisone、Bupropion、Morphine、Atropine、Triamcinolone、Betamethasone、Budesonide、多種鈣鹽
  - 輕度：Acetylsalicylic acid、Aluminum hydroxide、Attapulgite

正式的警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測沒有任何臨床試驗或直接研究的文獻支持，僅為模型預測，證據等級為 L5。
- Atenolol 本身已用於高血壓，此預測更像既有用途的延伸；且惡性高血壓屬緊急狀況，通常不以口服藥物處理。

**若要推進需要：**
- 取得直接研究 atenolol 用於惡性高血壓腎病變的臨床或觀察性資料
- 取得詳細的作用機轉資料（MOA）
- 取得香港仿單的核准適應症、警語與禁忌
- 釐清與現行急性降壓標準治療的定位差異
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

