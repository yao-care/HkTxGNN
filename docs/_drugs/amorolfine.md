---
layout: default
title: Amorolfine
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Amorolfine
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

# Amorolfine：從外用抗黴菌治療到藥物引起的骨質疏鬆

## 一句話總結

Amorolfine 是外用嗎啉類（morpholine）抗黴菌藥，在香港以乳膏和指甲油劑型上市。
TxGNN 模型預測它可能對**藥物引起的骨質疏鬆 (Drug-induced Osteoporosis)** 有效。
目前**沒有任何臨床試驗或文獻**支持這個預測，證據僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 外用抗黴菌治療（香港許可證資料未載明適應症文字） |
| 預測新適應症 | 藥物引起的骨質疏鬆 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 99.998% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Amorolfine 是外用嗎啉類抗黴菌藥，透過抑制黴菌麥角固醇（ergosterol）的生合成來發揮作用。

目前沒有資料顯示這個機轉與骨代謝有關，也看不出原適應症（黴菌感染）與骨質疏鬆之間有明確的病理關聯。此外，外用劑型的全身暴露量低，難以達到影響骨骼的濃度。

因此，這個預測目前只能視為模型輸出的假說，還不能說有機轉上的合理性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66253 | LOMORYL CREAM 2.5MG/G | JULIUS CHEN & COMPANY (HK) LIMITED |
| HK-63887 | NAIL CLEAR NAIL LACQUER 5%W/V | HIND WING CO LTD |
| HK-68692 | LOMORYL NAIL LACQUER 5% W/V | JULIUS CHEN & COMPANY (HK) LIMITED |
| HK-51795 | LOCERYL CREAM 0.25%W/W | GALDERMA HONG KONG LIMITED |
| HK-68691 | LAMOFIN NAIL LACQUER 5% W/V | JULIUS CHEN & COMPANY (HK) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這個預測只有 TxGNN 分數，沒有臨床試驗、文獻或機轉資料支持（L5）。
- 外用抗黴菌藥與骨代謝之間沒有已知關聯，全身暴露量也低。
- 同一批預測的前 10 名（如腹膜後疾病、腰椎狹窄、骨盆腔相關疾病等）同樣都是 L5 且沒有證據，這些預測整體可信度偏低。

**若要推進需要：**
- 補齊 DrugBank 的作用機轉資料，再評估與骨代謝的可能關聯。
- 取得香港衛生署仿單，確認警語與禁忌症。
- 先做前臨床或機轉研究，確認有生物學上的依據，再考慮臨床評估。
- 評估外用劑型是否可能達到足夠的全身暴露，若不可能，需要另行考慮劑型或給藥途徑。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

