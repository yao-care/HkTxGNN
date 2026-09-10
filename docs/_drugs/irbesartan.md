---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 411
evidence_level: L5
indication_count: 4
---

# Irbesartan
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

# Irbesartan：原適應症資料缺失，TxGNN 預測惡性腎血管性高血壓

## 一句話總結

Irbesartan（DB01029）在本次 Evidence Pack 中缺乏原適應症與完整作用機轉資料，但依 TxGNN 模型內附的機轉推論文字可知其屬於 ARB（血管收縮素 II 受體阻斷劑）類藥物。
TxGNN 模型預測它可能對**惡性腎血管性高血壓 (Malignant Renovascular Hypertension)** 有效，
但目前**無任何臨床試驗或直接相關文獻**支持，屬於純模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（Evidence Pack 未提供 original_indications；藥物屬 ARB 類，需以正式仿單核實） |
| 預測新適應症 | 惡性腎血管性高血壓 (Malignant Renovascular Hypertension) |
| TxGNN 預測分數 | 99.31% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Evidence Pack 中 `original_moa` 標記為資料缺失、`original_indications` 為空，因此無法從原廠適應症直接推論關聯性。但模型針對各預測適應症所附的機轉推論文字明確指出，Irbesartan 屬於 **ARB（Angiotensin II Receptor Blocker，血管收縮素 II 受體阻斷劑）**，這是公認的藥理分類。

對於排名第 1、2 的預測（惡性腎血管性高血壓、惡性高血壓性腎病），ARB 作用於腎素-血管收縮素-醛固酮系統（RAAS），在機轉上具有 class effect 層級的合理性，與 ARB 類藥物已知的腎臟保護作用理論相符。

但排名第 3、4 的預測（皆為肺動脈高壓相關亞型）機轉關聯薄弱——肺動脈高壓的標準治療路徑是 NO-cGMP、Endothelin、Prostacyclin 三大通路，並非 ARB 的作用範疇。且排名第 4 附帶的 20 篇文獻經檢視後，內容均為「hypoxia」關鍵字下的一般缺氧生物學／腫瘤代謝／神經退化基礎研究，未提及 irbesartan 或任何 ARB 藥理介入，判定為**關鍵字誤配**而非藥物特異性證據。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 其他預測適應症（同為 Hold，僅供對照）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 備註 |
|------|-----------|-----------|---------|------|
| 2 | 惡性高血壓性腎病 | 99.31% | L5 | 無臨床試驗/文獻，機轉與 rank 1 相同 |
| 3 | 肺動脈高壓（多因子不明機轉） | 99.25% | L5 | 機轉關聯薄弱，ARB 非標準路徑 |
| 4 | 肺動脈高壓（肺病/缺氧所致） | 99.25% | L5 | 20 篇文獻均為 hypoxia 泛用詞誤配，非藥物特異性證據 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
四個預測適應症的證據等級均為 L5，僅有 TxGNN 模型分數，無任何臨床試驗或直接相關文獻支持；且藥物本身缺乏 MOA、原適應症與安全性（警語/禁忌症）資料，香港亦未上市，尚不足以進入下一階段評估。

**若要推進需要：**
- 補齊 `original_moa` 與 `original_indications`（DrugBank API 查詢，DG002）
- 取得仿單警語與禁忌症資料（Blocking 等級缺口 DG001，屬進入 S1 安全性初評的前提）
- 針對 rank 1-2（腎血管性高血壓相關）另行檢索是否有 ARB 用於高血壓性腎病的既有臨床證據
- 排除 rank 3-4（肺動脈高壓）的機轉薄弱疑慮，或以更精準關鍵字重新執行文獻檢索，避免 hypoxia 泛用詞誤配
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

