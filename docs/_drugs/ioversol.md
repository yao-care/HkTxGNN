---
layout: default
title: Ioversol
parent: 僅模型預測 (L5)
nav_order: 480
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ioversol：預測新適應症為骨關節炎易感性 (Osteoarthritis Susceptibility)（證據等級 L5）。原適應症：本報告所整理的資料中，香港許可證未提供核准適應症文字"
monitor_inn: "Ioversol"
predicted_indications: ["osteoarthritis susceptibility", "osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "alopecia"]
---

# Ioversol
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

# Ioversol：從放射顯影造影（原適應症資料缺漏）到退化性關節炎（骨關節炎）

## 一句話總結

Ioversol 是一種含碘的非離子型放射顯影造影劑，用於影像檢查，並非治療藥物。
TxGNN 模型預測它可能對**骨關節炎易感性 (Osteoarthritis Susceptibility)** 有效，但目前**沒有任何臨床試驗**，也沒有直接支持的文獻，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本報告所整理的資料中，香港許可證未提供核准適應症文字 |
| 預測新適應症 | 骨關節炎易感性 (Osteoarthritis Susceptibility) |
| TxGNN 預測分數 | 99.67% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ioversol 是含碘的非離子型造影劑，其用途是在影像檢查中增強顯影，沒有已知的藥理作用會影響骨關節炎的遺傳易感性。

TxGNN 給出的高分（99.67%）來自知識圖譜中的網路關聯，而不是實際的藥理或臨床證據。同一份預測清單中，還出現了骨骼發育不良、血紅素病變、禿髮等彼此無關的疾病，這也提示分數較可能反映圖譜結構上的相近性，而非真正的治療潛力。

因此，這項預測在機轉上**沒有可辨識的合理連結**，不建議把高分解讀為療效訊號。

### 其他預測適應症概覽

| 排名 | 預測疾病 | TxGNN 分數 | 證據等級 | 說明 |
|------|---------|-----------|---------|------|
| 2 | 骨關節炎 (Osteoarthritis) | 99.63% | L4 | 僅有 1 篇間接文獻，為栓塞術研究，並非 ioversol 的藥理作用 |
| 3 | 類風濕性關節炎 (Rheumatoid Arthritis) | 99.56% | L5 | 兩篇文獻皆與 ioversol 無關 |
| 4–10 | 短軀幹症、血紅素病變、肌硬化症、禿髮等 | 99.25%–99.36% | L5 | 無試驗、無文獻、無機轉依據 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測（骨關節炎易感性），目前無相關文獻。

作為參考，相近的「骨關節炎」預測下有 1 篇間接文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | 臨床試驗（單臂、介入） | Diagnostic and Interventional Imaging | LipioJoint-1 試驗：以乙碘化油 (ethiodized oil) 乳劑進行膝部動脈栓塞，評估膝關節骨關節炎的安全性與療效。治療主體並非 ioversol，僅屬程序上的間接關聯 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-38527 | OPTIRAY-350 INJ 74% | 注射劑 | 請參考原廠仿單 |
| HK-38528 | OPTIRAY-300 INJ 64% | 注射劑 | 請參考原廠仿單 |
| HK-38526 | OPTIRAY-320 INJ 68% | 注射劑 | 請參考原廠仿單 |

三張許可證皆為單一成分、現行有效，持證商為 GUERBET ASIA PACIFIC LIMITED。

---

## 安全性考量

**藥物交互作用**：本次查詢共找到 100 筆交互作用紀錄，以下列出部分重要項目：

- **Major（嚴重）**：Metformin、Amphotericin B（含脂質複合體、膽固醇硫酸酯、脂質體劑型）、Mesalazine、Balsalazide、Olsalazine、Sulfasalazine、Vancomycin、Kanamycin、Neomycin、Streptomycin、Polymyxin B
- **Moderate（中度）**：Mannitol
- **等級未明**：Atropine、Famotidine、Acetylsalicylic acid、Morphine、Omeprazole

其中多數嚴重交互作用涉及具腎毒性的藥物，以及 Metformin，用藥前應評估腎功能。

其他警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症皆無臨床試驗，且沒有可辨識的藥理機轉。Ioversol 是診斷用造影劑，高 TxGNN 分數缺乏實質證據支持，證據等級為 L5。
- 唯一相關的文獻是以其他碘化油為主體的栓塞程序研究，不能視為 ioversol 的療效證據。

**若要推進需要：**
- 取得 ioversol 的作用機轉資料，並確認是否有任何生物學上可能影響關節或骨骼病理的途徑
- 取得香港仿單中的警語、禁忌症與核准適應症
- 至少有體外或動物模型的前臨床研究，作為支持
- 考量造影劑本身的腎毒性與交互作用風險，評估作為治療用途是否可行，並釐清給藥途徑
- 建議把資源優先放在有實際機轉與臨床依據的候選藥物上
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

