---
layout: default
title: Prednisolone Acetate
parent: 僅模型預測 (L5)
nav_order: 727
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Prednisolone Acetate：預測新適應症為寄生蟲性結膜炎 (Parasitic Conjunctivitis)（證據等級 L5）。原適應症：葡萄膜炎、虹彩疾病、睫狀體疾病、全葡萄膜炎、結膜炎、虹彩睫狀體炎等"
monitor_inn: "PREDNISOLONE ACETATE"
predicted_indications: ["parasitic conjunctivitis", "serous conjunctivitis except viral", "chronic follicular conjunctivitis", "conjunctival folliculosis", "papillary conjunctivitis"]
---

# Prednisolone Acetate
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

# Prednisolone Acetate：從葡萄膜炎與結膜炎到寄生蟲性結膜炎

## 一句話總結

Prednisolone Acetate 是局部使用的皮質類固醇，原本用於葡萄膜炎、虹彩睫狀體炎、結膜炎等眼部發炎疾病。
TxGNN 模型預測它可能對**寄生蟲性結膜炎 (Parasitic Conjunctivitis)** 有效（預測分數 99.74%），
但目前**沒有直接支持的臨床試驗或文獻**，僅屬模型預測階段。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 葡萄膜炎、虹彩疾病、睫狀體疾病、全葡萄膜炎、結膜炎、虹彩睫狀體炎等（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 寄生蟲性結膜炎 (Parasitic Conjunctivitis) |
| TxGNN 預測分數 | 99.74% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Prednisolone Acetate 是局部皮質類固醇，具有抗發炎作用，已用於多種眼部發炎疾病，包括一般結膜炎。機轉上，抑制發炎反應對寄生蟲性結膜炎的發炎成分可能有幫助。

不過，類固醇無法處理寄生蟲感染的病因。若在沒有抗寄生蟲治療的情況下使用，反而可能使感染惡化。因此這個預測在臨床上只能視為「輔助控制發炎」的假說，不能單獨作為治療。

另外值得注意，排名前四的預測（寄生蟲性、非病毒性漿液性、慢性濾泡性結膜炎、結膜濾泡增生）與既有結膜炎適應症高度相近，較像是既有適應症類別的重新標示，而非真正的藥物再利用。結膜濾泡增生常屬良性、非發炎性表現，使用類固醇的理由較弱。

---

## 臨床試驗證據

針對首要預測（寄生蟲性結膜炎）：目前無相關臨床試驗登記。

作為參考，排名第 5 的預測「乳突性結膜炎 (Papillary Conjunctivitis)」有 1 項間接相關試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01437982](https://clinicaltrials.gov/study/NCT01Ｕ437982) | Phase 4 | 完成 | 140 | Lotemax（loteprednol etabonate）0.5% 眼用懸液的上市後安全性監測；使用的是另一種類固醇，僅能間接參考，且未確認有乳突性結膜炎專屬的評估指標 |

---

## 文獻證據

針對首要預測（寄生蟲性結膜炎）：目前無相關文獻。

作為參考，排名第 5 的預測「乳突性結膜炎」有以下文獻（多數針對 loteprednol etabonate 或其他疾病，並非 Prednisolone Acetate 本身）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26984315](https://pubmed.ncbi.nlm.nih.gov/26984315/) | 2016 | Review | Advances in Therapy | 局部眼用類固醇有升高眼壓的風險，loteprednol 的酯類結構可能降低此風險 |
| [18020605](https://pubmed.ncbi.nlm.nih.gov/18020605/) | 1998 | Review | BioDrugs | Loteprednol etabonate 為「軟藥」設計，局部抗發炎且降低全身副作用 |
| [9713785](https://pubmed.ncbi.nlm.nih.gov/9713785/) | 1998 | 臨床研究 | Journal of Glaucoma | 分析長期使用 loteprednol 的眼壓變化；先前雙盲研究顯示其對巨大乳突性結膜炎等有效 |
| [29260110](https://pubmed.ncbi.nlm.nih.gov/29260110/) | 2017 | Cohort | Am J Ophthalmol Case Rep | 藥物難治性巨大乳突性結膜炎的手術切除結果 |
| [12917176](https://pubmed.ncbi.nlm.nih.gov/12917176/) | 2003 | 臨床研究 | Ophthalmology | 局部 cyclosporine A 0.5% 用於上輪部角結膜炎的初步成效 |
| [18724159](https://pubmed.ncbi.nlm.nih.gov/18724159/) | 2008 | Case report | Cornea | 菊池病相關乳突性結膜炎個案 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-19548 | 1% PRED FORTE STERILE OPHTH SUSP（Allergan） | 眼用懸液 | 未載明 |
| HK-24139 | ECONOPRED PLUS OPHTHAL SUSP 1%（Novartis） | 眼用懸液 | 未載明 |
| HK-67491 | MITEX EAR DROPS AND CUTANEOUS SUSPENSION FOR DOGS AND CATS（獸用） | 耳滴劑／皮膚用懸液 | 未載明 |
| HK-67882 | SUROLAN EAR DROPS AND CUTANEOUS SUSPENSION（獸用） | 耳滴劑／皮膚用懸液 | 未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜，非仿單內容）：
  - 眼部：單純皰疹病毒角膜炎、開放角青光眼、高眼壓、眼部感染性疾病、黴菌性眼感染、病毒性眼感染、眼結核、角膜色素沉著
  - 全身：糖尿病、糖尿病酮酸中毒、紫質症（含遺傳性）、G6PD 缺乏症、肝醣儲積症、胱胺酸尿症、半乳糖血症

  其中「眼部感染性疾病」與本次預測的寄生蟲性結膜炎直接相關，需特別留意。
- **長期使用風險**：文獻指出局部類固醇可能升高眼壓，長期使用也有白內障等疑慮，慢性結膜炎尤其需要注意。

其餘警語、禁忌與藥物交互作用資訊，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.74%），但屬純模型預測（L5），沒有針對 Prednisolone Acetate 的直接試驗或文獻。類固醇無法治療寄生蟲病因，且知識圖譜將眼部感染列為禁忌，使用不當可能使感染惡化。
- 多數預測與既有結膜炎適應症重疊，新增的再利用價值有限。

**若要推進需要：**
- 確認香港仿單核准的適應症文字與警語、禁忌
- 補充 Prednisolone Acetate 的作用機轉資料
- 針對寄生蟲性結膜炎搜尋直接證據，並評估「抗寄生蟲藥物＋類固醇」併用的合理性
- 若轉向排名第 5 的乳突性結膜炎，需取得 Prednisolone Acetate 本身的對照研究，不宜僅以 loteprednol 的證據類推
- 制訂眼壓與感染惡化的監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

