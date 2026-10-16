---
layout: default
title: Clomipramine
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Clomipramine：預測新適應症為焦慮症 (Anxiety Disorder)（證據等級 L5）。原適應症：強迫症 (Obsessive-compulsive disorder)"
---

# Clomipramine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Clomipramine：從強迫症到焦慮症

## 一句話總結

Clomipramine 是一種三環類抗憂鬱劑，原本用於強迫症 (OCD) 的治療。
TxGNN 模型預測它可能對**焦慮症 (Anxiety Disorder)** 有效，
目前有 **8 個臨床試驗**和 **20 篇文獻**與這個方向相關，但臨床試驗多為強迫症研究，並非直接驗證焦慮症療效。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 強迫症 (Obsessive-compulsive disorder)（香港許可證未列出適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 焦慮症 (Anxiety Disorder) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L3（無已完成的焦慮症專屬 RCT；僅有間接的強迫症試驗，另有觀察性研究、臨床研究與系統性回顧） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 的 MOA 欄位為空）。根據已知藥理，Clomipramine 是強效的血清素再回收抑制劑，其活性代謝物 desmethylclomipramine 另有去甲腎上腺素活性。血清素與去甲腎上腺素調節，是恐慌症等焦慮症治療的既定藥理基礎。

強迫症過去被歸類為焦慮症的一種，與恐慌症、廣泛性焦慮症、懼曠症在神經生物學上有重疊，因此模型給出高分是合理的。

需要注意：目前檢索到的臨床試驗大多是強迫症研究（即原適應症），並未直接測試 Clomipramine 對非強迫症焦慮症的效果。較直接的支持來自文獻，尤其是恐慌症與懼曠症的較早期研究。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00466609](https://clinicaltrials.gov/study/NCT00466609) | Phase 4 | 完成 | 54 | 對一線藥物無反應的強迫症患者，比較 fluoxetine 加 quetiapine 或加 clomipramine 的增效策略（強迫症，非焦慮症） |
| [NCT00074815](https://clinicaltrials.gov/study/NCT00074815) | Phase 3 | 完成 | 124 | 兒童強迫症，SRI 部分反應者加上認知行為治療 |
| [NCT00254735](https://clinicaltrials.gov/study/NCT00254735) | Phase 3 | 完成 | 44 | Quetiapine 增效於重度強迫症（baseline 為 SSRI/clomipramine） |
| [NCT00564564](https://clinicaltrials.gov/study/NCT00564564) | Phase 4 | 完成 | 21 | SSRI 治療失敗的強迫症，比較 quetiapine 與 clomipramine 增效 |
| [NCT00004310](https://clinicaltrials.gov/study/NCT00004310) | Phase 2 | 未知 | 76 | 靜脈與口服 clomipramine 用於強迫症的隨機比較 |
| [NCT01404871](https://clinicaltrials.gov/study/NCT01404871) | N/A | 完成 | 26 | 預測強迫症患者對 clomipramine 或 escitalopram 的反應 |
| [NCT02374567](https://clinicaltrials.gov/study/NCT02374567) | Phase 3 | 終止 | 407 | 老年精神科患者精神藥物安全性與藥物不良反應監測 |
| [NCT05737511](https://clinicaltrials.gov/study/NCT05737511) | Phase 4 | 尚未招募 | 80 | Hydroxyzine 對比常規治療用於恐慌症的開放性前導研究 |

> 以上試驗皆被評為低相關（C 級），沒有任何一項直接檢驗 Clomipramine 對焦慮症的療效。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38014714](https://pubmed.ncbi.nlm.nih.gov/38014714/) | 2023 | 網絡統合分析 | Cochrane Database Syst Rev | 成人恐慌症的藥物治療比較 |
| [40788541](https://pubmed.ncbi.nlm.nih.gov/40788541/) | 2026 | 系統性回顧/統合分析 | Eur Arch Psychiatry Clin Neurosci | 抗焦慮藥物對焦慮症的療效與可接受性比較 |
| [40946318](https://pubmed.ncbi.nlm.nih.gov/40946318/) | 2026 | 系統性回顧 | Psychother Psychosom | 難治性焦慮症的藥物、心理與神經刺激治療 |
| [35900217](https://pubmed.ncbi.nlm.nih.gov/35900217/) | 2023 | 指引 | World J Biol Psychiatry | WFSBP 焦慮、強迫症與創傷後壓力症藥物治療指引 |
| [2178909](https://pubmed.ncbi.nlm.nih.gov/2178909/) | 1990 | 回顧 | Drugs | Clomipramine 藥理特性及其在強迫症與恐慌症的治療用途 |
| [6373161](https://pubmed.ncbi.nlm.nih.gov/6373161/) | 1984 | 雙盲比較試驗 | Curr Med Res Opin | 基層醫療中 clomipramine 與 diazepam 用於懼曠症與社交畏懼症 |
| [2651491](https://pubmed.ncbi.nlm.nih.gov/2651491/) | 1989 | 開放性臨床研究 | J Clin Psychopharmacol | 17 位恐慌症／懼曠症患者低劑量 clomipramine，13 位恐慌發作完全停止 |
| [9585709](https://pubmed.ncbi.nlm.nih.gov/9585709/) | 1998 | 對照試驗 | Am J Psychiatry | 有氧運動、clomipramine 與安慰劑用於恐慌症的比較 |
| [11277602](https://pubmed.ncbi.nlm.nih.gov/11277602/) | 2001 | 臨床研究 | J Psychopharmacol | 恐慌症 clomipramine 劑量探索與停藥研究，70.3% 達到完全緩解 |
| [10665629](https://pubmed.ncbi.nlm.nih.gov/10665629/) | 1999 | 安慰劑對照試驗 | J Clin Psychiatry | Paroxetine、clomipramine 與認知治療用於恐慌症的比較 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-45562 | ANAFRANIL TAB 25MG S/C | 未提供 | 未提供 |
| HK-40592 | APO-CLOMIPRAMINE TAB 10MG | 未提供 | 未提供 |
| HK-45537 | ANAFRANIL TAB 10MG S/C | 未提供 | 未提供 |
| HK-41079 | APO-CLOMIPRAMINE TAB 25MG | 未提供 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜關聯，非仿單原文）：癲癇、躁型雙極性情感障礙、肝病、膽囊疾病、物質濫用/依賴、惡性高熱、嗜鉻細胞瘤、青光眼、甲狀腺機能亢進（含 Graves 病）、神經母細胞瘤，以及部分癌症類型。
- **藥物交互作用**：資料庫共記錄 100 筆，以下為部分主要交互作用：
  - 嚴重 (Major)：Epinephrine、Bupropion、Lorcaserin、Potassium citrate、Cisapride
  - 中度 (Moderate)：Famotidine、Cimetidine、Clarithromycin、Morphine、Acetylsalicylic acid、Atropine 等
- **文獻提及的安全訊號**：有 clomipramine 導致全血球減少的個案報告；三環類藥物常見抗膽鹼作用、性功能障礙，以及癲癇與心臟方面的風險。

詳細警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 對恐慌症／懼曠症已有多項較早期的臨床研究與回顧支持 Clomipramine 的抗恐慌效果，機轉合理，且該藥已在香港上市。但這些研究多為小型、年代較早的研究，登記的臨床試驗也沒有直接針對焦慮症，因此建議在限定範圍內謹慎推進，而不是直接擴大適應症。

**若要推進需要：**
- 先界定具體的焦慮症亞型（建議從恐慌症／懼曠症開始），因為「焦慮症」一詞過於廣泛。
- 取得香港原廠仿單的警語與禁忌資料（目前缺乏，為阻擋性資料缺口），並補齊作用機轉資料。
- 與 SSRI 等現行第一線藥物做效益與安全性的比較評估，因 Clomipramine 的耐受性與安全性較差。
- 針對上述高風險族群與嚴重藥物交互作用，建立篩選與監測計畫。
- 若要支持標示外使用或擴增適應症，需設計針對焦慮症亞型的對照試驗。

**其他預測適應症的簡要備註：**
- 重鬱症（證據 L3）與內因性憂鬱症（L3）：Clomipramine 本身即為抗憂鬱劑，更屬定位或標示問題，而非全新再利用。
- 過動症（ADHD，L4，Hold）：僅有三環類藥物整體的證據，缺乏 Clomipramine 專屬資料，且安全性限制其吸引力。
- 其餘預測（陣發性斜頸、偏執／類精神分裂／分裂型／做作型人格障礙）：僅有模型預測或不相關文獻，無實質支持，建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

