---
layout: default
title: Insulin Human
parent: 僅模型預測 (L5)
nav_order: 403
evidence_level: L5
indication_count: 5
---

# Insulin Human
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

# Insulin Human：從糖尿病到自體免疫性卵巢炎

## 一句話總結

Insulin Human（DrugBank ID: DB00030）是糖尿病治療的標準藥物。
TxGNN 模型預測它可能對**自體免疫性卵巢炎 (Autoimmune Oophoritis)** 有效，
但目前**無任何臨床試驗**、**無任何文獻**支持，證據等級為最低的 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 糖尿病（資料庫未提供香港許可證資料，此為胰島素之公認適應症） |
| 預測新適應症 | 自體免疫性卵巢炎 (Autoimmune Oophoritis) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Insulin Human 的詳細作用機轉資料（Data Gap，DG002：High severity）。

根據模型自身給出的機轉推論：此預測的高分很可能來自知識圖譜中「自體免疫／內分泌」相關節點的鄰近性，而非胰島素對自體免疫性卵巢炎具有實質治療機轉的證據。換言之，這是一個統計上的關聯，而非藥理學上可解釋的合理連結。

值得注意的是，本次評估同時產出的其他候選適應症（如 stiff person syndrome、thiamine-responsive dysfunction syndrome）雖然與糖尿病／胰島素訊號路徑有較明確的生物學重疊，但排名第一的自體免疫性卵巢炎並無此類線索，機轉合理性最弱。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

Insulin Human 目前在香港未上市，無許可證記錄（`total_licenses = 0`）。

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：TFDA 仿單警語/禁忌資料缺失（DG001，Blocking severity），此為進入 S1 安全性初評的必要前提，目前尚未補齊。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5（僅有模型預測分數，無任何臨床試驗或文獻支持）。
- 藥物本身的機轉推論明確指出這是知識圖譜節點鄰近性造成的高分，而非實質治療關聯。
- 安全性關鍵資料（仿單警語/禁忌，DG001）為 Blocking 等級缺口，無法進行下一階段評估。

**若要推進需要：**
- 補齊 TFDA／香港仿單警語與禁忌資料（DG001）
- 取得 Insulin Human 詳細作用機轉資料（DG002）
- 針對 autoimmune oophoritis 尋找具體的機轉研究或病例報告，確認是否存在可驗證的生物學連結
- 若機轉驗證失敗，建議改為評估證據等級較高的候選（如 thiamine-responsive dysfunction syndrome，已進入 S1 階段）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

