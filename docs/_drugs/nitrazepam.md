---
layout: default
title: Nitrazepam
parent: 中證據等級 (L3-L4)
nav_order: 623
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-14
description: "Nitrazepam：預測新適應症為睡眠起始與維持障礙 (sleep disorder, initiating and maintaining sleep)（證據等級 L4）。原適應症：失眠 (insomnia)、早期肌陣攣性腦病變"
monitor_inn: "NITRAZEPAM"
predicted_indications: ["sleep disorder, initiating and maintaining sleep", "acute encephalopathy with biphasic seizures and late reduced diffusion", "Wernicke-Korsakoff syndrome"]
---

# Nitrazepam
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

# Nitrazepam：從失眠到睡眠起始與維持障礙

## 一句話總結

Nitrazepam 是一種苯二氮平類（benzodiazepine）藥物，原本用於失眠與早期肌陣攣性腦病變。
TxGNN 模型預測它可能對**睡眠起始與維持障礙 (sleep disorder, initiating and maintaining sleep)** 有效，
目前**無臨床試驗登記**，有 **20 篇文獻**可參考。但此預測與原適應症（失眠）實質上重疊，並非真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 失眠 (insomnia)、早期肌陣攣性腦病變（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 睡眠起始與維持障礙 (sleep disorder, initiating and maintaining sleep) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥物類別知識，Nitrazepam 屬於苯二氮平類，可增強 GABA-A 受體介導的抑制作用，具有鎮靜催眠與抗痙攣效果。

這一機轉與入睡困難及睡眠維持困難的病理相符。但「睡眠起始與維持障礙」本質上就是失眠，與 Nitrazepam 已知的原適應症高度重疊。因此 99.89% 的高分，很可能反映的是模型對既有適應症的辨識，而不是新的藥物再利用發現。

另外兩個較低排名的預測（急性腦病變伴雙相痙攣與延遲性擴散受限、Wernicke-Korsakoff 症候群）僅有模型預測支持，沒有任何臨床試驗或文獻。前者可能與其抗痙攣作用有關，但苯二氮平類僅用於急性發作控制，無證據顯示能改變疾病進程；後者則只能處理併發的酒精戒斷，無法治療硫胺素缺乏，還可能加重認知損害與鎮靜，存在安全疑慮。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

下表列出與 Nitrazepam 及失眠最相關的文獻（資料中的文獻多為綜述或比較性回顧，優先列出有直接資料者）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1743245](https://pubmed.ncbi.nlm.nih.gov/1743245/) | 1991 | 雙盲交叉試驗 | Eur J Clin Pharmacol | 28 名失眠患者，Nitrazepam 5 mg/日與 Oxazepam 25 mg/日皆能有效誘導睡眠並提升睡眠品質 |
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | 臨床報告 | Br Med J | 雙盲試驗顯示 Nitrazepam 的催眠效果與 butobarbitone 相當；27 例急性過量僅見嗜睡 |
| [15252823](https://pubmed.ncbi.nlm.nih.gov/15252823/) | 2004 | 系統性回顧與統合分析 | Hum Psychopharmacol | 比較 Z-drugs 與包含 Nitrazepam 在內的苯二氮平類於短期失眠的療效 |
| [10804040](https://pubmed.ncbi.nlm.nih.gov/10804040/) | 2000 | Review | Drugs | Zolpidem 的催眠療效與包含 Nitrazepam 在內的多種苯二氮平類相當 |
| [15089115](https://pubmed.ncbi.nlm.nih.gov/15089115/) | 2004 | Review | CNS Drugs | 催眠藥的隔日殘餘效應（嗜睡、精神動作與認知受損）及事故風險 |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Review | BMJ Clin Evid | 老年人失眠的盛行率與危險因子 |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | 藥動學回顧 | Clin Pharmacokinet | Nitrazepam 的臨床藥動學 |
| [1125532](https://pubmed.ncbi.nlm.nih.gov/1125532/) | 1975 | 報告 | Br J Psychiatry | Nitrazepam (Mogadon) 依賴性 |
| [20171127](https://pubmed.ncbi.nlm.nih.gov/20171127/) | 2010 | Review | Sleep Med Rev | 催眠藥影響身體平衡，與跌倒及髖部骨折相關 |
| [39231170](https://pubmed.ncbi.nlm.nih.gov/39231170/) | 2024 | 觀察性研究 | PLoS One | 基層醫療中苯二氮平類的使用模式與不適當處方因素，長期使用與依賴、耐受及認知退化相關 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-46067 | ALODORM TAB 5MG | — | 資料未載明 |
| HK-57864 | NITREDON 5 TAB 5MG | — | 資料未載明 |
| HK-20882 | NIPA TAB 5MG | — | 資料未載明 |

---

## 安全性考量

- **藥物交互作用**：已查得 55 筆交互作用紀錄，但交互作用等級皆為未分級。部分紀錄包括 Morphine、Metformin、Bupropion、Metoclopramide、Omeprazole、Dexamethasone 等。其中與 Morphine 等中樞抑制劑併用，臨床上需特別留意。
- **文獻提示的風險**：苯二氮平類與隔日殘餘嗜睡、精神動作受損、跌倒及髖部骨折、依賴與耐受相關，老年人風險尤高。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測與原適應症（失眠）實質重疊，不構成真正的藥物再利用；其餘兩個預測僅有模型分數，無任何試驗或文獻支持，且 Wernicke-Korsakoff 症候群方向存在安全疑慮。

**若要推進需要：**
- 取得 DrugBank 的作用機轉資料，並補齊香港仿單的警語與禁忌症
- 釐清是否存在真正有別於失眠與早期肌陣攣性腦病變的新適應症候選
- 針對急性腦病變伴雙相痙攣的方向，蒐集是否有超越急性發作控制的疾病修飾證據
- 若考慮老年或酒精相關族群，需先建立跌倒、認知與依賴風險的評估與監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

