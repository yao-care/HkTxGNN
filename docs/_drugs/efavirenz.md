---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 308
evidence_level: L5
indication_count: 3
monitor_inn: "EFAVIRENZ"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-28
description: "Efavirenz：預測新適應症為猿猴免疫缺陷病毒感染 (simian immunodeficiency virus infection)（證據等級 L5）。原適應症：HIV 感染、AIDS"
---

# Efavirenz
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Efavirenz：從 HIV 感染到猿猴免疫缺陷病毒感染
{: .text-alpha }

## 一句話總結

Efavirenz 是一種 HIV-1 非核苷類逆轉錄酶抑制劑（NNRTI），知識圖譜中記錄的原適應症為 HIV 感染與 AIDS。
TxGNN 模型預測它可能對**猿猴免疫缺陷病毒感染 (simian immunodeficiency virus infection)** 有效，
但目前**沒有臨床試驗**，僅有 **13 篇文獻**，且多為動物與病毒學研究，並非針對新用途的療效證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染、AIDS（來自知識圖譜的記錄；本報告所取得的香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 猿猴免疫缺陷病毒感染 (simian immunodeficiency virus infection) |
| TxGNN 預測分數 | 0.9980 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 7 張／共 7 張） |
| 許可證數 | 7 張（有效 7 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Efavirenz 是 HIV-1 的 NNRTI，作用標的為 HIV-1 逆轉錄酶。

野生型 SIV 的逆轉錄酶缺少 NNRTI 結合口袋，天生對 NNRTI 不敏感。文獻中的研究使用的是 RT-SHIV，即在 SIV 骨架中置入 HIV-1 逆轉錄酶的嵌合病毒，用來在獼猴身上模擬 HIV-1 治療。因此這些研究呈現的活性來自 HIV-1 逆轉錄酶這個標的，屬於已知 HIV 用途的**前臨床動物模型**，並不是真正的新適應症。

TxGNN 模型（深度學習）給出的高分（0.9980）可能反映模型學到的相關疾病（如 HIV）之間的相似性，而非生物學證據，也不代表 Efavirenz 對野生型 SIV 的實際療效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下依與 Efavirenz 的相關程度挑選，均為動物或實驗室研究，沒有 RCT：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/) | 2004 | 動物研究 | Antimicrob Agents Chemother | 在感染 RT-SHIV 的恆河猴中評估 Efavirenz 的抗病毒活性 |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | 動物研究 | J Virol | Efavirenz、lamivudine、tenofovir 合併治療可降低 RT-SHIV 感染獼猴的病毒量 |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | 動物研究 | Antimicrob Agents Chemother | 四藥、五藥強化療法改善 RT-SHIV 病毒衰減動力學 |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | 動物研究 | Retrovirology | 短期 Efavirenz 單藥後接合併療法，追蹤 RT-SHIV 次族群動態 |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | 動物/病毒學研究 | J Virol | 抗病毒治療下 RT-SHIV 遺傳多樣性仍持續存在 |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | 動物/病毒學研究 | J Virol | 超靈敏 PCR 偵測到治療前即存在的罕見抗藥變異株 |
| [26559632](https://pubmed.ncbi.nlm.nih.gov/26559632/) | 2015 | 動物/病毒學研究 | Retrovirology | 血漿與組織病毒族群均勻混合，提示治療期間組織內缺乏病毒複製 |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | 體外研究 | J Virol | 體外特性分析 SIV-HIV 嵌合病毒，用於研究 NNRTI 抗藥性 |
| [35856680](https://pubmed.ncbi.nlm.nih.gov/35856680/) | 2022 | 前臨床影像研究 | Antimicrob Agents Chemother | 質譜影像分析抗反轉錄病毒藥物在獼猴脾臟的空間分布與纖維化關係 |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | 體外研究 | Antivir Ther | 比較多種抗 HIV 藥物對 HIV-2、SIV、SHIV 的活性 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66814 | APT-EFAVIRENZ TABLETS 600MG | 未提供 | 未提供 |
| HK-61617 | EFAVIRENZ SANDOZ TABLETS 600MG | 未提供 | 未提供 |
| HK-66482 | EFAVIRENZ TABLETS USP 600MG | 未提供 | 未提供 |
| HK-66634 | EFAVIRENZ TABLETS 200MG | 未提供 | 未提供 |
| HK-59769 | ESTIVA-600 TAB 600MG | 未提供 | 未提供 |

目前共有 7 張有效許可證，上表僅列出其中 5 張。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：肝衰竭、肝病、脂肪肝、慢性 B 型與 C 型肝炎、癲癇、焦慮症、精神官能症、妄想症、思覺失調症（偏執型）、腎病、Fanconi 腎小管症候群、乳酸中毒、高三酸甘油脂血症、低磷血症、骨軟化症、佝僂病、肥胖等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 重大：Dolasetron。
  - 中度：Clarithromycin、Bupropion、Aprepitant、Pioglitazone、Saxagliptin、Dexamethasone、Hydrocortisone、Betamethasone、Triamcinolone、Famotidine、Rabeprazole、Loperamide、Minocycline 等。

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻皆為獼猴與體外研究。這些研究依賴帶有 HIV-1 逆轉錄酶的嵌合病毒，等同於 HIV 既有用途的動物模型，並未顯示對野生型 SIV 有效。目前沒有直接證據顯示這是可轉化的新適應症，證據等級為 L5。
- SIV 感染屬於非人類動物疾病，沒有人類使用的臨床需求。

**若要推進需要：**
- 釐清此預測是否有實際的研究或臨床價值，否則建議將其視為模型網路鄰近性造成的假陽性。
- 取得香港許可證的核准適應症文字與仿單警語。
- 若仍要探索，應補充作用機轉資料，並以野生型 SIV 評估 Efavirenz 的實際活性。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

