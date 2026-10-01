---
layout: default
title: Adalimumab
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 6
---

# Adalimumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Adalimumab：從既有自體免疫適應症到類風濕性血管炎

## 一句話總結

Adalimumab（阿達木單抗）是抗 TNF-α 的單株抗體，香港已有 11 張許可證，原適應症資料在本次資料中缺漏。
TxGNN 模型預測它可能對**類風濕性血管炎 (Rheumatoid Vasculitis)** 有效。
目前有 **5 個臨床試驗**（皆不直接檢驗血管炎療效）和 **20 篇文獻**，主要是 1 篇系統性回顧與個案報告，且有數篇報告指出 adalimumab 本身可能誘發血管炎。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未提供適應症文字 |
| 預測新適應症 | 類風濕性血管炎 (Rheumatoid Vasculitis) |
| TxGNN 預測分數 | 99.80% |
| 證據等級 | L3（有系統性回顧與世代研究，但無針對血管炎的 RCT） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，adalimumab 是全人源化抗 TNF-α 單株抗體，用於類風濕性關節炎等自體免疫疾病。其機轉上可能適用於類風濕性血管炎。

類風濕性血管炎是類風濕性關節炎最嚴重的關節外表現之一，死亡率與病況嚴重度都高，通常需要類固醇或免疫抑制劑。TNF-α 在類風濕疾病的血管發炎中扮演重要角色，所以阻斷 TNF 在理論上說得通。近年生物製劑也被納入這類疾病的治療選項（見下方系統性回顧）。

不過方向並不確定。文獻中同時有多篇個案報告指出，adalimumab 治療期間出現白血球破碎性血管炎、ANCA 相關血管炎與腎炎，以及類狼瘡反應。也有個案在減量後出現急性肺高壓危象，顯示藥物可能有保護作用。整體而言，這個預測目前只能視為「值得研究的問題」，還不是已被證實的療效。

## 臨床試驗證據

以下 5 個試驗都與血管炎療效無直接關係，目前無專門檢驗 adalimumab 治療類風濕性血管炎的試驗。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | 尚未招募 | 80 | 風濕病患者肩關節置換前免疫抑制劑停藥時間的比較，不檢驗血管炎療效 |
| [NCT05111743](https://clinicaltrials.gov/study/NCT05111743) | N/A | 完成 | 9261 | Brolucizumab 用於濕性黃斑部病變的真實世界研究，與 adalimumab 及血管炎無關 |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | 完成 | 808 | 中國類風濕性關節炎生物製劑使用模式的橫斷面研究，無血管炎結果 |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | 完成 | 184 | Tocilizumab 用於類風濕性關節炎的非介入性研究，無血管炎結果 |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | 未知 | 750000 | 使用生物製劑治療單一免疫介導發炎疾病後，發生其他此類疾病的風險，不是療效試驗 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | 系統性回顧 | Clin Rheumatol | 依 PRISMA 回顧生物製劑用於類風濕性血管炎的證據（摘要未列出結果數據） |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | 世代研究 | RMD Open | BSRBR-RA 登錄資料，比較 TNF 抑制劑與傳統 DMARD 治療的類風濕性關節炎患者發生類狼瘡與類血管炎事件的風險 |
| [24854356](https://pubmed.ncbi.nlm.nih.gov/24854356/) | 2014 | 世代研究 | Ann Rheum Dis | 探討例行 ANA 檢測能否預測生物製劑誘發的狼瘡與血管炎 |
| [25133007](https://pubmed.ncbi.nlm.nih.gov/25133007/) | 2014 | 個案報告 | Case Rep Rheumatol | 類風濕性關節炎合併指端血管炎，使用 adalimumab 後反應良好 |
| [30773522](https://pubmed.ncbi.nlm.nih.gov/30773522/) | 2019 | 個案報告 | Intern Med | 類風濕性血管炎患者減少 adalimumab 劑量 8 個月後發生急性肺高壓危象 |
| [21385558](https://pubmed.ncbi.nlm.nih.gov/21385558/) | 2011 | 個案報告 | Clin Exp Rheumatol | 抗 TNF 治療無效的類風濕性血管炎，改用 tocilizumab 成功治療 |
| [28719435](https://pubmed.ncbi.nlm.nih.gov/28719435/) | 2018 | 個案報告 | Am J Dermatopathol | Adalimumab 治療類風濕性關節炎期間出現白血球破碎性血管炎 |
| [36418100](https://pubmed.ncbi.nlm.nih.gov/36418100/) | 2023 | 個案報告 | Intern Med | Abatacept 與 adalimumab 治療期間出現 ANCA 相關腎炎，改用 tocilizumab 後緩解 |
| [19482531](https://pubmed.ncbi.nlm.nih.gov/19482531/) | 2009 | 個案報告 | Nephrol Ther | Adalimumab 治療類風濕性關節炎期間出現 ANCA 相關血管炎與壞死性腎絲球腎炎 |
| [34068884](https://pubmed.ncbi.nlm.nih.gov/34068884/) | 2021 | 回顧 | J Clin Med | 類風濕性關節炎相關鞏膜炎的診斷與治療概述 |

## 香港上市資訊

香港共登記 11 張許可證，以下列出 5 張主要許可證（許可證資料未提供劑型與適應症文字）。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66711 | AMGEVITA 預充填筆注射液 40mg/0.8ml | AMGEN HONG KONG LIMITED |
| HK-66712 | AMGEVITA 預充填針筒注射液 40mg/0.8ml | AMGEN HONG KONG LIMITED |
| HK-67359 | HULIO 預充填筆注射液 40mg/0.8ml | PRIMEDICA LIMITED |
| HK-65215 | HUMIRA 預充填筆注射液 40mg/0.4ml | ABBVIE LIMITED |
| HK-65214 | HUMIRA 預充填針筒注射液 40mg/0.4ml | ABBVIE LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

另外，文獻提示 TNF 抑制劑本身可能誘發血管炎、類狼瘡反應與 ANCA 相關腎炎，用於血管炎族群時需特別留意。

## 結論與下一步

**決策：Hold**

**理由：**
目前沒有任何針對類風濕性血管炎的 adalimumab 臨床試驗，證據僅限於 1 篇系統性回顧、觀察性研究與個案報告。文獻同時顯示 adalimumab 可能誘發血管炎，療效方向不確定，因此先不推進。

**若要推進需要：**
- 精讀該系統性回顧（PMID 33058033），確認各生物製劑（含 adalimumab）在類風濕性血管炎的實際反應數據
- 從 BSRBR-RA 等世代研究（PMID 28123776）萃取血管炎事件的風險資料，評估 adalimumab 是助還是害
- 取得原適應症與香港仿單的警語、禁忌資料（目前皆缺漏），才能進行安全性篩選
- 補充作用機轉資料（DrugBank）
- 設計專門針對類風濕性血管炎的前瞻性研究，並與其他生物製劑（如 tocilizumab、rituximab）比較

**補充說明：** 同一份預測中，脊椎關節炎（inflammatory spondylopathy）與多關節型幼年類風濕性關節炎已有 Phase 3 證據，且很可能已是核准適應症，未必算真正的老藥新用。這兩項可另案評估。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

