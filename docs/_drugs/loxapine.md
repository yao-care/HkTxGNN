---
layout: default
title: Loxapine
parent: 僅模型預測 (L5)
nav_order: 544
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Loxapine：預測新適應症為躁期雙極性情感疾患 (Manic Bipolar Affective Disorder)（證據等級 L5）。原適應症：雙極性疾患、重度情感性疾患、思覺失調症"
monitor_inn: "LOXAPINE"
predicted_indications: ["manic bipolar affective disorder", "retinal dystrophy with or without extraocular anomalies", "hydranencephaly (disease)", "myopia X-linked", "congenital disorder of glycosylation with defective fucosylation"]
---

# Loxapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Loxapine：從雙極性疾患／思覺失調症到躁期雙極性情感疾患

## 一句話總結

Loxapine 是第一代抗精神病藥（dibenzoxazepine 類），原本用於雙極性疾患、重度情感性疾患與思覺失調症。
TxGNN 模型預測它可能對**躁期雙極性情感疾患 (Manic Bipolar Affective Disorder)** 有效，
目前**無臨床試驗登記**，但有 **20 篇文獻**支持這個方向（多為回顧型文章，主要涉及吸入式 loxapine 治療急性躁動）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 雙極性疾患、重度情感性疾患、思覺失調症（許可證未載明適應症文字，此處依知識圖譜資料） |
| 預測新適應症 | 躁期雙極性情感疾患 (Manic Bipolar Affective Disorder) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L3（見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Proceed with Guardrails |

**證據等級說明：** 本次整理的資料中沒有任何臨床試驗登記，文獻以回顧與系統性回顧為主，依判定規則屬 L3。文獻提到吸入式 loxapine 有兩項 Phase 3 隨機對照試驗，但原始試驗不在本次資料內，無法查證，因此未據此提高等級。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知藥理，Loxapine 屬於 dibenzoxazepine 類抗精神病藥，具有多巴胺 D2 與血清素 5-HT2A 受體拮抗作用。這類機轉與抗躁症及抗躁動作用相符。

躁期雙極性情感疾患與原適應症中的雙極性疾患屬同一疾病範疇。吸入式 loxapine (Adasuve) 已在美國與歐盟核准用於雙極性 I 型或思覺失調症相關的急性躁動，文獻也支持此用途。

需要注意：此預測較接近原有適應症的延伸，是針對躁期或躁動表現與給藥途徑的細分，並非真正的新用途。針對「躁症本身」（有別於躁動）的直接證據仍屬間接。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

下表列出 10 篇相關文獻（本次共 20 篇，皆以吸入式 loxapine 或急性躁動為主題，多為回顧型文章）。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [27151529](https://pubmed.ncbi.nlm.nih.gov/27151529/) | 2016 | 系統性回顧／統合分析 | Hum Psychopharmacol | 評估思覺失調症或雙極性疾患相關急性躁動的短期藥物治療 |
| [23740380](https://pubmed.ncbi.nlm.nih.gov/23740380/) | 2013 | Review | CNS Drugs | 吸入式 loxapine 在美歐獲准用於急性躁動；血中濃度約 2 分鐘達峰，並有兩項隨機雙盲試驗 |
| [22226343](https://pubmed.ncbi.nlm.nih.gov/22226343/) | 2012 | 試驗效果量分析 | Int J Clin Pract | 從兩項 Phase III 隨機對照試驗的效果量評估吸入式 loxapine 療效 |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatr Scand | 回顧躁症治療選項，提出心情穩定劑與抗精神病藥的選擇建議 |
| [31496709](https://pubmed.ncbi.nlm.nih.gov/31496709/) | 2019 | Review | Neuropsychiatr Dis Treat | 檢視吸入式 loxapine 治療躁動的安全性、療效與病人接受度 |
| [30721526](https://pubmed.ncbi.nlm.nih.gov/30721526/) | 2019 | Review | Drugs R D | 專家回顧吸入式 loxapine 用於雙極性疾患與思覺失調症的急性躁動 |
| [38301034](https://pubmed.ncbi.nlm.nih.gov/38301034/) | 2024 | Review | Prim Care Companion CNS Disord | 討論急性躁動處置的替代方式 |
| [37581475](https://pubmed.ncbi.nlm.nih.gov/37581475/) | 2023 | Review | Expert Opin Pharmacother | 探討雙極性疾患相關躁動的藥物治療改善方向 |
| [35913401](https://pubmed.ncbi.nlm.nih.gov/35913401/) | 2022 | Review | Expert Rev Neurother | 回顧 loxapine 五十年來用於急性行為困擾的非強制鎮靜經驗 |
| [28208695](https://pubmed.ncbi.nlm.nih.gov/28208695/) | 2017 | Review | Int J Mol Sci | 評估吸入式 loxapine 治療精神疾患急性躁動的療效與耐受性 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67228 | ADASUVE INHALATION POWDER, PRE-DISPENSED 9.1MG | 吸入粉劑 | 許可證資料未載明 |

## 安全性考量

- **禁忌症（知識圖譜資料，非仿單內容）：** 癲癇、良性攝護腺肥大、物質濫用／依賴、女性乳癌、心血管疾病、心臟病、青光眼、抗精神病藥惡性症候群、阿茲海默症、遲發性運動障礙、口舌顏面運動障礙、高泌乳素血症（含家族性與後天性）、泌乳素分泌型腦下垂體腫瘤。
- **藥物交互作用：** 共記錄 100 項。列出的重要項目中，**嚴重 (Major)** 包括 Bupropion、Morphine、Potassium citrate；**中度 (Moderate)** 包括 Epinephrine、Atropine、Hyoscyamine、Loperamide、Dicyclomine、Glycopyrronium 等（多為抗膽鹼或中樞抑制相關）。
- **其他注意事項（依藥物類別與文獻推論）：** 吸入劑型有支氣管痙攣風險，需限用於無氣道疾病的病人；另有鎮靜與錐體外症狀。

詳細警語請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 此預測與 loxapine 既有的雙極性疾患適應症高度重疊，且吸入式劑型已在香港上市，文獻也支持其用於躁動。
- 但沒有臨床試驗登記，文獻多為回顧，對躁症本身的直接證據有限。

**若要推進需要：**
- 取得吸入式 loxapine 兩項 Phase 3 隨機對照試驗的原始資料並查證
- 補充作用機轉（MOA）資料
- 取得香港衛生署仿單的警語與禁忌，並確認許可證核准適應症
- 建立支氣管痙攣、鎮靜與錐體外症狀的監測及病人篩選計畫
- 評估大量藥物交互作用的處方審查機制

## 其他預測的備註

排名第 2 至第 5 的預測（視網膜失養症、無腦畸形、X 連鎖近視、岩藻糖化缺陷之先天性糖基化異常）皆無試驗或文獻支持，也找不到合理的作用機轉，證據等級均為 L5，建議 **Hold**。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

