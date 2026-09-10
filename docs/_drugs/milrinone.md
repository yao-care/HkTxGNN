---
layout: default
title: Milrinone
parent: 僅模型預測 (L5)
nav_order: 498
evidence_level: L5
indication_count: 5
---

# Milrinone
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

# MILRINONE：原適應症資料缺失，預測新適應症為 Alopecia（禿髮）

## 一句話總結

MILRINONE（DrugBank ID: DB00235）目前資料庫中缺乏原始適應症與作用機轉記錄，於香港也尚未取得任何許可證上市。
TxGNN 模型預測它可能對**Alopecia（禿髮）**有效，預測分數高達 99.91%，
但目前**無任何臨床試驗或文獻**支持這個方向，屬於純模型預測（L5）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料庫無記錄（原始適應症、MOA 均為資料缺口） |
| 預測新適應症 | Alopecia（禿髮） |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 MILRINONE 詳細的正式作用機轉（MOA）資料庫記錄。根據 Evidence Pack 中提供的機轉推論：MILRINONE 為 PDE3 抑制劑，透過提升細胞內 cAMP 產生血管擴張作用。這個假說是理論上仿效 minoxidil（不同機轉的血管擴張/K⁺ channel opener）增加毛囊血流、進而促進毛髮生長的類比推論。

但此連結**沒有任何直接機轉研究或動物/細胞層級證據**支持 PDE3 抑制與毛囊生長訊號路徑的關聯，純粹是 TxGNN 預測分數驅動的推論性類比，機轉合理性偏弱。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 安全性考量

安全性資訊請參考原廠仿單。（注：目前存在一項 Blocking 等級資料缺口 — TFDA 仿單警語/禁忌尚未取得，導致此候選無法進入 S1 安全性初評。）

## 結論與下一步

**決策：Hold**

**理由：**
Alopecia 這項預測僅有 TxGNN 模型分數支持，無任何臨床試驗、文獻或機轉層級證據；藥物在香港尚未上市（0 張許可證）；且安全性資料存在阻斷級缺口（DG001），目前無法進行安全性初評。

**若要推進需要：**
- 補齊 TFDA 仿單警語與禁忌症資料（DG001，Blocking，會員無法進入 S1 前必須解決）
- 補齊 MILRINONE 作用機轉（MOA）資料（DG002，High）
- 對 PDE3 抑制與毛囊生長訊號路徑進行機轉層級或臨床前驗證研究
- 評估香港上市可行性（目前 0 張許可證）

**補充：** 本次 Evidence Pack 同時列出其他 4 個候選適應症（hypotrichosis simplex of the scalp、congenital hypotrichosis milia、diffuse alopecia areata、headache disorder）。其中 headache disorder 因有 3 篇個案文獻描述 milrinone 動脈內注射治療可逆性腦血管收縮症候群（RCVS），證據等級達 L4／S1（Research Question），機轉合理性優於 Alopecia，但其與廣義「headache disorder」標籤本身關聯薄弱（實際對應的是 RCVS 這一特定亞型）。若後續要推進，建議優先評估此候選而非 Alopecia。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

