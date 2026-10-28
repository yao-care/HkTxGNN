---
layout: default
title: Albutrepenonacog Alfa
parent: 僅模型預測 (L5)
nav_order: 31
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Albutrepenonacog Alfa：預測新適應症為偽性血管性血友病 (pseudo-von Willebrand disease)（證據等級 L5）。原適應症：血友病（hemophilia）、女性帶因者的症狀性血友病"
monitor_inn: "ALBUTREPENONACOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia"]
---

# Albutrepenonacog Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Albutrepenonacog alfa：從血友病到偽性血管性血友病（pseudo-von Willebrand disease）
{: .text-alpha }

## 一句話總結

Albutrepenonacog alfa 是與白蛋白融合的重組第九凝血因子（rFIX-FP），原本用於血友病（hemophilia）的治療。
TxGNN 模型預測它可能對**偽性血管性血友病 (pseudo-von Willebrand disease)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測分數，且機轉上缺乏合理依據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 血友病（hemophilia）、女性帶因者的症狀性血友病 |
| 預測新適應症 | 偽性血管性血友病 (pseudo-von Willebrand disease) |
| TxGNN 預測分數 | 0.9994 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Albutrepenonacog alfa 是融合白蛋白的重組第九凝血因子，可延長半衰期，用於 B 型血友病（缺乏第九因子）的補充治療。

偽性血管性血友病是血小板型疾病，由 GP1BA 基因功能增強變異造成，使血小板與血管性血友病因子（VWF）過度結合。第九因子補充無法修正這個血小板受體缺陷。因此，兩者雖同屬出血性疾病，但這個預測的高分（0.9994）來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據，也很可能只是「出血疾病」表型的相似，而非共同的標靶或路徑。

其他預測的適應症也有類似問題：

| 排名 | 預測適應症 | 分數 | 機轉評估 |
|------|-----------|------|---------|
| 2 | 血小板釋放功能異常 (primary release disorder of platelets) | 0.9994 | 第九因子無法矯正血小板功能缺陷 |
| 3 | Glanzmann 血小板無力症 | 0.9992 | 缺陷在 αIIbβ3 整合素與血小板聚集，屬不同路徑；標準治療為血小板輸注、重組第七因子 |
| 4 | Scott 症候群 | 0.9963 | 第九因子屬 tenase 複合體，理論上可能部分補償，但限制因素是膜表面而非第九因子，效益屬推測 |
| 5 | 膠原蛋白受體缺陷所致出血體質 | 0.9928 | 第九因子不影響受體介導的血小板黏附 |
| 6 | 先天性血小板減少所致出血性疾病 | 0.9926 | 第九因子無法矯正血小板數量 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65142 | IDELVION 注射用粉末及溶劑 250IU | 注射劑（粉末及溶劑） | 資料未提供 |
| HK-65143 | IDELVION 注射用粉末及溶劑 500IU | 注射劑（粉末及溶劑） | 資料未提供 |
| HK-65144 | IDELVION 注射用粉末及溶劑 1000IU | 注射劑（粉末及溶劑） | 資料未提供 |
| HK-65145 | IDELVION 注射用粉末及溶劑 2000IU | 注射劑（粉末及溶劑） | 資料未提供 |

四張許可證均為單方、有效，持證商為 CSL Behring Asia Pacific Limited。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有 TxGNN 模型預測（證據等級 L5），無臨床試驗與文獻支持。
- 偽性血管性血友病的病因是血小板受體缺陷，第九因子補充無法針對此機轉，預測可能源自出血性疾病表型的相似性。

**若要推進需要：**
- 取得 Albutrepenonacog alfa 完整的作用機轉資料。
- 取得香港原廠仿單，完成警語與禁忌症的安全性評估。
- 進行文獻與病例回顧，確認是否有第九因子用於血小板型出血疾病的任何證據。
- 若仍要探索，應優先評估機轉上較有可能的 Scott 症候群，並以前臨床研究驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

