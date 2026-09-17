---
layout: default
title: Nimodipine
parent: 僅模型預測 (L5)
nav_order: 524
evidence_level: L5
indication_count: 2
---

# Nimodipine
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

# Nimodipine：原適應症資料缺失 → 預測新適應症評估（Homozygous Familial Hypercholesterolemia）

## 一句話總結

Nimodipine（DB00393）目前香港未上市，且缺乏原適應症、作用機轉與仿單安全性資料。
TxGNN 模型預測其可能對**原發性家族性高膽固醇血症（純合子型，Homozygous Familial Hypercholesterolemia）**有效，
但**無任何臨床試驗或文獻支持**，證據等級為 L5，機轉關聯性經評估亦十分薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（未上市，仿單資訊缺失） |
| 預測新適應症 | Homozygous Familial Hypercholesterolemia（原發性家族性高膽固醇血症純合子型） |
| TxGNN 預測分數 | 99.29%（rank 11760） |
| 證據等級 | L5（僅模型預測，無臨床試驗或文獻） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Nimodipine 詳細的作用機轉整理資料（MOA 為 Data Gap），僅能依據既有藥理學共識描述：Nimodipine 為高脂溶性二氫吡啶類鈣離子通道阻斷劑（Cav1.2/L-type），臨床上機轉聚焦於腦血管平滑肌鬆弛。

HoFH 的病理機轉是 LDLR/APOB/PCSK9 基因缺陷導致 LDL 受體功能喪失、LDL-C 清除障礙，與 L-type 鈣通道阻斷之間**沒有已知的直接藥理路徑連結**。經評估，僅有少數體外研究提及部分鈣通道阻斷劑對脂質過氧化有微弱、非特異性的調節作用，屬間接推論，不足以構成機轉支持。

此配對純粹來自 TxGNN 圖譜相似性推論（score 0.993），無任何臨床試驗或文獻佐證，應視為假說而非可驗證訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

Nimodipine 目前**未於香港上市**，無許可證資料可供列出。

## 安全性考量

安全性資訊請參考原廠仿單（目前 TFDA/香港仿單警語與禁忌症資料尚未取得，屬 Blocking 等級資料缺口）。

## 其他預測適應症（同樣為 L5，供參考）

| 疾病 | TxGNN 分數 | 證據 | 建議 |
|------|-----------|------|------|
| Nephrogenic Syndrome of Inappropriate Antidiuresis | 99.05%（rank 14836） | 無臨床試驗、無文獻 | Hold |

此配對機轉上同樣缺乏支持：NSIAD 源於 AVPR2 受體組成性活化（Gs-cAMP-PKA-AQP2 路徑），與 Nimodipine 的 L-type 鈣通道標的無已知交集。

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個預測適應症皆為 L5（僅模型預測），零臨床試驗、零文獻支持。
- 機轉關聯性經評估薄弱甚至不存在，非可驗證訊號。
- 藥物本身在香港未上市，且仿單警語/禁忌症（Blocking 等級）與 MOA（High 等級）資料缺口尚未補齊，無法進入安全性初評（S1）。

**若要推進需要：**
- 取得 TFDA 官網仿單 PDF，解析警語與禁忌症資料
- 透過 DrugBank API 查詢完整作用機轉資料
- 待上述資料補齊後，重新評估是否有足夠基礎進入下一階段證據收集（臨床試驗/文獻搜尋）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

