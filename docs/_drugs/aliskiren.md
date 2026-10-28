---
layout: default
title: Aliskiren
parent: 僅模型預測 (L5)
nav_order: 38
evidence_level: L5
indication_count: 6
monitor_inn: "ALISKIREN"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome", "chronic pulmonary heart disease", "cerebrovascular disorder"]
last_modified_at: 2026-10-28
description: "Aliskiren：預測新適應症為肺疾病及／或缺氧所致肺動脈高壓（證據等級 L5）。原適應症：高血壓"
---

# Aliskiren
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

## Aliskiren：肺疾病及（或）缺氧所致肺高壓
{: .text-alpha }

## 一句話總結

Aliskiren 是一種直接腎素抑制劑，原本用於高血壓治療（此為知識圖譜中記錄的原適應症）。
TxGNN 模型預測它可能對**肺疾病及／或缺氧所致肺動脈高壓 (pulmonary hypertension owing to lung disease and/or hypoxia)** 有效，
但目前**沒有臨床試驗**，僅有 **4 篇**間接的前臨床或機轉文獻，且沒有一篇直接研究此疾病，因此屬於模型預測階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓（來自知識圖譜記錄；本地許可證未載明適應症文字） |
| 預測新適應症 | 肺疾病及／或缺氧所致肺動脈高壓 |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5（僅有模型預測，無直接研究此疾病的試驗或文獻） |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Aliskiren 屬於直接腎素抑制劑，抑制腎素-血管張力素系統 (RAS) 的第一個限速步驟，在高血壓的降壓作用已為人所知。

在前臨床研究中，血管張力素 II 與間歇性缺氧引起的交感神經興奮、心房重塑有關，因此阻斷 RAS 在缺氧相關的肺血管疾病上，生物學上有其合理性。不過，目前取得的研究都是大鼠或體外實驗，探討的是間歇性缺氧及其下游效應（例如心房重塑），並非病人的肺動脈高壓。

0.9998 的 TxGNN 分數只是計算預測，不能視為療效證據。同一預測清單中另有「機轉不明的多因素肺動脈高壓」（同分、無任何證據），顯示分數可能反映與其他肺動脈高壓分類的相似性。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下文獻皆為前臨床或機轉研究，並未直接研究肺動脈高壓。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [32982180](https://pubmed.ncbi.nlm.nih.gov/32982180/) | 2020 | 前臨床（大鼠） | Drug Des Devel Ther | 探討 aliskiren 對慢性間歇性缺氧大鼠心房重塑的潛在作用 |
| [29645283](https://pubmed.ncbi.nlm.nih.gov/29645283/) | 2018 | 前臨床（大鼠） | J Physiol | 間歇性缺氧後的交感神經興奮由循環血管張力素 II 經頸動脈體與穹窿下器官所介導 |
| [39133776](https://pubmed.ncbi.nlm.nih.gov/39133776/) | 2024 | 前臨床（體外） | Am J Physiol Regul Integr Comp Physiol | 於終板血管器官檢測腦部血管張力素 II 的自發與誘發釋放 |
| [26502369](https://pubmed.ncbi.nlm.nih.gov/26502369/) | 2016 | 前臨床／機轉 | Transplantation | 鈣調神經磷酸酶抑制劑使腎集合管局部腎素上調，進而增加 VEGF 生成 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-60309 | RASILEZ TAB 150MG (ITALY) | 未載明 | 未載明 |
| HK-60310 | RASILEZ TAB 300MG (ITALY) | 未載明 | 未載明 |

兩張許可證皆為單一成分製劑，持證商為 Lee's Pharmaceutical (H.K) Limited。

## 安全性考量

- **知識圖譜記錄的禁忌疾病**（來自知識圖譜關聯，非仿單文字）：肝衰竭、肝病、胰臟炎、膽囊疾病、血管性水腫（含遺傳性、後天性及 RAS 阻斷劑誘發）、全身性紅斑性狼瘡、缺鉀、糖尿病及糖尿病酮酸中毒、嗜中性白血球低下、低血壓、副甲狀腺功能亢進、肝性腦病變、無尿、痛風、高血鈣、腎鈣質沉著症、腎動脈阻塞、腎功能不全等。
- **藥物交互作用**：資料庫共記錄 100 筆，列出的皆為中度，例如皮質類固醇（hydrocortisone、dexamethasone、prednisone 等）、鉀補充劑（氯化鉀、檸檬酸鉀等）、SGLT2 抑制劑（canagliflozin、dapagliflozin、empagliflozin 等）、aspirin、clarithromycin、aprepitant 等。
- **相關臨床試驗訊號**：ALTITUDE 試驗中，於第 2 型糖尿病患者在 ACEi／ARB 之外加用 aliskiren，未見心血管或腎臟獲益，且不良事件增加（包含高血鉀、腎臟不良事件）。聯合使用 RAS 阻斷劑須特別謹慎。

仿單的警語與禁忌資料目前缺乏，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，也沒有直接研究此疾病的文獻，證據等級僅為 L5，高預測分數不足以支持推進。
- 前臨床研究僅涉及間歇性缺氧的下游效應，且 RAS 阻斷劑聯用有已知安全疑慮。

**若要推進需要：**
- 在肺動脈高壓動物模型（如缺氧誘發）中直接測試 aliskiren
- 取得作用機轉與香港仿單的警語、禁忌資料
- 釐清此族群中 aliskiren 對肺血管阻力、右心功能的影響及低血壓、高血鉀風險
- 若有後續臨床探索，設計小規模概念驗證研究，並避免與 ACEi／ARB 合併使用

## 其他預測適應症簡述

以下為同一份預測清單中的其他項目，證據皆不足以支持推進：

| 預測適應症 | TxGNN 分數 | 證據等級 | 說明 |
|-----------|-----------|---------|------|
| 機轉不明的多因素肺動脈高壓 | 0.9998 | L5 | 無試驗與文獻 |
| 惡性高血壓腎病 | 0.9998 | L5 | 僅 1 篇間接前臨床文獻（C3aR 拮抗劑，非 aliskiren） |
| Braddock 症候群 | 0.9997 | L5 | 無證據 |
| 慢性肺心病 | 0.9978 | L5 | 僅 1 篇 2007 年會議試驗回顧，間接相關 |
| 腦血管疾病 | 0.9919 | 依規則為 L5 | 有 1 個提前終止的動脈粥狀硬化 MRI 試驗 (NCT01417104，71 人) 及多篇前臨床中風研究，但均非直接以腦血管疾病為對象的研究，且 ALTITUDE 提示聯用風險 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

