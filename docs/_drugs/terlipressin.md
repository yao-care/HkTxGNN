---
layout: default
title: Terlipressin
parent: 中證據等級 (L3-L4)
nav_order: 736
evidence_level: L3
indication_count: 10
---

# Terlipressin
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

# Terlipressin：從急性食道靜脈曲張出血到門脈相關肺高壓（Portopulmonary Hypertension）

## 一句話總結

> Terlipressin 目前在香港**未取得藥品許可證**，本評估資料中無正式核准適應症紀錄；但從相關臨床試驗的背景描述可知，其現行國際臨床用途為**急性食道靜脈曲張出血**與**肝腎症候群 (hepatorenal syndrome)** 的急性處置。
> TxGNN 模型共提出 10 個預測新適應症，其中多數（含分數最高的「隅角開放性青光眼」）**缺乏任何臨床試驗或文獻支持**，模型自身的機轉分析甚至明確指出「缺乏生物學合理性驗證」。
> 唯一具有實質證據支持的候選適應症是**門脈相關肺高壓（Portopulmonary Hypertension，肝硬化併發肺高壓）**，共有 **4 個相關臨床試驗**（背景關聯性）與 **20 篇文獻**（多為小型觀察性研究），故本報告以此為主要評估對象。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無香港許可證資料（未上市）；依臨床試驗背景描述，現行用途為急性食道靜脈曲張出血、肝腎症候群 |
| 預測新適應症 | 肺動脈高壓 (Pulmonary Hypertension)，證據集中於門脈相關肺高壓亞群 |
| TxGNN 預測分數 | 99.56%（rank 8221 / 全部候選中排名第 3） |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

**備註**：TxGNN 對「隅角開放性青光眼」給出更高分數（99.78%），但模型的機轉分析文字明確指出「V1 受體血管收縮作用與眼壓調節無已報導之藥理連結」「純 embedding 相似性預測，缺乏生物學合理性驗證」，且無任何試驗或文獻佐證，故本報告不以其為主要候選，僅供參考。

---

## 為什麼這個預測合理？

目前缺乏 Terlipressin 詳細的作用機轉（MOA）結構化資料（Data Gap，見下方安全性章節）。但依據本評估中「肺動脈高壓」候選適應症的機轉推理內容：Terlipressin 為 **V1 受體促效劑**，透過內臟血管收縮降低門脈壓力。在肝硬化合併門脈-肺高壓（portopulmonary hypertension）患者中，數項小型觀察性研究顯示其可同步改善肺動脈壓力，推測機轉與降低高動力循環狀態（hyperdynamic circulation）及調節肺血管阻力有關。

需特別注意：這個機轉關聯**高度侷限於「肝硬化相關」肺高壓亞群**，並非原發性肺動脈高壓或其他病因肺高壓的直接證據。多篇文獻也顯示 Terlipressin 在新生兒持續性肺高壓（persistent pulmonary hypertension of the newborn）的個案報告中作為搶救治療，顯示其肺血管效應具跨族群（成人肝病、新生兒）的一致性訊號，但皆屬觀察性層級，尚未有針對「肺高壓」本身設計主要終點的隨機對照試驗。

---

## 臨床試驗證據

以下 4 個試驗與 Terlipressin 的既有用途（靜脈曲張出血、肝腎症候群）相關，經評分皆為 **C 級（背景關聯，非直接證據）**，未以肺動脈壓力為主要或次要終點：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03584087](https://clinicaltrials.gov/study/NCT03584087) | Phase 4 | 已完成 | 74 | 評估 EVL 後 Terlipressin 治療對急性靜脈曲張出血的療效，未評估肺動脈壓力終點 |
| [NCT06027970](https://clinicaltrials.gov/study/NCT06027970) | Phase 3 | 未知 | 165 | 持續輸注 Terlipressin 於 EVL 後急性靜脈曲張出血的療效，非肺高壓研究 |
| [NCT06256432](https://clinicaltrials.gov/study/NCT06256432) | Phase 2 | 招募中 | 54 | Ambrisentan（肺高壓標準用藥）用於肝腎症候群，Terlipressin 未列為介入藥物 |
| [NCT05315557](https://clinicaltrials.gov/study/NCT05315557) | NA | 未知 | 100 | Vasopressin vs Terlipressin 作為肝硬化敗血性休克第二線升壓劑，未評估肺動脈高壓 |

> 目前**無**以「肺動脈高壓」為主要適應症登記的 Terlipressin 臨床試驗。

---

## 文獻證據

以下為與肺動脈壓力/肺高壓直接相關之文獻（依觀察性研究優先排序）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18280605](https://pubmed.ncbi.nlm.nih.gov/18280605/) | 2008 | 病例系列 | J Hepatol | 肝硬化併門脈肺高壓患者接受 1 週 Terlipressin 治療後肺動脈壓力顯著改善 |
| [22893473](https://pubmed.ncbi.nlm.nih.gov/22893473/) | 2012 | Cohort | Hepatobiliary Pancreat Dis Int | 7 名肝硬化併肺高壓患者首劑 Terlipressin (2mg) 使肺血管阻力顯著下降 |
| [21733953](https://pubmed.ncbi.nlm.nih.gov/21733953/) | 2012 | Cohort | Angiology | 超音波研究顯示 Terlipressin 對有/無肺高壓之肝硬化患者肺血管阻力影響不同 |
| [15259082](https://pubmed.ncbi.nlm.nih.gov/15259082/) | 2004 | 觀察性研究 | World J Gastroenterol | 心臟超音波評估 Terlipressin 對肝硬化患者收縮期肺動脈壓的影響 |
| [19624374](https://pubmed.ncbi.nlm.nih.gov/19624374/) | 2009 | 病例報告/回顧 | Paediatr Anaesth | 先天性橫膈疝合併重度肺高壓新生兒使用 Terlipressin 之角色探討 |
| [34179513](https://pubmed.ncbi.nlm.nih.gov/34179513/) | 2021 | 系統性回顧（草案） | BMJ Paediatr Open | Vasopressin/Terlipressin 用於早產兒（含持續性肺高壓）之療效安全性系統性回顧計畫 |
| [30971593](https://pubmed.ncbi.nlm.nih.gov/30971593/) | 2019 | 臨床研究 | Ann Card Anaesth | 心臟手術合併肺高壓病人中，Terlipressin 較 Norepinephrine 更能避免 Milrinone 誘發之全身性低血壓，且未惡化 PVR/MPAP |
| [23128058](https://pubmed.ncbi.nlm.nih.gov/23128058/) | 2012 | 個案報告 | J Perinatol | 敗血性低體溫新生兒肺高壓，加入 Terlipressin 後心臟超音波顯示肺動脈壓改善 |
| [21292065](https://pubmed.ncbi.nlm.nih.gov/21292065/) | 2011 | 個案報告 | J Pediatr Surg | 先天性橫膈疝新生兒難治性肺高壓，以 Terlipressin 作為搶救治療 |
| [32999121](https://pubmed.ncbi.nlm.nih.gov/32999121/) | 2020 | 個案報告 | Indian Pediatr | 早產兒持續性肺高壓合併難治性休克，Terlipressin 搶救治療案例 |

> 以上文獻多屬小型觀察性研究或個案報告（tier 2-3），**無任何 RCT 直接以肺動脈高壓為主要終點**。另有 10 篇文獻與 Terlipressin 既有適應症（靜脈曲張出血、肝腎症候群、門脈高壓）相關，但與肺高壓無直接關聯，未列入上表。

---

## 香港上市資訊

Terlipressin 目前在香港**未取得任何藥品許可證**（`total_licenses: 0`），無法提供核准適應症或劑型資訊。

---

## 安全性考量

安全性資訊請參考原廠仿单。

> 本評估資料中，Terlipressin 的仿單警語、禁忌症、藥物交互作用（DDI）皆標記為資料缺口（Data Gap），且**主要警語/禁忌症項目被列為 Blocking 等級缺口**，尚未能完成 S1 安全性初評。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一具實證支持的候選適應症（門脈相關肺高壓）證據等級僅達 L3（觀察性研究/個案報告），無 RCT 以肺高壓為主要終點，且機轉關聯侷限於「肝硬化相關」肺高壓亞群，不能外推至一般肺動脈高壓族群。
- 安全性資料（仿單警語、禁忌症）為 **Blocking 等級缺口**，依規則無法進入 S1 安全性初評，這是比證據等級更急迫的推進障礙。
- 其餘 9 個 TxGNN 預測適應症（含分數最高之隅角開放性青光眼）皆為 L5、無試驗無文獻，模型本身機轉分析已註明「缺乏生物學合理性驗證」，不建議列入後續優先評估。

**若要推進需要：**
- **優先補齊**：Terlipressin 仿單警語與禁忌症（TFDA 或對應藥監機構來源），此為 Blocking 缺口，須先解決才能進行安全性評估。
- 補充 DrugBank 作用機轉（MOA）結構化資料，以強化機轉關聯性分析的嚴謹度。
- 若考慮推進門脈相關肺高壓方向，需規劃以肺動脈壓力/血流動力學為主要終點的前瞻性研究，並明確界定適用族群為「肝硬化合併門脈-肺高壓」，而非泛用於所有肺動脈高壓病因。
- 香港上市部分：由於目前無許可證，須先釐清藥品進口/註冊路徑，才能討論實際臨床應用可行性。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

