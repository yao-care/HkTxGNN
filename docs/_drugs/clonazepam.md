---
layout: default
title: Clonazepam
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Clonazepam：預測新適應症為不寧腿症候群 (Restless Legs Syndrome)（證據等級 L5）。原適應症：早期肌陣攣腦病變、失神癲癇、Lennox-Gastaut 症候群、焦慮症等"
monitor_inn: "CLONAZEPAM"
predicted_indications: ["restless legs syndrome", "trigeminal nerve neoplasm"]
---

# Clonazepam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Clonazepam：從癲癇與焦慮症到不寧腿症候群

## 一句話總結

Clonazepam 是一種苯二氮平類（benzodiazepine）藥物，原本用於早期肌陣攣腦病變、失神癲癇、Lennox-Gastaut 症候群及焦慮症等。
TxGNN 模型預測它可能對**不寧腿症候群 (Restless Legs Syndrome, RLS)** 有效，
目前**無已登記的臨床試驗**，但有 **20 篇文獻**支持這個方向，包含 1 篇 Cochrane 系統性回顧與 1 份 AASM 臨床指引。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 早期肌陣攣腦病變、失神癲癇、Lennox-Gastaut 症候群、焦慮症等（香港許可證未載明適應症文字，此處依知識圖譜資料） |
| 預測新適應症 | 不寧腿症候群 (Restless Legs Syndrome) |
| TxGNN 預測分數 | 99.65% |
| 證據等級 | L3（有系統性回顧與觀察性資料，無已完成的 Phase 3 RCT） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據藥物類別，Clonazepam 屬於苯二氮平類，為 GABA-A 受體的正向異位調節劑。其鎮靜與抗肌陣攣作用，可能減少不寧腿症候群患者的睡眠中斷與週期性肢體運動。

原適應症（癲癇、肌陣攣、焦慮）與 RLS 都涉及神經系統的過度興奮或運動異常，這是兩者的關聯所在。不過這個機轉連結來自藥物類別的一般性知識，並非針對 RLS 的專一機轉。

需要留意的是，現行指引並不把苯二氮平類列為首選，而是優先考慮 alpha-2-delta 配體及必要時補鐵。Clonazepam 較適合視為歷史上使用的第二線或輔助選項，主要用於失眠症狀明顯的患者。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39324694](https://pubmed.ncbi.nlm.nih.gov/39324694/) | 2025 | 臨床指引 | J Clin Sleep Med | AASM 針對成人與兒童 RLS 及週期性肢體運動障礙的治療建議 |
| [28319266](https://pubmed.ncbi.nlm.nih.gov/28319266/) | 2017 | 系統性回顧 (Cochrane) | Cochrane Database Syst Rev | 評估苯二氮平類（尤其 clonazepam）用於 RLS 的證據 |
| [6380197](https://pubmed.ncbi.nlm.nih.gov/6380197/) | 1984 | 隨機雙盲交叉試驗 | Acta Neurol Scand | 6 位 RLS 患者中，clonazepam 優於安慰劑，改善睡眠品質與腿部不適；長期療效待確認 |
| [11313161](https://pubmed.ncbi.nlm.nih.gov/11313161/) | 2001 | 安慰劑對照睡眠實驗室研究 | Eur Neuropsychopharmacol | 評估 1 mg clonazepam 對 RLS／週期性肢體運動障礙患者睡眠與清醒品質的急性效果 |
| [38708125](https://pubmed.ncbi.nlm.nih.gov/38708125/) | 2024 | Review | Tremor Other Hyperkinet Mov | 歷史回顧：約 25% 的 RLS 治療者使用苯二氮平類；整理 17 篇 clonazepam 用於 RLS 的文獻 |
| [18925578](https://pubmed.ncbi.nlm.nih.gov/18925578/) | 2008 | Review | Mov Disord | MDS 任務小組的 RLS 治療實證回顧 |
| [36692194](https://pubmed.ncbi.nlm.nih.gov/36692194/) | 2023 | 系統性回顧與統合分析 | J Clin Sleep Med | 探討各類藥物對 RLS 患者週期性肢體運動的抑制效果 |
| [20156514](https://pubmed.ncbi.nlm.nih.gov/20156514/) | 2010 | 臨床研究 | Prog Neuropsychopharmacol Biol Psychiatry | 提出 clonazepam 與 pramipexole 在 RLS 的等效劑量 |
| [35426627](https://pubmed.ncbi.nlm.nih.gov/35426627/) | 2022 | Review | Am Fam Physician | 成人常見睡眠障礙的診斷與處置 |
| [17876423](https://pubmed.ncbi.nlm.nih.gov/17876423/) | 2007 | 專家共識 | Arq Neuropsiquiatr | 巴西專家對 RLS 診斷與治療的共識意見 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-58637 | CLONOTRIL 2 TAB 2MG | 未載明 | 未載明 |
| HK-58638 | CLONOTRIL 0.5 TAB 0.5MG | 未載明 | 未載明 |
| HK-64321 | PMS-CLONAZEPAM-R TABLETS 0.5MG | 未載明 | 未載明 |
| HK-57404 | RIVOTRIL TAB 0.5MG | 未載明 | 未載明 |
| HK-57397 | RIVOTRIL TAB 2MG | 未載明 | 未載明 |

---

## 安全性考量

- **知識圖譜中的禁忌疾病**（來自知識圖譜關聯，並非仿單原文）：肝衰竭、肝病、腎病、膽囊疾病、紫質症、開角型與閉角型青光眼、阻塞性睡眠呼吸中止症、先天性中樞低通氣症候群、呼吸衰竭、物質濫用／依賴等。
- **藥物交互作用**：共查得 100 筆，以下為主要項目：
  - **重大 (Major)**：Morphine、Morphine (liposomal)（與鴉片類併用有中樞與呼吸抑制風險）
  - **中度 (Moderate)**：Bupropion、Aprepitant、Omeprazole、Cimetidine、Clarithromycin、Dronabinol、Metoclopramide、Nabilone、Opium、Sibutramine、Teduglutide
  - **輕微 (Minor)**：Magnesium oxide、Aluminum hydroxide、Calcium carbonate 等制酸劑
- **其他注意**：Clonazepam 半衰期長，需留意次日鎮靜、跌倒、耐受性、依賴與認知功能受損，老年人及神經退化性疾病患者尤其需謹慎。

仿單的警語與禁忌症原文請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有 Cochrane 系統性回顧、AASM 指引，以及小型安慰劑對照研究支持 clonazepam 用於 RLS，且 Clonazepam 已在香港上市，可行性高。
- 但現行指引不將其列為首選，且缺乏大型近期 RCT，並有依賴與鎮靜等風險，因此只適合作為第二線或輔助選項，並設置使用上的防護條件。

**若要推進需要：**
- 取得香港衛生署核准的仿單內容（警語、禁忌症、核准適應症），目前這些資料缺漏
- 補齊詳細的作用機轉資料
- 設計並登記針對 RLS 的現代對照試驗，與 alpha-2-delta 配體等現行首選藥物比較
- 制定使用條件：限定於失眠症狀明顯者、低劑量、短期使用，並監測鎮靜、跌倒與依賴風險
- 排除或審慎評估有睡眠呼吸中止、呼吸功能不全、肝腎疾病及物質濫用史的患者

---

## 其他預測適應症（供參考）

| 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|-----------|-----------|---------|------|
| 失眠 (Insomnia) | 99.32% | L4 | Research Question：現有文獻多為間接證據（如帕金森氏症睡眠障礙回顧），無針對失眠的 clonazepam RCT；另有 1 例 clonazepam 相關躁狂的病例報告，需先進行安全性評估 |
| 三叉神經腫瘤 (Trigeminal Nerve Neoplasm) | 99.30% | L5 | Hold：無臨床試驗與文獻，僅有模型預測，也無合理的抗腫瘤機轉，需先做機轉驗證 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

