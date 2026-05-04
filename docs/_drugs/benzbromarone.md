---
layout: default
title: Benzbromarone
parent: 僅模型預測 (L5)
nav_order: 89
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

# Benzbromarone：從高尿酸血症到腎性低尿酸血症

## 一句話總結

Benzbromarone 是一種強效尿酸促排藥，傳統上用於高尿酸血症與痛風的治療，其核心機轉為抑制腎小管 URAT1 轉運蛋白。
TxGNN 模型預測它可能對**腎性低尿酸血症（Hypouricemia, Renal）**有效，評分高達 **99.07%**，
然而深入的機轉分析顯示此為**典型假陽性**：藥物與疾病雖共享 URAT1 分子節點，但作用方向完全相反，臨床上屬禁忌，**目前有 20 篇文獻**以 Benzbromarone 作為診斷探針使用（而非治療藥物）。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高尿酸血症 / 痛風（國際已知藥理用途；香港未上市） |
| 預測新適應症 | 腎性低尿酸血症 (Hypouricemia, Renal) |
| TxGNN 預測分數 | 99.07% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold（機轉禁忌，假陽性預測） |

---

## 為什麼這個預測合理？（以及為何實際上不合理）

**TxGNN 高分的成因——URAT1 節點重疊**

Benzbromarone 是目前已知最強效的 URAT1（SLC22A12）抑制劑之一，透過阻斷腎小管近端對尿酸的重吸收，大幅促進尿酸從尿液排出，最終降低血清尿酸濃度，屬於「尿酸促排藥（Uricosuric Agent）」。TxGNN 識別到此藥與腎性低尿酸血症均高度關聯於 URAT1 分子節點，因而給出 99.07% 的極高預測分數。

**機轉方向性的根本矛盾**

> ⚠️ **此預測為機轉層面禁忌（Mechanistic Contraindication）**

腎性低尿酸血症的根本病因，恰恰是 **URAT1（或 GLUT9/SLC2A9）基因的功能喪失突變（loss-of-function mutation）**，導致腎小管本就無法正常重吸收尿酸——患者血清尿酸已極低（通常 < 2 mg/dL），且尿液中尿酸濃度異常升高。在這種狀態下投予 Benzbromarone（進一步抑制已功能缺損的 URAT1），將產生三重危害：① 進一步壓低血清尿酸；② 使尿液尿酸濃度更高，加重運動誘發急性腎衰竭（Exercise-Induced ARF）的風險；③ 增加尿路結石的發生機率。

**模型假陽性的啟示**

此案例是 TxGNN 知識圖譜演算法「分子標籤重疊假陽性（Molecular Label Overlap False Positive）」的典型範例。演算法正確識別出藥物與疾病共享靶點，但未能捕捉兩者對同一靶點的**作用方向性**（抑制劑 vs. 功能喪失突變）差異。臨床評估中，此類假陽性需透過機轉方向性分析加以篩除。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下 20 篇文獻中均提及 Benzbromarone，但其角色為**藥理診斷探針**（Benzbromarone/Pyrazinamide 測試），用以鑑別腎性低尿酸血症亞型（分泌前重吸收缺損 vs. 分泌後重吸收缺損 vs. 增強型分泌），而**非作為治療藥物**。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Narrative Review | Clin Rheumatol | 低尿酸血症病因分類與臨床處置完整回顧，供風濕科醫師參考 |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Molecular/Clinical Cohort | JASN | 32 名日本腎性低尿酸血症患者 SLC22A12 基因定序，確立 URAT1 突變為主因 |
| [14747372](https://pubmed.ncbi.nlm.nih.gov/14747372/) | 2004 | Basic Science | JASN | 小鼠 URAT1 同源蛋白（RST）的定位與功能研究，闡明 Benzbromarone 為 URAT1 受質/抑制劑 |
| [18670416](https://pubmed.ncbi.nlm.nih.gov/18670416/) | 2008 | Clinical Study | Am J Hypertens | Losartan 透過抑制 URAT1 產生尿酸促排效果的臨床驗證，與 Benzbromarone 機轉相似 |
| [8893184](https://pubmed.ncbi.nlm.nih.gov/8893184/) | 1996 | Mechanistic Study | Nephron | Fanconi 症候群合併腎性低尿酸血症，以 Benzbromarone/Pyrazinamide 探針分析尿酸轉運 |
| [8863890](https://pubmed.ncbi.nlm.nih.gov/8863890/) | 1996 | Case Report | Acta Paediatrica | 反覆運動誘發急性腎衰竭（14–25 歲，4 次發作），Benzbromarone 測試定位分泌前重吸收缺損 |
| [3380222](https://pubmed.ncbi.nlm.nih.gov/3380222/) | 1988 | Case Report / Mechanistic | Nephron | 投予 Benzbromarone 後尿酸清除率**更高**（而非降低），確認重吸收完全缺損亞型 |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Case Report / Mechanistic | Nephron | 增強型尿酸分泌引起低尿酸血症合併尿路結石，Benzbromarone 在 Pyrazinamide 預處理下失效 |
| [9510398](https://pubmed.ncbi.nlm.nih.gov/9510398/) | 1998 | Case Series | Intern Med | 16 名腎性低尿酸血症患者血尿發生率研究，以 Benzbromarone 進行亞型分類 |
| [4009341](https://pubmed.ncbi.nlm.nih.gov/4009341/) | 1985 | Case Series | J Pediatrics | 4 名遺傳性腎性低尿酸血症兒童，Benzbromarone 對清除率無抑制效果，確認完全缺損亞型 |

> 另有 10 篇文獻（PMID: 14655203、10879667、12862209、9144014、7933674、1501741、7853759、8976099、21139282、11676906）均為個案報告或機轉研究，Benzbromarone 同樣以診斷工具身份出現，不列入治療證據。

---

## 結論與下一步

**決策：Hold（機轉禁忌，不建議推進）**

**理由：**
- 此預測為 TxGNN 知識圖譜的機轉方向性假陽性——藥物抑制 URAT1，而疾病的成因正是 URAT1 功能喪失，兩者的病理生理方向完全相反，使用 Benzbromarone 將加重低尿酸血症並增加急性腎衰竭風險，屬臨床禁忌
- 全部 20 篇文獻均以 Benzbromarone 作為腎小管功能診斷探針，無一支持其作為腎性低尿酸血症的治療藥物

**若要推進需要：**
- **本預測建議不推進**；此案例應標記為假陽性典型案例，供 TxGNN 模型優化（加入作用方向性過濾規則）
- 若有意探索腎性低尿酸血症的治療策略，應尋找能**補償或恢復 URAT1 功能**的候選藥物，或針對運動誘發急性腎衰竭的預防措施（如充分水化）
- 建議對此類「藥物與疾病共享抑制靶點，但疾病為該靶點功能喪失」的結構型假陽性，建立系統性篩除規則
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

