---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 755
evidence_level: L5
indication_count: 5
---

# Tocilizumab
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

# Tocilizumab：從（未上市，無核准適應症資料）到僵直性脊椎炎

## 一句話總結

Tocilizumab（DrugBank ID: DB06273）是人源化抗 IL-6 受體單株抗體，目前**未於香港上市**，無許可證與核准適應症資料。TxGNN 模型預測其對**僵直性脊椎炎 (Ankylosing Spondylitis)** 可能有效（預測分數 99.99%），但唯二直接測試此假設的兩項 Phase 3 RCT（NCT01209689、NCT01209702）均因療效不足提前終止，屬於**負向直接證據**。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無官方資料（香港未上市，無許可證）；國際文獻顯示已核准用於類風濕性關節炎、幼年特發性關節炎、巨細胞動脈炎等 |
| 預測新適應症 | 僵直性脊椎炎 (Ankylosing Spondylitis) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1（兩項 Phase 3 RCT 皆為負向結果） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 正式的作用機轉資料。根據證據包中的文獻摘要，Tocilizumab 是人源化抗 IL-6 受體單株抗體，已核准用於類風濕性關節炎、全身型與多關節型幼年特發性關節炎，以及巨細胞動脈炎。僵直性脊椎炎與類風濕性關節炎同屬慢性發炎性關節病變，理論上共享部分細胞激素驅動的發炎路徑，這是 TxGNN 判斷兩者關聯的基礎。

然而，僵直性脊椎炎（及中軸型脊椎關節炎）的主要致病機轉普遍被認為以 **TNF-α/IL-17/IL-23 軸**為核心，IL-6 並非關鍵路徑。這項機轉落差已在臨床上得到驗證：兩項專屬測試 tocilizumab 於 AS 患者的 Phase 3 RCT（NCT01209689、NCT01209702）皆因期中分析未達療效標準而提前終止，PMID 23765873（BUILDER-1/2 試驗）進一步證實 tocilizumab 對 AS 症狀僅有短期、有限的效果。這使得本候選雖有高 TxGNN 分數與充分證據數量（達 L1 等級），但證據方向為**負向**。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | 已終止 | 113 | TCZ vs 安慰劑於 TNF 拮抗劑反應不佳之 AS 患者，期中分析未達療效標準而終止 |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | 已終止 | 306 | TCZ vs 安慰劑於 NSAID 治療失敗、TNF-naïve 之 AS 患者，同樣提前終止 |
| [NCT07477795](https://clinicaltrials.gov/study/NCT07477795) | Phase 2 | 尚未招募 | 52 | Secukinumab（非 tocilizumab）於重度 Takayasu 動脈炎之貝氏設計試驗，機轉參考價值有限 |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | 已完成 | 60 | Tocilizumab 對 RA 患者濾泡輔助 T 細胞的體內外機轉研究，非 AS 療效終點 |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | 招募中 | 2500 | 全身性發炎疾病細胞激素生物標記登錄研究，非藥物介入 |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | 已完成 | 1431 | Infliximab（非 tocilizumab）真實世界使用登錄 |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | 未知 | 750000 | 75 萬人巨型觀察研究，涵蓋多種生物製劑與免疫調節疾病，無藥物-疾病專屬因果推論力 |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | 尚未招募 | 80 | 風濕病患者接受全肩關節置換術之圍手術期免疫抑制劑管理研究 |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | 招募中 | 10000 | 韓國生物製劑與標靶治療登錄，觀察性、非介入性 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT | Ann Rheum Dis | BUILDER-1/2：評估 tocilizumab 於 AS 患者短期症狀療效與安全性 |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | 系統性回顧/網絡統合分析 | Medicine | 比較各生物製劑於 AS 之療效，含 tocilizumab 相對效果評估 |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Review | Semin Arthritis Rheum | RA、PsA、AS 二線生物製劑選擇策略之義大利專家共識 |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Cohort/Meta分析 | Clin Rheumatol | AS 及非放射學軸型 SpA 患者接受生物製劑之嚴重感染風險統合分析 |
| [31852268](https://pubmed.ncbi.nlm.nih.gov/31852268/) | 2020 | Cohort | Expert Rev Clin Immunol | 發炎性關節炎患者非生物製劑 vs 生物製劑之感染風險比較 |
| [20851032](https://pubmed.ncbi.nlm.nih.gov/20851032/) | 2010 | Case report | Joint Bone Spine | 難治型 AS 併克隆氏症患者使用 tocilizumab 之個案 |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case report | Front Med | AS 併 AA 型類澱粉沉積症以 tocilizumab 成功治療之兩例報告 |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflamm Allergy Drug Targets | AS 中 IL-6 拮抗簡短回顧，討論機轉可能性 |
| [19822066](https://pubmed.ncbi.nlm.nih.gov/19822066/) | 2009 | Review | Clin Exp Rheumatol | RA 與 AS 生物製劑治療綜述，指出抗 TNF 治療對 AS 不能抑制影像學進展 |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Curr Opin Rheumatol | TNF 抑制劑治療失敗之軸型 SpA 替代療法選項回顧 |

---

## 香港上市資訊

目前無香港許可證登記（`market_status`：未上市，`total_licenses`：0）。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 其他候選適應症總覽（同一 Evidence Pack）

本次評估包 (TW-DB06273-multi) 共含 5 個 TxGNN 預測候選，除上述僵直性脊椎炎外，其餘四項皆證據薄弱或負向：

| Rank | 適應症 | TxGNN 分數 | 證據等級 | 建議決策 | 備註 |
|------|--------|-----------|---------|---------|------|
| 2 | Rheumatoid vasculitis | 99.98% | L4 | Research Question | 機轉上合理（RA、GCA 已核准），但直接證據僅個案報告，方向矛盾（有成功案例也有 tocilizumab 誘發血管炎樣反應之個案） |
| 3 | Hypermobility of coccyx | 99.98% | L5 | Hold | 無任何試驗或文獻支持，判定為本體論雜訊配對 |
| 4 | Spondyloarthropathy, susceptibility to | 99.98% | L5 | Hold | 唯一文獻為機轉性免疫學研究，非療效證據 |
| 5 | Inflammatory spondylopathy | 99.98% | L1 | Hold | 與 Rank 1 共用同組 Phase 3 終止試驗，同為負向直接證據 |

---

## 結論與下一步

**決策：Hold**

**理由：**
- 主要候選（僵直性脊椎炎）雖達 L1 證據等級，但關鍵的兩項 Phase 3 RCT 皆因療效不足提前終止，屬於直接負向證據，與 IL-6 並非 AS 主要致病路徑的機轉推論一致。
- 安全性資料（DG001，Blocking）與正式 MOA 資料（DG002，High）皆缺，無法進入 S1 安全性初評，構成流程性阻斷。
- 其餘四個候選中，Rank 2 僅有個案報告等級證據且方向矛盾，Rank 3、4 缺乏臨床對應，Rank 5 與 Rank 1 共享同一負向試驗結果。

**若要推進需要：**
- 補齊 TFDA/香港仿單之警語與禁忌資料（解除 DG001 阻斷）
- 透過 DrugBank API 取得正式 MOA 資料（DG002）
- 若要重新評估 Rank 1，需檢視 NCT01209689/NCT01209702 終止原因之次族群分析，確認是否存在特定亞群可能有反應
- Rank 2（rheumatoid vasculitis）可列為機轉假說觀察對象，但需等待更多對照性研究，目前不足以支持任何決策推進
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

