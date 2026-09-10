---
layout: default
title: Obinutuzumab
parent: 高證據等級 (L1-L2)
nav_order: 535
evidence_level: L1
indication_count: 3
---

# Obinutuzumab
{: .fs-9 }

證據等級: **L1** | 預測適應症: **3** 個
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

# Obinutuzumab：從慢性淋巴性白血病（CLL）到濾泡性淋巴瘤（Follicular Lymphoma）

## 一句話總結

Obinutuzumab 是第二代人源化抗 CD20 單株抗體，依國際核准資訊原用於慢性淋巴性白血病（CLL，併用 Chlorambucil），但目前尚未在香港上市。TxGNN 模型預測它可能對**濾泡性淋巴瘤 (Follicular Lymphoma)** 有效，目前有 **50 個臨床試驗**和 **19 篇文獻**支持這個方向，其中包含 GALLIUM 等大型 Phase 3 隨機對照試驗已直接驗證其第一線治療療效。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性淋巴性白血病（CLL，依國際核准資訊；香港未上市無在地登記紀錄） |
| 預測新適應症 | 濾泡性淋巴瘤 (Follicular Lymphoma) |
| TxGNN 預測分數 | 99.18% |
| 證據等級 | L1 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Obinutuzumab（GA101）是第三代人源化、醣基工程改造之第 II 型抗 CD20 單株抗體，相較第一代 Rituximab，具有更強的抗體依賴性細胞毒殺作用（ADCC）、補體依賴性細胞毒殺（CDC）及直接誘導 B 細胞凋亡的能力。此為 `repurposing_rationale` 欄位提供的機轉描述，正式的 DrugBank MOA 欄位目前為資料缺口（DG002）。

濾泡性淋巴瘤（FL）與 CLL/SLL 同屬 CD20 陽性 B 細胞惡性腫瘤，藥理標的完全一致，因此機轉上高度支持跨適應症延伸。更重要的是，此預測已獲得實證支持而非僅停留在理論層面：GALLIUM（NCT01332968）等大型 Phase 3 RCT 已證實 Obinutuzumab 於初治晚期 FL 的療效優於 Rituximab 為主的化療方案，屬機轉與臨床雙重驗證的適應症。

另外，TxGNN 同時以相同分數（0.992）預測了兩個 CLL/SLL 分子亞型（依 IGHV somatic hypermutation 狀態分層），機轉關聯性同樣成立，但因搜尋詞為高度細分的亞型命名，目前查無對應臨床試驗或文獻佐證，證據等級僅為 L5，本報告不予展開，建議 Hold 並待重新以較寬泛的疾病詞彙查證。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03332017](https://clinicaltrials.gov/study/NCT03332017) | Phase 2 | 已完成 | 217 | ROSEWOOD：Zanubrutinib+Obinutuzumab 對比 Obinutuzumab 單用於復發/難治 FL，隨機對照，合併療法顯示優效 |
| [NCT06961500](https://clinicaltrials.gov/study/NCT06961500) | Phase 2 | 未開始招募 | 133 | 隨機比較 Obinutuzumab+CHOP 與 Obinutuzumab+Bendamustine 用於初治 FL Grade 3A |
| [NCT05899621](https://clinicaltrials.gov/study/NCT05899621) | N/A（真實世界） | 招募中 | 332 | 真實世界研究，觀察 Obinutuzumab 為主治療於初治 FL 之療效與安全性 |
| [NCT02611323](https://clinicaltrials.gov/study/NCT02611323) | Phase 1/2 | 已完成 | 133 | Obinutuzumab 併用 Polatuzumab Vedotin 及 Venetoclax，用於復發/難治 FL 誘導治療 |
| [NCT06549335](https://clinicaltrials.gov/study/NCT06549335) | Phase 2 | 未開始招募 | 66 | Zanubrutinib+Obinutuzumab+Lenalidomide（ZGR）方案用於高風險初治 FL |
| [NCT03980171](https://clinicaltrials.gov/study/NCT03980171) | Phase 1/2 | 進行中（未招募） | 50 | Lenalidomide+Venetoclax+Obinutuzumab 用於初治 FL 誘導與維持治療 |
| [NCT01691898](https://clinicaltrials.gov/study/NCT01691898) | Phase 1/2 | 已完成 | 231 | Polatuzumab Vedotin 併用 Obinutuzumab，用於復發/難治 B 細胞非何杰金氏淋巴瘤（含 FL） |
| [NCT06108232](https://clinicaltrials.gov/study/NCT06108232) | Phase 2 | 招募中 | 36 | Obinutuzumab+CC-99282 用於初治高腫瘤負荷 FL |
| [NCT01680991](https://clinicaltrials.gov/study/NCT01680991) | Phase 1 | 已完成 | 48 | 中國患者 CD20+ 惡性疾病之 Obinutuzumab 藥動學研究 |
| [NCT02393157](https://clinicaltrials.gov/study/NCT02393157) | Phase 2 | 招募中 | 25 | Obinutuzumab+ICE 化療用於兒童/青少年復發難治 CD20+ B 細胞非何杰金氏淋巴瘤 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [28976863](https://pubmed.ncbi.nlm.nih.gov/28976863/) | 2017 | RCT | NEJM | GALLIUM 試驗：Obinutuzumab 為主化療對比 Rituximab 為主化療，用於初治晚期 FL |
| [29856692](https://pubmed.ncbi.nlm.nih.gov/29856692/) | 2018 | RCT | J Clin Oncol | GALLIUM 化療骨幹亞組分析：不同化療組合對 Obinutuzumab 療效與安全性的影響 |
| [37404773](https://pubmed.ncbi.nlm.nih.gov/37404773/) | 2023 | RCT | HemaSphere | GALLIUM 最終分析：Obinutuzumab 對比 Rituximab 免疫化療於初治 FL/MZL 的長期結果 |
| [37506346](https://pubmed.ncbi.nlm.nih.gov/37506346/) | 2023 | RCT | J Clin Oncol | ROSEWOOD：Zanubrutinib+Obinutuzumab 對比 Obinutuzumab 單用於復發/難治 FL |
| [31296423](https://pubmed.ncbi.nlm.nih.gov/31296423/) | 2019 | RCT | Lancet Haematol | GALEN：Obinutuzumab 併用 Lenalidomide 用於復發/難治 FL 之單臂 Phase 2 研究 |
| [38660754](https://pubmed.ncbi.nlm.nih.gov/38660754/) | 2024 | Review | Turk J Haematol | 濾泡性淋巴瘤治療進展之全面性回顧 |
| [39830356](https://pubmed.ncbi.nlm.nih.gov/39830356/) | 2024 | Review | Front Pharmacol | Obinutuzumab 於 FL 的療效、安全性與成本效益快速回顧 |
| [35180337](https://pubmed.ncbi.nlm.nih.gov/35180337/) | 2022 | Review | Oncology | 濾泡性淋巴瘤現行與新興治療方式回顧 |
| [31360086](https://pubmed.ncbi.nlm.nih.gov/31360086/) | 2017 | Review | Blood Lymphat Cancer | Obinutuzumab 單用及合併治療於 FL 的影響回顧 |
| [28276536](https://pubmed.ncbi.nlm.nih.gov/28276536/) | 2016 | Review | Drugs of Today | Obinutuzumab 於濾泡性淋巴瘤之藥物回顧 |

---

## 香港上市資訊

目前查無 Obinutuzumab 在香港取得的藥品許可證，市場狀態為「未上市」（許可證數：0）。

---

## 細胞毒性

**判定依據**：CLL/FL 均屬惡性腫瘤（血液腫瘤），Obinutuzumab 屬抗腫瘤用單株抗體，故列出本章節。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（第二代人源化抗 CD20 單株抗體，屬免疫標靶治療，非傳統細胞毒性化療藥物） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- GALLIUM（Phase 3 RCT，NEJM 2017 / HemaSphere 2023 最終分析）已證實 Obinutuzumab 於初治 FL 的優效性，加上 ROSEWOOD、GALEN 等多項 Phase 2/3 RCT 持續累積證據，評為 L1，機轉與臨床證據雙重支持。
- 但香港尚未上市，且仿單警語、禁忌症與正式 MOA 資料均為缺口，須先補齊安全性基礎資料才能進入下一階段初評。

**若要推進需要：**
- 補齊香港仿單警語/禁忌症資料（DG001，Blocking，來源：需下載仿單並解析）
- 補齊正式 MOA 機轉資料（DG002，High，來源：DrugBank API）
- 若考慮引進香港市場，需辦理藥品查驗登記程序
- 對於 TxGNN 同時預測的 CLL/SLL 分子亞型（IGHV 分層），因無對應試驗/文獻，建議以較寬泛疾病詞彙重新查證後再評估，目前維持 Hold
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

