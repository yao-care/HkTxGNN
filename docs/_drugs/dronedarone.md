---
layout: default
title: Dronedarone
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dronedarone：預測新適應症為中風 (stroke disorder)（證據等級 L5）。原適應症：心房顫動 (atrial fibrillation)"
monitor_inn: "DRONEDARONE"
predicted_indications: ["stroke disorder", "obsolete susceptibility to ischemic stroke", "ABri amyloidosis", "cerebrovascular disorder", "brain stem infarction", "sick sinus syndrome 2, autosomal dominant", "duodenal obstruction", "cerebral artery occlusion", "sarcoglycanopathy", "Wildervanck syndrome"]
---

# Dronedarone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Dronedarone：從心房顫動到中風相關疾患
{: .text-alpha }

## 一句話總結

Dronedarone 是一種抗心律不整藥物，原本用於治療心房顫動 (atrial fibrillation)。
TxGNN 模型預測它可能對**中風 (stroke disorder)** 有效，
目前**無臨床試驗登記**，但有 **20 篇文獻**間接討論這個方向，且多數來自心房顫動族群的回溯或事後分析，並非直接的中風預防試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心房顫動 (atrial fibrillation) |
| 預測新適應症 | 中風 (stroke disorder) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L4（相關的腦血管疾患項目為 L3，皆為間接證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold（列為研究問題，暫不推進） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據文獻摘要，dronedarone 是與 amiodarone 結構相似、但不含碘的苯并呋喃衍生物，具多通道阻斷特性（抑制鈉、鉀、鈣電流），屬於抗心律不整藥物。

心房顫動是心源性栓塞中風的主要原因。若 dronedarone 能維持竇性心律、降低心房顫動負擔，理論上可能間接降低中風風險。ATHENA 試驗的事後分析也提示中風風險下降。另有研究提出 dronedarone 可能具有獨立於抗心律不整作用之外的抗凝血與抗血小板效果，以及對心臟與腦部缺血／再灌流損傷的保護作用，但後者仍屬實驗室或前臨床層級。

不過，這些證據都來自心房顫動患者，而非原發性腦血管疾病族群，也沒有直接的中風預防試驗。PALLAS 試驗（永久性心房顫動）顯示 dronedarone 在高風險族群中有安全疑慮。因此，目前只能說「機轉上可能相關」，不能視為已證實的新適應症。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下依證據強度挑選最相關的文獻（針對「中風」與「腦血管疾患」兩項預測）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22082198](https://pubmed.ncbi.nlm.nih.gov/22082198/) | 2011 | RCT | N Engl J Med | 高風險永久性心房顫動患者使用 dronedarone，重大血管事件結果不佳，構成安全疑慮 |
| [22149318](https://pubmed.ncbi.nlm.nih.gov/22149318/) | 2011 | RCT 事後分析／統合分析 | Am J Cardiovasc Drugs | 針對陣發性或持續性心房顫動，整合隨機試驗評估 dronedarone 與中風發生率的關係 |
| [25820938](https://pubmed.ncbi.nlm.nih.gov/25820938/) | 2015 | 系統性回顧／統合分析 | Cochrane Database Syst Rev | 評估抗心律不整藥物於心臟電擊後維持竇性心律的效果 |
| [40387892](https://pubmed.ncbi.nlm.nih.gov/40387892/) | 2025 | RCT 事後分析 | Clin Res Cardiol | 在 EAST-AFNET 4 試驗中評估 amiodarone 與 dronedarone 早期節律控制的長期安全性與療效 |
| [37485722](https://pubmed.ncbi.nlm.nih.gov/37485722/) | 2023 | 世代研究 | Circ Arrhythm Electrophysiol | 比較 dronedarone 與 sotalol 在未使用過抗心律不整藥物的退伍軍人心房顫動患者中的效果與安全性 |
| [41152878](https://pubmed.ncbi.nlm.nih.gov/41152878/) | 2025 | 世代研究 | BMC Med | 探討 DOAC 與具交互作用的抗心律不整藥物併用，對中風與出血風險的影響 |
| [22433576](https://pubmed.ncbi.nlm.nih.gov/22433576/) | 2012 | 指引 | Can J Cardiol | 加拿大心血管學會心房顫動指引更新，涵蓋中風預防與節律／心率控制 |
| [20396635](https://pubmed.ncbi.nlm.nih.gov/20396635/) | 2010 | Review | Clin Interv Aging | 回顧 dronedarone 於心房顫動／心房撲動對降低中風的影響 |
| [20730068](https://pubmed.ncbi.nlm.nih.gov/20730068/) | 2010 | Review | Vasc Health Risk Manag | ATHENA 試驗降低全因死亡與心血管住院，事後分析提示中風風險下降 |
| [22366819](https://pubmed.ncbi.nlm.nih.gov/22366819/) | 2012 | 前臨床／回顧 | Cardiovasc Drugs Ther | 回顧 dronedarone 對心臟與腦部缺血／再灌流損傷的多效性保護作用 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59499 | MULTAQ TAB 400MG | 未標示 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜的藥物－疾病禁忌關聯，並非仿單原文）：長 QT 症候群（含家族性）、尖端扭轉型心室頻脈 (torsades de pointes)、肝衰竭、缺鉀症、房室傳導阻滯、病竇症候群（含家族性）。
- **與本次預測相關的安全疑慮**：文獻指出 dronedarone 不適用於永久性心房顫動及失代償性心臟衰竭（PALLAS 試驗）。
- **藥物交互作用**：資料庫共收錄 100 筆交互作用，以下為部分列舉。
  - 嚴重 (Major)：Clarithromycin、Hydrocortisone、Amphotericin B（含各種劑型）、Loperamide、Dolasetron、Picosulfuric acid、Polyethylene glycol (3350 with electrolytes)
  - 中度 (Moderate)：Famotidine、Cimetidine、Aprepitant、Dexamethasone、Budesonide、Saxagliptin、Bisacodyl 等
- 此外，文獻提示與 DOAC 併用可能因藥動學交互作用升高 DOAC 濃度，需留意出血與中風風險。

其餘仿單警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數很高，但沒有任何臨床試驗，文獻也僅間接顯示心房顫動患者中風風險可能下降，且多為事後分析，未見直接的中風預防證據。
- dronedarone 在永久性心房顫動與失代償性心衰竭族群有明確安全疑慮，與中風高風險族群高度重疊，現階段不宜推進為新適應症。

**若要推進需要：**
- 取得 dronedarone 的作用機轉資料，釐清其降低中風風險是來自節律控制，還是獨立的抗凝血／抗血小板效果。
- 取得香港仿單的警語、禁忌與核准適應症全文。
- 設計以中風為主要終點的前瞻性研究，而非僅依賴 ATHENA 事後分析。
- 與 DOAC 等標準抗凝治療比較，並評估併用的交互作用與出血風險。
- 明確定義適用族群，排除永久性心房顫動與失代償性心衰竭患者。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

