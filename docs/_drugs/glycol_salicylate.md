---
layout: default
title: Glycol Salicylate
parent: 僅模型預測 (L5)
nav_order: 356
evidence_level: L5
indication_count: 10
---

# Glycol Salicylate
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

# Glycol Salicylate：從局部抗炎止痛到 Glanzmann 血小板無力症

## 一句話總結

Glycol salicylate（乙二醇水楊酸酯）是一種外用水楊酸類藥物，已知用於局部抗炎止痛（肌肉骨骼疼痛）。TxGNN 模型預測它最有可能對 **Glanzmann 血小板無力症 (Glanzmann thrombasthenia)** 有效，但目前 **無任何臨床試驗或文獻** 支持此方向，且機轉分析顯示此預測極可能為假陽性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無登錄資料（已知為局部水楊酸類止痛外用製劑） |
| 預測新適應症 | Glanzmann 血小板無力症 (Glanzmann thrombasthenia) |
| TxGNN 預測分數 | 98.17% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為資料缺口）。根據已知資訊，Glycol salicylate 屬水楊酸酯類外用藥物，其機轉與其他水楊酸類藥物相似——主要透過抑制 COX-1/COX-2 酶，減少前列腺素（PGE2、TXA2）合成，達到局部抗炎與止痛效果。

Glanzmann 血小板無力症（Glanzmann thrombasthenia）是一種先天性血小板功能障礙，源於 GPIIb/IIIa（整合素 αIIbβ3）缺陷，導致血小板無法正常聚集，患者常有嚴重出血傾向。

**然而，此預測存在重大機轉疑慮**：水楊酸類透過抑制 COX-1 → 降低 TXA2 → 抑制血小板活化，與 Glanzmann 血小板無力症的病理路徑在生物網絡上確有交集，但其臨床意義相反。水楊酸/NSAID 在血小板功能障礙患者中屬已知禁忌，可能進一步加重出血風險。TxGNN 模型很可能將「生物路徑共享」誤判為「治療潛力」，屬圖形預測假陽性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無針對 Glanzmann 血小板無力症的相關文獻。

> **附註（次要適應症）**：針對 rank 2 預測適應症「自體免疫疾病 (autoimmune disease)」，有 1 篇相關文獻可供參考：
>
> | PMID | 年份 | 類型 | 期刊 | 主要發現 |
> |------|------|------|------|---------|
> | [7759034](https://pubmed.ncbi.nlm.nih.gov/7759034/) | 1995 | 臨床研究（含 RCT 元素） | Fortschritte der Medizin | Hydroxyethylsalicylate 凝膠（本藥同類劑型）用於非關節性風濕性背痛，113 名患者雙盲多中心試驗顯示止痛效果顯著優於安慰劑，局部與全身耐受性佳 |

---

## 香港上市資訊

Glycol salicylate 目前在香港**未登錄上市**，無任何許可證紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> ⚠️ **特別提示**：水楊酸類藥物在血小板功能障礙疾病（包括 Glanzmann 血小板無力症、von Willebrand 病相關疾病）患者中通常屬禁忌，可能進一步抑制血小板活化並加重出血風險。若評估本藥用於任何血小板疾病適應症，應極度謹慎並優先查閱出血風險相關安全資料。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 最高排名預測（Glanzmann 血小板無力症）完全無臨床試驗或文獻支持（L5 證據等級），且機轉分析顯示水楊酸類藥物在血小板功能異常疾病中可能屬禁忌，而非治療選項。
- 香港目前未上市，缺乏監管基礎，且 0 張許可證意味著需從頭建立法規路徑。

**若要推進需要：**
- 補充詳細的作用機轉資料（MOA），確認藥物與各靶疾病的生物路徑關聯是否具有治療意義（而非禁忌）
- 優先重新評估次要適應症「**自體免疫疾病（rank 2）**」的可行性：該預測有抗炎機轉依據，且有初步臨床文獻支持（hydroxyethylsalicylate 凝膠用於風濕性疾病），屬相對可行方向
- 系統性搜尋 hydroxyethylsalicylate 或 glycol salicylate 局部外用於關節炎、風濕性疾病的更多臨床資料
- 若考慮香港上市，需評估藥監局登記路徑（本藥在香港無任何上市紀錄）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

