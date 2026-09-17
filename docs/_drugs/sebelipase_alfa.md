---
layout: default
title: Sebelipase Alfa
parent: 僅模型預測 (L5)
nav_order: 676
evidence_level: L5
indication_count: 10
---

# Sebelipase Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Sebelipase alfa：從 溶酶體酸性脂酶缺乏症 (LAL-D) 到 Scheie 症候群

## 一句話總結

> Sebelipase alfa 是用於治療溶酶體酸性脂酶缺乏症 (LAL-D，涵蓋 Wolman disease 與膽固醇酯儲積症 CESD 兩種表現型) 的酵素替代療法。
> TxGNN 模型預測分數最高的新適應症為 **Scheie 症候群**，但目前**沒有任何臨床試驗或文獻支持**，證據小組已將此判定為知識圖譜語意群聚造成的假陽性，而非真實機轉關聯。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 溶酶體酸性脂酶缺乏症 (LAL-D)（依 evidence pack 中文獻描述推得，結構化欄位 `original_indications` 為空） |
| 預測新適應症 | Scheie syndrome |
| TxGNN 預測分數 | 99.80%（KG rank 4615） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（`original_moa` 標記為 [Data Gap]，且列為 High severity 缺口）。但從證據小組對本候選的機轉評估可以看出，這個預測**並不合理**：

Scheie syndrome 屬於黏多醣症 I 型 (MPS I) 的輕型表現，致病機轉是 **alpha-L-iduronidase** 缺乏；而 sebelipase alfa 補充的是 **lysosomal acid lipase (LAL)**，兩者是完全不同的酵素系統，彼此無機轉關聯。證據小組的判讀明確指出：

> 「MPS I 輕型，同為 alpha-L-iduronidase 缺乏，與 LAL 酵素機轉無關；無任何臨床或文獻證據，純屬 KG 語意群聚假影。」

也就是說，TxGNN 給出的高分很可能只是因為 Scheie syndrome 與 LAL-D 都屬於「溶酶體儲積病」這個語意群集，在知識圖譜上距離相近，但沒有真正的生物學基礎支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

Sebelipase alfa 目前**未在香港上市**，無許可證資料可列出。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：本次資料收集中，TFDA/香港仿單警語與禁忌症被列為 **Blocking** 等級的資料缺口（DG001），在補齊前無法進行安全性初評 (S1)。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測適應症 (Scheie syndrome) 證據等級為 L5，無臨床試驗、無文獻，且經機轉分析判定為知識圖譜語意群聚造成的假陽性，不具備推進基礎。
- 安全性�292仿單資料為 Blocking 缺口，尚無法進行任何安全性初評。

**重要提醒（非本候選但需一併說明）：**
本組 10 個預測適應症中，多數（如 Hurler syndrome、Tay-Sachs disease、Gaucher disease 等）皆被證據小組標註為「與 LAL 機轉無關、屬 KG 雜訊」的假陽性；唯二有實質臨床試驗與文獻支持的 **cholesteryl ester storage disease（rank 4）** 與 **Wolman disease（rank 5）**，實際上正是 sebelipase alfa **原本已核准的適應症**（LAL-D 的兩種表現型），並非真正的「老藥新用」候選，而是模型正確識別出既有真實關聯。這代表本次 TxGNN 預測結果對於「新」適應症的挖掘價值有限。

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，解除 Blocking 狀態）
- 補齊作用機轉資料（DG002）
- 針對真正具生物學合理性的候選（若有）重新執行機轉比對，而非僅依賴 TxGNN 分數排序
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

