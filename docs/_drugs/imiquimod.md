---
layout: default
title: Imiquimod
parent: 高證據等級 (L1-L2)
nav_order: 394
evidence_level: L1
indication_count: 10
---

# Imiquimod
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

Using the report template supplied in your prompt — this is a direct content-generation task from the given Evidence Pack, no additional skill lookup needed for a one-shot report write-up.

I generated the report directly from the Evidence Pack JSON. Two data-fidelity notes before the report:

- `original_indications` is empty and `original_moa` is `[Data Gap]` in this pack — Hong Kong (`taiwan_regulatory`) shows **未上市 / 0 張許可證**, so there is no HK-specific "原適應症" to cite. I labeled the original indication using Imiquimod's globally-established approved uses (genital warts / actinic keratosis / superficial BCC) but flagged this explicitly as **not sourced from this Evidence Pack**, since the pack itself has no HK license data to confirm it.
- 細胞毒性 (cytotoxicity) 章節已省略：Imiquimod 是 TLR7 免疫調節劑而非傳統細胞毒性化療藥物，且 Evidence Pack 未提供 DrugBank categories 佐證其為 Antineoplastic/Cytotoxic 分類，依規則此章節不適用。

---

# Imiquimod：從外用皮膚病灶到癌前病變 (Pre-malignant Neoplasm)

## 一句話總結

Imiquimod 是一款外用 TLR7（Toll-like receptor 7）促效劑，在其他主要市場核准用於生殖疣、光化性角化症與淺層基底細胞癌等外用皮膚病灶治療。TxGNN 模型預測它可能對**癌前病變 (Pre-malignant Neoplasm)** 有效，目前有 **19 個臨床試驗**和 **9 篇文獻**支持這個方向，其中包含一項納入 259 人的 Phase 3 已完成試驗。

> ⚠️ 本藥物在香港**尚未上市**，且仿單警語/禁忌症資料為 Blocking 等級缺口（DG001），安全性初評尚無法完成。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 未在 Evidence Pack 中登記（香港未上市；已知於其他地區核准用於外用生殖疣、光化性角化症、淺層基底細胞癌，此為一般藥理知識，非本次資料來源） |
| 預測新適應症 | 癌前病變 (Pre-malignant Neoplasm) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L1 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為 Data Gap）。根據已知藥理資訊，Imiquimod 是外用 Toll-like receptor 7 (TLR7) 促效劑，活化局部免疫反應（誘導干擾素-α等細胞激素分泌），促使免疫系統辨識並清除病毒感染或異常增生的表皮細胞。

癌前病變（如光化性角化症、子宮頸/外陰/肛門上皮內瘤病變 CIN/VIN/AIN、Lentigo malignant、Bowenoid papulosis）在生物學上多與慢性紫外線傷害或 HPV 感染相關，病灶位置表淺、可局部給藥，這與 Imiquimod 目前已知的皮膚外用治療模式高度契合。

Evidence Pack 中的機轉論述指出：「Imiquimod 為 TLR7 促效劑，活化局部免疫反應以清除表淺上皮之異常增生/癌前病變細胞，此機轉已是核准適應症（光化性角化症）及廣泛 off-label 使用（VIN/CIN/AIN/Bowenoid papulosis）的基礎，機轉與臨床證據高度一致。」多個獨立臨床試驗（Lentigo malignant、CIN、VIN、Oral SCC 等）也從不同病灶類型驗證了這個機轉延伸的合理性。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01720407](https://clinicaltrials.gov/study/NCT01720407) | Phase 3 | 已完成 | 259 | Neoadjuvant imiquimod 用於臉部 Lentigo malignant，評估縮小手術切除範圍及降低病灶內復發風險（相關性 A 級） |
| [NCT01229319](https://clinicaltrials.gov/study/NCT01229319) | Phase 4 | 狀態不明 | 20 | Imiquimod 3.75% cream 於冷凍治療後用於手/前臂肥厚型光化性角化症之安全性與療效（相關性 A 級） |
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | 已完成 | 20 | Imiquimod 5% cream 每週3天、1-2 個療程治療頭部光化性角化症之療效持續性 |
| [NCT04883645](https://clinicaltrials.gov/study/NCT04883645) | Early Phase 1 | 已完成 | 16 | Neoadjuvant TLR7 促效劑（Aldara）用於早期口腔鱗狀細胞癌，評估腫瘤細胞自我毀滅與免疫活化效果（相關性 B 級） |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | 已終止 | 9 | 外用 Imiquimod 治療高度子宮頸上皮內瘤病變 (CIN 2-3)，作為 LLETZ 手術之非侵入性替代方案，惟提前終止（相關性 B 級） |
| [NCT00941811](https://clinicaltrials.gov/study/NCT00941811) | Phase 2 | 已完成 | 5 | 探討 HPV 相關免疫逃脫機制與 Imiquimod 治療外陰上皮內瘤病變 (VIN 2/3) 及生殖疣之反應（相關性 B 級） |
| [NCT03233412](https://clinicaltrials.gov/study/NCT03233412) | Phase 2 | 已完成 | 90 | 隨機對照試驗評估外用 Imiquimod 治療高度子宮頸上皮內病變之療效 |
| [NCT04219358](https://clinicaltrials.gov/study/NCT04219358) | Phase 1 | 已終止 | 49 | 比較 5% / 0.05% / 0.05% 奈米微囊化 Imiquimod 凝膠治療光化性唇炎（下唇癌前病變）之隨機對照試驗 |
| [NCT02242929](https://clinicaltrials.gov/study/NCT02242929) | Phase 3 | 狀態不明 | 145 | 手術切除 vs. 刮除術併用 Imiquimod 治療結節型基底細胞癌之非劣性隨機對照試驗 |
| [NCT04072900](https://clinicaltrials.gov/study/NCT04072900) | Phase 1 | 狀態不明 | 30 | 個人化 neoantigen 疫苗合併 anti-PD-1，Imiquimod 作為佐劑用於轉移性黑色素瘤（相關性 C 級，非直接治療癌前病變）|

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Review (Cochrane, Tier 1) | Cochrane Database Syst Rev | 肛門上皮內瘤病變 (AIN) 治療介入之系統性回顧，含 Imiquimod 應用 |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Review (Cochrane, Tier 1) | Cochrane Database Syst Rev | 高度外陰上皮內瘤病變 (VIN) 藥物治療之系統性回顧，缺乏最佳治療共識 |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | 非黑色素瘤皮膚癌合併光動力治療之綜述，涵蓋 Imiquimod 等外用療法 |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | 非黑色素瘤皮膚癌及癌前病變之外用藥物治療策略（含 Imiquimod） |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | 光化性角化症現行治療管理綜述 |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical (PK/PD, 動物模型) | Urol Oncol | TLR7 促效劑於大鼠模型膀胱內給藥之藥動/藥效學評估 |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Case report | Der Hautarzt | 播散性表淺光化性汗孔角化症合併多處癌前病變之光學同調斷層掃描影像案例 |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case report | Int J STD AIDS | 腎臟移植病人以 Imiquimod 5% 成功治療高度外陰上皮內瘤病變案例 |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case report | Int J STD AIDS | 外用 Imiquimod 5% cream 成功治療陰莖 Bowenoid papulosis（癌前病變）案例 |

## 香港上市資訊

Imiquimod 目前在香港**未上市**，Evidence Pack 中無許可證登記資料。

## 安全性考量

安全性資訊請參考原廠仿單。

> 補充說明：本次評估中，「TFDA 仿單警語/禁忌」被標記為 **Blocking** 等級資料缺口（DG001），影響是「無法進入 S1 安全性初評」；「作用機轉 (MOA)」為 **High** 等級缺口（DG002）。這兩項缺口須優先補齊。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有一項納入 259 人的 Phase 3 已完成試驗（NCT01720407）支持 Imiquimod 用於癌前病變（Lentigo malignant）之 neoadjuvant 治療，加上多個 Phase 2/3 試驗（CIN、VIN、光化性角化症、基底細胞癌）從不同病灶類型驗證機轉延伸的一致性，證據等級達 L1。
- 然而，仿單警語/禁忌症資料為 Blocking 等級缺口，且藥物尚未於香港上市，安全性初評（S1）尚無法完成，故不建議直接 Go，需以 Guardrails 方式推進。

**若要推進需要：**
- 取得香港/原廠仿單完整警語與禁忌症資料（解決 DG001，Blocking）
- 補充詳細作用機轉 (MOA) 資料以強化機轉關聯性分析（解決 DG002，High）
- 查詢完整藥物交互作用 (DDI) 資料庫（目前查詢結果為 not_found）
- 若評估於香港申請上市，需另行規劃藥品註冊與許可證申請流程
- 針對特定病灶族群（如 CIN/VIN/AIN 等 HPV 相關病變）之族群安全性監測計畫
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

