---
layout: default
title: Meloxicam
parent: 僅模型預測 (L5)
nav_order: 399
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

# MELOXICAM：從消炎鎮痛（NSAID）適應症到 Acromesomelic Dysplasia, Hunter-Thompson Type（罕見骨骼疾病）

## 一句話總結

Meloxicam 是一種 COX-2 優先抑制型 NSAID，但本評估包中缺乏其原始核准適應症的完整記錄（該藥目前**未在本地上市**）。
TxGNN 模型將其與**Acromesomelic Dysplasia, Hunter-Thompson Type**（一種罕見骨骼發育異常）連結，預測分數高達 **99.92%**，
但目前**無任何臨床試驗、無文獻、無上市紀錄**支持這個方向，且證據包本身已標註此關聯機轉上高度存疑。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（drug.original_indications 為空；該藥物未在本地上市，無許可證核准適應症可查） |
| 預測新適應症 | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN 預測分數 | 99.92%（KG 排名第 2073） |
| 證據等級 | L5（僅模型預測，無臨床/文獻證據） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Meloxicam 詳細作用機轉資料的結構化紀錄（DG002，High severity data gap）。根據證據包內附的機轉分析，Meloxicam 屬於 **COX-2 優先抑制型 NSAID**，其抗發炎/鎮痛效果來自抑制前列腺素合成路徑。

然而，Acromesomelic Dysplasia, Hunter-Thompson Type 是由 **GDF5/CDMP1（BMP 訊息通路）基因突變**所導致的生長板軟骨細胞分化缺陷，屬於**結構性骨骼發育異常，並非發炎介導疾病**。證據包中的機轉分析明確指出：Meloxicam 的 COX-2 抑制/抗發炎機轉與此疾病的致病路徑**沒有已知交集**。

換言之，TxGNN 給出的高分很可能反映的是知識圖譜中「骨骼系統疾病」節點與「NSAID 藥物」節點之間的**拓樸鄰近性（即兩者在圖上距離近，但不代表藥理上有真實關聯）**，而非真實的藥理學連結。此為模型侷限性的典型案例，需特別謹慎看待。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

本藥物（Meloxicam）在本地目前**未上市**，無許可證登記資料可供查詢（`total_licenses = 0`）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 注意：`key_warnings`、`contraindications`、DDI 查詢結果目前均無資料。其中**仿單警語/禁忌（DG001）已被標記為 Blocking severity**，代表在缺乏此資料前，此候選**無法進入 S1 安全性初評階段**。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5（僅有模型預測，無任何臨床試驗、文獻或上市支持），且證據包本身的機轉分析已指出此預測很可能是知識圖譜拓樸假訊號，機轉合理性極低。
- 安全性資料存在 Blocking 等級缺口（DG001：仿單警語/禁忌未知），依規則無法進入下一階段評估。
- 藥物於本地未上市，缺乏在地法規與適應症基礎資料。

**若要推進需要：**
- 取得 TFDA（或當地藥監局）官方仿單，解析警語與禁忌（解決 DG001，Blocking）
- 透過 DrugBank API 取得完整 MOA 資料，確認 Meloxicam 的藥理分類與作用位點（解決 DG002）
- 針對 rank 1 預測（Hunter-Thompson Type），需獨立驗證是否為知識圖譜拓樸假訊號，建議諮詢罕見骨骼疾病領域專家評估機轉合理性
- 若持續推進，應優先評估證據包中機轉相對較合理的候選（見下方附錄，rank 5 pseudoachondroplasia）

---

## 附錄：同批其他預測候選（供參考）

本次證據包共包含 5 個 TxGNN 預測候選，皆屬同一等級（L5 / Hold），列表如下供橫向比較：

| 排名 | 預測適應症 | TxGNN 分數 | 機轉合理性評估 | 建議 |
|------|-----------|-----------|---------------|------|
| 1 | Acromesomelic Dysplasia, Hunter-Thompson Type | 99.92% | 極低——很可能為知識圖譜拓樸假訊號，非真實藥理關聯 | Hold |
| 2 | Brachyolmia-Amelogenesis Imperfecta Syndrome | 99.92% | 極低——骨骼/牙釉質發育基因疾病，非發炎性，無機轉關聯 | Hold |
| 3 | Myosclerosis | 99.90% | 低——理論上或可調節纖維化相關發炎反應，但無任何實證支持 | Hold |
| 4 | Brachyolmia | 99.89% | 極低——軟骨基質/生長板缺陷，非發炎機轉，與 COX 抑制無重疊 | Hold |
| 5 | Pseudoachondroplasia | 99.81% | 相對較高但仍屬臆測——COMP 蛋白錯誤摺疊觸發 ER 壓力與類發炎（NF-κB）路徑，理論上與 NSAID 機轉較接近，但無臨床前/臨床證據佐證 | Hold |

**說明：** 五者證據等級皆為 L5，均無臨床試驗或文獻支持，建議決策皆為 Hold。若未來需優先深入研究，機轉層面相對值得關注的是 rank 5（Pseudoachondroplasia），但仍需臨床前研究驗證後才可能提升證據等級。

---

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過完整臨床驗證後才能應用於實際治療。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

