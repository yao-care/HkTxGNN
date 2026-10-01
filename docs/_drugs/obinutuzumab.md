---
layout: default
title: Obinutuzumab
parent: 僅模型預測 (L5)
nav_order: 622
evidence_level: L5
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Obinutuzumab：從（原適應症資料缺漏）到 CLL/SLL 亞型與濾泡性淋巴瘤

## 一句話總結

Obinutuzumab 是一種經糖基化改造的第二型抗 CD20 單株抗體，輸入資料中未載明原適應症。
TxGNN 預測分數最高的是兩個**慢性淋巴球性白血病/小淋巴球性淋巴瘤 (CLL/SLL) 亞型**，目前沒有任何試驗或文獻支持。
預測排名第 3 的**濾泡性淋巴瘤 (Follicular Lymphoma)** 則有 **44 個臨床試驗**和 **19 篇文獻**，其中包含 2 個已完成的 Phase 3 試驗。

## 快速總覽

| 項目 | 排名 1、2：CLL/SLL 亞型 | 排名 3：濾泡性淋巴瘤 |
|------|------|------|
| 預測新適應症 | CLL/SLL（免疫球蛋白重鏈可變區體細胞高突變型）、生發中心前 CLL/SLL | 濾泡性淋巴瘤 (Follicular Lymphoma) |
| TxGNN 預測分數 | 99.21%（兩者相同） | 99.18% |
| 證據等級 | L5 | L1 |
| 建議決策 | Hold | Proceed with Guardrails |

| 項目 | 內容 |
|------|------|
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |

> 香港許可證資料中沒有核准適應症文字，因此「原適應症」欄位省略。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位為空）。根據輸入資料，Obinutuzumab 是抗 CD20 單株抗體。CLL/SLL 與濾泡性淋巴瘤都屬於表現 CD20 的 B 細胞惡性腫瘤，因此機轉上可能適用。文獻中描述它可透過直接誘導細胞死亡、增強抗體依賴性細胞毒殺 (ADCC) 與吞噬作用，以及活化補體來作用。

**CLL/SLL 亞型（排名 1、2）：** 這兩個預測只有模型分數，沒有試驗或文獻。兩者分數完全相同，很可能對應同一個本體論節點，建議合併或對應到上層的 CLL/SLL 詞條後再審查。

**濾泡性淋巴瘤（排名 3）：** 文獻標題顯示，Phase 3 GALLIUM 試驗（PMID 29856692、37404773、28976863）比較了 Obinutuzumab 與 Rituximab 為基礎的免疫化療。此外還有 BTK 抑制劑、Lenalidomide、Venetoclax、Polatuzumab 等組合的 Phase 2 研究。這看起來更像是已確立的用途，而非全新的老藥新用，需先對照仿單確認核准狀態，才能算作老藥新用發現。

## 臨床試驗證據（濾泡性淋巴瘤，共 44 筆，列出最相關 10 筆）

CLL/SLL 亞型目前無相關臨床試驗登記。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01332968](https://clinicaltrials.gov/study/NCT01332968) | Phase 3 | 完成 | 1401 | Obinutuzumab 加化療 vs Rituximab 加化療，用於未治療的晚期惰性非何杰金氏淋巴瘤，緩解者接續維持治療 |
| [NCT01059630](https://clinicaltrials.gov/study/NCT01059630) | Phase 3 | 完成 | 413 | Bendamustine 單用 vs 加 Obinutuzumab，用於 Rituximab 難治的惰性非何杰金氏淋巴瘤 |
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | 完成 | 217 | Zanubrutinib 加 Obinutuzumab vs Obinutuzumab 單用，用於復發/難治濾泡性淋巴瘤（對應 ROSEWOOD） |
| [NCT05100862](https://clinicaltrials.gov/study/NCT05100862) | Phase 3 | 招募中 | 780 | Zanubrutinib 加抗 CD20 抗體 vs Lenalidomide 加 Rituximab，用於復發/難治濾泡性或邊緣區淋巴瘤 |
| [NCT05929222](https://clinicaltrials.gov/study/NCT05929222) | Phase 3 | 招募中 | 190 | 早期濾泡性淋巴瘤，局部放療 vs 放療加 Obinutuzumab（GAZEBO） |
| [NCT05045664](https://clinicaltrials.gov/study/NCT05045664) | Phase 3 | 招募中 | 100 | 早期濾泡性淋巴瘤，放療加抗 CD20 抗體 |
| [NCT03817853](https://clinicaltrials.gov/study/NCT03817853) | Phase 4 | 完成 | 114 | 未治療的晚期濾泡性淋巴瘤，評估 Obinutuzumab 短時間輸注的安全性 |
| [NCT03269669](https://clinicaltrials.gov/study/NCT03269669) | Phase 2 | 進行中（不招募） | 73 | 早期復發/難治濾泡性淋巴瘤，Obinutuzumab 合併不同藥物的隨機試驗 |
| [NCT02611323](https://clinicaltrials.gov/study/NCT02611323) | Phase 1/2 | 完成 | 133 | Obinutuzumab、Polatuzumab vedotin 與 Venetoclax 組合，用於復發/難治濾泡性淋巴瘤 |
| [NCT05899621](https://clinicaltrials.gov/study/NCT05899621) | N/A | 招募中 | 332 | 真實世界研究，觀察 Obinutuzumab 為基礎的療法用於未治療濾泡性淋巴瘤 |

## 文獻證據（濾泡性淋巴瘤，共 19 篇，列出最相關 10 篇）

CLL/SLL 亞型目前無相關文獻。摘要多被截斷，以下僅摘述研究設計與題旨。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | J Clin Oncol | GALLIUM：Obinutuzumab 相較 Rituximab 顯著延長無惡化存活期，本篇分析化療組合的影響 |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT | HemaSphere | GALLIUM 最終分析，比較兩種免疫化療用於未治療的惰性淋巴瘤 |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | J Clin Oncol | ROSEWOOD：Zanubrutinib 加 Obinutuzumab vs Obinutuzumab 單用，用於復發/難治濾泡性淋巴瘤 |
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | Review（資料庫分類） | N Engl J Med | 比較 Rituximab 與 Obinutuzumab 化療用於未治療的晚期濾泡性淋巴瘤 |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | Phase 2 單臂試驗 | Lancet Haematol | GALEN：Obinutuzumab 加 Lenalidomide 用於復發/難治濾泡性淋巴瘤 |
| [35359000](https://pubmed.ncbi.nlm.nih.gov/35359000/) | 2022 | Phase 1b/2 | Blood Adv | Atezolizumab 加 Obinutuzumab 與 Bendamustine 用於未治療濾泡性淋巴瘤 |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | 快速回顧 | Front Pharmacol | Obinutuzumab 用於濾泡性淋巴瘤的療效、安全性與成本效益 |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood Lymphat Cancer | Obinutuzumab 單用及合併治療濾泡性淋巴瘤的影響 |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Review | Turk J Haematol | 濾泡性淋巴瘤處置進展的綜述 |
| [28324270](https://pubmed.ncbi.nlm.nih.gov/28324270/) | 2017 | Review | Target Oncol | Obinutuzumab 用於 Rituximab 難治/復發濾泡性淋巴瘤的評述 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-64100 | GAZYVA CONCENTRATE FOR SOLUTION FOR INFUSION 1000MG/40ML | ROCHE HONG KONG LIMITED |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（第二型抗 CD20 單株抗體） |

其餘項目（骨髓抑制風險、致吐性、監測項目、處置防護）：請參考原廠仿單的警語與注意事項。

## 安全性考量

安全性資訊請參考原廠仿單。DDI 查詢結果為無資料。

## 結論與下一步

**決策：**
- **CLL/SLL 亞型（排名 1、2）：Hold**
- **濾泡性淋巴瘤（排名 3）：Proceed with Guardrails**

**理由：**
- CLL/SLL 亞型只有模型預測（L5），沒有試驗或文獻，且兩個詞條可能重複。
- 濾泡性淋巴瘤有 2 個已完成的 Phase 3 試驗（NCT01332968、NCT01059630）和多項 Phase 2 隨機試驗，證據等級為 L1。但這比較像既有適應症的確認，而非新發現。

**若要推進需要：**
- 補齊香港衛生署仿單的警語與禁忌症（目前為阻擋性資料缺口 DG001）
- 補上作用機轉資料（DG002，可查詢 DrugBank）
- 對照仿單，確認濾泡性淋巴瘤是否已是香港核准適應症
- 取得完整文獻紀錄，核實 GALLIUM 與 GADOLIN 的對應
- 合併或對應 CLL/SLL 兩個重複詞條到上層詞條，再評估是否需要補證據
- 建議僅限於已研究的病患族群

> 本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

