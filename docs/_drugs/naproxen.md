---
layout: default
title: Naproxen
parent: 僅模型預測 (L5)
nav_order: 514
evidence_level: L5
indication_count: 4
---

# Naproxen
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

# Naproxen：從 NSAID 疼痛消炎適應症到罕見骨骼發育症候群

## 一句話總結

Naproxen 是常見的非類固醇消炎止痛藥（NSAID），原始核准適應症資料目前尚未收集完整。TxGNN 模型將其與 4 個罕見先天性骨骼/發育症候群連結，分數最高的是**肢端骨發育異常—併指症候群 (Brachydactyly-Syndactyly Syndrome)**，但目前**無任何臨床試驗、無文獻**支持，且模型本身提供的機轉推論文字明確指出這些連結**缺乏藥理學基礎**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料尚未收集（HK 許可證與仿單資料均缺，僅知 Naproxen 為 NSAID 類藥物） |
| 預測新適應症 | 肢端骨發育異常—併指症候群 (Brachydactyly-Syndactyly Syndrome) |
| TxGNN 預測分數 | 99.35%（圖譜排名第 10,858 名） |
| 證據等級 | L5（僅有模型預測，無臨床或文獻證據） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Naproxen 的完整作用機轉（MOA）資料目前缺乏，但根據 Evidence Pack 中各候選項的機轉分析文字，可確認 Naproxen 屬 NSAID 類藥物，機轉為抑制 COX-1/COX-2 以緩解疼痛與發炎。

TxGNN 這次預測的 4 個新適應症，全部是罕見先天性骨骼/眼部發育異常症候群（分別涉及肢端骨形成缺陷、BMP/GDF5 訊號路徑異常、結締組織礦化缺陷等胚胎發育機制）。這些疾病的病理生理與 NSAID 的抗發炎/止痛機轉**沒有已知交集**。

Evidence Pack 提供的 `repurposing_rationale.mechanistic_link` 對每一項都明確標註「無已知機制連結」「僅為圖譜拓樸相似性訊號，非真實藥理機轉」，並直接提示這些高分預測應視為**潛在偽陽性**，而非真正的再利用機會。

---

## 其他候選適應症（Rank 2–4，同屬低信心）

| 排名 | 疾病名稱 | TxGNN 分數 | 證據等級 | 機轉關聯 |
|------|---------|-----------|---------|---------|
| 2 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.22% | L5 | 無已知關聯 |
| 3 | Acromesomelic dysplasia, Hunter-Thompson type | 99.17% | L5 | 無已知關聯（GDF5/BMP 路徑） |
| 4 | Brachyolmia-amelogenesis imperfecta syndrome | 99.06% | L5 | 無已知關聯 |

4 個候選皆無臨床試驗（ClinicalTrials.gov、ICTRP）與文獻（PubMed）檢索結果。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

Naproxen 目前**未在香港上市**，無有效許可證資料可列出。

## 安全性考量

安全性資訊請參考原廠仿單。

（註：TFDA/HK 仿單警語與禁忌資料為 Blocking 等級缺口，尚未補齊，無法進入安全性初評 S1 階段。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 4 個預測適應症皆為 L5 證據等級（僅模型分數，無臨床或文獻佐證），且模型自身提供的機轉分析已明確指出與 Naproxen 藥理機轉無關聯，偽陽性風險高。
- 安全性初評所需的仿單警語/禁忌資料為 Blocking 缺口，目前無法進行下一步評估。

**若要推進需要：**
- 補齊 Naproxen 完整 MOA 資料（DrugBank API）
- 補齊 TFDA/HK 仿單警語與禁忌症資料，解除 Blocking 缺口
- 若持續評估此候選，建議先釐清 TxGNN 高分是否為知識圖譜拓樸偽陽性，而非真實藥理訊號
- 目前 4 項候選皆缺乏臨床/文獻支持，建議暫緩投入資源，待有機轉層級新證據再重啟評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

