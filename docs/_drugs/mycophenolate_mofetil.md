---
layout: default
title: Mycophenolate Mofetil
parent: 高證據等級 (L1-L2)
nav_order: 512
evidence_level: L2
indication_count: 5
---

# Mycophenolate Mofetil
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# MYCOPHENOLATE MOFETIL：從器官移植排斥預防到 HIV 感染

## 一句話總結

Mycophenolate mofetil (MMF) 是一款 IMPDH（次黃嘌呤單核苷酸脫氫酶）抑制劑類免疫抑制劑，證據包內的臨床試驗顯示其原本用於器官移植排斥及 GVHD（移植物抗宿主病）預防。
TxGNN 模型預測它可能對 **HIV 感染 (HIV infectious disease)** 有輔助療效，
目前有 **10 個臨床試驗**和 **20 篇文獻**支持這個方向，但多數試驗年代較早（2000 年代初）、規模小且部分狀態長年未更新。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 查無許可證資料；依證據包內臨床試驗脈絡，MMF 屬免疫抑制劑，原用於器官移植排斥／GVHD 預防 |
| 預測新適應症 | HIV 感染 (HIV infectious disease) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L2 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

DrugBank 的 MOA 欄位目前缺失（[Data Gap]）。但證據包內的機轉論述指出，MMF 是 IMPDH 抑制劑，透過耗竭細胞內鳥嘌呤核苷酸池發揮作用：一方面抑制淋巴球增殖（降低 HIV 可感染的活化 CD4+ T 細胞族群），另一方面能增強部分核苷酸類逆轉錄酶抑制劑（如 abacavir、DAPD/amdoxovir）在細胞內的活化與抗病毒活性。

原適應症（移植排斥／GVHD 預防）與新適應症（HIV 感染）表面上跨科別，但機轉上的橋樑是「抗增殖／免疫調節」——這正是 2000 年代初一系列臨床試驗（MAN2 研究、DAPD 併用試驗等）積極驗證過的方向，屬於輔助治療角色而非直接抗病毒藥物。

需要強調的是，免疫抑制作用在 HIV 感染者身上存在理論風險（伺機性感染、腫瘤風險），這也是多數相關試驗設計為小規模、探索性研究的原因，而非大型確證性臨床試驗。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | 未知(UNKNOWN) | 90 | MAN2 研究：評估 MMF 能否治療 ART-naive 慢性 HIV 患者的免疫系統過度活化，減緩 CD4+ 下降 |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | 未知(UNKNOWN) | 90 | MAN2 子研究：評估 MMF 對 HIV 患者心血管替代指標的影響 |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 1/2 | 已完成 | 56 | 雙盲對照試驗：DAPD 單獨 vs. DAPD+MMF 併用於治療經驗患者，評估安全性與療效 |
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | 已完成 | 27 | HIV 感染腎移植患者之臨床與免疫追蹤研究，評估急性排斥發生率 |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 1/2 | 已撤回 | 0 | 評估 MMF 併用 abacavir 是否能進一步降低病毒量；因撤回無數據 |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | 已完成 | 80 | HLA 不合骨髓移植研究，MMF 作為 GVHD 預防用藥（非 HIV 適應症本身） |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | 已完成 | 10 | HIV 感染者腎臟移植安全性研究，MMF 為標準移植後免疫抑制方案 |
| [NCT06869265](https://clinicaltrials.gov/study/NCT06869265) | Phase 2 | 招募中 | 56 | 高風險 AML 造血幹細胞移植前置方案，MMF 用於 GVHD 預防 |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | 已完成 | 5 | HIV 患者異體造血幹細胞移植研究，MMF 為術後免疫抑制成分 |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | 已終止 | 8 | Anti-EPO 相關純紅血球再生不良治療比較，與 HIV 無直接關聯 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | 隨機前導研究 | J Acquir Immune Defic Syndr | HAART 中斷期間併用 MMF，評估免疫反應與病毒量變化 |
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | 臨床試驗 | AIDS | 治療初治 HIV-1 患者，評估 MMF 對病毒 RNA 衰減速率與潛伏儲存庫的影響 |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | 臨床研究 | AIDS Res Hum Retroviruses | 初治急慢性 HIV-1 患者併用 MMF 與 HAART，未見免疫學上的不良影響 |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | 臨床研究 | J Acquir Immune Defic Syndr | ART（含 abacavir）加入 MMF 後，細胞內 dGTP 耗竭並伴隨血漿 HIV-1 RNA 下降 |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | 前導研究 | J Acquir Immune Defic Syndr | 多重抗藥性 HIV-1 患者併用 MMF 作為治療組成之一的先導研究 |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | 臨床試驗 | AIDS | DAPD 併用或不併用 MMF 於抗藥性 HIV 感染的安全性與抗病毒活性評估 |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | 藥物動力學研究 | Clin Pharmacokinet | 低劑量 MMF 併用 abacavir/efavirenz/nelfinavir 的 PK/PD 監測 |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | 藥物動力學研究 | Clin Pharmacokinet | MMF 對抗反轉錄病毒藥物 PK 及細胞內核苷三磷酸池的影響 |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | 探討 HIV 疾病中免疫活化與免疫抑制劑（含 MMF）的角色 |
| [41118390](https://pubmed.ncbi.nlm.nih.gov/41118390/) | 2025 | 機轉研究 | J Clin Invest | 抗增殖藥物選擇性清除 HIV 感染 T 細胞株的機轉探討 |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
雖有多筆 Grade A 試驗與 2000 年代一系列機轉一致的臨床研究支持 MMF 對 HIV 感染的輔助潛力，但關鍵試驗（MAN2 系列）狀態長年為 UNKNOWN、樣本數小，且 TFDA/仿單安全性資料（DG001，Blocking）尚未取得，無法完成 S1 安全性初評；免疫抑制劑用於 HIV 感染者亦存在伺機性感染等理論風險。

**若要推進需要：**
- 取得 TFDA/香港藥品仿單之警語與禁忌症資料，完成 S1 安全性初評（現為 Blocking 缺口）
- 補齊 DrugBank 完整 MOA 資料
- 追蹤 MAN2 研究（NCT00120419／NCT00247494）是否有後續結果發表
- 界定適用人群的免疫抑制風險門檻（如 CD4 計數、伺機性感染排除標準）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

