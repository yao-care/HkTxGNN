---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 550
evidence_level: L5
indication_count: 5
---

# Meloxicam
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

# Meloxicam：從 NSAID 消炎止痛到肢中發育不良（Hunter-Thompson 型）

## 一句話總結

Meloxicam 是偏向抑制 COX-2 的非類固醇消炎止痛藥（NSAID）。
TxGNN 模型預測它可能對**肢中發育不良 Hunter-Thompson 型 (Acromesomelic Dysplasia, Hunter-Thompson Type)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 肢中發育不良 Hunter-Thompson 型 (Acromesomelic Dysplasia, Hunter-Thompson Type) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Meloxicam 屬於 NSAID 類別，已知作用是抑制 COX-2 以減輕發炎與疼痛。

不過，這個預測在機轉上**找不到已建立的關聯**。此疾病是 GDF5 相關的骨骼發育不良，根本原因是 BMP 訊號傳遞缺陷，而 Meloxicam 對這條路徑沒有已知作用。它唯一可能的角色是緩解疼痛或發炎的症狀，並不能改變疾病本身。0.9992 的高分僅代表模型預測，不等於有實證支持。

模型的其他預測同樣缺乏證據，且都屬於罕見遺傳性骨骼或結締組織疾病：

| 排名 | 預測疾病 | 分數 | 機轉評估 |
|------|---------|------|---------|
| 2 | 短軀幹發育不良合併琺瑯質發育不全症候群 (Brachyolmia-Amelogenesis Imperfecta Syndrome) | 99.92% | LTBP3 相關（影響 TGF-β），COX 抑制無已知關聯 |
| 3 | 肌硬化症 (Myosclerosis) | 99.90% | NSAID 理論上可緩解疼痛，但無疾病修飾證據 |
| 4 | 短軀幹發育不良 (Brachyolmia) | 99.89% | 遺傳性缺陷（如 PAPSS2、TRPV4），COX-2 抑制無法處理 |
| 5 | 假性軟骨發育不全 (Pseudoachondroplasia) | 99.81% | COMP 突變致病；臨床上 NSAID 用於關節痛的症狀控制，但這不是針對疾病本身的再利用訊號 |

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

Meloxicam 在香港共有 20 張許可證，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-53980 | MOXIC FORTE TAB 15MG | HANG LUNG TRADING (H.K.) CO |
| HK-51173 | MELOX TAB 7.5MG | STAR MEDICAL SUPPLIES LTD |
| HK-41788 | MOBIC TAB 7.5MG | BOEHRINGER INGELHEIM (HK) LTD |
| HK-54750 | APO-MELOXICAM TAB 15MG | HIND WING CO LTD |
| HK-68090 | REMOXIN TABLETS 15MG | SB PHARMA LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 五個預測適應症都只有模型分數，沒有臨床試驗、文獻或機轉關聯支持（L5），且與 Meloxicam 的 COX-2 抑制作用沒有合理連結。
- 香港衛生署仿單的警語與禁忌症資料尚未取得，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症資料。
- 從 DrugBank 補齊 Meloxicam 的作用機轉資料。
- 找出 COX-2 抑制與 GDF5/BMP 訊號路徑之間的機轉證據，或先做前臨床研究。
- 若目標只是症狀控制（如假性軟骨發育不全的關節痛），應另外定義為症狀治療研究，不宜視為疾病再利用。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

