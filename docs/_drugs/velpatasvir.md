---
layout: default
title: Velpatasvir
parent: 中證據等級 (L3-L4)
nav_order: 792
evidence_level: L4
indication_count: 5
---

# Velpatasvir
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Velpatasvir：從 C型肝炎 到 B型肝炎病毒感染

## 一句話總結

Velpatasvir 是 NS5A 抑制劑，原本作為 Sofosbuvir/Velpatasvir（Epclusa）複方成分用於治療慢性C型肝炎（HCV）。TxGNN 模型預測它可能對**B型肝炎病毒感染（Hepatitis B Virus Infection）**有效，目前雖有 **25 個相關臨床試驗**和 **20 篇文獻**被檢索到，但經逐筆核對後，證據內容實際指向的是「HCV治療過程中誘發HBV再活化」的**安全性風險訊號**，而非治療HBV的療效證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 慢性C型肝炎（依臨床試驗與文獻證據推定；Evidence Pack 中 `taiwan_regulatory.licenses` 與 `original_indications` 皆無資料） |
| 預測新適應症 | B型肝炎病毒感染 (Hepatitis B Virus Infection) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L4 |
| 香港上市 | 未上市 |
| 許可證數 | 0 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（`original_moa` 為資料缺口）。但根據 Evidence Pack 中大量臨床試驗與文獻的一致描述，可確認 Velpatasvir 是 HCV NS5A（非結構蛋白5A）抑制劑，透過抑制病毒複製與組裝發揮抗HCV作用，臨床上多以 Sofosbuvir/Velpatasvir 固定劑量複方（Epclusa）用於治療各基因型慢性HCV感染。

HBV 與 HCV 雖同屬「病毒性肝炎」的疾病本體分類，且常在知識圖譜中因「肝炎」「肝硬化」「肝癌」等共同下游併發症節點而被高度關聯，這很可能是 TxGNN 給出 99.87% 高分的原因。然而，HBV（Hepadnaviridae，具逆轉錄步驟的DNA病毒）與HCV（Flaviviridae，RNA病毒）在病毒學上分屬完全不同科別，Velpatasvir 標的的 NS5A 蛋白為HCV特有，HBV病毒並無對應的同源蛋白，機轉上缺乏可轉移性。

更關鍵的是，文獻中確實找到與HBV直接相關的證據（PMID 31542053），但內容描述的是**HBV/HCV共感染或HBV既往感染者，在使用Sofosbuvir/Velpatasvir治療HCV期間發生HBV再活化**的病例報告，以及一項HCV/HBV共感染者需搭配TAF預防性投藥以避免HBV再活化的臨床試驗（NCT04997564）。這些證據顯示的方向與「用Velpatasvir治療HBV」相反——它是風險訊號，而非療效訊號。

## 臨床試驗證據

以下為與此預測適應症相關度較高的試驗（多數實際仍以HCV為研究主體，詳見備註）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04997564](https://clinicaltrials.gov/study/NCT04997564) | Phase 4 | 未知 | 120 | HCV/HBV共感染患者接受SOF/VEL治療HCV，並搭配TAF預防性投藥以避免HBV再活化，非以VEL直接治療HBV |
| [NCT03549312](https://clinicaltrials.gov/study/NCT03549312) | Phase 4 | 未知 | 25 | HIV-HCV共感染者以SOF/VEL治療HCV後轉換抗反轉錄病毒方案，與HBV治療無關（相關性評級C） |
| [NCT02996682](https://clinicaltrials.gov/study/NCT02996682) | Phase 3 | 完成 | 102 | SOF/VEL±RBV治療HCV合併失代償性肝硬化，非HBV適應症（相關性評級C） |
| [NCT05016609](https://clinicaltrials.gov/study/NCT05016609) | Phase 4 | 未知 | 1800 | HCV快速篩檢與同日治療模式研究，非HBV（相關性評級C） |
| [NCT01858766](https://clinicaltrials.gov/study/NCT01858766) | Phase 2 | 完成 | 379 | SOF+VEL治療初治HCV基因型1-6感染者的療效與安全性 |
| [NCT02836925](https://clinicaltrials.gov/study/NCT02836925) | Phase 2 | 完成 | 40 | HCV相關惰性B細胞淋巴瘤患者接受SOF/VEL或SOF/LDV抗病毒治療 |
| [NCT03250910](https://clinicaltrials.gov/study/NCT03250910) | Phase 4 | 完成 | 228 | 學名藥VEL/SOF治療HIV/HCV共感染患者之療效安全性比較 |
| [NCT01826981](https://clinicaltrials.gov/study/NCT01826981) | Phase 2 | 完成 | 359 | SOF併用療法治療慢性HCV感染的療效安全性評估 |
| [NCT02201901](https://clinicaltrials.gov/study/NCT02201901) | Phase 3 | 完成 | 268 | SOF/VEL固定劑量複方治療HCV合併Child-Pugh B級肝硬化患者 |
| [NCT03570112](https://clinicaltrials.gov/study/NCT03570112) | N/A | 完成 | 40 | 妊娠合併慢性HCV感染之自然病史與垂直傳染研究，產後以SOF/VEL治療 |

**注意**：除 NCT04997564 觸及HBV再活化議題外，其餘試驗研究對象均為HCV感染者，並非以Velpatasvir治療HBV的直接證據。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35248213](https://pubmed.ncbi.nlm.nih.gov/35248213/) | 2022 | RCT | Lancet Gastroenterol Hepatol | 盧安達初治病人以SOF/VEL治療HCV基因型4，證實對含抗藥性突變的4r亞型仍具療效 |
| [35579223](https://pubmed.ncbi.nlm.nih.gov/35579223/) | 2022 | Review | Eur J Gen Pract | 慢性HCV診斷與治療之基層照護指引回顧 |
| [34092970](https://pubmed.ncbi.nlm.nih.gov/34092970/) | 2021 | Review | World J Gastroenterol | 兒童病毒性肝炎（HBV/HCV）治療進展回顧，含SOF/VEL兒科使用現況 |
| [31041789](https://pubmed.ncbi.nlm.nih.gov/31041789/) | 2019 | Review | Semin Liver Dis | DAA治療失敗後HCV患者再治療策略回顧 |
| [31114957](https://pubmed.ncbi.nlm.nih.gov/31114957/) | 2019 | Review | Clin Pharmacokinet | HCV抗病毒藥物（含SOF/VEL）藥動藥效學考量之更新回顧 |
| [31542053](https://pubmed.ncbi.nlm.nih.gov/31542053/) | 2019 | Case report | J Med Case Rep | HBsAg免疫逃逸突變株導致HBV再活化病例，發生於患者以SOF/VEL治療HCV期間——**顯示的是風險而非療效** |
| [38910758](https://pubmed.ncbi.nlm.nih.gov/38910758/) | 2024 | Cohort | Cureus | 慢性腎臟病患者以SOF/VEL治療HCV的療效評估橫斷性研究 |
| [33217040](https://pubmed.ncbi.nlm.nih.gov/33217040/) | 2021 | Cohort | J Gastroenterol Hepatol | 真實世界SOF/VEL±RBV治療HCV基因型3感染的療效與安全性 |
| [39735164](https://pubmed.ncbi.nlm.nih.gov/39735164/) | 2024 | Cohort | J Virus Erad | 中國患者以SOF/VEL為主之方案根除HCV的真實世界療效與安全性 |
| [37286314](https://pubmed.ncbi.nlm.nih.gov/37286314/) | 2023 | Cohort | BMJ Open | 台灣南部監獄HCV患者接受抗病毒治療之療效與副作用回溯性分析 |

## 安全性考量

正式安全性欄位（TFDA仿單警語、禁忌症、藥物交互作用）皆為資料缺口，**安全性資訊請參考原廠仿單**。

不過，文獻證據中發現一項重要的間接安全性訊號值得留意：**HBV/HCV共感染或既往HBV感染者，在使用含Velpatasvir之DAA療程治療HCV期間，有HBV再活化的風險**（PMID 31542053；NCT04997564 亦以TAF預防性投藥因應此風險）。此為已知的DAA藥物類別效應，若未來評估Velpatasvir用於HBV相關情境，應將此風險訊號納入考量，而非視為支持療效的證據。

## 結論與下一步

**決策：Hold**

**理由：**
- 關鍵資料缺口為 Blocking 等級（DG001：TFDA仿單警語/禁忌缺失），依規範無法進入 S1 安全性初評；MOA資料缺失（DG002）亦影響機轉關聯性判斷。
- 首選預測適應症（HBV感染，TxGNN分數99.87%）經證據核實後，方向與「再利用治療HBV」相反——找到的是HBV再活化風險證據，而非療效證據。
- 其餘4個候選適應症（E型肝炎、A型肝炎、動物病毒性肝炎、Omsk出血熱）證據等級均為 L5，人工核對後確認絕大部分試驗與文獻實為HCV相關研究，判斷為本體標籤污染（ontology contamination）所致的高分假訊號，並非真實藥理關聯。

**若要推進需要：**
- 補齊TFDA（或香港衛生署）仿單警語與禁忌症資料，以完成S1安全性初評
- 補充完整的作用機轉（MOA）資料，釐清Velpatasvir對HBV病毒複製週期是否存在任何體外/機轉證據
- 若考慮繼續探索HBV方向，須先由肝病專科釐清「HBV再活化風險」與「再利用假說」之間的矛盾，目前證據傾向於禁忌而非適應症
- 確認Velpatasvir在香港（或其他目標市場）之上市與許可證狀態，目前資料顯示未上市、無許可證
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

