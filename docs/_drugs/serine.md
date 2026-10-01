---
layout: default
title: Serine
parent: 僅模型預測 (L5)
nav_order: 793
evidence_level: L5
indication_count: 5
---

# Serine
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

# Serine：從胺基酸營養輸液成分到家族性內臟肌病變

## 一句話總結

Serine（絲胺酸）是一種胺基酸，在香港以多種胺基酸輸液產品的成分上市。
TxGNN 模型預測它可能對**家族性內臟肌病變 (Familial Visceral Myopathy)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 家族性內臟肌病變 (Familial Visceral Myopathy) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Serine 是蛋白質組成胺基酸，參與一碳代謝，以及甘胺酸與鞘脂質的合成。

家族性內臟肌病變是一種遺傳性平滑肌疾病（例如 ACTG2 相關）。現有資料中沒有任何已記載的路徑，能把 serine 與這個疾病連起來。

0.9999 的高分，較可能反映 serine 這類普遍存在的代謝物在知識圖譜中連結度很高，而不是特定的治療訊號。因此這個預測目前**不能視為機轉上合理**，只能當作待驗證的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 20 張相關許可證，以下列出 5 張主要許可證（資料中未提供劑型與核准適應症）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-58387 | AMINOLEBAN 8% AMINO ACID INJ | Otsuka Pharmaceutical (H.K.) Limited |
| HK-46283 | AMINOLEBAN INJ | Otsuka Pharmaceutical (H.K.) Limited |
| HK-67075 | AMINOVEN INFANT SOLUTION FOR INFUSION 10% W/V | Fresenius Kabi Hong Kong Limited |
| HK-36470 | VAMINOLACT I.V. SOLUTION | Fresenius Kabi Hong Kong Limited |
| HK-32746 | AMINOPLASMAL HEPA-10% INJ | B. Braun Medical (HK) Ltd |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，只有模型分數，沒有臨床試驗、文獻，也找不到機轉連結。
- 其他預測適應症也沒有可用的證據。腸阻塞一項雖檢索到試驗與文獻，但多為關鍵字誤配（腫瘤、中風等），並未測試 serine。

**若要推進需要：**
- 補齊 serine 的作用機轉資料（可查詢 DrugBank）。
- 取得香港衛生署仿單的警語與禁忌症（目前為阻擋性缺口，無法進入安全性篩選）。
- 針對 serine 與內臟肌病變或腸道動力障礙，進行有針對性的文獻檢索與前臨床機轉驗證。
- 釐清輸液劑型與家族性內臟肌病變所需給藥途徑是否相容。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

