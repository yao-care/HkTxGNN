---
layout: default
title: Ramipril
parent: 僅模型預測 (L5)
nav_order: 630
evidence_level: L5
indication_count: 5
---

# Ramipril
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ramipril：從（未提供原適應症）到缺氧/肺病相關肺動脈高壓

## 一句話總結

Ramipril（DrugBank ID: DB00178）目前的證據包未提供香港上市許可證或原適應症資料。TxGNN 模型預測它可能對**缺氧/肺病相關肺動脈高壓（Pulmonary Hypertension owing to Lung Disease and/or Hypoxia）**有效，雖然檢索到 **20 篇文獻**，但經核對後皆為與「hypoxia」關鍵字命中的一般缺氧生物學研究，**未有一篇直接涉及 ramipril 或此適應症**，證據強度極低。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無許可證資料（香港未上市，許可證數為 0） |
| 預測新適應症 | 缺氧/肺病相關肺動脈高壓 (Pulmonary Hypertension owing to Lung Disease and/or Hypoxia) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5（僅模型預測，文獻為關鍵字誤配） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為資料缺口）。根據一般藥理分類知識，Ramipril 屬 ACE 抑制劑類藥物，主要透過抑制腎素-血管收縮素-醛固酮系統（RAAS）發揮作用。

證據包中的機轉假說提出：RAAS 抑制理論上可能影響缺氧性肺血管收縮，因而與肺動脈高壓存在間接機轉關聯性假說。

然而，這僅是理論推測。提供的 20 篇文獻經查核，皆為以「hypoxia」關鍵字命中的一般缺氧生物學研究（涵蓋腦老化、胃癌代謝、多發性硬化症等主題），**沒有一篇實際研究 ramipril、ACE 抑制劑或肺動脈高壓治療**，屬於檢索關鍵字誤配，不構成直接或間接的臨床證據支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33862277](https://pubmed.ncbi.nlm.nih.gov/33862277/) | 2021 | Review | Ageing Research Reviews | 缺氧與腦老化、神經退化性疾病關聯之綜述 |
| [34618295](https://pubmed.ncbi.nlm.nih.gov/34618295/) | 2022 | Review | Metabolic Brain Disease | 缺氧導致認知功能障礙的分子機轉 |
| [21328446](https://pubmed.ncbi.nlm.nih.gov/21328446/) | 2011 | Review | J Cellular Biochemistry | 缺氧調控生物學功能之綜述 |
| [31706510](https://pubmed.ncbi.nlm.nih.gov/31706510/) | 2019 | Review | Trends in Cancer | 去泛素化酶（DUBs）與缺氧、癌症之關聯 |
| [34535359](https://pubmed.ncbi.nlm.nih.gov/34535359/) | 2021 | Review | Clinical Oncology | 缺氧的治療性調節（放療抗性） |
| [11172576](https://pubmed.ncbi.nlm.nih.gov/11172576/) | 2000 | Review | Respiratory Care Clinics | 低血氧症的機轉綜述 |
| [40347693](https://pubmed.ncbi.nlm.nih.gov/40347693/) | 2025 | Review | Redox Biology | 缺氧與多發性硬化症之關聯 |
| [40815459](https://pubmed.ncbi.nlm.nih.gov/40815459/) | 2025 | Review | Rev Med Inst Mex Seguro Soc | 高海拔缺氧生理學 |
| [37328448](https://pubmed.ncbi.nlm.nih.gov/37328448/) | 2023 | Basic Research | Advanced Science | 胃癌細胞在缺氧下的醣解代謝機轉 |
| [33278780](https://pubmed.ncbi.nlm.nih.gov/33278780/) | 2021 | Basic Research | Redox Biology | 蟹足腫纖維母細胞在缺氧下的代謝改變 |

> **重要提醒**：以上文獻皆為「hypoxia」關鍵字命中的一般缺氧生物學研究，主題涵蓋神經退化、腫瘤代謝、皮膚疾病等，**沒有一篇涉及 ramipril、ACE 抑制劑或肺動脈高壓治療**，屬檢索關鍵字誤配，不應視為支持本項預測的臨床證據。

## 安全性考量

安全性資訊為資料缺口（Blocking 等級）：TFDA/香港官方仿單警語、禁忌症、藥物交互作用皆未取得，導致**無法進入 S1 安全性初評階段**。建議推進前必須先取得官方仿單資料。

## 結論與下一步

**決策：Hold**

**理由：**
- 提供的 20 篇文獻經核對後皆與 ramipril、ACE 抑制劑或肺動脈高壓無直接關聯，屬關鍵字誤配，不構成可評估證據，證據等級僅為 L5。
- 安全性仿單資料缺失屬 Blocking 等級缺口，無法進行安全性初評。
- 其餘 4 個預測適應症（肺動脈高壓其他分型、惡性高血壓腎病、惡性腎血管性高血壓、Braddock 症候群）皆無任何文獻或試驗佐證，同為 L5，暫不評估。

**若要推進需要：**
- 取得 TFDA/香港官方仿單，補齊警語與禁忌症資料（Blocking，優先處理）
- 查詢 DrugBank API 補齊作用機轉（MOA）資料
- 針對「ramipril + 肺動脈高壓」重新執行精準文獻與臨床試驗檢索，排除關鍵字誤配結果
- 若欲評估香港上市可行性，需另行查證許可證登記狀態
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

