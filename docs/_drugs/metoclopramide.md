---
layout: default
title: Metoclopramide
parent: 中證據等級 (L3-L4)
nav_order: 492
evidence_level: L3
indication_count: 5
---

# Metoclopramide
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

# Metoclopramide：從止吐／腸胃促動力用途到胃潰瘍（Gastric Ulcer）

## 一句話總結

Metoclopramide 是一種 D2 受體拮抗劑／5-HT4 受體促效劑，目前已知用途為止吐及促進腸胃排空，本評估中香港未有上市許可證資料。TxGNN 模型預測它可能對**胃潰瘍 (Gastric Ulcer)** 有效，目前有 **2 個臨床試驗**和 **20 篇文獻**可供參考，但直接支持該適應症的證據仍薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無香港許可證資料；已知全球用途為止吐與腸胃促動力（見下方機轉說明） |
| 預測新適應症 | 胃潰瘍 (Gastric Ulcer) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L3 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

正式的 DrugBank 作用機轉資料目前缺失（資料缺口 DG002）。根據收集到的文獻（如 PMID 6336644），Metoclopramide 是中樞與周邊多巴胺（D2）拮抗劑，其藥理作用在於促進胃排空、增加下食道括約肌張力，並透過作用於延腦化學受體觸發區產生止吐效果，臨床上常用於預防化療（如順鉑）引起的嘔吐。

胃潰瘍的標準治療機轉是抑酸（PPI、H2 拮抗劑）或黏膜保護，Metoclopramide 並不具備這類藥理作用。TxGNN 給出 99.93% 的高分，較可能反映知識圖譜中「胃部」相關節點在拓撲結構上的鄰近性，而非直接的疾病修飾證據。其在胃潰瘍情境下較合理的角色，僅限於輔助改善胃排空延遲相關症狀，或用於上消化道出血內視鏡前清空胃內容物以利視野，並非治療潰瘍本身。因此機轉層面上，此預測的直接治療合理性有限。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03747107](https://clinicaltrials.gov/study/NCT03747107) | N/A | 完成 | 19 | 蘇格蘭 Tayside 藥師主導之初級照護處方安全品質改善計畫，非針對 Metoclopramide 治療胃潰瘍之介入性試驗，相關性低 |
| [NCT05746377](https://clinicaltrials.gov/study/NCT05746377) | Phase 4 | 狀態未知 | 60 | 評估上消化道出血病人內視鏡前給予 Metoclopramide 清空胃內容物、改善視野與減少重複內視鏡需求，非直接治療潰瘍本身之療效終點 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16807979](https://pubmed.ncbi.nlm.nih.gov/16807979/) | 2006 | RCT | Yonsei Med J | 靜脈注射 Metoclopramide 併 Ranitidine 可減少門診腹腔鏡婦科手術病人麻醉誘導前之胃內容物殘留 |
| [6336644](https://pubmed.ncbi.nlm.nih.gov/6336644/) | 1983 | Review | Ann Intern Med | 綜述 Metoclopramide 藥理與臨床應用，說明其止吐及腸胃促動力作用，未涉及潰瘍治療機轉 |
| [19225](https://pubmed.ncbi.nlm.nih.gov/19225/) | 1977 | Review | Drugs | 胃十二指腸潰瘍藥物治療綜述 |
| [797497](https://pubmed.ncbi.nlm.nih.gov/797497/) | 1976 | Review | Clin Pharmacokinet | 討論藥物與疾病（含胃潰瘍）對胃排空速率的影響 |
| [775822](https://pubmed.ncbi.nlm.nih.gov/775822/) | 1976 | 臨床研究（德文） | ZFA | 以 Metoclopramide 治療胃十二指腸潰瘍 |
| [4779253](https://pubmed.ncbi.nlm.nih.gov/4779253/) | 1973 | 臨床研究 | Curr Med Res Opin | 探討吸菸、Metoclopramide 與 Carbenoxolone 對胃潰瘍膽汁逆流之影響 |
| [6106882](https://pubmed.ncbi.nlm.nih.gov/6106882/) | 1980 | 臨床研究（德文） | Medizinische Klinik | 胃潰瘍保守治療綜述 |
| [2730234](https://pubmed.ncbi.nlm.nih.gov/2730234/) | 1989 | 動物實驗 | Arch Int Pharmacodyn Ther | Metoclopramide 於白老鼠阿斯匹靈誘發及幽門結紮胃潰瘍模型中具保護作用，效果與 Ranitidine 比較 |
| [6436177](https://pubmed.ncbi.nlm.nih.gov/6436177/) | 1984 | 動物實驗 | Indian J Physiol Pharmacol | 天竺鼠實驗誘發性胃潰瘍模型中，Metoclopramide 具保護作用但不影響胃酸分泌 |
| [6782467](https://pubmed.ncbi.nlm.nih.gov/6782467/) | 1981 | 臨床研究（德文） | MMW | Domperidone 與 Metoclopramide 對血清 Gastrin 濃度及胃酸分泌之影響，兩者均未顯著改變 |

## 安全性考量

安全性資訊請參考原廠仿單。

（TFDA 仿單警語／禁忌症資料為阻斷性缺口 DG001，目前無法進行 S1 安全性初評；藥物交互作用查詢亦無結果。）

## 結論與下一步

**決策：Hold**

**理由：**
- Metoclopramide 的已知藥理機轉（多巴胺拮抗、促胃排空）與胃潰瘍標準治療所需的抑酸／黏膜保護機轉本質不同，證據回顧本身也指出 TxGNN 高分較可能反映知識圖譜拓撲鄰近性而非真實療效訊號。
- 現有 2 個臨床試驗均非以「治療胃潰瘍」為主要終點（分別為處方安全品質改善計畫與內視鏡前清胃輔助用藥），直接證據不足；文獻證據多為 1970-1980 年代小型研究或動物實驗。
- TFDA 仿單警語與禁忌症資料缺失（DG001，阻斷性），目前無法完成安全性初評，不宜進入下一階段。

**若要推進需要：**
- 取得 TFDA／原廠仿單完整警語與禁忌症資料（DG001），完成 S1 安全性初評
- 補齊正式 DrugBank 作用機轉資料（DG002），釐清機轉關聯性
- 若要繼續此方向，需針對「Metoclopramide 治療胃潰瘍」設計具明確療效終點（如潰瘍癒合率、症狀緩解）的介入性試驗，而非僅以促動力／清胃為終點的間接研究
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

