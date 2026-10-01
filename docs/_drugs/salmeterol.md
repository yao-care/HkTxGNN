---
layout: default
title: Salmeterol
parent: 高證據等級 (L1-L2)
nav_order: 785
evidence_level: L1
indication_count: 5
---

# Salmeterol
{: .fs-9 }

證據等級: **L1** | 預測適應症: **5** 個
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

# Salmeterol：從氣喘／慢性阻塞性肺病維持治療到支氣管炎

## 一句話總結

Salmeterol 是長效 β2 腎上腺素受體促效劑（LABA），常用於氣喘與慢性阻塞性肺病（COPD）的維持治療。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，
目前有 **15 個臨床試驗**和 **20 篇文獻**支持這個方向。
這個預測很可能屬於既有用途的延伸（慢性支氣管炎是 COPD 的一種表現型），不是全新的藥物再利用發現。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 15 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 DrugBank 的詳細作用機轉資料。根據已知資訊，Salmeterol 是 LABA 類藥物。它刺激 β2 受體後，可放鬆氣道平滑肌，也可能提高纖毛擺動頻率，有助於黏液纖毛清除。

慢性支氣管炎是 COPD 的常見表現型（慢性咳嗽、咳痰、氣流受阻），而 Salmeterol 本來就用於 COPD 的維持治療。因此從機轉與臨床用途來看，這個預測相當合理。

使用上通常要與吸入型類固醇（ICS）或長效抗膽鹼藥（LAMA）併用，並遵守仿單的安全性警語。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00268177](https://clinicaltrials.gov/study/NCT00268177) | Phase 3 | 完成 | 130 | 13 週雙盲試驗，比較 Salmeterol/Fluticasone 與安慰劑對 COPD 患者支氣管抗發炎活性的影響 |
| [NCT02173691](https://clinicaltrials.gov/study/NCT02173691) | Phase 3 | 完成 | 584 | 6 個月雙盲試驗，比較 Tiotropium、Salmeterol 與安慰劑在 COPD 的支氣管擴張療效與安全性 |
| [NCT00064402](https://clinicaltrials.gov/study/NCT00064402) | Phase 3 | 完成 | 741 | 安慰劑與活性藥對照試驗，評估 Arformoterol 12 週維持治療 COPD 的效果（Salmeterol 可能為對照，屬間接證據） |
| [NCT00064415](https://clinicaltrials.gov/study/NCT00064415) | Phase 3 | 完成 | 799 | 開放標示的 12 個月長期安全性研究，Arformoterol 用於 COPD（Salmeterol 可能為對照） |
| [NCT00269087](https://clinicaltrials.gov/study/NCT00269087) | Phase 3 | 完成 | 122 | GW815SF（Salmeterol/Fluticasone 50/500µg）用於 COPD（慢性支氣管炎、肺氣腫）的 56 週長期安全性研究 |
| [NCT01110200](https://clinicaltrials.gov/study/NCT01110200) | Phase 4 | 完成 | 639 | 比較 Fluticasone/Salmeterol 與單用 Salmeterol，對 COPD 住院後急性惡化率的影響 |
| [NCT00857766](https://clinicaltrials.gov/study/NCT00857766) | Phase 4 | 完成 | 249 | 16 週雙盲試驗，評估 Fluticasone/Salmeterol 對 COPD 患者動脈硬化程度的影響 |
| [NCT00633217](https://clinicaltrials.gov/study/NCT00633217) | Phase 4 | 完成 | 247 | 12 週試驗，比較 Fluticasone/Salmeterol 的 HFA 定量噴霧劑與 DISKUS 乾粉吸入劑在 COPD 的療效與安全性 |
| [NCT00403286](https://clinicaltrials.gov/study/NCT00403286) | Phase 2 | 完成 | 457 | 劑量探索試驗，以 Advair Diskus（Fluticasone/Salmeterol）為參考，評估 Fluticasone/Formoterol 在 COPD 的肺功能與安全性 |
| [NCT01332409](https://clinicaltrials.gov/study/NCT01332409) | N/A | 完成 | 2000 | 日本上市後特別調查，評估 Salmeterol/Fluticasone 在 COPD（慢性支氣管炎／肺氣腫）的安全性與療效，以肺炎發生為優先項目 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [19124357](https://pubmed.ncbi.nlm.nih.gov/19124357/) | 2008 | RCT | Ther Adv Respir Dis | 以 12 個月比較 Arformoterol 與 Salmeterol 在 COPD 的安全性與耐受性，並檢視是否出現耐受現象 |
| [12970006](https://pubmed.ncbi.nlm.nih.gov/12970006/) | 2003 | RCT | Chest | 比較同一吸入器中 Fluticasone 250µg/Salmeterol 50µg 與安慰劑及單一成分在 COPD 的療效與安全性 |
| [9916607](https://pubmed.ncbi.nlm.nih.gov/9916607/) | 1998 | RCT（開放標示） | Clin Ther | 比較吸入 Salmeterol 與口服 Theophylline 在輕中度 COPD 的療效、耐受性與生活品質 |
| [15970448](https://pubmed.ncbi.nlm.nih.gov/15970448/) | 2006 | 臨床研究 | Pulm Pharmacol Ther | 在 14 位輕中度慢性支氣管炎患者中，評估 Salmeterol 對黏液纖毛清除與咳嗽清除的急性影響（摘要未提供結果數據） |
| [19210134](https://pubmed.ncbi.nlm.nih.gov/19210134/) | 2009 | 世代研究 | Curr Med Res Opin | 比較慢性支氣管炎患者起始 Fluticasone/Salmeterol 與其他吸入維持治療的住院、急診與醫療費用 |
| [17196106](https://pubmed.ncbi.nlm.nih.gov/17196106/) | 2006 | 統合分析 | Respir Res | 彙整分析 COPD 患者在常規治療上加用 Salmeterol 50mcg 每日兩次，對比安慰劑的臨床結果改善 |
| [15329047](https://pubmed.ncbi.nlm.nih.gov/15329047/) | 2004 | Review | Drugs | 回顧 Salmeterol/Fluticasone 乾粉吸入劑用於 COPD 的證據 |
| [16915216](https://pubmed.ncbi.nlm.nih.gov/16915216/) | 2006 | 病人經驗試驗 | MedGenMed | 以 Advair Diskus 250/50 治療 COPD（伴隨慢性支氣管炎）的病人經驗研究 |
| [10832348](https://pubmed.ncbi.nlm.nih.gov/10832348/) | 2000 | 專家評論 | MMW Fortschr Med | 針對吸菸引起的慢性支氣管炎與肺氣腫，建議運用完整的藥物治療選項 |

---

## 香港上市資訊

目前共有 15 張許可證，以下列出 5 張主要許可證。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-35936 | SEREVENT INHALER 25MCG/ACTUATION | GLAXOSMITHKLINE LIMITED |
| HK-51376 | SEROFLO 125 INHALER | CONTROLLED MEDICATIONS LIMITED |
| HK-51378 | SEROFLO 50 INHALER | CONTROLLED MEDICATIONS LIMITED |
| HK-48128 | SERETIDE INHALER 25/50 | GLAXOSMITHKLINE LIMITED |
| HK-65890 | SIRDUPLA PRESSURISED INHALATION SUSPENSION 25MCG/250MCG PER METERED DOSE | VIATRIS HEALTHCARE HONG KONG LIMITED |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有多個已完成的 Phase 3 試驗和多篇 RCT，證據等級達 L1，且臨床用途集中在 COPD（含慢性支氣管炎）。
- 這比較像既有用途的延伸，而非全新適應症。目前缺少香港仿單的警語與禁忌資料，所以只建議在管控條件下推進。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊警語與禁忌症（目前列為阻礙項目）。
- 確認香港核准適應症的實際文字，判斷「支氣管炎」是否已涵蓋在既有適應症內。
- 補充 DrugBank 的作用機轉資料。
- 釐清所指的是慢性支氣管炎還是急性支氣管炎。現有證據主要針對 COPD／慢性支氣管炎。
- 遵守併用原則：LABA 應與 ICS 或 LAMA 併用，並依仿單與指引監測安全性。

*本報告僅供研究參考，不構成醫療建議；預測結果需經臨床驗證。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

