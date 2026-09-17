---
layout: default
title: Mannitol
parent: 僅模型預測 (L5)
nav_order: 473
evidence_level: L5
indication_count: 5
---

# Mannitol
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

# Mannitol：作用機轉資料缺乏，預測新適應症為 Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)

## 一句話總結

Mannitol（DrugBank ID: DB00742）目前缺乏原適應症與作用機轉資料，香港尚未取得任何上市許可證。
TxGNN 模型預測它可能對**NSIAD（腎因性抗利尿激素分泌不當症候群）**有效，
但目前僅有 **0 個臨床試驗**和 **1 篇非特異性文獻**支持，證據薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺乏（Evidence Pack 未記錄） |
| 預測新適應症 | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 標記為缺口項目 DG002，嚴重度 High）。根據 Evidence Pack 中的臨床試驗脈絡線索（如 NCT01108744 提及 mannitol 用於顱內壓管理），Mannitol 屬於臨床常用的滲透性利尿劑，但這與 NSIAD 之間的機轉關聯並不明確。

根據候選項目本身的 `repurposing_rationale`：Mannitol 作為滲透性利尿劑理論上可能經由誘發水分排出影響低血鈉狀態，但 NSIAD 的病因是 V2 受體組成性活化（與 ADH 無關），Mannitol 並未針對此分子機轉。目前唯一支持的文獻是一篇低血鈉評估陷阱的一般性綜述，並未特定討論 Mannitol 的治療角色。

因此，儘管 TxGNN 分數極高（99.97%），機轉合理性與實證支持皆偏弱，這是典型「高分但低證據」的預測案例。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European journal of internal medicine | 低血鈉症評估常見的十個陷阱，屬一般性綜述，未特定討論 Mannitol 治療角色 |

## 安全性考量

安全性資訊請參考原廠仿單。（DDI 查詢無結果；警語與禁忌資料缺口 DG001 為 Blocking 等級，尚待自 TFDA/香港衛生署仿單補齊）

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數雖高達 99.97%，但機轉關聯薄弱——NSIAD 病因為 V2 受體組成性活化，與 ADH 及滲透性利尿無直接關係，Mannitol 未針對此路徑。
- 僅有 1 篇非特異性綜述文獻、無任何臨床試驗支持，證據等級僅 L5。

**若要推進需要：**
- 補齊作用機轉資料（DG002，High）
- 補齊香港/台灣仿單警語與禁忌症（DG001，Blocking，這是進入 S1 安全性初評的前提）
- 尋找更具體針對 Mannitol 於 NSIAD/低血鈉治療的文獻或臨床試驗
- 備註：本組候選中 rank 4「Malignant Hyperthermia, Susceptibility to」證據等級為 L4、已進入 S1（Research Question），機轉上有 Mannitol 輔助強迫利尿降低橫紋肌溶解腎損傷風險的支持性理由，若需優先資源投入可考慮改以該項目為主要研究方向。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

