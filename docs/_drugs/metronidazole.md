---
layout: default
title: Metronidazole
parent: 僅模型預測 (L5)
nav_order: 493
evidence_level: L5
indication_count: 10
---

# Metronidazole
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

# Metronidazole：從厭氧菌／原蟲感染用藥到肺囊蟲病 (Pneumocystosis) 老藥新用評估

## 一句話總結

Metronidazole 是硝基咪唑類抗生素，經典用途為厭氧菌與原蟲感染（如阿米巴病、滴蟲病）治療；正式核准適應症清單本評估未取得資料。TxGNN 模型將其與**肺囊蟲病 (Pneumocystosis)** 的預測分數推到 **99.99%**，但比對到的 **23 個臨床試驗**與 **10 篇文獻**經覆核後，均未提供支持此機轉的直接證據，機轉評估判定為**不成立**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無正式核准清單資料；文獻顯示傳統用於厭氧菌／原蟲感染（阿米巴病、滴蟲病等） |
| 預測新適應症 | 肺囊蟲病 (Pneumocystosis) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5（僅模型預測，無支持性研究） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料庫紀錄（DrugBank MOA 為資料缺口）。根據評估資料中反覆出現的描述，Metronidazole 屬於硝基咪唑類抗生素，其硝基官能基在厭氧菌或部分原蟲細胞內被還原後產生具細胞毒性的自由基，破壞病原體 DNA，因而對厭氧菌感染及原蟲感染（如陰道滴蟲病、阿米巴病、梨形鞭毛蟲病）具療效。

TxGNN 模型雖給出 99.99% 的高分，但人工覆核判定此機轉關聯**不成立**：Pneumocystis jirovecii 是真菌類病原體，並非厭氧菌或原蟲，metronidazole 已知的硝基還原殺菌機轉對其無已知活性；肺囊蟲肺炎的標準治療是 TMP-SMX、pentamidine 或 atovaquone，與 metronidazole 作用途徑無關。

比對到的 23 筆臨床試驗主題涵蓋鴉片類藥物治療、糖尿病照護、整合式醫療模式等，與 metronidazole 或 pneumocystosis 均無關聯；文獻證據也多是 HIV 伺機性感染的綜述或個案報告，其中提到 metronidazole 的案例，實際用途是治療病患**併發的阿米巴感染**，而非用於治療肺囊蟲病本身。整體屬於知識圖譜比對雜訊，不構成機轉支持。

## 臨床試驗證據

以下為資料庫檢索比對到的試驗，經相關性複核均判定為「不相關（grade C）」，未發現支持 metronidazole 治療 pneumocystosis 的臨床試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 不相關原因 |
|---------|------|------|------|-----------|
| [NCT02571673](https://clinicaltrials.gov/study/NCT02571673) | N/A | 完成 | 65 | 頭頸癌存活者照護工具可行性研究，與 metronidazole/pneumocystosis 無關 |
| [NCT01909076](https://clinicaltrials.gov/study/NCT01909076) | N/A | 完成 | 53 | 鴉片類藥物風險降低策略，主題不相關 |
| [NCT06160947](https://clinicaltrials.gov/study/NCT06160947) | N/A | 未開始招募 | 24 | 脊椎慢性疼痛徒手治療試驗，主題不相關 |
| [NCT06597123](https://clinicaltrials.gov/study/NCT06597123) | N/A | 未開始招募 | 150 | AI 動機式訪談訓練研究，主題不相關 |
| [NCT03466866](https://clinicaltrials.gov/study/NCT03466866) | Phase 3 | 完成 | 156 | 糖尿病急診就診教育試驗，主題不相關 |
| [NCT03451630](https://clinicaltrials.gov/study/NCT03451630) | N/A | 完成 | 1400 | 整合照護模式研究，主題不相關 |
| [NCT05256303](https://clinicaltrials.gov/study/NCT05256303) | N/A | 完成 | 160 | 農村居家醫院照護試驗，主題不相關 |
| [NCT03542084](https://clinicaltrials.gov/study/NCT03542084) | N/A | 完成 | 305 | 內分泌電子會診研究，主題不相關 |
| [NCT02208947](https://clinicaltrials.gov/study/NCT02208947) | Phase 3 | 終止 | 77 | 預立醫療計畫消費者參與研究，主題不相關 |
| [NCT05892666](https://clinicaltrials.gov/study/NCT05892666) | N/A | 招募中 | 4000 | 價值導向照護比較研究，主題不相關 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1545596](https://pubmed.ncbi.nlm.nih.gov/1545596/) | 1992 | Review | Mayo Clinic Proceedings | 抗寄生蟲藥物綜述，未針對 pneumocystosis 或 metronidazole 療效 |
| [7355683](https://pubmed.ncbi.nlm.nih.gov/7355683/) | 1980 | Review | American Family Physician | 抗原蟲藥物選擇綜述，明示 metronidazole 用於阿米巴/滴蟲病，PCP 首選為 TMP-SMX |
| [1782741](https://pubmed.ncbi.nlm.nih.gov/1782741/) | 1991 | Review | Clinical Pharmacokinetics | 抗原蟲治療藥物動力學綜述（美國觀點），非 pneumocystosis 專論 |
| [26518395](https://pubmed.ncbi.nlm.nih.gov/26518395/) | 2015 | Review | Topics in Antiviral Medicine | HIV 相關伺機性感染現況綜述，未提及 metronidazole 用於 PCP |
| [2996829](https://pubmed.ncbi.nlm.nih.gov/2996829/) | 1985 | Review | Clinical Pharmacy | AIDS 感染併發症治療綜述，PCP 為最常見伺機性感染，但治療藥非 metronidazole |
| [6771863](https://pubmed.ncbi.nlm.nih.gov/6771863/) | 1980 | Review | Reviews of Infectious Diseases | 抗菌預防性投藥文獻回顧，非 pneumocystosis 專論 |
| [2280469](https://pubmed.ncbi.nlm.nih.gov/2280469/) | 1990 | Review | Nihon Rinsho | 抗原蟲藥物綜述（摘要未提供） |
| [6282154](https://pubmed.ncbi.nlm.nih.gov/6282154/) | 1982 | Case Report | Am Review of Respiratory Disease | 健康成人 PCP 合併 CMV 肺炎個案，患者因腹瀉曾服用 metronidazole，非用於治療 PCP |
| [2338506](https://pubmed.ncbi.nlm.nih.gov/2338506/) | 1990 | Case Report | Kansenshogaku Zasshi | 日本 AIDS 個案因阿米巴痢疾併肝膿瘍以 metronidazole 治癒，之後才併發 PCP |
| [16496064](https://pubmed.ncbi.nlm.nih.gov/16496064/) | 2005 | Case Report | J Formosan Medical Association | AIDS 患者 CMV 與阿米巴結腸炎併腸穿孔個案，metronidazole 用於治療阿米巴腸炎而非 PCP |

## 香港上市資訊

目前 Metronidazole 於香港**未有上市許可證**（0 張登記）。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 對 pneumocystosis 的最高分預測經機轉與證據覆核判定不成立：Pneumocystis 為真菌，非 metronidazole 已知作用標的，比對到的臨床試驗與文獻均非直接支持證據，證據等級僅 L5。
- 藥品在香港尚未上市（0 張許可證），且仿單警語／禁忌（DG001，Blocking）尚缺，無法進入 S1 安全性初評。

**若要推進需要：**
- 補齊 TFDA/HK 仿單警語與禁忌資料（DG001，Blocking，來源：TFDA 官網仿單 PDF）
- 補齊 DrugBank 作用機轉資料（DG002，High，來源：DrugBank API）
- 若仍要探索 metronidazole 老藥新用方向，建議轉向本評估中證據等級較高的候選適應症，如 **cap polyposis**（L3，已有機轉假說文獻直接探討）、**ulcerative proctosigmoiditis** 與 **ulceration of vulva**（皆 L4，部分病因子群機轉成立），而非本報告聚焦之 pneumocystosis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

