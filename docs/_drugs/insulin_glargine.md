---
layout: default
title: Insulin Glargine
parent: 僅模型預測 (L5)
nav_order: 401
evidence_level: L5
indication_count: 5
---

# Insulin Glargine
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

# Insulin Glargine：從糖尿病到自體免疫性卵巢炎

## 一句話總結

Insulin Glargine 是長效胰島素類似物，廣泛用於糖尿病（第一型/第二型）的血糖控制。
TxGNN 模型預測它可能對**自體免疫性卵巢炎 (Autoimmune Oophoritis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，模型自身的機轉分析也指出此關聯很可能只是知識圖譜中的共病雜訊，而非真實治療訊號。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 糖尿病（第一型/第二型）— 香港許可證資料缺失，此為藥物公開已知用途，非本評估資料來源證實 |
| 預測新適應症 | 自體免疫性卵巢炎 (Autoimmune Oophoritis) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為 Data Gap）。根據 TxGNN 自身提供的機轉推論，自體免疫性卵巢炎常見於自體免疫多腺體症候群（APS type 2），可與第一型糖尿病共存於同一自體免疫體質病人身上——但這是**共病關係**，並非胰島素能治療卵巢炎的藥理依據。胰島素 glargine 沒有已知的內分泌卵巢保護或抗發炎機轉可解釋對卵巢炎的療效。

換言之，這個高分預測很可能反映的是知識圖譜中「胰島素—糖尿病—自體免疫」節點與「卵巢炎—自體免疫」節點之間的**間接共享路徑**，而不是真正的治療機轉關聯。這一點在 evidence pack 的 `repurposing_rationale` 中已被明確標註。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

目前無香港許可證登記（藥物狀態：未上市）。

## 其他候選適應症（同樣缺乏證據）

除排名第一的自體免疫性卵巢炎外，本次還有 4 個候選適應症，皆為 L5 證據等級、無臨床試驗或文獻佐證，且機轉分析同樣指出多屬共病雜訊而非直接治療訊號：

| 排名 | 疾病 | TxGNN 分數 | 機轉關聯摘要 |
|------|------|-----------|-------------|
| 2 | Thiamine-responsive dysfunction syndrome (TRMA) | 99.61% | 患者常因胰島 β 細胞功能不足需用胰島素治療糖尿病表現，屬症狀性共病治療，非針對疾病根本病因 |
| 3 | Classic stiff person syndrome | 99.60% | 與第一型糖尿病共享 anti-GAD65 自體免疫機轉，胰島素治療的是共病糖尿病，非 SPS 本身症狀 |
| 4 | Focal stiff limb syndrome | 99.60% | 與 SPS 譜系相同，機轉路徑高度重疊，無獨立藥理依據 |
| 5 | Opsismodysplasia | 99.59% | INPPL1 基因突變所致骨骼發育不良，與胰島素/糖尿病機轉無已知交集，高度懷疑為知識圖譜雜訊 |

## 安全性考量

安全性資訊請參考原廠仿單。（註：TFDA/香港仿單警語與禁忌症資料目前缺失，屬 Blocking 等級資料缺口，見下方。）

## 結論與下一步

**決策：Hold**

**理由：**
- 5 個預測適應症皆為 L5（僅模型預測），沒有任何臨床試驗或文獻佐證；
- 模型自身的機轉分析顯示，排名前 4 的關聯很可能源於糖尿病/自體免疫共病模式的知識圖譜雜訊，第 5 名（opsismodysplasia）則被判定為機轉上不合理的偽陽性；
- 藥物在香港尚未上市，且缺乏仿單警語/禁忌症資料（DG001，Blocking），無法進行 S1 安全性初評。

**若要推進需要：**
- 補齊 TFDA/香港衛生署仿單警語與禁忌症資料（DG001，Blocking）
- 補充 DrugBank 作用機轉資料（DG002，High）
- 針對排名最高的自體免疫性卵巢炎，擴大檢索是否有病例報告或機轉研究等級證據（目前為 0）
- 若持續無法找到直接證據，建議將此候選整組標記為低優先權或關閉評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

