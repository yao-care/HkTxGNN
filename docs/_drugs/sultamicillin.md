---
layout: default
title: Sultamicillin
parent: 中證據等級 (L3-L4)
nav_order: 714
evidence_level: L3
indication_count: 10
---

# Sultamicillin
{: .fs-9 }

證據等級: **L3** | 預測適應症: **10** 個
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

# Sultamicillin：從細菌感染到支氣管炎急性發作

## 一句話總結

Sultamicillin 是 ampicillin 與 sulbactam 以酯鍵結合而成的前驅藥複方抗生素，原本用於一般細菌感染治療（香港尚無完整核准適應症資料）。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，
目前有 **0 個臨床試驗登記**，但有 **16 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無完整資料（依藥理類別為細菌感染治療，Sultamicillin 為 ampicillin/sulbactam 前驅藥） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 96.20% |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空），但根據證據包提供的機轉關聯分析：Sultamicillin 是 ampicillin 與 sulbactam（一種 β-lactamase 抑制劑）以酯鍵結合而成的前驅藥，屬於廣效 β-lactam / β-lactamase 抑制劑複方抗生素，藥理上原本即涵蓋下呼吸道細菌感染的治療範圍。

慢性支氣管炎急性惡化（acute exacerbation of chronic bronchitis）多由細菌感染誘發，常見致病菌如 *Haemophilus influenzae*、*Streptococcus pneumoniae*、*Branhamella catarrhalis* 等，恰好落在 Sultamicillin 的抗菌範圍內。因此這項預測與其說是機轉上的跨適應症再利用，不如說是抗生素在既有抗菌譜內的**適應症延伸**——這也是為什麼多篇 1980–1990 年代的臨床觀察直接針對「急性支氣管炎惡化」進行療效評估。

需注意的是，現有文獻證據等級偏低（多為開放性試驗、世代評估或兒科藥動學研究，缺乏近代大型隨機對照試驗），且香港尚無此藥品的許可證資料，故雖機轉合理，仍建議以 Guardrails 方式推進，不宜直接視為確立適應症。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [6323377](https://pubmed.ncbi.nlm.nih.gov/6323377/) | 1984 | Open-label trial | J Antimicrob Chemother | 30 名慢性支氣管炎急性惡化住院病人口服 Sultamicillin，治療結束臨床治癒率 73%，追蹤一週後 60% |
| [8008659](https://pubmed.ncbi.nlm.nih.gov/8008659/) | 1993 | 對照臨床研究（vs cefuroxime axetil） | Pol Tyg Lek | 門診慢性支氣管炎急性惡化，Sultamicillin 與 cefuroxime axetil 療效比較 |
| [2041156](https://pubmed.ncbi.nlm.nih.gov/2041156/) | 1991 | 世代臨床評估 | Jpn J Antibiot | 132 名下呼吸道感染病人多中心試驗，支氣管炎有效率 78.5%（73/93） |
| [1451929](https://pubmed.ncbi.nlm.nih.gov/1451929/) | 1992 | 開放性治療研究 | J Int Med Res | 30 名成人下呼吸道感染口服 Sultamicillin，治癒率 76.6%，改善率 23.3% |
| [1458803](https://pubmed.ncbi.nlm.nih.gov/1458803/) | 1992 | 開放非對照研究（兒科） | La Clin Ter | 48 名兒童呼吸道感染（含 18 例支氣管炎），96% 臨床反應良好 |
| [3000026](https://pubmed.ncbi.nlm.nih.gov/3000026/) | 1985 | 病原學回顧 | Tohoku J Exp Med | 分析 *Branhamella catarrhalis* 相關呼吸道感染 74 例，含 14 例急性、36 例慢性支氣管炎 |
| [3249372](https://pubmed.ncbi.nlm.nih.gov/3249372/) | 1988 | 兒科藥動學/臨床研究 | Jpn J Antibiot | 兒童 Sultamicillin 顆粒劑血中及尿中濃度測定 |
| [3249362](https://pubmed.ncbi.nlm.nih.gov/3249362/) | 1988 | 兒科藥動學/臨床研究 | Jpn J Antibiot | 兒童細粒劑對多種呼吸道致病菌之抗菌活性與藥動學評估 |
| [3249365](https://pubmed.ncbi.nlm.nih.gov/3249365/) | 1988 | 兒科實驗室/臨床研究 | Jpn J Antibiot | 兒童單次口服劑量血清藥動學參數測定 |
| [3249373](https://pubmed.ncbi.nlm.nih.gov/3249373/) | 1988 | 兒科藥動學/臨床研究 | Jpn J Antibiot | 兒童 10% 細粒劑藥動學及多種感染臨床療效評估 |

---

## 香港上市資訊

目前香港尚無 Sultamicillin 相關許可證登記（市場狀態：未上市）。

---

## 安全性考量

目前缺乏可用的安全性資料——仿單警語、禁忌症與藥物交互作用查詢均無結果。這是一項 **Blocking 等級資料缺口**（見資料缺口 DG001），在取得完整的 TFDA/當地仿單資訊前，此候選無法進入 S1 安全性初評。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 16 篇跨國、跨年代（1984–1993）文獻支持 Sultamicillin 用於慢性支氣管炎急性惡化及下呼吸道感染，機轉合理（抗生素本身即可治療細菌性支氣管炎），但缺乏 RCT，整體證據等級僅 L3。
- 安全性資料為 Blocking 缺口，香港亦尚未上市，故不宜直接推進至臨床決策，需先補齊安全性資訊。

**若要推進需要：**
- 取得 TFDA／香港仿單完整警語與禁忌症資料（DG001，Blocking，需優先處理）
- 補充 DrugBank 完整作用機轉（MOA）資料（DG002）
- 若考慮於香港申請此適應症，建議規劃前瞻性對照試驗以提升證據等級
- 其餘 9 項預測適應症（thrombotic disease、heparin cofactor 2 deficiency 等）缺乏機轉基礎或文獻支持，維持 Hold，不建議投入資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

