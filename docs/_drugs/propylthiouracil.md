---
layout: default
title: Propylthiouracil
parent: 中證據等級 (L3-L4)
nav_order: 727
evidence_level: L4
indication_count: 3
---

# Propylthiouracil
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Propylthiouracil：從甲狀腺機能亢進到甲狀腺素抵抗症（THRB 突變）

## 一句話總結

Propylthiouracil（PTU）是抗甲狀腺藥物，原本用於治療甲狀腺機能亢進。
TxGNN 模型預測它可能對**甲狀腺素受體 β 突變所致的甲狀腺素抵抗症 (Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta)** 有效。
目前**沒有臨床試驗**，僅有 **6 篇文獻**，且都是疾病本身的研究，沒有 PTU 療效資料。機轉分析也不支持這個預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 甲狀腺機能亢進（Evidence Pack 未明列，依藥理推定） |
| 預測新適應症 | 甲狀腺素抵抗症（THRB 突變）(Resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta) |
| TxGNN 預測分數 | 99.66% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據 Evidence Pack 的分析，PTU 抑制甲狀腺過氧化酶（減少甲狀腺素合成），也抑制周邊組織 T4 轉換為 T3。

甲狀腺素抵抗症（RTH-β）的缺陷在受體端，患者的 T4/T3 偏高，TSH 卻無法被抑制。PTU 降低甲狀腺素產量，預期會讓 TSH 進一步上升，有甲狀腺腫大或增生的風險。因此，雖然 TxGNN 分數高達 0.997，機轉上並不支持。

現有文獻談的是疾病本身（突變、小鼠模型、新生兒影響），沒有任何 PTU 治療此疾病的療效資料。文獻中的 PTU 相關線索（見下方 PMID 10724359）反而是誤診為甲狀腺毒症、用 PTU 後甲狀腺腫變大的案例。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [18561095](https://pubmed.ncbi.nlm.nih.gov/18561095/) | 2009 | 病例／家族研究 | Exp Clin Endocrinol Diabetes | 土耳其一個家族（母子）帶有 THRB P453A 突變，出現甲狀腺素抵抗症表現 |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | 病例報告 | Clin Endocrinol | 同一家族的兩例 THRB M313T 突變：一名嬰兒出現新生兒甲狀腺毒症，母親有不孕問題 |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | 病例報告 | Endocr J | 泰國女性帶有新發 L330S 突變，先前被當作甲狀腺毒症以 PTU 治療 9 個月，甲狀腺腫反而更大 |
| [14684607](https://pubmed.ncbi.nlm.nih.gov/14684607/) | 2004 | 回顧／前臨床 | Endocrinology | 探討 TRβ 突變在心臟造成甲狀腺素抵抗的角色 |
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | 動物研究（小鼠） | Endocrinology | 在 THRB 單一等位基因突變的小鼠中，TSH 與不對稱甲狀腺癌發生有關 |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | 動物研究（小鼠） | Oncogene | 在濾泡性甲狀腺癌小鼠模型中，甲狀腺素活化腫瘤細胞增生 |

---

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-47993 | CP-PTU TAB 50MG | CHRISTO PHARM LTD |
| HK-04990 | PROPYLTHIOURACIL TAB 50MG (SYNCO) | SYNCO (H.K.) LIMITED |
| HK-59451 | PYROID TAB 50MG | NATURAL HEALTH RESOURCES COMPANY LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

補充：Evidence Pack 在其他預測適應症的分析中提到，PTU 有肝毒性黑框警語，兒童尤其需要注意。此項不在本藥物的警語欄位內，需以仿單核實。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 機轉上，降低甲狀腺素產量不針對受體端缺陷，還可能加重 TSH 刺激與甲狀腺腫。
- 證據僅限病例報告與動物研究，沒有臨床試驗，也沒有 PTU 療效資料。
- TxGNN 分數高，但在本案中沒有獲得實質證據支持。

**若要推進需要：**
- 有 PTU 用於 THRB 突變 RTH 的臨床療效證據；目前連初步訊號都沒有。
- 取得香港衛生署仿單的警語與禁忌症資料，並補上 DrugBank 作用機轉。
- 若要沿 PTU 的抗甲狀腺機轉繼續研究，Evidence Pack 中排名第 2 的「新生兒甲狀腺毒症」（證據等級 L3）是較合理的方向，但需先審查肝毒性風險。

*本報告僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

