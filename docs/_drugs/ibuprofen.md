---
layout: default
title: Ibuprofen
parent: 僅模型預測 (L5)
nav_order: 383
evidence_level: L5
indication_count: 5
---

# Ibuprofen
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

# Ibuprofen：從資料缺口的原適應症到肢端骨骼發育不全症（Acromesomelic Dysplasia, Hunter-Thompson Type）

## 一句話總結

Ibuprofen（DrugBank ID: DB01050）目前**原始適應症清單與正式 MOA 資料皆為缺口**，僅能從證據包內的機轉描述得知其為 COX-1/COX-2 抑制劑（NSAID 類）。TxGNN 模型針對此藥給出 5 項罕見骨骼/肌肉相關疾病預測，最高分為**肢端骨骼發育不全症 Hunter-Thompson 型**（預測分數 99.74%），但**目前無任何臨床試驗或文獻佐證**，且證據包內附帶的機轉評估多數直接指出生物學關聯薄弱，甚至可能是知識圖譜的結構性偽陽性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（原始適應症清單未提供；依機轉描述為 NSAID 類鎮痛/抗發炎用藥） |
| 預測新適應症 | 肢端骨骼發育不全症 Hunter-Thompson 型 (Acromesomelic Dysplasia, Hunter-Thompson Type)，另有 4 項罕見骨骼/肌肉疾病候選（詳下） |
| TxGNN 預測分數 | 99.74%（rank 1，其餘 4 項介於 99.66%–99.71%） |
| 證據等級 | L5（5 項預測皆無臨床試驗或文獻，僅為模型推論） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏正式的作用機轉資料（`original_moa` 為資料缺口，屬 DG002 高嚴重度缺口）。但證據包內各候選適應症的機轉推理欄位皆提及：Ibuprofen 為 **COX-1/COX-2 抑制劑**，其藥理作用為抗發炎與鎮痛。

以下是 5 項預測適應症的機轉評估摘要，**多數評估結果傾向不支持該預測**：

| 排名 | 預測適應症 | 分數 | 機轉合理性評估 |
|------|-----------|------|----------------|
| 1 | Acromesomelic dysplasia, Hunter-Thompson type | 99.74% | 為 GDF5 基因功能喪失導致的骨骼結構性缺陷，與 COX 抑制機轉無已知關聯；評估認為此高分**可能是知識圖譜結構偽陽性**，非真實機轉關聯 |
| 2 | Brachyolmia-amelogenesis imperfecta syndrome | 99.71% | 脊椎短小合併牙釉質形成不全的遺傳症候群，**無文獻支持** NSAID 對此有治療作用 |
| 3 | Myosclerosis | 99.68% | 進行性肌肉纖維化疾病，理論上抗發炎作用「或許」可延緩伴隨發炎的纖維化，但屬**極弱的間接推測**，無直接證據 |
| 4 | Brachyolmia | 99.67% | 軟骨內成骨調控異常（PAPSS2、TRPV4 相關），與 COX 抑制機轉**無已知交集** |
| 5 | Brachydactyly-syndactyly syndrome | 99.66% | 胚胎發育期基因調控異常導致的肢體結構缺陷，**非發炎或疼痛相關病理**，與藥理作用無合理連結 |

整體而言，這組預測分數雖高，但機轉層面的支持度普遍偏弱，僅 myosclerosis 存在理論上（非實證）的間接可能性。原適應症資料本身的缺口也使得「原適應症與新適應症關聯性」難以完整評估。

---

## 臨床試驗證據

目前無相關臨床試驗登記（5 項預測適應症皆查無 ClinicalTrials.gov 或 ICTRP 資料）。

---

## 文獻證據

目前無相關文獻（5 項預測適應症皆查無 PubMed 資料）。

---

## 香港上市資訊

Ibuprofen 目前**未在香港取得藥品許可證**（許可證數：0），無可列出之許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：證據包標記 TFDA/仿單警語與禁忌症資料為 **Blocking 等級缺口（DG001）**，此缺口直接導致本案**無法進入 S1 安全性初評**，需先取得官方仿單資料方可評估禁忌症與交互作用風險。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 5 項預測適應症均為 L5（純模型推論），無任何臨床試驗或文獻佐證；證據包內附帶的機轉評估多數認為生物學關聯薄弱，甚至可能是知識圖譜結構性偽陽性。
- 安全性資料存在 Blocking 等級缺口（DG001），無法完成 S1 安全性初評。
- 香港目前未上市（0 張許可證），基礎法規資訊尚未齊備。

**若要推進需要：**
- 取得 Ibuprofen 完整仿單警語與禁忌症資料，解除 DG001（Blocking）
- 向 DrugBank API 查詢正式 MOA 資料，解除 DG002（High），以驗證或推翻各候選適應症的機轉假說
- 針對相對較有理論可能性的 myosclerosis，進一步搜尋跨語言/區域資料庫是否有相關實證研究
- 若持續查無支持證據，建議將此組候選標記為低優先度，暫緩資源投入
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

