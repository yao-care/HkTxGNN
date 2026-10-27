---
layout: default
title: Zidovudine
parent: 僅模型預測 (L5)
nav_order: 950
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Zidovudine：預測新適應症為猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)（證據等級 L5）。原適應症：HIV 感染、AIDS"
monitor_inn: "ZIDOVUDINE"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
---

# Zidovudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Zidovudine：從 HIV 感染到猿猴免疫缺陷病毒感染
{: .text-alpha }

## 一句話總結

Zidovudine（AZT）是核苷類逆轉錄酶抑制劑（NRTI），原本用於治療 HIV 感染與 AIDS。
TxGNN 模型排名第一的預測為**猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)**，但這屬於動物模型，並非真正的新人類適應症；目前有 **0 個臨床試驗**和 **20 篇動物或體外文獻**。
本報告同時說明排名第五的**先天性（母嬰垂直傳染）HIV (Congenital HIV)**。該預測有較多人類證據，但本質上是原適應症的延伸。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染、AIDS（取自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 99.96% |
| 證據等級 | L4（僅有動物與體外研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

**其他預測適應症一覽：**

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 1 | 猿猴免疫缺陷病毒感染 | 99.96% | L4 | Hold |
| 2 | 貓後天免疫缺陷症候群（獸醫適應症） | 99.96% | L4 | Hold |
| 3 | 伴隨共濟失調步態、無語言及皮質白質減少的神經發展障礙 | 99.96% | L5 | Hold |
| 4 | 已廢止的家族性複合型高脂血症 | 99.62% | L5 | Hold |
| 5 | 先天性 HIV (Congenital HIV) | 99.19% | L1 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知的藥理學而言，zidovudine 屬於 NRTI，經細胞內磷酸化後抑制 HIV 逆轉錄酶，進而減少病毒複製。

SIV 是與 HIV 高度相近的慢病毒，同樣依賴逆轉錄酶複製，因此 zidovudine 在機轉上具合理性。獼猴研究顯示，它能降低病毒量、延長存活，並在暴露後預防給藥中降低傳染。不過 SIV 感染是人類 HIV 適應症的**前臨床動物模型**，並非新的人類適應症，所以沒有真正的藥物再利用價值。

相對地，先天性 HIV 與原適應症為同一病原體。Zidovudine 可通過胎盤，孕婦與新生兒的周產期預防是已確立的母嬰傳染阻斷策略，因此這屬於原適應症在特定族群與情境下的延伸，而非全新用途。

---

## 臨床試驗證據

**排名第一的預測（SIV 感染）：** 目前無相關臨床試驗登記。

**以下為排名第五的先天性 HIV 預測之相關試驗：**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00001104](https://clinicaltrials.gov/study/NCT00001104) | Phase 3 | 完成 | 538 | 安慰劑對照試驗，評估 zidovudine 用於血友病 HIV 感染者，是否延緩 AIDS 發生 |
| [NCT00102960](https://clinicaltrials.gov/study/NCT00102960) | Phase 3 | 完成 | 377 | 比較不同療程長度的抗 HIV 治療策略，對象為出生時感染的嬰兒（評估策略而非 zidovudine 本身） |
| [NCT00001007](https://clinicaltrials.gov/study/NCT00001007) | Phase 1 | 完成 | 18 | 靜脈與口服 zidovudine 用於周產期 HIV 暴露嬰兒的安全性與藥動學 |
| [NCT00000705](https://clinicaltrials.gov/study/NCT00000705) | Phase 1 | 完成 | 24 | AZT 用於血友病 HIV 感染者的早期安全性與藥理 |
| [NCT00002386](https://clinicaltrials.gov/study/NCT00002386) | Phase 4 | 完成 | 55 | 含 indinavir 的合併療法對血友病 HIV 患者凝血因子的影響（非對照） |
| [NCT00000989](https://clinicaltrials.gov/study/NCT00000989) | 未分類 | 完成 | 50 | Ganciclovir 合併 GM-CSF 治療 CMV 視網膜炎，zidovudine 為背景治療 |
| [NCT00002096](https://clinicaltrials.gov/study/NCT00002096) | Phase 1 | 完成 | 24 | 口服 ganciclovir 與 zidovudine、didanosine 的藥物交互作用 |
| [NCT00002034](https://clinicaltrials.gov/study/NCT00002034) | 未分類 | 完成 | 100 | 長期靜脈 ganciclovir 的安全性，併用 AZT（非以 zidovudine 為重點） |
| [NCT00000995](https://clinicaltrials.gov/study/NCT00000995) | 未分類 | 完成 | 60 | AZT 與 ganciclovir 合併用於 AIDS 合併 CMV 感染的毒性評估 |
| [NCT00002276](https://clinicaltrials.gov/study/NCT00002276) | 未分類 | 完成 | 未報告 | AZT 與 ibuprofen 在血友病 HIV 患者的出血傾向與血小板功能 |

---

## 文獻證據

**SIV 感染（排名第一，皆為動物或體外研究）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7695293](https://pubmed.ncbi.nlm.nih.gov/7695293/) | 1995 | 動物研究 | Antimicrob Agents Chemother | 立即口服 AZT 可預防或減輕新生獼猴 SIV 感染，降低病毒量 |
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | 動物研究 | AIDS | ZDV、3TC、indinavir 暴露後預防可阻止獼猴經陰道的 SIV 傳染 |
| [7797947](https://pubmed.ncbi.nlm.nih.gov/7797947/) | 1995 | 動物研究 | J Infect Dis | AZT 延長周產期感染獼猴的存活，降低中樞神經病毒量 |
| [7690823](https://pubmed.ncbi.nlm.nih.gov/7690823/) | 1993 | 動物研究 | J Infect Dis | 比較感染後不同時間開始 AZT 治療的效果 |
| [11020686](https://pubmed.ncbi.nlm.nih.gov/11020686/) | 2000 | Review | Ann Emerg Med | 非職業暴露後預防（PEP）的回顧，動物研究提供間接支持 |
| [8156147](https://pubmed.ncbi.nlm.nih.gov/8156147/) | 1993 | Review | Baillieres Clin Neurol | 逆轉錄病毒相關發炎性肌病變 |
| [9021180](https://pubmed.ncbi.nlm.nih.gov/9021180/) | 1997 | 體外／病毒學 | Antimicrob Agents Chemother | AZT 抗藥性 SIV 突變株（Q151M）可在新生獼猴引發 AIDS |

**先天性 HIV（排名第五，含人類研究）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [7913986](https://pubmed.ncbi.nlm.nih.gov/7913986/) | 1994 | 指引 | MMWR Recomm Rep | 美國公共衛生署建議使用 ZDV 降低周產期傳染，ACTG 076 顯示風險降低約三分之二 |
| [12197800](https://pubmed.ncbi.nlm.nih.gov/12197800/) | 2002 | 世代研究 | Arch Pediatr Adolesc Med | 觀察性資料評估 zidovudine 預防前後母嬰傳染的決定因素 |
| [28537936](https://pubmed.ncbi.nlm.nih.gov/28537936/) | 2017 | 世代／統合分析 | AIDS | 懷孕期使用 zidovudine 與先天畸形的關聯證據不一致 |
| [29912896](https://pubmed.ncbi.nlm.nih.gov/29912896/) | 2018 | 系統性回顧／網絡統合分析 | PLoS One | 比較周產期抗反轉錄病毒療法的安全性與有效性 |
| [38641597](https://pubmed.ncbi.nlm.nih.gov/38641597/) | 2024 | 系統性回顧／網絡統合分析 | BMC Infect Dis | 比較孕婦 HIV 抗病毒方案的安全性與有效性 |
| [8419601](https://pubmed.ncbi.nlm.nih.gov/8419601/) | 1993 | Phase 1 | J Pediatr | 暴露於 HIV 的嬰兒使用靜脈與口服 zidovudine 的安全性與藥動學 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-57407 | VICK-ZIDOVUDINE CAP 100MG | 未載明 | 未載明 |
| HK-59602 | RETROVIR ORAL SOLUTION 10MG/ML | 未載明 | 未載明 |
| HK-57408 | VICK-ZIDOVUDINE CAP 250MG | 未載明 | 未載明 |
| HK-66688 | ZIDOVUDINE TABLETS USP 300MG | 未載明 | 未載明 |
| HK-42757 | RETROVIR IV INFUSION 10MG/ML | 未載明 | 未載明 |

（共 8 張有效許可證，皆為單一成分，此處僅列出 5 張。）

---

## 細胞毒性

Zidovudine 為抗病毒藥物，非抗腫瘤藥物，故不適用。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：肝衰竭、肝病、脂肪肝／非酒精性脂肪肝炎、腎臟疾病、胰臟炎、膽囊疾病、肌病變／肌炎／皮肌炎、嗜中性白血球低下、顆粒球缺乏症、貧血（含巨球性貧血）、高三酸甘油脂血症、乳酸中毒、肥胖相關疾病等。這些來自知識圖譜，並非仿單內容。
- **血液學風險**：貓科動物毒性研究與預測資料均提示貧血與骨髓抑制，新生兒與嬰兒使用時應特別注意。
- **代謝風險**：HIV 治療中與脂肪代謝異常、血脂異常相關。
- **懷孕暴露**：懷孕期使用與先天畸形的關聯證據不一致。
- **藥物交互作用**（共查得 100 筆，以下列出主要項目）：
  - 中度：Amphotericin B（含脂質及膽固醇硫酸酯劑型）、類固醇（Betamethasone、Budesonide、Dexamethasone、Hydrocortisone、Prednisolone、Prednisone、Triamcinolone）、Naltrexone、Rosuvastatin、Simvastatin、Orlistat
  - 輕度：Cimetidine、Clarithromycin
  - 分級未明：Pantoprazole、Morphine、Metformin、Omeprazole

仿單層級的警語與禁忌尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（SIV 感染，排名第一）**

**理由：**
- SIV 感染是 HIV 的動物模型，證據僅有前臨床研究（L4），沒有人類臨床試驗，也沒有真正的再利用價值。排名第 2 至 4 的預測（貓免疫缺陷症候群、罕見神經發展障礙、已廢止的高脂血症）同樣不建議推進。
- 排名第五的先天性 HIV 證據最強（L1，建議 Proceed with Guardrails）。但它是原適應症在周產期情境下的延伸，且現行指引多主張以合併抗病毒療法取代 zidovudine 單藥。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症文字（目前許可證資料缺漏）
- 補充詳細的作用機轉資料
- 若走先天性 HIV 的路線：建立新生兒與嬰兒的血液學監測計畫（貧血、嗜中性白血球低下）、納入懷孕暴露安全性資料，並與現行合併療法指引比對
- 不建議在 SIV、貓免疫缺陷症候群等動物模型適應症上投入進一步資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

