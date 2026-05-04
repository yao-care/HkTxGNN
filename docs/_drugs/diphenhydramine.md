---
layout: default
title: Diphenhydramine
parent: 僅模型預測 (L5)
nav_order: 208
evidence_level: L5
indication_count: 1
---

# Diphenhydramine
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

# Diphenhydramine：從過敏及失眠治療到玫瑰斑結膜炎

## 一句話總結

Diphenhydramine 是廣為人知的第一代 H1 受體拮抗劑（抗組織胺藥），長期用於過敏、鼻炎及短期失眠的緩解。
TxGNN 模型預測它可能對**玫瑰斑結膜炎（Rosacea Conjunctivitis）** 有效，預測分數高達 **99.20%**。
然而，目前**無任何臨床試驗或文獻**支持此方向，且機轉分析顯示存在潛在的反向生理風險。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏性鼻炎、蕁麻疹、短期失眠（第一代 H1 拮抗劑） |
| 預測新適應症 | 玫瑰斑結膜炎（Rosacea Conjunctivitis） |
| TxGNN 預測分數 | 99.20% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Diphenhydramine 是第一代 H1 受體拮抗劑，同時具備抗組織胺、抗膽鹼及局部麻醉三種特性。理論上，H1 拮抗作用可減緩組織胺引發的血管擴張與搔癢感，而玫瑰斑結膜炎（ocular rosacea）的確存在慢性眼部發炎與搔癢症狀，這可能是 TxGNN 知識圖譜中 diphenhydramine–conjunctivitis–inflammation 間接路徑被激活的原因。

然而，玫瑰斑結膜炎的核心發病機轉是**慢性神經血管炎症、瞼板腺功能障礙（meibomian gland dysfunction）及先天免疫失調**，並非以 IgE 介導的過敏反應為主。因此，H1 拮抗的治療連結屬於間接且機轉匹配度偏低的假設。

更值得警惕的是，Diphenhydramine 強烈的**抗膽鹼效應**可能抑制淚液分泌，加重玫瑰斑患者本已常見的乾眼症狀，形成**反向生理風險**。TxGNN 的高分預測（0.9920）推測主要反映知識圖譜中的間接連結，而非直接的臨床適應症支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

Diphenhydramine 目前在香港**未有已登記許可證**，無核准上市產品資料可供查閱。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **特別注意**：根據藥理機轉分析，Diphenhydramine 的抗膽鹼效應可能**加重乾眼症狀**，對於玫瑰斑結膜炎患者而言存在潛在的反向生理風險，在獲得更多安全性資料前應審慎評估。

---

## 結論與下一步

**決策：Hold**

**理由：**
預測分數雖高（99.20%），但此分數主要反映知識圖譜中的間接關聯路徑，而非直接的臨床適應症依據。目前完全缺乏臨床試驗與文獻支持（L5），加上 Diphenhydramine 抗膽鹼效應可能惡化玫瑰斑結膜炎患者的乾眼症狀，機轉上存在明顯的反向生理風險，不建議優先推進此再利用候選。

**若要推進需要：**
- 補充 Diphenhydramine 完整作用機轉（MOA）資料，釐清 H1 拮抗與眼部炎症的實際關聯
- 系統性文獻搜尋（擴大至 ocular rosacea、dry eye、antihistamine 等交叉詞彙）
- 評估局部眼用劑型（eye drops）是否可規避全身抗膽鹼副作用
- 獲取香港或其他地區的上市許可證資料，了解目前核准的安全性輪廓
- 考慮以乾眼症（dry eye）/過敏性結膜炎（allergic conjunctivitis）作為替代預測方向，機轉匹配度可能更高
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

