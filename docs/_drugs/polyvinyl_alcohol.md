---
layout: default
title: Polyvinyl Alcohol
parent: 僅模型預測 (L5)
nav_order: 698
evidence_level: L5
indication_count: 4
---

# Polyvinyl Alcohol
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

# Polyvinyl Alcohol：從眼用潤滑（人工淚液）到先天性魚鱗癬樣紅皮症

## 一句話總結

Polyvinyl Alcohol（聚乙烯醇）是一種成膜高分子，在香港以眼用溶液、人工淚液的形式上市（由品名判斷，許可證未載明適應症）。
TxGNN 模型預測它可能對**先天性魚鱗癬樣紅皮症 (Congenital Ichthyosiform Erythroderma)** 有效。
目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明（品名為眼用溶液／人工淚液） |
| 預測新適應症 | 先天性魚鱗癬樣紅皮症 (Congenital Ichthyosiform Erythroderma) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 12 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Polyvinyl Alcohol 主要作為賦形劑和眼用潤滑劑使用，屬於成膜聚合物。理論上，它在皮膚表面形成的屏障或封閉效應，可能對角質過度增生的皮膚有些幫助，但這只是推測，沒有任何研究佐證。

模型另外預測了三個相關疾病：自癒性火棉膠嬰兒 (self-healing collodion baby, 99.83%)、板層狀魚鱗癬 (lamellar ichthyosis, 99.72%)、泳衣狀魚鱗癬 (bathing suit ichthyosis, 99.54%)。這四者都屬於常染色體隱性先天性魚鱗癬的範疇，**很可能是相互關聯的同一個訊號，而不是四個獨立的證據**。高分可能來自知識圖譜中魚鱗癬相關節點的鄰近相似性，不一定代表有藥理上的依據。

此外，魚鱗癬已有保濕劑、角質溶解劑、A酸類等標準照護。Polyvinyl Alcohol 能增加多少價值並不明確。用於新生兒時，皮膚通透性高，若要外用，需要另外做安全性評估。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

共 12 張許可證，以下列出 5 張主要許可證（許可證資料未載明劑型與適應症）：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-57590 | XTRA LUVERICAN OPHTHALMIC SOLUTION 1.4% | WILSON TRADING COMPANY LIMITED |
| HK-57165 | WETCO LUVERICAN OPHTHALMIC SOLUTION 1.4% | WILSON TRADING COMPANY LIMITED |
| HK-57164 | SUNRISE LUVERICAN OPHTHALMIC SOLUTION 1.4% | WILSON TRADING COMPANY LIMITED |
| HK-39377 | PMS-ARTIFICIAL TEARS DROPS 1.4% | TRENTON-BOMA LTD |
| HK-57591 | REVCO LUVERICAN OPHTHALMIC SOLUTION 1.4% | WILSON TRADING COMPANY LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 這是純模型預測（L5），沒有臨床試驗、文獻或作用機轉資料支持。
- 香港現有產品皆為眼用製劑，與預測的皮膚適應症在給藥途徑上不相容。魚鱗癬已有標準治療，增益價值不明。

**若要推進需要：**
- 取得 Polyvinyl Alcohol 的作用機轉資料，並評估其對皮膚屏障的作用是否合理（DrugBank 查詢）。
- 下載並解析香港衛生署的仿單，補齊警語與禁忌症。
- 搜尋魚鱗癬與外用成膜聚合物相關的前臨床或病例研究。
- 確認外用皮膚劑型的可行性，以及新生兒族群的經皮吸收與安全性。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

