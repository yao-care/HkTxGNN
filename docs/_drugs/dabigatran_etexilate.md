---
layout: default
title: Dabigatran Etexilate
parent: 僅模型預測 (L5)
nav_order: 241
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Dabigatran Etexilate：預測新適應症為硬化性膽管炎 (Sclerosing Cholangitis)（證據等級 L5）。原適應症：香港許可證資料未載明核准適應症"
monitor_inn: "DABIGATRAN ETEXILATE"
predicted_indications: ["sclerosing cholangitis", "obsolete familial combined hyperlipidemia", "hypoalphalipoproteinemia", "homozygous familial hypercholesterolemia", "primary release disorder of platelets"]
---

# Dabigatran Etexilate
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

## Dabigatran Etexilate：從（原適應症未登載）到硬化性膽管炎
{: .text-alpha }

## 一句話總結

Dabigatran etexilate 是口服直接凝血酶抑制劑（抗凝血劑），香港已有多張許可證上市。
TxGNN 模型預測它可能對**硬化性膽管炎 (Sclerosing Cholangitis)** 有效，但目前**沒有任何臨床試驗**，僅有 **1 篇間接相關文獻**（為其他藥物的交互作用研究），證據僅停留在模型預測層級。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症 |
| 預測新適應症 | 硬化性膽管炎 (Sclerosing Cholangitis) |
| TxGNN 預測分數 | 0.9982 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 許可證數 | 6 張（有效 6 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，dabigatran 是直接凝血酶（thrombin）抑制劑，屬於口服抗凝血劑。

從機轉推測，凝血酶／PAR-1 訊號與肝臟纖維化及發炎有關，理論上可能與膽管病變的纖維化過程有所關聯。不過這只是推論，目前沒有直接證據支持。

TxGNN 的高分（0.9982）僅是計算預測。唯一連結的文獻是另一個藥物（cilofexor）的藥物交互作用評估，並非 dabigatran 在硬化性膽管炎的療效研究。

其他排名較前的預測（家族性複合型高脂血症、低 α 脂蛋白血症、同合子家族性高膽固醇血症、血小板原發性釋放障礙）在機轉上的連結更弱，且部分疾病術語已過時；其分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [36906733](https://pubmed.ncbi.nlm.nih.gov/36906733/) | 2023 | 其他（藥物交互作用／藥理評估） | Clinical Pharmacokinetics | 評估 FXR 促效劑 cilofexor（開發用於 NASH 與原發性硬化性膽管炎）的 CYP450 與轉運蛋白交互作用；並非 dabigatran 的療效研究，僅屬間接相關 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-57315 | PRADAXA CAP 110MG | 膠囊（資料未載明） | 資料未載明 |
| HK-60516 | PRADAXA CAP 150MG | 膠囊（資料未載明） | 資料未載明 |
| HK-57316 | PRADAXA CAP 75MG | 膠囊（資料未載明） | 資料未載明 |
| HK-68583 | DABIGATRAN ETEXILATE SANDOZ CAPSULES 110MG | 膠囊（資料未載明） | 資料未載明 |
| HK-68584 | DABIGATRAN ETEXILATE SANDOZ CAPSULES 150MG | 膠囊（資料未載明） | 資料未載明 |

另有 HK-68585（SANDOZ 75MG），共 6 張有效許可證，均為單一成分製劑。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自 TxGNN 知識圖譜，非仿單內容）：凝血功能障礙、貧血、大球性貧血、腦內出血。作為抗凝血劑，出血風險是核心顧慮，尤其對於預測的新適應症中屬出血型缺陷的族群（如血小板釋放障礙）需格外謹慎。

其他警語、禁忌症與藥物交互作用資料目前缺乏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測皆僅有模型分數支持，沒有針對 dabigatran 的臨床試驗，唯一相關文獻也屬間接證據（證據等級 L5）。
- 機轉連結薄弱，且 dabigatran 本身有出血風險，部分預測方向（如血小板功能障礙）的獲益方向存疑。

**若要推進需要：**
- 補充詳細的作用機轉資料，並釐清凝血酶／PAR-1 訊號在膽管纖維化中的角色
- 進行前臨床研究（如膽管炎動物模型）驗證療效
- 取得香港許可證的核准適應症與仿單警語、禁忌症
- 評估肝功能受損或膽管疾病族群的出血風險與安全性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

