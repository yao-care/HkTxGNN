---
layout: default
title: Midodrine
parent: 僅模型預測 (L5)
nav_order: 586
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Midodrine"
predicted_indications: ["variably protease-sensitive prionopathy", "faciodigitogenital syndrome", "attention deficit-hyperactivity disorder", "hypotensive disorder", "attention deficit hyperactivity disorder, inattentive type", "sinoatrial node disease", "monogenic obesity", "specific developmental disorder", "obsolete hypertelorism (disease)", "sinoatrial block"]
description: "Midodrine：預測新適應症為Variably protease-sensitive prionopathy（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Midodrine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Midodrine: Variably protease-sensitive prionopathy
{: .text-alpha }

## 一句話總結

Midodrine 是一種周邊 α1 腎上腺素受體促效劑，原本用於姿位性（直立性）低血壓、多系統萎縮及姿勢性心搏過速症候群相關症狀。
TxGNN 模型預測分數最高的新適應症是**朊病毒相關疾病 (variably protease-sensitive prionopathy)**，但該預測沒有任何臨床試驗或文獻支持。
本報告改以證據最充分的**低血壓性疾患 (Hypotensive disorder)** 為主要評估對象，目前有 **1 個臨床試驗**和 **19 篇文獻**，但此適應症與現有用途高度重疊，並非真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Variably protease-sensitive prionopathy |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5（低血壓性疾患）；L5（排名第 1 的預測） |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Proceed with Guardrails（低血壓性疾患）；其他預測為 Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Midodrine 是前驅藥，其活性代謝物 desglymidodrine 會刺激小動脈與靜脈上的 α1 受體，增加血管張力並提升血壓。因此它直接針對低血壓狀態，包括神經性姿位性低血壓。

低血壓性疾患與藥物既有的姿位性低血壓適應症在病理生理上高度重疊，所以模型給出高分並不意外。需要強調的是，這個預測大致只是重述現有用途，**不能算真正的藥物再利用發現**。

其他高分預測則缺乏合理依據：
- **朊病毒相關疾病、Aarskog-Scott 症候群（faciodigitogenital syndrome）、單基因肥胖、已廢棄的 hypertelorism 條目**：機轉上沒有關聯；這些分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據。
- **注意力不足過動症（ADHD）**：Midodrine 是周邊 α1 促效劑，中樞神經穿透有限，與 guanfacine 等 α2 促效劑不同。僅有的 1 篇文獻是日本直立調節障礙的描述性研究，不能證明對 ADHD 有效。
- **竇房結疾病、竇房傳導阻滯**：Midodrine 可能造成反射性心搏過緩，在這類患者身上更像是安全警訊，而非治療機會。

---

## 臨床試驗證據

（低血壓性疾患）

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02893553](https://clinicaltrials.gov/study/NCT02893553) | Phase 2 | 完成 | 21 | 探討將脊髓損傷低血壓患者的血壓恢復正常後，對腦血流的影響；樣本小、族群特定，結果外推性有限 |

其他 9 項預測（含朊病毒相關疾病、ADHD 等）目前無相關臨床試驗登記。

---

## 文獻證據

（低血壓性疾患，依類型與相關性挑選）

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25644760](https://pubmed.ncbi.nlm.nih.gov/25644760/) | 2015 | RCT | Hepatology | 比較 terlipressin＋白蛋白與 midodrine＋octreotide＋白蛋白治療肝腎症候群 |
| [38123372](https://pubmed.ncbi.nlm.nih.gov/38123372/) | 2024 | Review | Revue Neurologique | 姿位性低血壓的回顧與專家立場聲明 |
| [38205630](https://pubmed.ncbi.nlm.nih.gov/38205630/) | 2024 | Review（科學聲明） | Hypertension | 美國心臟協會對高血壓成人合併姿位性低血壓的科學聲明 |
| [41941194](https://pubmed.ncbi.nlm.nih.gov/41941194/) | 2026 | Review | JAMA Internal Medicine | 姿位性低血壓的處置，指出常合併仰臥高血壓與餐後低血壓 |
| [28050656](https://pubmed.ncbi.nlm.nih.gov/28050656/) | 2017 | 共識建議 | Journal of Neurology | 神經性姿位性低血壓與相關仰臥高血壓的篩檢、診斷及治療共識 |
| [32979782](https://pubmed.ncbi.nlm.nih.gov/32979782/) | 2020 | Review | Autonomic Neuroscience | 姿位性低血壓的藥物治療 |
| [2480881](https://pubmed.ncbi.nlm.nih.gov/2480881/) | 1989 | Review | Drugs | Midodrine 的藥理特性及在姿位性低血壓與繼發性低血壓的治療應用 |
| [37978969](https://pubmed.ncbi.nlm.nih.gov/37978969/) | 2024 | Review（專家意見） | Gastroenterology | AGA 對肝硬化使用血管活性藥物與靜脈白蛋白的臨床實務更新 |
| [31996627](https://pubmed.ncbi.nlm.nih.gov/31996627/) | 2020 | Review | Continuum | 姿位性低血壓的處置，著重神經性類型 |
| [35029940](https://pubmed.ncbi.nlm.nih.gov/35029940/) | 2022 | Review | American Family Physician | 姿位性低血壓的實用處理方式 |

其他預測中，ADHD 與竇房結疾病各僅有 1 篇間接相關的觀察性研究（PMID 42351284、24634993），不足以支持療效。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68204 | MIDODRINE SUBSTIPHARM TABLETS 2.5MG | 未載明 | 未載明 |
| HK-68183 | MIDORINE TABLETS 2.5MG | 未載明 | 未載明 |
| HK-67094 | MIDODRINE HYDROCHLORIDE TABLETS USP 2.5MG | 未載明 | 未載明 |

三張許可證皆為單方、有效狀態。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：腎上腺嗜鉻細胞瘤、交感神經副神經節瘤、腎上腺癌、十二指腸癌、小腸癌、心臟癌、甲狀腺毒症、甲狀腺機能亢進、Graves 病。此資料來自知識圖譜，並非仿單內容，需對照原廠仿單確認。
- **藥物交互作用**：共記錄 81 筆，以下為已列出者的主要項目。
  - 中度：epinephrine、ephedrine、isometheptene、bupropion、lorcaserin、phentermine、diethylpropion、mazindol、sibutramine、trospium、rolapitant、glycerol phenylbutyrate（多為其他擬交感神經或血管收縮類藥物）
  - 輕度：ranitidine、cimetidine、metformin
- **臨床需留意的風險**（依機轉與預測分析）：仰臥高血壓、尿滯留、心搏過緩，尤其與其他血管收縮劑或抑制房室傳導／減慢心率的藥物併用時。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails（僅限低血壓性疾患）；其餘預測為 Hold**

**理由：**
- 低血壓性疾患有 1 個已完成的 Phase 2 試驗與多篇綜述支持，且機轉合理，但這大致等同現有適應症，不算新發現。
- 排名最高的朊病毒相關疾病及 ADHD、竇房結疾病等預測都沒有實質證據，部分更有安全疑慮，應維持 Hold。

**若要推進需要：**
- 取得香港衛生署核准仿單，釐清許可證的核准適應症、警語與禁忌症
- 補充作用機轉資料（MOA）
- 對低血壓性疾患，需有更大規模的對照試驗，並建立仰臥高血壓與心率的監測計畫
- 排除或重新審視 TxGNN 模型（深度學習）中明顯不合理的預測（如已廢棄的 hypertelorism 條目）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

