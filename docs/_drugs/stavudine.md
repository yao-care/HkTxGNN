---
layout: default
title: Stavudine
parent: 僅模型預測 (L5)
nav_order: 706
evidence_level: L5
indication_count: 3
---

# Stavudine
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

# STAVUDINE：從（原適應症資料缺失）到貓後天免疫缺乏症候群

## 一句話總結

> STAVUDINE 的原始適應症與作用機轉資料目前缺失（Data Gap DG002），香港亦無相關藥品許可證或上市紀錄。
> TxGNN 模型預測其可能對**貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome)** 有效，預測分數達 **99.55%**，
> 但目前**無臨床試驗**支持，僅有 **2 篇文獻**，且文獻實際研究對象為另一化合物 stampidine（並非 stavudine 本身），證據關聯性薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（本評估未取得核准適應症紀錄） |
| 預測新適應症 | 貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 99.55%（rank 8316） |
| 證據等級 | L5（僅有間接動物文獻，且研究對象非同一化合物） |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏 STAVUDINE 的詳細作用機轉（MOA）資料，也沒有可用的原始核准適應症紀錄可供比對（Data Gap DG002）。這使得機轉關聯性分析難以進行完整交叉比對。

根據本評估收集到的文獻脈絡，STAVUDINE 曾在動物實驗中與 didanosine 併用作為抗反轉錄病毒治療方案的一部分，用於治療猴免疫缺乏病毒 (SIV) 感染的獼猴模式（PMID 22013040）。這顯示 STAVUDINE 屬於雙脫氧核苷類（dideoxynucleoside）反轉錄酶抑制劑，與其他慢病毒（lentivirus）感染如 HIV、SIV、FIV 在藥理機轉上具有跨物種的潛在關聯性——這也可能是 TxGNN 模型將其連結至貓後天免疫缺乏症候群與 SIV 感染的原因。

然而需特別注意：rank 1 預測（貓後天免疫缺乏症候群）所附的兩篇文獻實際討論的化合物是 **stampidine**，一種結構相關但不同的實驗性 NRTI 前驅藥，並非 STAVUDINE 本身。此差異意味著現有證據對 STAVUDINE 用於此適應症的直接支持力有限，屬於**類別層級（class-level）**而非**藥物層級（drug-level）**的關聯推論，關聯性偏弱。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [16570826](https://pubmed.ncbi.nlm.nih.gov/16570826/) | 2006 | 動物藥動學/毒理學研究（⚠️研究對象為 stampidine，非 stavudine） | Arzneimittel-Forschung | Stampidine 口服 100 mg/kg 於犬與 FIV 感染貓可達治療血中濃度，無明顯毒性 |
| [12654652](https://pubmed.ncbi.nlm.nih.gov/12654652/) | 2003 | 動物體內抗病毒活性研究（⚠️研究對象為 stampidine，非 stavudine） | Antimicrobial Agents and Chemotherapy | 單次口服 stampidine 50-100 mg/kg 使 FIV 感染貓的病毒量短暫下降 ≥1 log，六隻中五隻無副作用 |

---

## 安全性考量

> 安全性資訊請參考原廠仿單。（key_warnings、contraindications、DDI 皆為 Data Gap，見 DG001）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 無任何臨床試驗支持，僅有的 2 篇文獻研究對象是結構相關但不同的化合物（stampidine），並非 STAVUDINE 本身，證據直接性不足。
- 預測適應症「貓後天免疫缺乏症候群」為獸醫學疾病，非人類醫療適應症，不具直接臨床轉譯價值。
- 香港未上市（0 張許可證），MOA 與仿單安全性資料均為 Blocking/High 等級的資料缺口（DG001、DG002），無法進入 S1 安全性初評。

**補充說明（其他預測適應症）：**
Evidence Pack 另列 2 項預測：rank 2「simian immunodeficiency virus infection」有較直接的 stavudine 相關文獻（如 PMID 22013040、15040537），但 SIV 為非人類感染疾病，仍須轉譯至人類 HIV 相關情境才具意義；rank 3「神經發育障礙合併步態失調」已由系統標註 **L5 / S0 / Hold**，並明確警示可能為嵌入空間偽相關（spurious signal），且與 stavudine 已知粒線體毒性存在因果方向混淆風險，不建議推進。

**若要推進需要：**
- 補齊 STAVUDINE 本身（而非類似物 stampidine）於慢病毒感染的直接藥理與體內外數據
- 取得香港衛生署／原廠仿單之警語、禁忌症、DDI 等安全性資料（DG001）
- 取得 STAVUDINE 完整作用機轉（MOA）資料（DG002）
- 若考慮人類適應症轉譯（如 rank 2 相關之抗反轉錄病毒交叉活性），需重新定義為人類臨床可操作的適應症族群，而非直接沿用動物疾病名稱
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

