---
layout: default
title: Formoterol
parent: 高證據等級 (L1-L2)
nav_order: 399
evidence_level: L1
indication_count: 6
last_modified_at: 2026-10-14
description: "Formoterol：預測新適應症為支氣管炎 (Bronchitis)（證據等級 L1）。原適應症：肺氣腫、內因性氣喘、過敏性氣喘"
monitor_inn: "Formoterol"
predicted_indications: ["respiratory malformation", "bronchitis", "Rienhoff syndrome", "obstructive lung disease", "asthma", "asthma-related traits, susceptibility to"]
---

# Formoterol
{: .fs-9 }

證據等級: **L1** | 預測適應症: **6** 個
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

# Formoterol：從肺氣腫與氣喘到支氣管炎

## 一句話總結

Formoterol 是長效 β2 受體促效劑（LABA），原本用於肺氣腫、內因性氣喘與過敏性氣喘。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，目前有 **19 個臨床試驗**和 **20 篇文獻**支持這個方向。
不過這項預測較接近既有 COPD 用途的延伸，並非全新的藥物再利用。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺氣腫、內因性氣喘、過敏性氣喘（來自知識圖譜；許可證未載明核准適應症文字） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Proceed with Guardrails |

> 說明：TxGNN 排名第 1 的預測為「呼吸道畸形」（分數 99.92%），但其機轉上缺乏合理連結，證據等級僅 L5，建議 Hold。本報告改以證據最完整、最具臨床意義的「支氣管炎」作為主要評估對象。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Formoterol 是長效 β2 受體促效劑，可放鬆氣道平滑肌、改善氣流受限，吸入後數分鐘內起效，作用可維持約 12 小時。

慢性支氣管炎屬於 COPD 範疇，與其原適應症（肺氣腫、氣喘）同為阻塞性氣道疾病。Formoterol 在 COPD 的使用已有大量 Phase 3 試驗支持，因此 TxGNN 的預測在臨床上合理。

需要注意：對急性支氣管炎、嗜酸性支氣管炎，以及造血幹細胞移植後的閉塞性細支氣管炎，證據較弱，多為小型 Phase 2 研究。因此這比較像是既有用途的延伸，而非全新適應症。

---

## 臨床試驗證據

以下列出最相關的 10 項試驗（資料中共 19 項）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | 完成 | 799 | arformoterol（formoterol 對映異構物）用於 COPD 的 12 個月長期安全性 |
| [NCT00250679](https://clinicaltrials.gov/study/NCT00250679) | Phase 3 | 完成 | 443 | arformoterol 吸入溶液用於 COPD 的 6 個月長期安全性 |
| [NCT01437540](https://clinicaltrials.gov/study/NCT01437540) | Phase 3 | 完成 | 590 | aclidinium/formoterol 複方用於穩定型 COPD 的長期安全性與耐受性 |
| [NCT01437397](https://clinicaltrials.gov/study/NCT01437397) | Phase 3 | 完成 | 1692 | aclidinium/formoterol 複方 24 週支氣管擴張效果 |
| [NCT01462942](https://clinicaltrials.gov/study/NCT01462942) | Phase 3 | 完成 | 2443 | aclidinium/formoterol 複方對穩定型 COPD 的療效與安全性 |
| [NCT01572792](https://clinicaltrials.gov/study/NCT01572792) | Phase 3 | 完成 | 921 | aclidinium/formoterol 複方 28 週延伸研究 |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Phase 3 | 完成 | 741 | arformoterol 12 週維持治療的支氣管擴張效果 |
| [NCT00624754](https://clinicaltrials.gov/study/NCT00624754) | Phase 2 | 完成 | 32 | budesonide/formoterol 用於異體造血幹細胞移植後閉塞性細支氣管炎 |
| [NCT01078623](https://clinicaltrials.gov/study/NCT01078623) | Phase 2 | 完成 | 176 | aclidinium/formoterol 兩種複方劑量範圍研究（COPD） |
| [NCT06571942](https://clinicaltrials.gov/study/NCT06571942) | Phase 4 | 未知 | 128 | 吸入三合一療法對 COPD 或無阻塞慢性支氣管炎小氣道的影響 |

---

## 文獻證據

以下列出最相關的 10 篇（資料中共 20 篇）：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31015757](https://pubmed.ncbi.nlm.nih.gov/31015757/) | 2019 | Meta-analysis | Int J Chron Obstruct Pulmon Dis | 評估 budesonide/formoterol 用於穩定型 COPD 的風險 |
| [20714376](https://pubmed.ncbi.nlm.nih.gov/20714376/) | 2010 | Review | Int J Chron Obstruct Pulmon Dis | 噴霧型 formoterol 用於 COPD 的療效與安全性回顧 |
| [27143870](https://pubmed.ncbi.nlm.nih.gov/27143870/) | 2016 | Review | Int J Chron Obstruct Pulmon Dis | LAMA + LABA 雙重療法用於 COPD 的科學依據 |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Guideline | Basic Clin Pharmacol Toxicol | 芬蘭穩定型 COPD 診斷與藥物治療指引 |
| [41654451](https://pubmed.ncbi.nlm.nih.gov/41654451/) | 2026 | Pharmacovigilance | Clin Ther | 以 FAERS、JADER、CVAR 資料庫評估 budesonide/formoterol 的真實世界安全性 |
| [25835160](https://pubmed.ncbi.nlm.nih.gov/25835160/) | 2015 | 臨床研究 | Am J Respir Crit Care Med | budesonide/formoterol 用於造血幹細胞移植後閉塞性細支氣管炎 |
| [27229850](https://pubmed.ncbi.nlm.nih.gov/27229850/) | 2016 | 臨床研究 | Respir Res | budesonide/formoterol、montelukast 與 N-acetylcysteine 用於移植後閉塞性細支氣管炎 |
| [27916620](https://pubmed.ncbi.nlm.nih.gov/27916620/) | 2017 | 臨床研究 | Chest | glycopyrrolate/formoterol MDI 用於 COPD 的療效與安全性（PINNACLE-1/2） |
| [28740376](https://pubmed.ncbi.nlm.nih.gov/28740376/) | 2017 | RCT | Int J Chron Obstruct Pulmon Dis | fluticasone propionate/formoterol 用於 COPD 的隨機對照試驗 |
| [35432356](https://pubmed.ncbi.nlm.nih.gov/35432356/) | 2022 | Cohort | Front Immunol | 非氣喘性嗜酸性支氣管炎與嗜酸性氣喘患者的嗜酸性球前驅細胞比較 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61392 | FOSTER PRESSURISED INHALATION SOLUTION 100/6 MICROGRAMS PER ACTUATION | 未載明 | 未載明 |
| HK-62090 | FLUTIFORM 250 MICROGRAM/10 MICROGRAM PER ACTUATION PRESSURISED INHALATION SUSPENSION | 未載明 | 未載明 |
| HK-64503 | DUAKLIR GENUAIR INHALATION POWDER 340 MCG/12 MCG | 未載明 | 未載明 |
| HK-60618 | VANNAIR PRESSURIZED METERED-DOSE INHALER 80/4.5MCG/DOSE | 未載明 | 未載明 |
| HK-49176 | SYMBICORT TURBUHALER 160/4.5MCG/DOSE | 未載明 | 未載明 |

共 13 張有效許可證，此處僅列 5 張。

---

## 安全性考量

- **禁忌症（來自知識圖譜的藥物－疾病關聯，非仿單內容）**：高血壓、long QT 症候群（含家族性）、癲癇、肝臟疾病、膽囊疾病，以及腦下垂體功能低下相關疾病等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 中度：acarbose、famotidine、clarithromycin、cisapride、dolasetron、ephedrine、isometheptene，以及多種降血糖藥（如 canagliflozin、dapagliflozin、empagliflozin、alogliptin、albiglutide、dulaglutide、chlorpropamide）
  - 輕度：beclomethasone、betamethasone、budesonide、dexamethasone 等皮質類固醇

香港仿單的警語與禁忌資料尚未取得，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 針對支氣管炎（以慢性支氣管炎／COPD 表型為主），有多項大型 Phase 3 試驗與 meta-analysis 支持，證據等級為 L1。但此用途與 Formoterol 現有的 COPD 與氣喘用途高度重疊，屬延伸應用。
- 排名第 1 的「呼吸道畸形」與第 3 的「Rienhoff 症候群」缺乏機轉依據，也沒有臨床證據，建議 Hold。「氣喘相關性狀易感性」是遺傳性狀而非可治療的疾病，同樣建議 Hold。

**若要推進需要：**
- 明確限定適用表型（慢性支氣管炎／COPD），急性支氣管炎、嗜酸性支氣管炎與移植後閉塞性細支氣管炎不納入。
- 取得香港仿單的核准適應症、警語與禁忌資料。
- 補充作用機轉資料。
- 擬定心血管風險監測計畫，涵蓋高血壓與 QT 延長風險族群。
- 使用固定劑量複方並遵循指引；氣喘患者不可單用 LABA 而不併用吸入型類固醇。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

