---
layout: default
title: Ipilimumab
parent: 高證據等級 (L1-L2)
nav_order: 410
evidence_level: L2
indication_count: 2
---

# Ipilimumab
{: .fs-9 }

證據等級: **L2** | 預測適應症: **2** 個
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

# Ipilimumab：從皮膚型黑色素瘤到非皮膚型黑色素瘤

## 一句話總結

Ipilimumab（DrugBank DB06186）是抗 CTLA-4 單株抗體，其療效已在皮膚型黑色素瘤的 Phase 3 樞紐試驗中確立。
TxGNN 模型預測它對**非皮膚型黑色素瘤（葡萄膜/黏膜/Merkel cell 等亞型）**可能同樣有效，
目前有多個臨床試驗（含針對葡萄膜黑色素瘤的直接試驗）與 **5 篇文獻**支持此方向，證據等級達 L2。
另有一個低置信度候選信號（choroideremia，遺傳性視網膜退化疾病）經檢視判定機轉上不相關，已建議 Hold。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 皮膚型黑色素瘤（cutaneous melanoma，Phase 3 樞紐試驗 MDX010-20 確立） |
| 預測新適應症 | 非皮膚型黑色素瘤 (Non-cutaneous Melanoma) |
| TxGNN 預測分數 | 99.02% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Ipilimumab 是抗 CTLA-4（cytotoxic T-lymphocyte-associated antigen 4）單株抗體，透過解除 CTLA-4 對 T 細胞的抑制訊號，恢復並強化抗腫瘤免疫反應。此機轉在皮膚型黑色素瘤已由 Phase 3 樞紐試驗（NCT00324155，n=681）確立療效與安全性，是全球核准 ipilimumab 治療黑色素瘤的關鍵證據。

非皮膚型黑色素瘤（葡萄膜/黏膜/肢端型等）與皮膚型同屬黑色素細胞來源腫瘤，理論上共享 CTLA-4 免疫檢查點機轉，因此免疫檢查點阻斷在機轉上具有合理延伸性。已有針對葡萄膜黑色素瘤（NCT01730157）及 Merkel cell carcinoma（NCT01913691）等非皮膚型亞群的臨床試驗與文獻直接評估 ipilimumab 療效。

但非皮膚型黑色素瘤的腫瘤突變負荷（TMB）普遍低於皮膚型，且腫瘤微環境不同，臨床反應率歷史上不如皮膚型，因此屬於機轉合理但非直接外推的中等強度證據，需審慎評估亞群反應差異。

目前缺乏 ipilimumab 完整的作用機轉技術資料（DG002，DrugBank MOA 待查），此結論主要根據試驗與文獻中呈現的機轉描述整理。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00324155](https://clinicaltrials.gov/study/NCT00324155) | Phase 3 | 完成 | 681 | Ipilimumab+Dacarbazine vs Dacarbazine+Placebo，確立晚期黑色素瘤療效與安全性之樞紐試驗 |
| [NCT01730157](https://clinicaltrials.gov/study/NCT01730157) | Early Phase 1 | 已終止 | 6 | 肝動脈栓塞合併全身性 Ipilimumab 治療葡萄膜黑色素瘤肝轉移（直接非皮膚型亞型） |
| [NCT01913691](https://clinicaltrials.gov/study/NCT01913691) | Phase 2 | 已撤回 | 0 | Ipilimumab 治療轉移性 Merkel cell carcinoma（非皮膚型/神經內分泌來源） |
| [NCT03068455](https://clinicaltrials.gov/study/NCT03068455) | Phase 3 | 完成 | 1844 | Nivolumab+Ipilimumab 輔助治療 vs Nivolumab 單用，術後 Stage IIIb-IV 黑色素瘤 |
| [NCT02506153](https://clinicaltrials.gov/study/NCT02506153) | Phase 3 | 進行中（未招募） | 1301 | 高風險術後黑色素瘤：Pembrolizumab vs 高劑量干擾素或 Ipilimumab |
| [NCT01783938](https://clinicaltrials.gov/study/NCT01783938) | Phase 2 | 完成 | 138 | Nivolumab 序貫合併 Ipilimumab 治療晚期/轉移性黑色素瘤 |
| [NCT02339571](https://clinicaltrials.gov/study/NCT02339571) | Phase 2/3 | 進行中 | 600 | Nivolumab+Ipilimumab±Sargramostim 治療不可切除 Stage III-IV 黑色素瘤 |
| [NCT02320058](https://clinicaltrials.gov/study/NCT02320058) | Phase 2 | 完成 | 119 | Nivolumab+Ipilimumab 治療腦轉移黑色素瘤 |
| [NCT01950390](https://clinicaltrials.gov/study/NCT01950390) | Phase 2 | 完成 | 169 | Ipilimumab±Bevacizumab 治療不可切除 Stage III-IV 黑色素瘤 |
| [NCT02905266](https://clinicaltrials.gov/study/NCT02905266) | Phase 3 | 完成 | 106 | Nivolumab+Ipilimumab 不同給藥方案安全性與療效評估 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24999899](https://pubmed.ncbi.nlm.nih.gov/24999899/) | 2014 | Cohort/Expanded-access | The Medical Journal of Australia | 評估 ipilimumab 於澳洲臨床實務中對皮膚型、葡萄膜及黏膜黑色素瘤之療效與耐受性差異 |
| [28183255](https://pubmed.ncbi.nlm.nih.gov/28183255/) | 2018 | Review | Current Cancer Drug Targets | 黑色素瘤輔助治療現況回顧，涵蓋非皮膚型（僅占約 5%）之治療選項 |
| [29466692](https://pubmed.ncbi.nlm.nih.gov/29466692/) | 2018 | Review | Discovery Medicine | Anti-PD-1 單獨或合併 ipilimumab 治療晚期黑色素瘤之臨床更新 |
| [37887546](https://pubmed.ncbi.nlm.nih.gov/37887546/) | 2023 | Review/Meta-analysis | Current Oncology | 比較不同年齡層患者接受 anti-PD-1 單療法或合併 ipilimumab 之療效差異 |
| [40236344](https://pubmed.ncbi.nlm.nih.gov/40236344/) | 2025 | Case Report | Cureus | 黑色素瘤橫結腸轉移個案報告，涉及免疫治療相關腸道副作用 |

## 細胞毒性

Ipilimumab 屬抗腫瘤藥物（原適應症黑色素瘤），但機轉為免疫檢查點阻斷而非傳統細胞毒性化療。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 免疫治療（Anti-CTLA-4 免疫檢查點抑制劑） |
| 骨髓抑制風險 / 致吐性分級 / 監測項目 / 處置防護 | 缺乏具體毒性資料，請參考原廠仿單的警語與注意事項（免疫檢查點抑制劑之特徵性風險為免疫相關不良事件 irAEs，如腸炎、肝炎、內分泌失調，非典型骨髓抑制，實際監測計畫仍應以仿單為準） |

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他預測候選（已篩除）

TxGNN 同時預測 ipilimumab 對 **choroideremia**（脈絡膜視網膜退化症，CHM 基因突變所致）分數達 99.06%，但：
- 無任何臨床試驗或文獻支持
- Choroideremia 病理機轉（Rab escort protein-1 缺陷）與 CTLA-4 免疫調節機轉無已知關聯
- 判定為知識圖譜關聯路徑推論之統計假影，非機轉合理性所致

**評等：L5 / S0 / Hold** — 不建議推進，僅供記錄。

## 結論與下一步

**決策：Proceed with Guardrails**（針對非皮膚型黑色素瘤）

**理由：**
- 抗 CTLA-4 機轉在皮膚型黑色素瘤已有 Phase 3 樞紐證據，且已有直接針對葡萄膜黑色素瘤、Merkel cell carcinoma 等非皮膚型亞型的臨床試驗與文獻，證據等級達 L2
- 但非皮膚型黑色素瘤 TMB 較低、腫瘤微環境不同，歷史反應率不如皮膚型，需以亞群分析與 guardrails 方式推進，不宜直接外推

**若要推進需要：**
- 補齊 TFDA/香港仿單警語與禁忌症資料（DG001，Blocking）
- 補齊 DrugBank MOA 完整技術資料（DG002）
- 針對非皮膚型黑色素瘤亞群（葡萄膜/黏膜/肢端型）之反應率與安全性做次族群分析
- Choroideremia 候選信號建議直接標記為低優先級，不投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

