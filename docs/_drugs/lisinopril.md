---
layout: default
title: Lisinopril
parent: 僅模型預測 (L5)
nav_order: 458
evidence_level: L5
indication_count: 5
---

# Lisinopril
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

# Lisinopril：從高血壓／心肌梗塞後治療 到 心肌梗塞後遺症（Posteroinferior MI）

## 一句話總結

Lisinopril 是一種 ACE 抑制劑（ACEI），透過抑制 RAAS（腎素-血管收縮素-醛固酮系統）廣泛用於高血壓與心臟保護治療，並在心肌梗塞後治療中具教科書等級地位。TxGNN 模型將其重新預測用於**心肌梗塞後遺症（Posteroinferior Myocardial Infarction）**，但本次資料集中未檢索到任何臨床試驗或文獻佐證，證據等級僅為 **L5**，且此預測實質上偏向既有 ACEI 治療地位的重新識別，而非真正的老藥新用發現。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 無香港許可證資料可查證；依機轉描述已知用於高血壓、心臟保護（ACEI 類） |
| 預測新適應症 | 心肌梗塞後遺症 — 下後壁心肌梗塞（Posteroinferior Myocardial Infarction） |
| TxGNN 預測分數 | 99.90%（rank 2758） |
| 證據等級 | L5（僅模型預測，無實際研究） |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

Lisinopril 為 ACEI，透過抑制 RAAS 系統減少心肌梗塞後的心室重塑、降低死亡率，這是已被 SAVE、GISSI-3、AIRE 等大型臨床試驗確立的標準治療機轉。從藥理學角度看，此預測方向本身並不意外。

然而需要指出的是，「posteroinferior myocardial infarction」僅是心肌梗塞的**解剖部位描述**（下後壁），並非一個獨立的臨床適應症分類。這代表 TxGNN 很可能是把 ACEI 於心梗後治療的既有、成熟適應症重新識別出來，而非發現了新穎的老藥新用機會。

本資料集中該適應症沒有任何臨床試驗或文獻紀錄（0/0），無法區分究竟是「資料檢索管線漏抓」還是「此預測本身缺乏可驗證證據」，建議人工核實檢索範圍後再做判斷。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

目前 Lisinopril 未在香港上市，無許可證資料可查詢。

## 安全性考量

安全性資訊（警語、禁忌症、藥物交互作用）目前皆為資料缺口（TFDA/香港仿單警語尚待取得，屬 Blocking 等級缺口），請參考原廠仿單。

> **已知藥理學風險提醒**（非本評估對象、但屬同一藥物的重要背景資訊）：ACEI 類藥物在雙側腎動脈狹窄或孤立腎伴腎動脈狹窄的惡性腎血管性高血壓患者中屬於高風險甚至禁忌用藥，因其抑制 Angiotensin II 對出球小動脈的收縮作用，可能誘發急性腎衰竭。此風險在評估本藥物其他候選適應症（見下方）時需特別留意。

## 其他候選適應症一覽（同一 Evidence Pack 中的排序候選）

本次 Evidence Pack 針對 Lisinopril 共預測 5 個候選適應症，皆為 L5／S0／Hold，列於此供參考：

| 排序 | 預測適應症 | TxGNN 分數 | 臨床試驗/文獻 | 備註 |
|------|-----------|-----------|--------------|------|
| 1 | Posteroinferior myocardial infarction | 99.90% | 0 / 0 | 本報告主軸；屬既有適應症重新識別 |
| 2 | Posterolateral myocardial infarction | 99.90% | 0 / 0 | 與 #1 同理，解剖部位變體 |
| 3 | Pulmonary hypertension（機轉不明/多重因子, WHO Group 5） | 99.89% | 0 / 0 | 機轉關聯薄弱，非特異性 |
| 4 | Pulmonary hypertension owing to lung disease and/or hypoxia（WHO Group 3） | 99.89% | 0 / 20 | 20 篇文獻皆為缺氧基礎生物學研究，無一篇涉及 ACEI 或 lisinopril；理論上全身性降壓可能加重右心灌注不足，需審慎看待 |
| 5 | Malignant renovascular hypertension | 99.89% | 0 / 0 | **安全性疑慮**：若為雙側腎動脈狹窄所致，ACEI 屬經典禁忌／高風險用藥，建議優先排除或加註禁忌症 |

## 結論與下一步

**決策：Hold**

**理由：**
5 個預測適應症證據等級皆為 L5，缺乏臨床試驗或直接相關文獻佐證；rank 1-2 實質為既有 ACEI 心梗後治療地位的重新識別而非新穎發現，rank 3-4 機轉關聯薄弱或無直接證據，rank 5 更存在已知的 ACEI 禁忌症風險，不宜貿然推進。

**若要推進需要：**
- 取得 TFDA／香港仿單警語與禁忌症資料（DG001，Blocking 等級缺口，目前無法進入 S1 安全性初評）
- 補齊完整作用機轉資料以確認機轉關聯性分析（DG002）
- 人工核實各候選適應症的檢索管線是否有遺漏試驗或文獻
- 若考慮推進 rank 5（惡性腎血管性高血壓），須先建立腎功能／腎動脈狹窄篩選機制以排除高風險族群
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

