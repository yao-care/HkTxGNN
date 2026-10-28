---
layout: default
title: Doravirine
parent: 僅模型預測 (L5)
nav_order: 293
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Doravirine：預測新適應症為猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)（證據等級 L4）。原適應症：HIV 感染、愛滋病"
monitor_inn: "DORAVIRINE"
predicted_indications: ["simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Doravirine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Doravirine：從 HIV 感染到猿猴免疫缺陷病毒感染
{: .text-alpha }

## 一句話總結

Doravirine 是一種非核苷類逆轉錄酶抑制劑，原本用於治療 HIV 感染與愛滋病。
TxGNN 模型預測它可能對**猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇間接相關文獻**，證據相當薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染、愛滋病 |
| 預測新適應症 | 猿猴免疫缺陷病毒感染 (Simian Immunodeficiency Virus Infection) |
| TxGNN 預測分數 | 0.9993 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Doravirine 屬於非核苷類逆轉錄酶抑制劑（NNRTI），已核准用於 HIV-1 感染。SIV 與 HIV 同屬慢病毒，都依賴逆轉錄酶複製，因此從機轉上抑制逆轉錄酶有一定的理論合理性。

不過需要留意幾點限制：
- NNRTI 對 HIV-2 及部分 SIV 株的活性普遍有限。
- 本次沒有任何 doravirine 針對 SIV 的資料。
- 高分預測很可能只是反映它與原本 HIV 適應症的高度相似。
- SIV 是動物或研究模型疾病，並非人類臨床適應症。

另外，同一預測清單中還有兩項較低優先的預測：
- **貓後天免疫缺乏症候群 (FIV)**：證據等級 L5，無任何試驗或文獻，NNRTI 對 FIV 活性普遍不佳，屬獸醫領域。
- **伴隨共濟失調步態、無語言能力及皮質白質減少的神經發育障礙**：證據等級 L5，未找到合理機轉連結，高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31658118](https://pubmed.ncbi.nlm.nih.gov/31658118/) | 2020 | Review | Current Opinion in HIV and AIDS | 探討 islatravir（另一種逆轉錄酶移位抑制劑）在 HIV-1 治療與預防的角色；並非 doravirine 或 SIV 的直接證據 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66558 | PIFELTRO TABLETS 100MG | 錠劑 | 請參考原廠仿單 |
| HK-66557 | DELSTRIGO TABLETS | 錠劑 | 請參考原廠仿單 |

兩張許可證均為單一成分、有效，持有者為 Merck Sharp & Dohme (Asia) Ltd。

---

## 安全性考量

- **藥物交互作用**：資料庫共收錄 59 筆交互作用，以下為其中較重要者：
  - **主要 (Major)**：Dexamethasone、Lumacaftor
  - **中度 (Moderate)**：Glycerol phenylbutyrate、Metreleptin、Troglitazone、Deferasirox、Praziquantel、Griseofulvin
  - 其餘多為輕微 (Minor) 等級，例如 Aprepitant、Cimetidine、Clarithromycin、Fluconazole 等。

其他警語與禁忌症資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測的新適應症為動物或研究模型疾病，不是人類臨床適應症，且缺乏 doravirine 專屬的 SIV 研究。
- 唯一的文獻是關於另一種藥物的綜述，證據等級僅為 L4，其餘預測則為 L5。

**若要推進需要：**
- 補齊詳細的作用機轉資料，並確認 doravirine 對 SIV 株的體外活性。
- 進行前臨床（體外或動物模型）研究，驗證抗 SIV 效果。
- 釐清此預測是否有研究或轉譯價值；若無，建議把資源放在 HIV 領域內的相關用途。
- 取得香港衛生署核准仿單，補足警語與禁忌症。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

