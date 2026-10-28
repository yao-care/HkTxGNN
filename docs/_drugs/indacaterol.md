---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 467
evidence_level: L5
indication_count: 10
monitor_inn: "INDACATEROL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "headache disorder", "trigeminal autonomic cephalalgia", "paratenonitis", "calcific tendinitis", "hypertrichosis (disease)", "bronchial disease", "myositis", "anaphylaxis", "Ambras type hypertrichosis universalis congenita"]
last_modified_at: 2026-10-28
description: "Indacaterol：預測新適應症為腎因性抗利尿激素分泌不當症候群 (NSIAD)（證據等級 L5）。原適應症：許可證資料未載明"
---

# Indacaterol
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

## Indacaterol：從原適應症未載明到腎因性抗利尿激素分泌不當症候群
{: .text-alpha }

## 一句話總結

Indacaterol 是一種超長效 β2 腎上腺素受體促效劑（吸入劑），香港已有多張許可證，但本次整理的許可證資料未載明適應症文字。
TxGNN 模型預測它可能對**腎因性抗利尿激素分泌不當症候群 (NSIAD)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬電腦模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 腎因性抗利尿激素分泌不當症候群 (NSIAD) |
| TxGNN 預測分數 | 0.9954 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 13 張／共 13 張） |
| 許可證數 | 13 張（有效 13 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就藥理類別而言，indacaterol 屬於 β2 促效劑，經 β2 受體與 Gs 蛋白偶聯，提高細胞內 cAMP，使支氣管平滑肌放鬆。

NSIAD 是由血管加壓素 V2 受體 (AVPR2) 的功能獲得性突變所致，該受體同樣經 Gs 蛋白偶聯並走 cAMP 路徑。兩者雖共用 cAMP 訊號路徑，但這只是表面上的相似，並沒有已知的治療依據顯示 β2 促效可使 NSIAD 受益。

整體而言，這項高分預測目前只能視為電腦運算的假說，缺乏機轉與臨床上的支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

以下僅列出單方 indacaterol 產品（ONBREZ BREEZHALER 吸入粉末），均為有效許可證，持有人為 NOVARTIS PHARMACEUTICALS (HK) LIMITED。許可證資料未載明核准適應症文字。

| 許可證號 | 品名 | 規格 |
|---------|------|------|
| HK-67628 | ONBREZ BREEZHALER INHALATION POWDER | 150 mcg/膠囊 |
| HK-67725 | ONBREZ BREEZHALER INHALATION POWDER | 300 mcg/膠囊 |
| HK-60180 | ONBREZ BREEZHALER INHALATION POWDER | 150 mcg/膠囊 |
| HK-60179 | ONBREZ BREEZHALER INHALATION POWDER | 300 mcg/膠囊 |

另有 9 張許可證屬於含 indacaterol 的複方產品（ATECTURA、ULTIBRO、ENERZAIR 系列）。複方許可證不能用來說明單方 indacaterol 的核准或上市情形，因此不在此列出。

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：高血壓、長 QT 症候群（含家族性）、癲癇、高血糖、缺鉀、糖尿病、糖尿病酮酸中毒、心因性猝死、心臟傳導疾病、甲狀腺毒症／甲狀腺功能亢進、葛瑞夫茲氏病、冠狀動脈疾病。這些是模型知識圖譜中的關聯，不等同於正式仿單禁忌。
- **藥物交互作用**：資料庫共收錄 100 筆。多數為中度，例如 acarbose、famotidine、epinephrine、metformin、pioglitazone、canagliflozin、dapagliflozin、clarithromycin、isometheptene 等；皮質類固醇（hydrocortisone、dexamethasone、budesonide 等）及 aprepitant 為輕度。降血糖藥物與 epinephrine 的組合需特別留意。

主要警語及仿單禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測只有模型分數，沒有臨床試驗、文獻或合理的機轉依據，證據等級為 L5。
- 長效 β2 促效劑也有潛在的心血管與代謝風險，在缺乏任何療效證據下，不建議推進。

**若要推進需要：**
- 提出 β2 受體訊號與 AVPR2 功能亢進之間的機轉假說，並取得前臨床數據（細胞或動物模型）。
- 補齊 indacaterol 的作用機轉資料，以及香港仿單的警語與禁忌。
- 說明許可證核准適應症的來源資料。

**補充說明：**
同一份分析中，排名第 7 的預測「支氣管疾病」有多項氣喘相關的 Phase 2/3 試驗（例如 NCT01079130、NCT00529529、NCT02554786）及 RCT 文獻。但這大致是印證 indacaterol 本身作為支氣管擴張劑的既有類別用途，並非新的藥物再利用發現。若要評估此方向，應另行確認各地區的標示狀態，以及 LABA 不宜單方用於氣喘的類別警語。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

