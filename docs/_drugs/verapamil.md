---
layout: default
title: Verapamil
parent: 僅模型預測 (L5)
nav_order: 931
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Verapamil：預測新適應症為惡性腎血管性高血壓 (Malignant Renovascular Hypertension)（證據等級 L5）。原適應症：高血壓、心房顫動、急性冠心症、變異型心絞痛、心室心搏過速"
monitor_inn: "Verapamil"
predicted_indications: ["obsolete bundle branch block", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "periodic paralysis with transient compartment-like syndrome"]
---

# Verapamil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Verapamil：從高血壓與心律不整到惡性腎血管性高血壓

## 一句話總結

Verapamil 是一種鈣離子通道阻斷劑，原本用於高血壓、心房顫動、急性冠心症、變異型心絞痛及心室心搏過速等心血管疾病。
TxGNN 模型預測它可能對**惡性腎血管性高血壓 (Malignant Renovascular Hypertension)** 有效，但目前**沒有臨床試驗**，且檢索到的 2 篇文獻都沒有直接測試 Verapamil，證據僅停留在模型預測層級。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、心房顫動、急性冠心症、變異型心絞痛、心室心搏過速（取自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 惡性腎血管性高血壓 (Malignant Renovascular Hypertension) |
| TxGNN 預測分數 | 99.27% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Verapamil 屬於 L-type 鈣離子通道阻斷劑，會減慢房室結傳導並使血管擴張，其降血壓作用已在原發性高血壓中被證實。

惡性腎血管性高血壓屬於繼發性、腎素驅動的高血壓。Verapamil 的血管擴張降壓作用與其已核准的高血壓適應症有機轉上的重疊，這也是模型給出高分的可能原因。

不過，鈣離子通道阻斷劑在這類腎素驅動的情境中療效並未確立。檢索到的兩篇文獻（醛固酮／腎素比值的干擾因素、嬰兒腎肌纖維瘤）都沒有在此疾病中測試 Verapamil。

另外要注意，本次預測清單的其他項目大多缺乏支持，例如「obsolete bundle branch block」很可能只是本體論（ontology）的人為產物，而肺高壓相關預測在臨床上反而有疑慮（見下文）。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22147655](https://pubmed.ncbi.nlm.nih.gov/22147655/) | 2012 | Review | Hormone and Metabolic Research | 探討影響醛固酮／腎素比值的因素；惡性或腎血管性高血壓可刺激腎素而造成偽陰性。未測試 Verapamil |
| [10224210](https://pubmed.ncbi.nlm.nih.gov/10224210/) | 1999 | Case report | Pediatrics | 孤立性腎肌纖維瘤病是嬰兒腎血管性高血壓的罕見原因。與 Verapamil 無直接關聯 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-01261 | ISOPTIN TAB 40 MG | 未載明 | 未載明 |
| HK-40707 | AKILEN TAB 40MG | 未載明 | 未載明 |
| HK-33700 | ANPEC 80 TAB 80MG | 未載明 | 未載明 |
| HK-55703 | VERAPAMIL HYDROCHLORIDE INJ 2.5MG/ML | 注射劑（依品名） | 未載明 |
| HK-36259 | APO-VERAP TAB 80MG | 未載明 | 未載明 |

（共 8 張有效單方許可證，上表列出其中 5 張。）

## 安全性考量

- **禁忌症（來自知識圖譜的藥物－疾病禁忌關聯，非仿單文字）**：包含主動脈瓣狹窄、肥厚性心肌症、低血壓、房室傳導阻滯、心衰竭、心室心搏過速、重症肌無力、腎臟疾病、肝臟疾病、血管性水腫、嗜中性白血球低下及顆粒球缺乏症等。其中房室傳導阻滯與心衰竭尤其值得注意。
- **藥物交互作用**：資料庫共收錄 100 筆，以下為部分範例：
  - 重大 (Major)：Loperamide
  - 中度 (Moderate)：Clarithromycin、Cimetidine、Acetylsalicylic acid、Metformin、Bupropion、Aprepitant、Canagliflozin，以及多種類固醇（Hydrocortisone、Dexamethasone、Betamethasone、Budesonide、Triamcinolone）與鈣鹽類
  - 輕微 (Minor)：Morphine
- **預測適應症相關疑慮**：Verapamil 具負性肌力作用；用於肺高壓時，可能因減弱缺氧性肺血管收縮而惡化氣體交換，因此不建議用於缺氧或肺疾病相關的肺高壓。

仿單警語與禁忌的正式內容請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型（L5），沒有臨床試驗，兩篇文獻也未直接測試 Verapamil。惡性腎血管性高血壓有其他更成熟的標準治療。

**若要推進需要：**
- 取得 Verapamil 的作用機轉資料（MOA）與香港仿單的警語與禁忌
- 系統性檢索 Verapamil 或鈣離子通道阻斷劑用於腎血管性或惡性高血壓的臨床與觀察性研究
- 與現行標準治療（如腎素－血管張力素系統阻斷劑）比較其潛在角色
- 針對此族群（常合併腎功能受損）評估安全性與藥物交互作用
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

