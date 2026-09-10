---
layout: default
title: Mirtazapine
parent: 僅模型預測 (L5)
nav_order: 501
evidence_level: L5
indication_count: 3
---

# Mirtazapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# MIRTAZAPINE：從精神科用藥到 Ohdo Syndrome 及其變異型

## 一句話總結

Mirtazapine（DB00370）為 NaSSA（正腎上腺素及特定血清素抗憂鬱劑）類抗憂鬱藥物，目前**未在香港取得任何許可證**。TxGNN 模型預測其可能對 **Ohdo Syndrome 及其變異型**（一種罕見的先天染色質重塑基因缺陷症候群）有效，但**目前無任何臨床試驗或文獻支持**，屬純模型關聯推測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（evidence pack 未提供核准適應症；依內部 MOA 敘述推測為憂鬱症相關適應症） |
| 預測新適應症 | Ohdo syndrome and variants |
| TxGNN 預測分數 | 99.42% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為 [Data Gap]）。根據 evidence pack 中的機轉推論敘述，Mirtazapine 屬於 NaSSA 類抗憂鬱藥，主要透過 α2-腎上腺素受體拮抗及 5-HT2A/5-HT2C/5-HT3/H1 受體拮抗發揮作用。

Ohdo syndrome（含 SBBYSS 亞型）主因為 KAT6B/KAT6A 基因突變導致染色質重塑異常，是一種先天發育性疾病，與單胺受體調節機轉之間**沒有已知的生物學路徑交集**。同樣地，第二項預測「blepharophimosis - intellectual disability syndrome, Ohdo type」是 Ohdo syndrome 的亞型，機轉關聯性同樣缺乏支持。

第三項預測「benign paroxysmal torticollis of infancy」（嬰兒陣發性良性斜頸）多與 CACNA1A 離子通道病變相關；Mirtazapine 的抗組織胺與 5-HT2/5-HT3 拮抗特性理論上與偏頭痛相關噁心/嘔吐症狀有間接連結，但此關聯屬推測性，並未觸及該疾病離子通道功能異常的病理生理核心。三項預測皆為 TxGNN 知識圖譜的高分關聯，**不具明確藥理機轉支持**。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Mirtazapine 目前於香港**未取得任何許可證**（`total_licenses = 0`），無法提供品名、劑型與核准適應症資訊。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（說明：evidence pack 標記 DG001 為 Blocking 等級缺口——缺乏 TFDA/仿單警語與禁忌症資料，尚無法進入 S1 安全性初評；藥物交互作用查詢亦無結果。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 三項預測適應症皆屬證據等級 L5，僅有 TxGNN 模型關聯分數，無任何臨床試驗或文獻佐證。
- 機轉關聯性分析顯示，Mirtazapine 的受體藥理與 Ohdo syndrome 相關的染色質調控病因之間缺乏合理連結。
- 藥物於香港未上市，且安全性資料（警語、禁忌症）為 Blocking 等級缺口，無法進行安全性初評。

**若要推進需要：**
- 取得 DrugBank 完整 MOA 資料，釐清機轉關聯性（DG002）。
- 下載並解析 TFDA／原廠仿單，補齊警語與禁忌症資料，以解除 S1 安全性初評的 Blocking 缺口（DG001）。
- 針對三項預測適應症持續監測是否有新臨床試驗或文獻登記，目前皆為零筆。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

