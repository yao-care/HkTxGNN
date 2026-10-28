---
layout: default
title: Pitolisant
parent: 僅模型預測 (L5)
nav_order: 708
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Pitolisant：預測新適應症為失眠症 (Insomnia)（證據等級 L4）。原適應症：猝睡症（narcolepsy）、猝睡症合併猝倒症候群"
monitor_inn: "PITOLISANT"
predicted_indications: ["insomnia (disease)", "attention deficit-hyperactivity disorder", "faciodigitogenital syndrome"]
---

# Pitolisant
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Pitolisant：從猝睡症到失眠 (Insomnia)（預測）
{: .text-alpha }

## 一句話總結

Pitolisant 是一種組織胺 H3 受體拮抗劑／反向促效劑，原本用於猝睡症（narcolepsy，含猝倒型）的治療。
TxGNN 模型預測它可能對**失眠症 (Insomnia)** 有效，但目前**沒有任何臨床試驗**，且現有文獻僅涉及猝睡症與阻塞性睡眠呼吸中止症，**並未直接支持失眠適應症**，機轉上甚至可能相反。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 猝睡症（narcolepsy）、猝睡症合併猝倒症候群 |
| 預測新適應症 | 失眠症 (Insomnia) |
| TxGNN 預測分數 | 0.9971 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中未收錄原廠 MOA 欄位）。根據文獻，Pitolisant 是選擇性組織胺 H3 受體拮抗劑／反向促效劑，能增加腦內組織胺的神經傳導並促進清醒，已在歐美核准用於成人猝睡症。

**但這個預測在機轉上並不合理。** 失眠的治療通常是要降低覺醒程度，而 Pitolisant 的作用是提高覺醒，方向恰好相反。失眠本身也是 Pitolisant 已知的不良反應之一，因此它可能使失眠惡化。

TxGNN 模型（深度學習）給出的高分（0.9971）可能反映模型學到的相關疾病之間的相似性，而不是生物學證據。

**其他預測（供參考）：**
- **注意力不足過動症（ADHD，分數 0.9936，證據 L4）**：H3 受體阻斷會增加前額葉的組織胺、多巴胺、正腎上腺素與乙醯膽鹼釋放，與 ADHD 的注意力和認知缺損有間接關聯。但目前無 ADHD 專屬試驗，僅有綜述文獻，且文獻提到 H3 拮抗劑在 ADHD 的臨床試驗結果令人失望。可視為「研究假說」，尚不足以建議推進。
- **面指趾生殖器症候群（Aarskog-Scott 症候群，分數 0.9929，證據 L5）**：這是 FGD1 突變引起的罕見 X 染色體連鎖發育疾病，與 H3 拮抗作用無合理機轉關聯，也沒有任何試驗或文獻，僅為計算預測。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下文獻皆**非失眠症研究**，主要反映 Pitolisant 在猝睡症及相關嗜睡疾病的證據。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | 評估 Pitolisant 對已接受 CPAP 的阻塞性睡眠呼吸中止症患者殘餘日間嗜睡的效果 |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | 評估 Pitolisant 對拒絕 CPAP 的中重度睡眠呼吸中止症患者日間嗜睡的療效與安全性 |
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | 臨床試驗（Phase 3） | Lancet Neurol | 評估 Pitolisant 在 6 歲以上猝睡症兒童（含或不含猝倒）的安全性與療效 |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | 真實世界世代研究 | Rev Neurol | 對既往治療無效或不耐受的 1 型猝睡症患者，評估 Pitolisant 的效果與安全性 |
| [41588264](https://pubmed.ncbi.nlm.nih.gov/41588264/) | 2026 | 真實世界世代研究 | Neurol Sci | 中國 40 名兒童猝睡症患者使用 Pitolisant 的回溯性觀察研究 |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Review | Drug Des Devel Ther | Pitolisant 在猝睡症治療的設計、開發與定位 |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Review | Curr Neuropharmacol | 神經精神疾病中組織胺系統的變化與潛在治療；提及 Pitolisant 用於猝睡症嗜睡，doxepin（H1 拮抗劑）用於改善失眠 |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Review | Handb Clin Neurol | 組織胺受體、促效劑與拮抗劑在健康與疾病中的角色 |
| [42525367](https://pubmed.ncbi.nlm.nih.gov/42525367/) | 2026 | Review | Neurol Ther | 兒童睡眠障礙（含失眠、猝睡症、OSA）的現有與新興療法 |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Review | Clin Neuropharmacol | Pitolisant 作為難治性嗜睡青少年猝睡症的替代興奮劑 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67770 | WAKIX TABLETS 4.5MG | 錠劑 | 未提供 |
| HK-67769 | WAKIX TABLETS 18MG | 錠劑 | 未提供 |

兩張許可證皆為單一成分、狀態有效，持證商為 JACOBSON MARKETING LIMITED。

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為部分代表：
  - **嚴重 (Major)**：Bupropion、Dolasetron
  - **中度 (Moderate)**：Famotidine、Hydrocortisone、Metformin、Loperamide、Triamcinolone、Morphine、Acetylsalicylic acid、Dexamethasone、Clarithromycin、Cimetidine 等
- **與預測適應症相關的提醒**：失眠為 Pitolisant 已知的不良反應，若用於失眠患者有惡化症狀的風險。

其他警語與禁忌症資料不足，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- Pitolisant 促進清醒的機轉與失眠治療的目標相反，且無任何失眠專屬的臨床試驗或文獻，TxGNN 的高分應視為網絡關聯而非治療證據。
- 證據等級僅為 L4，現有文獻皆針對猝睡症與睡眠呼吸中止症的嗜睡。

**若要推進需要：**
- 釐清模型預測與機轉相反的原因（例如是否為睡眠－覺醒網絡鄰近性造成的假陽性）
- 取得完整的作用機轉資料與香港仿單的警語、禁忌症
- 若有興趣探索，可將 **ADHD** 作為較合理的假說方向，先進行前臨床或小型探索性研究
- 不建議針對失眠症或 Aarskog-Scott 症候群投入進一步開發資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

