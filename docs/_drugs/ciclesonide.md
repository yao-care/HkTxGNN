---
layout: default
title: Ciclesonide
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Ciclesonide：預測新適應症為異位性皮膚炎 (Atopic Eczema)（證據等級 L5）。原適應症：氣喘、內因性氣喘、過敏性氣喘、過敏性鼻炎、血管運動性鼻炎"
monitor_inn: "CICLESONIDE"
predicted_indications: ["atopic eczema", "2-hydroxyethyl methacrylate sensitization", "dermatitis, atopic", "bronchitis", "contact dermatitis", "asthma-related traits, susceptibility to"]
---

# Ciclesonide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Ciclesonide：從氣喘與過敏性鼻炎到異位性皮膚炎

## 一句話總結

Ciclesonide 是一種吸入型皮質類固醇前驅藥，原本用於氣喘與過敏性鼻炎。
TxGNN 模型預測它可能對**異位性皮膚炎 (Atopic Eczema)** 有效，
但目前**沒有臨床試驗**，也**沒有直接相關文獻**支持，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 氣喘、內因性氣喘、過敏性氣喘、過敏性鼻炎、血管運動性鼻炎 |
| 預測新適應症 | 異位性皮膚炎 (Atopic Eczema) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ciclesonide 是吸入型皮質類固醇，進入體內後經酯酶活化為 des-ciclesonide，作用於糖皮質素受體，產生抗發炎效果。

異位性皮膚炎的核心是皮膚的過敏性發炎，局部皮質類固醇本身就是標準治療。因此從抗發炎機轉來看，此預測具有合理性。

不過這屬於類別層級的推論。Ciclesonide 目前的劑型是吸入與鼻用，資料中沒有確立的皮膚外用劑型，也沒有針對此適應症的研究。其他排名較高的預測還包括異位性皮膚炎的重複條目（dermatitis, atopic，分數 99.73%）、支氣管炎（99.70%）與接觸性皮膚炎（99.25%），同樣缺乏直接證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

（補充：在其他預測適應症中，支氣管炎有一篇芬蘭 COPD 指引 [PMID 25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/)，僅為吸入型類固醇的間接證據；接觸性皮膚炎有一篇病例報告 [PMID 22957490](https://pubmed.ncbi.nlm.nih.gov/22957490/)，指出吸入型 budesonide 引起全身過敏性皮膚炎，並與 ciclesonide 在貼膚試驗中有交叉反應，屬於安全性訊號，並非療效證據。）

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53034 | ALVESCO 80 INHALER 80MCG/ACTUATION | 吸入劑 | 未提供 |
| HK-59322 | OMNARIS NASAL SPRAY 50MCG | 鼻噴劑 | 未提供 |
| HK-53035 | ALVESCO 160 INHALER 160MCG/ACTUATION | 吸入劑 | 未提供 |

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜關聯，非仿單文字）：單純疱疹病毒角膜炎、腎上腺皮質功能不全、愛迪生氏症、骨質疏鬆（含停經後骨質疏鬆）、黴菌感染、皮癬菌病、高眼壓、青光眼、寄生蟲感染。
- **藥物交互作用**：共查得 63 筆，以下為主要項目：
  - 重度：Cladribine
  - 中度：Clarithromycin、Miconazole、Cobicistat、Atazanavir、Fosamprenavir、Amprenavir、Boceprevir、Ceritinib、Conivaptan、Fostamatinib、Insulin human（吸入型速效）、Abametapir（外用）
  - 輕度：Formoterol、Salbutamol、Arformoterol
  - 其中多個中度交互作用屬於 CYP3A4 抑制劑類，使用時需留意。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.96%），但沒有任何臨床試驗或文獻，證據等級僅為 L5。
- 現有劑型為吸入與鼻用，缺乏皮膚外用的劑型依據，且有皮質類固醇交叉過敏的安全性訊號。

**若要推進需要：**
- 補充作用機轉資料，並釐清 ciclesonide 在皮膚局部的活化與藥效。
- 評估是否有外用劑型或給藥途徑的可行性。
- 進行文獻與臨床試驗的系統性檢索，並與現有局部類固醇做比較。
- 取得香港衛生署仿單，完成警語與禁忌症的安全性審查。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

