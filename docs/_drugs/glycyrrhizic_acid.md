---
layout: default
title: Glycyrrhizic Acid
parent: 僅模型預測 (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Glycyrrhizic Acid：預測新適應症為多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "Glycyrrhizic acid"
predicted_indications: ["multiple endocrine neoplasia", "amenorrhea (disease)", "hypoalphalipoproteinemia", "malignant catarrh", "infectious bovine rhinotracheitis", "cytomegalovirus infection", "acne (disease)", "kyphoscoliotic heart disease", "pulmonary hypertension", "rheumatoid arthritis"]
---

# Glycyrrhizic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Glycyrrhizic acid（甘草酸）：從（原適應症未載明）到多發性內分泌腫瘤

## 一句話總結

Glycyrrhizic acid（甘草酸）是甘草的主要活性成分，目前在香港有 4 張單方許可證，但本次整理的資料中未載明其核准適應症。
TxGNN 模型預測它可能對**多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)** 有效，預測分數很高，但**目前沒有任何臨床試驗或文獻**支持，屬於純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 多發性內分泌腫瘤 (Multiple Endocrine Neoplasia) |
| TxGNN 預測分數 | 99.28% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，甘草酸是甘草萃取的三萜類皂苷成分，已有多個單方產品在香港取得許可。但就「多發性內分泌腫瘤」這個預測而言，現有資料無法建立任何機轉上的連結。

TxGNN 的高分（0.993）僅是計算模型的輸出。沒有臨床試驗，也沒有文獻可佐證，因此這個預測目前只能視為待驗證的假設，不宜作為推進依據。

另外，甘草酸已知可抑制 11β-羥類固醇脫氫酶，並有類鹽皮質素效應。這些作用雖可能影響內分泌系統，但與內分泌腫瘤之間並無資料支持的關聯。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49857 | OUTERDZEN TAB | 資料未載明 | 資料未載明 |
| HK-34639 | BETTY CAP | 資料未載明 | 資料未載明 |
| HK-49914 | NORSETOA CAP | 資料未載明 | 資料未載明 |
| HK-42269 | BAO FU LING CREAM | 資料未載明 | 資料未載明 |

以上 4 張許可證均為有效的單方許可證，製造商包括 HITPHARM PHARMACEUTICAL CO LTD、YUNG SHIN CO LTD 與 HONG KONG WAH SHENG MEDICAL CO LTD。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測新適應症完全沒有臨床試驗與文獻支持，證據等級僅為 L5。
- 原適應症、作用機轉與仿單安全性資料都缺漏，無法進行機轉分析與安全性篩選。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊核准適應症、警語與禁忌症
- 從 DrugBank 補充作用機轉（MOA）資料
- 針對多發性內分泌腫瘤進行文獻與臨床試驗檢索，確認是否有任何直接證據
- 釐清甘草酸與內分泌腫瘤之間是否存在可驗證的機轉假設，再評估是否進入前臨床研究

---

### 補充說明：其他預測適應症

在排名前 10 的預測中，下列兩項有較多證據，但仍屬前臨床階段，皆為 Hold 或需進一步研究。

| 預測適應症 | TxGNN 分數 | 證據等級 | 證據概況 |
|-----------|-----------|---------|---------|
| 類風濕性關節炎 | 97.82% | L4 | 約 20 篇文獻，皆為前臨床、複方或製劑研究，無臨床試驗。其中甘草酸與芒果苷的組合在動物實驗中顯示抑制滑膜新生血管等效果 |
| 肺動脈高壓 | 97.91% | L4 | 僅有大鼠動物研究。需注意甘草酸本身可能升高血壓並造成水分滯留 |

類風濕性關節炎是目前證據量最多的方向，若要探索新適應症，可優先考慮，但仍需先有直接以甘草酸為對象的臨床證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

