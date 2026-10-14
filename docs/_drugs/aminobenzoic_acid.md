---
layout: default
title: Aminobenzoic Acid
parent: 僅模型預測 (L5)
nav_order: 51
evidence_level: L5
indication_count: 10
---

# Aminobenzoic Acid
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

# Aminobenzoic Acid：從硬皮症等纖維化疾病到遺傳性血管性水腫（C1 抑制劑缺乏）

## 一句話總結

Aminobenzoic acid（對胺基苯甲酸，PABA）原本用於天疱瘡、Peyronie 病、硬皮症、全身性硬化症與皮肌炎等纖維化或結締組織相關疾病。
TxGNN 模型預測它可能對**遺傳性血管性水腫（C1 抑制劑缺乏型）**有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。
在所有預測中，機轉上最合理的是「局限性全身性硬化症」，但它其實屬於原適應症的延伸，而非真正的新用途。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 天疱瘡、Peyronie 病、陰莖纖維瘤病、閉塞性乾燥性龜頭炎、硬皮症、局限性硬皮症、全身性硬化症、皮肌炎（來自知識圖譜，香港許可證未載明適應症文字） |
| 預測新適應症 | 遺傳性血管性水腫（C1 抑制劑缺乏型）(hereditary angioedema with C1Inh deficiency) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Aminobenzoic acid 在纖維化皮膚與結締組織疾病（如硬皮症、Peyronie 病）中曾以胺基苯甲酸鉀的形式使用，推測具抗纖維化作用，但其確切機轉尚未證實。

就首位預測而言，目前沒有已知的機轉連結能把 aminobenzoic acid 與 C1 抑制劑缺乏、補體或激肽釋放酶-緩激肽路徑聯繫起來。排名第 2、第 3 的 C1 抑制劑缺乏與 serpinopathy，很可能反映同一個圖譜網路鄰近性訊號，應視為模型的人為結果而非獨立證據。

若從機轉合理性來看，其他預測中較值得注意的有：
- **局限性全身性硬化症（分數 99.55%）**：與原適應症高度重疊，屬於既有適應症類別的延伸，是最連貫的候選。
- **Camurati-Engelmann 病（99.65%）**：涉及 TGF-β1 失調，與抗纖維化存在推測性關聯，但無直接證據。
- **Geleophysic dysplasia（99.54%）**：涉及細胞外基質與 TGF-β 訊號，同樣僅是推測。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

首位預測（遺傳性血管性水腫）目前無相關文獻。以下為資料中與其他預測相關的文獻，僅供參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17217320](https://pubmed.ncbi.nlm.nih.gov/17217320/) | 2006 | Review | Alternative Medicine Review | 回顧硬皮症的天然療法，包含對胺基苯甲酸（對應局限性全身性硬化症） |
| [2406809](https://pubmed.ncbi.nlm.nih.gov/2406809/) | 1990 | Review | Rheumatic Diseases Clinics of North America | 全身性硬化症治療概述，指出多種療法在對照試驗中未能證實療效（對應局限性全身性硬化症） |
| [14151992](https://pubmed.ncbi.nlm.nih.gov/14151992/) | 1964 | 前臨床/實驗 | Acta Unio Int Contra Cancrum | 針對 novocain、urethan 等衍生物的毒性與抗腫瘤活性的早期實驗研究，相關性低（對應癌肉瘤） |

以上文獻皆無法確認為對照試驗證據。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49362 | PANTOGAR CAP | 未載明 | 未載明 |

製造商為 HONGKONG WINHEALTH PHARMA GROUP CO. LIMITED，屬單一成分製劑，狀態有效。

## 安全性考量

- **知識圖譜標示的禁忌疾病**：腎臟疾病、輸尿管積膿（pyoureter）、厭食症（anorexia nervosa）。此資訊來自知識圖譜，並非仿單內容。
- **藥物交互作用**：共查得 27 筆，其中以下為主要項目：
  - **嚴重（Major）**：Sulfasalazine、Sulfamethizole、Sulfamethoxazole、Eplerenone
  - **中度（Moderate）**：多種非類固醇消炎藥（NSAIDs），如 Ibuprofen、Naproxen、Diclofenac、Ketorolac、Indomethacin、Meloxicam、Piroxicam 等

其餘警語與仿單禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測（遺傳性血管性水腫）僅有模型分數，沒有臨床試驗、文獻或可驗證的機轉支持，證據等級為 L5。
- 前幾名預測彼此高度相關，很可能來自同一個圖譜訊號。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，以驗證與 C1 抑制劑/補體/激肽路徑的關聯
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩查
- 若要優先投入資源，建議改以「局限性全身性硬化症」作為研究問題，先系統性檢索 PABA（胺基苯甲酸鉀）在硬皮症的對照試驗證據
- 針對腎功能不全族群與 NSAIDs、磺胺類藥物併用的風險，制定安全性評估計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

