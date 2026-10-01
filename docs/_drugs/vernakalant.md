---
layout: default
title: Vernakalant
parent: 僅模型預測 (L5)
nav_order: 917
evidence_level: L5
indication_count: 6
---

# Vernakalant
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

# Vernakalant：從心房顫動轉復到中風

## 一句話總結

Vernakalant 是一種心房選擇性抗心律不整藥物，用於近期發作心房顫動 (AF) 的藥理學轉復。
TxGNN 模型預測它可能對**中風 (Stroke Disorder)** 有效。
目前有 **3 個臨床試驗**和 **7 篇文獻**，但全部針對心房顫動轉復，沒有任何研究以中風為評估終點，因此屬於間接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 近期發作心房顫動的藥理學轉復（香港許可證未載明適應症文字，此為依 Evidence Pack 說明） |
| 預測新適應症 | 中風 (Stroke Disorder) |
| TxGNN 預測分數 | 99.83% |
| 證據等級 | L4（僅有間接的機轉與心房顫動相關研究，無中風直接證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Vernakalant 一般被認為是心房選擇性的混合型鈉／鉀離子通道阻斷劑，可將心房顫動轉為竇性節律。

心房顫動是中風的主要危險因子，TxGNN 的預測訊號很可能是經由這層關聯產生。部分試驗的設計背景也提到心房收縮功能與中風風險有關，例如心臟復律後的心房收縮力。

不過，**藥物與中風之間沒有直接的機轉或臨床連結**。復律本身有圍術期血栓栓塞風險，不能假設有中風獲益。0.998 的分數是圖譜預測，不是臨床證據。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04485195](https://clinicaltrials.gov/study/NCT04485195) | Phase 4 | 完成 | 350 | RAFF4：急診室中 vernakalant 對比 procainamide 用於急性心房顫動復律，為最大型試驗，無中風終點 |
| [NCT01447862](https://clinicaltrials.gov/study/NCT01447862) | Phase 4 | 完成 | 101 | Vernakalant 對比 ibutilide 用於近期發作心房顫動，評估節律轉復，無中風終點 |
| [NCT01646281](https://clinicaltrials.gov/study/NCT01646281) | Phase 4 | 未知 | 70 | Vernakalant 與 flecainide 對心房顫動患者心房收縮力的影響，僅與血栓風險間接相關 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27292602](https://pubmed.ncbi.nlm.nih.gov/27292602/) | 2016 | Cohort | Am J Emerg Med | 單中心經驗：急診近期發作心房顫動藥物復律的安全性與療效，並追蹤 30 天血栓栓塞或死亡發生率 |
| [17371199](https://pubmed.ncbi.nlm.nih.gov/17371199/) | 2007 | Review | Expert Opin Investig Drugs | 介紹 vernakalant (RSD1235) 的機轉特性與開發進展，用於心房顫動急性轉復 |
| [22576674](https://pubmed.ncbi.nlm.nih.gov/22576674/) | 2012 | Review | Curr Hypertens Rep | 高血壓患者心房顫動的近期試驗，涵蓋 dronedarone 與 vernakalant 的療效與安全性 |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | Review | Lancet | 心房顫動處置進展，包括新型口服抗凝血劑與中風風險分層 |
| [23553811](https://pubmed.ncbi.nlm.nih.gov/23553811/) | 2013 | Review | Pharmacotherapy | 心房顫動處置的臨床更新 |
| [19678722](https://pubmed.ncbi.nlm.nih.gov/19678722/) | 2009 | Review | J Manag Care Pharm | 心房顫動藥物治療的現有與新興選項 |
| [25024989](https://pubmed.ncbi.nlm.nih.gov/25024989/) | 2014 | Review | Heart Lung Vessels | 2013 年心胸血管麻醉與重症主題回顧，包含新型抗心律不整藥與左心耳封堵以降低中風 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61191 | BRINAVESS CONCENTRATE FOR SOLUTION FOR INFUSION 20MG/ML | — | — |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有試驗與文獻都針對心房顫動復律，沒有中風終點，TxGNN 分數僅是圖譜預測，不是臨床證據。
- 復律本身有血栓栓塞風險，不能假設有中風獲益。
- 其餘 5 個預測（竇房結症候群、已廢止的缺血性中風易感性、肌聚醣病、Wildervanck 症候群、ABri 類澱粉變性）都只有模型預測，證據等級 L5，同為 Hold。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選。
- 補齊作用機轉資料（例如查詢 DrugBank）。
- 將問題重新定義為「vernakalant 復律後的血栓栓塞或中風發生率」，並以現有 AF 試驗的追蹤資料做次級分析，而非直接宣稱中風適應症。

> 本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

