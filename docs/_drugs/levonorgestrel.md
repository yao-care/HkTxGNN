---
layout: default
title: Levonorgestrel
parent: 中證據等級 (L3-L4)
nav_order: 453
evidence_level: L3
indication_count: 5
---

# Levonorgestrel
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Levonorgestrel：從避孕到痤瘡

## 一句話總結

Levonorgestrel 是廣泛使用的黃體素類避孕成分，涵蓋口服避孕藥、子宮內投藥系統（IUS）與皮下植入劑等劑型。
TxGNN 模型預測它可能對**痤瘡 (Acne)** 有效，
目前有 **5 個臨床試驗**和 **20 篇文獻**支持這個方向，但機轉上存在內部矛盾（見下文）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 避孕（口服避孕藥、子宮內投藥系統、皮下植入劑；依文獻佐證，香港許可證資料缺失） |
| 預測新適應症 | 痤瘡 (Acne) |
| TxGNN 預測分數 | 99.88% |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 Levonorgestrel 的詳細作用機轉資料（DrugBank MOA 欄位為空）。根據文獻佐證，Levonorgestrel 是複方口服避孕藥、子宮內投藥系統與皮下植入劑的黃體素成分，其避孕效果已在臨床上廣泛確立。

機轉上，複方口服避孕藥（雌激素+黃體素）透過抑制下視丘-腦垂體-卵巢軸、降低游離睪固酮並升高 SHBG（性荷爾蒙結合球蛋白），是治療荷爾蒙性痤瘡的已知路徑，這類效果通常見於含**低雄性化黃體素**（如 drospirenone、cyproterone acetate、chlormadinone acetate）的複方製劑。

然而，Levonorgestrel 本身是**雄性化程度較高**的第二代黃體素（PMID 7825629），其單獨作用理論上可能抵銷甚至惡化痤瘡，需與同複方中雌激素成分的淨效應合併評估。文獻中也有直接比較顯示，含 chlormadinone acetate 的複方在治療痤瘡上顯著優於含 Levonorgestrel 的複方（PMID 15025547）。因此這個預測方向存在機轉上的內部矛盾，不宜視為單純正向關聯。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00480532](https://clinicaltrials.gov/study/NCT00480532) | N/A | 完成 | 131 | 連續口服避孕藥合併 doxycycline 之研究，與痤瘡間接相關，惟為複方介入且未標示是否含 LNG 成分（相關性：中） |
| [NCT01650168](https://clinicaltrials.gov/study/NCT01650168) | N/A | 完成 | 101,498 | 含 nomegestrel acetate 之單相口服避孕藥安全性世代研究，對照組含 LNG 複方，非痤瘡治療試驗（相關性：低） |
| [NCT00161226](https://clinicaltrials.gov/study/NCT00161226) | N/A | 終止 | 44 | LNG 子宮內投藥系統用於子宮內膜癌預防研究，非痤瘡適應症，疑似知識圖譜配對錯誤（相關性：低） |
| [NCT05570786](https://clinicaltrials.gov/study/NCT05570786) | Phase 2 | 完成 | 100 | Gestrinone（非 LNG）皮下植入劑用於子宮內膜異位症骨盆疼痛，藥物成分與適應症皆不符（相關性：低） |
| [NCT05492487](https://clinicaltrials.gov/study/NCT05492487) | Phase 2 | 未知 | 60 | Mirena（LNG-IUS）用於非典型子宮內膜增生生育保留治療，與痤瘡無關（相關性：低） |

**注意：** 上述試驗多數並非直接針對「Levonorgestrel 治療痤瘡」設計，部分為知識圖譜間接配對，證據強度有限。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12196750](https://pubmed.ncbi.nlm.nih.gov/12196750/) | 2002 | RCT | J Am Acad Dermatol | 低劑量 EE/LNG（20μg/100μg）複方避孕藥治療中度痤瘡之隨機安慰劑對照試驗 |
| [15025547](https://pubmed.ncbi.nlm.nih.gov/15025547/) | 2004 | 比較研究 | Drugs | EE/Chlormadinone acetate 治療輕中度痤瘡效果顯著優於 EE/Levonorgestrel |
| [6084924](https://pubmed.ncbi.nlm.nih.gov/6084924/) | 1984 | 臨床研究 | Acta Derm Venereol | 比較兩種含黃體素（含 LNG）口服避孕藥對痤瘡患者睪固酮與 SHBG 之影響 |
| [21895044](https://pubmed.ncbi.nlm.nih.gov/21895044/) | 2011 | Review | Am J Clin Dermatol | 探討高雄性素狀態與痤瘡、多毛症等皮膚病灶之關聯及低雄性化黃體素之皮膚科效益 |
| [16796485](https://pubmed.ncbi.nlm.nih.gov/16796485/) | 2006 | Review | J Womens Health | 比較 drospirenone 與 medroxyprogesterone acetate、Levonorgestrel 對痤瘡及脂質參數之影響 |
| [7825629](https://pubmed.ncbi.nlm.nih.gov/7825629/) | 1995 | Review | Am J Med | 黃體素雄性化作用之機轉綜論，說明 Levonorgestrel 屬雄性化程度較高之黃體素 |
| [11727177](https://pubmed.ncbi.nlm.nih.gov/11727177/) | 2001 | Review | Semin Reprod Med | Levonorgestrel 子宮內投藥系統之避孕機轉與臨床特性綜論（背景資料） |

---

## 香港上市資訊

此藥物目前**未在香港上市**，無許可證資料可提供。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
機轉證據存在內部矛盾——Levonorgestrel 屬雄性化程度較高的黃體素，文獻直接比較顯示其治療痤瘡效果劣於低雄性化黃體素複方（如 chlormadinone acetate），且該藥物目前未於香港上市，難以支持積極推進。

**若要推進需要：**
- Levonorgestrel 的完整作用機轉（MOA）資料，釐清其雄性化效應對痤瘡淨效果的實際影響
- 針對「LNG 單方或複方 vs. 低雄性化黃體素複方」治療痤瘡的頭對頭比較研究
- 香港上市狀態與仿單警語/禁忌資料（現為 Blocking 等級資料缺口，需先補齊才能進入安全性初評 S1）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

