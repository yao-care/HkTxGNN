---
layout: default
title: Ruxolitinib
parent: 僅模型預測 (L5)
nav_order: 668
evidence_level: L5
indication_count: 5
---

# Ruxolitinib
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

# Ruxolitinib：JAK 抑制劑跨腫瘤適應症的多重假說評估

## 一句話總結

Ruxolitinib（DB08877）為 JAK1/JAK2 抑制劑，惟本次 Evidence Pack 未提供其原始核准適應症與完整 MOA 資料。
TxGNN 模型針對此藥物提出 **5 個候選新適應症**，主要集中於 PEComa 家族腫瘤（TSC-mTOR 驅動）與**黏液樣脂肪肉瘤 (Liposarcoma)**；
除黏液樣脂肪肉瘤外，其餘候選僅有模型預測分數支持，**無任何臨床試驗或文獻佐證**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（Evidence Pack 未提供） |
| 預測新適應症（TxGNN 首位） | Uterine Corpus Perivascular Epithelioid Cell Tumor (PEComa) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

> **資料缺口提示**：DG001（TFDA/仿單警語缺失，*Blocking*）已阻斷 S1 安全性初評；DG002（MOA 資料缺失，*High*）影響下方機轉關聯性判斷的可信度。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為 Data Gap，DG002）。根據 `predicted_indications` 中各候選的 `mechanistic_link` 敘述可反推，Ruxolitinib 應為 **JAK1/JAK2 抑制劑**，此推論僅來自預測結果的機轉假說欄位，並非官方 MOA 資料，仍需以 DrugBank API 查證補齊。

排名前 4 的候選（uterine PEComa、benign PEComa、lymphangiomyoma、lymphangioleiomyomatosis）皆屬 **PEComa/LAM 家族**，其標準驅動機轉為 **TSC1/TSC2 失能 → mTORC1 過度活化**（現行標準療法為 mTOR 抑制劑 Sirolimus/Everolimus），與 Ruxolitinib 標靶的 JAK-STAT 通路**無直接機轉證據連結**。TxGNN 給出的高分很可能只反映知識圖譜中這些疾病彼此鄰近（同家族聚類），而非藥物-疾病機轉上的真實關聯。

相對地，排名第 5 的**黏液樣脂肪肉瘤 (myxoid liposarcoma)** 具有較明確的機轉基礎：其特徵性 **FUS-DDIT3 融合致癌蛋白**已被兩篇臨床前研究證實會活化 **JAK-STAT 訊號（含 STAT3 磷酸化上升）**，並與腫瘤幹細胞特性及化療抗藥性相關，為 Ruxolitinib 介入提供了目前唯一有機轉文獻支持的候選方向。

---

## 各候選適應症比較

| 排名 | 預測疾病 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|---------|-----------|---------|---------|------|
| 1 | Uterine Corpus PEComa | 99.73% | L5 | S0 | Hold |
| 2 | Benign PEComa | 99.73% | L5 | S0 | Hold |
| 3 | Lymphangiomyoma | 99.72% | L5 | S0 | Hold |
| 4 | Lymphangioleiomyomatosis (LAM) | 99.64% | L5 | S0 | Hold |
| **5** | **Liposarcoma（黏液樣型）** | 99.52% | **L4** | **S1** | **Research Question** |

排名與分數呈負相關（分數越低反而證據等級越高），提示 TxGNN 分數本身在此案例中**不足以代表可信度**，須以機轉/文獻證據交叉驗證。

---

## 臨床試驗證據

目前無相關臨床試驗登記（5 個候選皆無 `clinical_trials` 或 `ictrp_trials` 紀錄）。

---

## 文獻證據

僅 **Liposarcoma** 候選有文獻支持，其餘 4 個候選目前無相關文獻。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35186752](https://pubmed.ncbi.nlm.nih.gov/35186752/) | 2022 | Preclinical/Mechanistic | Frontiers in Oncology | FUS-DDIT3 融合致癌蛋白提升 STAT3 表現與磷酸化，顯示其與 JAK-STAT 訊號的關聯 |
| [30650179](https://pubmed.ncbi.nlm.nih.gov/30650179/) | 2019 | Preclinical/Mechanistic | International Journal of Cancer | JAK-STAT 訊號調控黏液樣脂肪肉瘤腫瘤幹細胞特性，包括化療抗藥性 |

---

## 香港上市資訊

Ruxolitinib 目前於香港**未上市**，無任何許可證登記資料（`total_licenses = 0`）。

---

## 安全性考量

安全性資訊請參考原廠仿單。（`key_warnings`、`contraindications`、DDI 查詢結果均無資料，DG001 為 Blocking 缺口，需先取得 TFDA/HSA 官方仿單方能進行 S1 安全性初評。）

---

## 結論與下一步

**決策：Hold（PEComa 家族 4 項候選）／Research Question（Liposarcoma 候選）**

**理由：**
- 排名前 4 的 PEComa/LAM 家族候選僅有 TxGNN 分數支持，缺乏機轉關聯與任何試驗/文獻證據，且核心藥物資料（MOA、仿單警語）尚未補齊，暫不推進。
- Liposarcoma 候選具備臨床前機轉文獻支持（FUS-DDIT3 → JAK-STAT 活化），可列為值得進一步探索的研究假說，但仍未有臨床試驗驗證，不宜貿然推進至開發階段。

**若要推進需要：**
- 補齊 DG001（TFDA/仿單警語與禁忌，Blocking）——此為進入 S1 安全性初評的前提條件。
- 補齊 DG002（DrugBank MOA 查詢，High）——確認 Ruxolitinib 的正式作用機轉與適應症範圍。
- 針對 Liposarcoma 候選，建議規劃體外/體內驗證性研究，確認 Ruxolitinib 對 FUS-DDIT3 陽性黏液樣脂肪肉瘤細胞株的 JAK-STAT 抑制效果。
- 針對 PEComa 家族候選，建議重新檢視 TxGNN 圖譜鄰近性是否造成分數虛高，必要時降低其後續資源投入優先度。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

