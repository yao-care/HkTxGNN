---
layout: default
title: Pyridostigmine
parent: 中證據等級 (L3-L4)
nav_order: 733
evidence_level: L4
indication_count: 7
---

# Pyridostigmine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **7** 個
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

# Pyridostigmine：從重症肌無力到重症肌無力合併胸腺增生

## 一句話總結

Pyridostigmine 是可逆性乙醯膽鹼酯酶抑制劑，臨床上用於重症肌無力的症狀治療。
TxGNN 預測它可能對**重症肌無力合併胸腺增生 (Myasthenia Gravis with Thymus Hyperplasia)** 有效。
目前**沒有臨床試驗**，只有 **3 篇文獻**，且都不是直接評估 pyridostigmine 療效的研究。這個預測屬於既有適應症的亞型，並非真正的跨疾病再利用。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 重症肌無力（香港許可證資料未載明適應症文字，此項依藥理分類與文獻判斷） |
| 預測新適應症 | 重症肌無力合併胸腺增生 (Myasthenia Gravis with Thymus Hyperplasia) |
| TxGNN 預測分數 | 99.76% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Pyridostigmine 是可逆性乙醯膽鹼酯酶抑制劑。它延長乙醯膽鹼在神經肌肉接合處的作用時間，部分補償重症肌無力中功能性乙醯膽鹼受體 (AChR) 的減少。這個機轉不依賴胸腺是否有病變。DrugBank 的 MOA 欄位目前缺漏，上述機轉依據的是證據包中的藥理說明。

胸腺增生是重症肌無力常見的病理表現，尤其見於 AChR 抗體陽性的較年輕患者。因此「重症肌無力合併胸腺增生」其實是既有適應症的亞型，TxGNN 的高分預測在機轉上合理。

需要注意的是，現有文獻談的是胸腺切除預後和 MuSK 陽性病例，並未直接檢驗 pyridostigmine。MuSK 陽性患者對膽鹼酯酶抑制劑常反應不佳或無法耐受，使用時需密切觀察療效。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34225443](https://pubmed.ncbi.nlm.nih.gov/34225443/) | 2021 | Review | Molecular Medicine Reports | 重症肌無力的基因體、表型與表觀遺傳機轉及自體免疫病理回顧，未直接評估 pyridostigmine |
| [25683765](https://pubmed.ncbi.nlm.nih.gov/25683765/) | 2015 | Cohort | Journal of Neurology | 回溯分析 39 位非胸腺瘤晚發型重症肌無力患者胸腺切除後兩年的預後，主題為手術而非藥物 |
| [18053719](https://pubmed.ncbi.nlm.nih.gov/18053719/) | 2008 | Case report | Neuromuscular Disorders | 一位 MuSK 陽性、合併胸腺增生的患者，以垂頭症候群為突出表現 |

## 其他預測適應症（簡要）

| 預測適應症 | 分數 | 證據等級 | 建議 |
|-----------|------|---------|------|
| 新生兒重症肌無力 | 99.76% | L3 | Proceed with Guardrails（文獻以回顧為主，無新生兒劑量試驗，須專科監督） |
| 周邊神經系統自體免疫疾病 | 99.75% | L3 | Proceed with Guardrails（範圍過廣，須依疾病實體個別評估；部分先天性亞型可能因膽鹼酯酶抑制劑惡化） |
| 自體免疫肢帶型肌無力 | 99.74% | L4 | Research Question（僅單一病例報告） |
| 受體活性疾病 | 99.73% | L4 | Research Question（非特定疾病名稱，不宜視為獨立臨床適應症） |
| 脾功能亢進 | 99.30% | L5 | Hold（無機轉連結，僅圖譜預測） |
| 非典型溶血性尿毒症候群（B 因子異常） | 99.22% | L5 | Hold（補體 B 因子異常與膽鹼機轉無關，可能是知識圖譜假象） |

## 香港上市資訊

香港共有 6 張許可證，以下列出 5 張。證據包未提供劑型與核准適應症文字，品名顯示均為錠劑。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-03376 | MESTINON TAB 60MG | A. MENARINI HONG KONG LIMITED |
| HK-03386 | MESTINON TAB 10MG | A. MENARINI HONG KONG LIMITED |
| HK-56949 | JM-PYRIDOSTIGMINE TAB 10MG | VICKMANS LABORATORIES LTD |
| HK-67155 | PYRINON TABLETS 60MG | CHEMILL PHARMA LIMITED |
| HK-56950 | JM-PYRIDOSTIGMINE TAB 60MG | VICKMANS LABORATORIES LTD |

## 安全性考量

目前缺乏香港衛生署仿單的警語與禁忌症資料，藥物交互作用查詢也無結果。安全性資訊請參考原廠仿單。

文獻中有以下與使用相關的提醒：
- MuSK 陽性患者對膽鹼酯酶抑制劑反應常不佳。小鼠研究（PMID 23440963）顯示 pyridostigmine 可能加重 MuSK 抗體誘發的 AChR 流失。
- 新生兒使用須由專科醫師監督，採新生兒專用劑量並監測膽鹼性不良反應。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 作用機轉與重症肌無力的標準症狀治療一致，預測合理。但現有文獻沒有直接測試 pyridostigmine，證據只到 L4。
- 這是既有適應症的亞型，不是新的藥物用途，主要風險在於特定亞型（如 MuSK 陽性）可能反應不佳。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語與禁忌症。這是目前的阻擋性資料缺口，在補齊前無法進入安全性篩選。
- 補充 DrugBank 的作用機轉資料。
- 依抗體亞型（AChR、MuSK）分層評估療效與耐受性。
- 針對新生兒使用，蒐集專科劑量與監測建議。

本報告僅供研究參考，不構成醫療建議。老藥新用候選需經臨床驗證後方可應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

