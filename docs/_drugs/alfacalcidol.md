---
layout: default
title: Alfacalcidol
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Alfacalcidol：預測新適應症為家族性孤立性副甲狀腺功能低下症（familial isolated hypoparathyroidism due to impaired…（證據等級 L5）。原適應症：副甲狀腺功能亢進、纖維性骨炎、副甲狀腺功能低下、腎性骨病變"
monitor_inn: "ALFACALCIDOL"
predicted_indications: ["familial isolated hypoparathyroidism due to impaired PTH secretion", "Dahlberg-Borer-Newcomer syndrome", "craniofacial conodysplasia", "acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis"]
---

# Alfacalcidol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Alfacalcidol：從副甲狀腺功能亢進到家族性孤立性副甲狀腺功能低下症

## 一句話總結

Alfacalcidol 是 1-α-羥基化的活性維生素 D 類似物，原本用於副甲狀腺功能亢進、纖維性骨炎、副甲狀腺功能低下及腎性骨病變。
TxGNN 模型預測它可能對**家族性孤立性副甲狀腺功能低下症（PTH 分泌受損型）**有效，分數很高（99.6%）。
但目前**沒有臨床試驗與文獻**直接支持，證據僅來自模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 副甲狀腺功能亢進、纖維性骨炎、副甲狀腺功能低下、腎性骨病變（來自知識圖譜；香港許可證未登載適應症文字） |
| 預測新適應症 | 家族性孤立性副甲狀腺功能低下症（familial isolated hypoparathyroidism due to impaired PTH secretion） |
| TxGNN 預測分數 | 99.61% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。不過 alfacalcidol 已是 1-α-羥基化的維生素 D，可繞過腎臟 1-α-羥化酶，不依賴 PTH 就能提高血鈣。對 PTH 缺乏的狀態來說，這在生物學上是合理的。

家族性孤立性副甲狀腺功能低下症是副甲狀腺功能低下的遺傳亞型，而後者本來就是 alfacalcidol 的既有適應症。因此這個預測較可能只是原適應症的延伸，**不太算是真正的藥物再利用**。

高分（0.996）僅是模型預測。針對這個亞型，沒有檢索到任何臨床試驗或文獻。

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
| HK-37801 | ALPHA D3 0.25MCG CAP 0.25MCG | 未提供 | 未提供 |
| HK-65502 | JECEFARMA ALFACALCIDOL CAPSULES 1MCG | 未提供 | 未提供 |
| HK-37802 | ALPHA D3 1MCG CAP 1MCG | 未提供 | 未提供 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

另外，alfacalcidol 作用於鈣代謝，臨床使用時一般需留意血鈣與腎功能的監測。

---

## 其他排名較後的預測（供參考）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 摘要 |
|------|-----------|-----------|---------|------|
| 2 | Dahlberg-Borer-Newcomer 症候群（疑為 Fanconi-Bickel 症候群的異名） | 99.60% | L5 | 活性維生素 D 只用於骨骼與礦物質併發症的支持治療，不針對根本缺陷。檢索到的文獻多與主題無關，沒有 alfacalcidol 的直接證據 |
| 3 | 顱面錐形發育不良 | 99.55% | L5 | 無法建立機轉連結，也無試驗或文獻 |
| 4 | 肢中型發育不良（Campailla-Martinelli 型） | 99.53% | L5 | 非維生素 D 或鈣缺乏所致，推測僅是知識圖譜中骨骼相關節點的鄰近性 |
| 5 | 腎小管酸中毒 | 99.27% | L4 | 有 4 篇病例報告顯示骨軟化症在合併治療後改善，但無法分離出 alfacalcidol 單獨的效果；需留意高鈣尿症與腎鈣化風險 |

其中以腎小管酸中毒的證據相對較多，屬值得進一步探討的研究問題；其餘皆缺乏支持。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測與既有適應症（副甲狀腺功能低下）高度重疊，沒有針對該亞型的試驗或文獻，證據等級僅 L5。
- 香港許可證的適應症文字與仿單警語、禁忌資料皆缺漏，目前無法完成安全性篩選。

**若要推進需要：**
- 取得香港衛生署許可證仿單，補齊核准適應症、警語與禁忌症
- 補充 DrugBank 的作用機轉資料
- 確認首位預測是否只是既有適應症的延伸，而非新適應症
- 若要追蹤其他方向，可針對腎小管酸中毒所致骨軟化症，蒐集 alfacalcidol 的系統性回顧或對照研究證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

