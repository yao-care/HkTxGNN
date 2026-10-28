---
layout: default
title: Uracil
parent: 僅模型預測 (L5)
nav_order: 918
evidence_level: L5
indication_count: 10
monitor_inn: "Uracil"
predicted_indications: ["colonic neoplasm", "gastric carcinoma", "rectosigmoid junction neoplasm", "lipoma of colon", "colonic lymphangioma", "cecum villous adenoma", "cecum neuroendocrine tumor G1", "cavernous hemangioma of colon", "cecal disease", "colon leiomyoma"]
last_modified_at: 2026-10-28
description: "Uracil：預測新適應症為大腸腫瘤（證據等級 L5）。原適應症：許可證資料未載明"
---

# Uracil
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

## Uracil：從許可證未載明的原適應症，到大腸腫瘤
{: .text-alpha }

## 一句話總結

Uracil（尿嘧啶）在香港有 2 張單一成分許可證，但本報告彙整的許可證資料未載明原核准適應症。
TxGNN 模型預測它可能對**大腸腫瘤**有效，預測分數 0.9950。
目前有 1 個相關臨床試驗登記和 20 篇文獻，但臨床試驗並未測試 uracil。
文獻中的療效證據來自 **tegafur-uracil 複方（UFT）**，不是 uracil 單方。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 大腸腫瘤 |
| TxGNN 預測分數 | 0.9950 |
| 證據等級 | L5（證據來自 UFT 複方，非 uracil 單方） |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏 uracil 本身詳細的作用機轉資料。根據已知資訊，uracil 是口服氟嘧啶複方 UFT（tegafur-uracil）的搭配成分。Tegafur 是 5-FU 的前驅藥，uracil 則競爭性抑制二氫嘧啶去氫酶（DPD）。DPD 負責分解 5-FU，抑制它可減緩 5-FU 代謝，提高腫瘤組織中的 5-FU 濃度。

這是 UFT 用於大腸直腸癌的藥理基礎，與 TxGNN 的預測方向一致。不過 uracil 單獨使用時不是主要的抗癌成分。已有的療效證據屬於 tegafur 與 uracil 的組合，不能直接視為 uracil 單方的療效。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT04164069](https://clinicaltrials.gov/study/NCT04164069) | Phase 1 | 完成 | 9 | 以 dasatinib 預防 FOLFOX 化療引起的周邊神經病變，屬支持性照護研究，未測試 uracil |

此試驗與 uracil 的療效無直接關聯，不能作為支持證據。

---

## 文獻證據

下表所列研究的受試者多數使用 UFT 複方（tegafur + uracil），而非 uracil 單方。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [29677641](https://pubmed.ncbi.nlm.nih.gov/29677641/) | 2018 | RCT | Eur J Cancer | SACURA 試驗：比較第 II 期結腸癌術後 1 年口服 UFT 輔助化療與單純手術 |
| [31917122](https://pubmed.ncbi.nlm.nih.gov/31917122/) | 2020 | 隨機 Phase III | Clin Colorectal Cancer | ACTS-CC 02：高風險第 III 期結腸癌，比較 S-1 加 oxaliplatin 與 UFT/LV 輔助化療 |
| [33714860](https://pubmed.ncbi.nlm.nih.gov/33714860/) | 2021 | Phase III 追蹤分析 | ESMO Open | ACTS-CC 02 的 5 年存活更新：SOX 在無病存活期上未優於 UFT/LV |
| [33950962](https://pubmed.ncbi.nlm.nih.gov/33950962/) | 2021 | 世代研究與統合分析 | Medicine | 台灣第 II、III 期結腸癌術後輔助化療，比較 UFT 與 5-FU |
| [15108041](https://pubmed.ncbi.nlm.nih.gov/15108041/) | 2004 | 隨機對照試驗 | Int J Clin Oncol | 大腸直腸癌輔助免疫化療，比較 OK-432 與口服嘧啶類（HCFU、UFT）的不同組合 |
| [17952521](https://pubmed.ncbi.nlm.nih.gov/17952521/) | 2007 | Review | Surg Today | UFT 作為肺、胃、大腸、乳房癌術後輔助化療的臨床證據與機轉 |
| [25209093](https://pubmed.ncbi.nlm.nih.gov/25209093/) | 2014 | Review | Clin Colorectal Cancer | 亞洲轉移性大腸直腸癌治療指引共識 |
| [16111469](https://pubmed.ncbi.nlm.nih.gov/16111469/) | 2005 | Review | Expert Rev Anticancer Ther | 結腸癌各分期的化療選項 |
| [12174936](https://pubmed.ncbi.nlm.nih.gov/12174936/) | 2002 | 回顧 | Anticancer Res | 回顧美、歐、日大腸直腸癌輔助化療的發展 |
| [11320674](https://pubmed.ncbi.nlm.nih.gov/11320674/) | 2001 | Case report | Cancer Chemother Pharmacol | 轉移性結腸癌患者使用 UFT 後出現溶血性貧血 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-48265 | UNITORAL CAP | 未載明 | 未載明 |
| HK-60904 | UFUR CAP | 未載明 | 未載明 |

兩張許可證目前皆為有效狀態，均登記為單一成分產品。本次彙整的資料未包含核准適應症文字，因此無法確認原適應症。

---

## 安全性考量

安全性資訊請參考原廠仿單。

文獻中有一例值得注意的訊號：一名轉移性結腸癌患者使用 UFT 後出現溶血性貧血（個案報告，PMID 11320674）。此為單一個案，且針對複方，僅供監測參考。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 多項針對結腸癌的 Phase III RCT 以 UFT 作為治療組或對照組，機轉（抑制 DPD 以增強 5-FU）也合理，因此大腸腫瘤方向有一定支持。
- 但這些證據屬於 tegafur-uracil 複方，而非 uracil 單方。現有臨床試驗登記未測試 uracil，仿單的警語與禁忌資料也有缺口，因此須以限制條件推進。

**若要推進需要：**
- 釐清兩張香港許可證的實際成分、劑型與核准適應症，並取得仿單。
- 明確評估對象是 UFT 複方還是 uracil 單方，不要把複方的療效套用到單方。
- 補充 uracil 的作用機轉資料（DrugBank）。
- 建立血液學與溶血等不良反應的監測計畫。

**其他預測適應症：** 胃癌的證據也達 L2，同樣來自 UFT 複方的 Phase II 研究與一項 Phase 3 RCT（SAMIT），可作為次要方向。直腸乙狀結腸交界腫瘤、盲腸疾病等其他預測缺乏直接證據，建議 Hold。結腸脂肪瘤、淋巴管瘤、絨毛腺瘤等良性病變目前僅有模型預測，無任何研究支持。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

