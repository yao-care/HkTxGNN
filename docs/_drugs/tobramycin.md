---
layout: default
title: Tobramycin
parent: 中證據等級 (L3-L4)
nav_order: 754
evidence_level: L4
indication_count: 5
---

# Tobramycin
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

# TOBRAMYCIN：從細菌感染治療（Aminoglycoside 抗生素）到 Exposure Keratitis（暴露性角膜炎）

## 一句話總結

TOBRAMYCIN 是一種 aminoglycoside 類抗生素，臨床上用於治療綠膿桿菌（Pseudomonas aeruginosa）等革蘭氏陰性菌感染。
TxGNN 模型預測它可能對**Exposure Keratitis（暴露性角膜炎）**有效，
目前僅有 **2 個臨床試驗**（相關性評級皆為 C，間接相關）與 **7 篇文獻**（多為個案報告），證據強度有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無資料（該藥物香港未上市，無許可證登記可供比對） |
| 預測新適應症 | Exposure Keratitis (暴露性角膜炎) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L4 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Research Question（暫緩推進，先釐清機轉合理性） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，TOBRAMYCIN 是 aminoglycoside 類抗生素，
其藥理作用為抑制細菌蛋白質合成，對革蘭氏陰性菌（尤其是綠膿桿菌）具強效殺菌力，
臨床上廣泛用於眼科局部感染（如細菌性結膜炎、角膜炎）。

然而，evidence pack 中對此預測的機轉關聯性分析持保留態度：**Exposure keratitis 本質是眼瞼閉合不全導致的角膜暴露性機械性/物理性損傷，並非感染性疾病**。Tobramycin 至多能作為預防繼發性細菌感染的輔助用藥，與其抗菌機轉並無直接治療暴露性角膜病變的因果關係。

所附文獻也印證了這個保留態度——多數文獻是其他病原體（MRSA、Bacillus cereus、Shewanella algae）引起的**感染性**角膜炎個案，與 exposure keratitis 的疾病定義並不完全對應；另有一篇是 aminoglycoside 對角膜上皮的體外毒性研究，顯示 tobramycin 本身對角膜上皮可能具有一定細胞毒性，需納入風險考量。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05313828](https://clinicaltrials.gov/study/NCT05313828) | N/A | 未知 | 40 | 針對 dendritic ulcer（皰疹性角膜炎，病毒性）之各種治療方式比較，未明確使用 Tobramycin 作為介入（相關性 C） |
| [NCT06200727](https://clinicaltrials.gov/study/NCT06200727) | N/A | 未知 | 170 | 探討 PRF（富血小板纖維蛋白膜）於角膜潰瘍等眼科疾病的應用，未特定針對 Tobramycin 或 exposure keratitis（相關性 C） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2707046](https://pubmed.ncbi.nlm.nih.gov/2707046/) | 1989 | 體外毒性研究 | Current Eye Research | 比較 4 種 aminoglycoside（含 tobramycin）對兔角膜上皮細胞的體外毒性 |
| [12861116](https://pubmed.ncbi.nlm.nih.gov/12861116/) | 2003 | 個案報告 | Eye & Contact Lens | PRK 術後雙側 MRSA 角膜炎個案 |
| [34987857](https://pubmed.ncbi.nlm.nih.gov/34987857/) | 2021 | 個案報告 | Oxford Medical Case Reports | 無海洋暴露史之多重抗藥性 Shewanella algae 細菌性角膜炎個案 |
| [11581057](https://pubmed.ncbi.nlm.nih.gov/11581057/) | 2001 | 個案報告 | Ophthalmology | 隱形眼鏡相關 Bacillus cereus 角膜炎首例報告 |
| [17228760](https://pubmed.ncbi.nlm.nih.gov/17228760/) | 2006 | 未分類 | Nippon Ganka Gakkai Zasshi | 日本全國感染性角膜炎監測中，各抗生素眼藥水之 MIC 與後抗生素效應比較 |
| [14574976](https://pubmed.ncbi.nlm.nih.gov/14574976/) | 2003 | 未分類 | Yan Ke Xue Bao (Eye Science) | Graves 眼病所致 paracentral corneal dellen 個案（與感染無關） |
| [33847093](https://pubmed.ncbi.nlm.nih.gov/33847093/) | 2021 | 未分類 | Polish Journal of Veterinary Sciences | 貓弓形蟲眼疾之血清盛行率與治療結果分析（動物研究，非人類適應症） |

---

## 香港上市資訊

目前無香港許可證登記資料，該藥物尚未於香港上市。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：Evidence Pack 標記兩項 Blocking/High 等級資料缺口——TFDA 仿單警語/禁忌（DG001，Blocking，影響是否可進入 S1 安全性初評）與作用機轉資料（DG002，High，影響機轉關聯性分析）。這兩項尚未補齊。

---

## 結論與下一步

**決策：Research Question（暫緩推進，列為研究問題）**

**理由：**
- 機轉關聯性薄弱：exposure keratitis 本質為機械性角膜暴露損傷，非感染性疾病，抗生素僅能作為輔助預防用藥，難以直接解釋 TxGNN 高分。
- 現有臨床試驗相關性評級皆為 C（間接相關），文獻證據以個案報告與體外研究為主，證據等級僅達 L4。
- 安全性（TFDA/仿單警語禁忌）與詳細 MOA 資料皆為 Blocking/High 等級缺口，尚未補齊，無法進入 S1 安全性初評。

**若要推進需要：**
- 補齊 TOBRAMYCIN 仿單警語與禁忌資料（DG001）
- 補齊 DrugBank 作用機轉資料（DG002）
- 針對「exposure keratitis 併發細菌感染時輔助抗生素治療」設計具體臨床研究問題，而非直接視為新適應症候選

> 補充觀察：同一 Evidence Pack 中，Tobramycin 對 **otitis externa（外耳道炎，尤其壞死性外耳道炎）** 之預測證據等級達 L3、決策階段 S3（Proceed with Guardrails），且有多篇長期高劑量安全性文獻支持，機轉上（對綠膿桿菌強效殺菌）已是臨床既有用法，證據品質明顯優於本報告之 exposure keratitis 候選，建議後續可另行評估該適應症。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

