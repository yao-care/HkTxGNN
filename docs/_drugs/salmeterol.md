---
layout: default
title: Salmeterol
parent: 中證據等級 (L3-L4)
nav_order: 800
evidence_level: L3
indication_count: 5
monitor_inn: "SALMETEROL"
predicted_indications: ["bronchitis", "respiratory malformation", "obstructive lung disease", "Rienhoff syndrome", "atopic eczema"]
last_modified_at: 2026-10-28
description: "Salmeterol：預測新適應症為支氣管炎 (Bronchitis)（證據等級 L3）。原適應症：肺氣腫、內因性氣喘、過敏性氣喘"
---

# Salmeterol
{: .fs-9 }

證據等級: **L3** | 預測適應症: **5** 個
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

## Salmeterol：從肺氣腫與氣喘到支氣管炎
{: .text-alpha }

## 一句話總結

Salmeterol 是長效 β2 腎上腺素受體促效劑，知識圖譜記錄的原適應症包括肺氣腫、內因性氣喘與過敏性氣喘。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，目前有 **8 個臨床試驗**和 **20 篇文獻**列入參考，其中直接以慢性支氣管炎為對象的研究數量有限。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肺氣腫、內因性氣喘、過敏性氣喘（知識圖譜記錄的關係；香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L3 |
| 香港上市 | 上市中（有效許可證 15 張／共 15 張） |
| 許可證數 | 15 張（有效 15 張） |
| 建議決策 | Proceed with Guardrails |

證據等級說明：有一篇直接研究 salmeterol 對慢性支氣管炎病人黏液纖毛清除與咳嗽清除作用的臨床研究（PMID 15970448，14 位受試者），以及以慢性支氣管炎為主題的觀察性世代研究（PMID 19210134）。但沒有已完成、直接以支氣管炎為對象的 Phase 3 RCT，因此判定為 L3。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Salmeterol 屬於長效 β2 受體促效劑，一般認為其透過放鬆氣道平滑肌產生持續的支氣管擴張。一項小型研究顯示，salmeterol 可能改善慢性支氣管炎病人的黏液纖毛清除（PMID 15970448），這與慢性支氣管炎的黏液滯留問題相關。

慢性支氣管炎屬於慢性阻塞性肺病（COPD）的範疇，而 salmeterol（單方或與 fluticasone 複方）已廣泛用於 COPD 的維持治療。因此這項預測較接近既有用藥範圍的延伸，而非全新的再利用方向。

需注意：多數 COPD 試驗以 COPD 為條件，而非單獨針對支氣管炎，且許多試驗使用的是 salmeterol/fluticasone 複方或將 salmeterol 作為對照組，證據需謹慎解讀。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Phase 3 | 完成 | 584 | 比較 tiotropium、salmeterol 吸入氣霧劑與安慰劑於 COPD 的六個月支氣管擴張療效與安全性 |
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Phase 3 | 完成 | 130 | salmeterol/fluticasone 50/500 對比安慰劑，評估 COPD 氣道抗發炎作用 |
| [NCT00269087](https://clinicaltrials.gov/study/NCT00269087) | Phase 3 | 完成 | 122 | salmeterol/fluticasone 複方於 COPD（含慢性支氣管炎、肺氣腫）的 56 週長期安全性 |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | 完成 | 799 | arformoterol 12 個月 COPD 長期安全性研究（以活性藥物為對照，是否為 salmeterol 未確認） |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Phase 3 | 完成 | 741 | arformoterol 12 週 COPD 維持治療，安慰劑與活性對照（對照藥未確認） |
| [NCT00269126](https://clinicaltrials.gov/study/NCT00269126) | Phase 3 | 完成 | 150 | 比較兩種藥物於 COPD 的效果，詳細內容不明 |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Phase 2 | 完成 | 457 | fluticasone/formoterol 劑量探索，以 fluticasone/salmeterol 為參考 |
| [NCT01361984](https://clinicaltrials.gov/study/NCT01361984) | Phase 4 | 狀態未知 | 20 | 比較霧化 arformoterol 與乾粉吸入 salmeterol 於 COPD 的緩解效果 |
| [NCT00233051](https://clinicaltrials.gov/study/NCT00233051) | 不適用 | 提前終止 | 20 | 以誘導痰基因表現作為 COPD 藥物反應的生物標記 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [17557771](https://pubmed.ncbi.nlm.nih.gov/17557771/) | 2007 | RCT | Thorax | 評估 salmeterol/fluticasone 對 COPD 氣道發炎的影響 |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | 臨床研究 | Chest | fluticasone 250/salmeterol 50 於 Diskus 用於 COPD 的療效與安全性，對比安慰劑及單一成分 |
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | 臨床研究 | Pulm Pharmacol Ther | 14 位輕中度慢性支氣管炎病人，評估 salmeterol 對黏液纖毛清除與咳嗽清除的急性效果 |
| [17196106](https://pubmed.ncbi.nlm.nih.gov/17196106/) | 2006 | 統合分析 | Respir Res | salmeterol 50 mcg 每日兩次於 COPD 的臨床相關終點，與安慰劑或常規治療比較 |
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | 臨床研究 | Ther Adv Respir Dis | arformoterol 與 salmeterol 於 COPD 一年的安全性與耐受性 |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | 世代研究 | Curr Med Res Opin | 慢性支氣管炎病人起始 fluticasone/salmeterol 與其他吸入維持治療的住院、急診與費用比較 |
| [15329047](https://pubmed.ncbi.nlm.nih.gov/15329047/) | 2004 | 回顧 | Drugs | salmeterol/fluticasone 乾粉吸入劑於 COPD 的使用回顧 |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | 臨床研究 | Clin Ther | 吸入 salmeterol 與口服 theophylline 於輕中度 COPD 的療效與耐受性（開放性研究） |
| [12236842](https://pubmed.ncbi.nlm.nih.gov/12236842/) | 2002 | 回顧 | Br J Clin Pharmacol | 長效 β2 促效劑的拮抗現象與抗發炎作用探討 |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | 指引 | Basic Clin Pharmacol Toxicol | 芬蘭穩定期 COPD 診斷與藥物治療指引 |

---

## 香港上市資訊

香港共有 15 張單一成分登記的有效許可證（資料中標示為單方，其中多數品名實際為與其他成分合併的吸入製劑）。以下列出 5 張，完整清單可能不止於此；許可證資料未載明劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-35936 | SEREVENT INHALER 25MCG/ACTUATION | 資料未載明 | 資料未載明 |
| HK-51376 | SEROFLO 125 INHALER | 資料未載明 | 資料未載明 |
| HK-51378 | SEROFLO 50 INHALER | 資料未載明 | 資料未載明 |
| HK-48128 | SERETIDE INHALER 25/50 | 資料未載明 | 資料未載明 |
| HK-44735 | SERETIDE ACCUHALER 50MCG/250MCG | 資料未載明 | 資料未載明 |

---

## 安全性考量

- **知識圖譜記錄的禁忌關係（非仿單內容）**：高血壓、長 QT 症候群（含家族性）、癲癇、高血糖、單純疱疹病毒角膜炎、腦下垂體功能低下相關疾病、骨質疏鬆、胸腺疾病等。
- **藥物交互作用**：共查得 100 筆，以下列出部分。
  - 嚴重（Major）：Clarithromycin
  - 中度（Moderate）：Epinephrine、Famotidine、Acarbose、Canagliflozin、Dapagliflozin、Empagliflozin 及多種降血糖藥
  - 輕微（Minor）：Hydrocortisone、Dexamethasone、Budesonide 等皮質類固醇
- **類別提醒**：LABA 於氣喘不建議單獨使用，應與吸入型皮質類固醇併用。

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 支氣管炎（尤其慢性支氣管炎）屬於 COPD 範疇，salmeterol 在此領域已有多項 Phase 3 試驗與臨床研究，TxGNN 分數也很高。
- 但直接以支氣管炎為對象的證據不多，且多數研究使用複方或將 salmeterol 作為對照，且尚無仿單層級的核准適應症資料可確認。

**若要推進需要：**
- 取得香港仿單，確認核准適應症、警語與禁忌
- 釐清各試驗中 salmeterol 單方的角色與直接針對慢性支氣管炎的療效數據
- 補足作用機轉資料
- 針對心血管疾病、長 QT 或併用降血糖藥等族群擬定安全監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

