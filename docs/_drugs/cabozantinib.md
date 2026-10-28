---
layout: default
title: Cabozantinib
parent: 僅模型預測 (L5)
nav_order: 143
evidence_level: L5
indication_count: 5
monitor_inn: "Cabozantinib"
predicted_indications: ["liposarcoma", "ovarian myxoid liposarcoma", "amyotrophic lateral sclerosis", "bilateral parasagittal parieto-occipital polymicrogyria", "angiolipoma"]
last_modified_at: 2026-10-27
description: "Cabozantinib：預測新適應症為脂肪肉瘤 (liposarcoma)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Cabozantinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Cabozantinib：多重激酶抑制劑 → 脂肪肉瘤 (liposarcoma)
{: .text-alpha }

## 一句話總結

Cabozantinib 是一種多重激酶抑制劑（VEGFR2、MET、AXL）。
TxGNN 模型預測它可能對**脂肪肉瘤 (liposarcoma)** 有效，
目前有 **1 個臨床試驗**和 **1 篇文獻**與軟組織肉瘤相關，但尚無直接針對脂肪肉瘤的研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 脂肪肉瘤 (liposarcoma) |
| TxGNN 預測分數 | 0.9983 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Cabozantinib 屬於多重酪胺酸激酶抑制劑，標靶包括 VEGFR2、MET 與 AXL。這些分子與腫瘤血管新生及腫瘤進展有關，在軟組織肉瘤中也被認為扮演角色。

脂肪肉瘤屬於軟組織肉瘤的一種，因此從機轉上推測，抑制血管新生與 MET/AXL 訊號的藥物可能具有潛在療效。

不過，目前已有的研究都是針對一般軟組織肉瘤或肢體肉瘤，並未提供脂肪肉瘤亞型的結果。因此這個預測目前仍屬於假說階段。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05836571](https://clinicaltrials.gov/study/NCT05836571) | Phase 2 | 進行中（未招募） | 66 | 隨機分組比較 Ipilimumab + Nivolumab 與加上 Cabozantinib 的組合，用於晚期軟組織肉瘤；尚無脂肪肉瘤亞型的結果 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41770651](https://pubmed.ncbi.nlm.nih.gov/41770651/) | 2026 | Phase 1 試驗 | American Journal of Clinical Oncology | 評估 Cabozantinib 併用放射治療作為肢體軟組織肉瘤的術前治療之安全性 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65656 | CABOMETYX TABLETS 20MG | — | 本地資料未記錄 |
| HK-65654 | CABOMETYX TABLETS 40MG | — | 本地資料未記錄 |
| HK-65655 | CABOMETYX TABLETS 60MG | — | 本地資料未記錄 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（多重酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：本報告彙整的資料顯示共有 100 筆交互作用紀錄，以下為部分重點：
  - 重度：Acetylsalicylic acid、Cisapride、Clarithromycin、Dolasetron、Granisetron、Levofloxacin
  - 中度：Loperamide、Aprepitant、Dexamethasone、Bisacodyl 等
  - 輕度：Fidaxomicin

其他警語與禁忌症請參考原廠仿單。另有一項觀察：在肉瘤合併放射治療的情境下，曾有人擔心瘻管或穿孔風險，這部分需特別留意。

## 結論與下一步

**決策：Hold**

**理由：**
目前沒有任何研究直接探討 Cabozantinib 用於脂肪肉瘤，現有的試驗與文獻僅涉及一般軟組織肉瘤，因此證據等級為 L5。TxGNN 分數雖高，但仍屬計算預測。

**若要推進需要：**
- 取得脂肪肉瘤亞型的臨床試驗結果（例如 NCT05836571 的亞型分析）
- 補充詳細的作用機轉資料（MOA）
- 取得香港原廠仿單的警語與禁忌症資訊
- 針對併用放射治療或免疫治療時的安全性（如瘻管、穿孔風險）建立監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

