---
layout: default
title: Dobutamine
parent: 僅模型預測 (L5)
nav_order: 287
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dobutamine：預測新適應症為禿髮 (Alopecia)（證據等級 L5）。原適應症：本次彙整資料未載明"
monitor_inn: "DOBUTAMINE"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "open-angle glaucoma", "Raynaud disease", "primary hereditary glaucoma", "headache disorder", "hypertrichosis (disease)", "migraine disorder"]
---

# Dobutamine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Dobutamine：從（原適應症未登載）到禿髮（Alopecia）

## 一句話總結

Dobutamine 是靜脈注射用的 β1 腎上腺素受體促效劑（強心藥），香港已有 4 張有效許可證，但本次彙整的資料未載明原核准適應症。
TxGNN 模型預測它可能對**禿髮 (Alopecia)** 有效，但目前**沒有臨床試驗**，只有 **1 篇**相關度很低的獸醫病例報告。
整體而言，這是純模型預測，缺乏實際證據，也找不到合理的藥理機轉。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次彙整資料未載明 |
| 預測新適應症 | 禿髮 (Alopecia) |
| TxGNN 預測分數 | 99.85% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Dobutamine 屬於 β1 腎上腺素受體促效劑類的強心藥（inotrope），靜脈輸注給藥，用於需要心肌收縮支持的情況。

**這個預測的機轉合理性很低。** Dobutamine 的 β 腎上腺素作用在毛囊週期調控中沒有已知角色。高分很可能是知識圖譜的假象：圖譜中 dobutamine 與 minoxidil（血管擴張劑，可促進毛髮生長）有共同關聯，而不是來自 dobutamine 本身的藥理。

排名較前的其他預測（先天性毛髮稀少、圓形禿、多毛症等）同樣缺乏機轉與臨床依據。圓形禿屬自體免疫疾病，dobutamine 沒有相關的免疫調節作用。多毛症是 minoxidil 的副作用，誘發毛髮生長也不是 dobutamine 有意義的再利用目標。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41046802](https://pubmed.ncbi.nlm.nih.gov/41046802/) | 2025 | 病例報告（獸醫） | Journal of Veterinary Cardiology | 一隻貓因 minoxidil 中毒導致心衰竭，住院期間因低血壓使用 dobutamine；並非以 dobutamine 治療禿髮 |

此篇文獻僅是 minoxidil 中毒病例中的併用處置，不能支持 dobutamine 對禿髮的療效。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68119 | DOBUTAMINE CONCENTRATE FOR SOLUTION FOR INFUSION 250MG/20ML | 輸注用濃縮液 | 未載明 |
| HK-40604 | DOBUTAMINE HCL INJ 250MG/20ML (HOSPIRA) | 注射劑 | 未載明 |
| HK-63922 | DOBUTEL CONCENTRATE FOR SOLUTION FOR INFUSION 250MG/5ML | 輸注用濃縮液 | 未載明 |
| HK-66677 | DOBUTAMINE-HAMELN CONCENTRATE FOR SOLUTION FOR INFUSION 250MG/20ML | 輸注用濃縮液 | 未載明 |

---

## 安全性考量

- **禁忌／需謹慎的疾病（來自知識圖譜的藥物－疾病禁忌關聯，非仿單內容）**：高血壓、低血鉀症、心房顫動、主動脈瓣狹窄（含瓣膜疾病、主動脈瓣上狹窄）、心肌梗塞（含冠狀動脈血栓）、血紅素病變、肥厚性心肌病變（含家族性）。
- **藥物交互作用**：資料庫共收錄 100 筆交互作用，以下為其中的中度等級項目：
  - 降血糖藥物：acarbose、albiglutide、alogliptin、metformin、pioglitazone、canagliflozin、chlorpropamide、dapagliflozin、dulaglutide、empagliflozin、linagliptin、repaglinide、semaglutide、liraglutide、胰島素（aspart、degludec）
  - 其他：cimetidine、diethylpropion、phentermine、vancomycin
- **用藥途徑相關**：dobutamine 僅為靜脈給藥，具心律不整風險；用於毛髮疾病並不合理。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測全為 L5 等級，沒有臨床試驗，也沒有支持性文獻；唯一一篇文獻只是 minoxidil 中毒的獸醫病例。
- 高分來自與 minoxidil 的圖譜關聯，缺乏藥理依據，且 dobutamine 只能靜脈給藥，具心血管風險，不適合毛髮疾病的長期治療。

**若要推進需要：**
- 補齊香港仿單的核准適應症、警語與禁忌資料
- 補齊作用機轉資料，並重新評估與禿髮的機轉關聯
- 先做前臨床（如毛囊模型）研究，確認是否有任何生物學訊號
- 評估局部給藥等替代途徑的可行性
- 建議將資源轉向機轉與證據更完整的候選藥物
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

