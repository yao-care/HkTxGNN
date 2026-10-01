---
layout: default
title: Minoxidil
parent: 中證據等級 (L3-L4)
nav_order: 581
evidence_level: L4
indication_count: 5
---

# Minoxidil
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

# Minoxidil：從雄激素性禿髮到遺傳性頭皮稀毛症

## 一句話總結

Minoxidil 是外用及口服的生髮藥物，在香港以 5% 外用溶液和泡沫劑型上市。
TxGNN 模型預測它可能對**遺傳性頭皮稀毛症 (Hypotrichosis Simplex of the Scalp)** 有效。
目前**沒有臨床試驗**，只有 **3 篇個案報告**，且每篇都合併其他療法。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 雄激素性禿髮（依文獻記載；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 遺傳性頭皮稀毛症 (Hypotrichosis Simplex of the Scalp) |
| TxGNN 預測分數 | 99.9999% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。依現有資訊，Minoxidil 是已確立的生髮藥物，其硫酸鹽代謝物會開啟 K-ATP 通道，可能延長生長期 (anagen)，並可能上調 VEGF。

遺傳性頭皮稀毛症是一種罕見的單基因顯性遺傳疾病，特徵是毛髮生長不良、長度與密度不足。文獻提到病例與 *CDSN* 基因變異有關。它和雄激素性禿髮同屬毛髮週期或毛囊微小化的問題，因此機轉上有合理的對應。

但這個預測目前只有低層級證據支持。三篇報告中，Minoxidil 都與其他介入合併使用（口服加生長因子、加植物萃取物、加 PRP 注射），無法區分 Minoxidil 本身的療效。另外，*CDSN* 突變造成的遺傳缺陷是否對 Minoxidil 有反應，仍不確定。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35761391](https://pubmed.ncbi.nlm.nih.gov/35761391/) | 2022 | 個案報告 | Dermatologic Therapy | 以口服 Minoxidil 合併生長因子治療遺傳性頭皮稀毛症（無摘要，依標題整理） |
| [39902296](https://pubmed.ncbi.nlm.nih.gov/39902296/) | 2024 | 個案報告 | Frontiers in Genetics | 一名 *CDSN* 突變的 8 歲男童，使用植物萃取物合併 Minoxidil 治療 |
| [36651821](https://pubmed.ncbi.nlm.nih.gov/36651821/) | 2023 | 個案報告 | J Dermatol Treat | 一名 14 歲患者，以 PRP 注射合併外用 Minoxidil 2% 治療，報告成功 |

## 香港上市資訊

許可證資料未提供劑型與適應症欄位，下表劑型由品名推斷。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56024 | HUDSON MOXIDIL SOLUTION 5% | 外用溶液 | 許可證資料未載明 |
| HK-56023 | OSCO MOXIDIL SOLUTION 5% | 外用溶液 | 許可證資料未載明 |
| HK-51765 | MINOXI 5 SOLUTION 5%W/V | 外用溶液 | 許可證資料未載明 |
| HK-52161 | REGAINE EXTRA STRENGTH FOR MEN TOPICAL SOLN 5% | 外用溶液 | 許可證資料未載明 |
| HK-64008 | REGAINE FOR MEN TOPICAL FOAM 5%W/W | 外用泡沫 | 許可證資料未載明 |

以上為 20 張許可證中的 5 張。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數極高，但實際證據只有 3 篇個案報告，且 Minoxidil 皆為合併療法的一部分，無法判斷單獨療效。
- 香港衛生署仿單的警語與禁忌資料尚未取得，這是阻擋進入安全性篩選的缺口。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症資料
- 取得 DrugBank 的作用機轉資料，強化機轉連結分析
- 取得三篇個案報告的全文，確認 Minoxidil 的劑量、劑型（口服或外用）和療效指標
- 設計能分離 Minoxidil 單獨效果的研究（例如 Minoxidil 單藥對照），並評估 *CDSN* 相關基因型是否有反應
- 確認香港上市產品皆為外用劑型；若考慮口服 Minoxidil，需另行評估其安全性與法規狀態
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

