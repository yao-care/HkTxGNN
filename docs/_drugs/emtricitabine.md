---
layout: default
title: Emtricitabine
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 3
---

# Emtricitabine
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

# Emtricitabine：從 HIV-1 感染到貓後天免疫缺乏症候群（FIV）

## 一句話總結

Emtricitabine 是核苷類逆轉錄酶抑制劑（NRTI），常見於 Truvada、Descovy 等 HIV 複方，香港許可證未載明適應症，依藥理類別判斷用於 HIV-1 感染。
TxGNN 模型預測它可能對**貓後天免疫缺乏症候群（feline acquired immunodeficiency syndrome，FIV 感染）**有效。
目前有 **4 個臨床試驗**和 **1 篇文獻**，但 4 個試驗全是人類 HIV 研究、與貓無直接關聯，文獻是唯一的貓科前臨床研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明；依藥理類別推斷為 HIV-1 感染 |
| 預測新適應症 | 貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L4（僅有前臨床研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 15 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Emtricitabine 屬於 NRTI 類別，作用是抑制病毒的逆轉錄酶。FIV 是慢病毒，其逆轉錄酶與 HIV-1 相關，因此在生物學上有合理性。

TxGNN 給出的高分，很可能反映 HIV 與 FIV 在知識圖譜中的相似性。目前沒有任何以 emtricitabine 為主要測試對象的貓科療效或劑量資料。

唯一的文獻是 2023 年一項 FIV 感染家貓研究，測試 dolutegravir、tenofovir 與 emtricitabine（40 mg/kg）的組合抗病毒療法。摘要只載明評估藥物動力學與臨床結果，未提供結果，無法判斷 emtricitabine 的個別貢獻。

同一份資料中另有兩個預測：猴免疫缺乏病毒（SIV）感染有多篇獼猴研究，但屬於動物模型，主要是暴露前預防（PrEP），只能支持生物學合理性；某罕見神經發展疾患沒有任何證據，也無機轉關聯，應視為知識圖譜的假象。

## 臨床試驗證據

以下 4 個試驗都是人類 HIV 研究，emtricitabine 只是背景療法或對照組成分，對貓科疾病只有間接參考價值（相關性 C 級）。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | 完成 | 828 | Dolutegravir 對比 raltegravir，搭配 ABC/3TC 或 TDF/FTC，用於初治 HIV-1 成人 |
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | 完成 | 844 | Dolutegravir + ABC/3TC 對比 Atripla（含 emtricitabine），僅出現在對照組 |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | 完成 | 208 | Dolutegravir 劑量選擇，搭配 ABC/3TC 或 TDF/FTC |
| [NCT02770508](https://clinicaltrials.gov/study/NCT02770508) | Phase 4 | 完成 | 145 | Darunavir + lamivudine 對比 darunavir + TDF/FTC，emtricitabine 僅在對照組 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | 動物前臨床研究 | Viruses | 在 FIV 感染家貓評估 dolutegravir、tenofovir、emtricitabine 組合療法的藥動學與臨床結果；摘要未呈現結果 |

## 香港上市資訊

15 張許可證中列出 5 張主要許可證，資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-57749 | TRUVADA TAB (IRELAND) | Gilead Sciences Hong Kong Limited |
| HK-64704 | DESCOVY TABLETS 200MG/25MG | Gilead Sciences Hong Kong Limited |
| HK-66324 | TENO-EM TABLETS | Neopharm Limited |
| HK-67846 | TENEM TABLETS 200MG/245MG | Lotus Pharmaceutical HK Limited |
| HK-67560 | APO-EMTRICITABINE-TENOFOVIR TABLETS 200MG/300MG | Hind Wing Co Ltd |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據僅到 L4。唯一與貓相關的研究是組合療法的動物前臨床研究，emtricitabine 的個別療效與安全性未知，4 個臨床試驗也都與貓無直接關聯。
- 預測適應症屬於獸醫領域，並非人類新適應症，不能直接套用現有人用許可證。
- 香港許可證的警語與禁忌資料尚未取得，無法進行安全性篩選。

**若要推進需要：**
- 取得 PMID 37112803 全文，確認 emtricitabine 在貓體內的藥動學、療效與耐受性
- 補充貓科劑量、毒性與長期安全性資料（必要時另做單藥比較）
- 取得香港衛生署仿單的警語與禁忌
- 取得 DrugBank 的作用機轉資料
- 釐清人用藥物用於動物的法規與獸醫使用路徑

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

