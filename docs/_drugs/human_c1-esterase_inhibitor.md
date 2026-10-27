---
layout: default
title: Human C1-Esterase Inhibitor
parent: 僅模型預測 (L5)
nav_order: 441
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Human C1-Esterase Inhibitor：預測新適應症為嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)（證據等級 L5）。原適應症：資料中未載明"
monitor_inn: "HUMAN C1-ESTERASE INHIBITOR"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "primary release disorder of platelets", "diabetic retinopathy", "pseudo-von Willebrand disease"]
---

# Human C1-Esterase Inhibitor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## 人類 C1 酯酶抑制劑：從（原適應症未載明）到嚴重非增殖性糖尿病視網膜病變
{: .text-alpha }

## 一句話總結

人類 C1 酯酶抑制劑（Human C1-Esterase Inhibitor）是一種血漿衍生蛋白質藥物，香港已有 1 張有效許可證，但本次整理的資料中未載明原適應症。
TxGNN 模型預測它可能對**嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)** 有效。
目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未載明 |
| 預測新適應症 | 嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 預測分數 | 99.61% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

其他排名較前的預測（皆為 L5、建議 Hold）：

| 排名 | 預測適應症 | TxGNN 分數 |
|------|-----------|-----------|
| 2 | 血小板釋放功能異常 (Primary Release Disorder of Platelets) | 99.31% |
| 3 | 糖尿病視網膜病變 (Diabetic Retinopathy) | 99.25% |
| 4 | 偽血管性血友病 (Pseudo-von Willebrand Disease) | 99.09% |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。C1 酯酶抑制劑已知可調控激肽釋放酶–緩激肽系統與補體系統，並抑制 XIIa 因子、激肽釋放酶與纖溶酶等蛋白酶。

血漿激肽釋放酶與緩激肽訊號，被認為與糖尿病視網膜病變中的血管通透性增加及視網膜血管功能異常有關。因此推測 C1 酯酶抑制劑可能透過調節這些路徑，減少視網膜血管滲漏與發炎。

這**僅是未經驗證的假說**，需要前臨床與機轉研究確認。此外，本藥為靜脈注射的血漿衍生蛋白質，要送達眼部有實務上的挑戰，血漿衍生生物製劑的成本與供應也是疑慮。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67361 | BERINERT POWDER AND SOLVENT FOR SOLUTION FOR INJECTION/INFUSION 500IU（CSL Behring Asia Pacific Limited） | 未載明 | 未載明 |

## 安全性考量

- **藥物交互作用**：已查詢到 41 筆交互作用。以下為部分列示（資料來源 DDInter）：
  - **嚴重 (Major)**：Carfilzomib
  - **中度 (Moderate)**：
    - 雄性素類：Oxandrolone、Oxymetholone、Stanozolol、Testosterone、Danazol
    - 雌激素類：Ethinylestradiol、Estradiol、Conjugated estrogens、Esterified estrogens、Diethylstilbestrol
    - 溶栓劑：Alteplase、Anistreplase
    - 紅血球生成刺激劑：Darbepoetin alfa、Erythropoietin
- **預測適應症相關的潛在顧慮**：本藥抑制凝血路徑中的蛋白酶，若用於出血性疾病（如血小板釋放功能異常、偽血管性血友病），需評估血栓或止血方面的風險。此為推論，並非仿單警語。

主要警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 只有 TxGNN 預測分數（99.61%），沒有臨床試驗、文獻或機轉資料，證據等級為 L5。
- 原適應症、作用機轉及仿單安全性資訊皆缺乏，目前無法進行安全性篩選。靜脈給藥對眼部疾病的可行性也存疑。

**若要推進需要：**
- 取得香港衛生署仿單，確認核准適應症、警語與禁忌症。
- 補充 DrugBank 的作用機轉資料，釐清 C1 酯酶抑制劑與視網膜血管病變的機轉連結。
- 進行文獻回顧與前臨床研究（如激肽釋放酶–緩激肽路徑在糖尿病視網膜病變動物模型中的作用）。
- 評估全身性給藥到達視網膜的可行性、劑量，以及成本與供應。
- 評估血栓與止血相關的安全性。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

