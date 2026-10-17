---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Carvedilol：預測新適應症為惡性腎血管性高血壓 (Malignant Renovascular Hypertension)（證據等級 L5）。原適應症：高血壓 (Hypertension)"
monitor_inn: "CARVEDILOL"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
---

# Carvedilol
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

# Carvedilol：從高血壓到惡性腎血管性高血壓

## 一句話總結

Carvedilol 是一種兼具 α1 阻斷作用的非選擇性 β 受體阻斷劑，原本用於高血壓治療。
TxGNN 模型預測它可能對**惡性腎血管性高血壓 (Malignant Renovascular Hypertension)** 有效，
但目前**沒有臨床試驗與文獻**直接支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓 (Hypertension) |
| 預測新適應症 | 惡性腎血管性高血壓 (Malignant Renovascular Hypertension) |
| TxGNN 預測分數 | 99.55% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Carvedilol 是非選擇性 β 受體阻斷劑，同時具 α1 阻斷活性，已被核准用於高血壓。惡性腎血管性高血壓是一種嚴重、與腎素活性相關的高血壓，因此 β 阻斷（減少腎素釋放）與血管擴張在機轉上有其合理性。

不過，0.995 的高分很可能反映的是此疾病在本體論（ontology）上與已核准的高血壓適應症非常接近，而不是獨立的療效證據。

此外，惡性腎血管性高血壓屬於急症，臨床上通常以靜脈藥物與血管重建術處理，口服 Carvedilol 不太可能是第一線選擇。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 20 張有效許可證，皆為單方製劑。資料中未提供劑型與核准適應症文字。以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-42822 | DILATREND TAB 6.25MG（DKSH） | 錠劑 | 未提供 |
| HK-36984 | DILATREND TAB 25MG（DKSH） | 錠劑 | 未提供 |
| HK-42821 | DILATREND 12.5 TAB 12.5MG（DKSH） | 錠劑 | 未提供 |
| HK-55539 | APO-CARVEDILOL TAB 6.25MG（HIND WING） | 錠劑 | 未提供 |
| HK-52638 | PMS-CARVEDILOL TAB 25MG（TRENTON-BOMA） | 錠劑 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物與疾病關係資料，非仿單原文）：肝衰竭、支氣管炎、氣喘（含內因性與過敏性）、肺氣腫、支氣管疾病、糖尿病、糖尿病酮酸中毒、低血壓、周邊血管疾病、間歇性跛行、周邊動脈疾病、房室傳導阻滯、病竇症候群（含家族性）、變異型心絞痛 (Prinzmetal angina)、過敏性休克、術中虹膜鬆弛症候群。
- **藥物交互作用**：共查得 100 筆，以下為主要項目：
  - **嚴重 (Major)**：Epinephrine
  - **中度 (Moderate)**：Hydrocortisone、Hyoscyamine、Bupropion、Triamcinolone、Morphine、Atropine、Dexamethasone、Lorcaserin、Betamethasone、Budesonide、Canagliflozin、Acetohexamide，以及多種鈣製劑（磷酸鈣、醋酸鈣、碳酸鈣、檸檬酸鈣）
  - **輕微 (Minor)**：Acetylsalicylic acid、Aluminum hydroxide、Attapulgite

仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅有模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。高分很可能來自與原適應症的本體論接近性。
- 此疾病為高血壓急症，口服 Carvedilol 並非標準處置，臨床定位不明確。

**若要推進需要：**
- 取得 Carvedilol 的作用機轉資料，並釐清其在腎素驅動型高血壓中的角色
- 取得香港仿單的警語與禁忌資料，完成安全性篩查
- 檢索腎血管性或惡性高血壓相關的臨床研究與文獻
- 評估口服劑型是否符合此急症的臨床使用情境

---

### 其他預測適應症（供參考）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 2 | 惡性高血壓性腎病 (Malignant Hypertensive Renal Disease) | 99.55% | L5 | Hold |
| 3 | 肺部疾病和/或缺氧所致肺高壓 | 99.54% | L4 | Research Question |
| 4 | 機轉不明的多因素肺高壓 | 99.54% | L5 | Hold |
| 5 | Braddock 症候群 | 99.37% | L5 | Hold |

其中**肺部疾病和/或缺氧所致肺高壓**有間接的前臨床證據。例如 PMID 26291659 顯示 Carvedilol 能逆轉大鼠慢性間歇性缺氧誘發的高血壓。但該模型屬全身性高血壓，並非肺高壓，且非選擇性 β 阻斷可能加重肺部疾病患者的呼吸功能，也沒有人體試驗。其餘預測皆無支持證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

