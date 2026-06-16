---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 257
evidence_level: L5
indication_count: 3
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

<div id="pharmacist">

## 藥師評估報告

</div>

# Efavirenz：從 HIV-1 感染到貓免疫缺陷症候群

## 一句話總結

Efavirenz 是非核苷逆轉錄酶抑制劑（NNRTI），全球廣泛用於 HIV-1 感染的抗病毒治療。TxGNN 模型預測它可能對**貓免疫缺陷症候群（Feline Acquired Immunodeficiency Syndrome）**有效，目前僅有 **1 篇體外研究文獻**直接支持此方向，所有檢索到的臨床試驗經審查後均判定為不相關。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV-1 感染（NNRTI 類抗愛滋病毒藥物） |
| 預測新適應症 | 貓免疫缺陷症候群（Feline Acquired Immunodeficiency Syndrome） |
| TxGNN 預測分數 | 99.80% |
| 證據等級 | L4（前臨床體外研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉原始資料（MOA Data Gap）。根據現有醫學知識，Efavirenz 是 NNRTI 類抗病毒藥物，透過非競爭性嵌合至 HIV-1 逆轉錄酶（RT）的 NNRTI 結合口袋，抑制 RNA 依賴性 DNA 聚合活性，阻斷病毒基因組複製。其作為複方製劑 Atripla（EFV＋TDF＋FTC）的核心成分，曾長期是全球 HIV-1 感染一線標準治療藥物。

貓免疫缺陷病毒（FIV）與 HIV-1 同屬慢病毒屬（*Lentivirus*），兩者均具逆轉錄酶，且 FIV 在貓隻中引起類似人類 AIDS 的進行性免疫缺陷症候群。從機轉角度推論，若 NNRTI 能有效抑制 FIV 的逆轉錄酶，理論上可延緩 FIV 病程進展，此為 TxGNN 模型預測的核心假說。

然而，此假說面臨顯著的科學限制。FIV RT 與 HIV-1 RT 的氨基酸序列同源性僅約 40–50%，NNRTI 結合口袋構象差異顯著，使多數為 HIV-1 設計的 NNRTI 對 FIV RT 的活性大幅降低。2023 年一篇體外暨結構生物學研究（PMID 38031646）比較了 Efavirenz（EFV）、Nevirapine（NVP）及 Rilpivirine（RPV）對 FIV 與 HIV 逆轉錄酶的生化特性與結合構象差異，初步評估 NNRTI 跨物種應用的可行性，惟目前尚無任何體內動物療效或臨床數據。此外，FIV 為純獸醫疾病，不感染人類，此預測方向若要推進，須走獸醫藥品開發路徑，而非人體再利用策略。

---

## 臨床試驗證據

> ⚠️ **審查說明**：Evidence Pack 中檢索到的 2 個試驗，經人工審查後均判定為**不相關（Grade C）**，屬系統自動詞彙關聯錯誤，不計入本適應症證據體：
> - **NCT00951015**：Phase 2，研究藥物為 Dolutegravir（整合酶抑制劑），用於**人類** HIV-1 感染，與 Efavirenz 及 FIV 均無關。
> - **NCT01263015**：Phase 3（n=844），同為 Dolutegravir＋Abacavir/Lamivudine 用於**人類** HIV-1 感染，與本適應症無關。

**目前無相關臨床試驗登記。**

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [38031646](https://pubmed.ncbi.nlm.nih.gov/38031646/) | 2023 | 體外研究 / 結構生物學 | Journal of Veterinary Science | 比較第一、二代 NNRTI（NVP、EFV、RPV）對 FIV 及 HIV 逆轉錄酶的生化特性與結構差異，初步評估 NNRTI 治療 FIV 感染的可行性；FIV 目前無有效治療方案 |

---

## 香港上市資訊

Efavirenz 目前**未在香港上市**，無任何藥品許可證記錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 其他預測適應症概覽

本次 Evidence Pack 另包含 2 項預測，摘要如下：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議決策 | 備註 |
|------|-----------|-----------|---------|---------|------|
| 2 | 猿猴免疫缺陷病毒感染（SIV Infection） | 99.80% | L3 | Research Question | 多個 NHP 動物模型（RT-SHIV）研究直接使用 Efavirenz；屬學術研究工具平台，非人體臨床適應症 |
| 3 | 神經發育障礙伴共濟失調步態、失語及皮質白質減少 | 99.77% | L5 | Hold | 完全無臨床試驗及文獻支持，機轉關聯不明，僅模型預測 |

**排名 2（SIV）補充**：多篇非人靈長類（NHP）研究直接在 RT-SHIV 嵌合體模型中測試 Efavirenz，確認其對含 HIV-1 RT 之 SIV 嵌合體的體內抑制療效（見 PMID [15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/)、[15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/)、[20668516](https://pubmed.ncbi.nlm.nih.gov/20668516/) 等共 16 篇文獻）。惟 SIV 不感染人類，此方向的學術意義在於提供 HIV 儲存庫、耐藥性及治療動力學研究的動物模型平台，而非獨立的人體再利用適應症，故決策維持 Research Question 待學術確認層級。

---

## 結論與下一步

**決策：Hold**

**理由：**
頂級預測適應症（貓免疫缺陷症候群）目前僅有 1 篇體外結構生物學研究支持，缺乏動物體內療效數據及任何臨床試驗；目標疾病屬獸醫適應症，不存在人體再利用路徑，加之 Efavirenz 目前於香港未上市、無監管基礎。次要預測（SIV 感染）係動物模型研究工具，亦非獨立人體適應症。整體而言，此 Evidence Pack 目前未揭示可進入臨床評估階段的人體再利用機會。

**若要推進需要：**
- FIV 細胞培養體外抑制活性確認（IC₅₀、EC₅₀），量化 Efavirenz 對 FIV RT 的實際抑制效力
- 分子對接或 X 射線晶體結構分析，確認 Efavirenz 與 FIV RT NNRTI 口袋的結合可行性
- FIV 貓隻體內模型的療效與安全性研究
- 獸醫藥品開發可行性評估（法規路徑、市場規模、競爭格局）
- 補充安全性資料：原廠仿單警語、禁忌症及主要藥物交互作用
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

