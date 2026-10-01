---
layout: default
title: Fluorouracil
parent: 僅模型預測 (L5)
nav_order: 384
evidence_level: L5
indication_count: 10
---

# Fluorouracil
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

# Fluorouracil：從（原適應症未載明）到橫紋肌肉瘤

## 一句話總結

Fluorouracil（5-FU）是抗代謝型細胞毒性化療藥物，香港已有 3 張許可證，但資料中未載明原適應症。
TxGNN 模型預測它可能對**橫紋肌肉瘤 (Rhabdomyosarcoma)** 相關疾病有效，但目前僅有**極少量、間接的文獻**，且**沒有直接相關的臨床試驗**，屬於以模型預測為主的假說。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未載明（香港許可證的核准適應症欄位皆為空白） |
| 預測新適應症 | 陰道葡萄狀胚胎型橫紋肌肉瘤 (botryoid-type embryonal rhabdomyosarcoma of the vagina) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

其他排名前列的預測還包括：橫紋肌肉瘤（一般）、腦膜旁胚胎型橫紋肌肉瘤、肝外膽管橫紋肌肉瘤、前列腺胚胎型橫紋肌肉瘤、肝肉瘤，以及數種鐮狀細胞疾病症候群。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Fluorouracil 是抗代謝藥物，會抑制胸苷酸合成酶（thymidylate synthase），並被納入 RNA 與 DNA 中，機轉上對快速分裂的腫瘤細胞有作用，因此對肉瘤細胞有理論上的合理性。

不過，Fluorouracil 並不是橫紋肌肉瘤標準治療方案中的常用藥物。多個預測的分數幾乎相同（例如三種鐮狀細胞症候群的分數完全一致），顯示模型分數可能來自知識圖譜中相鄰疾病節點的類別傳播，而非針對個別疾病的獨立訊號。

針對鐮狀細胞疾病，細胞毒性 S 期藥物在實驗上可提高胎兒血紅素，但已確立的選擇是 hydroxyurea；Fluorouracil 的骨髓抑制在非惡性慢性疾病中會是主要的安全性障礙。

---

## 臨床試驗證據

**排名第 1 的預測（陰道葡萄狀胚胎型橫紋肌肉瘤）：** 目前無相關臨床試驗登記。

以下為排名第 7 的「肝肉瘤」所檢索到的試驗，皆屬間接相關（相關性評級 C），並未在肉瘤中評估 Fluorouracil：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01228734](https://clinicaltrials.gov/study/NCT01228734) | Phase 3 | 完成 | 553 | Cetuximab 併用 FOLFOX-4 對比單用 FOLFOX-4，用於中國 RAS 野生型轉移性大腸直腸癌第一線治療 |
| [NCT01374425](https://clinicaltrials.gov/study/NCT01374425) | Phase 2 | 完成 | 376 | MAVERICC：Bevacizumab 併用 mFOLFOX6 或 FOLFIRI，用於轉移性大腸直腸癌 |
| [NCT03914170](https://clinicaltrials.gov/study/NCT03914170) | N/A | 完成 | 70 | FOLFIRINOX 併用 Cetuximab 的回溯性研究，用於 RAS 野生型轉移性大腸直腸癌 |
| [NCT04999761](https://clinicaltrials.gov/study/NCT04999761) | Phase 1 | 招募中 | 917 | AB122 為基礎治療的晚期實體瘤平台研究，無 Fluorouracil 特異訊號 |
| [NCT07059494](https://clinicaltrials.gov/study/NCT07059494) | Phase 4 | 招募中 | 40 | Atezolizumab + Bevacizumab 併用 Y-90 放射栓塞，用於肝細胞癌肝臟移植前治療 |

這些試驗都不是肉瘤試驗，不能視為對 Fluorouracil 用於橫紋肌肉瘤的支持。

---

## 文獻證據

以下為排名第 2 的「橫紋肌肉瘤」所檢索到的文獻，皆為 1973–1991 年的舊文獻：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Review | Cancer | 兒童肉瘤輔助化療的價值；橫紋肌肉瘤約佔軟組織肉瘤的 50%，但未確立 Fluorouracil 特異療效 |
| [6277228](https://pubmed.ncbi.nlm.nih.gov/6277228/) | 1981 | Review | Ann Acad Med Singapore | 晚期癌症化療可治癒性概述，提及橫紋肌肉瘤等兒童癌症 |
| [3951398](https://pubmed.ncbi.nlm.nih.gov/3951398/) | 1986 | Cohort | Med Pediatr Oncol | 兒童未分化鼻咽癌 22 例的 13 年治療經驗（非橫紋肌肉瘤） |
| [1908651](https://pubmed.ncbi.nlm.nih.gov/1908651/) | 1991 | Cohort | Gan To Kagaku Ryoho | 惡性軟組織腫瘤術前連續動脈內化療，38 例中僅 2 例為橫紋肌肉瘤 |
| [4129552](https://pubmed.ncbi.nlm.nih.gov/4129552/) | 1973 | Cohort | Arch Chir Neerl | 頭頸癌動脈內灌注化療的臨床與實驗研究 |

另外，肝肉瘤預測有 1 篇較相關的回溯性研究：[29346784](https://pubmed.ncbi.nlm.nih.gov/29346784/)（2019，Cohort，Digestive Surgery），為中國單一醫院成人原發性肝肉瘤的手術與化療經驗，但無法確認 Fluorouracil 特異療效。其餘多為動物或體外研究（如 Sarcoma 180 小鼠模型），屬前臨床證據。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-40254 | FLUOROURACIL INJ 50MG/ML VIAL-PHARMACHEM（TEVA） | 未載明 | 未載明 |
| HK-45512 | 5-FLUOROURACIL INJ 50MG/ML (EBEWE)（SANDOZ） | 未載明 | 未載明 |
| HK-15219 | VERRUMAL SOLUTION EXTERNAL（ZUELLIG PHARMA） | 外用溶液 | 未載明 |

其中 VERRUMAL 為外用劑型，注射劑與外用劑的用途與風險不同，若評估橫紋肌肉瘤，僅注射劑型具有相關性。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（Fluoropyrimidine 類抗代謝藥） |
| 骨髓抑制風險 | 中度（一般認知；資料中無 toxicity 細節，請以仿單為準） |
| 致吐性分級 | 低至中度 |
| 監測項目 | CBC（含分類）、肝腎功能、電解質 |
| 處置防護 | 注射劑需依細胞毒性藥物處置規範操作 |

詳細警語請參考原廠仿單。

---

## 安全性考量

安全性資訊請參考原廠仿單。

（目前香港衛生署仿單的警語與禁忌症資料尚未取得，藥物交互作用查詢也無結果。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（陰道葡萄狀胚胎型橫紋肌肉瘤）只有模型分數，無任何試驗或文獻。相關文獻老舊且多為間接證據，證據等級為 L5（最相關的一般橫紋肌肉瘤與肝肉瘤為 L4）。
- 香港仿單的安全性資料尚缺，屬阻斷性缺口，無法進入安全性篩檢。

**若要推進需要：**
- 下載並解析香港衛生署仿單，補齊警語、禁忌症與核准適應症（DG001，阻斷性）
- 從 DrugBank 補充作用機轉資料（DG002）
- 系統性檢索 Fluorouracil 用於橫紋肌肉瘤的臨床與文獻證據，並與現行標準治療方案比較
- 確認 PMID 29346784 中化療方案是否包含 Fluorouracil
- 鐮狀細胞相關預測建議不再優先追蹤（分數疑為類別傳播，且骨髓抑制風險與 hydroxyurea 已有的標準選項相比不利）

---

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

