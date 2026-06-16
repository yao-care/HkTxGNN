---
layout: default
title: Guselkumab
parent: 僅模型預測 (L5)
nav_order: 364
evidence_level: L5
indication_count: 5
---

# Guselkumab
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

# Guselkumab：從乾癬到藥物性骨質疏鬆

## 一句話總結

Guselkumab 是一種人源化 IL-23 p19 亞基抑制劑（單株抗體），全球已獲 FDA/EMA 核准用於中重度斑塊型乾癬及乾癬性關節炎，但香港目前**尚無上市許可**。TxGNN 模型的最高排名預測顯示，此藥可能對**藥物性骨質疏鬆 (Drug-induced Osteoporosis)** 有效，然而目前**無臨床試驗**及**無支持文獻**，仍處於純模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 中重度斑塊型乾癬（全球核准；香港未上市） |
| 預測新適應症 | 藥物性骨質疏鬆 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 99.84% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏完整的 MOA 資料記錄，根據現有研究文獻，Guselkumab 選擇性結合 IL-23 的 p19 亞基，阻斷 IL-23 訊號傳遞，抑制 Th17 細胞分化與 IL-17A/F、IL-22 等效應細胞因子的產生，最終減少角質細胞過度增生與皮膚慢性發炎。這一機轉在乾癬（其 TxGNN 預測排名第 3，證據等級 L1）的治療中已獲充分驗證。

IL-23/Th17 軸與骨代謝之間存在間接生物學關聯：Th17 細胞分泌的 IL-17 可刺激成骨細胞表面 RANKL 表現，進而促進破骨細胞分化與骨吸收。從理論上推論，阻斷 IL-23 可減少 IL-17 驅動的骨吸收路徑，對骨質流失有潛在保護效果。

然而，藥物性骨質疏鬆（尤其是類固醇誘發型）的核心病理機轉為 Wnt/BMP 路徑抑制、腸道鈣吸收減少、腎小管鈣流失增加，以及成骨細胞凋亡加速等，與 IL-23 通路的關聯屬**間接且高度推測性**，尚無任何臨床前或臨床資料支持。TxGNN 高預測分數（99.84%）反映的是知識圖譜中節點間的連結強度，而非臨床療效訊號。

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

**決策：Hold**

**理由：**
藥物性骨質疏鬆與 IL-23/Th17 路徑的機轉關聯屬純理論推測，目前完全缺乏臨床前動物模型、體外實驗、臨床試驗及文獻支持，證據等級僅為 L5。此外，Guselkumab 在香港尚未取得任何上市許可，存在法規缺口，需優先處理。

**若要推進需要：**
- **臨床前研究**：在藥物性骨質疏鬆動物模型中，評估 IL-23 抑制對骨密度（BMD）及骨轉換標記的影響
- **機轉釐清**：確認 guselkumab 的 MOA 與藥物性骨質疏鬆病理的重疊性（例如：RANKL/OPG 比值變化、Wnt 訊號交互作用）
- **香港法規途徑**：先完成乾癬適應症的 HK Department of Health 上市申請（現有 FDA/EMA 核准可作為依據）
- **安全性資料補齊**：下載原廠仿單 PDF，解析警語、禁忌症及主要不良事件資料

> **附註**：TxGNN 預測中，乾癬（Psoriasis）排名第 3（預測分數 99.75%，證據等級 L1，建議 Proceed with Guardrails），具有 **50 個臨床試驗**及 **20 篇文獻**支持，為本次 Evidence Pack 中科學證據最充分的適應症，建議優先以乾癬適應症推動香港上市申請。
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

