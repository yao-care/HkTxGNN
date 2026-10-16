---
layout: default
title: Erdafitinib
parent: 僅模型預測 (L5)
nav_order: 331
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Erdafitinib：預測新適應症為肺動脈高壓 (Pulmonary Hypertension)（證據等級 L5）。原適應症：本次整理的資料中未載明"
---

# Erdafitinib
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

# Erdafitinib：從（原適應症資料未提供）到肺動脈高壓

## 一句話總結

Erdafitinib 是一種泛 FGFR（FGFR1-4）酪胺酸激酶抑制劑，目前在香港已有上市許可證，但本報告所整理的資料中未載明其核准適應症。
TxGNN 模型預測它可能對**肺動脈高壓 (Pulmonary Hypertension)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次整理的資料中未載明 |
| 預測新適應症 | 肺動脈高壓 (Pulmonary Hypertension) |
| TxGNN 預測分數 | 99.38% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Erdafitinib 是泛 FGFR（FGFR1-4）酪胺酸激酶抑制劑。FGF/FGFR 訊號與肺動脈高壓中的肺血管重塑、平滑肌及內皮細胞增生有關，因此理論上存在機轉連結。

不過，這項預測純粹來自計算模型，目前沒有臨床試驗或文獻佐證。激酶抑制劑也可能帶來心血管與體液相關的毒性，加上已記錄 100 筆藥物交互作用，會讓安全性評估更複雜。目前沒有臨床證據支持將其用於肺動脈高壓。

目前缺乏來自 DrugBank 的詳細作用機轉資料，上述機轉說明僅為依已知 FGFR 生物學所做的推論。

### 其他預測適應症（皆為 L5，建議 Hold）

| 排名 | 預測疾病 | TxGNN 分數 | 備註 |
|------|---------|-----------|------|
| 2 | 脊柱後側彎性心臟病 | 99.27% | 與 FGFR 抑制無明確機轉關聯，可能反映與肺動脈高壓的網絡接近性 |
| 3 | 閉經 | 99.26% | FGFR 功能喪失才會致病，抑制預期無治療效果 |
| 4 | 類風濕性關節炎 | 99.25% | FGFR 與滑膜纖維母細胞活化有關，但未經驗證；僅有 1 篇一般性激酶抑制劑綜述 |
| 5 | 肌萎縮性脊髓側索硬化症 (ALS) | 99.06% | FGF 訊號在 ALS 模型中失調，但方向與治療相關性不明 |
| 6 | 短指併指症候群 | 99.03% | 先天發育異常，成人藥物治療不太可能逆轉 |
| 7–8 | ALS 22 型、ALS 易感性 | 98.91%、98.88% | 與一般 ALS 預測重疊，無直接證據 |
| 9 | 軸性脊椎幹骺端發育不良 | 98.83% | 無已知機轉 |
| 10 | Mills 症候群 | 98.78% | 可能因接近 ALS／運動神經元疾病群集而被預測 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首要預測（肺動脈高壓）目前無相關文獻。

在排名第 4 的類風濕性關節炎預測下，僅有以下一篇一般性文獻，與 erdafitinib 用於類風濕性關節炎無直接關聯：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31862477](https://pubmed.ncbi.nlm.nih.gov/31862477/) | 2020 | Review | Pharmacological Research | FDA 核准小分子蛋白激酶抑制劑的性質更新，涵蓋 2019 年核准的 erdafitinib 等藥物 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66726 | BALVERSA TABLETS 3MG | 錠劑 | 未載明 |
| HK-66727 | BALVERSA TABLETS 4MG | 錠劑 | 未載明 |
| HK-66728 | BALVERSA TABLETS 5MG | 錠劑 | 未載明 |

三張許可證均為單方、有效狀態，持證商為 Johnson & Johnson (Hong Kong) Ltd.。

---

## 細胞毒性

Erdafitinib 屬標靶抗腫瘤藥物（FGFR 激酶抑制劑），不是傳統細胞毒性化療藥物。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（FGFR 酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：已記錄 100 筆交互作用，以下為部分主要項目：
  - **嚴重 (Major)**：Cholecalciferol、Dexamethasone、Calcium Phosphate、Calcifediol、Calcitriol、Calcium acetate、Clarithromycin、Magnesium oxide、Magnesium sulfate、Magnesium chloride
  - **中度 (Moderate)**：Metformin、Loperamide、Saxagliptin、Eliglustat、Empagliflozin、Linagliptin、Naldemedine、Naloxegol、Prucalopride、Rifaximin

其餘警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型預測（L5），沒有臨床試驗，也沒有 erdafitinib 專屬的文獻支持。
- 肺動脈高壓雖有 FGFR 訊號的理論依據，但缺乏實證；同時缺少仿單安全性資料與作用機轉資料，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌症、核准適應症）並完成解析
- 補充 DrugBank 的作用機轉資料
- 進行肺動脈高壓相關的前臨床研究（如 FGFR 抑制於肺血管重塑模型）與文獻系統性檢索
- 評估 FGFR 抑制劑在肺動脈高壓族群的心血管與體液相關安全風險
- 審視 100 筆藥物交互作用，特別是 Major 等級者，作為風險管理依據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

