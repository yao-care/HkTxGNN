---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 552
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Mannitol：預測新適應症為腎因性抗利尿不適當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis)（證據等級 L5）。原適應症：充血性心衰竭、腦水腫、眼壓過高、假性腦瘤、顱內高壓、囊性纖維化"
monitor_inn: "MANNITOL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "malignant hyperthermia, susceptibility to", "familial periodic paralysis"]
---

# Mannitol
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

# Mannitol：從腦水腫與顱內高壓到抗利尿不適當症候群（腎因性）

## 一句話總結

Mannitol（甘露醇）是一種滲透性利尿劑，原本用於腦水腫、顱內高壓、眼壓過高、充血性心衰竭等情況。
TxGNN 模型預測它可能對**腎因性抗利尿不適當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇**相關的一般性文獻，且該文獻並不支持以甘露醇作為治療。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 充血性心衰竭、腦水腫、眼壓過高、假性腦瘤、顱內高壓、囊性纖維化（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 腎因性抗利尿不適當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，甘露醇是滲透性利尿劑，會提高血漿滲透壓並促進滲透性水分排出。理論上與抗利尿異常疾病有關聯，但這個關聯並未被證實。

實際上，這個預測在機轉上有疑慮。甘露醇會造成水分在細胞內外的滲透性位移，預期可能**加重**低血鈉，引起稀釋性或移位性低血鈉。NSIAD 的標準處置是限水、補充尿素或類似措施，並非使用甘露醇。

高預測分數可能反映知識圖譜中的關聯，而非真正的治療效果。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | 說明低血鈉評估的十大常見陷阱，屬一般性回顧，並未支持甘露醇可作為治療 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-21527 | OSMITROL (MANNITOL) INJ 20% "VIAFLEX" | 未載明 | 未載明 |
| HK-28237 | OSMOFUNDIN IV INFUSION 20% | 未載明 | 未載明 |
| HK-43086 | NEUROLITE FOR INJ WITH BUFFER VIAL | 未載明 | 未載明 |

---

## 安全性考量

- **禁忌症（知識圖譜推論，非仿單內容）**：知識圖譜列出的相關疾病包括肝衰竭、肝性腦病變／肝昏迷、無尿、腎功能受損、肺水腫、顱內出血、血小板減少、嗜中性球減少、顆粒球缺乏症、貧血、紫質症、睡眠呼吸中止症及物質濫用／依賴等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 重大 (Major)：Amikacin
  - 中度 (Moderate)：Lamivudine、Formoterol、Salbutamol、Amifostine、Benazepril、Captopril、Carbamazepine、Citalopram、Canagliflozin、Dapagliflozin 等
  - 輕微 (Minor)：Doxycycline
- **與預測適應症相關的風險**：甘露醇可能加重低血鈉，並可能因滲透性容積擴張而誘發肺水腫。

香港仿單的警語與禁忌症資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型，沒有任何臨床試驗，唯一的文獻也不支持甘露醇治療 NSIAD。
- 機轉上甘露醇反而可能惡化低血鈉，風險大於潛在效益。

**若要推進需要：**
- 取得完整的作用機轉資料，並釐清模型預測的來源（可能是圖譜關聯而非療效）。
- 取得香港仿單的警語與禁忌症，完成安全性篩選。
- 找到直接評估甘露醇於 NSIAD 的機轉或臨床證據；否則建議不予推進。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

