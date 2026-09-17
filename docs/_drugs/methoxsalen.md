---
layout: default
title: Methoxsalen
parent: 僅模型預測 (L5)
nav_order: 488
evidence_level: L5
indication_count: 5
---

# Methoxsalen
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

# Methoxsalen（8-MOP）：老藥新用於皮膚 T 細胞淋巴瘤譜系疾病

## 一句話總結

Methoxsalen（DrugBank DB00553）目前在本地並未上市，原始核准適應症資料尚未取得。
TxGNN 模型將其與多個皮膚/淋巴系統腫瘤關聯，排名最高的是**局限型佩吉樣網狀細胞增生症（Localized Pagetoid Reticulosis，CTCL 亞型）**，
但此候選目前**無直接臨床試驗或文獻佐證**，僅有機轉層面的類比推論；證據較實在的則是次位候選**惰性原發性皮膚 T 細胞淋巴瘤**，有 **2 篇文獻**支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口——尚無許可證或原始適應症紀錄，待補充 TFDA/仿單資料（見 DG001） |
| 預測新適應症 | Localized Pagetoid Reticulosis（局限型佩吉樣網狀細胞增生症） |
| TxGNN 預測分數 | 99.97%（rank 1120） |
| 證據等級 | L4（機轉推論為主，無直接試驗/文獻） |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 Methoxsalen 詳細的作用機轉資料庫紀錄，且原始核准適應症亦無資料可查（DG001、DG002 皆列為待補資料缺口）。
不過根據 evidence pack 內附的機轉推論文字，Methoxsalen（8-MOP）是一種光敏化 psoralen 化合物，經 UVA 活化後可使 DNA 產生交聯，誘導淋巴球（尤其是惡性 T 細胞）凋亡。
這正是 PUVA（局部光化學治療）與體外光分離置換術（ECP/UVADEX）用於治療蕈狀肉芽腫（Mycosis Fungoides）及其他皮膚 T 細胞淋巴瘤（CTCL）病譜的藥理基礎。

Localized Pagetoid Reticulosis（Woringer-Kolopp disease）屬於 CTCL 的局限型亞型，理論上與 PUVA 的標準適應症機轉相通，但本次收集到的證據庫中**沒有直接鎖定此罕見亞型的臨床試驗或文獻**，屬於「同類疾病外推」的間接推論，因此證據強度僅達 L4。
相對地，次位候選「惰性原發性皮膚 T 細胞淋巴瘤」機轉關聯更明確——美國 FDA 已核准 Methoxsalen 用於 ECP 治療 CTCL 皮膚表現，且有實際文獻佐證（見下方文獻證據）。

## 臨床試驗證據

目前無相關臨床試驗登記（針對 Localized Pagetoid Reticulosis 的 clinicaltrials.gov 與 ICTRP 查詢均為 0 筆）。

## 文獻證據

目前無相關文獻（針對 Localized Pagetoid Reticulosis 的 PubMed 查詢為 0 筆）。

> 說明：本評估以 TxGNN 排名第一的候選適應症為主體，故上方兩節依規則呈現「無資料」。實際證據較強的候選為次位排名的「惰性原發性皮膚 T 細胞淋巴瘤」，詳見下方補充。

## 其他預測適應症與證據（補充）

同一藥物在本次評估中還有 4 個候選適應症，證據強度差異很大，一併列出供決策參考：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|------|-----------|-----------|---------|---------|------|
| 2 | 惰性原發性皮膚 T 細胞淋巴瘤 | 99.91% | L3 | S2 | Proceed with Guardrails |
| 3 | 成熟 B 細胞腫瘤（廣泛分類） | 99.84% | L5 | S0 | Hold |
| 4 | 小腸柏基特氏淋巴瘤 | 99.80% | L5 | S0 | Hold |
| 5 | 甲狀腺黏膜相關淋巴組織淋巴瘤 | 99.78% | L5 | S0 | Hold |

排名 2 是本次證據最紮實的候選，機轉上與 Methoxsalen 已核准的 ECP 適應症直接相通，且有以下文獻支持：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12118838](https://pubmed.ncbi.nlm.nih.gov/12118838/) | 2000 | Cohort | The International Journal of Artificial Organs | 光分離置換術治療皮膚T細胞淋巴瘤的五年經驗，MF 為最常見型且病程惰性 |
| [23074497](https://pubmed.ncbi.nlm.nih.gov/23074497/) | 2006 | Review | Ontario Health Technology Assessment Series | 體外光分離置換術（ECP）用於難治型紅皮病性 CTCL 之實證分析 |

排名 3-5（成熟 B 細胞腫瘤、柏基特氏淋巴瘤、甲狀腺 MALT 淋巴瘤）皆為深部器官系統性腫瘤，不在 Methoxsalen 光敏化機轉可及範圍內，無任何試驗或文獻支持，純屬模型分數驅動，判定為 Hold。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**（主候選 Localized Pagetoid Reticulosis）

**理由：**
- 排名第一的候選僅有機轉類比推論，無任何直接臨床試驗或文獻證據，且藥物本身在本地未上市、TFDA 仿單警語/禁忌資料缺失（DG001，屬 Blocking 等級），無法完成 S1 安全性初評。
- 次位候選「惰性原發性皮膚 T 細胞淋巴瘤」證據較強（L3、已有 FDA 核准的 ECP 機轉基礎），若要推進老藥新用，建議優先評估此候選並標記 Proceed with Guardrails。

**若要推進需要：**
- 取得 TFDA 仿單全文，解決 DG001（安全性警語/禁忌）blocking 缺口
- 補充 Methoxsalen 完整 MOA 資料（DG002），確認光敏化機轉細節與劑型（口服 vs. 外用 vs. ECP 專用配方 UVADEX）
- 針對 Localized Pagetoid Reticulosis 執行專門的文獻/試驗檢索（含 CTCL/MF 大類關鍵字擴大搜尋），驗證是否有病例報告等級證據
- 確認給藥途徑相容性（route_compatibility 目前為 pending，尚未評估）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

