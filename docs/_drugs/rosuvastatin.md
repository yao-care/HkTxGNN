---
layout: default
title: Rosuvastatin
parent: 僅模型預測 (L5)
nav_order: 788
evidence_level: L5
indication_count: 6
monitor_inn: "ROSUVASTATIN"
predicted_indications: ["cholesterol-ester transfer protein deficiency", "brain stem infarction", "HIV infectious disease", "hypoalphalipoproteinemia", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "ABri amyloidosis"]
last_modified_at: 2026-10-30
description: "Rosuvastatin：預測新適應症為膽固醇酯轉運蛋白缺乏症（證據等級 L5）。原適應症：本資料未收錄香港許可證的核准適應症文字"
---

# Rosuvastatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Rosuvastatin：從高三酸甘油酯血症與動脈粥狀硬化到膽固醇酯轉運蛋白缺乏症
{: .text-alpha }

## 一句話總結

Rosuvastatin 是一種降血脂藥物，知識圖譜中記錄的相關疾病包含高三酸甘油酯血症、動脈粥狀硬化、腦梗塞與家族性高膽固醇血症等。
TxGNN 模型預測排名第一的新適應症為**膽固醇酯轉運蛋白缺乏症 (cholesterol-ester transfer protein deficiency)**，但目前完全沒有臨床試驗或文獻支持。
證據最完整的候選是排名第三的**HIV 感染 (HIV infectious disease)**，有 **13 個臨床試驗**和 **20 篇文獻**，但多數屬於心血管風險與血脂管理，而非治療感染本身。以下以排名第一的預測為主軸，並補充其他候選。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本資料未收錄香港許可證的核准適應症文字；知識圖譜記錄的相關疾病包含高三酸甘油酯血症、動脈粥狀硬化、腦梗塞、家族性高膽固醇血症等（僅為知識圖譜關係，非核准適應症） |
| 預測新適應症 | 膽固醇酯轉運蛋白缺乏症 |
| TxGNN 預測分數 | 0.9954 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Rosuvastatin 屬於他汀類（HMG-CoA 還原酶抑制劑），主要作用為降低 LDL-C，並對血脂代謝有調節效果。

膽固醇酯轉運蛋白（CETP）缺乏會使 HDL-C 上升並改變脂蛋白代謝，在生物學上與 rosuvastatin 的脂質調節作用有所重疊。但這僅是計算模型的預測。此外，該病為罕見遺傳特質，常不具臨床危害，是否真有治療需求並不明確。

## 臨床試驗證據

目前無相關臨床試驗登記（針對膽固醇酯轉運蛋白缺乏症）。

## 文獻證據

目前無相關文獻（針對膽固醇酯轉運蛋白缺乏症）。

## 其他預測候選概覽

| 排名 | 預測疾病 | TxGNN 分數 | 證據等級 | 建議 |
|------|---------|-----------|---------|------|
| 2 | 腦幹梗塞 | 0.9944 | L5 | Hold |
| 3 | HIV 感染 | 0.9937 | L2 | Research Question |
| 4 | 低 α 脂蛋白血症 | 0.9925 | L5 | Research Question |
| 5 | 伴有共濟失調步態、無語言及皮質白質減少的神經發展障礙 | 0.9922 | L5 | Hold |
| 6 | ABri 類澱粉變性 | 0.9918 | L5 | Hold |

說明：

- **腦幹梗塞**：僅有兩篇間接文獻（大鼠外泌體合併 rosuvastatin 的前臨床研究、血液透析患者的生物標記研究），沒有任何研究直接針對腦幹梗塞，因此依規則為 L5。該病屬於既有腦中風類別的延伸，並非真正的再利用。
- **低 α 脂蛋白血症**：兩個試驗（攝護腺癌、無關的第一期新藥）與該病不符，文獻為綜述與個案報告，沒有直接研究，因此為 L5。
- **其他兩項**：沒有試驗或文獻，也缺乏明確機轉，需先做標靶或路徑層級的驗證。

## HIV 感染候選的證據摘要

此候選的研究針對 HIV 族群的心血管風險、發炎與血脂管理，與感染治療本身不同。

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01218802](https://clinicaltrials.gov/study/NCT01218802) | Phase 2 | 完成 | 147 | 安慰劑對照，評估 96 週 rosuvastatin 對 HIV 患者心血管風險與骨流失的影響 |
| [NCT03037372](https://clinicaltrials.gov/study/NCT03037372) | Phase 3 | 狀態未知 | 320 | 比較 atorvastatin 與 rosuvastatin 對免疫活化與發炎的等效性（他汀間比較） |
| [NCT06317051](https://clinicaltrials.gov/study/NCT06317051) | Phase 3 | 進行中（不招募） | 300 | 因子設計，比較 dapagliflozin 及 rosuvastatin/ezetimibe 與 pitavastatin |
| [NCT00117494](https://clinicaltrials.gov/study/NCT00117494) | Phase 4 | 完成 | 86 | 比較 rosuvastatin 與 pravastatin 用於接受抗病毒治療的血脂異常患者 |
| [NCT02841774](https://clinicaltrials.gov/study/NCT02841774) | Phase 2 | 完成 | 10 | 急性冠心症後高劑量 rosuvastatin 與 pravastatin 比較（樣本極小） |
| [NCT02234492](https://clinicaltrials.gov/study/NCT02234492) | Phase 4 | 完成 | 35 | 以冠狀動脈血流儲備與發炎指標為替代終點 |
| [NCT00673582](https://clinicaltrials.gov/study/NCT00673582) | Phase 4 | 提前終止 | 250 | 以頸動脈超音波評估粥狀硬化進展 |
| [NCT01813357](https://clinicaltrials.gov/study/NCT01813357) | Phase 4 | 完成 | 84 | 中度心血管風險 HIV 患者的粥狀硬化進展 |
| [NCT00885495](https://clinicaltrials.gov/study/NCT00885495) | Phase 1/2 | 完成 | 17 | darunavir/ritonavir 的藥動學交互作用研究 |
| [NCT00184951](https://clinicaltrials.gov/study/NCT00184951) | Phase 2 | 完成 | 30 | 與 lopinavir/ritonavir 併用的藥動/藥效研究 |

另有數個 Phase 1 藥動交互作用研究，僅提供劑量與安全參考。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39088828](https://pubmed.ncbi.nlm.nih.gov/39088828/) | 2024 | RCT／次要分析 | AIDS | 男性 HIV 患者中 rosuvastatin 未改善動脈硬度，可能伴隨心臟代謝不良事件 |
| [25514794](https://pubmed.ncbi.nlm.nih.gov/25514794/) | 2015 | 臨床研究 | J Acquir Immune Defic Syndr | 降低血管發炎與 T 細胞、單核球活化 |
| [32955957](https://pubmed.ncbi.nlm.nih.gov/32955957/) | 2021 | 臨床研究 | Infect Dis (Lond) | 降低發炎標記並減緩代謝症候群患者的粥狀硬化進展 |
| [40158388](https://pubmed.ncbi.nlm.nih.gov/40158388/) | 2025 | 機轉／轉譯研究 | EBioMedicine | 探討對 HIV 患者 CD8+ T 細胞記憶潛能與功能的影響 |
| [29804227](https://pubmed.ncbi.nlm.nih.gov/29804227/) | 2018 | 綜述 | Curr Infect Dis Rep | 彙整他汀在 HIV 族群降低心血管風險的角色 |
| [26658651](https://pubmed.ncbi.nlm.nih.gov/26658651/) | 2016 | 綜述 | Curr Opin Infect Dis | 評估他汀改善 HIV 患者心血管結果的證據 |
| [25907504](https://pubmed.ncbi.nlm.nih.gov/25907504/) | 2015 | 系統性回顧 | Am J Cardiol | 他汀在 HIV 感染者的效用 |
| [27941393](https://pubmed.ncbi.nlm.nih.gov/27941393/) | 2017 | 臨床研究 | AIDS | 先導研究，評估對 HIV 相關 COPD 肺功能的影響 |

## 香港上市資訊

資料顯示至少有 20 張單一成分的有效許可證（清單可能不完整），以下列出 5 張。本資料未收錄各許可證的劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65620 | ROSETOR 5 TABLETS 5MG | 錠劑 | 資料未收錄 |
| HK-65073 | VICKROSTOR TABLETS 10MG | 錠劑 | 資料未收錄 |
| HK-64427 | ROSUVASTATIN ALVOGEN TABLETS 20MG | 錠劑 | 資料未收錄 |
| HK-61457 | APO-ROSUVASTATIN TABLET 20MG | 錠劑 | 資料未收錄 |
| HK-61936 | PMS-ROSUVASTATIN TABLETS 10MG | 錠劑 | 資料未收錄 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：肝病、膽囊疾病、甲狀腺功能低下、肌病變、橫紋肌溶解症、蛋白尿等。
- **藥物交互作用**（共 100 筆，列出部分）：
  - 重大：Fenofibrate、Atazanavir
  - 中度：Atorvastatin、Ezetimibe、Amiodarone、Bempedoic acid、Paclitaxel、Adalimumab 等
  - 輕微：Levonorgestrel、Norethisterone、Desogestrel

仿單的警語與禁忌資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold（膽固醇酯轉運蛋白缺乏症）**

**理由：**
- 排名第一的預測沒有任何臨床試驗或文獻，證據僅為 L5，且該病多為無症狀的遺傳特質，治療需求不明。
- 值得追蹤的是 HIV 候選：有 Phase 2 安慰劑對照試驗，建議列為研究問題，但證據集中於替代終點與心血管風險管理，且近期文獻結果並不一致。

**若要推進需要：**
- 取得原廠仿單的核准適應症、警語與禁忌，並補齊作用機轉資料
- 針對 CETP 缺乏症，需先釐清臨床需求與生物學驗證
- 針對 HIV 候選，需確認 NCT03037372 與 NCT06317051 的結果，並以硬性心血管終點取得確證性資料
- 評估與抗病毒藥物併用時的交互作用監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

