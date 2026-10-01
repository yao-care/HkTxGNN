---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 764
evidence_level: L5
indication_count: 5
---

# Risperidone
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

# Risperidone：從抗精神病藥物到家族性水平凝視麻痺合併進行性脊柱側彎

## 一句話總結

Risperidone 是非典型抗精神病藥物，香港已有多張許可證上市，但資料中未載明核准適應症。
TxGNN 預測它可能對**家族性水平凝視麻痺合併進行性脊柱側彎 (gaze palsy, familial horizontal, with progressive scoliosis)** 有效，但這筆預測**沒有任何臨床試驗或文獻支持**，僅為模型預測 (L5)。

> 本次共有 5 個預測適應症，其中證據最多的是**拔毛症 (trichotillomania)**（排名第 5，L4，僅有個案報告與小型病例系列），詳見下方「其他預測適應症」。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 家族性水平凝視麻痺合併進行性脊柱側彎 |
| TxGNN 預測分數 | 99.76% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Risperidone 一般認為透過 D2／5-HT2A 受體拮抗發揮作用。

這個預測的合理性很低。該疾病與 ROBO3 相關，是腦幹與脊柱的發育異常，和 D2／5-HT2A 拮抗之間沒有明顯關聯。0.998 的高分較可能是知識圖譜的假象，不是真實的藥理訊號。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 其他預測適應症

| 排名 | 疾病 | 分數 | 證據等級 | 說明 |
|------|------|------|---------|------|
| 2 | Asperger 症候群易感性 | 99.74% | L5 | 無試驗或文獻。Risperidone 臨床上用於自閉症相關易怒，但那是治療症狀，並非針對此易感性基因座。 |
| 3 | 髮育不全-腦-少汗症候群 | 99.69% | L5 | 超罕見症候群，無已知藥理依據。 |
| 4 | Phelan-McDermid 症候群 | 99.59% | L4 | 僅有間接證據：1 篇臨床處置回顧、1 篇斑馬魚 shank3 模型研究、1 篇雙相情緒障礙個案報告。無人體對照資料。 |
| 5 | 拔毛症 (trichotillomania) | 99.51% | L4 | 見下表。 |

**拔毛症屬強迫症譜系。** 在 SRI 難治型強迫症及相關疾患中，以 D2／5-HT2A 阻斷的抗精神病藥加成 SRI 是已知的治療策略。目前沒有 RCT 或已登記試驗。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9108814](https://pubmed.ncbi.nlm.nih.gov/9108814/) | 1997 | 病例系列 | J Clin Psychiatry | 以 risperidone 加成 SRI 用於強迫症及相關疾患 |
| [10357517](https://pubmed.ncbi.nlm.nih.gov/10357517/) | 1999 | 病例系列（3 例） | J Child Adolesc Psychopharmacol | 在 SRI 難治型拔毛症加入低劑量 risperidone（0.5–3 mg/日） |
| [11320684](https://pubmed.ncbi.nlm.nih.gov/11320684/) | 2001 | 個案報告 | Can J Psychiatry | 難治型拔毛症以 risperidone 加成 fluvoxamine |
| [12297616](https://pubmed.ncbi.nlm.nih.gov/12297616/) | 2002 | 個案報告 | Psychosomatics | 難治型拔毛症使用 risperidone |
| [24598474](https://pubmed.ncbi.nlm.nih.gov/24598474/) | 2014 | 個案報告 | J Am Med Dir Assoc | 老年拔毛症以 risperidone 合併 naltrexone 治療 |
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | 回顧 | Int J Dermatol | 拔毛症藥物治療現況與治療指引缺口 |

## 香港上市資訊

共 20 張許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症。

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-64107 | RISPERIDONE ACTAVIS TABLETS 1MG | Teva Pharmaceutical Hong Kong |
| HK-59970 | RISPERIDONE SANDOZ TAB 1MG | Sandoz Hong Kong |
| HK-62997 | JMP-RISPERIDONE TABLET 1MG | Jean-Marie Pharmacal |
| HK-59971 | RISPERIDONE SANDOZ TAB 4MG | Sandoz Hong Kong |
| HK-57140 | RISPERIDONE-TEVA TAB 3MG | Teva Pharmaceutical Hong Kong |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第 1 的預測沒有任何試驗或文獻，機轉上也無關聯，應視為模型假象，不建議投入資源。
- 若要探索，拔毛症是 5 個預測中證據最多的方向（L4，建議為「研究問題」）。但證據僅限個案報告與小型病例系列，且 risperidone 的代謝與錐體外症候群風險需與有限證據一併權衡。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症（目前缺漏，阻擋安全性初篩）。
- 補齊作用機轉資料（可由 DrugBank 取得）。
- 若轉向拔毛症：系統性搜尋 RCT 與臨床試驗登記，並評估與現行標準治療（如 SRI、行為治療）的比較。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

