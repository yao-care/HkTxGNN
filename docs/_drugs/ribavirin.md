---
layout: default
title: Ribavirin
parent: 高證據等級 (L1-L2)
nav_order: 768
evidence_level: L1
indication_count: 9
monitor_inn: "RIBAVIRIN"
predicted_indications: ["chronic hepatitis B virus infection", "hepatoportal sclerosis", "primitive portal vein thrombosis", "hepatopulmonary syndrome", "early-onset familial noncirrhotic portal hypertension", "hepatic porphyria", "IgG4-related pachymeningitis", "eosinophilic angiocentric fibrosis", "IgG4-related mediastinitis"]
last_modified_at: 2026-10-30
description: "Ribavirin：預測新適應症為慢性 B 型肝炎（證據等級 L5）。原適應症：香港許可證資料中未載明核准適應症文字"
---

# Ribavirin
{: .fs-9 }

證據等級: **L1** | 預測適應症: **9** 個
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

## Ribavirin：從 C 型肝炎到慢性 B 型肝炎
{: .text-alpha }

## 一句話總結

Ribavirin（利巴韋林）在知識圖譜中記錄的已知用途為慢性 C 型肝炎與呼吸道融合病毒感染。
TxGNN 模型預測它可能對**慢性 B 型肝炎 (Chronic Hepatitis B Virus Infection)** 有效，
目前有 **15 個臨床試驗**和 **20 篇文獻**與此方向相關，但其中直接以 B 型肝炎為對象的研究有限，且多為合併干擾素的療法。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料中未載明核准適應症文字；知識圖譜記錄的關聯為慢性 C 型肝炎、呼吸道融合病毒感染 |
| 預測新適應症 | 慢性 B 型肝炎 |
| TxGNN 預測分數 | 0.9986 |
| 證據等級 | L1（依規則為候選上限，詳見下方說明） |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

**關於證據等級：** 有 2 個已完成的 Phase 3 試驗與 B 型肝炎直接相關性較高的只有 NCT00114361（完成，n=138，且為合併 peginterferon 的療法）；NCT00154869 狀態為「未知」，NCT03759782 狀態亦為「未知」，均不算已完成。因此嚴格來說不符合「≥2 個已完成 Phase 3 RCT」的 L1 條件。NCT00114361 為 1 個已完成的 Phase 3 試驗，且為合併療法、無法分離 ribavirin 單獨貢獻，本報告保守地將證據等級評為 **L2**（以此為準）。

> 更正：快速總覽中的證據等級以 **L2** 為準。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Ribavirin 是核苷類似物，具廣譜抗病毒活性（一般認為涉及抑制 IMPDH、耗竭 GTP 以及免疫調節），在 C 型肝炎與呼吸道融合病毒感染的用途已有知識圖譜記錄。

C 型與 B 型肝炎同屬慢性病毒性肝炎，臨床上常使用相似的干擾素療法，這可能是模型給出高分的原因。不過，ribavirin 單用對 B 型肝炎病毒的抑制作用很弱，若有效益，較可能來自與干擾素合併時的免疫調節，而不是直接抑制病毒複製。TxGNN 的高分也可能反映肝炎與抗病毒網路的相近性，本身不足以證明療效。

## 臨床試驗證據

以下列出與 B 型肝炎較相關的試驗（其餘多為 C 型肝炎試驗，ribavirin 僅為背景用藥，未列入）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00114361](https://clinicaltrials.gov/study/NCT00114361) | Phase 3 | 完成 | 138 | 比較 peginterferon alfa-2a 加 ribavirin 與 peginterferon 單用於 HBeAg 陰性慢性 B 型肝炎；為最直接的證據，但屬合併療法 |
| [NCT00275938](https://clinicaltrials.gov/study/NCT00275938) | Phase 2/3 | 完成 | 120 | 干擾素 alpha-2b 加 ribavirin 治療慢性 B 型肝炎的先導研究 |
| [NCT00154869](https://clinicaltrials.gov/study/NCT00154869) | Phase 3 | 未知 | 320 | peginterferon alfa-2a 加 ribavirin 用於 C/B 型肝炎共同感染；開放標籤 |
| [NCT03759782](https://clinicaltrials.gov/study/NCT03759782) | Phase 3 | 未知 | 24 | 探討 ribavirin 的免疫調節作用，與 B 型肝炎核苷類似物併用的先導試驗 |
| [NCT00117533](https://clinicaltrials.gov/study/NCT00117533) | Phase 4 | 未知 | 20 | peginterferon alfa-2b 加 ribavirin 用於 B 型合併 D 型肝炎的先導研究 |

## 文獻證據

多數文獻為 B 型與 C 型肝炎的綜述，未見以 ribavirin 治療 B 型肝炎的隨機對照試驗。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32664198](https://pubmed.ncbi.nlm.nih.gov/32664198/) | 2020 | Review | Viruses | HCV/HBV 共同感染；HCV RNA 陽性者過去建議 peginterferon 加 ribavirin |
| [24659886](https://pubmed.ncbi.nlm.nih.gov/24659886/) | 2014 | Review | World J Gastroenterol | HCV/HBV 雙重感染的治療與預後更新 |
| [11160766](https://pubmed.ncbi.nlm.nih.gov/11160766/) | 2001 | Review | Annu Rev Med | 慢性 B 型與 C 型肝炎目前治療策略 |
| [16838649](https://pubmed.ncbi.nlm.nih.gov/16838649/) | 2006 | Review | Nihon Rinsho | HCV-HBV 感染；C 型肝炎以 peginterferon alpha-2b 加 ribavirin 療效最佳 |
| [25048716](https://pubmed.ncbi.nlm.nih.gov/25048716/) | 2015 | Review | Hepatology | B 型與 C 型肝炎抗病毒治療的免疫學層面 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-37449 | ROBAVIN CAP 100MG | 未載明 | 未載明 |

此為單一成分製劑，狀態為有效。

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）：** 慢性阻塞性肺病、氣喘、肝硬化、鐮刀型貧血、溶血性貧血、貧血、全血球減少、心肌梗塞、冠狀動脈疾病、間質性肺病、腎功能不全、自體免疫性肝炎、胰臟炎、類肉瘤病等。
- **藥物交互作用：** 資料庫查得 100 筆，等級多為未知，例如 calcitriol、pantoprazole、glimepiride、mesalazine、doxycycline、metformin、omeprazole、prednisone 等。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 唯一直接、已完成的 B 型肝炎 Phase 3 試驗為合併 peginterferon 的療法，無法判斷 ribavirin 的單獨貢獻；其餘試驗多為 C 型肝炎，ribavirin 僅是背景用藥。
- 安全性資料不足，且知識圖譜顯示多項禁忌關聯（尤其貧血與心肺疾病）。

**若要推進需要：**
- 取得 NCT00114361 的完整結果，評估 ribavirin 相對於 peginterferon 單用的增益。
- 補齊香港仿單的警語、禁忌症與核准適應症。
- 補充作用機轉資料，釐清 ribavirin 對 B 型肝炎的免疫調節假說。
- 追蹤 NCT03759782 的結果，並考慮設計 ribavirin 併用核苷類似物的對照試驗。

**其他預測適應症（肝門脈硬化、原發性門靜脈血栓、肝肺症候群、早發家族性非肝硬化性門脈高壓、肝性卟啉症、IgG4 相關肥厚性腦膜炎、嗜酸性血管中心性纖維化、IgG4 相關縱隔炎）：** 均缺乏支持其療效的研究，證據等級皆為 L5，建議 Hold。肝性卟啉症的文獻多為 ribavirin 合併療法期間誘發卟啉症的個案報告，並非療效證據。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

