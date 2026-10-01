---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 423
evidence_level: L5
indication_count: 5
---

# Guselkumab
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

# Guselkumab：從（原適應症資料缺漏）到藥物性骨質疏鬆症

## 一句話總結

Guselkumab 是抗 IL-23（p19 次單元）單株抗體，在香港以 Tremfya 品牌上市，但許可證資料未載明原適應症。
TxGNN 模型預測它可能對**藥物性骨質疏鬆症 (Drug-induced Osteoporosis)** 有效，
目前**沒有任何臨床試驗或文獻**支持這個預測，僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺漏（香港許可證未載明適應症文字） |
| 預測新適應症 | 藥物性骨質疏鬆症 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Guselkumab 阻斷 IL-23 的 p19 次單元。IL-23/IL-17 軸被認為可能影響 RANKL 介導的破骨細胞生成，所以理論上有骨保護作用的可能。

不過這個連結**純屬推測**。糖皮質素引起的骨流失，主要機轉與 IL-23/IL-17 軸不同。0.998 的分數是模型輸出，不是臨床證據。

Evidence Pack 缺少 DrugBank 的正式作用機轉欄位，上述機轉是依預測理由整理而來，需再以 DrugBank 資料確認。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 補充：其他預測適應症的證據

Evidence Pack 中，**乾癬 (Psoriasis)** 排名第 3（分數 99.75%），有大量證據，證據等級為 L1，決策為 Proceed with Guardrails。
但乾癬很可能是 guselkumab 的**既有核准適應症**。原適應症欄位為空是資料缺漏所致，所以這不算真正的老藥新用，需對照香港核准仿單確認。

**代表性臨床試驗（乾癬）**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02325219](https://clinicaltrials.gov/study/NCT02325219) | Phase 3 | 完成 | 192 | 對照安慰劑，評估中重度斑塊型乾癬療效 |
| [NCT03818035](https://clinicaltrials.gov/study/NCT03818035) | Phase 3 | 完成 | 880 | 超級反應者延長給藥間隔至 16 週的維持效果 |
| [NCT02951533](https://clinicaltrials.gov/study/NCT02951533) | Phase 3 | 完成 | 119 | 與富馬酸酯比較，用於未接受過全身性治療者 |
| [NCT03573323](https://clinicaltrials.gov/study/NCT03573323) | Phase 4 | 完成 | 1027 | Ixekizumab 對比 guselkumab 的 24 週療效與安全性 |

**代表性文獻（乾癬）**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28057360](https://pubmed.ncbi.nlm.nih.gov/28057360/) | 2017 | RCT | J Am Acad Dermatol | VOYAGE 1：療效優於 adalimumab 與安慰劑 |
| [28057361](https://pubmed.ncbi.nlm.nih.gov/28057361/) | 2017 | RCT | J Am Acad Dermatol | VOYAGE 2：含隨機停藥與再治療，療效優於 adalimumab |
| [28635018](https://pubmed.ncbi.nlm.nih.gov/28635018/) | 2018 | RCT | Br J Dermatol | NAVIGATE：對 ustekinumab 反應不佳者仍有療效 |
| [31402114](https://pubmed.ncbi.nlm.nih.gov/31402114/) | 2019 | RCT | Lancet | ECLIPSE：第 48 週療效優於 secukinumab |

提醒：試驗清單中沒有列出 Phase 3 註冊試驗的 NCT 紀錄（列出的 Phase 3 試驗多為 3b），Phase 3 證據主要來自上述文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65944 | TREMFYA 注射液（預充填注射針筒 100mg/1ml） | 注射劑（預充填注射針筒） | 許可證資料未載明 |
| HK-67037 | TREMFYA 注射液（預充填注射筆 100mg/1ml） | 注射劑（預充填注射筆） | 許可證資料未載明 |

兩張許可證的持有廠商皆為 Johnson & Johnson (Hong Kong) Ltd.。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 針對藥物性骨質疏鬆症，目前只有模型預測，沒有臨床試驗或文獻，機轉也屬推測，且與糖皮質素引起的骨流失主要機轉不同。
- 骨相關預測（藥物性骨質疏鬆、腎性骨病變）與視網膜病變預測，同樣都是 L5，不應視為獨立證據。

**若要推進需要：**
- 補齊香港衛生署仿單中的適應症、警語與禁忌症
- 查詢 DrugBank，取得正式作用機轉
- 進行 IL-23/IL-17 與骨代謝的前臨床或機轉文獻回顧
- 確認乾癬是否為既有核准適應症，並以正確的原適應症重新歸類預測
- 若要評估乾癬使用，遵循現行生物製劑指引（如 AAD-NPF），並在治療前篩檢感染與結核風險

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

