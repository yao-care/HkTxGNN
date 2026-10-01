---
layout: default
title: Galantamine
parent: 僅模型預測 (L5)
nav_order: 399
evidence_level: L5
indication_count: 5
---

# Galantamine
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

# Galantamine：從阿茲海默症到心因性動作障礙

## 一句話總結

Galantamine 是一種乙醯膽鹼酯酶抑制劑，文獻摘要describes其用於阿茲海默症的認知障礙。
TxGNN 模型預測它可能對**心因性動作障礙 (Psychogenic Movement Disorders)** 有效。
目前**沒有臨床試驗**和**文獻**支持這個方向，僅有模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 阿茲海默症認知障礙（依文獻摘要；香港許可證資料未載明適應症） |
| 預測新適應症 | 心因性動作障礙 (Psychogenic Movement Disorders) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。已知 Galantamine 具有兩種藥理作用：抑制乙醯膽鹼酯酶，以及對菸鹼型乙醯膽鹼受體 (nAChR) 做變構調節。它在阿茲海默症認知障礙中的用途已為人所知。

但這兩種作用與功能性（心因性）動作障礙之間，現有資料找不到已建立的關聯。0.999 的預測分數只是模型輸出，並非機轉或臨床證據。

膽鹼系統調節基底核迴路，是合理的推測方向，但仍未經證實。這個預測目前只能視為待驗證的假說。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 9 張許可證，以下列出 5 張主要許可證。資料中未載明核准適應症與劑型欄位，劑型依品名判讀。

| 許可證號 | 品名 | 劑型（依品名） | 廠商 |
|---------|------|------|------|
| HK-55293 | REMINYL PROLONGED RELEASE CAP 8MG | 緩釋膠囊 | Johnson & Johnson (Hong Kong) Ltd. |
| HK-65459 | GALANTAMINE HYDROBROMIDE EXTENDED-RELEASE CAPSULES 16MG | 緩釋膠囊 | Hong Kong Medical Supplies Ltd |
| HK-65460 | GALANTAMINE HYDROBROMIDE EXTENDED-RELEASE CAPSULES 8MG | 緩釋膠囊 | Hong Kong Medical Supplies Ltd |
| HK-67084 | GALANTAMINE-PHARMATHEN PROLONGED-RELEASE CAPSULES 16MG | 緩釋膠囊 | I & C (Hong Kong) Limited |
| HK-67085 | GALANTAMINE-PHARMATHEN PROLONGED-RELEASE CAPSULES 24MG | 緩釋膠囊 | I & C (Hong Kong) Limited |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有模型分數，沒有任何臨床試驗或文獻，也找不到可支持的機轉關聯，證據等級為 L5。
- 同一藥物的其他預測適應症中，「錐體外系及動作疾病」有 2 個精神分裂症試驗和 4 篇文獻，但都屬間接證據。其中 2025 年系統性回顧談的是乙醯膽鹼酯酶抑制劑引起的動作障礙，反而提示可能的不良反應訊號，而非療效。

**若要推進需要：**
- 補齊 Galantamine 的作用機轉資料（DrugBank）。
- 取得香港衛生署的仿單，確認核准適應症、警語與禁忌，這是進入安全性篩選的前提。
- 系統性搜尋 Galantamine 與心因性動作障礙的病例報告和臨床研究，確認是否有任何直接證據。
- 評估膽鹼調節與功能性動作障礙的機轉關聯，再決定是否重新評估。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

