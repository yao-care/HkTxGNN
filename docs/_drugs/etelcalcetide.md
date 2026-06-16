---
layout: default
title: Etelcalcetide
parent: 中證據等級 (L3-L4)
nav_order: 289
evidence_level: L3
indication_count: 4
---

# Etelcalcetide
{: .fs-9 }

證據等級: **L3** | 預測適應症: **4** 個
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

# Etelcalcetide：從次發性副甲狀腺功能亢進症到高磷血症

## 一句話總結

Etelcalcetide 是一種靜脈注射型擬鈣劑（calcimimetic），原本用於血液透析患者的次發性副甲狀腺功能亢進症（SHPT）治療。
TxGNN 模型預測它可能對**高磷血症 (Hyperphosphatemia)** 有效，
目前有 **1 個臨床試驗**和 **3 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 次發性副甲狀腺功能亢進症（血液透析患者） |
| 預測新適應症 | 高磷血症 (Hyperphosphatemia) |
| TxGNN 預測分數 | 99.42% |
| 證據等級 | L3 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Etelcalcetide 是一種鈣敏感受體（CaSR）促效劑（calcimimetic），透過靜脈注射在血液透析結束時給藥，其主要作用為抑制副甲狀腺素（PTH）的分泌。

就機轉關聯性而言，PTH 受到抑制後，骨骼釋出磷酸鹽的速率下降，血清磷濃度可間接降低；同時，PTH 下降亦可能改善 FGF23 的上游調控，進一步輔助磷代謝趨於正常。這條「CaSR 促效 → PTH 抑制 → 骨吸收減少 → 血磷下降」的生物路徑，具有充分的生理合理性。

在臨床情境上，SHPT 與高磷血症在慢性腎臟病（CKD）血液透析族群中高度共病——也就是說，Etelcalcetide 在治療其原始適應症（SHPT）的過程中，即有機會附帶改善高磷血症。這使得本次預測屬於「間接但具生物合理性的機轉延伸」，而非無根據的跨領域推測。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03527511](https://clinicaltrials.gov/study/NCT03527511) | N/A | 已完成 | 21 | 評估 Etelcalcetide 對 CKD 患者破骨細胞的影響；屬 CKD-MBD 骨礦物質代謝研究，涵蓋高磷血症、高副甲亢等共病管理，提供間接機轉支持證據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33305109](https://pubmed.ncbi.nlm.nih.gov/33305109/) | 2020 | Prospective RCT | Kidney International Reports | DUET 試驗：評估 Etelcalcetide 靜脈注射擬鈣劑對血液透析患者 SHPT 的療效，屬多機轉 CKD-MBD 管理策略研究 |
| [29440923](https://pubmed.ncbi.nlm.nih.gov/29440923/) | 2018 | Review | Int J Nephrology and Renovascular Disease | 回顧 Etelcalcetide 在血液透析患者 SHPT 管理中的角色，含磷酸鹽控制與 PTH 抑制的綜合討論 |
| [33211001](https://pubmed.ncbi.nlm.nih.gov/33211001/) | 2021 | Case Report | Clinical Nephrology | 腹膜透析患者 SHPT 伴轉移性肺鈣化個案，闡述磷代謝失調在 ESRD 中的臨床後果 |

---

## 香港上市資訊

Etelcalcetide 目前**未在香港取得上市許可**，無相關藥品登記紀錄。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
Etelcalcetide 的 CaSR 促效機轉與高磷血症的病理生理具備生物合理性連結，且 SHPT 與高磷血症在血液透析族群中高度共病，臨床情境契合。現有的前瞻性 RCT（DUET 試驗）及系統性回顧提供初步間接支持，達到 L3 證據等級，足以進入可行性評估階段，但尚未有以高磷血症為主要療效終點的專屬臨床試驗。

**若要推進需要：**
- 補充詳細作用機轉（MOA）資料（可查詢 DrugBank API）
- 取得台灣 / 香港 TFDA / DOH 仿單，評估警語、禁忌及適應症外使用之安全性邊界
- 規劃以高磷血症為主要終點的獨立臨床試驗或次群體分析（建議 Phase 2）
- 確認香港上市申請路徑（目前未上市，需評估引進可行性）
- 建立高磷血症特定族群的安全性監測計畫（尤其是低血鈣風險）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

