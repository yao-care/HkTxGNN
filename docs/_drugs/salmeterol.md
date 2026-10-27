---
layout: default
title: Salmeterol
parent: 高證據等級 (L1-L2)
nav_order: 800
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Salmeterol：預測新適應症為支氣管炎 (Bronchitis)（證據等級 L1）。原適應症：肺氣腫、內因性氣喘、過敏性氣喘"
monitor_inn: "SALMETEROL"
predicted_indications: ["bronchitis", "respiratory malformation", "obstructive lung disease", "Rienhoff syndrome"]
---

# Salmeterol
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Salmeterol：從肺氣腫與氣喘到支氣管炎
{: .text-alpha }

## 一句話總結

Salmeterol 是長效 β2 腎上腺素受體促效劑（LABA），原本用於肺氣腫、內因性氣喘與過敏性氣喘。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，
目前有 **9 個臨床試驗**和 **20 篇文獻**支持這個方向。
不過支氣管炎與原適應症同屬慢性阻塞性肺病（COPD）家族，較接近原用途的延伸，而非全新的再利用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺氣腫、內因性氣喘、過敏性氣喘（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 15 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫未收錄）。根據已知資訊，Salmeterol 是長效 β2 受體促效劑，可放鬆氣道平滑肌、緩解氣流受限。慢性支氣管炎屬 COPD 的一種表型，在肺氣腫與氣喘中已證實的支氣管擴張作用，機轉上可適用於支氣管炎。

有一項研究（PMID 15970448）顯示，Salmeterol 在輕至中度慢性支氣管炎患者中，可能改善黏液纖毛清除與咳嗽清除。此外，市售的 salmeterol/fluticasone 複方已被用於 COPD，涵蓋慢性支氣管炎族群。

整體而言，這是同一疾病家族內的延伸。TxGNN 分數很高，但應理解為與既有適應症高度重疊，不是全新的作用機轉發現。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Phase 3 | 完成 | 130 | Salmeterol/Fluticasone 50/500 對比安慰劑，評估 COPD 患者的支氣管抗發炎作用 |
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Phase 3 | 完成 | 584 | Tiotropium、Salmeterol 氣霧劑與安慰劑的六個月 COPD 療效與安全性比較 |
| [NCT00269087](https://clinicaltrials.gov/study/NCT00269087) | Phase 3 | 完成 | 122 | Salmeterol/Fluticasone 50/500 用於 COPD（慢性支氣管炎、肺氣腫）的 56 週長期安全性 |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Phase 3 | 完成 | 741 | Arformoterol 對比安慰劑與活性對照，用於 COPD（Salmeterol 可能為活性對照，屬間接證據） |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | 完成 | 799 | Arformoterol 12 個月 COPD 長期安全性研究（間接證據） |
| [NCT00269126](https://clinicaltrials.gov/study/NCT00269126) | Phase 3 | 完成 | 150 | 比較兩種藥物對 COPD 的效果，詳情無法確認 |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Phase 2 | 完成 | 457 | Fluticasone/Formoterol 劑量探索，以 Advair（含 Salmeterol）為參考（間接證據） |
| [NCT01361984](https://clinicaltrials.gov/study/NCT01361984) | Phase 4 | 未知 | 20 | 噴霧 Arformoterol 與 Serevent 乾粉吸入劑在 COPD 的比較 |
| [NCT00233051](https://clinicaltrials.gov/study/NCT00233051) | NA | 終止 | 20 | 誘發痰液發炎介質基因表現作為 COPD 藥物反應生物標記，療效價值有限 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | RCT／臨床生理 | Pulm Pharmacol Ther | Salmeterol 對慢性支氣管炎患者（n=14）黏液纖毛與咳嗽清除的急性效果 |
| [17557771](https://pubmed.ncbi.nlm.nih.gov/17557771/) | 2007 | RCT | Thorax | Salmeterol/Fluticasone 對 COPD 氣道發炎的影響 |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | 臨床試驗 | Chest | Fluticasone 250/Salmeterol 50 Diskus 用於 COPD 的療效與安全性 |
| [17196106](https://pubmed.ncbi.nlm.nih.gov/17196106/) | 2006 | 統合分析 | Respir Res | Salmeterol 相較安慰劑／常規治療，改善 COPD 臨床結果 |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | 臨床試驗 | Ther Adv Respir Dis | Arformoterol 與 Salmeterol 在 COPD 的一年安全性與耐受性 |
| [15329047](https://pubmed.ncbi.nlm.nih.gov/15329047/) | 2004 | Review | Drugs | 吸入型 Salmeterol/Fluticasone 用於 COPD 的回顧 |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | 世代研究 | Curr Med Res Opin | 慢性支氣管炎患者起始 Fluticasone/Salmeterol 與其他維持治療的醫療利用及費用比較 |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | 開放性研究 | Clin Ther | 吸入 Salmeterol 與口服茶鹼用於輕中度 COPD 的療效、耐受性與生活品質 |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | 指引 | Basic Clin Pharmacol Toxicol | 芬蘭穩定期 COPD 診斷與藥物治療指引 |
| [12236842](https://pubmed.ncbi.nlm.nih.gov/12236842/) | 2002 | Review | Br J Clin Pharmacol | 長效 β2 促效劑拮抗現象的藥理回顧 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-35936 | SEREVENT INHALER 25MCG/ACTUATION | 吸入劑 | 詳見原廠仿單 |
| HK-48128 | SERETIDE INHALER 25/50 | 吸入劑 | 詳見原廠仿單 |
| HK-44735 | SERETIDE ACCUHALER 50MCG/250MCG | 吸入劑 | 詳見原廠仿單 |
| HK-51376 | SEROFLO 125 INHALER | 吸入劑 | 詳見原廠仿單 |
| HK-65890 | SIRDUPLA PRESSURISED INHALATION SUSPENSION 25MCG/250MCG | 吸入懸浮液 | 詳見原廠仿單 |

（共 15 張有效許可證，皆為單一成分登記，無已註銷者；以上僅列 5 張主要許可證。劑型欄位依品名判斷。）

## 安全性考量

- **藥物交互作用**：共記錄 100 筆交互作用，其中重要者：
  - **Major**：Clarithromycin（強效 CYP3A4 抑制劑，需特別留意）
  - **Moderate**：Epinephrine、Famotidine、Isometheptene，以及多種降血糖藥物（如 Acarbose、Alogliptin、Canagliflozin、Dapagliflozin、Empagliflozin、Dulaglutide、Albiglutide、Chlorpropamide），另有 Diethylpropion、Dolasetron
  - **Minor**：多種皮質類固醇（Hydrocortisone、Dexamethasone、Budesonide 等）
- **知識圖譜標示的疾病禁忌（非仿單內容）**：高血壓、長 QT 症候群、癲癇、高血糖、骨質疏鬆等。
- **類別層級的警語**：文獻（Cochrane 系統性回顧，PMID 30521673、23543548）指出，氣喘患者單獨規律使用 LABA 與嚴重不良事件風險增加有關，應與吸入型皮質類固醇併用。

香港仿單的警語與禁忌資料尚未取得，正式使用前請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 多個已完成的 Phase 3 試驗（如 NCT00268177、NCT02173691、NCT00269087）在 COPD／慢性支氣管炎族群中直接測試 Salmeterol 或其複方，且 Salmeterol 複方已在香港上市。
- 但此適應症與原適應症高度重疊，屬疾病家族內延伸；且香港仿單安全性資料仍缺漏。

**若要推進需要：**
- 取得並解析香港衛生署核准仿單的警語、禁忌與核准適應症文字
- 補充詳細作用機轉（MOA）資料
- 訂定安全使用防護：LABA 不單獨用於氣喘、併用強效 CYP3A4 抑制劑（如 Clarithromycin）的管理，以及心血管（QT 延長、高血壓）監測
- 釐清「慢性支氣管炎」與「COPD」在實際核准適應症中的涵蓋範圍

*附註：模型預測排名較後的「呼吸道畸形」與「Rienhoff 症候群」缺乏機轉與臨床證據支持，建議 Hold，不在本報告推進範圍內。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

