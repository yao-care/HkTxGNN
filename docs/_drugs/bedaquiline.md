---
layout: default
title: Bedaquiline
parent: 僅模型預測 (L5)
nav_order: 96
evidence_level: L5
indication_count: 10
---

# Bedaquiline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Bedaquiline：從多重抗藥性肺結核到牛結核病

## 一句話總結

Bedaquiline 是抗結核藥物，核准用途為多重抗藥性肺結核（MDR-TB）。
TxGNN 模型預測它可能對**牛結核病 (Tuberculosis, bovine)** 有效。
目前**沒有任何臨床試驗或文獻**直接支持這個預測，僅有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 牛結核病 (Tuberculosis, bovine) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Bedaquiline 抑制分枝桿菌的 ATP 合成酶（subunit c，AtpE），這是分枝桿菌高度保守的藥物標靶。DrugBank 目前沒有提供完整的作用機轉資料，以上機轉來自模型的推論說明。

牛結核病由牛分枝桿菌（*M. bovis*）引起，屬於結核分枝桿菌複合群（*M. tuberculosis* complex）。這個菌群與 Bedaquiline 已證實有效的結核菌親緣很近，共用同一個標靶，所以藥理上有活性的可能。

不過，目前沒有任何針對 *M. bovis* 的試驗或文獻，這個預測只是機轉上說得通，尚未有實際證據。

## 臨床試驗證據

目前無相關臨床試驗登記

## 文獻證據

目前無相關文獻

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-64766 | SIRTURO TABLETS 100MG | JOHNSON & JOHNSON (HONG KONG) LTD. |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 「牛結核病」這項預測只有模型分數（L5），沒有試驗或文獻，暫不建議推進。
- 同一份資料中，「非活動性結核 (inactive tuberculosis)」的證據較多，包括 Phase 2/3 的 BREACH-TB 預防試驗（尚未開始收案），可優先評估。

**若要推進需要：**
- 取得 Bedaquiline 對 *M. bovis* 的體外或動物實驗活性資料
- 收集牛結核病（含人類感染 *M. bovis*）的相關臨床或病例文獻
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症
- 補充 DrugBank 的作用機轉資料
- 評估給藥途徑與劑型是否適用於目標族群
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

