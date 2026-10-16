---
layout: default
title: Stavudine
parent: 僅模型預測 (L5)
nav_order: 834
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Stavudine：預測新適應症為貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome)（證據等級 L5）。原適應症：HIV 感染、AIDS"
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

# Stavudine：從 HIV 感染／AIDS 到貓免疫缺乏症候群

## 一句話總結

Stavudine 是一種核苷類逆轉錄酶抑制劑，原本用於治療 HIV 感染與 AIDS。
TxGNN 模型預測它可能對**貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome)** 有效，但目前**沒有臨床試驗與文獻**支持這個預測，僅屬模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染、AIDS（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 99.55% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Stavudine 是胸腺嘧啶核苷類似物（thymidine analogue）的核苷類逆轉錄酶抑制劑（NRTI），其在 HIV 感染中的療效已被證實。

貓免疫缺乏病毒（FIV）與 HIV 同屬慢病毒，同樣依賴逆轉錄酶複製，因此在機轉上有類推的可能性。TxGNN 的高分很可能源自知識圖譜中 FIV 與 HIV 疾病節點的相似性，而非獨立的實證。

需要留意：這是動物（獸醫）疾病，並非人類臨床適應症，對人用藥物的再利用價值有限。

另外兩個排名較後的預測也值得一提：
- **猿猴免疫缺乏病毒（SIV）感染**（分數 99.55%，證據等級 L4）：僅有間接的前臨床文獻，且猕猴研究出現致命性胰臟炎的安全性訊號。
- **伴隨共濟失調步態、無語言及皮質白質減少的神經發展障礙**（分數 99.51%，證據等級 L5）：看不出明確的機轉關聯，且 Stavudine 本身有周邊神經病變與粒線體毒性的疑慮。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首要預測（貓免疫缺乏症候群）目前無相關文獻。

作為參考，第二順位預測（SIV 感染）有以下前臨床文獻，僅提供間接支持：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [22013040](https://pubmed.ncbi.nlm.nih.gov/22013040/) | 2012 | 動物研究（非人靈長類） | Journal of Virology | SIV 感染的獼猴在接受 ddI 與 stavudine 合併 CTLA-4 及 IDO 阻斷後發生致命性胰臟炎 |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | 體外敏感性研究 | Antiviral Therapy | 評估 16 種已核准藥物對 HIV-2、SIV 與 SHIV 的抗病毒活性 |
| [11435599](https://pubmed.ncbi.nlm.nih.gov/11435599/) | 2001 | 體外研究（人類泡沫病毒，間接相關） | Journal of Virology | 評估雙脫氧核苷對人類泡沫病毒的效力，與 stavudine 在 SIV 的療效關聯低 |
| [9021177](https://pubmed.ncbi.nlm.nih.gov/9021177/) | 1997 | 體外研究（不同化合物，相關性低） | Antimicrob Agents Chemother | 二硫鍵大環內酯 SRR-SB3 抑制 HIV 複製晚期階段，與 stavudine 無直接關係 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63085 | STAVUDINE CAPSULES 30MG | 膠囊（依品名） | 資料中未載明 |
| HK-63084 | STAVUDINE CAPSULES 40MG | 膠囊（依品名） | 資料中未載明 |

兩張許可證均為單一成分、現行有效，持有人為 I & C (HONG KONG) LIMITED。

---

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎情況**（非仿單內容）：腎臟疾病、胰臟炎、肝臟疾病、膽囊疾病、高血糖、糖尿病、糖尿病酮酸中毒、周邊神經系統疾病、周邊神經病變、物質濫用／依賴、肥胖相關疾病、脂肪肝、非酒精性脂肪肝炎、乳酸中毒。
- **藥物交互作用**：資料庫共查得 100 筆，以下為其中列出的中度交互作用：
  - Metronidazole
  - Naltrexone
  - Orlistat
  - Rosuvastatin
  - Simvastatin
  - Tinidazole

  其餘多項（如 Metformin、Omeprazole、Morphine、Prednisone 等）的嚴重度尚未分級。
- **動物研究訊號**：SIV 感染獼猴合併用藥時曾出現致命性胰臟炎，與上述胰臟炎相關的警示方向一致。

香港仿單的警語與禁忌資料尚未取得，完整安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（貓免疫缺乏症候群）僅有模型分數，沒有任何臨床試驗或文獻，證據等級為 L5，且屬獸醫領域疾病，與人用藥物再利用的目標不一致。
- 其他預測同樣缺乏實證，並伴隨胰臟炎及神經毒性等安全性疑慮。

**若要推進需要：**
- 取得香港仿單的警語與禁忌資料，完成安全性篩選
- 補齊作用機轉（MOA）資料
- 釐清再利用的目標是人用還是獸醫用途；若為獸醫用途，需另行蒐集 FIV 的體外與動物療效證據
- 評估 Stavudine 的粒線體毒性、胰臟炎與周邊神經病變風險是否可接受（臨床上此藥已因毒性而少用，此點需由專家另行確認）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

