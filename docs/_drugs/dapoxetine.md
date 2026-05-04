---
layout: default
title: Dapoxetine
parent: 中證據等級 (L3-L4)
nav_order: 175
evidence_level: L4
indication_count: 3
---

# Dapoxetine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Dapoxetine：從早洩到偏頭痛

## 一句話總結

Dapoxetine 是一種短效 SERT 抑制劑，臨床核准適應症為早洩（Premature Ejaculation）。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
目前有 **0 個臨床試驗**和 **2 篇文獻**支持這個方向，且文獻均非直接針對此適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 早洩（Premature Ejaculation） |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.34% |
| 證據等級 | L4 |
| 台灣上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Dapoxetine 是一種短半衰期的選擇性血清素再回收抑制劑（SERT 抑制劑），t½ 約 1.5 小時，設計用於「按需給藥」（on-demand dosing）以治療早洩，而非每日長期服用。

從類別效應（Class Effect）角度看，同屬 SSRI 的藥物（如 fluoxetine、amitriptyline）確實具有偏頭痛預防效果，其機轉涉及 5-HT 系統調節與三叉神經血管通路抑制。Dapoxetine 理論上具有相同靶點，因此 TxGNN 模型透過知識圖譜中的 SSRI 類別連結而做出此預測。

然而，此預測屬於**間接推論**，存在根本的藥動學障礙：偏頭痛預防需要持續穩定的血藥濃度（每日給藥），而 Dapoxetine 的超短半衰期（1.5h）使其無法維持所需的持續 5-HT 調節效果，與臨床上用於預防偏頭痛的 SSRI 藥物的藥動學特性（t½ 24–72h）有本質差異。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [33998993](https://pubmed.ncbi.nlm.nih.gov/33998993/) | 2022 | Narrative Review | Current Neuropharmacology | SSRI 類藥物超適應症使用綜述，提及偏頭痛為 SSRI 可能的超適應症應用領域之一，非 dapoxetine 特異性資料 |
| [23504864](https://pubmed.ncbi.nlm.nih.gov/23504864/) | 2013 | Observational Study | Urologia | 研究 dapoxetine 用於早洩的治療依從性，與偏頭痛無直接關聯 |

> ⚠️ **注意**：上述兩篇文獻均非直接研究 dapoxetine 用於偏頭痛；第一篇僅在 SSRI 類別層面提及偏頭痛，第二篇與偏頭痛完全無關。

---

## 台灣上市資訊

Dapoxetine 目前在台灣**尚未取得藥品許可證**，無相關上市資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
雖然 TxGNN 模型基於 SSRI 類別效應給出高預測分數（99.34%），但 dapoxetine 的超短半衰期（t½ ≈ 1.5h）在藥動學上根本不適合偏頭痛預防給藥，且目前完全缺乏針對此適應症的臨床試驗或直接文獻支持，僅有間接的 SSRI 類別層面推論。

**若要推進需要：**
- 補充完整的 MOA 資料（DrugBank API 查詢），確認 dapoxetine 是否有任何偏頭痛相關的特異性機轉
- 評估是否有緩釋劑型（Extended-Release）的研發計畫，以克服藥動學限制
- 進行台灣 TFDA 仿單查詢，補充安全性警語與禁忌症資料
- 考慮將此候選列入低優先序，優先評估其他 TxGNN 預測候選（如 dysthymic disorder）的機轉可行性，儘管後者同樣面臨藥動學挑戰
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

