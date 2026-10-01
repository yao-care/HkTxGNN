---
layout: default
title: Rotigotine
parent: 中證據等級 (L3-L4)
nav_order: 774
evidence_level: L4
indication_count: 5
---

# Rotigotine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Rotigotine：從帕金森氏症與不寧腿症候群到注意力不足過動症

## 一句話總結

Rotigotine 是一種多巴胺促效劑貼片，文獻記載用於帕金森氏症與不寧腿症候群 (RLS)。
TxGNN 模型預測它可能對**注意力不足過動症 (ADHD)** 有效，但目前**沒有任何臨床試驗**，只有 **3 篇間接文獻**（2 篇 RLS 回顧、1 篇前臨床研究）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症；文獻指出用於帕金森氏症與不寧腿症候群 |
| 預測新適應症 | 注意力不足過動症 (Attention Deficit-Hyperactivity Disorder) |
| TxGNN 預測分數 | 99.997% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

DrugBank 的作用機轉欄位目前缺資料。依現有分析，Rotigotine 是非麥角鹼類多巴胺促效劑，作用於 D1–D5 受體，對 D3 親和力高並有 D2 活性，同時作用於 5-HT1A 與 α2B 受體。ADHD 的病理涉及多巴胺與正腎上腺素系統失調，所以在機轉上有生物學合理性。

間接線索有兩條。第一，一篇前臨床研究（PMID 34182128）探討 D4 多巴胺受體與 α2A 腎上腺素受體的異聚體，這條路徑與 ADHD 相關，但研究並未在 ADHD 中測試 Rotigotine。第二，兩篇 RLS 回顧支持 Rotigotine 用於 RLS，而兒童 RLS 常與 ADHD 共病，這只是重疊疾病的旁證，不是 ADHD 的直接證據。

TxGNN 的高分來自知識圖譜推論，不等於臨床證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18656214](https://pubmed.ncbi.nlm.nih.gov/18656214/) | 2008 | Review | Revue neurologique | 不寧腿症候群的臨床特徵、盛行率（西方約 2–3%）與治療回顧，屬共病旁證，非 ADHD 直接證據 |
| [21476956](https://pubmed.ncbi.nlm.nih.gov/21476956/) | 2011 | Review | Current pharmaceutical design | 兒童不寧腿症候群的藥物選項回顧，該族群常與 ADHD 重疊 |
| [34182128](https://pubmed.ncbi.nlm.nih.gov/34182128/) | 2021 | 前臨床／體外 | Pharmacological research | D4 與 α2A 受體異聚體在不同多型變異下有藥理差異，與 ADHD 及衝動控制障礙相關，未測試 Rotigotine |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-55447 | NEUPRO TRANSDERMAL PATCH 2MG/24H | 經皮貼片（依品名判斷） | — |
| HK-55444 | NEUPRO TRANSDERMAL PATCH 8MG/24H | 經皮貼片（依品名判斷） | — |
| HK-55446 | NEUPRO TRANSDERMAL PATCH 4MG/24H | 經皮貼片（依品名判斷） | — |
| HK-55445 | NEUPRO TRANSDERMAL PATCH 6MG/24H | 經皮貼片（依品名判斷） | — |

四張許可證的持有廠商均為 UCB Pharma (Hong Kong) Limited。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
ADHD 沒有任何臨床試驗，現有文獻都是間接證據（RLS 回顧、前臨床研究），證據等級僅 L4。香港仿單的警語與禁忌資料尚缺，無法進入安全性篩選。

另外四項預測的證據更弱。精神分裂症有類別層級的統合分析，但多巴胺促效劑可能惡化精神病症狀，風險需特別評估。其餘三項罕見疾病完全沒有證據與機轉連結。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌症與藥物交互作用資料
- 補齊 DrugBank 作用機轉資料
- 搜尋 Rotigotine 用於 ADHD 的臨床或真實世界研究，若無，先規劃探索性研究
- 評估貼片劑型與預期 ADHD 族群（含兒童）的適用性
- 本結果僅供研究參考，不構成醫療建議，需經臨床驗證
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

