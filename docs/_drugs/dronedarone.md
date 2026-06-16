---
layout: default
title: Dronedarone
parent: 高證據等級 (L1-L2)
nav_order: 251
evidence_level: L1
indication_count: 10
---

# Dronedarone
{: .fs-9 }

證據等級: **L1** | 預測適應症: **10** 個
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

# Dronedarone：從心房顫動到中風疾病

## 一句話總結

Dronedarone 是一種非碘化的多通道阻斷型第三類抗心律失常藥物，在全球多個國家已核准用於心房顫動（AF）與心房撲動的治療，但香港尚未上市。TxGNN 模型預測它可能對**中風疾病 (Stroke Disorder)** 有效，目前有 **19 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心房顫動／心房撲動（國際核准；香港尚未上市） |
| 預測新適應症 | 中風疾病 (Stroke Disorder) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Dronedarone 是 Amiodarone 的非碘化類似物，具備多通道阻斷特性（Class I–IV 複合效應），透過抑制鈉通道（Nav1.5）、鉀通道（Kv11.1、Kv4.3）、鈣通道（Cav1.2）及 β 腎上腺素受體，有效控制心房顫動節律並降低心率。其再利用機制建立在明確的因果鏈上：**AF → 左心房血栓形成 → 心源性栓塞型中風**。透過維持竇性心律，可顯著減少左心房血栓脫落，從而預防缺血性中風。

最強直接證據來自 ATHENA Phase 3 大型 RCT（n > 4,600）：Dronedarone 使 AF 患者中風相對風險降低 **34%**（HR 0.66, p = 0.03）。機轉研究（PMID 28992468）進一步揭示，Dronedarone 在抗心律失常效應之外，尚具有獨立的直接抗凝血（弱 Factor Xa/IIa 抑制）與抗血小板活性，構成雙重腦血管保護機制。此外，PMID 22366819 回顧了 Dronedarone 對心臟及腦部缺血/再灌流損傷的多效性（pleiotropic effects），進一步豐富其機轉基礎。

值得注意的是，PALLAS 試驗（NCT01151137, n = 3,236）顯示，在**高風險永久性 AF** 族群中 Dronedarone 反而增加中風及心血管死亡風險，導致試驗提早終止。因此，預測的獲益僅適用於**非永久性 AF**（陣發性或持續性）且心功能保存（LVEF ≥ 35%）的患者族群，需嚴格把關適用條件。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01288352](https://clinicaltrials.gov/study/NCT01288352) | Phase 4 | 已完成 | 2,789 | EAST 試驗：早期 AF 節律控制策略（Dronedarone 為主要抗心律失常藥）vs 常規治療，中風為複合主要終點組成，結果顯示早期節律控制顯著降低心血管事件 |
| [NCT07270848](https://clinicaltrials.gov/study/NCT07270848) | Phase 4 | 未開始招募 | 1,898 | 多中心前瞻性 RCT，直接比較 Dronedarone 早期節律控制的療效、安全性及生活品質改善，為近期設計最直接相關試驗 |
| [NCT05293080](https://clinicaltrials.gov/study/NCT05293080) | Phase 3 | 未開始招募 | 1,746 | 急性缺血性中風合併 AF 患者早期節律控制（含 Dronedarone），主要終點為預防不良心血管結局及中風再發 |
| [NCT05130268](https://clinicaltrials.gov/study/NCT05130268) | Phase 4 | 已完成 | 339 | 首次確診 AF 患者早期 Dronedarone vs 常規治療 RCT，直接評估腦血管結局改善，2024 年完成 |
| [NCT01151137](https://clinicaltrials.gov/study/NCT01151137) | Phase 3 | 已終止 | 3,236 | PALLAS 試驗：高風險永久性 AF 患者，主要終點為預防中風/全身性栓塞/心肌梗塞/心血管死亡；因 Dronedarone 組事件率升高提早終止（重要安全性警示） |
| [NCT01856075](https://clinicaltrials.gov/study/NCT01856075) | 觀察性 | 已完成 | 1,015 | Dronedarone vs 其他抗心律失常藥真實世界比較效果研究（德、西、義、美四國多中心），評估含中風在內的心血管結局 |
| [NCT05279833](https://clinicaltrials.gov/study/NCT05279833) | 系統性回顧 | 已完成 | 87,810 | Dronedarone vs Sotalol 的系統性文獻回顧與網絡 Meta 分析，綜合評估兩藥的安全性與有效性 |
| [NCT00911508](https://clinicaltrials.gov/study/NCT00911508) | 觀察性 | 已完成 | 2,204 | CABANA 試驗：導管消融 vs 抗心律失常藥物策略（含 Dronedarone），評估 AF 患者長期心血管結局 |
| [NCT01266681](https://clinicaltrials.gov/study/NCT01266681) | N/A | 不明 | 100 | Dronedarone vs Amiodarone 持續性 AF 心臟復律後竇律維持 RCT，間接評估中風預防獲益 |
| [NCT02618577](https://clinicaltrials.gov/study/NCT02618577) | Phase 3 | 已終止 | 2,608 | NOAH 試驗：AF 高心率發作患者 NOAC（Edoxaban）預防中風，含評估與 Dronedarone 合用之交互作用影響 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT 次要分析 | Clin Res Cardiology | EAST-AFNET 4 子分析：長期評估 Amiodarone 與 Dronedarone 早期節律控制的安全性與心血管結局，探討兩藥的臨床適用差異 |
| [28992468](https://pubmed.ncbi.nlm.nih.gov/28992468/) | 2017 | 機轉研究 | Atherosclerosis | Dronedarone 具獨立於抗心律失常作用之外的直接抗凝血（Factor Xa 抑制）及抗血小板效應，為 ATHENA 中風下降提供雙重機制解釋 |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | 回顧性世代研究 | Circ Arrhythm Electrophysiol | 大型退伍軍人資料庫真實世界數據：Dronedarone vs Sotalol 在 AF 患者的竇律維持療效與安全性頭對頭比較 |
| [35293087](https://pubmed.ncbi.nlm.nih.gov/35293087/) | 2022 | ATHENA 事後分析 | Eur J Heart Failure | ATHENA 試驗事後分析：Dronedarone 用於合併 HFpEF/HFmrEF 的 AF 患者可降低心血管事件，拓展其潛在適用族群 |
| [28496906](https://pubmed.ncbi.nlm.nih.gov/28496906/) | 2013 | 回顧性資料庫研究 | J Atrial Fibrillation | 真實世界 10,455 例分析：比較 Dronedarone vs 其他抗心律失常藥在中風、心衰竭、間質性肺病及肝損傷的相對風險 |
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | Phase 3 RCT | N Engl J Med | PALLAS 試驗：高風險永久性 AF 患者使用 Dronedarone 顯著增加中風及心血管死亡風險，為核心安全性警示文獻 |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | 藥物核准回顧 | Vasc Health Risk Manag | Dronedarone FDA 核准回顧：ATHENA 試驗證實全因死亡率與心血管住院降低，事後分析提示中風風險下降 |
| [24469871](https://pubmed.ncbi.nlm.nih.gov/24469871/) | 2013 | 療效與耐受性回顧 | Cardiology Journal | 系統性評估 Dronedarone 用於 AF 治療的臨床療效、耐受性及與其他抗心律失常藥物的比較定位 |
| [22166900](https://pubmed.ncbi.nlm.nih.gov/22166900/) | 2012 | 綜合性回顧 | Lancet | AF 管理全面概述，涵蓋 Dronedarone 在節律控制與心源性中風預防的角色及其與新型口服抗凝藥的配合使用 |
| [37777298](https://pubmed.ncbi.nlm.nih.gov/37777298/) | 2023 | 指引章節 | Am J Cardiology | AF 頻率控制 vs 節律控制最新指引，詳述 Dronedarone 的適應族群選擇、禁忌條件及臨床決策框架 |

---

## 香港上市資訊

Dronedarone 目前在香港**尚未取得藥物許可證**，無任何上市記錄（許可證數：0）。

> 國際上，Dronedarone 以品牌名 **Multaq®** 在美國（FDA，2009 年）、歐盟（EMA）、澳洲（TGA）等地已獲核准，適應症為非永久性心房顫動或心房撲動患者的竇律維持治療。若在香港推進本藥使用，需先完成香港衛生署的藥物注冊程序。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **來自全球臨床試驗的重要安全提示（供參考）：**
>
> - **PALLAS 試驗警示**：高風險永久性 AF 合併心血管危險因子患者使用 Dronedarone，中風與心血管死亡風險**顯著增加**，試驗提早終止。此族群為明確禁忌。
> - **心衰竭禁忌**：ANDROMEDA 試驗顯示 Dronedarone 增加嚴重心衰（NYHA III-IV 級）患者死亡率，LVEF < 35% 患者禁用。
> - **竇房結功能障礙禁忌**：因 Class I 效應（Nav1.5 阻斷）可能惡化竇性停搏，無人工節律器患者禁用。
> - **藥物交互作用**：透過抑制 P-glycoprotein 可升高 Digoxin 血中濃度（PMID 33888353）；與 Rivaroxaban 合用可提高後者暴露量（PMID 27693025）；需關注與 NOAC 合用之出血與中風風險（PMID 41152878, 40243197）。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
EAST（Phase 4, n=2,789）及 ATHENA（Phase 3, n>4,600）等多個大型 RCT 提供 L1 等級證據，支持 Dronedarone 在**非永久性 AF 且心功能保存**族群中使中風相對風險降低 34%（HR 0.66）；機轉研究確認其兼具直接抗凝血與抗血小板雙重保護效應，生物學合理性充分。然而，PALLAS 試驗揭示的永久性 AF 族群安全性禁忌，以及香港尚未上市的現狀，需要系統性應對。

**若要推進需要：**
- 補齊香港衛生署仿單的完整警語與禁忌症資料（目前為資料缺口）
- 確認 Dronedarone 詳細作用機轉（MOA）文獻（目前為資料缺口）
- 向香港衛生署申請藥物注冊許可（目前 0 張許可證）
- 嚴格訂定適用族群標準：**非永久性 AF（陣發性或持續性）、LVEF ≥ 35%、無病態竇房結、無嚴重肝腎功能不全**
- 制定與 NOAC 或 Digoxin 合用時的藥物交互作用監測方案
- 追蹤 NCT05130268 完整結果發表（2024 年完成招募，腦血管結局數據待公布）
- 待 NCT07270848（n=1,898，預計 2028 年完成）結果以進一步強化療效與安全性證據
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

