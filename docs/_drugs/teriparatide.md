---
layout: default
title: Teriparatide
parent: 僅模型預測 (L5)
nav_order: 865
evidence_level: L5
indication_count: 9
monitor_inn: "TERIPARATIDE"
predicted_indications: ["duodenal ulcer (disease)", "non-syndromic esophageal malformation", "duodenal obstruction", "duodenogastric reflux", "esophageal disease", "Worth syndrome", "autosomal dominant neovascular inflammatory vitreoretinopathy", "succinyl-CoA:3-ketoacid CoA transferase deficiency", "amenorrhea (disease)"]
last_modified_at: 2026-11-20
description: "Teriparatide：預測新適應症為十二指腸潰瘍 (Duodenal Ulcer)（證據等級 L5）。原適應症：知識圖譜中記錄的關聯為停經後骨質疏鬆症、骨質疏鬆症"
---

# Teriparatide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Teriparatide：從骨質疏鬆症到十二指腸潰瘍 (Duodenal Ulcer)
{: .text-alpha }

## 一句話總結

Teriparatide（PTH 1-34）是副甲狀腺素的重組片段，在知識圖譜中記錄的原適應症為停經後骨質疏鬆症與骨質疏鬆症。
TxGNN 模型對**十二指腸潰瘍 (Duodenal Ulcer)** 給出最高預測分數，但目前**沒有任何臨床試驗與文獻**直接支持這個方向，僅屬模型預測（證據等級 L5）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的關聯為停經後骨質疏鬆症、骨質疏鬆症（香港許可證資料中未載明核准適應症文字） |
| 預測新適應症 | 十二指腸潰瘍 (Duodenal Ulcer) |
| TxGNN 預測分數 | 0.9986 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Teriparatide 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「內源性 84 個胺基酸的副甲狀腺素（PTH）是骨骼及腎臟中鈣與磷酸鹽代謝的主要調節因子。PTH 的生理作用包括調節骨骼代謝、腎小管對鈣與磷酸鹽的再吸收，以及腸道對鈣的吸收。[…] PTH 與 teriparatide 的生物作用是透過與特定高親和力細胞表面受體結合而介導。」英文原文："Endogenous 84-amino acid parathyroid hormone (PTH) is the primary regulator of calcium and phosphate metabolism in bone and kidney. Physiological actions of PTH include regulation of bone metabolism, renal tubular reabsorption of calcium and phosphate, and intestinal calcium absorption. […] The biological actions of PTH and teriparatide are mediated through binding to specific high-affinity cell-surface receptors."（[DailyMed: Bonsity (teriparatide) prescribing information, Alvogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d0c89a2-3849-adf6-007d-aeca21cf417c)，版本日期 2026-08-31；查閱日期 2026-11-19）。根據藥理資料，teriparatide 是人類 PTH 1-34 肽段，作用於 PTH1 受體（PTH1R），也可結合 PTH2 受體，臨床上用於骨折高風險的骨質疏鬆症患者，促進成骨細胞介導的骨形成。

骨質疏鬆症與十二指腸潰瘍屬於不同器官系統的疾病。目前沒有已識別的合理機轉，能將 PTH1R 活化與骨合成作用連結到十二指腸黏膜潰瘍。此高分來自 TxGNN 模型（深度學習），可能反映模型在相關疾病之間學到的相似性，而非生物學證據，應審慎看待。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無針對十二指腸潰瘍的相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59594 | FORTEO PRE-FILLED PEN FOR INJ 20MCG/80MCL（Eli Lilly Asia） | 注射劑（預填充筆） | 資料中未載明 |
| HK-68098 | TERIPARATIDE TEVA SOLUTION FOR INJECTION IN PRE-FILLED PEN 20MCG/80MCL（Teva） | 注射劑（預填充筆） | 資料中未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：低血壓疾病、高鈣血症、腎鈣質沉著症、磷代謝疾病、骨肉瘤、骨 Paget 氏病、幼年型 Paget 氏病、骨軟化症、佝僂病、泌尿道結石、腎性骨營養不良、纖維性骨炎、副甲狀腺機能亢進。
- **藥物交互作用**（共 8 筆，含 2 筆藥理標靶資料）：
  - 中度：Calcitriol（外用）、Calcipotriol（外用）、Digoxin、Digitoxin
  - 輕度：Hydrochlorothiazide、Furosemide
- 相關文獻提及 teriparatide 治療期間有鈣質沉著症（calcinosis cutis）惡化的個案報告，以及骨質疏鬆症藥物的不良事件回顧（含骨肉瘤等）。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 十二指腸潰瘍的預測僅來自模型分數，沒有臨床試驗或文獻，也找不到合理的作用機轉，屬於 L5。
- 同批預測中，閉經（amenorrhea）相關的骨密度議題雖有間接文獻脈絡，但那是針對閉經引起的骨流失，並非直接治療該疾病，且尚缺乏試驗資料。

**若要推進需要：**
- 補齊作用機轉資料，評估 PTH1R 訊號與消化道黏膜之間是否存在生物學關聯
- 取得香港仿單中的核准適應症、警語與禁忌
- 先做系統性文獻檢索與前臨床研究，確認是否有任何支持十二指腸潰瘍的證據
- 若有進一步研究，需評估已知安全性風險（如骨肉瘤相關警語、高鈣血症）是否影響使用族群

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Bonsity (teriparatide) prescribing information, Alvogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2d0c89a2-3849-adf6-007d-aeca21cf417c) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

