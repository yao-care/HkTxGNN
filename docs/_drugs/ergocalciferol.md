---
layout: default
title: Ergocalciferol
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 10
---

# Ergocalciferol
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

# Ergocalciferol：從維生素 D 補充到家族性孤立性副甲狀腺功能低下症

## 一句話總結

Ergocalciferol（維生素 D2）是維生素 D 的一種形式，在香港以複方營養製劑（靜脈脂溶性維生素、嬰兒藥膏、營養粉劑等）上市。
TxGNN 模型預測它可能對**家族性孤立性副甲狀腺功能低下症（因 PTH 分泌受損）**有效。
目前**沒有臨床試驗，也沒有文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症文字 |
| 預測新適應症 | 家族性孤立性副甲狀腺功能低下症 (familial isolated hypoparathyroidism due to impaired PTH secretion) |
| TxGNN 預測分數 | 99.85%（模型排名 3634） |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，ergocalciferol 是維生素 D 類化合物，本品在香港以複方製劑形式上市，其成分在維生素 D 缺乏與鈣磷代謝異常的療效已被廣泛使用。機轉上可能適用於副甲狀腺功能低下症。

副甲狀腺功能低下症的核心問題是 PTH 不足，導致低血鈣。臨床上常用維生素 D 類藥物矯正低血鈣，這是預測看似合理的主要原因。

但有一個限制要注意：PTH 不足時，腎臟將維生素 D 轉成活性型（1,25-二羥基維生素 D）的能力會下降。依一般藥理知識，原型維生素 D（如 ergocalciferol）在這類疾病的效果可能不如活性型類似物。這一點需要進一步查證。目前資料中沒有任何證據顯示 ergocalciferol 對此疾病有效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-36205 | VITALIPID N INFANT INJ（Fresenius Kabi Hong Kong） | 未載明 | 未載明 |
| HK-36206 | VITALIPID N ADULT INJ（Fresenius Kabi Hong Kong） | 未載明 | 未載明 |
| HK-01178 | POLIBABY CREAM（Sato Pharmaceutical (HK)） | 未載明 | 未載明 |
| HK-52479 | AMINOLEBAN EN POWDER（Otsuka Pharmaceutical (H.K.)） | 未載明 | 未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
這個預測只有模型分數，沒有任何臨床試驗或文獻佐證（L5）。香港許可證資料也沒有載明適應症與警語。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語、禁忌與適應症（目前是阻擋性缺口）
- 從 DrugBank 補上作用機轉資料
- 針對「ergocalciferol 用於副甲狀腺功能低下症」做專門文獻檢索，並釐清原型維生素 D 與活性型的療效差異
- 若要在同一藥物上找較有依據的方向，同一份資料中的**腎性骨病變**與**低磷佝僂病**（兩者皆為 L3）證據較多，可優先評估。其中腎性骨病變已有 Phase 4 試驗 NCT01799317（ergocalciferol 合併 doxercalciferol，狀態未知）

本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

