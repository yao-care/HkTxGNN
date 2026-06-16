---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 317
evidence_level: L5
indication_count: 5
---

# Filgrastim
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

# Filgrastim：從嗜中性白血球減少症到原發性血小板釋放障礙

## 一句話總結

Filgrastim 是重組人類顆粒球群落刺激因子（G-CSF），廣泛用於化療後嗜中性白血球減少症的預防與治療。TxGNN 模型預測它可能對**原發性血小板釋放障礙 (Primary Release Disorder of Platelets)** 有效，目前有 **0 個直接臨床試驗**和 **1 篇間接文獻**，整體支持證據不足。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無香港許可證登記 |
| 預測新適應症 | 原發性血小板釋放障礙 (Primary Release Disorder of Platelets) |
| TxGNN 預測分數 | 99.998% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Filgrastim 透過結合 G-CSF 受體（G-CSFR），啟動 JAK2/STAT3 下游訊號路徑，促進骨髓中骨髓系祖細胞增殖與分化，以及周邊血液中嗜中性白血球的成熟動員。本次 Evidence Pack 的作用機轉欄位尚待補充（DG002），完整 MOA 資料需查詢 DrugBank API 取得。

原發性血小板釋放障礙是一類血小板功能障礙，核心缺陷在於血小板顆粒（dense granule 或 alpha granule）的釋放機制異常，常見成因包括 SNARE 複合體缺陷或顆粒形成不全（如 Hermansky-Pudlak 症候群）。G-CSF 雖可間接上調 TPO（血小板生成素），理論上能促進巨核球分化，但對血小板顆粒的胞內釋放路徑並無已知的直接調控機制。

此項預測屬**遠距機轉推論**：TxGNN 知識圖譜的連結路徑可能為「G-CSF → 骨髓增殖 → 巨核球 → 血小板顆粒」的多跳推論，而非真正的直接機轉對應，生物學合理性偏低。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Clinical Cohort | Frontiers in Immunology | G-CSF 動員健康捐贈者周邊血液幹細胞時，優先動員特定淋巴球亞群；研究聚焦於異體 HSCT 移植後免疫調節，未直接探討血小板釋放功能，與目標適應症相關性低 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測的 5 項適應症（原發性血小板釋放障礙、偽 von Willebrand 病、Glanzmann 血小板無力症、Scott 症候群、先天性血小板減少症出血障礙）均為 L5 等級，無直接臨床試驗支持，且各適應症的機轉分析均顯示 G-CSF 對目標血小板病理機制缺乏直接介入能力；香港目前無上市許可，MOA 及安全性資料亦待補充。

**若要推進需要：**
- 補充 Filgrastim 完整 MOA 資料，查詢 DrugBank API（解決 DG002）
- 補充香港仿單警語與禁忌症資料（解決 DG001）
- 搜尋 G-CSF 對血小板顆粒功能影響的體外或動物研究，以評估機轉可行性
- 若考慮先天性血小板減少症（Rank 5），可針對 G-CSF 促血小板生成的 off-label 使用進行系統性文獻回顧
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

