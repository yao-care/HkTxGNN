---
layout: default
title: Ezetimibe
parent: 高證據等級 (L1-L2)
nav_order: 361
evidence_level: L1
indication_count: 4
last_modified_at: 2026-10-14
description: "Ezetimibe：預測新適應症為高脂蛋白血症 (Hyperlipoproteinemia)（證據等級 L1）。原適應症：高脂血症、家族性高膽固醇血症、麩固醇血症等"
monitor_inn: "EZETIMIBE"
predicted_indications: ["hypercholesterolemia due to cholesterol 7alpha-hydroxylase deficiency", "cholesterol-ester transfer protein deficiency"]
---

# Ezetimibe
{: .fs-9 }

證據等級: **L1** | 預測適應症: **4** 個
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

# Ezetimibe：從高脂血症到高脂蛋白血症

## 一句話總結

Ezetimibe（依澤替米貝）是膽固醇吸收抑制劑，原本用於高脂血症、家族性高膽固醇血症及麩固醇血症的治療。
TxGNN 模型預測它對**高脂蛋白血症 (Hyperlipoproteinemia)** 有效，目前有 **40 個臨床試驗**和 **18 篇文獻**支持這個方向。
但此預測屬於已核准的既有用途，並非真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高脂血症、家族性高膽固醇血症、麩固醇血症等（來自知識圖譜） |
| 預測新適應症 | 高脂蛋白血症 (Hyperlipoproteinemia) |
| TxGNN 預測分數 | 99.63% |
| 證據等級 | L1 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏完整的作用機轉欄位資料。依據已知資訊，Ezetimibe 抑制小腸 NPC1L1 介導的膽固醇吸收，降低 LDL-C。可單獨使用，也可與 statin 併用。

高脂蛋白血症與高脂血症本質上同屬血脂異常，Ezetimibe 的降 LDL-C 機轉直接適用。因此高 TxGNN 分數與已知藥理相符。

需要注意：這是既有適應症，而非真正的藥物再利用。多數試驗是併用或對照設計（如與 statin、evolocumab、inclisiran 併用或比較），Ezetimibe 單獨的效果部分被混雜。

其他預測的疾病中，**膽固醇 7α-羥化酶缺乏所致高膽固醇血症**僅有一篇前臨床文獻支持（證據等級 L4，建議 Hold）。**膽固醇酯轉運蛋白 (CETP) 缺乏症**僅有模型預測與間接文獻（L5，建議 Hold）。CETP 缺乏通常使 HDL-C 升高，不需降 LDL 治療，機轉上缺乏合理連結。

---

## 臨床試驗證據

以下列出與高脂蛋白血症最相關的 10 個試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00753883](https://clinicaltrials.gov/study/NCT00753883) | Phase 4 | 完成 | 40 | 比較 Ezetimibe 加 statin 與單用 statin 的降脂效果 |
| [NCT01984424](https://clinicaltrials.gov/study/NCT01984424) | Phase 3 | 完成 | 511 | Evolocumab 對比 Ezetimibe，用於無法耐受 statin 的患者（Ezetimibe 為活性對照） |
| [NCT03847506](https://clinicaltrials.gov/study/NCT03847506) | Phase 4 | 完成 | 127 | Ezetimibe/Rosuvastatin 複方併用降壓複方，用於高血壓合併高脂血症 |
| [NCT00092833](https://clinicaltrials.gov/study/NCT00092833) | Phase 3 | 終止 | 49 | 開放標示治療使用研究，對象為同合子家族性高膽固醇血症或麩固醇血症 |
| [NCT00271817](https://clinicaltrials.gov/study/NCT00271817) | Phase 3 | 完成 | 1220 | Ezetimibe/Simvastatin 併用 Niacin 緩釋錠，用於 IIa/IIb 型高脂血症 |
| [NCT00092573](https://clinicaltrials.gov/study/NCT00092573) | Phase 3 | 完成 | 576 | Fenofibrate 併用 Ezetimibe，用於混合型高脂血症 |
| [NCT00093899](https://clinicaltrials.gov/study/NCT00093899) | Phase 3 | 完成 | 611 | Ezetimibe/Simvastatin 併用 Fenofibrate，用於混合型高脂血症 |
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | 完成 | 720 | ENHANCE：Ezetimibe 加高劑量 Simvastatin 對頸動脈粥狀硬化進展的影響 |
| [NCT00705211](https://clinicaltrials.gov/study/NCT00705211) | N/A | 完成 | 1794 | 日本 52 週上市後觀察研究，評估長期安全性與療效 |
| [NCT00704535](https://clinicaltrials.gov/study/NCT00704535) | N/A | 完成 | 4105 | 菲律賓上市後監測，評估安全性、耐受性與療效 |

---

## 文獻證據

文獻檢索以家族性高膽固醇血症與血脂異常為主，多數為綜述，Ezetimibe 特異性的直接證據有限：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40347969](https://pubmed.ncbi.nlm.nih.gov/40347969/) | 2025 | RCT（Phase 3） | Lancet | TANDEM：Obicetrapib 與 Ezetimibe 固定複方降低 LDL-C |
| [41206969](https://pubmed.ncbi.nlm.nih.gov/41206969/) | 2026 | RCT | JAMA | 口服 PCSK9 抑制劑 Enlicitide 用於雜合子家族性高膽固醇血症 |
| [25282519](https://pubmed.ncbi.nlm.nih.gov/25282519/) | 2015 | RCT | Lancet | RUTHERFORD-2：Evolocumab 用於雜合子 FH（背景治療含 Ezetimibe） |
| [37850379](https://pubmed.ncbi.nlm.nih.gov/37850379/) | 2024 | RCT | Circulation | ORION-5：Inclisiran 用於同合子 FH |
| [35101175](https://pubmed.ncbi.nlm.nih.gov/35101175/) | 2022 | 世代研究 | Lancet | 全球同合子 FH 的回溯性世代研究 |
| [40682836](https://pubmed.ncbi.nlm.nih.gov/40682836/) | 2025 | Review | Mol Med Rep | 高脂血症藥物研究進展 |
| [33766264](https://pubmed.ncbi.nlm.nih.gov/33766264/) | 2021 | Review | J Am Coll Cardiol | LDL-C 與 ApoB 降低的新興療法 |
| [19654419](https://pubmed.ncbi.nlm.nih.gov/19654419/) | 2009 | Review | Drug Ther Bull | Ezetimibe 更新：可降低 LDL-C，但當時缺乏心血管結果證據，不應取代 statin |
| [23956253](https://pubmed.ncbi.nlm.nih.gov/23956253/) | 2013 | Review | Eur Heart J | 歐洲動脈粥狀硬化學會共識：FH 診斷不足與治療不足 |
| [29219151](https://pubmed.ncbi.nlm.nih.gov/29219151/) | 2017 | Review | Nat Rev Dis Primers | 家族性高膽固醇血症綜述 |

---

## 香港上市資訊

香港共有 20 張有效許可證，皆為單一許可證（含與 statin 等的複方製劑）。以下列出 5 張主要許可證，資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51223 | EZETROL TAB 10 MG（Organon） | 錠劑 10 mg | — |
| HK-64454 | EZETIMIBE SANDOZ TABLETS 10MG | 錠劑 10 mg | — |
| HK-53014 | VYTORIN TAB 10MG/20MG（Ezetimibe/Simvastatin） | 錠劑 | — |
| HK-64636 | ATOZET TABLETS 10MG/20MG（Ezetimibe/Atorvastatin） | 錠劑 | — |
| HK-67819 | NUSTENDI TABLETS 180MG/10MG（Bempedoic acid/Ezetimibe） | 錠劑 | — |

---

## 安全性考量

- **知識圖譜標示的相關疾病風險**（非仿單文字）：胰臟炎、肝臟疾病、膽囊疾病、肌病變、肌肉疾病、骨骼肌疾病、家族性週期性麻痺、物質濫用/依賴、橫紋肌溶解症、結節性筋膜炎。
- **藥物交互作用**：共查詢到 100 筆。中度等級包括 Chenodeoxycholic acid、Eluxadoline、Rosuvastatin、Simvastatin。其餘多為等級未知，如 Cimetidine、Metformin、Omeprazole 等。
- 官方警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 高脂蛋白血症與家族性高膽固醇血症有多個已完成的 Phase 3 試驗，Ezetimibe 在香港已廣泛上市，證據充分（L1）。但這屬於既有適應症，並非新的再利用機會。
- 另兩項預測（CYP7A1 缺乏、CETP 缺乏）證據薄弱，建議 Hold。

**若要推進需要：**
- 取得香港衛生署核准的仿單，確認警語、禁忌症與核准適應症（目前許可證資料缺少適應症文字）。
- 補充 Ezetimibe 作用機轉的結構化資料。
- 若要評估獨立效果，需區分單用與併用試驗的數據，降低混雜影響。
- 對肝病、肌病變、膽囊疾病患者及與 statin 併用者，建立肝功能與肌肉症狀的監測計畫。
- 若有意探索 CYP7A1 缺乏等罕見疾病，需先累積臨床前至病例層級的證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

