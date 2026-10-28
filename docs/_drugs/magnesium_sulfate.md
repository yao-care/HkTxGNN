---
layout: default
title: Magnesium Sulfate
parent: 僅模型預測 (L5)
nav_order: 550
evidence_level: L5
indication_count: 9
monitor_inn: "MAGNESIUM SULFATE"
predicted_indications: ["toxemia of pregnancy", "thrombotic disease", "pharyngitis", "nasal cavity disease", "psychotic disorder", "acute laryngopharyngitis", "headache disorder", "trigeminal autonomic cephalalgia", "treatment-refractory schizophrenia"]
last_modified_at: 2026-10-28
description: "Magnesium Sulfate：預測新適應症為妊娠毒血症 (Toxemia of Pregnancy)（證據等級 L1）。原適應症：知識圖譜記錄：便秘、輕度/重度子癇前症"
---

# Magnesium Sulfate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## 硫酸鎂 (Magnesium Sulfate)：從便秘與子癇前症到妊娠毒血症
{: .text-alpha }

## 一句話總結

硫酸鎂在知識圖譜中記錄的原有用途為便秘與子癇前症（輕度與重度）。
TxGNN 模型（深度學習）預測它對**妊娠毒血症 (Toxemia of Pregnancy)** 的分數最高（1.0000）；此分數可能反映模型學到的相關疾病之間的相似性，而非生物學證據。
目前有 **28 個臨床試驗**和 **19 篇文獻**與此預測疾病相關。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄：便秘、輕度/重度子癇前症（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 妊娠毒血症 (Toxemia of Pregnancy) |
| TxGNN 預測分數 | 1.0000 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 11 張／共 11 張） |
| 許可證數 | 11 張（有效 11 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（DrugBank 未提供）。就文獻與既有研究所知，鎂離子被認為是 NMDA 受體拮抗劑與鈣離子通道阻斷劑，並可引起腦血管擴張，因而能降低癲癇發作風險與腦血管痙攣。

妊娠毒血症與子癇前症、子癇屬同一疾病譜系。硫酸鎂預防子癇發作是產科的標準做法，所以模型給出高分與既有知識相符。需要說明的是，這個預測並非真正的「再利用」，而是與知識圖譜已記錄關聯一致的結果。

其他預測疾病中，頭痛疾患（Phase 3 偏頭痛試驗）與術後咽喉痛有一定研究，其餘多為證據薄弱的預測，詳見結論。

## 臨床試驗證據

以下為與子癇前症直接相關且最相關的試驗（共 28 筆，列出 10 筆）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02317146](https://clinicaltrials.gov/study/NCT02317146) | Phase 2/3 | 完成 | 280 | 重度子癇前症產後硫酸鎂 6 小時與 24 小時方案比較 |
| [NCT02307201](https://clinicaltrials.gov/study/NCT02307201) | Phase 2/3 | 完成 | 1114 | 產前已用藥逾 8 小時者，產後 24 小時與不續用比較 |
| [NCT03164304](https://clinicaltrials.gov/study/NCT03164304) | Phase 4 | 完成 | 222 | 重度子癇前症維持劑量 1 g 與 2 g 比較 |
| [NCT00004399](https://clinicaltrials.gov/study/NCT00004399) | 未標示 | 完成 | 2000 | Nimodipine 與硫酸鎂預防子癇發作比較 |
| [NCT04501289](https://clinicaltrials.gov/study/NCT04501289) | 未標示 | 完成 | 114 | 低劑量方案與標準 Pritchard 方案比較 |
| [NCT01408979](https://clinicaltrials.gov/study/NCT01408979) | Phase 4 | 完成 | 120 | 重度子癇前症產後短療程預防 |
| [NCT03318211](https://clinicaltrials.gov/study/NCT03318211) | Phase 4 | 未知 | 100 | 產後續用與停用硫酸鎂比較 |
| [NCT02396030](https://clinicaltrials.gov/study/NCT02396030) | Phase 4 | 提前終止 | 62 | 維持劑量 1 g/h 與 2 g/h 預防子癇 |
| [NCT06486025](https://clinicaltrials.gov/study/NCT06486025) | Phase 1/2 | 未知 | 100 | 過重及肥胖女性的替代劑量方案 |
| [NCT07220902](https://clinicaltrials.gov/study/NCT07220902) | Phase 3 | 尚未招募 | 1240 | Levetiracetam 與硫酸鎂預防子癇發作的等效性試驗 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32980358](https://pubmed.ncbi.nlm.nih.gov/32980358/) | 2022 | Review | Am J Obstet Gynecol | 21 世紀子癇的發生率與處置 |
| [38669914](https://pubmed.ncbi.nlm.nih.gov/38669914/) | 2024 | Review | Pregnancy Hypertens | 硫酸鎂於子癇前症的廣泛適應，不限於神經症狀 |
| [36822712](https://pubmed.ncbi.nlm.nih.gov/36822712/) | 2023 | Review | Obstet Gynecol Clin North Am | 高收入與中低收入國家的用藥方案 |
| [10803454](https://pubmed.ncbi.nlm.nih.gov/10803454/) | 2000 | Review | Clin Pharmacokinet | 子癇及子癇前症的藥動學原則 |
| [8879973](https://pubmed.ncbi.nlm.nih.gov/8879973/) | 1996 | Review | Drug Saf | 硫酸鎂預防子癇發作優於 diazepam 與 phenytoin |
| [38872116](https://pubmed.ncbi.nlm.nih.gov/38872116/) | 2024 | 藥動學研究 | BMC Pregnancy Childbirth | 中國子癇前症族群的群體藥動學與劑量最佳化 |
| [32642964](https://pubmed.ncbi.nlm.nih.gov/32642964/) | 2020 | 藥動學研究 | Drugs R D | 子癇前症群體藥動學及相關因素 |
| [37467840](https://pubmed.ncbi.nlm.nih.gov/37467840/) | 2023 | Review | Am J Obstet Gynecol | 產後晚期重度高血壓是否皆需硫酸鎂 |
| [38574215](https://pubmed.ncbi.nlm.nih.gov/38574215/) | 2024 | Review | Am Fam Physician | 妊娠高血壓疾患概述 |
| [19464502](https://pubmed.ncbi.nlm.nih.gov/19464502/) | 2009 | Review | Semin Perinatol | 子癇前症與子癇的全球影響 |

## 香港上市資訊

香港共有 11 張含硫酸鎂成分的單一成分許可證，皆為有效。資料中未載明核准適應症文字，以下列出 5 張。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-32142 | MAGNESIUM SULPHATE CONCENTRATED INJ 49.3% | 未載明 | 未載明 |
| HK-47730 | CHESTOK ENEMA | 未載明 | 未載明 |
| HK-47731 | PERSTON ENEMA | 未載明 | 未載明 |
| HK-52179 | QUICK MICROENEMA ENEMA | 未載明 | 未載明 |
| HK-47729 | HARRICO ENEMA | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單文字）：腎臟疾病、高鈣血症、腎鈣質沉著症、磷代謝疾病、慢性腹瀉、闌尾炎、房室傳導阻滯、高血鉀週期性麻痺、週期性麻痺、低醛固酮症、先天性肌強直、胃輕癱等。
- **藥物交互作用**：共 92 筆。主要（Major）包括 Dolutegravir、Amikacin、Bictegravir；中度（Moderate）包括 Nifedipine、Amlodipine、Doxycycline、Tetracycline、Ciprofloxacin、Cisatracurium、數種雙磷酸鹽類與皮質類固醇、維生素 D 類。
- **用藥監測**：血清鎂濃度、深部肌腱反射、呼吸速率、尿量；腎功能不全及肥胖者需調整劑量。

仿單警語與正式禁忌請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 針對妊娠毒血症，有多個已完成的 Phase 2/3 及 Phase 4 隨機試驗，涵蓋劑量與療程，證據等級 L1。
- 其他預測疾病中，頭痛疾患有 1 個已完成的 Phase 3 試驗但結果未提供（建議研究問題）；術後咽喉痛有多項隨機試驗與統合分析，但與感染性咽炎不同；血栓性疾病、精神病性疾患的證據薄弱，鼻腔疾病、急性喉咽炎、難治型思覺失調症僅有模型預測（L5），均建議暫緩（Hold）。

**若要推進需要：**
- 取得香港仿單的適應症、警語與禁忌資料，並補齊作用機轉資料
- 建立血清鎂、反射、呼吸、尿量的監測計畫，並訂定腎功能不全與肥胖者的劑量調整準則
- 評估 Dolutegravir、Amikacin、Bictegravir 等主要交互作用的處置
- 若評估頭痛疾患，需先確認 NCT05967442 的試驗結果
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

