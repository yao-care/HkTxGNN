---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 632
evidence_level: L5
indication_count: 5
---

# Ranibizumab
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

# Ranibizumab：從（原適應症資料缺失）到嚴重非增殖性糖尿病視網膜病變

## 一句話總結

Ranibizumab（DB01270）目前在本 Evidence Pack 中未提供原始核准適應症與作用機轉資料。
TxGNN 模型預測它可能對**嚴重非增殖性糖尿病視網膜病變（Severe Nonproliferative Diabetic Retinopathy）**有效，
目前有 **6 個臨床試驗**（含 2 個已完成 Phase 3 RCT）和 **19 篇文獻**支持這個方向。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 預測分數 | 99.99%（rank 244） |
| 證據等級 | L1（2 個已完成 Phase 3 RCT：NCT00444600、NCT02634333） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

> 註：Evidence Pack 未提供 Ranibizumab 的原始核准適應症資料（`original_indications` 為空），故標題與本表無法列出原適應症。

## 為什麼這個預測合理？

Evidence Pack 中 `original_moa` 標記為資料缺口（DG002，待查 DrugBank API），因此無法直接引用官方機轉描述。不過，收錄的多篇文獻本身即說明了 Ranibizumab 的藥理定位：它是一種抗血管內皮生長因子（anti-VEGF）藥物，VEGF 已被證實是糖尿病視網膜病變（DR）進展的關鍵驅動因子（PMID 31669065、33966556）。

嚴重非增殖性 DR（severe NPDR）與 Ranibizumab 目前已知的眼科應用（如糖尿病黃斑水腫 DME）同屬同一疾病光譜的不同病程階段，機轉上高度重疊：兩者皆源於視網膜微血管病變導致 VEGF 上調。2025 年發表的 PAVILION 隨機對照試驗（PMID 40048178）直接顯示，預防性玻璃體內抗 VEGF 注射（含 Ranibizumab port delivery system）可降低無黃斑水腫的 NPDR 患者惡化風險，支持此預測具有機轉與臨床雙重合理性。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04503551](https://clinicaltrials.gov/study/NCT04503551) | Phase 3 | 進行中（未招募） | 174 | Port Delivery System 遞送 Ranibizumab 於無黃斑水腫之 DR 患者的療效與安全性比較 |
| [NCT00444600](https://clinicaltrials.gov/study/NCT00444600) | Phase 3 | 完成 | 691 | 比較雷射、雷射+Triamcinolone、雷射+Ranibizumab、單獨 Ranibizumab 治療 DME 之療效 |
| [NCT03452657](https://clinicaltrials.gov/study/NCT03452657) | Phase 3 | 未知 | 118 | 玻璃體內 Ranibizumab vs 假注射，用於預防高風險 DR 惡化 |
| [NCT02634333](https://clinicaltrials.gov/study/NCT02634333) | Phase 3 | 完成 | 399 | 抗 VEGF 治療預防高風險增殖前期 DR 惡化為視力威脅病變 |
| [NCT02834663](https://clinicaltrials.gov/study/NCT02834663) | Phase 4 | 完成 | 25 | 玻璃體內 Ranibizumab 對 NPDR 合併黃斑水腫之微血管瘤與無灌流區域影響 |
| [NCT05222633](https://clinicaltrials.gov/study/NCT05222633) | N/A | 未知 | 1000 | 真實世界觀察抗 VEGF 治療於濕性 AMD、增殖性 DR、黃斑水腫等之視力與解剖結構效果 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | PAVILION 試驗：Port Delivery System 持續釋放 Ranibizumab vs 監測，用於無黃斑水腫之 NPDR |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | RCT 衍生分析 | Retina | DRCR.net Protocol I 5 年報告：Ranibizumab 治療 DME 後 DR 嚴重度變化 |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | RCT 次分析 | JAMA Ophthalmology | 比較 Aflibercept、Bevacizumab、Ranibizumab 對 DR 惡化/改善之 2 年影響 |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2024 | 系統性回顧+統合分析 | Health Technol Assess | 抗 VEGF 藥物 vs 雷射光凝治療 DR 之系統性回顧 |
| [40347224](https://pubmed.ncbi.nlm.nih.gov/40347224/) | 2025 | 系統性回顧+經濟分析 | Health Technol Assess | 抗 VEGF vs 雷射治療 DR 之系統性回顧與成本效益分析 |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | 統合分析 | Ophthalmology Retina | 基準 DR 嚴重度與 Ranibizumab 治療後 DME 消退時間之關聯 |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | RCT 次分析 | Clin Ophthalmol | RIDE/RISE 試驗中早期 DR 改善之預測因子 |
| [35417296](https://pubmed.ncbi.nlm.nih.gov/35417296/) | 2022 | RCT 事後分析 | Ophthalmic Surg Lasers Imaging Retina | RIDE/RISE 未治療對側眼之 DR 自然病程 |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | RCT 開放性延伸研究 | BMJ Open Ophthalmol | RIDE/RISE 開放性延伸期減少治療頻率對 DRSS 分數的影響 |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opin Biol Ther | Ranibizumab 治療糖尿病視網膜病變之綜述 |

## 香港上市資訊

目前尚無香港上市許可證登記（`market_status`：未上市，`total_licenses`：0）。

## 安全性考量

安全性資訊目前為資料缺口：`key_warnings`、`contraindications`、DDI 查詢皆無資料（DG001，Blocking，需下載並解析 TFDA 仿單 PDF 才能取得）。在補齊前**無法進行 S1 安全性初評**，請暫以原廠仿單為準。

## 結論與下一步

**決策：Hold**

**理由：**
- 效力證據充分（L1：2 個已完成 Phase 3 RCT + 19 篇文獻，含 2025 年 PAVILION RCT 直接支持），機轉合理性高。
- 但藥物在香港尚未上市（0 張許可證），且仿單警語/禁忌為 Blocking 等級資料缺口，依規則無法進入安全性初評，MOA 亦待 DrugBank API 查證（DG002）。因此即使效力面已達 L1，整體仍判定為 Hold。

**若要推進需要：**
- 取得並解析 TFDA（或香港衛生署對應）仿單，補齊警語、禁忌與 DDI 資料（DG001）
- 透過 DrugBank API 查詢正式 MOA 描述（DG002）
- 確認 Ranibizumab 香港上市/許可證狀態
- 待安全性資料補齊後，重新評估是否可轉為 Proceed with Guardrails

---

### 附錄：其他預測適應症（已評估，證據不足）

同一批預測中另有 4 個白內障相關適應症，經初步評估後已排除，列此供參：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 排除理由 |
|------|-----------|-----------|---------|---------|
| 2 | 第二型糖尿病相關白內障 | 99.99% | L4 | 現有文獻僅為白內障手術合併抗 VEGF 注射處理共病之 DME，非治療白內障本身；判斷為 DR 患者共病之間接關聯 |
| 3 | 未熟期白內障 | 99.99% | L5 | 無任何臨床試驗或文獻支持，僅為模型預測分數 |
| 4 | 顱狹窄症相關白內障 | 99.99% | L5 | 罕見先天症候群，與抗 VEGF 機轉無關聯，判定為模型雜訊 |
| 5 | 成熟期白內障 | 99.99% | L4 | 文獻僅涉及白內障手術合併 Ranibizumab 注射控制黃斑水腫，未證實對白內障本身有療效 |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

