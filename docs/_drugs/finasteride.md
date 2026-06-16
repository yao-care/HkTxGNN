---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 318
evidence_level: L5
indication_count: 5
---

# Finasteride
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

# Finasteride：從雄激素性禿髮到 Ambras 型先天性普遍性多毛症

## 一句話總結

Finasteride 是第二型 5α-reductase 抑制劑（5α-RI），臨床上用於治療男性雄激素性禿髮及良性前列腺增生。
TxGNN 模型預測它可能對 **Ambras 型先天性普遍性多毛症 (Ambras type hypertrichosis universalis congenita)** 等 5 項罕見疾病有效，
然而目前**無任何臨床試驗或直接相關文獻**支持，且機轉分析顯示預測合理性極低。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 雄激素性禿髮、良性前列腺增生（香港無上市許可證）|
| 預測新適應症 | Ambras 型先天性普遍性多毛症 (Ambras type hypertrichosis universalis congenita) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏正式的作用機轉登錄資料（香港仿單及 DrugBank MOA 均為資料缺口）。根據已知藥理，Finasteride 透過抑制 5α-reductase，減少睪固酮轉化為二氫睪固酮（DHT），從而降低雄激素敏感性毛囊的退化速度，發揮護髮及縮小前列腺體積的效果。

然而，**Ambras 型先天性普遍性多毛症的致病機轉與雄激素完全無關。** Ambras 症候群由 8q22-q24 染色體重排導致 TRPS1 附近基因異位表達所致，屬先天性非雄激素依賴性多毛症；5α-RI 對非雄激素路徑的毛囊激活無效，機轉對應度極低。TxGNN 模型可能因「毛髮相關」的表面語義連結而產生此預測，但 Ambras 症候群（過多毛髮生長）與雄激素性禿髮（毛囊萎縮退化）在病理方向上恰好相反，不宜直接類推。

其餘 4 項預測的機轉關聯度同樣極低：一般性多毛症（hypertrichosis）定義上為非雄激素依賴性；牙周-牙齒畸形症候群的理論連結屬高度推測性，且 Finasteride 本身曾有藥物誘發性牙齦增生之不良反應報告；Dandy-Walker 畸形為先天性腦發育異常，與 5α-RI 機轉毫無交集；遺傳性毛幹異常源於毛幹角蛋白基因突變，非毛囊雄激素敏感性問題。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無與 Finasteride 及上述預測適應症直接相關的文獻。

> **補充說明**：第 3 項預測（牙周-牙齒畸形症候群）雖於 PubMed 檢索到 20 篇文獻，但均為牙周病學通論文獻（牙周炎治療指引、糖尿病與牙周炎雙向關係、牙齦纖維母細胞病理等），無一涉及 Finasteride 的應用，**不構成本藥物的有效支持證據**。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
所有 5 項預測適應症均為 L5 等級（僅模型預測，無臨床試驗及文獻支持），且機轉分析顯示預測適應症與 Finasteride 的雄激素拮抗機轉普遍不匹配，缺乏生物合理性，不具備進入 S1 安全性初評的條件。

**若要推進需要：**
- 補充 DrugBank MOA 及香港仿單，以建立完整的安全性基線資料
- 重新評估 TxGNN 預測的生物合理性篩選機制，本批次預測存在系統性語義關聯偏差（毛髮相關詞彙聚集）
- 若欲探索毛髮相關再利用方向，建議聚焦於**雄激素依賴性多毛症（hirsutism）**，而非先天性/非雄激素性多毛症（hypertrichosis），前者在機轉上存在合理連結
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

