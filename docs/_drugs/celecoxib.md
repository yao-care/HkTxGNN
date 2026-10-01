---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Celecoxib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Celecoxib：從 COX-2 選擇性消炎止痛藥到肢中發育不良（Hunter-Thompson 型）

## 一句話總結

Celecoxib 是一種 COX-2 選擇性抑制劑，在香港已上市。
TxGNN 模型預測它可能對**肢中發育不良，Hunter-Thompson 型 (Acromesomelic Dysplasia, Hunter-Thompson Type)** 有效。
目前**沒有任何臨床試驗或文獻**支持這個預測，僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 肢中發育不良，Hunter-Thompson 型 (Acromesomelic Dysplasia, Hunter-Thompson Type) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Celecoxib 是 COX-2 選擇性抑制劑，能降低前列腺素生成，用於消炎止痛。

這個預測的合理性偏低。Hunter-Thompson 型肢中發育不良是由 CDMP1/GDF5 相關基因變異造成的遺傳性骨骼發育不良。COX-2 路徑對這類疾病沒有明確的疾病修飾作用。模型給出高分，較可能是因為知識圖譜中它與肌肉骨骼相關術語距離接近，而非真實的機轉關聯。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 持有廠商 |
|---------|------|---------|
| HK-68903 | ECKERD CELECOXIB CAPSULES 200MG | WILSON TRADING COMPANY LIMITED |
| HK-68726 | CELECOXIB CAPSULES 200MG | NATURAL HEALTH RESOURCES COMPANY LIMITED |
| HK-67848 | CELECOXIB CAPSULES 200MG | CHEMILL PHARMA LIMITED |
| HK-44731 | CELEBREX CAP 200MG | VIATRIS HEALTHCARE HONG KONG LIMITED |
| HK-52808 | CELCOX CAP 100MG | GAILY PHARMACEUTICAL COMPANY LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
這個預測只有模型分數，沒有臨床試驗、文獻或合理的機轉支持，應暫緩推進。

**若要推進需要：**
- 取得 Celecoxib 的作用機轉與原適應症資料，並下載香港衛生署的仿單，補齊安全性資訊
- 找出 COX-2 與 GDF5/CDMP1 相關骨骼發育之間的機轉證據；目前沒有，建議不再投入資源

**補充：** 同一份分析中，排名第 9 的「發炎性脊椎病變 (Inflammatory Spondylopathy，即軸心型脊椎關節炎／僵直性脊椎炎)」證據明顯較強。它有 Phase 3 與 Phase 4 隨機試驗，也有多篇文獻，證據等級為 L1，建議決策為 Proceed with Guardrails。若要選一個方向深入評估，建議改以這個適應症為主，另行產出報告。推進前須先確認香港標示中對這個適應症的核准狀態，並留意 NSAID 的心血管、腸胃與腎臟風險。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

