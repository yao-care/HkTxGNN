---
layout: default
title: Lanadelumab
parent: 僅模型預測 (L5)
nav_order: 433
evidence_level: L5
indication_count: 10
---

# Lanadelumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Lanadelumab：從遺傳性血管性水腫（HAE）預防到 C1 抑制因子缺乏症

## 一句話總結

Lanadelumab（Takhzyro®）是一種人類單株抗體，用於預防遺傳性血管性水腫（HAE）發作。
TxGNN 模型預測其對**C1 抑制因子缺乏症（C1 Inhibitor Deficiency）**有效——
但這其實正是 HAE 的病因分型，兩者高度重疊。目前有 **22 個臨床試驗**和 **20 篇文獻**支持，
其中已包含 1 個完成的 Phase 3 隨機對照試驗（HELP Study）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 遺傳性血管性水腫（HAE）發作預防（此為藥品的全球已知用途，非源自本地許可證資料——見下方說明） |
| 預測新適應症 | C1 抑制因子缺乏症（C1 Inhibitor Deficiency） |
| TxGNN 預測分數 | 99.996%（模型排名第 198） |
| 證據等級 | L2（1 個完成的 Phase 3 RCT：NCT02586805） |
| 本地上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

作用機轉部分本地資料缺乏（`original_moa` 為 Data Gap），但根據收集到的文獻摘要（PMID 30267321），
Lanadelumab 是全人源單株抗體，標靶抑制血漿激肽釋放酶（plasma kallikrein）。SERPING1 基因突變會導致
C1 抑制因子（C1-INH）缺乏或功能異常，使激肽釋放酶活性失控，進而過度產生緩激肽（bradykinin，一種血管
擴張物質），被認為是血管性水腫症狀的成因。

值得特別說明的是：TxGNN 預測的「新適應症」C1 inhibitor deficiency，實際上就是 HAE Type I/II 的病因學分型，
與 Lanadelumab 目前全球已核准的適應症（HAE 發作預防）幾乎是同一疾病實體。因此本案與其說是「老藥新用」，
更接近「已知全球核准用途的證據彙整」——TxGNN 在此正確識別出藥物與其真實作用族群的強關聯，可視為模型
準確性的驗證案例，而非全新的機轉外推。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02586805](https://clinicaltrials.gov/study/NCT02586805) | Phase 3 | 完成 | 125 | HELP Study：隨機雙盲安慰劑對照，評估 DX-2930（lanadelumab）長期預防 HAE 急性發作之療效與安全性 |
| [NCT02741596](https://clinicaltrials.gov/study/NCT02741596) | Phase 3 | 完成 | 212 | HELP Study Extension：開放標籤長期安全性與療效追蹤 |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Phase 3 | 完成 | 12 | 日本受試者中評估 lanadelumab 療效與安全性 |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Phase 3 | 完成 | 20 | 中國受試者中評估安全性、藥動學與療效，治療 26 週 |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) | Phase 3 | 完成 | 21 | SPRING Study：2 至 <12 歲兒童受試者安全性、藥動學與藥效學評估 |
| [NCT04130191](https://clinicaltrials.gov/study/NCT04130191) | N/A | 完成 | 140 | ENABLE：三年期真實世界研究，比較用藥前後 HAE 發作次數 |
| [NCT03845400](https://clinicaltrials.gov/study/NCT03845400) | N/A | 完成 | 168 | EMPOWER：美加地區觀察性研究，比較用藥前後發作率 |
| [NCT04861090](https://clinicaltrials.gov/study/NCT04861090) | N/A | 完成 | 207 | 回溯性病歷回顧，評估真實世界長期預防治療成效 |
| [NCT05397431](https://clinicaltrials.gov/study/NCT05397431) | N/A | 完成 | 155 | 日本上市後使用調查，長期投藥之副作用與症狀改善追蹤 |
| [NCT06346899](https://clinicaltrials.gov/study/NCT06346899) | N/A | 完成 | 115 | 中國真實世界研究：lanadelumab 與 icatibant 治療 HAE 之有效性與安全性 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab 對比安慰劑之隨機臨床試驗，證實可顯著預防 HAE 發作（HELP Study） |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | 延伸研究 | Allergy | HELP OLE 研究：評估 lanadelumab 長期療效與安全性 |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Meta分析 | Drugs in R&D | 網絡統合分析比較 lanadelumab 與 garadacimab、C1INH、berotralstat 等長期預防藥物 |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | 系統性回顧 | Clin Rev Allergy Immunol | 系統性回顧接受長期預防治療患者仍發生 HAE 發作之特徵 |
| [30539362](https://pubmed.ncbi.nlm.nih.gov/30539362/) | 2019 | Review | BioDrugs | 回顧 lanadelumab 於 C1-INH 缺乏症之臨床前與 Phase I 研究 |
| [32187470](https://pubmed.ncbi.nlm.nih.gov/32187470/) | 2020 | Review | NEJM | 遺傳性血管性水腫之整體疾病回顧 |
| [30267321](https://pubmed.ncbi.nlm.nih.gov/30267321/) | 2018 | Review | Drugs | Lanadelumab 全球首次核准回顧，含機轉說明 |
| [39701274](https://pubmed.ncbi.nlm.nih.gov/39701274/) | 2025 | 真實世界研究 | J Allergy Clin Immunol Pract | 多國 INTEGRATED 研究：lanadelumab 真實世界有效性 |
| [37898409](https://pubmed.ncbi.nlm.nih.gov/37898409/) | 2024 | Review | J Allergy Clin Immunol | 亞太地區 C1-INH 缺乏症 HAE 疾病負擔回顧 |
| [35079346](https://pubmed.ncbi.nlm.nih.gov/35079346/) | 2022 | Review | Clin Transl Allergy | C1 抑制因子預防治療之臨床考量與指引回顧 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

⚠️ 需特別注意：本評估存在一項 **Blocking 等級資料缺口（DG001）**——TFDA 仿單警語/禁忌症資料缺失，
直接導致**無法進入 S1 安全性初評**，須先取得官方仿單 PDF 並解析後方可補齊。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 療效證據強度已達 L2（1 個完成的 Phase 3 RCT + 大量真實世界研究佐證），但因 DG001（TFDA 仿單警語/禁忌缺失，Blocking 等級）尚無法完成安全性初評，不宜貿然推進。
- 本案實質為「已知全球核准適應症（HAE 預防）」的證據彙整，而非新機轉外推，需與法規團隊確認正確的推進路徑（新藥上市申請 vs. 老藥新用研究）。

**若要推進需要：**
- 取得 TFDA（或本地相當機構）官方仿單，完成警語、禁忌症與 DDI 資料補齊
- 補充 DrugBank MOA 結構化資料（DG002）
- 確認本地藥品上市/引進計畫現況（目前 0 張許可證）
- 釐清此候選案應歸類為「新藥適應症申請」而非典型「老藥新用」研究案
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

