---
layout: default
title: Ceftazidime
parent: 中證據等級 (L3-L4)
nav_order: 171
evidence_level: L4
indication_count: 10
---

# Ceftazidime
{: .fs-9 }

證據等級: **L4** | 預測適應症: **10** 個
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

# Ceftazidime：從細菌感染到高澱粉酶血症

## 一句話總結

Ceftazidime 是第三代頭孢菌素類抗生素，資料中未記載原適應症，依藥物類別推定用於細菌感染。
TxGNN 預測它可能對**高澱粉酶血症 (Hyperamylasemia)** 有效，但目前只有 **0 個臨床試驗**和 **1 篇文獻**，且文獻僅為間接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia) |
| TxGNN 預測分數 | 99.51% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ceftazidime 屬於第三代頭孢菌素，一般認為它抑制細菌細胞壁合成，對腸內菌科與綠膿桿菌有活性。

高澱粉酶血症是實驗室檢驗異常，不是可直接用抗生素治療的感染。唯一的關聯是抗生素預防可能降低 ERCP 後胰臟炎，並連帶減少澱粉酶上升，這只是預防感染帶來的間接效果。Ceftazidime 本身對澱粉酶沒有已知的直接作用。

因此這個預測的機轉支持度低，較可能是知識圖譜的關聯假象，而不是真正可轉化的新用途。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [11985972](https://pubmed.ncbi.nlm.nih.gov/11985972/) | 2001 | 前瞻性研究（研究設計待確認） | J Gastrointest Surg | 探討常規抗生素預防能否降低 ERCP 後胰臟炎。摘要被截斷，無法確認是否使用 ceftazidime |

## 香港上市資訊

共 8 張許可證，以下列出 5 張主要許可證。資料中的劑型與核准適應症皆為空白。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-21523 | FORTUM FOR INJ 2G | SANDOZ HONG KONG LIMITED |
| HK-21522 | FORTUM FOR INJ 500MG | SANDOZ HONG KONG LIMITED |
| HK-21251 | FORTUM FOR INJ 1G | SANDOZ HONG KONG LIMITED |
| HK-57297 | CEFTAZIDIME FOR INJ 1G (REYOUNG) | JINDUN PHARMA (H.K.) LIMITED |
| HK-61251 | CEFTAZIDIME POWDER FOR SOLUTION FOR INJECTION 2G | CEUTICAL TRADING COMPANY LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 其他預測適應症（證據較強者）

排名第一的高澱粉酶血症證據薄弱。同一批預測中，以下兩項較值得優先評估：

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 | 重點 |
|-----------|-----------|---------|------|------|
| 泌尿道感染 (UTI) | 99.41% | L2 | Proceed with Guardrails | 有數個 Phase 2 試驗，如 [NCT00690378](https://clinicaltrials.gov/study/NCT00690378)（NXL104/ceftazidime 用於複雜性 UTI）、[NCT02497781](https://clinicaltrials.gov/study/NCT02497781)（兒童複雜性 UTI）。多數為 ceftazidime-avibactam 複方，不能直接外推到單方 |
| 感染性中耳炎 | 99.19% | L3 | Research Question | 1992–2000 年數個小型研究，涵蓋綠膿桿菌所致慢性化膿性中耳炎的兒童，如 [PMID 10826908](https://pubmed.ncbi.nlm.nih.gov/10826908/)（ceftazidime 對 aztreonam，各 15 名兒童）。證據老舊且規模小 |

UTI 很可能是已核准的既有用途，而不是真正的老藥新用，需對照許可證確認。

其餘預測適應症（多囊性高黏滯症候群、先天性無白蛋白血症、Ureaplasma 尿道炎、血型不合等）機轉不合理或缺乏證據，皆為 Hold。

## 結論與下一步

**決策：Hold**

**理由：**
- 高澱粉酶血症是檢驗異常，機轉上只有間接關聯，沒有臨床試驗，僅有 1 篇未確認使用 ceftazidime 的文獻。
- 香港衛生署仿單的警語與禁忌資料缺漏，屬阻擋性缺口，無法進入安全性篩選。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌與核准適應症（許可證的適應症欄位目前為空）
- 補充作用機轉資料（DrugBank）
- 確認 PMID 11985972 的全文，看是否使用 ceftazidime 及是否以澱粉酶為終點
- 建議把評估重心轉向 UTI 與慢性化膿性中耳炎，並先確認其是否已是核准適應症

> 本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

