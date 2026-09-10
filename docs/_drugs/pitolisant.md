---
layout: default
title: Pitolisant
parent: 僅模型預測 (L5)
nav_order: 594
evidence_level: L5
indication_count: 3
---

# Pitolisant
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

# Pitolisant：從猝睡症到失眠、ADHD 等候選新適應症（多重候選，證據品質分歧）

## 一句話總結

Pitolisant（DB11642）目前未在香港上市，原廠仿單與正式作用機轉（MOA）資料皆缺失。
TxGNN 模型針對此藥產出 3 個新適應症候選——**失眠 (Insomnia)**、**注意力不足過動症 (ADHD)**、**Aarskog 症候群 (Faciodigitogenital syndrome)**，
但三者證據品質差異極大：失眠候選經機轉檢視後判定**方向矛盾、疑似偽陽性**，ADHD 候選有機轉合理性但**零人體試驗**，Aarskog 候選則**完全無支持證據**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 正式資料缺失（未上市；文獻脈絡顯示核准適應症為猝睡症 Narcolepsy，非正式來源） |
| 候選新適應症 1 | Insomnia（失眠）— TxGNN 99.71%，證據等級 L5，**Hold** |
| 候選新適應症 2 | ADHD（注意力不足過動症）— TxGNN 99.36%，證據等級 L4，**Research Question** |
| 候選新適應症 3 | Faciodigitogenital syndrome（Aarskog 症候群）— TxGNN 99.29%，證據等級 L5，**Hold** |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold**（三項候選均不建議推進至下一階段） |

---

## 為什麼這個預測合理？

目前缺乏正式的作用機轉（MOA）資料庫欄位。根據 Evidence Pack 中多篇文獻摘要可知，
Pitolisant 是選擇性 **組織胺 H3 受體反向致效劑/拮抗劑**，藥理上會**促進覺醒**（增加大腦皮質區組織胺、多巴胺、正腎上腺素釋放），
在歐美已核准用於猝睡症（narcolepsy）及 OSA 患者殘餘白日嗜睡（EDS）的治療。

**候選 1（失眠）— 機轉方向矛盾：** Pitolisant 的藥理效果是「促醒」而非「誘導睡眠」，與失眠治療所需的鎮靜/助眠機轉方向相反。
唯一連結的臨床試驗（NCT02800083）實際上是酒精使用障礙（Alcohol Use Disorder）研究，已 **WITHDRAWN**、招募人數 0，標題被截斷，
高度懷疑是資料庫將此試驗誤連結到 insomnia 節點，而非真正的失眠試驗。此候選應視為知識圖譜對「睡眠障礙」大類的偽陽性高分。

**候選 2（ADHD）— 機轉上具合理性但無臨床驗證：** 阻斷突觸前 H3 自體受體可增加皮質區組織胺、多巴胺與正腎上腺素，
理論上可改善注意力與認知功能，與 ADHD 病理生理有合理連結。但目前僅有機轉層級的回顧文獻，
無任何 ADHD 人體臨床試驗資料（試驗數 = 0），無法排除「促醒/警覺度提升」與「ADHD 核心症狀改善」之間的落差。

**候選 3（Aarskog 症候群）— 無可辨識關聯：** 此病為 FGD1 基因相關的先天性骨骼/泌尿生殖發育疾患，
與 pitolisant 的組織胺 H3 受體調節機轉無已知病理生理連結，純屬模型預測分數，無任何支持性資料（0 試驗、0 文獻）。

---

## 臨床試驗證據

**候選 1：Insomnia**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Phase 2 | WITHDRAWN | 0 | 標題實為「酒精使用障礙」試驗（Alcohol Use Disorder Treatment），已終止、零招募，疑似資料連結錯誤，不構成失眠療效證據 |

**候選 2：ADHD** — 目前無相關臨床試驗登記

**候選 3：Aarskog 症候群** — 目前無相關臨床試驗登記

---

## 文獻證據

**候選 1：Insomnia**（8 篇，主題均為猝睡症/OSA 嗜睡治療，非失眠）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT | Lancet Neurology | 兒童猝睡症患者使用 pitolisant 之安全性與療效（3 期試驗） |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | Pitolisant 用於 CPAP 治療下仍殘餘白日嗜睡的 OSA 患者 |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | Pitolisant 用於拒絕 CPAP 治療的 OSA 白日嗜睡患者 |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Cohort | Revista de neurologia | 真實世界研究：pitolisant 用於對先前治療無反應的第一型猝睡症 |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Current Neuropharmacology | 組織胺系統變化與神經精神疾病治療潛力 |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Des Devel Ther | Pitolisant 於猝睡症治療中的定位 |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handbook Clin Neurol | 組織胺受體與致效/拮抗劑於健康與疾病中的角色 |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Review | Clin Neuropharmacol | Pitolisant 作為青少年難治性嗜睡猝睡症的替代刺激藥物 |

**候選 2：ADHD**（7 篇，均為機轉層級回顧，無臨床試驗）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32882898](https://pubmed.ncbi.nlm.nih.gov/32882898/) | 2020 | Review | Medicines (Basel) | H3 受體拮抗劑於認知增強之治療潛力更新 |
| [27363923](https://pubmed.ncbi.nlm.nih.gov/27363923/) | 2016 | Review | Behav Brain Res | H3 受體作為神經精神疾病認知症狀的潛在標的 |
| [30359639](https://pubmed.ncbi.nlm.nih.gov/30359639/) | 2019 | Review | Neuropharmacology | H3 受體拮抗劑於 ADHD 等疾病之受體動力學比較 |
| [21615387](https://pubmed.ncbi.nlm.nih.gov/21615387/) | 2011 | Review | Br J Pharmacol | H3 受體從發現到 pitolisant 臨床試驗之歷程 |
| [24122734](https://pubmed.ncbi.nlm.nih.gov/24122734/) | 2013 | Review | Drugs | 猝睡症藥物治療現況與新興選項 |
| [34534876](https://pubmed.ncbi.nlm.nih.gov/34534876/) | 2021 | Review | Epilepsy Behav | 癲癇合併白日嗜睡患者的藥物治療（含 ADHD 共病討論） |
| [20716022](https://pubmed.ncbi.nlm.nih.gov/20716022/) | 2010 | Review | Expert Opin Ther Pat | H3 受體拮抗劑/反向致效劑近期進展 |

**候選 3：Aarskog 症候群** — 目前無相關文獻

---

## 香港上市資訊

目前無許可證登記（未上市，0 張）。

---

## 安全性考量

安全性資料存在阻斷性缺口（DG001，Blocking）：TFDA/HK 仿單警語與禁忌症尚未取得，
無法完成 S1 安全性初評。安全性資訊請參考原廠仿單（EU/US 核准版本）。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名最高的失眠候選經機轉檢視後判定方向矛盾（促醒藥物 vs. 助眠需求），且唯一連結試驗疑似資料誤連結，證據等級僅 L5。
- ADHD 候選雖有機轉合理性，但零人體試驗支持，證據等級 L4，僅適合列為研究假說（Research Question），非推進候選。
- Aarskog 症候群候選無任何機轉或實證關聯，純屬模型雜訊。
- 安全性資料（DG001）為阻斷級缺口，即使候選證據充分，現階段也無法進入 S1。

**若要推進需要：**
- 補齊 TFDA/HK 仿單之警語、禁忌症、DDI 資料（解除 DG001 阻斷）
- 向 DrugBank 或原廠查證正式 MOA 資料（解除 DG002）
- 查核 NCT02800083 是否為資料庫連結錯誤，確認失眠適應症是否有其他真實試驗支持
- 若欲推進 ADHD 方向，需先有前臨床或早期人體概念驗證（proof-of-concept）試驗資料
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

