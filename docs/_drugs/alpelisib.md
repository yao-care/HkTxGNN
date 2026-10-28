---
layout: default
title: Alpelisib
parent: 僅模型預測 (L5)
nav_order: 41
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Alpelisib：預測新適應症為肺動脈高壓 (Pulmonary Hypertension)（證據等級 L5）。原適應症：香港許可證資料未載明"
monitor_inn: "Alpelisib"
predicted_indications: ["pulmonary hypertension"]
---

# Alpelisib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

## Alpelisib：從乳癌（原適應症資料未載明）到肺動脈高壓
{: .text-alpha }

## 一句話總結

Alpelisib 是 PI3Kα 選擇性抑制劑，在香港已取得上市許可。本次編入的資料未載明其核准適應症。
TxGNN 模型預測它可能對**肺動脈高壓 (Pulmonary Hypertension)** 有效，但目前沒有相關臨床試驗，只有 **1 篇文獻**（病例報告），且內容是藥物引起肺部不良反應，不是療效證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明 |
| 預測新適應症 | 肺動脈高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 0.9903 |
| 證據等級 | L5（僅有 1 篇病例報告，且為安全性訊號） |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Alpelisib 為 PI3Kα 選擇性抑制劑，PI3K 訊號路徑與肺血管重塑在生物學上可能有關聯，所以模型給出高分。

不過，目前沒有證據顯示抑制 PI3Kα 能治療肺動脈高壓。唯一相關的文獻是 alpelisib 引起間質性肺病的病例報告，這是肺部毒性的警訊，反而提示需要謹慎。

TxGNN 分數很高，但排名為 15076，且此分數來自 TxGNN 模型（深度學習），可能反映模型在相關疾病之間學到的相似性，並非生物學證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35730191](https://pubmed.ncbi.nlm.nih.gov/35730191/) | 2023 | 病例報告 | J Oncol Pharm Pract | 晚期乳癌患者使用 alpelisib 後發生間質性肺病，屬安全性訊號，並非療效證據 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66925 | PIQRAY TABLETS 150MG | 未載明 | 未載明 |
| HK-66926 | PIQRAY TABLETS 200MG | 未載明 | 未載明 |
| HK-66927 | PIQRAY TABLETS 200MG+50MG | 未載明 | 未載明 |

三張許可證皆為單一成分、有效狀態，持證商為 Novartis Pharmaceuticals (HK) Limited。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（PI3Kα 抑制劑），用於 PIK3CA 突變的 HR+/HER2- 晚期乳癌 |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 血糖（高血糖為已知不良反應）；其餘請參考原廠仿單 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **肺部毒性**：文獻有 alpelisib 引起間質性肺病的病例報告，對肺部疾病族群尤須留意。
- **高血糖**：相關試驗（NCT04300790）顯示高血糖是常見不良反應，需使用 metformin 預防。
- **藥物交互作用**：已查得 100 筆交互作用，以下為部分中度（Moderate）交互作用：
  - 降血糖藥物：Acarbose、Albiglutide、Alogliptin、Metformin、Pioglitazone、Glimepiride、Glipizide、Canagliflozin、Dapagliflozin、Empagliflozin 等
  - 其他：Dexamethasone、Bupropion、Alosetron、Dronabinol、Fidaxomicin

仿單的警語與禁忌症資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 模型分數雖高，但沒有臨床試驗，唯一的文獻是肺部不良反應的病例報告，不支持療效。
- 肺部毒性的訊號使這個方向風險更高。

**若要推進需要：**
- 取得 alpelisib 完整作用機轉資料與香港仿單（警語、禁忌症、核准適應症）
- 前臨床研究，評估 PI3Kα 抑制在肺動脈高壓模型中的作用
- 釐清間質性肺病風險，以及高血糖對肺動脈高壓族群的影響
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

