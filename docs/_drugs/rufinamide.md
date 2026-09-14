---
layout: default
title: Rufinamide
parent: 僅模型預測 (L5)
nav_order: 667
evidence_level: L5
indication_count: 5
---

# Rufinamide
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

# Rufinamide：從 Lennox-Gastaut 症候群 (LGS) 到熱性感染相關癲癇症候群 (FIRES)

## 一句話總結

> Rufinamide 是已知核准用於 Lennox-Gastaut 症候群 (LGS) 的廣效抗癲癇藥物，但其詳細作用機轉資料目前缺失。
> TxGNN 模型預測它可能對**熱性感染相關癲癇症候群 (Febrile Infection-Related Epilepsy Syndrome, FIRES)** 有效，
> 但目前**無臨床試驗**、**無相關文獻**支持，僅屬模型拓樸相似性預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | Lennox-Gastaut 症候群 (LGS)（依證據包內其他候選項之機轉描述推得，非直接來自香港許可證欄位） |
| 預測新適應症 | 熱性感染相關癲癇症候群 (Febrile Infection-Related Epilepsy Syndrome, FIRES) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Rufinamide 詳細的作用機轉資料（列為 High 等級資料缺口 DG002，待查詢 DrugBank API）。根據證據包中其他候選適應症的機轉描述可得知，Rufinamide 核准用於 Lennox-Gastaut 症候群 (LGS)，透過鈉通道調節機轉發揮廣效抗癲癇作用，對 LGS 常見的混合型發作（含全身性與局部性成分）具療效。

FIRES 是一種好發於兒童、常伴隨高死亡率的難治型癲癇性腦病，多在感染後急性發生。臨床病理生理上，FIRES 與 LGS 同屬「癲癇性腦病」譜系，皆呈現多灶性/廣泛性皮質過度放電，且對傳統抗癲癇藥物反應不佳，這是兩者機轉延伸具一定合理性的基礎。

然而需特別指出：此候選項（rank 1）在證據包中的 `repurposing_rationale` 欄位標示為 **pending**，代表模型本身尚未產出針對 FIRES 的具體機轉關聯說明。因此上述 LGS/FIRES 病理生理重疊僅為背景推論，並非直接機轉證據，建議視為**研究假設**而非**臨床假設**。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：TFDA 仿單警語/禁忌資料目前為 **Blocking** 等級缺口（DG001），在此資料補齊前，本候選無法進入 S1 安全性初評階段。

## 結論與下一步

**決策：Hold**

**理由：**
- Rufinamide 詳細作用機轉（MOA）與仿單安全性資料（警語、禁忌）皆為缺失，其中仿單資料屬 Blocking 等級缺口，無法進行 S1 安全性初評。
- 本候選（FIRES）及其他 4 個 TxGNN 預測適應症（perioral myoclonia with absences、photosensitive occipital lobe epilepsy、atypical childhood epilepsy with centrotemporal spikes、cryptogenic late-onset epileptic spasms）皆無任何臨床試驗或文獻支持，證據等級均為 L5，僅為模型拓樸相似性預測。
- 香港目前未上市，無許可證資料可供交叉比對適應症關聯性。

**若要推進需要：**
- 取得 TFDA/香港衛生署仿單完整警語與禁忌症資料，解除 DG001 Blocking 缺口
- 查詢 DrugBank API 補充 Rufinamide 詳細作用機轉資料（DG002）
- 針對 FIRES 等候選適應症搜尋近期病例系列研究、系統性回顧或臨床試驗登記，補足 L5 以上證據
- 若確認具治療潛力，評估香港恩慈療法或專案進口管道的可行性（因目前未上市）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

