---
layout: default
title: Esomeprazole
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 3
---

# Esomeprazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Esomeprazole：從胃食道逆流症到十二指腸胃逆流

## 一句話總結

Esomeprazole（艾美拉唑）是質子幫浦抑制劑（PPI），廣泛用於治療胃食道逆流症、侵蝕性食道炎及幽門螺旋桿菌感染的根除療法。
TxGNN 模型預測它可能對**十二指腸胃逆流（Duodenogastric Reflux）**有效，
目前有 **0 個臨床試驗**和 **1 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 胃食道逆流症（GERD）、侵蝕性食道炎、幽門螺旋桿菌感染、NSAID 相關消化性潰瘍 |
| 預測新適應症 | 十二指腸胃逆流（Duodenogastric Reflux） |
| TxGNN 預測分數 | 99.53% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未查得上市記錄 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據文獻記載（PMID 18679668），Esomeprazole 是奧美拉唑（Omeprazole）的 S-對映異構體，屬質子幫浦抑制劑（PPI）類藥物。其主要作用在於不可逆地抑制胃壁細胞的 H⁺/K⁺-ATPase（質子幫浦），大幅減少胃酸分泌，相比消旋奧美拉唑具有更一致的藥代動力學特性與更強的胃酸控制效果。

十二指腸胃逆流（Duodenogastric Reflux，DGR）是指含有膽汁和胰液的十二指腸內容物異常逆流至胃腔，導致胃黏膜損傷與症狀。在有胃酸共存的環境下，膽汁的細胞毒性作用更強，理論上抑制胃酸分泌可緩解胃黏膜所受的複合刺激，這正是 TxGNN 模型預測合理性的主要機轉依據。

然而，DGR 的核心病理機轉與胃酸過多並不相同，主要涉及幽門括約肌功能失調及上消化道動力異常。PPI 在胃食道逆流症（GERD）的療效已有充分臨床數據支持，但針對單純十二指腸胃逆流的療效，目前缺乏直接的臨床試驗驗證，機轉關聯性有限，需謹慎解讀此預測結果。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [18679668](https://pubmed.ncbi.nlm.nih.gov/18679668/) | 2008 | Review | European Journal of Clinical Pharmacology | 回顧 PPI 類藥物臨床應用與藥代動力學，確認 Esomeprazole 等 PPI 為消化性潰瘍、H. pylori 感染、GERD、NSAID 相關腸胃損傷及 Zollinger-Ellison 症候群的第一線用藥 |

---

## 香港上市資訊

目前資料庫查詢未找到 Esomeprazole 在香港的藥品許可證記錄（市場狀態：未上市，許可證數：0）。

> ⚠️ 注意：Esomeprazole（商品名 Nexium®）在全球多個地區已為廣泛上市藥品，建議進一步向香港衛生署藥物辦公室（Pharmaceutical and Poisons Branch）確認最新登記狀態，可能存在資料庫收錄落差。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
目前預測的新適應症「十二指腸胃逆流」僅有 1 篇 PPI 通論性回顧文獻，缺乏針對 DGR 的直接臨床試驗與機轉研究；加上十二指腸胃逆流的主要病理機轉（幽門功能失調、膽汁逆流）與 PPI 的胃酸抑制機轉存在根本差異，在累積更充分的直接證據之前，不建議推進。

**若要推進需要：**
- 搜尋 PPI 用於十二指腸胃逆流的觀察性研究或隨機對照試驗
- 確認 Esomeprazole 在膽汁逆流性胃炎或混合性逆流（GERD + DGR）患者中的療效數據
- 向香港衛生署藥物辦公室核實 Esomeprazole 正式上市許可狀態及核准適應症
- 補充完整的作用機轉（MOA）資料及香港仿單警語與禁忌症
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

