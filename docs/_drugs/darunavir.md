---
layout: default
title: Darunavir
parent: 中證據等級 (L3-L4)
nav_order: 242
evidence_level: L4
indication_count: 4
---

# Darunavir
{: .fs-9 }

證據等級: **L4** | 預測適應症: **4** 個
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

# Darunavir：從 HIV-1 感染到猿猴免疫缺陷病毒感染

## 一句話總結

Darunavir 是 HIV-1 蛋白酶抑制劑，原本用於人類 HIV-1 感染。
TxGNN 模型預測它可能對**猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)** 有效。
目前**沒有臨床試驗**，只有 **4 篇**獼猴前臨床研究，且 darunavir 只是聯合抗病毒療法的成分之一，不是被單獨測試的藥物。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV-1 感染（許可證資料未載明適應症文字，此為藥理分類） |
| 預測新適應症 | 猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 17 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供 MOA）。根據已知資訊，Darunavir 屬於 HIV-1 蛋白酶抑制劑，在人類 HIV-1 感染中的療效已被證實。SIV 是 HIV 在獼猴身上的標準動物模型，兩種病毒的蛋白酶高度相關，因此模型的連結在生物學上說得通。

不過要小心解讀。這個「新適應症」是動物疾病模型，不是新的人類適應症。它主要反映 darunavir 既有的抗反轉錄病毒機轉，並不代表發現了新的治療用途。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

四篇文獻都是 SIV 感染獼猴的前臨床動物研究（證據包分級為 Tier 3），沒有 RCT。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | 動物前臨床研究 | AIDS Res Hum Retroviruses | 在 SIVmac239 感染的恆河猴中，比較兩種複方注射型 cART 方案（含 FTC、TDF 的三藥方案等）的病毒抑制效果 |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | 動物前臨床研究 | PLoS One | 在 SIV 感染的中國恆河猴中，探討強化 cART 合併 HDAC 抑制劑 SAHA 對病毒庫的影響 |
| [22737073](https://pubmed.ncbi.nlm.nih.gov/22737073/) | 2012 | 動物前臨床研究 | PLoS Pathog | 高強度多藥 ART 方案在 SIVmac251 感染獼猴中達成長期病毒抑制，並限制病毒庫 |
| [21505294](https://pubmed.ncbi.nlm.nih.gov/21505294/) | 2011 | 動物前臨床研究 | AIDS | 金化合物 auranofin 搭配 ART，可縮小猴 AIDS 模型的病毒庫，並在停藥後抑制病毒量 |

這些研究測試的是整個聯合療法，無法從提供的資料中分離出 darunavir 的個別貢獻。

## 香港上市資訊

香港共有 17 張許可證，以下列出 5 張。證據包未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66733 | DARUNAVIR SANDOZ TABLETS 800MG | SANDOZ HONG KONG LIMITED |
| HK-68460 | DARUNAVIR TABLETS 800MG | CHEMILL PHARMA LIMITED |
| HK-67175 | DARUNAVIR KRKA TABLETS 600MG | SINO PACIFIC PHARMA COMPANY LIMITED |
| HK-58980 | PREZISTA TAB 600MG | JOHNSON & JOHNSON (HONG KONG) LTD. |
| HK-68320 | PROTOMUNE TABLETS 400MG | LOTUS PHARMACEUTICAL HK LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有前臨床動物研究，沒有臨床試驗，且 darunavir 只是聯合方案的成分之一。
- SIV 是動物模型，不是新的人類適應症，因此不構成實質的藥物再利用機會。
- 同一份預測清單中，其他預測也不支持推進：
  - 貓後天免疫缺乏症候群：只有人類 HIV-1 的 Phase 4 試驗（NCT02770508），對貓病毒屬間接證據。
  - 神經發展疾患：找不到合理機轉，高分很可能是知識圖譜的假象。
  - 高脂血症：HIV 蛋白酶抑制劑本身會升高血脂，方向相反，且該疾病術語已被本體標為過時。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料（目前是阻擋性缺口，無法進入安全性篩選）。
- 補齊 DrugBank 的作用機轉資料。
- 找出 darunavir 單藥或其個別貢獻的 SIV／FIV 專屬數據。
- 先確認是否真有人類疾病的再利用目標，再評估是否值得投入。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

