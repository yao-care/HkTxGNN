---
layout: default
title: Human Immunoglobulin G
parent: 僅模型預測 (L5)
nav_order: 374
evidence_level: L5
indication_count: 10
---

# Human Immunoglobulin G
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Human Immunoglobulin G (IVIG)：從免疫缺乏症到嚴重非增殖性糖尿病視網膜病變

## 一句話總結

Human Immunoglobulin G（靜脈注射免疫球蛋白，IVIG）是由人類血漿萃取的多克隆 IgG 製劑，臨床上廣泛用於原發性免疫缺乏症及多種自體免疫疾病。
TxGNN 模型預測它可能對**嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)** 有效，
目前有 **0 個臨床試驗**和 **1 篇文獻**支持這個方向，且該文獻屬生物標記研究而非治療研究。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 原發性免疫缺乏症、自體免疫疾病（本 Pack 無正式資料登錄） |
| 預測新適應症 | 嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy) |
| TxGNN 預測分數 | 99.75% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 欄位未收錄）。根據已知藥理，IVIG 的主要抗發炎機轉包括：Fc 受體封鎖（阻斷巨噬細胞及 NK 細胞的病理活化）、補體抑制（透過 IgG Fc 端競爭性結合 C1q）、以及調節細胞激素環境。

糖尿病視網膜病變的病理核心之一是低度慢性發炎：視網膜微血管內皮損傷、周細胞凋亡、以及補體活化介導的屏障破壞，理論上均為 IVIG 潛在介入切入點。此外，近年研究（PMID 40204274, 2025）指出嚴重非增殖性糖尿病視網膜病變患者體內 IgG Fc 端 N-醣基化（特別是半乳糖基化與唾液酸化）顯著異常，提示 IgG 的功能性修飾與疾病嚴重度分期相關。

然而，上述文獻屬於**診斷性生物標記研究**，並非 IVIG 治療的療效數據。IgG 糖基化異常代表的是疾病的生物標記，而非 IVIG 治療的依據。因此，TxGNN 高分（99.75%）很可能反映的是知識圖譜中 IgG-糖尿病視網膜病變節點的拓撲相關性，而非直接療效信號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|------|------|------|---------|
| [40204274](https://pubmed.ncbi.nlm.nih.gov/40204274/) | 2025 | Observational/Biomarker | Molecular & Cellular Proteomics | 探討血清疾病特異性 IgG Fc N-醣基化作為非增殖性與增殖性糖尿病視網膜病變診斷生物標記（160 名患者分三組），非 IVIG 治療研究 |

---

## 香港上市資訊

Human Immunoglobulin G 在香港目前**未取得上市許可**（許可證數：0），無核准適應症資料。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
現有證據僅有 1 篇生物標記研究（非療效研究），完全無臨床試驗支持 IVIG 用於嚴重非增殖性糖尿病視網膜病變，且本藥在香港無任何上市許可，屬 L5 最低證據等級，尚不具備進入臨床評估的條件。

**若要推進需要：**
- 確認 IVIG 用於糖尿病視網膜病變的直接療效前臨床或探索性臨床試驗（Phase 1/2）
- 補充完整的作用機轉（MOA）資料，建立合理的治療假說
- 獲取香港藥監局安全性核准資料（仿單警語、禁忌症）作為 S1 安全性初評依據
- 評估給藥途徑適配性（眼部適應症通常需要局部或玻璃體內給藥，IVIG 為靜脈注射劑型，需重新評估可行性）
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

