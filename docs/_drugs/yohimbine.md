---
layout: default
title: Yohimbine
parent: 僅模型預測 (L5)
nav_order: 947
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Yohimbine：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "Yohimbine"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "attention deficit-hyperactivity disorder", "faciodigitogenital syndrome", "migraine with or without aura, susceptibility to", "primary hereditary glaucoma", "headache disorder", "transient ischemic attack (disease)", "common cold", "open-angle glaucoma"]
---

# Yohimbine
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

## Yohimbine：從（原適應症未載明）到偏頭痛 (Migraine Disorder)
{: .text-alpha }

## 一句話總結

Yohimbine（育亨賓）是一種選擇性 alpha-2 腎上腺素受體拮抗劑，香港已有 1 張許可證，但資料中未載明核准適應症。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，不過目前**沒有臨床試驗**，僅有 **7 篇間接的前臨床或機轉文獻**，且作用方向（拮抗劑 vs. 激動劑）存疑。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明（許可證的核准適應症欄位為空） |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.94% |
| 證據等級 | L4（僅有前臨床／機轉研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Yohimbine 是經典的 alpha-2 腎上腺素受體拮抗劑，對 alpha-1 受體也有中等親和力。藥理資料庫另顯示它與多種血清素受體（5-HT1A/1B/1D/1E/1F、5-HT2B、5-HT5A、5-HT7）及 alpha-2A/2B/2C 受體有交互作用。

偏頭痛的病理與去甲腎上腺素、血清素訊號有關。前臨床文獻指出，這些系統會影響皮質擴散性抑制（cortical spreading depression，偏頭痛先兆的生物學基礎）、三叉神經血管痛覺傳導，以及腦膜動脈張力。這是模型預測的合理來源。

但要特別注意：文獻中被研究的多半是 alpha-2 **激動劑**（如 clonidine），而 Yohimbine 是**拮抗劑**，預期方向可能相反，或淨效果不明。因此這個預測目前只能視為研究假說，而非治療依據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [2905875](https://pubmed.ncbi.nlm.nih.gov/2905875/) | 1988 | Review | Annals of Clinical Research | 回顧作用於 alpha 腎上腺素受體藥物的治療應用，焦點多在 alpha-2 激動劑 |
| [27497768](https://pubmed.ncbi.nlm.nih.gov/27497768/) | 2016 | 人體實驗研究 | The Journal of Pain | 健康人體雙盲交叉試驗，探討鴉片受體與 alpha-2 受體在抑制性痛覺調節的角色 |
| [2985264](https://pubmed.ncbi.nlm.nih.gov/2985264/) | 1985 | 小型觀察性研究（兒童） | Cephalalgia | 以 3H-yohimbine 測量偏頭痛兒童血小板 alpha 受體，結合量與對照組無差異，解離常數較高 |
| [15829916](https://pubmed.ncbi.nlm.nih.gov/15829916/) | 2005 | 前臨床（大鼠） | J Cereb Blood Flow Metab | 腎上腺素激動劑與拮抗劑皆影響皮質擴散性抑制的傳播，可能與偏頭痛預防有關 |
| [29856967](https://pubmed.ncbi.nlm.nih.gov/29856967/) | 2018 | 前臨床（動物） | Experimental Neurology | 壓力經由 alpha-2 與糖皮質素受體調節皮質興奮性 |
| [15778266](https://pubmed.ncbi.nlm.nih.gov/15778266/) | 2005 | 前臨床（動物） | J Pharmacol Exp Ther | 多巴胺在三叉神經血管痛覺模型中的角色 |
| [17103145](https://pubmed.ncbi.nlm.nih.gov/17103145/) | 2006 | 體外（豬腦膜動脈） | Naunyn-Schmiedeberg's Arch Pharmacol | 比較現有與潛在抗偏頭痛藥物對腦膜動脈的作用 |
| [23707349](https://pubmed.ncbi.nlm.nih.gov/23707349/) | 2013 | 前臨床（大鼠） | Eur J Pharmacol | Ergotamine 的升壓反應可被 yohimbine 阻斷，辨識 alpha 受體亞型 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-44766 | PMS-YOHIMBINE TAB 6MG | 錠劑（資料未載明） | 資料未載明 |

---

## 安全性考量

- **知識圖譜標示的潛在禁忌疾病**（來自 TxGNN 知識圖譜，並非仿單內容）：焦慮症、神經症、輕鬱症 (dysthymic disorder)、腎臟疾病、輸尿管積膿、肝臟疾病、膽囊疾病、低血壓、心臟疾病、心血管疾病。
- **藥物交互作用**（共查得 20 筆，列出主要者）：
  - **嚴重 (Major)**：Iobenguane (I-131)
  - **中度 (Moderate)**：Lorcaserin、Troglitazone、Doxepin（含外用）、Procarbazine
  - **輕微 (Minor)**：Morphine（含脂質體劑型）
- 另外，與 alpha-2 作用相關的前臨床文獻提示，阻斷 alpha-2 受體可能使 ADHD 樣症狀（過動、認知受損）惡化，在相關族群需格外謹慎。

仿單的警語與禁忌資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，證據僅為間接的前臨床與機轉研究（L4）。
- Yohimbine 為 alpha-2 拮抗劑，而偏頭痛相關研究多使用 alpha-2 激動劑，作用方向可能相反。TxGNN 分數雖高，但不足以支持推進。
- 知識圖譜顯示多項心血管、肝腎與精神科相關禁忌，且資料中缺少仿單的警語與禁忌。

**若要推進需要：**
- 取得香港仿單（警語、禁忌、核准適應症）及 DrugBank 的作用機轉資料。
- 釐清 alpha-2 拮抗在偏頭痛模型中的作用方向（可先進行專門的前臨床實驗）。
- 在有任何人體證據之前，不建議進入臨床開發；可考慮改評估其他預測適應症，但目前其他預測（如 ADHD、青光眼、短暫性腦缺血發作）的機轉也多指向相反方向或無證據支持。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

