---
layout: default
title: Teriparatide
parent: 僅模型預測 (L5)
nav_order: 865
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Teriparatide：預測新適應症為十二指腸潰瘍 (Duodenal Ulcer)（證據等級 L5）。原適應症：停經後骨質疏鬆症、骨質疏鬆症"
monitor_inn: "TERIPARATIDE"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease"]
---

# Teriparatide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Teriparatide：從停經後骨質疏鬆症到十二指腸潰瘍

## 一句話總結

Teriparatide 是副甲狀腺素（PTH 1-34）的類似物，原本用於治療停經後骨質疏鬆症與骨質疏鬆症。
TxGNN 模型預測它可能對**十二指腸潰瘍 (Duodenal Ulcer)** 有效，但目前**沒有任何臨床試驗，也沒有直接支持此適應症的文獻**，僅是模型的計算預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 停經後骨質疏鬆症、骨質疏鬆症 |
| 預測新適應症 | 十二指腸潰瘍 (Duodenal Ulcer) |
| TxGNN 預測分數 | 99.86% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥理資料，teriparatide 是 PTH 1-34 胜肽，作用於 PTH1 受體（PTH1R）與 PTH2 受體（PTH2R），在骨質疏鬆症中用於刺激骨形成、降低高骨折風險患者的骨折機率。

骨質疏鬆症與十二指腸潰瘍屬於不同器官系統的疾病，目前沒有已知機轉可將 PTH1R 介導的骨合成作用連結到十二指腸潰瘍的癒合。高分數（99.86%）僅代表知識圖譜中的網路關聯，不等於生物學上的合理性。

因此，這項預測應視為假說產生的線索，在取得機轉或實驗證據之前，不宜視為有效的再利用方向。排名較後的其他預測（食道畸形、十二指腸阻塞、十二指腸胃逆流）同樣缺乏證據，且多屬結構性或動力性疾病，與骨合成作用無明顯關聯。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無針對十二指腸潰瘍的相關文獻。

（備註：在同一藥物排名第 5 的預測「食道疾病」下，檢索到 2 篇文獻，但均為安全性資訊，並非療效證據，僅供參考。）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19412101](https://pubmed.ncbi.nlm.nih.gov/19412101/) | 2009 | Review | Current opinion in rheumatology | 回顧骨質疏鬆症治療的不良事件，包括心房顫動、骨痛、顎骨壞死、非典型骨折與骨肉瘤 |
| [26992073](https://pubmed.ncbi.nlm.nih.gov/26992073/) | 2016 | Case report | The British journal of dermatology | 兩名患自體免疫疾病的骨質疏鬆患者在使用 teriparatide 後皮膚鈣質沉著症惡化 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59594 | FORTEO PRE-FILLED PEN FOR INJ 20MCG/80MCL（Eli Lilly Asia） | 預填充注射筆 | 未提供 |
| HK-68098 | TERIPARATIDE TEVA SOLUTION FOR INJECTION IN PRE-FILLED PEN 20MCG/80MCL（Teva） | 預填充注射筆 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：低血壓疾病、高血鈣、腎鈣質沉著症、磷代謝疾病、骨肉瘤、骨 Paget 病、幼年型 Paget 病、骨軟化症、佝僂病、泌尿道結石、腎性骨營養不良、纖維囊性骨炎、副甲狀腺機能亢進。（此為知識圖譜的藥物－疾病關聯，並非仿單內容。）
- **藥物交互作用**（共 8 筆，其中 6 筆為藥物交互作用）：
  - 中度：Calcitriol（外用）、Calcipotriol（外用）、Digoxin、Digitoxin
  - 輕度：Hydrochlorothiazide、Furosemide
- **文獻中的安全訊號**：有病例報告指出使用 teriparatide 後皮膚鈣質沉著症惡化；綜述亦提及骨肉瘤、心房顫動等需關注的不良事件。

仿單的警語與禁忌資料尚未取得，完整安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 十二指腸潰瘍此預測僅有模型分數，沒有臨床試驗與文獻支持，且找不到 PTH1R 作用與潰瘍癒合之間的合理機轉。
- 同時，teriparatide 具有多項潛在禁忌（如高血鈣、骨肉瘤風險），對未經驗證的新適應症不宜貿然推進。

**若要推進需要：**
- 補齊 teriparatide 的作用機轉資料，並評估其與十二指腸潰瘍病理的可能關聯
- 進行前臨床研究（如動物潰瘤模型），驗證是否有任何保護或癒合效果
- 取得香港仿單的警語與禁忌內容，完成安全性篩檢
- 系統性檢索文獻與試驗登記，確認是否存在未被收錄的證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

