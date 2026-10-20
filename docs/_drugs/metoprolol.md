---
layout: default
title: Metoprolol
parent: 僅模型預測 (L5)
nav_order: 578
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Metoprolol：預測新適應症為惡性腎血管性高血壓 (Malignant Renovascular Hypertension)（證據等級 L5）。原適應症：高血壓、急性冠心症、心肌梗塞"
monitor_inn: "Metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "trichotillomania"]
---

# Metoprolol
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

# Metoprolol：從高血壓與心肌梗塞到惡性腎血管性高血壓

## 一句話總結

Metoprolol 是 β1 選擇性受體阻斷劑，原本用於高血壓、急性冠心症與心肌梗塞等心血管疾病。
TxGNN 模型預測它可能對**惡性腎血管性高血壓 (Malignant Renovascular Hypertension)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇**關聯性很低的文獻（嗜鉻細胞瘤的診斷研究），證據實質上只有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、急性冠心症、心肌梗塞（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 惡性腎血管性高血壓 (Malignant Renovascular Hypertension) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Metoprolol 是 β1 選擇性阻斷劑，可降低腎素釋放與心輸出量，機轉上可能適用於腎素依賴型的高血壓。

惡性腎血管性高血壓本質上是高血壓的一種嚴重亞型，與 Metoprolol 已核准的高血壓適應症高度重疊，因此模型給出高分並不意外。不過這也代表它**不算真正的新適應症**，而是既有適應症的延伸。

唯一檢索到的文獻討論的是嗜鉻細胞瘤的診斷標記（Chromogranin A），與 Metoprolol 治療此疾病無關，無法作為支持證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1988765](https://pubmed.ncbi.nlm.nih.gov/1988765/) | 1991 | 診斷研究 | Medicine | Chromogranin A 用於嗜鉻細胞瘤診斷，敏感度 83%、特異度 96%；未評估 Metoprolol 療效，僅間接相關 |

## 香港上市資訊

Metoprolol 在香港共有 20 張有效單方許可證（無已註銷）。資料中未載明劑型與核准適應症文字，下表列出其中 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-19220 | BETALOC TAB 50MG | 未載明 | 未載明 |
| HK-49649 | BETALOC ZOK TAB 25MG | 未載明 | 未載明 |
| HK-34975 | BETALOC ZOK TAB 50MG CONTROL RELEASE | 未載明 | 未載明 |
| HK-19885 | BETALOC IV INJ 1MG/ML | 未載明 | 未載明 |
| HK-36511 | MINAX 100 TAB | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜標示的禁忌疾病**：焦慮症、胰臟炎、肝臟疾病、膽囊疾病、全身性紅斑性狼瘡、乾癬、糖尿病與糖尿病酮酸中毒、低血壓、痛風、重症肌無力、嗜鉻細胞瘤等（來自知識圖譜關聯，並非仿單原文，需以仿單核對）。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 中度：Epinephrine、Bupropion、Morphine、Cimetidine、Canagliflozin、Dapagliflozin、Chlorpropamide，以及多種皮質類固醇（Hydrocortisone、Dexamethasone、Betamethasone 等）
  - 輕度：Acetylsalicylic acid、Magnesium oxide

仿單的警語與禁忌資料尚未取得，完整安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但沒有任何臨床試驗或直接文獻支持，證據僅為 L5。
- 此適應症屬於已核准高血壓的亞型，不是真正的新用途，投入開發的附加價值有限。

**若要推進需要：**
- 補齊作用機轉資料（MOA）與香港仿單的警語、禁忌內容
- 針對惡性腎血管性高血壓的專屬臨床或文獻證據
- 評估是否改以既有高血壓適應症的範圍來定位
- 同批預測中，**慢性肺心病（chronic pulmonary heart disease）**的證據較多（有 Phase 3/4 試驗與 COPD 合併心衰的研究，等級 L3），但結果不一（NCT02587351 提前終止，bisoprolol COPD 試驗未顯示益處），可作為後續研究問題另行評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

