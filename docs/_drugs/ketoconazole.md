---
layout: default
title: Ketoconazole
parent: 中證據等級 (L3-L4)
nav_order: 425
evidence_level: L3
indication_count: 1
---

# Ketoconazole
{: .fs-9 }

證據等級: **L3** | 預測適應症: **1** 個
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

# Ketoconazole：從黴菌感染到痤瘡

## 一句話總結

Ketoconazole 是一種 imidazole 類抗真菌藥物，原本用於治療黴菌感染。
TxGNN 模型預測它可能對**痤瘡 (Acne)** 有效，
目前有 **1 個臨床試驗**和 **15 篇文獻**支持這個方向，但整體證據仍偏初期。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 黴菌感染（抗真菌用途）－台灣無許可證登記資料 |
| 預測新適應症 | 痤瘡 (Acne) |
| TxGNN 預測分數 | 99.80% |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 正式的作用機轉 (MOA) 資料，但根據現有文獻可歸納出兩條可能路徑：

第一條路徑是抗真菌機轉：Ketoconazole 能抑制 *Malassezia furfur/ovale* 等皮膚常在菌的生長。臨床上常有 Pityrosporum（Malassezia）毛囊炎、新生兒 Malassezia 膿疱病被誤診為「尋常性痤瘡」，因此 ketoconazole 在這類易混淆的痤瘡樣皮疹上可能有直接效益。此外，體外研究顯示 ketoconazole 可抑制 *Propionibacterium acnes*（痤瘡主要致病菌）的脂肪酶活性與生長，提供另一條非抗真菌、直接抗菌的可能機轉。

第二條路徑是全身性抗雄激素/抗皮質醇機轉：Ketoconazole 全身性使用可抑制類固醇生成酵素（如 17,20-lyase、11β-hydroxylase），降低雄激素與皮質醇濃度，因此對 PCOS 相關的高雄激素性痤瘡、以及 Cushing's 症候群相關皮膚表現可能有間接效益。不過此用途已因肝毒性黑框警語，多被 levoketoconazole 等衍生藥物取代。

整體而言，這兩條機轉都不是針對尋常性痤瘡的第一線病理路徑，證據強度因此被稀釋，也是目前僅有一個小型、非註冊性設計臨床試驗的原因。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07237763](https://clinicaltrials.gov/study/NCT07237763) | Phase NA | 進行中（未招募，尚無結果） | 52 | 頭對頭比較外用 Ketoconazole 2% cream 與外用 Adapalene 2% cream 治療輕度粉刺與丘疹膿疱型痤瘡，探討 ketoconazole 能否作為副作用較少、順從性較佳的視黃酸替代方案 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28111792](https://pubmed.ncbi.nlm.nih.gov/28111792/) | 2017 | 體外研究 | Microbiol Immunol | Ketoconazole 可抑制 P. acnes 脂肪酶活性，為抗痤瘡機轉提供直接體外證據 |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | 體外研究 | Biol Pharm Bull | Azole 類抗真菌藥（含 ketoconazole）對痤瘡患者分離之 P. acnes 具體外抗菌活性 |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | 病例系列 | Clin Exp Dermatol | Pityrosporum（Malassezia）毛囊炎常被誤診為尋常性痤瘡，提示抗真菌治療對此亞型可能有效 |
| [8255067](https://pubmed.ncbi.nlm.nih.gov/8255067/) | 1993 | 回顧 | Keio J Med | Pityrosporum ovale 與多種皮膚病（含毛囊炎）相關，支持抗真菌藥物皮膚科應用基礎 |
| [12566804](https://pubmed.ncbi.nlm.nih.gov/12566804/) | 2003 | 回顧 | Dermatology | 系統性痤瘡治療現況回顧，抗生素為中重度痤瘡主流，未直接評估 ketoconazole |
| [8090657](https://pubmed.ncbi.nlm.nih.gov/8090657/) | 1993 | 回顧/病例系列 | Pol Tyg Lek | PCOS 高雄激素相關痤瘡的治療經驗，降雄激素療法可改善痤瘡與皮脂漏 |
| [33216275](https://pubmed.ncbi.nlm.nih.gov/33216275/) | 2021 | RCT（非痤瘡適應症） | Pituitary | Levoketoconazole（ketoconazole 衍生物）改善 Cushing's 症候群症狀，支持其抑制類固醇生成之全身性機轉 |
| [19445767](https://pubmed.ncbi.nlm.nih.gov/19445767/) | 2009 | 回顧 | BMJ Clin Evid | PCOS 與痤瘡、多毛症等雄激素過高表現相關之綜述 |
| [8629828](https://pubmed.ncbi.nlm.nih.gov/8629828/) | 1996 | 病例報告 | Arch Dermatol | 新生兒 Malassezia furfur 膿疱病外觀近似「新生兒痤瘡」，提示黴菌感染可能被誤判為痤瘡 |
| [32872149](https://pubmed.ncbi.nlm.nih.gov/32872149/) | 2020 | 回顧 | Pharmaceuticals | 比較藥物 Adapalene 於痤瘡治療的最新進展回顧，非 ketoconazole 主體研究 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
現有直接證據僅 1 個小型、非註冊性設計（Phase NA）且尚未有結果的臨床試驗，文獻多為體外研究、病例報告或與 PCOS/Cushing's 症候群相關的間接證據（L3，決策階段 S1，Research Question）；同時台灣未上市、無許可證資料，且 TFDA 仿單警語/禁忌屬 Blocking 等級的資料缺口，尚無法進入安全性初評。

**若要推進需要：**
- 取得 TFDA 仿單警語與禁忌症資料（DG001，Blocking）
- 補齊 DrugBank 正式作用機轉資料（DG002）
- 等待 NCT07237763 完成並公布結果，並釐清其適應症究竟為尋常性痤瘡或 Malassezia 毛囊炎
- 評估台灣上市與許可證申請可行性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

