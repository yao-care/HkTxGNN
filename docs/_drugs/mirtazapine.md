---
layout: default
title: Mirtazapine
parent: 僅模型預測 (L5)
nav_order: 582
evidence_level: L5
indication_count: 3
---

# Mirtazapine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Mirtazapine：從憂鬱症到 Ohdo 症候群及其變異型

## 一句話總結

Mirtazapine 是一種抗憂鬱藥，在香港已有多張上市許可證。
TxGNN 模型預測它可能對 **Ohdo 症候群及其變異型 (Ohdo syndrome and variants)** 有效。
目前**沒有任何臨床試驗或文獻**支持這個預測，僅有模型分數。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明適應症文字（Mirtazapine 屬抗憂鬱藥，一般用於憂鬱症） |
| 預測新適應症 | Ohdo 症候群及其變異型 (Ohdo syndrome and variants) |
| TxGNN 預測分數 | 99.42% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Mirtazapine 已知的藥理作用包括 alpha-2 受體拮抗，以及 5-HT2、5-HT3 和 H1 受體阻斷。這些作用與 Ohdo 症候群沒有明顯的關聯。

Ohdo 症候群（KAT6B 相關）是一種罕見的先天性神經發展疾病，成因是染色質修飾蛋白功能異常。從現有資料看，Mirtazapine 的作用路徑與這個致病機轉之間**無法建立機轉上的連結**。

TxGNN 的 0.994 分是知識圖譜推算的結果，沒有試驗或文獻佐證，只能視為假說。

**其他預測適應症（同樣僅有模型預測）：**

| 排名 | 預測疾病 | TxGNN 分數 | 證據等級 | 備註 |
|------|---------|-----------|---------|------|
| 2 | Blepharophimosis - intellectual disability syndrome, Ohdo type | 99.11% | L5 | 與第 1 名屬同一疾病家族，不能算獨立的佐證 |
| 3 | 嬰兒良性陣發性斜頸 (Benign paroxysmal torticollis of infancy) | 99.11% | L5 | 此病被視為偏頭痛相關或離子通道相關的陣發性疾病，血清素或抗組織胺藥物偶爾被用於偏頭痛預防，因此僅有推測性的關聯。此病在嬰兒期可自行緩解，而嬰幼兒使用抗憂鬱藥有安全疑慮 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證：

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-66562 | MIRTA ORODISPERSIBLE TABLETS 30MG | SB PHARMA LIMITED |
| HK-52381 | REMERON SOLTAB ORODISPERSIBLE TAB 15MG | ORGANON HONG KONG LIMITED |
| HK-67333 | MIRZENTAC TABLETS 30MG | SB PHARMA LIMITED |
| HK-53225 | PMS-MIRTAZAPINE TAB 30MG | TRENTON-BOMA LTD |
| HK-56412 | PMS-MIRTAZAPINE TAB 15MG | TRENTON-BOMA LTD |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 三個預測都只有模型分數，沒有臨床試驗、文獻或機轉證據，證據等級為 L5。
- Mirtazapine 的已知藥理與 Ohdo 症候群的致病機轉缺乏連結，仿單安全性資料也尚未取得，目前不宜推進。

**若要推進需要：**
- 取得香港衛生署仿單的警語與禁忌症資料，才能進行安全性篩選。
- 補齊 Mirtazapine 的作用機轉資料（例如查詢 DrugBank）。
- 檢索 Mirtazapine 與 KAT6B、染色質修飾或相關神經發展疾病的前臨床與文獻證據。
- 若考慮嬰兒良性陣發性斜頸，需另行評估嬰幼兒使用抗憂鬱藥的安全性。
- 目前所有預測只有模型分數，需先有任何實際研究證據，才值得重新評估。

*本報告僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

