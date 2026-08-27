---
layout: default
title: Hydroxocobalamin
parent: 僅模型預測 (L5)
nav_order: 379
evidence_level: L5
indication_count: 2
---

# Hydroxocobalamin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Hydroxocobalamin：從維生素B12相關療法到食道靜脈曲張出血

## 一句話總結

Hydroxocobalamin（羥鈷胺）為維生素B12衍生物，過去用於維生素B12缺乏症與氰化物中毒解毒。TxGNN 模型預測它可能對**食道靜脈曲張出血 (Esophageal Varices with Bleeding)** 有效，但目前**無任何臨床試驗或文獻支持**，屬純模型層級的推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（此藥品未在香港取得許可證，無官方核准適應症紀錄）；文獻普遍記載其用於維生素B12缺乏症及氰化物中毒解毒 |
| 預測新適應症 | 食道靜脈曲張出血 (Esophageal Varices with Bleeding) |
| TxGNN 預測分數 | 99.23% |
| 證據等級 | L5（僅有模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Hydroxocobalamin 詳細的官方作用機轉資料（MOA 為 Data Gap），無法從原廠文件直接確認其藥理路徑。根據已知藥理學資訊，Hydroxocobalamin 具有**一氧化氮（NO）清除**特性，臨床上已被用於治療血管擴張性休克（如敗血性休克）以提升血壓——這是其核心已知藥理作用之一。

食道靜脈曲張出血的病理機轉之一，是肝硬化門脈高壓導致內臟循環（splanchnic circulation）因 NO 過度產生而擴張，使門脈血流增加、門脈壓上升。理論上，Hydroxocobalamin 的 NO 清除作用可能降低內臟血管擴張，進而降低門脈壓——這可能是 TxGNN 模型在知識圖譜中捕捉到的間接機轉關聯。

需特別注意：這是**推論性連結**，並非經過驗證的機轉。模型對「有出血」與「無出血」兩種食道靜脈曲張給出完全相同的分數（99.23%），顯示模型可能未區分急性/慢性臨床情境，僅反映疾病節點在知識圖譜中的鄰近性，不等同於臨床證據。原始核准適應症資料也缺失，無法確認此藥理特性是否曾在肝硬化/門脈高壓族群中系統性驗證過。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，僅有 TxGNN 模型預測分數，無任何臨床試驗或文獻支持此適應症方向。
- 機轉連結（NO 清除 → 降低門脈壓）目前僅為理論推論，且模型未能區分「有出血」與「無出血」兩種臨床情境，可信度存疑。

**若要推進需要：**
- 補齊 Hydroxocobalamin 完整作用機轉（MOA）資料（可透過 DrugBank API 查詢，對應 Data Gap DG002）
- 取得原廠仿單警語與禁忌症資料，完成安全性初評（Data Gap DG001，屬 Blocking 等級，需先解決才能進入 S1 階段）
- 針對「NO 清除作用是否能降低門脈壓」進行機轉層級的前臨床或藥理學文獻搜尋，以補強機轉關聯性
- 持續監測是否有新登記的臨床試驗或病例報告，目前兩個相關搜尋（含/不含出血）皆無結果
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

