---
layout: default
title: Fluocinolone Acetonide
parent: 僅模型預測 (L5)
nav_order: 325
evidence_level: L5
indication_count: 4
---

# Fluocinolone Acetonide
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

# Fluocinolone Acetonide：從發炎性皮膚疾病到肥厚型扁平苔蘚

## 一句話總結

Fluocinolone Acetonide 是一種 Class II 強效外用皮質類固醇，廣泛用於治療各種發炎性皮膚疾病。TxGNN 模型預測它可能對**肥厚型扁平苔蘚 (Hypertrophic Lichen Planus)** 有效，預測分數高達 **99.42%**，但目前**無任何臨床試驗或文獻直接支持**此適應症，結論完全基於模型機轉推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 發炎性皮膚疾病（香港未登記，監管資料不足） |
| 預測新適應症 | 肥厚型扁平苔蘚 (Hypertrophic Lichen Planus) |
| TxGNN 預測分數 | 99.42% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Research Question |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA Data Gap）。根據已知資訊，Fluocinolone acetonide 屬 **Class II 強效外用皮質類固醇**，其藥理效果主要透過抑制 NF-κB 訊號路徑、阻斷 T 淋巴球活化，以及減少促炎細胞激素（如 IL-1、IL-6、TNF-α）的分泌來達成強效抗炎與局部免疫抑制效果。

肥厚型扁平苔蘚（Hypertrophic LP）是扁平苔蘚的慢性亞型，以**慢性角化過度**（hyperkeratosis）合併 **CD8+ T 細胞媒介之真皮介面炎症**（interface dermatitis）為主要病理特徵。由於其病生理高度倚賴 T 細胞活化與炎症介質的持續作用，fluocinolone acetonide 的藥理機轉在理論上與致病路徑具有高度相符性。

臨床上，肥厚型病灶因角化層厚實，通常需要效能較強的外用類固醇（Class I–II）或病灶內注射，才能有效穿透並抑制炎症。Fluocinolone acetonide 的強效特性符合此臨床需求，使 TxGNN 的預測具有合理的機轉基礎。然而，此預測目前**完全缺乏直接臨床研究支持**，需進一步驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Research Question**

**理由：**
Fluocinolone acetonide 用於肥厚型扁平苔蘚的機轉關聯性合理（Class II 強效外用皮質類固醇的抗炎機轉與 T 細胞媒介慢性皮膚炎高度相符），但目前完全缺乏直接臨床或文獻證據（L5），且藥物在香港尚未上市，屬純研究假說階段，尚不具備進入安全性評估的條件。

**若要推進需要：**
- **MOA 資料補充**：從 DrugBank API 取得詳細作用機轉資料，強化機轉關聯性分析
- **安全性仿單解析**：下載原廠仿單 PDF，評估禁忌症、主要警語及長期使用風險（如皮膚萎縮、HPA 軸抑制）
- **間接證據蒐集**：系統性文獻回顧，蒐集其他同類強效外用類固醇（如 clobetasol、betamethasone）用於肥厚型扁平苔蘚的現有證據，作為 class effect 推論基礎
- **其他預測適應症評估**：本次 TxGNN 同時預測 3 個扁平苔蘚亞型（環狀萎縮型、色素沉著型、類天皰瘡型），建議一併納入文獻回顧範圍，評估整體研究價值
- **Pilot Study 設計**：若文獻支持，考慮設計個案系列研究（case series）或前導性臨床試驗
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

