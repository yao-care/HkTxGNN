---
layout: default
title: Tyrosine
parent: 僅模型預測 (L5)
nav_order: 916
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tyrosine：預測新適應症為馬尾症候群 (Cauda Equina Syndrome)（證據等級 L5）。原適應症：目前許可證資料中未載明核准適應症"
monitor_inn: "Tyrosine"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "angle-closure glaucoma", "hyperthyroidism", "postural orthostatic tachycardia syndrome", "hyperthyroxinemia", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "traumatic glaucoma", "aqueous misdirection", "neovascular glaucoma"]
---

# Tyrosine
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

# Tyrosine：從營養支持用途到 Cauda Equina Syndrome（馬尾症候群）

## 一句話總結

Tyrosine（酪胺酸）是一種胺基酸，在香港主要以靜脈營養輸液與胺基酸製劑的成分上市。
TxGNN 模型預測它可能對**馬尾症候群 (Cauda Equina Syndrome)** 有效（預測分數最高），但此預測**沒有任何臨床試驗或文獻支持**。
在所有預測適應症中，證據最多的是**甲狀腺功能亢進 (Hyperthyroidism)**（1 個臨床試驗、約 20 篇文獻），但其中多為一般性疾病回顧，且機轉上並不支持以酪胺酸治療。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前許可證資料中未載明核准適應症 |
| 預測新適應症 | 馬尾症候群 (Cauda Equina Syndrome) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 16 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Tyrosine 是多種胺基酸輸液與營養製劑的成分，為兒茶酚胺（多巴胺、正腎上腺素）及甲狀腺素的前驅物。

就馬尾症候群而言，現有資料中找不到任何機轉連結。馬尾症候群是腰薦神經根受壓迫造成的損傷，酪胺酸與此並無已知關聯。高分數僅是計算模型的預測結果，沒有試驗與文獻佐證。

其他預測適應症的情況類似：
- **甲狀腺功能亢進、高甲狀腺素血症**：酪胺酸是甲狀腺素的結構骨架，但增加前驅物原則上無法治療甲亢，甚至可能適得其反。
- **姿勢性心搏過速症候群**：酪胺酸是多巴胺與正腎上腺素的前驅物，理論上與自主神經功能有關，但唯一文獻是使用酪胺酸羥化酶*抑制劑*的病例報告，作用方向相反。
- **青光眼相關疾病**（隅角閉鎖性、新生血管性、外傷性）：文獻為描述性或觀察性研究，未測試酪胺酸作為治療。
- **甲狀腺素阻抗症**：屬受體層級缺陷，前驅物胺基酸不太可能矯正。
- **神經性膀胱**：該疾病術語在本體論中已標記為過時，預測可能對應到已廢棄的概念。

## 臨床試驗證據

以下為證據最多的預測適應症（甲狀腺功能亢進）之試驗；首位預測（馬尾症候群）目前無相關臨床試驗登記。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06264544](https://clinicaltrials.gov/study/NCT06264544) | Phase NA | 尚未招募 | 150 | 以鋅、硒及 L-酪胺酸複合補充劑，預防帶有 SEPP1 基因多型性且 TPOAb 升高者發生甲狀腺毒症；酪胺酸的單獨貢獻無法區分，尚無結果 |

## 文獻證據

首位預測（馬尾症候群）目前無相關文獻。以下列出其他預測適應症中較相關的文獻（多為回顧，無直接評估酪胺酸治療者）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36848916](https://pubmed.ncbi.nlm.nih.gov/36848916/) | 2023 | Review | Lancet Diabetes Endocrinol | 甲狀腺功能亢進的病因、診斷、治療與預後總覽 |
| [38044176](https://pubmed.ncbi.nlm.nih.gov/38044176/) | 2024 | Review | Semin Nucl Med | 自體免疫甲狀腺疾病回顧 |
| [34913664](https://pubmed.ncbi.nlm.nih.gov/34913664/) | 2021 | Review | Am Fam Physician | 甲狀腺炎的評估與治療 |
| [40142311](https://pubmed.ncbi.nlm.nih.gov/40142311/) | 2025 | Review | Medicina (Kaunas) | Graves' 病的標靶治療敘述性回顧 |
| [30886364](https://pubmed.ncbi.nlm.nih.gov/30886364/) | 2019 | Review | Nat Rev Endocrinol | 甲狀腺球蛋白中酪胺酸殘基碘化與甲狀腺素合成 |
| [42812246](https://pubmed.ncbi.nlm.nih.gov/42812246/) | 2026 | Cohort | Front Med | 早期原發性隅角閉鎖性青光眼的血漿胺基酸代謝改變與眼部參數相關（生物標記關聯，非治療證據） |
| [27758063](https://pubmed.ncbi.nlm.nih.gov/27758063/) | 2017 | Cohort | Clin Exp Ophthalmol | 急性隅角閉鎖性青光眼發作後血清自體抗體變化 |
| [35087972](https://pubmed.ncbi.nlm.nih.gov/35087972/) | 2021 | Review | Rom J Ophthalmol | 新生血管性青光眼的病因與治療 |
| [39063020](https://pubmed.ncbi.nlm.nih.gov/39063020/) | 2024 | Case report | Int J Mol Sci | 一例慢性疲勞症候群患者對酪胺酸羥化酶抑制劑 AMPT 有反應（與酪胺酸補充作用相反） |
| [19169471](https://pubmed.ncbi.nlm.nih.gov/19169471/) | 2008 | Case report | Arq Bras Endocrinol Metabol | 甲狀腺素受體 β E449X 突變合併自體免疫甲狀腺疾病 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-32089 | KETOSTERIL TAB | — | 未載明 |
| HK-36470 | VAMINOLACT I.V. SOLUTION | — | 未載明 |
| HK-64293 | SMOFKABIVEN ELECTROLYTE FREE EMULSION FOR INFUSION 493ML | — | 未載明 |
| HK-61211 | AMINOPLASMAL B. BRAUN 10% E SOLUTION FOR INFUSION | — | 未載明 |
| HK-67504 | OLIMEL N12E EMULSION FOR INFUSION | — | 未載明 |

以上為 16 張有效單一成分許可證中的 5 張，其餘包括 SMOFKABIVEN、OLIMEL、PERIOLIMEL、NUMETA 及 BFLUID 等系列產品。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症均為 L4–L5，首位預測（馬尾症候群）完全沒有試驗與文獻，機轉上也找不到連結。
- 唯一的臨床試驗（NCT06264544）是多成分補充劑，無法判斷酪胺酸的貢獻；多數預測在機轉上甚至方向相反或不合理。

**若要推進需要：**
- 取得完整的作用機轉資料（MOA）
- 取得香港衛生署仿單的警語與禁忌症資料
- 釐清各預測適應症與酪胺酸的具體機轉假說，優先針對有生物學連結者（如自主神經相關疾病）
- 若要評估甲狀腺相關用途，需有能單獨測試酪胺酸效果的對照試驗設計
- 確認「神經性膀胱」預測是否對應到已廢棄的疾病概念
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

