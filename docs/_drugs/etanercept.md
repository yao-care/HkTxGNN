---
layout: default
title: Etanercept
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 6
---

# Etanercept
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Etanercept：從自體免疫關節炎治療到類風濕性血管炎

## 一句話總結

Etanercept 是 TNF-α 抑制劑（可溶性 TNF 受體–Fc 融合蛋白），在文獻中已用於類風濕性關節炎等自體免疫關節疾病。
TxGNN 模型預測它可能對**類風濕性血管炎 (Rheumatoid Vasculitis)** 有效，但目前只有 **1 個相關的 Phase 2 試驗（適應症為韋格納肉芽腫，並非類風濕性血管炎）**和 **1 篇系統性回顧**，其餘 **6 個試驗**與多數文獻都無法直接支持這個方向。文獻中另有不少 etanercept 誘發血管炎的通報。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 類風濕性血管炎 (Rheumatoid Vasculitis) |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L3（僅有系統性回顧與觀察性研究，無針對該適應症的 RCT） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏 DrugBank 提供的詳細作用機轉資料。根據文獻，etanercept 是由 p75 TNF 受體與 IgG1 Fc 片段組成的融合蛋白，能結合 TNF-α 並阻斷其活性。TNF-α 是類風濕性關節炎發炎反應的核心細胞激素，這是預測的主要理論基礎。

類風濕性血管炎是類風濕性關節炎最嚴重的關節外表現之一，過去以皮質類固醇和免疫抑制劑治療。近年已有生物製劑被用於此病，並有系統性回顧整理相關經驗。在 ANCA 相關血管炎中，TNF-α 也被認為參與病理，但 TNF 阻斷在該病的角色仍有爭議。

不過這個預測的證據明顯偏弱，甚至互相矛盾。唯一的 Phase 2 試驗（NCT00001901）針對韋格納肉芽腫，是另一種血管炎，不能直接外推。此外，多篇病例報告與藥物安全性研究描述 etanercept 相關或誘發的血管炎，形成矛盾的安全性訊號。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Phase 2 | 完成 | 60 | Etanercept 用於韋格納肉芽腫（血管炎的一種）。疾病相關但不是類風濕性血管炎，不能直接外推 |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | 尚未招募 | 80 | 風濕病患者接受肩關節置換術前，免疫抑制劑停藥時間的管理。並未測試 etanercept 對血管炎的效果 |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | N/A | 完成 | 1754 | 中度類風濕性關節炎的真實世界治療路徑觀察，無血管炎結果 |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | N/A | 完成 | 808 | 中國類風濕性關節炎患者使用生物 DMARD 的橫斷面研究，無血管炎結果 |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | N/A | 完成 | 184 | Tocilizumab 治療類風濕性關節炎的非介入性研究，無血管炎結果 |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | 未知 | 750000 | 使用生物製劑後發生其他免疫媒介發炎疾病風險的大型登錄研究，探討風險而非治療 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | 系統性回顧 | Clin Rheumatol | 依 PRISMA 整理生物製劑用於類風濕性血管炎的文獻，是與此適應症最直接相關的證據 |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Review | Nephrol Dial Transplant | 討論 TNFα 阻斷在 ANCA 相關血管炎與腎絲球腎炎的角色，指出 TNFα 參與病理，但療效是否適用仍待釐清 |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | 世代研究 | RMD Open | BSRBR-RA 資料，比較 TNF 抑制劑與傳統 DMARD 治療的類風濕性關節炎患者發生類狼瘡及類血管炎事件的風險（屬安全性研究） |
| [15624748](https://pubmed.ncbi.nlm.nih.gov/15624748/) | 2004 | Review | J Drugs Dermatol | 回顧 etanercept 的用途與副作用，皮膚副作用少見，包括注射部位反應、皮膚型狼瘡與皮膚血管炎 |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | 免疫學／不良事件 | Scand J Immunol | 探討 etanercept 與 infliximab 相關皮膚血管炎的免疫機轉，屬罕見的自體免疫副作用 |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | 病例報告 | Arthritis Rheum | 類風濕性關節炎患者使用 etanercept 後出現結節加速形成與血管炎 |
| [11792895](https://pubmed.ncbi.nlm.nih.gov/11792895/) | 2002 | 病例報告 | Rheumatology (Oxford) | Etanercept 與 infliximab 相關的皮膚血管炎 |
| [15801034](https://pubmed.ncbi.nlm.nih.gov/15801034/) | 2005 | 病例報告 | J Rheumatol | Etanercept 治療期間出現增生性狼瘡腎炎與白血球破裂性血管炎 |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | 病例報告 | Case Rep Med | 類風濕性關節炎患者接受抗 TNF 治療期間發生大血管血管炎 |
| [19648728](https://pubmed.ncbi.nlm.nih.gov/19648728/) | 2009 | 病例報告 | Dermatology | 使用 etanercept 的類風濕性關節炎患者，散播性帶狀疱疹被誤認為類風濕性血管炎，延誤診斷 |

## 香港上市資訊

共 7 張許可證，以下列出 5 張主要許可證，皆由 Pfizer 或 Sandoz 持有。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-55983 | ENBREL SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 25MG | PFIZER CORPORATION HONG KONG LIMITED |
| HK-59796 | ENBREL SOLUTION FOR INJ IN PRE-FILLED PEN 50MG | PFIZER CORPORATION HONG KONG LIMITED |
| HK-55984 | ENBREL SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 50MG | PFIZER CORPORATION HONG KONG LIMITED |
| HK-48914 | ENBREL PDR & SOLVENT FOR INJ 25MG | PFIZER CORPORATION HONG KONG LIMITED |
| HK-67841 | ERELZI SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 25MG/0.5ML | SANDOZ HONG KONG LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

另外，文獻中有多篇病例報告與藥物安全性研究指出，etanercept 可能與皮膚血管炎、類狼瘡反應等事件相關。這與預測的治療方向相反，評估時需特別留意。

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數很高（99.71%），但唯一的 Phase 2 試驗針對的是另一種血管炎（韋格納肉芽腫），沒有 etanercept 用於類風濕性血管炎的 RCT。
- 文獻中同時存在 etanercept 誘發或相關血管炎的安全性訊號，風險效益尚不明朗。

**若要推進需要：**
- 仔細閱讀系統性回顧（PMID 33058033）全文，確認 etanercept 在類風濕性血管炎中的實際療效與安全性數據
- 取得 DrugBank 的作用機轉資料與香港衛生署仿單的警語、禁忌
- 設計或尋找針對類風濕性血管炎的前瞻性研究，並釐清「治療性」與「藥物誘發性」血管炎的區別

**補充：**同一份預測清單中，第 3 位的發炎性脊椎病變、第 5 位的多關節型幼年類風濕性關節炎與第 6 位的脊椎疾病，已有 Phase 3 RCT 支持（證據等級 L1）。但這些疾病多半屬 etanercept 已核准的適應症，比較像既有適應症的確認，而非真正的老藥新用。第 2 位的尾骨過度活動與第 4 位的 Kummell 病則沒有任何試驗或文獻，應維持 Hold。

本報告結果僅供研究參考，不構成醫療建議，所有預測均需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

