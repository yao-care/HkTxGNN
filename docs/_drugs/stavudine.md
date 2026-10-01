---
layout: default
title: Stavudine
parent: 中證據等級 (L3-L4)
nav_order: 819
evidence_level: L4
indication_count: 3
---

# Stavudine
{: .fs-9 }

證據等級: **L4** | 預測適應症: **3** 個
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

# Stavudine：從抗 HIV 治療到貓免疫缺陷病毒感染

## 一句話總結

Stavudine 是一種胸腺嘧啶核苷類逆轉錄酶抑制劑（NRTI），屬於抗病毒藥物。
TxGNN 模型預測它可能對**貓後天免疫缺陷症候群 (Feline Acquired Immunodeficiency Syndrome)** 有效。
目前**沒有臨床試驗**，只有 **2 篇動物前臨床文獻**，且都是研究 Stavudine 衍生物 Stampidine，不是 Stavudine 本身，證據屬間接。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明（藥理分類為抗病毒 NRTI） |
| 預測新適應症 | 貓後天免疫缺陷症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 99.55% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Stavudine 是胸腺嘧啶核苷類 NRTI，一般認為它透過抑制病毒的逆轉錄酶來阻斷病毒複製。

貓免疫缺陷病毒 (FIV) 是慢病毒，和 HIV 同屬一類，同樣依賴逆轉錄酶複製。因此 NRTI 類藥物在機轉上有可能對 FIV 起作用，這也是 TxGNN 給出高分的合理背景。

不過現有文獻研究的是 Stavudine 的衍生物 Stampidine（芳基磷醯胺酸酯類），不是 Stavudine 本身，所以只能算間接支持。另外，這個預測的對象是貓的疾病，屬於獸醫領域，並非人類適應症。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12654652](https://pubmed.ncbi.nlm.nih.gov/12654652/) | 2003 | 動物體內療效研究 | Antimicrob Agents Chemother | Stampidine（Stavudine 衍生物）單次口服 50 或 100 mg/kg，6 隻慢性 FIV 感染貓中有 5 隻的血中病毒量短暫下降 1 個 log 以上，且無副作用 |
| [16570826](https://pubmed.ncbi.nlm.nih.gov/16570826/) | 2006 | 動物藥動學／毒性研究 | Arzneimittel-Forschung | Stampidine 在犬與 FIV 感染貓口服 100 mg/kg 的無毒劑量下，血漿濃度可達 IC50 的 3-4 個 log 以上 |

## 香港上市資訊

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-63085 | STAVUDINE CAPSULES 30MG | I & C (HONG KONG) LIMITED |
| HK-63084 | STAVUDINE CAPSULES 40MG | I & C (HONG KONG) LIMITED |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據只有動物前臨床研究，且研究對象是衍生物 Stampidine，不是 Stavudine 本身。
- 預測對象是貓的疾病，不是人類適應症。
- 另有 SIV 預測項目的文獻，提到猕猴使用二去氧核苷類似物治療後發生致命性胰臟炎（原文標題被截斷，確切藥物需再確認）。這是需要留意的安全性訊號。

**若要推進需要：**
- 確認 Stavudine 本身（而非 Stampidine）在 FIV 的體外或動物療效資料
- 取得香港衛生署仿單的警語與禁忌症
- 取得詳細的作用機轉資料（DrugBank）
- 釐清這項預測是否有人類或獸醫上的轉譯價值

*本報告僅供研究參考，不構成醫療建議。預測結果需經臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

