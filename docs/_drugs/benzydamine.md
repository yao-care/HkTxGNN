---
layout: default
title: Benzydamine
parent: 僅模型預測 (L5)
nav_order: 107
evidence_level: L5
indication_count: 1
---

# Benzydamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Benzydamine：從咽喉局部消炎止痛到良性前列腺增生

## 一句話總結

Benzydamine 在香港以漱口液、咽喉噴劑、含片等局部劑型上市，許可證資料未載明適應症，依品名與劑型推測為口咽局部消炎止痛。
TxGNN 模型預測它可能對**良性前列腺增生 (Benign Prostatic Hyperplasia, BPH)** 有效。
目前**沒有臨床試驗和文獻**支持，僅有模型分數。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明（依品名推測為咽喉局部消炎，需查原廠仿單確認） |
| 預測新適應症 | 良性前列腺增生 (Benign Prostatic Hyperplasia) |
| TxGNN 預測分數 | 99.26% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前沒有完整的作用機轉資料可供查核，TxGNN 的知識圖譜連結因此無法對照原始紀錄驗證。一般認為 Benzydamine 是局部作用的消炎止痛藥，可能降低促發炎細胞激素（如 TNF-α、IL-1β），並具有穩定細胞膜的作用。

慢性前列腺發炎被認為可能與 BPH 的發生有關，所以「抗發炎 → BPH」在理論上說得通。不過這只是未經驗證的假說。

有兩點需要保留：
- Benzydamine 對 BPH 的既有標靶（5-α 還原酶、α1 腎上腺素受體）沒有已知作用。
- 已上市產品（漱口液、噴劑、外用）為局部使用，全身暴露量低，能否在前列腺組織達到有效濃度並不清楚。

因此 99.26% 的分數只能視為計算層面的假說，不能當作療效證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證。資料中劑型與核准適應症欄位皆為空白。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-59261 | ZUHOTAN SPRAY 1.5MG/ML | VAST RESOURCES PHARMACEUTICAL LTD |
| HK-31754 | DIFFLAM SOLN FOR GARGLE 0.15% | INOVA PHARMACEUTICALS (HONG KONG) LIMITED |
| HK-42350 | DANTUM SOLUTION 0.15% | SYNCO (H.K.) LIMITED |
| HK-56224 | DIFFLAM ANTI-INFLAMMATORY THROAT SPRAY 0.15% | INOVA PHARMACEUTICALS (HONG KONG) LIMITED |
| HK-42365 | DIFFLAM ANTI-INFLAMMATORY LOZ 3MG S/F | INOVA PHARMACEUTICALS (HONG KONG) LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 只有 TxGNN 模型分數，沒有任何臨床試驗或文獻，證據等級為 L5。
- 香港現有產品皆為局部劑型，全身暴露量低，是否適用於前列腺尚屬未知。

**若要推進需要：**
- 取得香港衛生署的仿單，確認原核准適應症與安全性資訊（警語、禁忌）。
- 補齊作用機轉資料，例如從 DrugBank 查詢。
- 檢索 Benzydamine 與前列腺發炎、BPH 相關的前臨床或機轉研究。
- 評估給藥途徑與組織分佈，確認局部劑型能否作用於前列腺。
- 若有初步支持證據，再評估是否需要新劑型或全身給藥的可行性。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

