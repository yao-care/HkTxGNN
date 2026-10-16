---
layout: default
title: Ranibizumab
parent: 僅模型預測 (L5)
nav_order: 756
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ranibizumab：預測新適應症為嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)（證據等級 L5）。原適應症：香港許可證未載明核准適應症文字"
monitor_inn: "RANIBIZUMAB"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetes mellitus type 2 associated cataract", "immature cataract", "craniostenosis cataract", "mature cataract"]
---

# Ranibizumab
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

# Ranibizumab：從糖尿病視網膜病變到嚴重非增殖性糖尿病視網膜病變

## 一句話總結

Ranibizumab 是一種抗 VEGF 抗體片段，原本用於糖尿病視網膜病變、黃斑部病變、糖尿病黃斑水腫等眼科疾病。
TxGNN 模型預測它可能對**嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)** 有效，
目前有 **19 篇文獻**支持這個方向，但**無已登記的臨床試驗紀錄**。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症文字；知識圖譜列出的原適應症包括糖尿病視網膜病變、黃斑部病變、糖尿病黃斑水腫、早產兒視網膜病變等 |
| 預測新適應症 | 嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L1（依文獻標題推定，詳見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

Ranibizumab 是抗 VEGF（血管內皮生長因子）的抗體片段。目前缺乏詳細的作用機轉資料，但就已知資訊，VEGF 會促進視網膜血管滲漏與新生血管形成，而糖尿病視網膜病變患者的血清與玻璃體 VEGF 濃度升高（PMID 36580154）。因此抑制 VEGF 在機轉上相當直接。

需要注意，糖尿病視網膜病變本身已是 ranibizumab 的原適應症之一。這項預測比較像是在同一疾病家族內，延伸到特定嚴重度（嚴重非增殖性階段），而非全新的疾病。

證據等級 L1 是依文獻標題與已知背景推定：文獻包含 RIDE/RISE 試驗的事後分析，以及 Port Delivery System 搭配 ranibizumab 對比觀察組用於非增殖性糖尿病視網膜病變的隨機試驗（Pavilion）。這些試驗的具體階段與設計並未由摘要逐一核實，且無臨床試驗登記資料，建議後續查證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

（依 RCT／RCT 事後分析優先，其次為系統性回顧與綜述，列出 10 篇）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [40048178](https://pubmed.ncbi.nlm.nih.gov/40048178/) | 2025 | RCT | JAMA Ophthalmology | Pavilion 試驗：ranibizumab 持續釋放系統 (PDS) 對比監測，用於無黃斑水腫的非增殖性糖尿病視網膜病變 |
| [32606578](https://pubmed.ncbi.nlm.nih.gov/32606578/) | 2020 | RCT 事後分析 | Clin Ophthalmol | RIDE/RISE 試驗中早期糖尿病視網膜病變改善的預測因子 |
| [36774994](https://pubmed.ncbi.nlm.nih.gov/36774994/) | 2023 | RCT 事後分析／統合分析 | Ophthalmol Retina | 基線視網膜病變嚴重度與 ranibizumab 治療後黃斑水腫緩解時間的關係 |
| [39673354](https://pubmed.ncbi.nlm.nih.gov/39673354/) | 2025 | 系統性回顧與統合分析 | Health Technol Assess | 抗 VEGF 藥物與雷射光凝治療糖尿病視網膜病變的比較 |
| [42219053](https://pubmed.ncbi.nlm.nih.gov/42219053/) | 2026 | 系統性回顧與統合分析 | Eur J Pharmacol | Ranibizumab 持續釋放系統用於糖尿病視網膜病變與黃斑水腫的疾病修飾與durability |
| [30234859](https://pubmed.ncbi.nlm.nih.gov/30234859/) | 2018 | RCT 長期分析 | Retina | DRCR.net Protocol I 五年報告：ranibizumab 治療糖尿病黃斑水腫時視網膜病變嚴重度的變化 |
| [28448655](https://pubmed.ncbi.nlm.nih.gov/28448655/) | 2017 | RCT 次要分析 | JAMA Ophthalmol | 比較 aflibercept、bevacizumab、ranibizumab 兩年間視網膜病變的變化 |
| [36161830](https://pubmed.ncbi.nlm.nih.gov/36161830/) | 2022 | 延伸試驗分析 | BMJ Open Ophthalmol | RIDE/RISE 延伸期：減少給藥頻率後視網膜病變嚴重度量表的變化 |
| [33966556](https://pubmed.ncbi.nlm.nih.gov/33966556/) | 2021 | Review | Expert Opin Biol Ther | Ranibizumab 治療糖尿病視網膜病變的回顧 |
| [40969370](https://pubmed.ncbi.nlm.nih.gov/40969370/) | 2025 | 回溯性世代研究 | Front Endocrinol | 嚴重非增殖性糖尿病視網膜病變接受抗 VEGF 併用雷射的療效預測列線圖模型 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65166 | LUCENTIS SOLUTION FOR INJECTION 2.3MG/0.23ML (VIAL+FILTER NEEDLE PACK) | 注射液 | 資料未載明 |
| HK-68384 | LUCENTIS SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 10MG/ML | 預充填注射針筒 | 資料未載明 |
| HK-63860 | LUCENTIS SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 10MG/ML | 預充填注射針筒 | 資料未載明 |

三張許可證皆為有效的單一成分製劑，持證商為 Novartis Pharmaceuticals (HK) Limited。

## 安全性考量

- **知識圖譜標示的禁忌疾病**：眼部感染性疾病、結膜炎。此資訊來自知識圖譜關聯，並非仿單原文，仍須以仿單為準。

其餘警語、禁忌症與藥物交互作用，請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 抗 VEGF 對糖尿病視網膜病變的機轉直接，且有多項 RCT 及其事後分析、系統性回顧支持，包括針對非增殖性階段的 Pavilion 試驗。
- 但該適應症屬於既有原適應症疾病家族內的延伸，且證據等級是依文獻標題推定，並無臨床試驗登記資料，因此需要設定查證與安全防護條件。

**若要推進需要：**
- 取得並解析香港衛生署仿單，確認核准適應症、警語與禁忌症
- 核實 Pavilion、RIDE/RISE 等試驗的實際階段、設計與嚴重非增殖性亞群的結果
- 補充作用機轉資料（DrugBank）
- 確認 Port Delivery System 等劑型在香港的可及性
- 建立眼內注射相關風險（如眼內感染、眼壓上升）的監測計畫

---

**附註：其他預測適應症**

模型亦預測了糖尿病第 2 型相關白內障、未成熟白內障、顱縫早閉白內障與成熟白內障（分數皆約 99.99%）。這些預測缺乏抗 VEGF 治療晶體混濁的機轉依據，現有文獻僅涉及黃斑水腫合併白內障手術的情境，或是與 ranibizumab 無關的案例報告，分數高可能反映知識圖譜中眼科疾病的鄰近關係。建議皆為 **Hold**。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

