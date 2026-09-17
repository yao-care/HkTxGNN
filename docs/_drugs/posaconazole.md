---
layout: default
title: Posaconazole
parent: 中證據等級 (L3-L4)
nav_order: 601
evidence_level: L4
indication_count: 1
---

# Posaconazole
{: .fs-9 }

證據等級: **L4** | 預測適應症: **1** 個
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

# Posaconazole：從侵襲性黴菌感染預防到肺囊蟲病

## 一句話總結

Posaconazole 是廣譜三唑類抗黴菌藥，原本用於高風險族群（如異體移植患者）的侵襲性麴菌病、念珠菌病等黴菌感染預防。
TxGNN 模型預測它可能對**肺囊蟲病 (Pneumocystosis)** 有效，
目前有 **2 個臨床試驗**（相關性均低）和 **5 篇文獻**（均為背景性回顧/佇列研究）支持這個方向，證據仍屬初步。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 侵襲性黴菌感染預防（麴菌病、念珠菌病等，依機轉論述推論） |
| 預測新適應症 | 肺囊蟲病 (Pneumocystosis) |
| TxGNN 預測分數 | 99.77% |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Posaconazole 透過抑制真菌 CYP51（lanosterol 14α-demethylase）阻斷 ergosterol 合成，是廣譜三唑類抗黴菌藥，臨床上已用於異體移植等高風險免疫低下族群，預防侵襲性麴菌病與念珠菌病。

原適應症與肺囊蟲病的病人族群高度重疊——兩者都好發於免疫低下、骨髓/器官移植患者，這也是 TxGNN 模型捕捉到關聯性的可能原因。

但機轉上有一項已知限制：*Pneumocystis jirovecii* 的細胞膜主要以宿主來源膽固醇構成，內生 ergosterol 合成量極低，這正是傳統三唑類藥物（如 fluconazole、itraconazole）對肺囊蟲病活性受限的已知原因。Posaconazole 是否能克服此限制缺乏直接藥理證據；目前臨床上對肺囊蟲病的「效果」多來自「移植病人已用於黴菌預防、順帶覆蓋 Pneumocystis」的間接推論，而非針對性治療/預防試驗設計，這也是本預測證據等級僅達 L4 的主因。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Phase 3 | 進行中（未招募） | 602 | ReSPECT 研究：比較 IV Rezafungin 與標準抗微生物療法用於異體移植病人侵襲性黴菌病預防；**主體藥物為 Rezafungin 非 posaconazole**，相關性低（Grade C），僅供背景參考 |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | 招募中 | 358 | 比較不同藥物組合預防異體周邊血幹細胞移植後 GVHD；可能涵蓋抗黴菌預防用藥但非以肺囊蟲病療效為主要終點，屬間接族群重疊（Grade C） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2025 | Review | The Lancet Infectious Diseases | 英國醫學真菌學會更新嚴重真菌病診斷最佳實務建議 |
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Review | Swiss Medical Weekly | 侵襲性念珠菌病、麴菌病、隱球菌病與肺囊蟲肺炎總覽，提及 posaconazole 抗黴菌預防已顯著降低高風險血液腫瘤病人侵襲性念珠菌病發生率 |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Review | 中華結核和呼吸雜誌 | 侵襲性肺部真菌病診療指引（2025版），聚焦非免疫抑制族群 |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Cohort | Transplant Infectious Disease | 肝臟移植後急性 GVHD 病人感染併發症回顧性佇列研究 |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | PK/PD Study | Clinical Pharmacokinetics | 抗黴菌等抗感染藥物於肺上皮襯液（ELF）之穿透性研究 |

---

## 香港上市資訊

目前 Posaconazole 尚未在香港上市，無許可證資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 現有臨床試驗相關性均為 Grade C（背景參考），且主要文獻皆為回顧性/機轉性質，缺乏針對肺囊蟲病的前瞻性直接證據，證據等級僅達 L4。
- 機轉上 Pneumocystis jirovecii 對三唑類藥物的已知抗性缺口尚未被排除，需更多藥理證據才能支持機轉合理性。

**若要推進需要：**
- 取得 TFDA/原廠仿單警語與禁忌資料（現為 Blocking 缺口，無法完成 S1 安全性初評）
- 補充 Posaconazole 完整作用機轉資料，釐清對 Pneumocystis ergosterol 合成路徑的實際抑制效果
- 針對肺囊蟲病設計的前瞻性藥理或臨床研究（目前僅有間接族群重疊證據）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

