---
layout: default
title: Alfacalcidol
parent: 中證據等級 (L3-L4)
nav_order: 30
evidence_level: L4
indication_count: 5
---

# Alfacalcidol
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Alfacalcidol：從 鈣磷代謝疾病 到 家族性孤立性副甲狀腺機能低下症（PTH分泌受損型）

## 一句話總結

Alfacalcidol（1α-羥基維生素D₃）是活性維生素D類似物，廣泛用於腎性骨病、佝僂症及副甲狀腺功能低下症等鈣磷代謝疾病的治療。TxGNN 模型預測它可能對 **PTH分泌受損型家族性孤立性副甲狀腺機能低下症 (Familial Isolated Hypoparathyroidism due to Impaired PTH Secretion)** 有效。目前搜尋到 **0 個臨床試驗**及 **0 篇直接文獻**（可能因疾病命名特殊性導致搜尋遺漏），但機轉連結強度評定為 **A 級**，直接對應疾病核心病理生理缺陷。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無香港許可證記錄（依藥學文獻，廣泛用於腎性骨病、副甲狀腺功能低下症及佝僂症） |
| 預測新適應症 | PTH分泌受損型家族性孤立性副甲狀腺機能低下症 (Familial Isolated Hypoparathyroidism due to Impaired PTH Secretion) |
| TxGNN 預測分數 | 99.61% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 資料缺口待補充）。根據已知藥理資訊，Alfacalcidol（1α-羥基膽鈣化醇）是維生素D的活性類似物，口服後在肝臟經25-羥化酶迅速轉化為骨化三醇（1,25-(OH)₂D₃），**不需腎臟CYP27B1（1α-羥化酶）的參與**。這一特性正是其在1α-羥化步驟受損場景下的核心藥理優勢。

PTH分泌受損型家族性孤立性副甲狀腺機能低下症的病理鏈清晰：PTH分泌缺陷 → 腎小管1α-羥化酶（CYP27B1）活性驅動不足 → 25-OH D無法有效轉化為活性骨化三醇 → 持續性低血鈣與高血磷。Alfacalcidol完全繞過PTH驅動的腎臟1α-羥化環節，直接在肝臟羥化為骨化三醇，從根本上補充因PTH缺乏而無法自行產生的活性維生素D，此機轉連結被評定為 **A 級——直接針對疾病核心病理生理缺陷**。

值得特別指出的是，Alfacalcidol用於一般性副甲狀腺功能低下症的臨床應用在全球多國已建立多年。本次搜尋顯示0篇文獻，很可能係因本疾病的特定罕見病命名（"familial isolated hypoparathyroidism due to impaired PTH secretion"）導致的搜尋策略不匹配，而非真正缺乏臨床應用紀錄。強烈建議以「hypoparathyroidism AND alfacalcidol」等更廣泛的策略補充搜尋後重新評估。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無針對此適應症的直接相關文獻。

> **⚠️ 搜尋備註**：Evidence Pack 記錄0篇文獻，但依據再利用理由評估（A 級機轉連結），此極可能為疾病名稱特殊性所致之搜尋遺漏，而非實際臨床使用空缺。建議以「hypoparathyroidism AND alfacalcidol」或「vitamin D analog AND hypoparathyroidism」擴大文獻搜尋策略後重新評估。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Alfacalcidol 的藥理作用機轉與本適應症的核心病理生理缺陷直接對應（**A 級機轉連結**），TxGNN 預測分數達 99.61%。其於副甲狀腺功能低下症的全球臨床應用已有長期實踐基礎，理論依據充分；現有文獻空白很可能源於疾病罕見命名導致的搜尋策略不匹配，而非臨床缺乏應用記錄。

**若要推進需要：**
- 擴大文獻搜尋（策略：「hypoparathyroidism AND alfacalcidol」、「1α-hydroxyvitamin D AND PTH deficiency」），確認現有臨床應用與有效性證據
- 補充正式作用機轉資料（查詢 DrugBank API 取得完整 MOA，DrugBank ID：DB01436）
- 取得香港或其他已上市地區之完整仿單，評估禁忌症、劑量調整建議及藥物交互作用（目前均為資料缺口）
- 確認是否符合罕見疾病適應症申請資格（本適應症屬罕見病範疇，可能享有加速審查路徑）
- 訂定特定族群（兒科患者、合併腎功能不全者）的安全性監測計畫，防範高血鈣等維生素D毒性風險
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

