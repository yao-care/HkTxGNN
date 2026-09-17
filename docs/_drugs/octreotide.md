---
layout: default
title: Octreotide
parent: 僅模型預測 (L5)
nav_order: 537
evidence_level: L5
indication_count: 2
---

# Octreotide
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

# Octreotide：從內分泌腫瘤適應症到 Vulvar Inverted Follicular Keratosis

## 一句話總結

Octreotide（DrugBank DB00104）是 somatostatin 類似物，透過 SSTR1-5 受體抑制生長激素、胰島素及胃腸胰內分泌分泌，臨床上用於肢端肥大症、類癌症候群等疾病。TxGNN 模型預測它可能對罕見皮膚病灶「**外陰倒生性毛囊角化症 (Vulvar Inverted Follicular Keratosis)**」有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型相似度分數。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | [Data Gap]（本證據包未提供正式清單；已知臨床用途含肢端肥大症、類癌症候群等，見下方機轉說明） |
| 預測新適應症 | Vulvar Inverted Follicular Keratosis（外陰倒生性毛囊角化症） |
| TxGNN 預測分數 | 99.58% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 標記為 [Data Gap]）。根據證據包中的機轉推論，Octreotide 為 somatostatin 類似物，主要透過 SSTR1-5 受體抑制生長激素、胰島素、胃腸胰內分泌分泌，臨床用於肢端肥大症、類癌症候群、食道靜脈曲張出血等。

Vulvar inverted follicular keratosis 屬毛囊良性角化增生病灶，與 somatostatin 訊號路徑、生長激素軸或已知 octreotide 藥理作用**沒有可辨識的生物學關聯**。此預測僅來自 TxGNN 知識圖譜嵌入相似度（score 0.996），並無機轉假說支持。

第二順位候選「脂漏性角化症 (Seborrheic Keratosis)」情況類似：該病致病機轉主要涉及 FGFR3、PIK3CA 體突變，與 somatostatin 受體訊號無已知交集，同樣僅為 embedding 相似度預測（score 0.995），無臨床或機轉佐證。

---

## 臨床試驗證據

目前無相關臨床試驗登記

---

## 文獻證據

目前無相關文獻

---

## 香港上市資訊

Octreotide 目前**未在香港取得任何藥品許可證登記**（total_licenses: 0），故無許可證資料可列。

---

## 安全性考量

安全性資訊請參考原廠仿單。（本證據包中的仿單警語、禁忌症及藥物交互作用查詢均為資料缺口）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一支持證據為 TxGNN 相似度分數（L5，無臨床試驗、無文獻），且模型本身推論的機轉關聯性極弱甚至無關聯。
- 香港未上市、無許可證，仿單警語/禁忌症資料為 Blocking 缺口，尚無法進入安全性初評 (S1)。

**若要推進需要：**
- 補齊 Octreotide 仿單警語與禁忌症資料（Blocking gap，DG001）
- 補齊 DrugBank MOA 詳細資料（DG002）
- 針對兩個候選適應症搜尋是否有 somatostatin 路徑與皮膚角化增生相關的機轉研究或個案報告
- 確認香港上市/許可證申請狀態
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

