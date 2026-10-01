---
layout: default
title: Flecainide
parent: 僅模型預測 (L5)
nav_order: 373
evidence_level: L5
indication_count: 10
---

# Flecainide
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

# Flecainide：從心律不整（心房顫動）到中風

## 一句話總結

Flecainide 是 Class IC 鈉通道阻斷劑，臨床上用於心房顫動（AF）等心律不整的節律控制。
TxGNN 模型預測它可能對**中風 (Stroke Disorder)** 有效，目前有 **21 個臨床試驗**和 **20 篇文獻**與此方向相關。
但其中真正以 flecainide 為干預的研究很少，中風效益也只能經由 AF 節律控制間接推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明適應症；依文獻為心房顫動等心律不整的節律控制 |
| 預測新適應症 | 中風 (Stroke Disorder) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L3（見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

> 證據等級說明：資料包自動評為 L2。但依判定規則，目前沒有「已完成、以 flecainide 為干預、以中風為結局」的 Phase 2/3 RCT。最大的 EAST-AFNET 4 是 Phase 4 的策略性試驗，flecainide 只是其中一個選項。因此這裡保守判定為 L3（有觀察性研究與系統性回顧）。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Flecainide 是 Class IC 鈉通道阻斷劑，用於 AF 的節律控制。它的藥理作用是抑制心臟電傳導，並未證實直接作用於腦缺血。

AF 是中風的重要危險因子。若能有效維持竇性心律，理論上可降低心因性栓塞的風險，這是模型預測合理的主要依據。EAST-AFNET 4 測試了早期節律控制策略（flecainide 為選項之一），其複合結局包含中風。不過這個效果無法單獨歸因於 flecainide。

還有兩個限制。Flecainide 在結構性或缺血性心臟病患者中禁用（CAST 試驗），而中風族群常有這類疾病。此外，有觀察性資料顯示抗心律不整藥與 DOAC 的交互作用可能影響中風風險。

模型的其他 9 項預測中，「腦血管疾病」有類似的間接證據。其餘 8 項（如 ABri 類澱粉變性、肌聚糖病、十二指腸阻塞等）沒有試驗、文獻或合理機轉，僅為模型輸出。

## 臨床試驗證據

以下列出最相關的 10 項（共 21 項）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | 完成 | 2789 | EAST-AFNET 4：早期節律控制（含 flecainide）vs 常規照護，預防 AF 相關併發症；中風為複合結局之一 |
| [NCT05213104](https://clinicaltrials.gov/study/NCT05213104) | Phase 3 | 進行中（不再招募） | 186 | 以 flecainide 降低 PFO 關閉術後房性心律不整風險；主要結局為心律不整，屬中風風險的替代指標 |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | 招募中 | 1746 | EAST-STROKE：急性缺血性中風合併 AF 患者的早期節律控制；未確認使用 flecainide |
| [NCT07405671](https://clinicaltrials.gov/study/NCT07405671) | Phase 4 | 招募中 | 988 | 比較 flecainide 與 sotalol/amiodarone 用於 AF 合併穩定冠心病的安全性 |
| [NCT01646281](https://clinicaltrials.gov/study/NCT01646281) | Phase 4 | 未知 | 70 | Vernakalant 與 flecainide 對 AF 患者心房收縮力的影響；結局為替代指標 |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | N/A | 完成 | 2204 | CABANA：導管消融 vs 抗心律不整藥；藥物組未明確指定 flecainide |
| [NCT00523978](https://clinicaltrials.gov/study/NCT00523978) | Phase 3 | 完成 | 245 | STOP AF：冷凍消融 vs 藥物（flecainide、propafenone 或 sotalol）；非中風結局 |
| [NCT06783868](https://clinicaltrials.gov/study/NCT06783868) | N/A | 尚未招募 | 100 | 近期中風合併 AF 患者，消融 vs 藥物治療的神經學結局；無 flecainide 干預 |
| [NCT06096337](https://clinicaltrials.gov/study/NCT06096337) | N/A | 進行中（不再招募） | 484 | 脈衝電場消融 vs 抗心律不整藥作為持續性 AF 第一線治療；藥物未指定為 flecainide |
| [NCT02459574](https://clinicaltrials.gov/study/NCT02459574) | N/A | 完成 | 321 | 簡化消融 vs 抗心律不整藥，減少 AF 復發住院 |

## 文獻證據

以下列出最相關的 10 篇（共 20 篇）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38702961](https://pubmed.ncbi.nlm.nih.gov/38702961/) | 2024 | RCT（次分析） | Europace | EAST-AFNET 4 中以鈉通道阻斷劑（flecainide、propafenone）執行早期節律控制的長期安全性與療效 |
| [37109225](https://pubmed.ncbi.nlm.nih.gov/37109225/) | 2023 | RCT | J Clin Med | Carvedilol 與 flecainide 用於特發性流出道 PVC 的隨機先導研究（非中風） |
| [25820938](https://pubmed.ncbi.nlm.nih.gov/25820938/) | 2015 | 系統性回顧 | Cochrane Database Syst Rev | 抗心律不整藥於 AF 電擊復律後維持竇性心律的效果 |
| [41954064](https://pubmed.ncbi.nlm.nih.gov/41954064/) | 2026 | 世代研究 | J Am Heart Assoc | 1C 類抗心律不整藥用於 AF 的長期結果；相對於心率控制的心血管效益仍不明確 |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | 世代研究 | BMC Med | 非瓣膜性 AF 患者同時使用 DOAC 與有交互作用的抗心律不整藥，其中風與出血風險 |
| [23871349](https://pubmed.ncbi.nlm.nih.gov/23871349/) | 2013 | 分析研究 | Int J Cardiol | Flec-SL 試驗分析：AF 選擇性復律後的中風風險低 |
| [8729366](https://pubmed.ncbi.nlm.nih.gov/8729366/) | 1995 | 臨床研究 | Arch Mal Coeur Vaiss | 38 位不明原因缺血性腦血管事件患者，評估心房易損性及靜脈注射 flecainide 對電生理的影響 |
| [27159789](https://pubmed.ncbi.nlm.nih.gov/27159789/) | 2016 | Review | Nat Rev Dis Primers | AF 的流行病學與處置；AF 使中風風險上升 |
| [35114252](https://pubmed.ncbi.nlm.nih.gov/35114252/) | 2022 | 機轉研究 | J Mol Cell Cardiol | 心房與心室鈉通道的生物物理差異，使 flecainide 對心房更有效 |
| [40800559](https://pubmed.ncbi.nlm.nih.gov/40800559/) | 2025 | 病例報告 | Eur Heart J Case Rep | Flecainide 相關的難治性室性心搏過速，及更新的處置策略 |

## 香港上市資訊

共 5 張許可證。資料中未載明劑型與核准適應症，因此不列出這兩欄。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-24395 | TAMBOCOR TAB 100MG | INOVA PHARMACEUTICALS (HONG KONG) LIMITED |
| HK-60853 | TAMBOCOR CR CAP 100MG | INOVA PHARMACEUTICALS (HONG KONG) LIMITED |
| HK-60854 | TAMBOCOR CR CAP 200MG | INOVA PHARMACEUTICALS (HONG KONG) LIMITED |
| HK-56748 | VICK-FLECAINIDE TAB 100MG | VICKMANS LABORATORIES LTD |
| HK-56061 | APO-FLECAINIDE TAB 100MG | HIND WING CO LTD |

## 安全性考量

- **結構性或缺血性心臟病**：Flecainide 在此類患者中禁用（CAST 試驗），而中風族群常有這類疾病，是最大的族群限制。
- **心律不整風險**：文獻指出鈉通道阻斷劑可能有致心律不整作用，也可能在 Brugada 體質者身上誘發 Brugada 波形。
- **藥物交互作用**：抗心律不整藥與 DOAC 併用可能影響中風與出血風險，需逐一檢視併用藥物。

香港衛生署仿單的警語、禁忌與藥物交互作用資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 中風效益只能經由 AF 節律控制間接推論，沒有以 flecainide 為主體、以中風為結局的已完成試驗。
- 香港仿單的安全性資料缺口屬阻斷性（Blocking），無法進入安全性篩選，且中風族群與 flecainide 的禁忌族群高度重疊。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症。
- 補充作用機轉資料（DrugBank）。
- 追蹤 NCT05293080（EAST-STROKE）與 NCT05213104（PFO 關閉後 flecainide）的結果。
- 設計排除結構性或缺血性心臟病的篩選條件，並建立 DOAC 等併用藥物的審查流程。

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

