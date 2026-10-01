---
layout: default
title: Bexarotene
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 3
---

# Bexarotene
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Bexarotene：從皮膚 T 細胞淋巴瘤到原發性皮膚 B 細胞淋巴瘤

## 一句話總結

Bexarotene 是 RXR 選擇性的 retinoid（rexinoid），原本用於皮膚 T 細胞淋巴瘤（CTCL）。
TxGNN 模型預測它可能對**原發性皮膚 B 細胞淋巴瘤 (Primary Cutaneous B-cell Lymphoma)** 有效，但目前**沒有任何直接測試 bexarotene 於 B 細胞疾病的研究**。
支持這個方向的只有 2 個間接相關的臨床試驗（1 個 Phase 1 T 細胞研究、1 個已撤回）和一批綜述與病例報告，這個預測較可能是知識圖譜的鄰近效應。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 皮膚 T 細胞淋巴瘤 (CTCL)（香港許可證未載明適應症，依藥物分類與文獻判斷） |
| 預測新適應症 | 原發性皮膚 B 細胞淋巴瘤 (Primary Cutaneous B-cell Lymphoma) |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L5（Evidence Pack 標示為 L4，但供應資料中沒有 B 細胞相關的機轉研究，故從嚴判定） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。已知 Bexarotene 是 RXR 選擇性 retinoid，能誘導惡性 T 細胞凋亡並使細胞週期停滯，這是它取得 CTCL 適應症的基礎。

「原發性皮膚淋巴瘤」同時涵蓋 T 細胞與 B 細胞亞型，兩者都以皮膚為主要侵犯器官。TxGNN 給出高分，很可能是因為 bexarotene 與 CTCL 在知識圖譜中共用這個「原發性皮膚淋巴瘤」上層節點。

現有資料不支持 B 細胞特異的機轉理由。在有直接證據之前，應把這個預測視為圖譜鄰近所產生的假象，而不是真正的新適應症訊號。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01134341](https://clinicaltrials.gov/study/NCT01134341) | Phase 1 | 完成 | 34 | Pralatrexate 合併口服 bexarotene 用於復發/難治性 CTCL 的劑量探索，評估劑量、安全性與早期療效。研究對象是 T 細胞淋巴瘤，未測試 B 細胞疾病 |
| [NCT05106192](https://clinicaltrials.gov/study/NCT05106192) | NA | 已撤回 | 0 | 以無針注射系統施打 triamcinolone 治療皮膚淋巴瘤斑塊（含 T 與 B 細胞型）。不涉及 bexarotene，也沒有產出資料 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31466585](https://pubmed.ncbi.nlm.nih.gov/31466585/) | 2019 | Review | Dermatologic Clinics | 皮膚 B 細胞淋巴瘤的診斷與處置。治療指引資料有限，各機構做法不一，以局部治療為主 |
| [34059248](https://pubmed.ncbi.nlm.nih.gov/34059248/) | 2021 | Review | Medical Clinics of North America | 皮膚淋巴瘤（含 CTCL 與 B 細胞型）的診斷與處置概述 |
| [19786826](https://pubmed.ncbi.nlm.nih.gov/19786826/) | 2009 | Review | Skin Pharmacology and Physiology | 皮膚淋巴瘤的新型與實驗性皮膚導向治療 |
| [14616487](https://pubmed.ncbi.nlm.nih.gov/14616487/) | 2003 | Review | Australasian Journal of Dermatology | 原發性皮膚淋巴瘤處置。傳統策略包括外用類固醇、光療、放療、retinoid 等 |
| [20806174](https://pubmed.ncbi.nlm.nih.gov/20806174/) | 2010 | Review | Therapeutische Umschau | 皮膚淋巴瘤的 WHO/EORTC 分類與概述 |
| [31932947](https://pubmed.ncbi.nlm.nih.gov/31932947/) | 2020 | Review | Der Pathologe | 皮膚淋巴瘤的臨床表現、診斷與治療。晚期 MF 與 Sézary 症候群的全身治療包括 bexarotene（T 細胞疾病） |
| [22031653](https://pubmed.ncbi.nlm.nih.gov/22031653/) | 2011 | Case report | Dermatology Online Journal | 局部復發的原發性皮膚邊緣區 B 細胞淋巴瘤病例 |
| [23941646](https://pubmed.ncbi.nlm.nih.gov/23941646/) | 2013 | Case report | Journal of Cutaneous Pathology | 皮膚濾泡輔助 T 細胞淋巴瘤的診斷陷阱。曾被誤診為 B 細胞淋巴瘤，rituximab 治療失敗 |
| [22508770](https://pubmed.ncbi.nlm.nih.gov/22508770/) | 2012 | Case report | Archives of Dermatology | 5 例皮膚濾泡輔助 T 細胞淋巴瘤病例系列（T 細胞亞型） |
| [29881891](https://pubmed.ncbi.nlm.nih.gov/29881891/) | 2018 | Case series | Der Hautarzt | 163 例原發性皮膚淋巴瘤的臨床病例系列 |

以上文獻均未直接評估 bexarotene 對 B 細胞淋巴瘤的療效。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68294 | TARGRETIN CAPSULES 75MG（廠商：MAIN LIFE CORP LTD） | 膠囊劑（依品名） | 未提供 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（RXR 選擇性 retinoid / rexinoid），非傳統細胞毒性化療 |
| 骨髓抑制風險 | 低至中（文獻提及口服劑型可見嗜中性白血球低下） |
| 致吐性分級 | 低 |
| 監測項目 | 血脂（三酸甘油酯、膽固醇）、甲狀腺功能（中樞性甲狀腺低下）、CBC 含分類、肝功能 |
| 處置防護 | 具致畸胎性，需嚴格避孕與排除懷孕；孕婦應避免接觸藥物 |

以上依藥物類別與文獻判斷，詳細內容請參考原廠仿單的警語與注意事項。

## 安全性考量

安全性資訊請參考原廠仿單。DrugBank 與香港仿單資料均缺，且查無藥物交互作用資料。

文獻中常提及的 bexarotene 相關風險有高三酸甘油酯血症、中樞性甲狀腺低下與致畸胎性。

## 結論與下一步

**決策：Hold**

**理由：**
- 現有證據沒有任何針對 B 細胞淋巴瘤的 bexarotene 研究，唯二的相關試驗一個是 T 細胞的 Phase 1，一個已撤回。
- 高預測分數很可能來自與 CTCL 共用的「原發性皮膚淋巴瘤」節點，而非 B 細胞特異的生物學。

**若要推進需要：**
- 找到 bexarotene 在 B 細胞淋巴瘤的前臨床或臨床證據（目前為零）。
- 補齊作用機轉資料（DrugBank），並說明 RXR 訊號在 B 細胞惡性腫瘤中的角色。
- 取得香港衛生署仿單的警語與禁忌症，才能進入安全性篩選。
- 若目標是實際可行的方向，同一份資料中的 **Sézary 症候群**（預測排名第 2，證據等級 L2）機轉直接，臨床上更接近既有 CTCL 適應症，值得優先評估。

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

