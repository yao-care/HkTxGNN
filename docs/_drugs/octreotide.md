---
layout: default
title: Octreotide
parent: 僅模型預測 (L5)
nav_order: 624
evidence_level: L5
indication_count: 2
---

# Octreotide
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

# Octreotide：從原核准適應症到外陰倒置性毛囊角化症

## 一句話總結

Octreotide 是一種在香港已上市的注射劑，本次資料未載明其原核准適應症。
TxGNN 模型預測它可能對**外陰倒置性毛囊角化症 (Vulvar Inverted Follicular Keratosis)** 有效，另外還預測了**脂漏性角化症 (Seborrheic Keratosis)**。
目前**沒有任何臨床試驗或文獻**支持，只有模型分數。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 外陰倒置性毛囊角化症 (Vulvar Inverted Follicular Keratosis) |
| TxGNN 預測分數 | 99.58% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。以下是依一般藥理知識所做的推論，並非來自本次輸入資料。Octreotide 屬於體抑素 (somatostatin) 類似物，作用於 SSTR2/SSTR5 受體，可抑制生長激素與 IGF-1 訊號。理論上，這條路徑可能影響良性角質細胞增生，但這只是未經驗證的假說。

這兩個預測疾病（外陰倒置性毛囊角化症、脂漏性角化症）都是良性表皮病變，通常以局部切除、冷凍或刮除處理。它們的分數幾乎相同（99.58% 與 99.55%），很可能來自知識圖譜中相近的區域，不應視為兩個獨立的發現。

對良性病變使用全身性注射胜肽藥物，在缺乏支持資料的情況下，效益與風險比不利。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68447 | OCTREOTIDE SOLUTION FOR INJECTION OR INFUSION 0.5MG/1ML | HONG KONG MEDICAL SUPPLIES LTD |
| HK-59308 | OCTREOTIDE INJ 100MCG/ML | HONG KONG MEDICAL SUPPLIES LTD |
| HK-62639 | DBL OCTREOTIDE INJECTION 0.5MG/ML | PFIZER CORPORATION HONG KONG LIMITED |
| HK-68446 | OCTREOTIDE SOLUTION FOR INJECTION OR INFUSION 0.1MG/1ML | HONG KONG MEDICAL SUPPLIES LTD |
| HK-32471 | SANDOSTATIN INJ 0.1MG/ML | NOVARTIS PHARMACEUTICALS (HK) LIMITED |

以上列出 5 張主要許可證，全部為注射劑型。劑型欄位與核准適應症在本次資料中均為空白。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據僅有模型預測分數（L5），沒有臨床試驗與文獻。
- 目標疾病是良性且有簡單局部療法的病變，全身性注射不具明顯優勢。

**若要推進需要：**
- 取得香港衛生署 (Department of Health) 的仿單，補齊警語與禁忌症，並確認原核准適應症。
- 補充 Octreotide 的作用機轉資料（可查詢 DrugBank）。
- 進行文獻檢索，確認體抑素受體在角質細胞與脂漏性角化症中是否有表現。
- 評估局部給藥的可行性（目前給藥途徑相容性尚待確認）。

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

