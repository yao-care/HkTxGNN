---
layout: default
title: Oxcarbazepine
parent: 中證據等級 (L3-L4)
nav_order: 637
evidence_level: L4
indication_count: 5
---

# Oxcarbazepine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Oxcarbazepine：從癲癇相關適應症到視覺性癲癇

## 一句話總結

Oxcarbazepine（奧卡西平）是一種抗癲癇藥物，臨床上用於局部性癲癇發作的治療。
TxGNN 模型預測它可能對**視覺性癲癇 (Visual Epilepsy)** 有效，
目前有 **1 個臨床試驗**和 **18 篇文獻**與此方向相關，但皆為一般癲癇的間接證據，並無視覺性癲癇的專一研究。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺漏，請參考原廠仿單 |
| 預測新適應症 | 視覺性癲癇 (Visual Epilepsy) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold（列為研究問題） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據文獻，Oxcarbazepine 的活性代謝物 MHD（10-hydroxycarbazepine）可阻斷電壓門控鈉離子通道，降低神經元過度興奮，這是其控制局部性癲癇發作的主要機轉。

視覺性癲癇（枕葉或光敏感性癲癇）屬於局部性或反射性癲癇的亞型，因此在機轉上與 Oxcarbazepine 的作用範圍有合理的關聯。

需注意的是，現有資料中沒有任何證據專門針對視覺性癲癇。極高的 TxGNN 分數（0.9995）很可能只是反映了它與一般癲癇節點在知識圖譜中的距離很近，而不是疾病專一的訊號。另外，藥物的原適應症在資料中缺漏，是否已涵蓋此適應症需人工核對。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | 完成 | 111 | 觀察性研究：新一代抗癲癇藥（含 Oxcarbazepine）作為局部性癲癇第一線合併治療的實際療效；非隨機，也非視覺性癲癇專一 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35429132](https://pubmed.ncbi.nlm.nih.gov/35429132/) | 2022 | 隨機開放性試驗 | CNS Neurosci Ther | 中國新診斷局部性癲癇患者中，比較 Oxcarbazepine 與 Levetiracetam 單一療法的療效、生活品質與心理健康 |
| [35380580](https://pubmed.ncbi.nlm.nih.gov/35380580/) | 2022 | Review | JAMA | 成人癲癇的抗癲癇藥物治療總覽 |
| [39899099](https://pubmed.ncbi.nlm.nih.gov/39899099/) | 2025 | Review | Continuum | 2025 年抗癲癇藥物更新，含藥物動力學與使用方式 |
| [33334546](https://pubmed.ncbi.nlm.nih.gov/33334546/) | 2020 | Review | Seizure | Carbamazepine 與 Oxcarbazepine 在癲癇治療中的現今角色 |
| [37092337](https://pubmed.ncbi.nlm.nih.gov/37092337/) | 2023 | Review | Pharmacogenomics | Oxcarbazepine 藥物基因體學，不同族群間療效與安全性有差異 |
| [12697143](https://pubmed.ncbi.nlm.nih.gov/12697143/) | 2003 | 回溯性比較 | Epilepsy Behav | 65 歲以上癲癇患者使用 Oxcarbazepine 的安全性與耐受性，與較年輕族群無顯著差異 |
| [22091603](https://pubmed.ncbi.nlm.nih.gov/22091603/) | 2012 | 臨床研究 | Epilepsia | 40 位成人口服負荷劑量 Oxcarbazepine 的療效、耐受性與藥物動力學 |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | 三叉神經痛藥物治療更新，Carbamazepine 與 Oxcarbazepine 為有效選項 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49918 | TRILEPTAL TAB 600MG | — | 資料缺漏 |
| HK-50215 | TRILEPTAL TAB 300MG | — | 資料缺漏 |
| HK-50007 | TRILEPTAL ORAL SUSP 60MG/ML | — | 資料缺漏 |
| HK-66355 | TRILOJUB TABLETS 300MG | — | 資料缺漏 |
| HK-66356 | TRILOJUB TABLETS 600MG | — | 資料缺漏 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他預測適應症（供參考）

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 證據摘要 |
|------|-----------|-----------|---------|------|---------|
| 2 | 不寧腿症候群 (Restless Legs Syndrome) | 99.89% | L4 | 研究問題 | 僅有 3 篇病例報告與敘述性回顧，無對照試驗 |
| 3 | 性高潮誘發癲癇 (Orgasm-induced Seizures) | 99.89% | L5 | Hold | 僅有模型預測，無試驗或文獻 |
| 4 | 思考誘發癲癇 (Thinking Seizures) | 99.89% | L4 | 研究問題 | 僅有間接的一般癲癇試驗與小鼠 MES 前臨床研究 |
| 5 | 驚嚇性癲癇 (Startle Epilepsy) | 99.89% | L5 | Hold | 僅有模型預測，無試驗或文獻 |

排名 3–5 的三種反射性癲癇分數完全相同，推測是知識圖譜本體結構造成，而非各疾病獨立的訊號。

## 結論與下一步

**決策：Hold**

**理由：**
- 視覺性癲癇沒有專一的臨床證據，現有資料僅能支持 Oxcarbazepine 用於一般局部性癲癇，證據等級為 L4。
- 香港藥品安全性資料（仿單警語與禁忌）缺漏，屬阻擋性資料缺口，無法進入安全性篩檢。

**若要推進需要：**
- 從香港衛生署取得仿單，補齊原適應症、警語與禁忌症
- 從 DrugBank 補充作用機轉（MOA）
- 確認視覺性癲癇是否已涵蓋在既有適應症內
- 檢索枕葉癲癇或光敏感性癲癇使用 Oxcarbazepine 的病例或亞群分析
- 若要評估不寧腿症候群，需有對照試驗支持，現階段僅有病例報告

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證後才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

