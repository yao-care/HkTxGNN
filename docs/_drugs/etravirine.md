---
layout: default
title: Etravirine
parent: 僅模型預測 (L5)
nav_order: 355
evidence_level: L5
indication_count: 5
---

# Etravirine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Etravirine：從 HIV 感染到貓免疫缺陷病毒感染（預測）

## 一句話總結

Etravirine 是一種 HIV-1 非核苷類逆轉錄酶抑制劑（NNRTI），原本用於 HIV 感染與愛滋病治療。
TxGNN 模型預測分數最高的新適應症為**貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome)**，但目前**沒有任何臨床試驗或文獻**直接支持，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染、愛滋病 |
| 預測新適應症 | 貓後天免疫缺乏症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Etravirine 屬於 HIV-1 NNRTI，透過抑制病毒逆轉錄酶阻斷病毒複製，對許多對第一代 NNRTI 產生抗藥性的 HIV 株仍具活性。

貓免疫缺陷病毒 (FIV) 與 HIV 同屬慢病毒，因此模型在知識圖譜中將兩者拉近。不過，FIV 的逆轉錄酶一般被認為對 NNRTI 具天然抗藥性，這個高分較可能反映的是圖譜上與 HIV 的鄰近關係，而非已驗證的機轉。

其他預測結果也需謹慎解讀：猿猴免疫缺陷病毒 (SIV) 感染同樣缺乏可靠的 NNRTI 敏感性證據；「AIDS 相關症候群」其實屬於原有 HIV 適應症的另一種說法，並非真正的新適應症；而神經發展障礙一項在機轉上沒有合理關聯，應屬圖譜運算的假象。其中，**先天性（母嬰）HIV** 是機轉上最直接適用的方向，但目前僅有小型病例報告。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對排名第一的預測（貓後天免疫缺乏症候群），目前無相關文獻。

下表為其他預測適應症中較相關的文獻，僅供參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20587860](https://pubmed.ncbi.nlm.nih.gov/20587860/) | 2010 | 病例系列／回溯性報告 | Antiviral Therapy | 兩例高度治療經驗的孕婦使用 darunavir 與 etravirine（加或不加 raltegravir），提供懷孕期使用的有限安全性與藥動學資料（對應「先天性 HIV」） |
| [19290032](https://pubmed.ncbi.nlm.nih.gov/19290032/) | 2009 | 世代研究 | AIDS Reviews | HIV 患者（治療與未治療）腸胃道不良事件的風險因子（對應「AIDS 相關症候群」，屬間接證據） |
| [27067022](https://pubmed.ncbi.nlm.nih.gov/27067022/) | 2016 | 前臨床／病毒學 | AIDS Research and Human Retroviruses | L228I 與 Y232H 新突變以組合方式造成 NNRTI 抗藥性（對應「AIDS 相關症候群」，屬間接證據） |
| [26529558](https://pubmed.ncbi.nlm.nih.gov/26529558/) | 2015 | 前臨床（體外） | Molecular Pharmaceutics | 奈米顆粒抗病毒藥物組合可協同抑制 HIV 的游離病毒與細胞間傳播（對應「SIV 感染」，間接且僅為前臨床） |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61470 | INTELENCE TAB 200MG | （未提供） | （未提供） |

製造商：Johnson & Johnson (Hong Kong) Ltd.，狀態：有效。

## 安全性考量

- **知識圖譜標記的禁忌疾病**（來自知識圖譜關聯，並非仿單內容）：慢性 C 型肝炎病毒感染、C 型肝炎病毒感染、慢性 B 型肝炎病毒感染、周邊神經系統疾病、周邊神經病變。
- **藥物交互作用**：共查得 100 筆，以下為部分列示（皆為 DDInter 資料）：
  - 中度：Rabeprazole、Omeprazole、Cimetidine、Clarithromycin、Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Aprepitant、Pioglitazone、Saxagliptin、Linagliptin、Glimepiride、Chlorpropamide、Metronidazole 等
  - 輕度：Ranitidine

主要警語與正式禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測（貓免疫缺陷）完全沒有試驗與文獻支持，證據等級僅為 L5，且 FIV 逆轉錄酶對 NNRTI 具天然抗藥性，高分可能是圖譜假象。
- 唯一較有臨床意義的方向是先天性（母嬰）HIV，機轉直接適用，但目前僅有小型病例報告（L3），屬於值得研究的問題，而非可直接推進的新適應症。

**若要推進需要：**
- 以體外試驗驗證 etravirine 對 FIV／SIV 逆轉錄酶的實際抑制活性
- 若關注母嬰 HIV：蒐集孕婦與新生兒的藥動學、安全性與療效資料，並檢視相關臨床試驗
- 取得詳細作用機轉資料（MOA）
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選
- 評估 B/C 型肝炎共感染與周邊神經病變族群的使用風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

