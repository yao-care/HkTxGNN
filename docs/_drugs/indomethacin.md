---
layout: default
title: Indomethacin
parent: 僅模型預測 (L5)
nav_order: 397
evidence_level: L5
indication_count: 5
---

# Indomethacin
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

# Indomethacin：原適應症資料缺失，預測用於 Brachydactyly-Syndactyly Syndrome

## 一句話總結

Indomethacin（DrugBank DB00328）為 COX-1/2 抑制劑類 NSAID，但此份 Evidence Pack 未提供其原始核准適應症與香港上市資料。
TxGNN 模型預測其可能對罕見先天性肢端骨骼發育疾病 **Brachydactyly-Syndactyly Syndrome** 有效（預測分數 99.97%），
但目前**無任何臨床試驗、無任何文獻**支持，機轉連結亦屬間接推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（Evidence Pack 未提供原始適應症紀錄，香港亦無許可證資料） |
| 預測新適應症 | Brachydactyly-Syndactyly Syndrome |
| TxGNN 預測分數 | 99.97%（rank 1093） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

此份 Evidence Pack 缺乏 Indomethacin 的作用機轉（MOA）資料，也沒有原始適應症紀錄，因此無法比對「原適應症→新適應症」的臨床關聯性。

根據模型提供的機轉推論：Brachydactyly-Syndactyly Syndrome 為先天性肢芽發育異常，病因與 BMP/GDF5-Wnt 訊號路徑相關；Indomethacin 透過抑制 COX/PGE2 可影響間葉幹細胞成骨分化，此機轉在「異位性骨化（heterotopic ossification）預防」中有實證支持。但異位性骨化屬**後天誘發**的骨化反應，與此症**先天基因突變導致的肢芽 patterning 缺陷**在病理本質上不同，屬間接類比推論，並無直接證據顯示藥物能逆轉此先天畸形。

整體而言，此預測目前僅為知識圖譜層級的關聯，缺乏機轉層級與臨床層級的雙重驗證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ 本評估存在一項 **Blocking 等級資料缺口**：缺乏 TFDA 仿單警語與禁忌症資料，導致本案**無法進入 S1 安全性初評**（見 meta.data_gaps DG001）。

## 其他 TxGNN 預測候選（同批查詢）

本次查詢同時輸出 5 個候選適應症，除主要候選外，其餘 4 項評分與機轉合理性摘要如下：

| 排名 | 疾病 | 預測分數 | 機轉合理性摘要 |
|------|------|---------|---------------|
| 2 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.97% | 機轉關聯薄弱，COX/PGE2 路徑與視泡閉合、近端肢骨發育無已知直接關聯 |
| 3 | Acromesomelic dysplasia, Hunter-Thompson type | 99.89% | 與 GDF5/BMP 路徑有理論上游下游關係，但方向相反（此症為成骨不足，Indomethacin 藥理上抑制成骨），理論上可能加重表現型 |
| 4 | WHIM syndrome | 99.88% | 機轉不合理，COX/PGE2 與 CXCR4 訊號路徑無已知關聯，極可能為知識圖譜偽陽性 |
| 5 | Brachyolmia-amelogenesis imperfecta syndrome | 99.87% | 機轉證據薄弱，與琺瑯質基質蛋白形成無已知關聯 |

所有候選皆為 L5（僅模型預測）、決策階段 S0、建議 Hold，且均無臨床試驗或文獻查詢結果。

## 結論與下一步

**決策：Hold**

**理由：**
- 5 個候選適應症均屬 L5 等級（僅模型預測，無臨床/文獻證據），且部分候選（如 rank 3）機轉方向甚至與藥理作用相反。
- 存在 Blocking 等級資料缺口（TFDA 仿單警語/禁忌），依規則無法進入下一階段安全性初評。

**若要推進需要：**
- 取得 TFDA 仿單警語與禁忌症資料（解除 DG001 Blocking 缺口）
- 透過 DrugBank API 查詢 Indomethacin 完整作用機轉（解除 DG002）
- 針對候選疾病補充臨床前機轉研究，驗證 TxGNN 高分是否反映真實藥理關聯或僅為知識圖譜節點鄰近性造成的偽陽性
- 若無法取得任何後續證據，建議維持 Hold 並降低此候選優先序
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

