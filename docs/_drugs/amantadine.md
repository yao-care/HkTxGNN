---
layout: default
title: Amantadine
parent: 僅模型預測 (L5)
nav_order: 44
evidence_level: L5
indication_count: 4
---

# Amantadine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Amantadine：從（原適應症未載明）到 Rasmussen 亞急性腦炎

## 一句話總結

Amantadine（金剛胺）在香港已有 5 張許可證，但現有資料未載明其核准適應症。
TxGNN 模型預測它可能對 **Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis)** 有效。
目前**沒有臨床試驗，也沒有文獻**支持這個方向，只有模型預測分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明 |
| 預測新適應症 | Rasmussen 亞急性腦炎 (Rasmussen subacute encephalitis) |
| TxGNN 預測分數 | 99.48% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。本次取得的資料未包含 Amantadine 的原適應症與 MOA，因此無法從原適應症推導它與 Rasmussen 腦炎的關聯。

一個尚未被資料證實的推測是：Amantadine 具 NMDA 受體拮抗作用，可能與 Rasmussen 腦炎中被提出的麩胺酸興奮性毒性有關。這只是假說，本次提供的資料中沒有任何證據支持。

目前唯一的支持是 TxGNN 的高分預測（99.48%，全體排名 9153）。高分不等於有臨床意義，在缺乏其他證據下不宜過度解讀。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-27366 | PK-MERZ TAB 100MG | HONGKONG WINHEALTH PHARMA GROUP CO. LIMITED |
| HK-34789 | ENZIL TAB 100MG | YUNG SHIN CO LTD |
| HK-62120 | AMANDIN CAPSULES 100MG | YAT SENG TRADING CO |
| HK-45493 | PMS-AMANTADINE HYDROCHLORIDE CAP 100MG | TRENTON-BOMA LTD |
| HK-59608 | AMANTADINE F.C. TAB 100MG | JULIUS CHEN & COMPANY (HK) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
證據等級僅為 L5，沒有任何臨床試驗或文獻直接支持 Rasmussen 亞急性腦炎這個適應症，機轉資料也缺乏。這種罕見神經免疫疾病目前僅有模型預測，不足以推進。

**若要推進需要：**
- 補齊 Amantadine 的 MOA（可查詢 DrugBank）與香港衛生署的原適應症、仿單警語與禁忌症
- 針對 Rasmussen 腦炎與 Amantadine 做專題文獻檢索，確認有無病例報告或機轉研究
- 評估 NMDA 拮抗作用與該疾病病理的關聯，再決定是否進入下一階段

**補充：**
同一藥物的其他預測適應症中，「脊髓炎 (myelitis)」與「PLA2G6 相關神經退化 (PLA2G6-associated neurodegeneration)」各有間接文獻，證據等級為 L4，建議列為研究問題。若要優先排序，可考慮先評估這兩項。

> 本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

