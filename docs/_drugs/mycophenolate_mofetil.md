---
layout: default
title: Mycophenolate Mofetil
parent: 高證據等級 (L1-L2)
nav_order: 594
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

# Mycophenolate Mofetil：從器官移植免疫抑制到 HIV 感染

## 一句話總結

Mycophenolate mofetil（MMF）是一種免疫抑制劑，常用於器官移植的抗排斥治療，香港許可證資料未載明核准適應症文字。
TxGNN 模型預測它可能對 **HIV 感染 (HIV infectious disease)** 有效。
目前有 **9 個臨床試驗**和 **20 篇文獻**與此方向相關，但直接測試 MMF 抗 HIV 的證據多為小型先導研究，結果不一致。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症（一般用於器官移植免疫抑制） |
| 預測新適應症 | HIV 感染 (HIV infectious disease) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L2 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

MMF 抑制 IMPDH 酶，使鳥嘌呤核苷酸（guanosine nucleotides）耗竭，進而抑制淋巴球增生。
HIV 需要活化的 CD4+ T 細胞才能複製，MMF 可能縮小這個細胞池。
細胞內 dGTP 下降還可能增強 abacavir 等核苷類似物的抗病毒活性。
DrugBank 的 MOA 欄位目前缺資料，以上機轉來自本次分析的推論。

HIV 疾病進展與慢性免疫過度活化密切相關，因此「抑制免疫活化」被視為輔助治療的假說。
一篇 2006 年的回顧文章（PMID 17017956）也討論了免疫抑制藥物用於 HIV 的概念。

不過臨床結果並不一致。部分先導研究顯示有抗病毒或免疫調節的效果，另一些則未見明確的病毒學優勢。
目前只能視為「可產生假說的輔助角色」，並非已確立的抗病毒適應症。
MMF 在 HIV 陽性患者中用於移植免疫抑制，是另一種使用情境，不等於治療 HIV。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | 未知 | 90 | MAN2 試驗：評估 MMF 能否減緩未接受抗病毒治療的慢性 HIV 患者免疫過度活化與 CD4 下降，無結果 |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | 未知 | 90 | MAN2 的子研究，觀察 MMF 對 HIV 患者心血管替代指標的影響，終點非抗病毒 |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 1/2 | 完成 | 56 | 隨機雙盲：DAPD 對比 DAPD 加 MMF 用於治療經驗豐富的 HIV 患者，MMF 為組合夥伴 |
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | 完成 | 27 | HIV 患者腎移植後 6 個月急性排斥率，與 MMF 的關聯待人工確認 |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 1/2 | 撤回 | 0 | 設計為 MMF 加 abacavir 的安全性與抗病毒活性，未收案，無證據價值 |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | 完成 | 10 | HIV 陽性末期腎病患者接受腎移植，屬移植管理，非 HIV 治療 |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | NA | 完成 | 5 | HIV 患者異體幹細胞移植，MMF 為移植後免疫抑制成分 |
| [NCT02793544](https://clinicaltrials.gov/study/NCT02793544) | Phase 2 | 完成 | 80 | HLA 不合骨髓移植，MMF 用於 GVHD 預防，與 HIV 無關 |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | 終止 | 8 | 抗 EPO 相關純紅血球再生不良的治療，與 HIV 無關 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | 隨機先導研究 | J Acquir Immune Defic Syndr | 17 位慢性 HIV 患者，比較 HAART 中斷期間加用 MMF 的免疫反應與病毒量，摘要未列結果 |
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | 臨床研究 | AIDS | 評估 MMF 對初治患者血漿 HIV-1 RNA 下降速率與潛伏感染細胞庫的影響，摘要僅列研究目的 |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | 臨床研究 | AIDS | 評估 DAPD 加或不加 MMF 對高度抗藥 HIV 的安全性與抗病毒活性 |
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | 臨床研究 | J Acquir Immune Defic Syndr | 5 位治療失敗患者加用 MMF 後，細胞內 dGTP 耗竭且血漿 HIV-1 RNA 下降 |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | 先導臨床研究 | J Acquir Immune Defic Syndr | 7 位多重抗藥 AIDS 患者使用 MMF 組合治療，耐受良好，病毒學結果因摘要截斷無法確認 |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | 臨床研究 | AIDS Res Hum Retroviruses | MMF 加 HAART 在初治急性與慢性感染者中，未見不良的免疫學影響 |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | 藥動/藥效研究 | Clin Pharmacokinet | 低劑量 MMF 與 abacavir、efavirenz、nelfinavir 併用的藥動學與藥效學，建議做藥物監測 |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | 藥動學研究 | Clin Pharmacokinet | 探討 MMF 對抗病毒藥物藥動學及細胞內核苷三磷酸池的影響 |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | 討論免疫過度活化與 HIV 進展，以及免疫抑制藥物作為輔助策略的概念 |
| [19112763](https://pubmed.ncbi.nlm.nih.gov/19112763/) | 2008 | Case report | J Drugs Dermatol | HIV 合併乾癬與乾癬性關節炎的患者，使用 MMF 治療安全有效，針對的是自體免疫疾病 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64778 | MYCOPHENOLATE MOFETIL CAPSULES 250MG | 膠囊（依品名） | 資料未載明 |
| HK-61952 | APO-MYCOPHENOLATE TABLETS 500MG | 錠劑（依品名） | 資料未載明 |
| HK-67222 | MOFECON 250 CAPSULES 250MG | 膠囊（依品名） | 資料未載明 |
| HK-44333 | CELLCEPT TAB 500MG | 錠劑（依品名） | 資料未載明 |
| HK-61953 | APO-MYCOPHENOLATE CAPSULES 250MG | 膠囊（依品名） | 資料未載明 |

## 安全性考量

安全性資訊請參考原廠仿單。本次未取得香港衛生署仿單的警語與禁忌資料，藥物交互作用查詢也無結果。

## 結論與下一步

**決策：Hold**

**理由：**
- 直接測試 MMF 用於 HIV 的研究多為小型或早期先導試驗，結果不一致，兩個 Phase 4 試驗狀態未知且無結果。
- 香港仿單的安全性資料缺漏，屬阻礙性缺口，無法進入安全性篩選。
- 本次 5 個預測中，其餘 4 個（神經發育疾病、骨 Paget 病、貓免疫缺陷症、猴免疫缺陷病毒感染）皆為 L5 且建議 Hold。後兩者的分數與 HIV 節點相同，可能是從 HIV 傳播而來，不視為獨立證據。

**若要推進需要：**
- 取得並解析香港衛生署的仿單，補齊警語與禁忌。
- 補齊 DrugBank 的作用機轉資料。
- 人工確認 NCT01453192 與 MMF 的關聯。
- 追蹤 MAN2 試驗（NCT00120419）是否有已發表的結果。
- 若要進一步評估，需要設計針對 HIV 的對照試驗，並評估感染風險與免疫抑制的取捨。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

