---
layout: default
title: Etodolac
parent: 中證據等級 (L3-L4)
nav_order: 293
evidence_level: L3
indication_count: 10
---

# Etodolac
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

# Etodolac：從骨關節炎到強直性脊椎炎

## 一句話總結

Etodolac 是一種 COX-2 選擇性非甾體抗炎藥（NSAID），在多國已核准用於骨關節炎、類風濕性關節炎等風濕性疾病，但目前在香港並無上市許可。TxGNN 模型在 10 個預測適應症中，對**強直性脊椎炎（Ankylosing Spondylitis）**的評估最具臨床可行性，預測分數達 **99.93%**，目前有 **1 個臨床試驗背景資料**和 **10 篇文獻**支持此方向，且 ASAS/EULAR 指引已確認 NSAID 為強直性脊椎炎的一線治療選擇。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 骨關節炎、類風濕性關節炎（國際核准適應症；香港未上市） |
| 最佳預測適應症 | 強直性脊椎炎（Ankylosing Spondylitis） |
| TxGNN 預測分數 | 99.93%（全模型排名第 2,031） |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 預測適應症總覽

本次 Evidence Pack 共分析 10 個 TxGNN 預測適應症，以下為完整摘要：

| TxGNN 排名 | 適應症 | 預測分數 | 證據等級 | 建議 |
|-----------|--------|---------|---------|------|
| 914 | Acromesomelic Dysplasia, Hunter-Thompson Type | 99.97% | L5 | Hold |
| 1,039 | Brachyolmia-Amelogenesis Imperfecta Syndrome | 99.97% | L5 | Hold |
| 1,116 | Myosclerosis | 99.97% | L5 | Hold |
| 1,157 | Spondyloarthropathy, Susceptibility To | 99.96% | L4 | Research Question |
| 1,200 | Brachyolmia | 99.96% | L5 | Hold |
| **2,031** | **強直性脊椎炎（Ankylosing Spondylitis）** | **99.93%** | **L3** | **Proceed with Guardrails** |
| 2,035 | Pseudoachondroplasia | 99.93% | L5 | Hold |
| 3,280 | Rheumatoid Vasculitis | 99.87% | L4 | Research Question |
| 3,330 | Hypermobility of Coccyx | 99.87% | L4 | Research Question |
| **3,517** | **炎症性脊椎病（Inflammatory Spondylopathy）** | **99.86%** | **L3** | **Proceed with Guardrails** |

> ⚠️ **重要提醒**：TxGNN 預測分數高≠臨床可行性高。排名前五的預測（如 Acromesomelic Dysplasia、Brachyolmia 等）均為遺傳性骨骼發育異常，COX-2 抑制機轉與其致病機轉無直接關聯，建議暫緩（Hold）。本報告的深度分析聚焦於最具臨床意義的**強直性脊椎炎**。

---

## 為什麼這個預測合理？

Etodolac 的核心作用機轉為 **COX-2 偏好性抑制**（COX-2 選擇性高於 COX-1），透過抑制花生四烯酸代謝，顯著降低前列腺素 E2（PGE2）的合成，從而達到抗炎、鎮痛效果。與傳統非選擇性 NSAID 相比，其胃腸道副作用負擔相對較輕。文獻（Bellamy, 1997）確認其 COX-2 偏好性機轉，口服吸收迅速，達峰時間 1-2 小時，半衰期 6-8 小時。

強直性脊椎炎（AS）是一種 HLA-B27 相關的慢性炎症性脊椎關節病，核心致病因子包括 IL-1、IL-6、TNF-α 及前列腺素。**前列腺素在 AS 脊椎關節炎症和疼痛中扮演關鍵角色**，因此 Etodolac 的 COX-2 抑制機轉與 AS 病生理高度吻合。多項臨床研究（1989-1997 年）已直接記載 Etodolac 在 AS 患者中的療效，並與 naproxen、piroxicam 等標準 NSAID 相當。

值得注意的是，ASAS/EULAR 臨床指引明確將 NSAID 列為 AS 的**一線治療**，且 Annals of the Rheumatic Diseases（2011）建議將 NSAID 攝取量列為 AS 臨床試驗的核心結果指標，進一步確認此藥物類別在 AS 治療中的核心地位。本次 TxGNN 預測可視為對已知臨床知識的圖譜驗證，而非全新假說。

---

## 臨床試驗證據

*以下為強直性脊椎炎相關背景臨床試驗（Etodolac 或 NSAID 類可能作為背景用藥）：*

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05164198](https://clinicaltrials.gov/study/NCT05164198) | Phase 4 | 未知 | 448 | 穩定期 AS 患者 TNF 抑制劑標準劑量 vs. 減量之隨機試驗；NSAID 可能作為背景用藥，Etodolac 非主要干預措施 |

> 目前無直接以 Etodolac 為主要干預措施的 AS 隨機對照試驗登記。歷史療效資料主要來自下方文獻。

---

## 文獻證據

*以下為 Etodolac 用於強直性脊椎炎的相關文獻（優先順序：綜合回顧 > 臨床試驗 > 安全性研究）：*

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [1717225](https://pubmed.ncbi.nlm.nih.gov/1717225/) | 1991 | 綜合回顧 | Drugs | Etodolac 有效治療 RA、OA 及 AS，鎮痛效果不亞於其他 NSAID；腹痛和消化不良為主要副作用 |
| [2146130](https://pubmed.ncbi.nlm.nih.gov/2146130/) | 1990 | 系統性概述 | Eur J Rheumatol Inflamm | 多項隨機雙盲研究：Etodolac（200-300 mg bid）療效與 naproxen、piroxicam 相當，適用 RA、OA 及 AS |
| [17694363](https://pubmed.ncbi.nlm.nih.gov/17694363/) | 1997 | 臨床回顧 | Inflammopharmacology | 確認 Etodolac COX-2 偏好性機轉；廣泛用於 RA、AS、痛風及 OA，口服吸收良好 |
| [2525800](https://pubmed.ncbi.nlm.nih.gov/2525800/) | 1989 | 開放性臨床試驗 | Rev Med Interne | 974 位風濕科醫師、4,947 名 RA/AS/OA 患者：Etodolac 600 mg/d 初始劑量顯示良好療效與耐受性 |
| [2150569](https://pubmed.ncbi.nlm.nih.gov/2150569/) | 1990 | 大型開放性試驗 | Rheumatol Int | 法國兩項大型研究（含 51,355 名上市後監測患者），確認 Etodolac 在 RA、AS、OA 的安全性 |
| [2150568](https://pubmed.ncbi.nlm.nih.gov/2150568/) | 1990 | 上市後監測 | Rheumatol Int | 義大利、瑞士、英國、法國 8,334 名患者（含 AS）研究，確認 Etodolac 上市後良好安全性 |
| [22071858](https://pubmed.ncbi.nlm.nih.gov/22071858/) | 2011 | Cochrane 回顧 | Cochrane Database Syst Rev | NSAID（含 Etodolac）與 methotrexate 併用於炎症性關節炎（含 AS、psoriatic arthritis）之安全性系統性回顧 |
| [20829199](https://pubmed.ncbi.nlm.nih.gov/20829199/) | 2011 | 臨床指引 | Ann Rheum Dis | ASAS 建議將 NSAID 攝入量列為 AS 臨床試驗核心結果指標，反映 NSAID 在 AS 治療的核心地位 |
| [21140116](https://pubmed.ncbi.nlm.nih.gov/21140116/) | 2010 | 開放性前瞻性試驗 | Singapore Med J | 評估 pamidronate 於 NSAID 難治/不耐受型 AS 的療效（間接確認 NSAID 為 AS 標準一線治療） |
| [24449987](https://pubmed.ncbi.nlm.nih.gov/24449987/) | 2013 | 回顧 | IMAJ | 軸向脊椎關節炎（含 AS）的診斷挑戰及評估方法回顧 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

> Etodolac 屬 NSAID 類藥物，常見注意事項包括：胃腸道刺激（腹痛、消化不良）、長期使用的心血管風險（血壓上升、水腫）、腎功能影響，以及與抗凝血藥物的潛在交互作用。具體警語、禁忌症及完整藥物交互作用資訊，請查閱原廠或 FDA/EMA 核准仿單。本次 Evidence Pack 尚未取得 TFDA/衛生署相關安全性資料，此為待補充的關鍵資料缺口。

---

## 結論與下一步

**決策：Proceed with Guardrails（強直性脊椎炎）**

**理由：**
Etodolac 的 COX-2 選擇性抑制機轉與強直性脊椎炎的前列腺素介導炎症病生理高度一致；多篇 1989-1997 年臨床研究已直接記載其在 AS 中的療效，ASAS/EULAR 指引亦支持 NSAID 為 AS 一線治療。然而，Etodolac 目前在香港無上市許可，缺乏本地監管資料，且近期尚無高等級直接 RCT 支持。

**若要推進需要：**
- 補充完整作用機轉（MOA）資料，建議查詢 DrugBank API（DB00749）
- 取得香港衛生署或 TFDA 核准仿單，補充警語、禁忌症及藥物交互作用資料
- 評估是否可透過 bibliographic application（文獻申請）申請香港上市
- 針對目標族群（AS 患者）制定風險管理計畫，重點監測心血管及胃腸道安全性
- 對於排名 4（Spondyloarthropathy susceptibility）、8（Rheumatoid Vasculitis）、9（Hypermobility of Coccyx）可列為**研究方向**，待機轉資料補齊後再評估
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

