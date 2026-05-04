---
layout: default
title: Aztreonam
parent: 高證據等級 (L1-L2)
nav_order: 79
evidence_level: L2
indication_count: 10
---

# Aztreonam
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Aztreonam：從革蘭氏陰性菌感染到淋菌性尿道炎

## 一句話總結

Aztreonam 是唯一上市的單環 β-內醯胺類（monobactam）抗生素，原本用於治療革蘭氏陰性菌引起的嚴重感染症。
TxGNN 模型共預測了 10 個新適應症，其中**淋菌性尿道炎 (Gonococcal Urethritis)** 是實證等級最高的預測，
目前有 **1 個已完成的 Phase 2/3 臨床試驗**和 **8 篇臨床文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 革蘭氏陰性菌感染症（泌尿道感染、肺炎、敗血症等） |
| 預測新適應症（最高實證） | 淋菌性尿道炎 (Gonococcal Urethritis) |
| TxGNN 預測分數 | 99.59% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

> **說明**：TxGNN 排名第 1 的預測（多克隆高黏滯症）及其他多數預測缺乏機轉連結或屬機轉偽陽性，本報告以具最高實證等級（L2）且機轉合理的**淋菌性尿道炎**為核心適應症進行詳細評估。

---

## 為什麼這個預測合理？

Aztreonam 透過選擇性結合革蘭氏陰性菌的**青黴素結合蛋白 PBP-3**，抑制細胞壁肽聚糖的交聯合成，達到殺菌效果。其關鍵優勢在於對多數 β-lactamase 具有高度穩定性，且對革蘭氏陽性菌及厭氧菌完全無活性——這使其在耐藥性革蘭氏陰性菌感染中具有精準的應用價值。

淋病奈瑟菌（*Neisseria gonorrhoeae*）正是革蘭氏陰性雙球菌，屬 Aztreonam 抗菌譜的直接目標。美國 CDC 已將耐藥性淋球菌列為三大緊急公衛威脅之一：自 1930 年代抗生素問世以來，淋球菌已對 penicillin、tetracycline、fluoroquinolone 等多類一線藥物產生廣泛耐藥，目前全球僅餘注射型第三代頭孢菌素（ceftriaxone）一線可用。

正因如此，重新評估 Aztreonam 作為**耐藥性淋球菌替代療法**具有明確的科學與公衛依據。尤其對產 β-lactamase 的淋球菌（PPNG）株，Aztreonam 能規避酵素水解而保有殺菌活性。早在 1983 年即有臨床資料支持其對淋球菌的療效，2019 年的 Phase 2/3 試驗更專門針對「老藥新用」此一方向進行驗證。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03867734](https://clinicaltrials.gov/study/NCT03867734) | Phase 2/3 | 已完成 | 32 | 評估單劑肌注 Aztreonam 2g 治療咽喉部淋病（AMR *N. gonorrhoeae*）。背景：CDC 緊急耐藥威脅，咽喉部比尿道更難清除，若咽喉有效則尿道炎適應症可延伸推論。樣本數偏小，主要終點清除率待確認。 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | 單臂臨床試驗 | Antimicrob Agents Chemother | 單劑肌注 Aztreonam 2g，評估咽喉部及泌尿生殖道淋球菌清除率，直接驗證「老藥新用」可行性 |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | 臨床試驗 | Antimicrob Agents Chemother | Aztreonam 1g im vs Spectinomycin 2g im 隨機比較：兩組均無治療失敗，尿道、直腸、子宮頸部位均有效 |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | 臨床試驗 | Genitourin Med | 單劑 Aztreonam 1g im 治療 87 例男女患者（多部位），除 1 例咽喉外全數清除，對 penicillin 敏感及耐藥株均有效 |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | 臨床研究 | J Infect Dis | 最早評估 Aztreonam 對 PPNG（產青黴素酶淋球菌）之臨床研究，確認可作為 spectinomycin 耐藥株替代選項 |
| [6438364](https://pubmed.ncbi.nlm.nih.gov/6438364/) | 1984 | 臨床評估 | Jpn J Antibiot | 30 例男性淋菌性尿道炎接受 Aztreonam 治療，PPNG（15%）及非 PPNG 株均有效，細菌學與臨床雙重評估 |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | 前瞻性研究 | Acta Urol Jpn | 244 株臨床分離株含 17.2% PPNG，Aztreonam 單次注射治療淋球菌感染之療效與流行病學分析 |
| [6226596](https://pubmed.ncbi.nlm.nih.gov/6226596/) | 1983 | 臨床研究 | G Ital Dermatol Venereol | 急性淋菌性尿道炎患者使用 Aztreonam 之早期臨床報告 |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | 耐藥監測 | J Infect Chemother | ⚠️ 警示性文獻：首例不產 β-lactamase 但對 cephem 及 aztreonam 高度耐藥之淋球菌株，提示持續耐藥監測的必要性 |

---

## 其他預測適應症摘要

| 排名 | 適應症 | 分數 | 證據等級 | 建議 | 評語 |
|------|--------|------|---------|------|------|
| 1 | Polyclonal hyperviscosity syndrome | 99.73% | L5 | Hold | 免疫球蛋白血液流變學異常，抗生素無直接治療機轉 |
| 2 | Hyperamylasemia | 99.73% | L5 | Hold | 高澱粉酶血症為功能性指標，無降酶機轉 |
| 3 | Congenital analbuminemia | 99.69% | L5 | Hold | 遺傳性白蛋白合成缺陷，抗生素完全無效 |
| **4** | **Gonococcal urethritis** | **99.59%** | **L2** | **Proceed with Guardrails** | **本報告主要評估對象，機轉合理、實證最充分** |
| 5 | Ureaplasma urethritis | 99.59% | L5 | Hold | ⛔ 明確機轉偽陽性：Ureaplasma 無細胞壁，天然耐藥所有 β-lactam |
| 6 | Blood group incompatibility | 99.59% | L5 | Hold | 免疫介導反應，文獻（PMID 34956120）屬完全不相關噪音 |
| 7 | Premalignant hematological disease | 99.54% | L5 | Hold | 異常造血克隆增生，抗生素無腫瘤治療機轉 |
| 8 | Epiglottitis | 99.53% | L4 | 研究問題 | 有機轉基礎（Hib 為革蘭氏陰性菌），僅案例系列，疫苗普及後臨床需求已大幅縮減 |
| 9 | Monoclonal gammopathy | 99.50% | L5 | Hold | 文獻（PMID 4079014）描述的是血液惡性病患者的伴隨感染治療，非治療單株免疫球蛋白病 |
| 10 | Xanthogranulomatous pyelonephritis | 99.49% | L5 | Hold | 有機轉基礎但外科手術為主要治療，零臨床文獻支持 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：目前 Evidence Pack 中 Aztreonam 的 TFDA/衛生署仿單警語、禁忌症及藥物交互作用資料均尚未取得（Data Gap），正式評估前需補充完整安全性資訊。

---

## 結論與下一步

**決策：Proceed with Guardrails（針對淋菌性尿道炎）**

**理由：**
Aztreonam 對淋病奈瑟菌具有直接且機轉明確的抗菌活性（PBP-3 結合抑制細胞壁合成），在全球抗生素耐藥危機背景下，作為 PPNG 株及頭孢耐藥淋球菌的替代療法具有強烈的臨床需求。已完成的 Phase 2/3 試驗（NCT03867734）加上從 1983 年延伸至 2020 年的 8 篇臨床文獻，達到 L2 證據等級，理由充分。

**若要推進需要：**

- 📋 **取得 NCT03867734 詳細結果**：確認咽喉部淋球菌清除率主要終點數據，評估是否達標
- 🔬 **補充完整 MOA 資料**：從 DrugBank API 或原廠資料取得完整作用機轉說明（現為 Data Gap）
- 📄 **補充安全性仿單**：取得 TFDA/原廠仿單警語、禁忌症及 DDI 資料（現為 Blocking Data Gap）
- 🇭🇰 **評估香港引入路徑**：Aztreonam 在香港目前未上市（0 張許可證），需評估特殊藥品進口申請或新許可證申請可行性
- 🦠 **香港本地耐藥監測**：取得香港淋球菌抗生素耐藥性（GASP-HK）最新數據，確認本地 PPNG 及頭孢耐藥盛行率，評估實際臨床需求規模
- ⚠️ **明確排除偽陽性預測**：Ureaplasma urethritis（排名第 5）為確認的機轉偽陽性，應在後續篩選流程中標記排除
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

