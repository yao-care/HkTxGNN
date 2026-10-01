---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 871
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

# Tocilizumab：從類風濕性關節炎到強直性脊椎炎

## 一句話總結

Tocilizumab 是抗介白素-6 受體 (IL-6R) 的單株抗體，文獻中主要用於類風濕性關節炎等疾病。
TxGNN 模型預測它可能對**強直性脊椎炎 (Ankylosing Spondylitis)** 有效，但直接相關的 **2 個 Phase 2/3、Phase 3 隨機對照試驗皆提前終止**，未建立正面療效。另有多篇文獻（含系統性回顧、病例報告），目前不建議推進。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未記載適應症文字；文獻描述主要用於類風濕性關節炎、幼年型特發性關節炎 |
| 預測新適應症 | 強直性脊椎炎 (Ankylosing Spondylitis) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L3（依規則判定，說明見下） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

**證據等級說明：** 資料包自動標示為 L1，但 L1 需有 ≥2 個「已完成」的 Phase 3 RCT。兩個相關 RCT（NCT01209689、NCT01209702）的狀態都是「提前終止」，不符合 L1。因此改依系統性回顧與觀察性資料判定為 L3。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。依一般藥理知識，Tocilizumab 阻斷 IL-6 受體，抑制 IL-6 介導的發炎訊號。IL-6 在強直性脊椎炎患者體內偏高，所以模型把它連到這個疾病有其生物學依據。

但強直性脊椎炎的主要致病軸是 **TNF 與 IL-17/IL-23**，IL-6 不是核心驅動因子。兩個針對 AS 的 RCT 提前終止，也暗示阻斷 IL-6 對軸向疾病未必有效。

文獻中有 2 則病例報告顯示，Tocilizumab 可能改善 AS 合併 AA 類澱粉沉積症的情況。這屬於另一條機轉，不能當作 AS 本身有效的證據。

---

## 臨床試驗證據

資料包共列出 8 個與此預測相關的試驗，以下列出與 AS 或 Tocilizumab 較相關者（其餘為與 Tocilizumab 無直接關係的觀察性研究或其他藥物試驗，從略）。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | 提前終止 | 113 | 隨機、雙盲、安慰劑對照；TNF 拮抗劑反應不佳的 AS 患者，Tocilizumab 8 或 4 mg/kg 靜脈注射 vs 安慰劑，每 4 週一次共 24 週。 |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | 提前終止 | 306 | 無縫式、隨機、雙盲、安慰劑對照；NSAID 失敗且未用過 TNF 拮抗劑的 AS 患者，評估症狀改善與結構損傷抑制。 |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | 完成 | 60 | 機轉研究：Tocilizumab 對類風濕性關節炎患者濾泡輔助 T 細胞與 B 細胞成熟的影響，無臨床療效指標。 |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | 招募中 | 10,000 | 韓國生物製劑登錄研究，涵蓋類風濕性關節炎、AS、乾癬性關節炎，觀察安全性，無療效假設。 |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | N/A | 招募中 | 2,500 | 法蘭德斯系統性發炎疾病的細胞激素與生物標記縱貫觀察。 |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | 未知 | 750,000 | 以登錄資料評估單一免疫介導發炎疾病患者使用生物製劑後，新發其他免疫疾病的風險，無療效資料。 |

兩個 RCT 的標題在資料包中有截斷，其藥物與族群需再向原始登錄頁面核實。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT | Ann Rheum Dis | 彙整 BUILDER-1、BUILDER-2 兩個隨機安慰劑對照試驗，評估 Tocilizumab 在 AS 的短期症狀療效與安全性（摘要未提供結果數據）。 |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | 系統性回顧／網絡統合分析 | Medicine | 比較各種生物製劑用於 AS 的相對療效。 |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | 統合分析 | Clin Rheumatol | 評估 AS 與非放射學軸向脊椎關節炎患者使用生物製劑的嚴重感染風險。 |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflamm Allergy Drug Targets | 簡述在 AS 中拮抗 IL-6 的理論基礎。 |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Curr Opin Rheumatol | 討論 TNF 抑制劑無效的 AS 患者有哪些替代療法。 |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Review／世代 | Semin Arthritis Rheum | 義大利 ITABIO 小組整理類風濕性關節炎、乾癬性關節炎、AS 的第二線生物製劑選擇策略。 |
| [31852268](https://pubmed.ncbi.nlm.nih.gov/31852268/) | 2020 | Review | Expert Rev Clin Immunol | 比較發炎性關節炎使用非生物與生物製劑的感染風險。 |
| [39963138](https://pubmed.ncbi.nlm.nih.gov/39963138/) | 2025 | Review | Front Immunol | 自體免疫關節炎患者使用生物與標靶製劑時，結核病風險的篩檢與預防。 |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | 病例報告 | Front Med | 2 例 AS 合併 AA 類澱粉沉積症，使用 Tocilizumab 治療成功。 |
| [20851032](https://pubmed.ncbi.nlm.nih.gov/20851032/) | 2010 | 病例報告 | Joint Bone Spine | 1 例 TNF 拮抗劑難治的 AS 合併克隆氏症患者使用 Tocilizumab（無摘要）。 |

---

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-59200 | ACTEMRA 輸注用濃縮液 400mg/20ml | ROCHE HONG KONG LIMITED |
| HK-59201 | ACTEMRA 輸注用濃縮液 200mg/10ml | ROCHE HONG KONG LIMITED |
| HK-59202 | ACTEMRA 輸注用濃縮液 80mg/4ml | ROCHE HONG KONG LIMITED |
| HK-63771 | ACTEMRA 預充填注射筒 162mg/0.9ml | ROCHE HONG KONG LIMITED |

資料包中這 4 張許可證的劑型與核准適應症欄位皆為空白，無法確認香港核准的適應症是否包含 AS。

---

## 安全性考量

安全性資訊請參考原廠仿單。資料包中的警語與禁忌症皆為資料缺口，藥物交互作用查詢也無結果。

文獻僅提示一般性的關注方向，不能取代仿單：生物製劑在 AS 族群有嚴重感染風險，使用前須做結核病篩檢與預防評估。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個直接針對 AS 的 RCT 都提前終止，沒有正面療效證據。AS 的主要致病軸是 TNF 與 IL-17/IL-23，IL-6R 阻斷缺乏強的機轉支持。
- 香港仿單的警語與禁忌症資料缺失（DG001，屬阻擋級缺口），目前無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單（警語、禁忌症、核准適應症）。
- 補齊 DrugBank 的作用機轉資料。
- 取得 BUILDER-1/2 完整結果與終止原因，並核實兩個試驗被截斷的標題。
- 與已核准的 TNF 與 IL-17 抑制劑比較，評估 Tocilizumab 在 AS 是否有臨床定位。
- 同批預測中，類風濕性血管炎（排名 2）有大血管血管炎相關資料，但因 Tocilizumab 可能誘發血管炎反應，建議另案評估。

本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

