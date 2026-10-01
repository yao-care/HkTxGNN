---
layout: default
title: Benzbromarone
parent: 僅模型預測 (L5)
nav_order: 102
evidence_level: L5
indication_count: 1
---

# Benzbromarone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Benzbromarone：從高尿酸血症／痛風到腎性低尿酸血症（不建議推進）

## 一句話總結

Benzbromarone 是促尿酸排泄藥，臨床上用於降低血中尿酸（許可證資料未載明適應症，此為藥理常識）。
TxGNN 模型預測它可能對**腎性低尿酸血症 (Renal Hypouricemia)** 有效，但目前**沒有臨床試驗**，文獻中也沒有支持治療效果的證據。文獻只把它當作診斷用的探針藥物。從機轉看，這個預測方向很可能是相反的。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明（藥理上用於痛風／高尿酸血症） |
| 預測新適應症 | 腎性低尿酸血症 (Renal Hypouricemia) |
| TxGNN 預測分數 | 99.07% |
| 證據等級 | L5（僅有模型預測） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料，以下分析根據一般藥理知識，而非 Evidence Pack 的資料。Benzbromarone 抑制腎小管的尿酸轉運蛋白 URAT1 (SLC22A12)，阻斷尿酸再吸收，因此血中尿酸會下降。

腎性低尿酸血症主要由 URAT1（或 GLUT9）的功能喪失變異引起，患者本來就因尿酸再吸收缺陷而大量排出尿酸。再給予 URAT1 抑制劑，等於重現甚至加重疾病表型，可能增加運動誘發急性腎損傷、腎結石和血尿的風險，這些都是文獻中描述的已知併發症。

TxGNN 的高分（99.07%）較可能反映知識圖譜中 benzbromarone、URAT1 與尿酸代謝之間的關聯，而不是治療關係。因此這個預測在機轉上互相矛盾，不應視為有效的老藥新用線索。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下文獻中，benzbromarone 多半作為「診斷腎小管尿酸轉運缺陷的測試藥物」，並非治療用途。沒有 RCT。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | 為風濕科醫師整理低尿酸血症的病因與臨床處置 |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Cohort | JASN | 分析 32 位日本腎性低尿酸血症患者，探討 SLC22A12 (URAT1) 基因與尿酸排泄的關係 |
| [8893184](https://pubmed.ncbi.nlm.nih.gov/8893184/) | 1996 | Case report | Nephron | 以 pyrazinamide 與 benzbromarone 分析 Fanconi 症候群合併低尿酸血症的尿酸轉運 |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | Case report | Acta Paediatrica | 患者反覆發生運動後急性腎衰竭；benzbromarone/pyrazinamide 測試顯示近端小管分泌前再吸收缺陷 |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | Case report | Nephron | 腎性低尿酸血症患者服用 benzbromarone 後尿酸清除率進一步升高 |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Case report | Nephron | 低尿酸血症合併尿路結石；probenecid 與 benzbromarone 都使尿酸清除率明顯上升，以鹼化尿液治療結石 |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | Case series | J Pediatrics | 4 位遺傳性腎性低尿酸血症兒童，pyrazinamide 與 benzbromarone 對多數患者的清除率比值無影響 |
| [1501741](https://pubmed.ncbi.nlm.nih.gov/1501741/) | 1992 | Case report | Nephron | 2 位受試者中，pyrazinamide 未能抑制 benzbromarone 的促尿酸排泄作用 |
| [11676906](https://pubmed.ncbi.nlm.nih.gov/11676906/) | 2001 | Case report | Anales Espanoles de Pediatria | 12 個月男嬰因腎性低尿酸血症出現膀胱尿酸結石，對 benzbromarone 有反應，符合分泌前缺陷 |
| [9144014](https://pubmed.ncbi.nlm.nih.gov/9144014/) | 1997 | Case report | Internal Medicine | 2 例腎性低尿酸血症合併腎結石，以 benzbromarone 與 pyrazinamide 抑制試驗分型 |

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-29832 | NARCARICIN MITE TAB 50MG | WAH HING TRADING CO |
| HK-37906 | NARCARICIN CAP 50MG | WILCOME PHARMACEUTICAL CO LTD |
| HK-58488 | EURICON TAB 50MG | SYNMOSA BIOPHARMA (HONG KONG) COMPANY LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，文獻多為病例報告，且僅將 benzbromarone 用作診斷探針，並非治療證據。
- 機轉上，促尿酸排泄藥可能加重腎性低尿酸血症，並增加急性腎損傷與結石風險。高分預測應視為圖譜關聯的假象。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌資料。
- 補齊 DrugBank 的作用機轉資料，確認 URAT1 抑制與疾病機轉的關係。
- 除非有新的機轉或臨床證據推翻上述判斷，否則不建議投入資源。

*本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

