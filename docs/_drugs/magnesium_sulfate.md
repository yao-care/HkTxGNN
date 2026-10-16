---
layout: default
title: Magnesium Sulfate
parent: 高證據等級 (L1-L2)
nav_order: 550
evidence_level: L1
indication_count: 5
last_modified_at: 2026-10-14
description: "Magnesium Sulfate：預測新適應症為子癇前症/子癇 (preeclampsia/eclampsia)（證據等級 L1）。原適應症：便秘、子癇前症"
monitor_inn: "MAGNESIUM SULFATE"
predicted_indications: ["preeclampsia/eclampsia", "toxemia of pregnancy", "thrombotic disease", "pharyngitis", "nasal cavity disease"]
---

# Magnesium Sulfate
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

# Magnesium Sulfate：從便秘與子癇前症到子癇前症/子癇

## 一句話總結

硫酸鎂 (Magnesium Sulfate) 原本用於便秘及子癇前症（輕度與重度）的治療。
TxGNN 模型預測它對 **子癇前症/子癇 (preeclampsia/eclampsia)** 有效，目前有 **29 個臨床試驗**和 **19 篇文獻**支持這個方向。需要說明的是，這其實是已確立的標準治療，並非真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 便秘、子癇前症（香港許可證未提供核准適應症文字，此處依知識圖譜原適應症列出） |
| 預測新適應症 | 子癇前症/子癇 (preeclampsia/eclampsia) |
| TxGNN 預測分數 | 99.999% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 11 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供 MOA）。根據已知資訊，硫酸鎂是 NMDA 受體拮抗劑與鈣離子通道阻斷劑，並能促進腦血管擴張。這些作用可降低子癇的癲癇發作風險，並緩解腦血管痙攣。

子癇前症本身就是硫酸鎂的原適應症之一，因此這個預測較接近「已確立的標準治療」，而不是新的藥物再利用。TxGNN 給出極高分數，與臨床現況一致。

另外，「toxemia of pregnancy（妊娠毒血症）」是子癇前症/子癇的舊稱，兩筆預測實質上重複，共用同一批證據，報告中不應重複計算。

---

## 臨床試驗證據

以下列出與子癇前症最相關的 10 個試驗（共 29 個登記試驗）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | 完成 | 280 | 重度子癇前症產前用藥不足 8 小時者，產後 6 小時 vs 24 小時的硫酸鎂方案 |
| [NCT03164304](https://clinicaltrials.gov/study/NCT03164304) | Phase 4 | 完成 | 222 | 重度子癇前症靜脈維持劑量 1 g vs 2 g 的療效與安全性 |
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | N/A | 完成 | 2000 | Nimodipine 與硫酸鎂預防重度子癇前症抽搐的比較 |
| [NCT04501289](https://clinicaltrials.gov/study/NCT04501289) | N/A | 完成 | 114 | 低劑量方案 vs 標準 Pritchard 方案 |
| [NCT06486025](https://clinicaltrials.gov/study/NCT06486025) | Phase 1/2 | 未知 | 100 | 過重及肥胖孕婦的替代劑量方案 |
| [NCT03318211](https://clinicaltrials.gov/study/NCT03318211) | Phase 4 | 未知 | 100 | 產後繼續 vs 停用硫酸鎂 |
| [NCT02396030](https://clinicaltrials.gov/study/NCT02396030) | Phase 4 | 提前終止 | 62 | 維持劑量 1 g/h vs 2 g/h 預防子癇（檢定力有限） |
| [NCT02307201](https://clinicaltrials.gov/study/NCT02307201) | Phase 2/3 | 完成 | 1114 | 產前已用藥超過 8 小時者，產後 24 小時 vs 不繼續給藥 |
| [NCT07220902](https://clinicaltrials.gov/study/NCT07220902) | Phase 3 | 尚未招募 | 1240 | Levetiracetam 與硫酸鎂預防子癇發作的等效性試驗 |
| [NCT03412552](https://clinicaltrials.gov/study/NCT03412552) | N/A | 完成 | 1238 | 重度子癇前症/子癇加護照護的觀察性研究（間接證據） |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32980358](https://pubmed.ncbi.nlm.nih.gov/32980358/) | 2022 | Review | Am J Obstet Gynecol | 21 世紀子癇的發生率與預後，已開發與開發中國家差距大 |
| [38669914](https://pubmed.ncbi.nlm.nih.gov/38669914/) | 2024 | Review | Pregnancy Hypertens | 硫酸鎂在子癇前症的適應症不限於神經症狀 |
| [36822712](https://pubmed.ncbi.nlm.nih.gov/36822712/) | 2023 | Review | Obstet Gynecol Clin North Am | 高收入與中低收入國家的硫酸鎂方案比較 |
| [10803454](https://pubmed.ncbi.nlm.nih.gov/10803454/) | 2000 | Review | Clin Pharmacokinet | 硫酸鎂治療子癇的藥物動力學原理 |
| [9794688](https://pubmed.ncbi.nlm.nih.gov/9794688/) | 1998 | Review | Obstet Gynecol | 硫酸鎂預防癲癇的療效、效益與風險 |
| [2288560](https://pubmed.ncbi.nlm.nih.gov/2288560/) | 1990 | Review | Am J Obstet Gynecol | 硫酸鎂是子癇前症/子癇的理想抗痙攣藥物 |
| [38574215](https://pubmed.ncbi.nlm.nih.gov/38574215/) | 2024 | Review | Am Fam Physician | 妊娠高血壓疾病的處置 |
| [8879973](https://pubmed.ncbi.nlm.nih.gov/8879973/) | 1996 | 文獻回顧 | Drug Saf | 硫酸鎂預防復發性癲癇優於 diazepam 與 phenytoin |
| [38872116](https://pubmed.ncbi.nlm.nih.gov/38872116/) | 2024 | 族群藥動學 | BMC Pregnancy Childbirth | 中國子癇前症族群的劑量優化 |
| [1566765](https://pubmed.ncbi.nlm.nih.gov/1566765/) | 1992 | 前臨床 | Am J Obstet Gynecol | 硫酸鎂對海馬迴癲癇的中樞抗痙攣作用 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-32142 | MAGNESIUM SULPHATE CONCENTRATED INJ 49.3% | 未提供 | 未提供 |
| HK-47730 | CHESTOK ENEMA | 未提供 | 未提供 |
| HK-47731 | PERSTON ENEMA | 未提供 | 未提供 |
| HK-52179 | QUICK MICROENEMA ENEMA | 未提供 | 未提供 |
| HK-47729 | HARRICO ENEMA | 未提供 | 未提供 |

共 11 張有效許可證，皆為單方製劑。其餘包括 FANITON、MAIBIO 灌腸劑，以及 SMOFKABIVEN 系列和 AMINOLEBAN EN 等營養輸液/粉劑。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：腎臟疾病、高鈣血症、腎鈣化症、磷代謝疾病、慢性腹瀉、闌尾炎、房室傳導阻滯、高血鉀週期性麻痺、週期性麻痺、低醛固酮症、先天性肌強直、胃輕癱、輸尿管積膿（此為知識圖譜關聯，並非仿單文字）。
- **藥物交互作用**：共 92 筆，主要包括：
  - 嚴重 (Major)：Dolutegravir、Amikacin、Bictegravir
  - 中度 (Moderate)：Nifedipine、Amlodipine、Cisatracurium、Doxycycline、Tetracycline、Ciprofloxacin、Alendronic acid、Risedronic acid、Ibandronate、類固醇（Dexamethasone、Hydrocortisone 等）、維生素 D 類

臨床使用時應監測血清鎂濃度（反射、呼吸速率、尿量），腎功能不全者需調整劑量，肥胖及產後患者亦需劑量調整。其他警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 硫酸鎂用於子癇前症/子癇已有大量臨床試驗與文獻支持，屬於已確立的標準治療；但這並非新的再利用適應症，且香港許可證缺乏核准適應症文字。

**其他預測適應症：**
- 血栓性疾病（L3，僅有動物資料、小型先導研究及一項 TTP 的 Phase 3 試驗，結果未公布）：列為研究問題。
- 咽炎（L2）：證據針對術後插管相關喉嚨痛，並非感染性咽炎，不宜直接推論；列為研究問題。
- 鼻腔疾病（L5）：僅有模型預測，無任何試驗或文獻，建議 Hold。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症
- 補充詳細作用機轉（MOA）資料
- 建立血清鎂監測與腎功能、肥胖、產後劑量調整的用藥規範
- 對術後喉嚨痛等其他適應症，需另行設計試驗
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

