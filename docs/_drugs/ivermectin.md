---
layout: default
title: Ivermectin
parent: 僅模型預測 (L5)
nav_order: 486
evidence_level: L5
indication_count: 10
---

# Ivermectin
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

# Ivermectin：從抗寄生蟲用藥到外陰陰道念珠菌症

## 一句話總結

Ivermectin 是抗寄生蟲藥，香港已有人用（外用乳膏）與動物用製劑上市。
TxGNN 模型預測它可能對**外陰陰道念珠菌症 (Vulvovaginal Candidiasis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 外陰陰道念珠菌症 (Vulvovaginal Candidiasis) |
| TxGNN 預測分數 | 99.95% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Ivermectin 主要作用於無脊椎動物的麩胺酸門控氯離子通道，而念珠菌（真菌）並沒有這類標的。因此，這個預測在機轉上沒有明確支持。

TxGNN 的高分（0.9995）較可能反映知識圖譜中它與抗感染藥物的相近性，而不是經驗證的抗真菌機轉。原適應症與新適應症之間的關聯性也尚未評估。

這個預測應視為低信心的計算結果。要提高可信度，至少需要體外抗真菌活性或機轉研究。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

補充：本藥其他預測適應症各有 1 篇文獻，但都不支持療效。
- 食道念珠菌症：PMID [35835488](https://pubmed.ncbi.nlm.nih.gov/35835488/)，2022 年病例報告，內容是類固醇長期治療後的散播性糞小桿線蟲症。
- 先天性念珠菌症：PMID [10098288](https://pubmed.ncbi.nlm.nih.gov/10098288/)，1999 年病例報告，內容是口服 ivermectin 治療免疫功能低下兒童的結痂型疥瘡。

兩篇都是 ivermectin 的抗寄生蟲用途，與念珠菌症無關。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-58372 | ALFAMEC INJ 1% (VET) | ALFAMEDIC LIMITED |
| HK-64980 | SOOLANTRA CREAM 10MG/G | GALDERMA HONG KONG LIMITED |
| HK-47901 | HEARTGARD PLUS CHEW TAB 136MCG/114MG (VET) | BOEHRINGER INGELHEIM ANIMAL HEALTH (HONG KONG) LIMITED |
| HK-47899 | HEARTGARD-PLUS CHEW TAB 272MCG/227MG (VET) | BOEHRINGER INGELHEIM ANIMAL HEALTH (HONG KONG) LIMITED |
| HK-47900 | HEARTGARD PLUS CHEW TAB 68MCG/57MG (VET) | BOEHRINGER INGELHEIM ANIMAL HEALTH (HONG KONG) LIMITED |

共 8 張許可證，此處列出 5 張。本資料未提供核准適應症與劑型，5 張中有 4 張是動物用（VET）製劑。

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據等級為 L5，只有模型預測，沒有試驗或文獻。
- 機轉上沒有可辨識的抗真菌標的，高分很可能是圖譜相近性造成的假象。
- 同批的其他預測（食道念珠菌症、陰道炎、外陰炎等）同樣是 L5、Hold。

**若要推進需要：**
- 香港衛生署仿單的警語與禁忌資料（目前是阻擋性缺口，無法進入安全性篩選）。
- 從 DrugBank 補齊作用機轉（MOA）資料。
- Ivermectin 對念珠菌的體外抗真菌活性或機轉研究。
- 確認疾病映射是否正確，並確認人用製劑的劑型與給藥途徑是否適用於陰道給藥。

*本報告結果僅供研究參考，不構成醫療建議。老藥新用候選需經過臨床驗證才能應用。*
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

