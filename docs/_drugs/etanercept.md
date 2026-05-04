---
layout: default
title: Etanercept
parent: 中證據等級 (L3-L4)
nav_order: 245
evidence_level: L3
indication_count: 6
---

# Etanercept
{: .fs-9 }

證據等級: **L3** | 預測適應症: **6** 個
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

# Etanercept：從類風濕性關節炎到類風濕血管炎

## 一句話總結

Etanercept 是一種 TNF-α 受體融合蛋白，已被廣泛用於類風濕性關節炎（RA）及多種自體免疫疾病的治療。
TxGNN 模型預測它可能對**類風濕血管炎（Rheumatoid Vasculitis）** 有效，目前有 **6 個臨床試驗**和 **20 篇文獻**涉及此研究方向；然而，現有最直接的 Phase I/II 試驗結果呈陰性，並記錄到矛盾性血管炎誘發風險，建議暫緩進一步開發。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 類風濕性關節炎（Rheumatoid Arthritis） |
| 預測新適應症 | 類風濕血管炎（Rheumatoid Vasculitis） |
| TxGNN 預測分數 | 99.71% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Etanercept 是由兩個人類 p75 TNF 受體胞外域與 IgG1 Fc 段組成的二聚體融合蛋白，透過捕捉循環中的 TNF-α 阻斷其與細胞表面受體結合，進而抑制免疫介導的全身性炎症。

> 目前缺乏詳細的作用機轉資料（需補充 DrugBank MOA 查詢）。根據已知資訊，Etanercept 是 TNF 抑制劑（TNFi）家族的代表性藥物，1998 年首先於美國取得 RA 適應症核准，在 RA 中具有豐富的長期使用與安全監測經驗。

類風濕血管炎（RV）是重度 RA 最嚴重的關節外表現之一，由免疫複合物沉積於中小血管壁引發補體激活和中性球浸潤，造成血管壁壞死性炎症。TNF-α 在此病理過程中扮演重要的促炎角色，理論上 Etanercept 的 TNF-α 阻斷機轉應能抑制 RV 的血管壁炎症，此為 TxGNN 模型給出高分預測的機轉依據。

然而，臨床證據呈現重要的矛盾性：最關鍵的直接證據來自 Etanercept 用於 Wegener's 肉芽腫（ANCA 相關血管炎）的 Phase I/II 試驗（NCT00001901，N=60），結果顯示 Etanercept 對此類血管炎**無顯著療效**，且觀察到實體腫瘤風險升高。此外，多項藥物流行病學研究與病例系列記錄到 Etanercept 可「矛盾性」誘發皮膚及 ANCA 相關血管炎，安全性顧慮不容忽視。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00001901](https://clinicaltrials.gov/study/NCT00001901) | Phase I/II | 完成 | 60 | 直接以 Etanercept 治療 Wegener's 肉芽腫（ANCA 相關血管炎）；結果為陰性，療效不顯著，且觀察到實體腫瘤風險上升，為本適應症最重要的**負向直接證據** |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | 觀察性 | 狀態未知 | 750,000 | 大型藥物流行病學研究，追蹤生物製劑使用者罹患免疫介導炎症疾病（含血管炎）風險，間接提供安全性流行病學資料 |
| [NCT01557322](https://clinicaltrials.gov/study/NCT01557322) | 觀察性 | 完成 | 1,754 | RA 真實世界觀察性研究，比較 Etanercept 與非生物製劑 DMARD 的特性，未特定針對 RV 亞群，相關性有限 |
| [NCT02590562](https://clinicaltrials.gov/study/NCT02590562) | 觀察性 | 完成 | 808 | 中國 RA 患者生物製劑治療模式橫斷面研究，未聚焦血管炎亞群，相關性低 |
| [NCT01579006](https://clinicaltrials.gov/study/NCT01579006) | 觀察性 | 完成 | 184 | Tocilizumab 用於 RA 非介入性觀察研究，非 Etanercept 直接相關，提供比較治療背景 |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase II | 尚未招募 | 80 | 評估骨科手術前免疫抑制劑管理策略（含 Etanercept），與 RV 治療無直接關聯 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33058033](https://pubmed.ncbi.nlm.nih.gov/33058033/) | 2021 | Systematic Review | Clinical Rheumatology | 生物製劑用於類風濕血管炎治療的系統性文獻回顧（PRISMA），為本適應症最高等級直接文獻 |
| [28391344](https://pubmed.ncbi.nlm.nih.gov/28391344/) | 2017 | Narrative Review | Nephrol Dial Transplant | 探討 TNFα 阻斷用於 ANCA 相關血管炎的可行性，概述現有證據的支持與侷限 |
| [28123776](https://pubmed.ncbi.nlm.nih.gov/28123776/) | 2017 | Cohort（Pharmacovigilance） | RMD Open | 比較 TNFi（含 Etanercept）與傳統 DMARD 在 RA 患者中誘發狼瘡樣及血管炎樣事件的藥物特異性風險 |
| [15853915](https://pubmed.ncbi.nlm.nih.gov/15853915/) | 2005 | Case Series | Scand J Immunology | 記錄 Etanercept 與 Infliximab 相關皮膚血管炎的免疫機制，分析自體抗體形成路徑 |
| [11792895](https://pubmed.ncbi.nlm.nih.gov/11792895/) | 2002 | Case Series | Rheumatology | Etanercept 與 Infliximab 相關皮膚血管炎早期病例系列報告 |
| [15468348](https://pubmed.ncbi.nlm.nih.gov/15468348/) | 2004 | Narrative Review | J Rheumatology | 綜述 TNF-α 阻斷與血管炎風險的關聯機制，提出臨床監測建議 |
| [15801034](https://pubmed.ncbi.nlm.nih.gov/15801034/) | 2005 | Case Report | J Rheumatology | Etanercept 治療期間出現增生性狼瘡性腎炎及白血球碎裂性血管炎，記錄矛盾性免疫激活現象 |
| [12209493](https://pubmed.ncbi.nlm.nih.gov/12209493/) | 2002 | Case Report | Arthritis & Rheumatism | RA 患者接受 Etanercept 治療後出現加速性類風濕結節及血管炎，為最早期的矛盾性反應報告之一 |
| [15624748](https://pubmed.ncbi.nlm.nih.gov/15624748/) | 2004 | Review | J Drugs Dermatology | 全面綜述 Etanercept 的醫療用途與副作用，皮膚血管炎列為罕見但已知的不良反應 |
| [25544845](https://pubmed.ncbi.nlm.nih.gov/25544845/) | 2014 | Case Report | Case Reports in Medicine | RA 患者接受抗 TNF 治療期間出現大血管血管炎，提醒臨床需鑑別藥物誘發與疾病進展 |

---

## 香港上市資訊

Etanercept 目前**在香港未持有任何核准上市許可證**（許可證數：0），尚未通過香港衛生署藥物核准登記，無法直接作為已上市藥物進行老藥新用評估。如有再利用開發計劃，需同步規劃進口及使用許可事宜。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> **注意**：雖然結構化安全性資料尚待補充（仿單警語與禁忌症均為資料缺口），但本報告的文獻回顧發現重要安全訊號——多項研究記錄 Etanercept 可矛盾性誘發皮膚血管炎及 ANCA 相關血管炎，此為評估 RV 適應症時不可忽略的安全性疑慮，建議優先查閱原廠仿單中的免疫相關不良反應警語。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 預測分數高達 99.71%，機轉上 TNF-α 阻斷理論具合理性，但現有最直接的臨床試驗（Etanercept 用於 Wegener's 肉芽腫，Phase I/II，N=60）結果為陰性，且多項藥物警戒研究和病例報告記錄 Etanercept 本身可矛盾性誘發血管炎，安全性風險超過現有可見效益，不建議以此路徑優先推進。

**若要推進需要：**
- 補充完整作用機轉資料（MOA），以釐清 Etanercept 在類風濕血管炎中的具體生物學機制（與 ANCA 相關血管炎的病理差異）
- 下載並解析原廠仿單 PDF，完成 S1 安全性初評，特別確認免疫相關警語與禁忌症
- 深入分析系統性文獻回顧（PMID 33058033）所納入的生物製劑類型，評估是否有特定生物製劑（如 Rituximab、IL-6 抑制劑）在 RV 中表現優於 TNFi
- 若仍考慮探索 Etanercept 於 RA 相關**皮膚**血管炎（而非 ANCA 型），需設計前瞻性小型先導研究並搭配嚴格的安全監測計劃
- 評估香港藥物進口許可途徑，作為任何研究前置作業
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

