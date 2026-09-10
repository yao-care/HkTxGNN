---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 655
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

# Risperidone：多重適應症再利用評估（5 項候選）

> 本評估的 Evidence Pack 為多候選型（`TW-DB00734-multi`），TxGNN 針對 Risperidone 一次列出 5 個候選新適應症，證據品質落差很大，故以下不採用單一適應症的標準版型，改為逐一呈現。

---

## 一句話總結

Risperidone 是廣為人知的非典型抗精神病藥物（作用於 D2/5-HT2A 受體），但本評估資料包中缺乏正式的原適應症與 MOA 紀錄，香港亦**未上市**。TxGNN 針對本藥列出 **5 個候選新適應症**，其中僅 **Phelan-McDermid 症候群**與**拔毛症 (Trichotillomania)** 有實際病例報告／系列文獻支持（各 3 篇、10 篇），其餘 3 項（含分數最高的「家族性水平凝視麻痺併脊椎側彎」）**完全無任何試驗或文獻佐證**，研判為知識圖譜雜訊。

---

## 快速總覽

| 排名 | 預測新適應症 | TxGNN 分數 | 證據等級 | 決策階段 | 建議 |
|---|---|---|---|---|---|
| 1 | Gaze palsy, familial horizontal, with progressive scoliosis | 99.76% | 無證據（pending） | pending | Hold |
| 2 | Asperger syndrome, susceptibility to | 99.74% | L5 | S0 | Hold |
| 3 | Amelocerebrohypohidrotic syndrome | 99.69% | L5 | S0 | Hold |
| 4 | Phelan-McDermid syndrome | 99.59% | L4 | S1 | Research Question |
| 5 | Trichotillomania | 99.51% | L4 | S1 | Research Question |

| 項目 | 內容 |
|------|------|
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 作用機轉 (MOA) | 資料缺口（DrugBank 未提供，DG002） |
| 仿單警語/禁忌 | 資料缺口，屬 **Blocking** 等級（DG001），阻擋 S1 安全性初評 |
| 整體建議決策 | **Hold**（個別候選見上表） |

---

## 為什麼這些預測合理／不合理？

目前缺乏 Risperidone 正式的作用機轉資料（DrugBank 未回傳，列為 High 等級資料缺口）。根據各候選項的 rationale 欄位所引用的一般藥理學知識，Risperidone 為 D2/5-HT2A 雙重拮抗劑，臨床上常用於調節邊緣系統情緒與衝動行為迴路——這是以下兩個「有文獻支持」候選的機轉基礎：

- **Phelan-McDermid syndrome**（22q13 缺失／SHANK3 突變）常合併自閉症類群行為、易怒與雙相情緒障礙樣症狀，Risperidone 用於控制此類行為症狀與其他自閉症類群疾病的既有臨床實務一致，但證據僅止於病例報告與斑馬魚模式動物研究，無對照試驗。
- **拔毛症 (Trichotillomania)** 屬強迫症類群（OCD-spectrum），病理生理涉及血清素-多巴胺失調的衝動控制迴路。Risperidone 的 5-HT2A 拮抗作用可增強 SSRI/SRI 效果，臨床上作為 SRI 抗藥性個案的增強治療，此用法在 1997–2025 年間累積約 10 篇文獻，但多為個案報告與小型病例系列。

另外 3 個候選（家族性水平凝視麻痺併脊椎側彎、Asperger 症候群易感性、Amelocerebrohypohidrotic syndrome）**完全沒有臨床試驗或文獻佐證**，且後兩者的 rationale 欄位已明確指出：
- Asperger 易感性的連結僅是套用「ASD 相關易怒行為」的一般機轉推論，並非針對「易感性」本身，不可據以升級證據等級；
- Amelocerebrohypohidrotic syndrome（罕見外胚層發育異常症候群）與 D2/5-HT2A 路徑無已知病理生理連結，判定為知識圖譜雜訊。
- 排名第 1 的候選（家族性水平凝視麻痺併脊椎側彎）連 rationale 都未填寫（pending），資料本身不完整，無法評估合理性。

---

## 臨床試驗證據

目前無相關臨床試驗登記（5 個候選項的 `clinical_trials` 與 `ictrp_trials` 均為空）。

---

## 文獻證據

### Phelan-McDermid syndrome（3 篇）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35328058](https://pubmed.ncbi.nlm.nih.gov/35328058/) | 2022 | Review | Genes | PMS 為 SHANK3 相關罕見神經發育障礙的跨領域臨床與遺傳學回顧 |
| [37868296](https://pubmed.ncbi.nlm.nih.gov/37868296/) | 2023 | Preclinical (斑馬魚模式) | F1000Research | PMS 常用藥物對 shank3 斑馬魚模式感覺行為的影響研究 |
| [35603006](https://pubmed.ncbi.nlm.nih.gov/35603006/) | 2022 | Case report | Int J Dev Disabilities | PMS 合併自閉症/智能障礙/雙相情緒障礙個案之藥物治療組織經驗 |

### 拔毛症 Trichotillomania（10 篇）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10357517](https://pubmed.ncbi.nlm.nih.gov/10357517/) | 1999 | Case series（3 例） | J Child Adolesc Psychopharmacol | SRI 抗藥性拔毛症患者加用 Risperidone 0.5–3 mg/day，3 例皆明顯改善 |
| [9108814](https://pubmed.ncbi.nlm.nih.gov/9108814/) | 1997 | Case series | J Clin Psychiatry | Risperidone 增強 SSRI/SRI 治療強迫症類群疾患的多巴胺機轉論述 |
| [12297616](https://pubmed.ncbi.nlm.nih.gov/12297616/) | 2002 | Case report | Psychosomatics | 頑固型拔毛症以 Risperidone 治療的個案報告 |
| [11320684](https://pubmed.ncbi.nlm.nih.gov/11320684/) | 2001 | Case report | Can J Psychiatry | Risperidone 增強 Fluvoxamine 治療頑固型拔毛症個案 |
| [24598474](https://pubmed.ncbi.nlm.nih.gov/24598474/) | 2014 | Case report（老年） | J Am Med Dir Assoc | 老年拔毛症以 Risperidone + Naltrexone 成功治療 |
| [15034500](https://pubmed.ncbi.nlm.nih.gov/15034500/) | 2002 | Case report | CNS Spectrums | 思覺失調症患者合併拔毛症，Risperidone + Citalopram 部分緩解 |
| [34563228](https://pubmed.ncbi.nlm.nih.gov/34563228/) | 2021 | Case report | Ann Gen Psychiatry | 拔毛症合併暴食症，併用 N-acetylcysteine 協同治療個案 |
| [38797877](https://pubmed.ncbi.nlm.nih.gov/38797877/) | 2025 | Review/Perspective | Int J Dermatol | 拔毛症藥物治療缺乏統一指引，呼籲加強教育與更嚴謹證據 |
| [17484394](https://pubmed.ncbi.nlm.nih.gov/17484394/) | 2006 | Review | J Pract Nursing | 拔毛症治療總覽 |
| [23466108](https://pubmed.ncbi.nlm.nih.gov/23466108/) | 2013 | Review | Asian J Psychiatry | 妄想性寄生蟲病（相關衝動控制疾患）臨床概況 |

---

## 安全性考量

安全性資訊請參考原廠仿單。（本評估之仿單警語、禁忌症、藥物交互作用查詢均無資料，且警語缺失已列為 **Blocking** 等級資料缺口 DG001，直接阻擋任一候選進入 S1 安全性初評。）

---

## 結論與下一步

**整體決策：Hold**

**理由：**
- 香港未上市、無許可證，且仿單警語與禁忌症資料完全缺失（Blocking），任何候選都無法完成正式的安全性初評。
- 5 個候選中僅 2 個（Phelan-McDermid syndrome、拔毛症）有實際文獻支持，證據等級皆為 L4（病例報告／系列），列為 **Research Question**，值得列入下一步文獻回顧範圍；其餘 3 個候選缺乏任何佐證，建議直接 Hold 或剔除。

**若要推進需要：**
- 取得 TFDA/香港仿單 PDF 並解析警語與禁忌症（DG001，優先處理）
- 透過 DrugBank API 查詢正式 MOA 資料（DG002）
- 針對 Asperger 症候群連結，另行查證 RUPP Autism Network 等已知隨機對照試驗文獻，避免僅憑機轉推論分級
- 若推進 Phelan-McDermid syndrome 或拔毛症兩項候選，建議規劃前瞻性病例系列或小型對照試驗以補足證據等級
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

