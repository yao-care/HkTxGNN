---
layout: default
title: Prednisolone Acetate
parent: 僅模型預測 (L5)
nav_order: 727
evidence_level: L5
indication_count: 10
monitor_inn: "PREDNISOLONE ACETATE"
predicted_indications: ["conjunctival folliculosis", "parasitic conjunctivitis", "chronic follicular conjunctivitis", "serous conjunctivitis except viral", "papillary conjunctivitis", "Angelucci syndrome", "pseudomembranous conjunctivitis", "acute hemorrhagic conjunctivitis", "vernal conjunctivitis", "postinfectious vasculitis"]
last_modified_at: 2026-10-28
description: "Prednisolone Acetate：預測新適應症為結膜濾泡增生症 (Conjunctival Folliculosis)（證據等級 L5）。原適應症：香港許可證未提供核准適應症文字"
---

# Prednisolone Acetate
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

## Prednisolone Acetate：從葡萄膜炎到結膜濾泡增生症
{: .text-alpha }

## 一句話總結

Prednisolone Acetate 是局部用皮質類固醇，知識圖譜中記錄的相關疾病包括葡萄膜炎、結膜炎、虹彩睫狀體炎等眼部發炎性疾病。
TxGNN 模型預測它可能對**結膜濾泡增生症 (Conjunctival Folliculosis)** 有效，但這項預測目前**沒有任何臨床試驗或文獻**直接支持。
在本次預測的 10 個候選適應症中，證據最完整的是**春季結膜炎**與**乳突狀結膜炎**，但現有證據仍屬間接。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未提供核准適應症文字；知識圖譜記錄的相關疾病包括葡萄膜炎、結膜炎、虹彩睫狀體炎等（僅為知識圖譜關聯，非核准適應症） |
| 預測新適應症 | 結膜濾泡增生症 (Conjunctival Folliculosis) |
| TxGNN 預測分數 | 0.9974 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Prednisolone Acetate 屬於皮質類固醇，局部使用時可抑制眼表發炎反應。TxGNN 模型（深度學習）的預測分數可能反映模型從相關疾病間學到的相似性，並非生物學證據；該模型預測其與多種葡萄膜炎及結膜炎相關疾病有關聯。

結膜濾泡增生症與已記錄的結膜炎屬於同一類眼表疾病，因此模型給出高分。不過這類病症常為良性或可自行緩解，且病因（感染性、毒性或過敏性）須先釐清。機轉上合理，但沒有藥物專屬的證據支持。

### 其他預測適應症概況

| 排名 | 預測疾病 | 分數 | 證據等級 | 說明 |
|------|---------|------|---------|------|
| 2 | 寄生蟲性結膜炎 | 0.9974 | L5 | 僅有預測；未配合抗寄生蟲治療時，類固醇可能使感染惡化 |
| 3 | 慢性濾泡性結膜炎 | 0.9974 | L5 | 僅有預測；須先確認病因 |
| 4 | 非病毒性漿液性結膜炎 | 0.9974 | L5 | 僅有預測；分類不具特異性 |
| 5 | 乳突狀結膜炎 | 0.9972 | L5 | 僅有同類藥物 loteprednol 的間接資料，無直接研究 |
| 6 | Angelucci 症候群 | 0.9972 | L5 | 僅有預測 |
| 7 | 偽膜性結膜炎 | 0.9971 | L5 | 僅有個案層級文獻，未檢驗本藥 |
| 8 | 急性出血性結膜炎 | 0.9970 | L5 | 為自限性病毒感染；活動性病毒感染使用類固醇有風險 |
| 9 | 春季結膜炎 | 0.9958 | L5 | 有一項實驗性過敏性結膜炎模型比較研究，但非直接針對該疾病 |
| 10 | 感染後血管炎 | 0.9944 | L5 | 局部眼用給藥的全身暴露有限，相關性存疑 |

> 註：乳突狀結膜炎、偽膜性結膜炎與春季結膜炎的現有資料多為相關疾病、同類藥物（loteprednol）、其他藥物（cyclosporine）或個案報告，並無直接以 Prednisolone Acetate 研究該疾病者，故依規則一律評為 L5。

## 臨床試驗證據

針對首位預測（結膜濾泡增生症）：目前無相關臨床試驗登記。

下列為其他預測適應症的間接試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 對應疾病 | 主要發現 |
|---------|------|------|------|---------|---------|
| [NCT01437982](https://clinicaltrials.gov/study/NCT01437982) | Phase 4 | 完成 | 140 | 乳突狀結膜炎 | Lotemax（loteprednol etabonate，非本藥）的上市後安全性監測 |
| [NCT04705584](https://clinicaltrials.gov/study/NCT04705584) | 不適用 | 狀態未知 | 180 | 春季結膜炎 | 比較 cyclosporine 2% 與 tacrolimus 0.3% 作為類固醇替代方案，未確認有本藥組別 |

## 文獻證據

針對首位預測（結膜濾泡增生症）：目前無相關文獻。

下列為其他預測適應症中較相關的文獻（均非直接研究本藥於該疾病）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [24055903](https://pubmed.ncbi.nlm.nih.gov/24055903/) | 2013 | 臨床研究 | Cornea | 在實驗性過敏性結膜炎模型中，比較 cyclosporine A、epinastine 與 prednisolone acetate 1% 對過敏性發炎的作用 |
| [9713785](https://pubmed.ncbi.nlm.nih.gov/9713785/) | 1998 | 臨床研究 | Journal of Glaucoma | Loteprednol 長期使用期間的眼壓變化 |
| [26984315](https://pubmed.ncbi.nlm.nih.gov/26984315/) | 2016 | Review | Advances in Therapy | 局部眼用類固醇（loteprednol）對眼壓的影響，點出類別安全性議題 |
| [18020605](https://pubmed.ncbi.nlm.nih.gov/18020605/) | 1998 | Review | BioDrugs | Loteprednol 於眼部發炎處置的臨床潛力 |
| [32621983](https://pubmed.ncbi.nlm.nih.gov/32621983/) | 2020 | 個案報告 | J AAPOS | 黴漿菌相關皮疹與黏膜炎的眼部表現，治療包含局部 prednisolone acetate |
| [21434554](https://pubmed.ncbi.nlm.nih.gov/21434554/) | 2011 | 個案報告 | Indian J Tuberc | 原發性結膜結核被誤診為過敏性結膜炎，使用 1% prednisolone acetate 後無改善 |
| [12931748](https://pubmed.ncbi.nlm.nih.gov/12931748/) | 2003 | 世代研究 | Asian Pac J Allergy Immunol | 泰國春季角結膜炎的臨床特徵與治療結果，嚴重病例使用局部類固醇 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-19548 | 1% PRED FORTE 無菌眼用懸液 | 未提供 | 未提供 |
| HK-24139 | ECONOPRED PLUS 眼用懸液 1% | 未提供 | 未提供 |
| HK-67491 | MITEX 犬貓用耳滴劑及皮膚用懸液（獸醫用） | 未提供 | 未提供 |
| HK-67882 | SUROLAN 耳滴劑及皮膚用懸液（獸醫用） | 未提供 | 未提供 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜，非仿單內容）：單純疱疹病毒角膜炎、開角型青光眼、高眼壓、眼部感染性疾病（含黴菌性、病毒性眼部感染與眼結核）、糖尿病及糖尿病酮酸中毒、紫質症等。
- **與預測適應症相關的風險**：局部類固醇可能造成眼壓升高，尤其在慢性或兒童族群（如春季結膜炎）需留意。寄生蟲性及病毒性結膜炎使用類固醇可能使感染惡化。

其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測（結膜濾泡增生症）沒有任何臨床試驗或文獻，僅有模型分數，證據等級為 L5。
- 其餘候選疾病也沒有直接以 Prednisolone Acetate 研究該疾病的證據，且部分疾病（寄生蟲性、病毒性）使用類固醇有安全疑慮。

**若要推進需要：**
- 取得香港仿單的核准適應症、警語與禁忌資料
- 補充 Prednisolone Acetate 的作用機轉資料
- 優先針對春季結膜炎、乳突狀結膜炎等免疫性發炎型疾病，檢索直接以本藥為對象的研究
- 釐清結膜濾泡增生症的病因分型，再評估是否有使用類固醇的必要
- 制定眼壓監測與感染排除的安全計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

