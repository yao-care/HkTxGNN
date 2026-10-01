---
layout: default
title: Dihydrocodeine
parent: 僅模型預測 (L5)
nav_order: 272
evidence_level: L5
indication_count: 9
---

# Dihydrocodeine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Dihydrocodeine：從疼痛／咳嗽（藥理類別推論）到鼻腔疾病

## 一句話總結

Dihydrocodeine（雙氫可待因）是一種鴉片類藥物，一般用於止痛與鎮咳。香港許可證資料未載明原適應症，此處為依藥理類別推論。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Dihydrocodeine 屬於鴉片類鎮痛／鎮咳藥，一般認為透過中樞鴉片受體發揮作用，但這是依一般藥理知識推論，並非來自本次提供的資料。

就現有資訊看，這個預測的機轉支持很弱。鴉片類藥物對鼻黏膜病變沒有已知的作用，0.9999 的高分只是知識圖譜的關聯推算，不代表有生物學或臨床依據。若說有關聯，最多只是症狀層面的間接連結，例如咳嗽或不適感的緩解，不是針對鼻腔疾病本身的療效。

因此，這個預測應視為待驗證的假說，不宜視為已有依據的再利用方向。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 11 張許可證，以下列出 5 張主要許可證（資料中未提供劑型與核准適應症）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-65861 | VICK-DICOT TABLETS 30MG | VICKMANS LABORATORIES LTD |
| HK-57588 | DICODEIN TAB 30MG | BRIGHT FUTURE PHARMACEUTICALS FACTORY |
| HK-54981 | REUTOO SYRUP 10MG/5ML | VICKMANS LABORATORIES LTD |
| HK-57139 | DICODEIN ORAL SOLUTION 15MG/5ML | BRIGHT FUTURE PHARMACEUTICALS FACTORY |
| HK-55815 | PARACODONE TAB | BRIGHT FUTURE PHARMACEUTICALS FACTORY |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有模型預測，沒有試驗或文獻，證據等級為 L5。
- 機轉上也找不到合理連結，鴉片類藥物對鼻腔疾病沒有已知作用。
- 同一藥物的其他預測適應症中，頭痛 (Headache Disorder) 有 2 篇間接文獻，分別是止咳糖漿濫用報告與 Cochrane 綜述清單，兩者都未證明療效，且鴉片類藥物本身可能引發藥物過度使用性頭痛，風險與效益方向不明。

**若要推進需要：**
- 取得香港衛生署仿單，確認警語、禁忌與核准適應症（目前為阻擋性資料缺口）
- 從 DrugBank 補齊作用機轉 (MOA)
- 以文獻與試驗檢索，確認鼻腔疾病是否有任何生物學或臨床依據
- 釐清預測的疾病定義與可能的症狀性用途，再評估是否值得投入研究

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

