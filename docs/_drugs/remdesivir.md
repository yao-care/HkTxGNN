---
layout: default
title: Remdesivir
parent: 僅模型預測 (L5)
nav_order: 764
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
monitor_inn: "Remdesivir"
predicted_indications: ["multiple endocrine neoplasia", "HIV infectious disease", "feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "homozygous familial hypercholesterolemia"]
description: "Remdesivir：預測新適應症為多發性內分泌腫瘤 (multiple endocrine neoplasia)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Remdesivir
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

## Remdesivir: 多發性內分泌腫瘤 (multiple endocrine neoplasia)
{: .text-alpha }

## 一句話總結

Remdesivir 是一種核苷酸類似物前驅藥，為抗病毒藥物，在香港以 VEKLURY 品名上市，但目前整理的資料中沒有記載其核准適應症。
TxGNN 模型預測它可能對**多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)** 有效，分數很高，但**沒有任何臨床試驗或文獻**支持，且機轉上找不到合理關聯，較可能是模型的假象。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 多發性內分泌腫瘤 (multiple endocrine neoplasia) |
| TxGNN 預測分數 | 0.9950 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Remdesivir 是核苷酸類似物前驅藥，作用在病毒的 RNA 依賴性 RNA 聚合酶 (RdRp)，抑制病毒 RNA 複製。

多發性內分泌腫瘤是遺傳性腫瘤症候群（例如 MEN1、RET 基因突變），致病原因與病毒無關，Remdesivir 在其中沒有已知的作用標的。因此**目前找不到合理的機轉關聯**。這個高分預測的分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據，沒有研究佐證，很可能是模型假象。

**其他預測適應症的簡要觀察：**
- **HIV 感染（排名 2，分數 0.9932）**：證據最多，但文獻幾乎都在談 COVID-19，唯一的試驗 (NCT04385719) 是藥物動力學研究，並非 HIV 療效試驗。HIV 使用逆轉錄酶，Remdesivir 沒有已確立的抗 HIV 活性。
- CMV 是 DNA 病毒，直接抗病毒活性在機轉上不太可能。
- 其餘預測（貓免疫缺乏症候群、猴免疫缺乏病毒感染、同型合子家族性高膽固醇血症、變異型心絞痛、痲瘋病、第 2 型抗凝血酶缺乏等）均無臨床證據，也無合理機轉。

---

## 臨床試驗證據

針對首要預測（多發性內分泌腫瘤），目前無相關臨床試驗登記。

---

## 文獻證據

針對首要預測（多發性內分泌腫瘤），目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66766 | VEKLURY POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 100MG | 輸注濃縮液用粉劑（依品名） | 資料未載明 |

製造商：Gilead Sciences Hong Kong Limited（單一成分、有效）。

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用，以下為部分中度（Moderate）等級的藥物：Acarbose、Doxycycline、Pioglitazone、Amphotericin B、Bupropion、Mesalazine、Clarithromycin、Minocycline、Tetracycline、Vancomycin、Levofloxacin、Neomycin 等。

警語與禁忌症資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測沒有任何臨床試驗或文獻，機轉上也無關聯，屬於僅有模型預測的 L5 等級。
- 即使是證據較多的 HIV 與 CMV，現有資料也只顯示 COVID-19 相關研究，並不支持 Remdesivir 對這些疾病有效。

**若要推進需要：**
- 補齊香港仿單中的核准適應症、警語與禁忌症
- 補充詳細的作用機轉（MOA）資料
- 若仍想探索，先做前臨床或體外實驗，驗證是否存在任何合理的生物學連結
- 優先重新審視與病毒感染相關的預測（如 HIV、CMV），並以直接療效研究而非共病或藥動學研究作為依據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

