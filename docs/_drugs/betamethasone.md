---
layout: default
title: Betamethasone
parent: 高證據等級 (L1-L2)
nav_order: 98
evidence_level: L2
indication_count: 10
---

# Betamethasone
{: .fs-9 }

證據等級: **L2** | 預測適應症: **10** 個
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

# Betamethasone：從炎症性皮膚疾病到斑禿

## 一句話總結

Betamethasone 是強效合成糖皮質激素，廣泛用於炎症性及自身免疫性疾病的治療。
TxGNN 模型預測它可能對**斑禿 (Alopecia Areata)** 有效，
目前有 **7 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 炎症性及自身免疫性疾病（已知為強效糖皮質激素，當地許可證資料待補充） |
| 預測新適應症 | 斑禿 (Alopecia Areata) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L2 |
| 香港上市 | ✗ 許可證資料查無（建議重新確認衛生署資料庫） |
| 許可證數 | 0 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Betamethasone 是強效合成糖皮質激素，效價約為 Prednisolone 的 25–30 倍。其作用機轉為與胞內糖皮質激素受體（GR）結合後，下調 IL-1β、TNF-α、IFN-γ 等促炎細胞因子，並抑制 NF-κB 信號通路，從而全面壓制 T 細胞的活化與增殖。

斑禿的核心病理為 CD8⁺ T 細胞介導的自身免疫反應——毛囊「免疫豁免區」（immune privilege）崩潰後，淋巴細胞大量浸潤毛球並攻擊毛囊，導致非瘢痕性脫髮。Betamethasone 的廣譜免疫抑制機轉直接作用於這一病理核心，理論連結強且具高度生物學合理性。

值得注意的是，Betamethasone 已具備外用（valerate/dipropionate）、病灶內注射（intralesional）及口服小劑量衝擊（oral mini-pulse, BOMP）三種施用形式，均有對應斑禿的臨床試驗，且多篇直接以 Betamethasone 為介入的 RCT 已完成，進一步支持了 TxGNN 模型的預測合理性。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Phase 2 | 完成 | 60 | 直接比較 Betamethasone 口服小劑量衝擊（BOMP）vs Azathioprine 每週衝擊治療中重度斑禿，為本資料集最直接相關的已完成試驗 |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | 未知 | 59 | 直接比較外用 Betamethasone valerate 0.1% vs 外用 Cetirizine 1% 治療局限性斑禿，結果解讀需待狀態確認 |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Phase 1 | 未知 | 60 | 以外用 Betamethasone valerate 作為主動對照，評估外用 Pentoxifylline 2% 及 Metformin 10% 治療片狀斑禿之療效與安全性 |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Phase 4 | 完成 | 50 | 比較外用 Latanoprost vs 外用皮質類固醇（corticosteroid class）治療局限性斑禿，提供同類藥物療效框架，間接支持 Betamethasone 外用可行性 |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Phase 4 | 完成 | 40 | 評估外用 5% Minoxidil + 強效外用皮質類固醇 vs 病灶內皮質類固醇治療斑禿，提供聯合治療策略參考 |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | 招募中 | 250 | 瘢痕性脫髮（CCCA）多中心前瞻性預後研究，比較不同治療組別結果，直接相關性較低 |
| [NCT01111981](https://clinicaltrials.gov/study/NCT01111981) | Phase 4 | 未知 | 30 | 評估 Clobetasol Propionate 0.05% 治療中心性離心性瘢痕性禿髮（CCCA），非 Betamethasone 且為不同脫髮類型，相關性低 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | RCT | J Am Acad Dermatol | 微針經皮遞送 Compound Betamethasone 治療斑禿的隨機對照試驗；評估此法作為病灶內注射替代方案的療效，重點在減輕注射疼痛 |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | RCT | Cureus | 評估口服 Betamethasone Mini-Pulse 治療中重度斑禿的療效與安全性；間歇性口服皮質類固醇方案作為長期治療的可行替代策略 |
| [40510104](https://pubmed.ncbi.nlm.nih.gov/40510104/) | 2025 | RCT | Cureus | 非盲隨機平行對照試驗（n=60），比較口服 Cyclosporine 3mg/kg vs 口服 Betamethasone Mini-Pulse 治療斑禿的療效與安全性 |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | RCT | Iranian J Pharm Res | 雙盲安慰劑對照試驗（n=36），比較口服 Betamethasone 衝擊（3mg/週）、Methotrexate（15mg/週）及聯合治療嚴重斑禿的療效 |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | RCT | Cureus | 比較外用 Betamethasone Dipropionate vs 外用 Minoxidil 治療斑禿的療效；外用皮質類固醇作為一線局部治療的實證支持 |
| [36114868](https://pubmed.ncbi.nlm.nih.gov/36114868/) | 2023 | RCT | Arch Dermatol Res | 評估 CO₂ 分段雷射單獨 vs 聯合 Betamethasone valerate 乳膏治療斑禿的臨床及皮膚鏡療效與安全性（n=30） |
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network Meta-analysis | Cochrane Database Syst Rev | Cochrane 系統回顧與網路統合分析，涵蓋斑禿各類免疫抑制劑及毛髮生長刺激劑的療效比較，為最高等級系統性證據 |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatol Pract Concept | 系統性回顧皮質類固醇衝擊療法在斑禿的療效、復發率、副作用及不同衝擊方案的預後因子 |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | Comparative Clinical Study | Dermatol Ther | 六組隨機雙盲試驗（每組 n=18），比較 Latanoprost、Minoxidil 5%、Betamethasone 及三者聯合方案治療斑禿的療效與患者滿意度 |
| [37765130](https://pubmed.ncbi.nlm.nih.gov/37765130/) | 2023 | Experimental | Pharmaceuticals (Basel) | 開發共包封 Betamethasone + Minoxidil 之聚合物及脂質奈米粒子，提升毛囊靶向遞藥效率，為新型局部遞藥系統的前臨床研究 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
已有多個直接以 Betamethasone 為介入的隨機對照試驗（包含 Phase 2 已完成試驗）及 Cochrane 網路統合分析支持，機轉連結明確（糖皮質激素直接作用於斑禿核心免疫病理），且具備外用、病灶內注射、口服多種可行施用途徑，整體證據達 L2 等級，支持謹慎推進。

**若要推進需要：**
- 補充 Betamethasone 完整作用機轉（MOA）資料（建議查詢 DrugBank API，解決 DG002）
- 取得香港衛生署核准的完整安全性資訊，包括仿單警語與禁忌症（解決 DG001，Blocking）
- 重新查詢香港衛生署藥劑業及毒藥管理局（PSDH）資料庫，確認許可證登記狀態
- 明確目標施用途徑（外用 vs 口服 mini-pulse vs 病灶內注射），各途徑需個別評估風險效益
- 建立長期使用的系統性副作用監測計畫（HPA 軸抑制、皮膚萎縮等已知風險）
- 針對兒童及特殊族群制定安全性使用指引
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

