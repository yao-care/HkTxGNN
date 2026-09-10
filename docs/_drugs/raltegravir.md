---
layout: default
title: Raltegravir
parent: 中證據等級 (L3-L4)
nav_order: 629
evidence_level: L3
indication_count: 3
---

# Raltegravir
{: .fs-9 }

證據等級: **L3** | 預測適應症: **3** 個
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

# Raltegravir：（原適應症資料缺失）與 3 項 TxGNN 預測適應症評估

## 一句話總結

Raltegravir（DrugBank ID: DB06817）目前在香港**未上市**，且無許可證登記，原適應症資料缺失。文獻證據顯示其屬於 integrase strand transfer inhibitor（INSTI）類藥物。TxGNN 對本藥共預測 3 項新適應症（分數均 ~99.8%），但逐一檢視臨床試驗與文獻後發現，**三項預測均非真實可行的老藥新用機會**——分別為動物模式研究、知識圖譜本體錯配、以及零證據的模型假影。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（`original_indications` 為空，`original_moa` 亦缺失） |
| 預測新適應症（Rank 1） | Simian Immunodeficiency Virus Infection（SIV 感染） |
| TxGNN 預測分數 | 99.78%（rank 4879） |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | **Hold** |

## 為什麼這個預測合理？

目前缺乏 DrugBank 結構化的作用機轉（MOA）資料。但根據 evidence pack 中的文獻摘要（PMID 20233398）可知，raltegravir 屬於 **integrase strand transfer inhibitor（INSTI）**類藥物，透過抑制病毒整合酶阻斷前病毒基因體嵌入宿主 DNA，此為抗反轉錄病毒（HIV）藥物的核心機轉。

SIV（猿猴免疫缺陷病毒）與 HIV 同科、整合酶結構高度同源，raltegravir 對 SIV 整合酶確實具體外/體內抑制活性，文獻上也支持這點。**但這並不構成「老藥新用」機會**：SIV 感染是研究 HIV 病理機轉與抗病毒策略時所使用的**非人類靈長類動物模式**，而非一個獨立存在、需要藥物核准的人類疾病適應症。換言之，這些證據早已被涵蓋在 raltegravir 既有的 HIV 治療研究範疇內，只是模型把「動物模式疾病節點」誤判為新的治療標的。

另外兩項預測（貓愛滋 FIV、罕見神經發育疾病）經檢視後問題更明顯：FIV 相關的兩筆臨床試驗實際上是人類 HIV 患者的 dolutegravir vs raltegravir 頭對頭試驗（SPRING-2 系列），判斷為知識圖譜疾病本體節點錯置；神經發育疾病則完全無臨床試驗與文獻支持，屬於 embedding 相似度產生的模型假影。

## 臨床試驗證據（Rank 1：SIV Infection）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | NA | WITHDRAWN | 0 | 研究 HIV（非 SIV）整合酶抑制劑之病毒衰減動力學，試驗已撤回、未招募任何受試者，無可用證據（相關性評級 C） |

## 文獻證據（Rank 1：SIV Infection）

以下均為動物模式（SIVmac251 感染獼猴等）研究，非人類臨床證據：

| PMID | 年份 | 研究類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20233398](https://pubmed.ncbi.nlm.nih.gov/20233398/) | 2010 | 動物藥理研究 | Retrovirology | 建立以 raltegravir 為主的 SIVmac251 感染獼猴治療方案，作為慢病毒持續性動物模式 |
| [29643246](https://pubmed.ncbi.nlm.nih.gov/29643246/) | 2018 | 動物病毒動力學 | J Virol | 分析 CD8+ 細胞存在/缺失下 SIV 2-LTR circles 的動態變化 |
| [31597776](https://pubmed.ncbi.nlm.nih.gov/31597776/) | 2019 | 動物病毒基因體研究 | J Virol | 評估 ART 早期介入後 SIV 持續性病毒基因體完整性 |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | 動物代謝副作用研究 | Clin Infect Dis | Dolutegravir 與 raltegravir 對人類/猿猴脂肪組織有促脂生成與胰島素阻抗作用 |
| [29466356](https://pubmed.ncbi.nlm.nih.gov/29466356/) | 2018 | 動物抗藥性突變研究 | PLoS One | 非抑制性 ART 下 SIV 感染獼猴出現抗藥性突變 |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | 體外抗藥性特徵分析 | J Virol | SIVmac239 對整合酶抑制劑之抗藥性表現型特徵 |
| [24622515](https://pubmed.ncbi.nlm.nih.gov/24622515/) | 2014 | 動物暴露後預防研究 | Sci Transl Med | 局部整合酶抑制劑對獼猴陰道 SHIV 感染之暴露後保護效果 |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | 動物神經免疫研究 | mBio | 慢病毒感染在有效 ART 下仍持續存在於腦組織 |
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | 體外抗病毒活性研究 | Antimicrob Agents Chemother | Bictegravir/Cabotegravir 對抗藥性 SIVmac239 與 HIV-1 之活性 |
| [23365453](https://pubmed.ncbi.nlm.nih.gov/23365453/) | 2013 | 體外藥敏分析 | J Virol | 猿猴反轉錄病毒第4型對多種抗反轉錄病毒藥物之敏感性分析 |

> 提醒：以上皆為非人類靈長類 SIV/SHIV 動物模式研究，用於支持 HIV 相關機轉研究，不構成人類新適應症的直接證據。

## 香港上市資訊

Raltegravir 目前在香港**未上市**，無任何許可證登記（`total_licenses = 0`）。

## 其他預測適應症（Rank 2、3）

| Rank | 預測適應症 | TxGNN 分數 | 證據等級 | 問題摘要 | 決策 |
|------|-----------|-----------|---------|---------|------|
| 2 | Feline Acquired Immunodeficiency Syndrome（貓愛滋） | 99.78% | L4 | 唯二相關試驗（NCT01231516、NCT01227824）實為人類 HIV 患者的 dolutegravir vs raltegravir 頭對頭試驗，與貓愛滋無關，判斷為知識圖譜疾病節點錯置 | Hold |
| 3 | Neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter | 99.77% | L5 | 零臨床試驗、零文獻，與 raltegravir 機轉無已知生物學連結，判斷為模型預測假影 | Hold |

## 安全性考量

安全性資訊請參考原廠仿單。（`key_warnings`、`contraindications`、DDI 查詢均無資料）

## 結論與下一步

**決策：Hold**

**理由：**
- 3 項預測分數雖高（皆 >99.7%），但逐一查證後皆非可行的老藥新用機會：Rank 1（SIV）屬既有 HIV 動物模式研究範疇、非新適應症；Rank 2（FIV）為知識圖譜本體錯配之人類 HIV 試驗誤植；Rank 3 為零證據的模型假影。
- 藥物本身在香港未上市、無許可證，且 MOA 與安全性資料均缺失，尚不具備進入 S1 安全性初評的基礎條件。

**若要推進需要：**
- 修正 TxGNN 知識圖譜中 SIV / FIV 疾病節點與人類 HIV 節點的本體映射，避免動物模式與人類疾病混淆
- 補齊 DrugBank 作用機轉（MOA）資料
- 取得仿單警語/禁忌資料（原資料缺口標記來源為 TFDA 官網，須確認是否應改查香港衛生署或原廠仿單）
- 若日後 TxGNN 產出真正屬於人類疾病的新預測適應症，應重新執行完整證據收集流程
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

