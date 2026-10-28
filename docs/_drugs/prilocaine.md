---
layout: default
title: Prilocaine
parent: 僅模型預測 (L5)
nav_order: 731
evidence_level: L5
indication_count: 10
monitor_inn: "PRILOCAINE"
predicted_indications: ["papillary conjunctivitis", "manic bipolar affective disorder", "bronchitis", "migraine disorder", "neuralgia", "migraine with brainstem aura", "atopic eczema", "allergic asthma", "rhinitis", "rosacea conjunctivitis"]
last_modified_at: 2026-10-28
description: "Prilocaine：預測新適應症為乳頭狀結膜炎（證據等級 L5）。原適應症：香港許可證資料未載明核准適應症"
---

# Prilocaine
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

## Prilocaine：從知識圖譜記錄的早洩到乳頭狀結膜炎
{: .text-alpha }

## 一句話總結

Prilocaine（丙胺卡因）是醯胺類局部麻醉藥。知識圖譜記錄它與早洩、心因性性交疼痛有關，但這兩項不是香港核准適應症。
TxGNN 模型預測它可能對**乳頭狀結膜炎**有效，但目前**沒有任何臨床試驗或文獻**直接研究這個疾病，僅屬模型推測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症；知識圖譜記錄的關聯為早洩、心因性性交疼痛（僅為圖譜關聯，非核准適應症） |
| 預測新適應症 | 乳頭狀結膜炎 |
| TxGNN 預測分數 | 0.9978 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 13 張／共 13 張） |
| 許可證數 | 13 張（有效 13 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Prilocaine 屬於局部麻醉藥，一般認為是透過阻斷鈉離子通道來抑制神經傳導。這個機轉可能緩解眼表面的不適感。

但乳頭狀結膜炎的核心問題是過敏性或機械性發炎,局部麻醉作用並不能處理這些病因。此外,眼部局部麻醉藥有已知的眼表毒性疑慮,不利於長期使用。因此,高分預測來自 TxGNN 模型(深度學習),可能反映模型從相關疾病間學到的相似性,並非生物學證據,機轉上的支持很薄弱。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 13 張 prilocaine 相關許可證，以下列出 5 張。各許可證的劑型與核准適應症欄位在本報告彙整的資料中皆為空白。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67286 | LIPROKING CREAM | 未載明 | 未載明 |
| HK-59758 | EMLO CREAM | 未載明 | 未載明 |
| HK-59439 | LIPRY CREAM | 未載明 | 未載明 |
| HK-65470 | ZENOCANE CREAM | 未載明 | 未載明 |
| HK-66145 | PRIDOPAN CREAM | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自圖譜的藥物與疾病關係，並非仿單文字）：高血壓、癲癇、腎臟疾病、肝臟疾病、糖尿病、冠狀動脈疾病、心肌梗塞、心臟傳導疾病、房室傳導阻滯、呼吸衰竭、閉角型青光眼、重症肌無力、丁醯膽鹼酯酶缺乏、甲狀腺機能亢進等。
- **藥物交互作用**：共查得 22 筆，其中多數為嚴重等級。主要包括：
  - Metoclopramide
  - Sulfasalazine
  - Amyl Nitrite
  - Rasburicase
  - Chloroquine
  - Primaquine
  - Quinine
  - Tafenoquine
  - Lidocaine（含外用）
  - Benzocaine（外用）
  - Nitric Oxide
  - Dapsone（含外用）
  - Cinchocaine（外用）
  - Silver nitrate（外用）
  - Silver sulfadiazine（外用）
- 其他為中度或輕微等級，例如 Morphine（脂質體）為中度，Hyaluronidase 為輕微。
- 系統性暴露時有高鐵血紅素血症的風險。眼部使用則需留意眼表毒性。

仿單的警語與禁忌資料在本報告彙整的資料中缺漏，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 乳頭狀結膜炎沒有任何直接研究，證據等級僅 L5。
- 局部麻醉作用無法處理病因，且有眼表毒性疑慮，因此不建議推進。

**若要推進需要：**
- 取得 prilocaine 的作用機轉資料與香港仿單的警語、禁忌內容
- 先有針對乳頭狀結膜炎的前臨床或小型臨床研究，並評估眼部安全性

**補充觀察：** 在同一批預測中，**神經痛**（排名第 5，預測分數 0.9934）有較多直接證據。這包括 1 個已完成的 Phase 2 開放標籤研究（NCT00916942，20 人），以及數篇探討 lidocaine/prilocaine 乳膏用於帶狀疱疹後神經痛的文獻，例如 PMID 2493878 與 2616182。這些證據規模小、多為開放標籤且年代較早，也無法區分 prilocaine 與 lidocaine 各自的作用。若要優先探索新適應症，神經痛比乳頭狀結膜炎更值得作為研究問題。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

