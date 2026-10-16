---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 276
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Digoxin：預測新適應症為變異型心絞痛 (Prinzmetal angina)（證據等級 L5）。原適應症：心房顫動、毛地黃中毒"
monitor_inn: "DIGOXIN"
predicted_indications: ["Prinzmetal angina", "duodenal obstruction", "duodenal ulcer (disease)", "duodenogastric reflux", "obsolete susceptibility to ischemic stroke", "hypoalphalipoproteinemia"]
---

# Digoxin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Digoxin：從心房顫動到變異型心絞痛（Prinzmetal angina）

## 一句話總結

Digoxin（地高辛）是強心配醣體類藥物，原本用於心房顫動與毛地黃中毒相關適應症。
TxGNN 模型預測它可能對**變異型心絞痛 (Prinzmetal angina)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇**關聯性很低的文獻，實質證據非常薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 心房顫動、毛地黃中毒（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 變異型心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 99.81% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知藥理而言，Digoxin 抑制心肌細胞的 Na⁺/K⁺-ATPase，使細胞內鈣濃度上升，增強心肌收縮力並減慢房室結傳導，這是它用於心房顫動心率控制的基礎。

變異型心絞痛的成因是冠狀動脈痙攣，標準治療為鈣離子通道阻斷劑與硝酸鹽類。理論上，細胞內鈣上升可能促進血管平滑肌收縮，因此 Digoxin 不僅不太可能有幫助，還可能不利。

兩者同屬心血管疾病，這可能是模型給出高分的原因。我們判斷這較可能是圖譜鄰近性（共同心血管關聯）造成的假象，而非真正的機轉關聯。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Review | Acta Physiol Pharmacol Bulg | 探討時辰藥理學對降血壓治療的影響，並未直接評估 Digoxin 對變異型心絞痛的療效 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60869 | LANOXIN PAEDIATRIC ELIXIR 50MCG/ML | 未載明 | 未載明 |
| HK-03798 | LANOXIN-PG TAB 0.0625MG | 未載明 | 未載明 |
| HK-03780 | LANOXIN TAB 0.25MG | 未載明 | 未載明 |
| HK-03795 | LANOXIN INJ 0.5MG/2ML | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單內容）：腎臟疾病、低鉀血症、高鈣血症、心肌梗塞、冠狀動脈血栓、肺心症、Wolff-Parkinson-White 症候群、病竇症候群、心室顫動、肥厚型心肌病變、房室傳導阻滯、黏液水腫與甲狀腺低下、心肌炎、縮窄性心包膜炎、限制型心肌病變等。其中多項為心臟缺血與傳導異常，與心絞痛族群高度重疊，需特別留意。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 中度：Acarbose、Rabeprazole、Doxycycline、Epinephrine、Hydrocortisone、Metformin、Amphotericin B、Bupropion、Acetylsalicylic acid、Dexamethasone、Tetracycline
  - 輕度：Albiglutide、Hyoscyamine、Atropine、Glycopyrronium

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級僅 L5：沒有臨床試驗，唯一文獻與 Digoxin 無直接關聯。
- 機轉上並不支持（增加細胞內鈣可能加重血管痙攣），高分預測應視為模型假象。

**若要推進需要：**
- 補齊作用機轉資料與香港仿單的警語、禁忌資料
- 釐清 Digoxin 對冠狀動脈痙攣的實際影響（前臨床或機轉研究）
- 若仍要探索，需先有機轉層面的正向證據，再考慮臨床研究；否則建議將研究資源轉向其他候選
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

