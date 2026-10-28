---
layout: default
title: Rifaximin
parent: 僅模型預測 (L5)
nav_order: 772
evidence_level: L5
indication_count: 6
monitor_inn: "RIFAXIMIN"
predicted_indications: ["oral candidiasis", "commissural lip fistula", "osteoradionecrosis of the mandible", "burning mouth syndrome", "oral leukoedema", "candidiasis"]
last_modified_at: 2026-10-28
description: "Rifaximin：預測新適應症為口腔念珠菌症 (oral candidiasis)（證據等級 L5）。原適應症：肝腦病變、肝昏迷"
---

# Rifaximin
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

## Rifaximin：從肝腦病變到口腔念珠菌症
{: .text-alpha }

## 一句話總結

Rifaximin 是一種幾乎不被腸道吸收的口服抗菌藥，知識圖譜中記錄的相關用途為肝腦病變與肝昏迷。
TxGNN 模型預測它可能對**口腔念珠菌症 (oral candidiasis)** 有效，但目前**沒有任何臨床試驗**，僅有 **1 篇相關文獻**，且該文獻顯示的訊號反而是使用 rifaximin 可能增加念珠菌感染風險。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肝腦病變、肝昏迷（知識圖譜中記錄的關聯；香港許可證未提供適應症文字） |
| 預測新適應症 | 口腔念珠菌症 (oral candidiasis) |
| TxGNN 預測分數 | 0.9975 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 rifaximin 是非吸收性的口服抗菌藥，作用集中在腸道，全身暴露極低，並沒有已知的直接抗真菌活性。

從臨床訊號來看，預測並不被支持。唯一相關文獻（PMID 34180023）是一項異體造血幹細胞移植患者的研究，結果指出使用 rifaximin 與對 micafungin 具抗藥性的念珠菌感染增加有關。這提示它可能透過改變腸道菌叢而促進念珠菌過度生長，而不是治療念珠菌。

因此，高 TxGNN 分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病間學到的相似性，而非生物學證據。臨床訊號甚至指向相反方向，有潛在的傷害風險。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34180023](https://pubmed.ncbi.nlm.nih.gov/34180023/) | 2021 | 世代研究 | Annals of Hematology | 異體造血幹細胞移植患者使用 rifaximin 預防腸道細菌感染，與對 micafungin 具抗藥性的念珠菌感染增加有關 |

此文獻研究的是移植患者的念珠菌感染，並非以 rifaximin 治療口腔念珠菌症，因此不構成直接支持該預測的證據。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61689 | XIFAXAN TAB 200MG | 未提供 | 未提供 |
| HK-64602 | REFERO TABLETS 550MG | 未提供 | 未提供 |

兩張許可證均為單方製劑，持有人為 CHONG LAP (HK) CO LTD，狀態皆為有效。

## 安全性考量

- **知識圖譜記錄的禁忌關聯（非仿單內容）**：艱難梭菌結腸炎 (Clostridium difficile colitis)、新生兒壞死性腸炎 (perinatal necrotizing enterocolitis)
- **藥物交互作用**：共查詢到 69 項交互作用，其中以下列舉部分：
  - 重度：霍亂活疫苗（Vibrio cholerae CVD 103-HgR strain live antigen）
  - 中度：Warfarin、Cyclosporine、Tolvaptan、Alpelisib、Apalutamide、Cabozantinib、Daclatasvir、Ledipasvir 等

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，唯一相關文獻顯示 rifaximin 可能與念珠菌感染風險上升有關，與預測方向相反。
- 沒有已知的抗真菌機轉，且研究並未直接探討 rifaximin 治療口腔念珠菌症，故證據等級僅為 L5。

**若要推進需要：**
- 取得 rifaximin 的作用機轉資料，並評估是否有任何抗真菌或黏膜局部作用的依據
- 釐清念珠菌風險訊號是藥物本身造成，還是受到原發疾病嚴重程度的干擾
- 取得香港原廠仿單，確認核准適應症、警語與禁忌症
- 在有直接研究支持前，不建議針對口腔念珠菌症進一步開發
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

