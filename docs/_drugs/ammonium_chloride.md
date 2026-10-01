---
layout: default
title: Ammonium Chloride
parent: 僅模型預測 (L5)
nav_order: 54
evidence_level: L5
indication_count: 2
---

# Ammonium Chloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ammonium Chloride（氯化銨）：從祛痰複方到急性喉咽炎

## 一句話總結

Ammonium Chloride（氯化銨）在香港以祛痰類複方咳嗽藥的成分上市，資料中沒有登錄正式的原適應症。
TxGNN 模型預測它可能對**急性喉咽炎 (Acute Laryngopharyngitis)** 有效。
目前**沒有臨床試驗，也沒有文獻**支持，這只是模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 急性喉咽炎 (Acute Laryngopharyngitis) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，資料中也沒有登錄原適應症。以下說明來自一般藥理知識，不是本資料集的內容。氯化銨常用於咳嗽感冒複方中作為祛痰劑，可能透過胃部刺激反射促進呼吸道分泌物排出。香港上市的相關產品名稱（如 Expectorant、Syrup）也符合這個用途。

急性喉咽炎屬於上呼吸道發炎，機轉上可能與祛痰、改變分泌物的作用有間接關聯。這個關聯尚未經驗證，也沒有任何試驗或文獻支持。高圖譜分數本身不等於臨床證據。

TxGNN 另外預測了**鼻腔疾病 (Nasal Cavity Disease)**（分數 99.94%，同為 L5）。這個疾病名稱太籠統，任何機轉連結都只是推測。若要進一步評估，需先界定具體的鼻部病症。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

資料中共有 20 張許可證，以下列出 5 張主要許可證。劑型與核准適應症欄位在來源資料中皆為空白。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-43251 | UNI-COPHEDENE SYRUP | Universal Pharmaceutical Laboratories, Limited |
| HK-07157 | UNI-PHEN EXPECTORANT | Universal Pharmaceutical Laboratories, Limited |
| HK-08384 | DIPHENAMINE EXPECTORANT | Vickmans Laboratories Ltd |
| HK-64814 | AXCEL FLEMIN EXPECTORANT SYRUP | Kotra Pharma (Hong Kong) Company |
| HK-54338 | BEANAMINE EXPECTORANT | Prudentlink Limited |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
兩個預測適應症都只有模型分數，沒有臨床試驗、文獻或已確認的機轉，證據等級為 L5。作用機轉與香港仿單的警語、禁忌症也都缺資料，無法進入安全性篩選。

**若要推進需要：**
- 從香港衛生署下載並解析仿單，補齊警語與禁忌症
- 從 DrugBank 補齊作用機轉 (MOA) 與原適應症
- 系統性搜尋氯化銨用於急性喉咽炎的臨床與文獻證據
- 界定「鼻腔疾病」預測所指的具體病症
- 評估給藥途徑是否與新適應症相容

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

