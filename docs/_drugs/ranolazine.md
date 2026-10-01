---
layout: default
title: Ranolazine
parent: 僅模型預測 (L5)
nav_order: 743
evidence_level: L5
indication_count: 1
---

# Ranolazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Ranolazine：從原適應症（資料未提供）到腎因性抗利尿激素分泌不當症候群

## 一句話總結

Ranolazine 目前在香港有 3 張緩釋錠許可證，但本次資料未登載原適應症。
TxGNN 模型預測它可能對**腎因性抗利尿激素分泌不當症候群 (Nephrogenic Syndrome of Inappropriate Antidiuresis, NSIAD)** 有效。
目前**沒有臨床試驗和文獻**支持，只有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未提供 |
| 預測新適應症 | 腎因性抗利尿激素分泌不當症候群 (NSIAD) |
| TxGNN 預測分數 | 99.65%（排名 7050） |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，原適應症也未提供，因此無法從資料中建立藥物與 NSIAD 之間的機轉關聯。

NSIAD 的成因是 AVPR2（血管加壓素 V2 受體）的功能增益變異。這類變異使 cAMP 訊號持續活化，在沒有血管加壓素的情況下，AQP2 仍會促進水分再吸收。依一般藥理知識（非本次資料提供），ranolazine 是晚期鈉電流（Nav1.5）抑制劑，對脂肪酸氧化也有部分影響。這兩者都沒有已知作用於 V2 受體、cAMP/AQP2 訊號或腎臟水分調節。

因此，0.996 的高分應視為未經驗證的圖譜預測，可能來自網路鄰近性造成的假象，不能當作生物學上的支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-63607 | RANEXA PROLONGED-RELEASE TABLETS 375MG | A. MENARINI HONG KONG LIMITED |
| HK-63608 | RANEXA PROLONGED-RELEASE TABLETS 500MG | A. MENARINI HONG KONG LIMITED |
| HK-63609 | RANEXA PROLONGED-RELEASE TABLETS 750MG | A. MENARINI HONG KONG LIMITED |

劑型與核准適應症在本次資料中皆未登載。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，只有模型預測，沒有任何臨床試驗或文獻，也找不到合理的機轉連結。
- 香港衛生署仿單的警語與禁忌資料缺漏，無法進入安全性篩選。

**若要推進需要：**
- 下載並解析香港衛生署仿單，補齊原適應症、警語與禁忌症
- 從 DrugBank 補充作用機轉（MOA）
- 驗證 ranolazine 與 AVPR2/cAMP/AQP2 路徑之間是否有任何實驗證據
- 檢索 NSIAD 相關的臨床前或病例研究，確認預測是否只是圖譜假象
- 評估給藥途徑與 NSIAD 治療情境的相容性

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

