---
layout: default
title: Econazole
parent: 僅模型預測 (L5)
nav_order: 306
evidence_level: L5
indication_count: 2
monitor_inn: "Econazole"
predicted_indications: ["ectothrix infectious disease", "endothrix infectious disease"]
last_modified_at: 2026-10-28
description: "Econazole：預測新適應症為毛外型感染性疾病 (Ectothrix Infectious Disease)（證據等級 L5）。原適應症：知識圖譜記錄的用途：足癬、體癬、癬菌感染、皮膚念珠菌症、花斑癬、腹股溝與肛周皮癬菌病"
---

# Econazole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Econazole：從皮膚黴菌感染到毛外型髮癬菌感染 (Ectothrix Infectious Disease)
{: .text-alpha }

## 一句話總結

Econazole 是咪唑類抗黴菌藥，知識圖譜記錄的用途包括足癬、體癬、皮膚念珠菌症與花斑癬等皮膚黴菌感染。
TxGNN 模型預測它可能對**毛外型感染性疾病 (Ectothrix Infectious Disease)** 有效，預測分數約 0.9997。
目前**沒有任何臨床試驗或文獻**直接支持這個方向，證據僅限於模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的用途：足癬、體癬、癬菌感染、皮膚念珠菌症、花斑癬、腹股溝與肛周皮癬菌病（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 毛外型感染性疾病 (Ectothrix Infectious Disease) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 16 張／共 16 張） |
| 許可證數 | 16 張（有效 16 張） |
| 建議決策 | Hold |

另有第二個預測：毛內型感染性疾病 (Endothrix Infectious Disease)，分數 0.9997，同樣為 L5、Hold，詳見後文。

## 為什麼這個預測合理？

目前缺乏經資料確認的作用機轉資料。就藥理類別而言，Econazole 屬咪唑類抗黴菌藥，一般認為其作用是抑制真菌 14α-去甲基酶 (CYP51)，阻斷麥角固醇合成，破壞真菌細胞膜完整性。此機轉描述屬於分析推論，並非來自本報告的資料欄位。

毛外型感染是皮癬菌（如小孢子菌、毛癬菌）在毛髮表面形成孢子的感染。分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病間學到的相似性，並非生物學實證。

實務上有明顯限制：毛髮感染（如頭癬）外用藥難以穿透毛囊，標準治療通常需全身性抗黴菌藥。毛內型感染（孢子位於毛幹內，如 *T. tonsurans*）的穿透問題更明顯。外用 Econazole 單獨使用的療效值得存疑。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

香港共有 16 張有效的單一成分許可證，皆為上市狀態。以下列出 5 張主要許可證，資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-36295 | ECOMI VAGINAL PESSARIES 150MG | 未提供 | 未提供 |
| HK-34621 | ECONAZOLE SUPP 150MG "YUNG SHIN" | 未提供 | 未提供 |
| HK-57772 | ZYME SOLUTION 10MG/ML | 未提供 | 未提供 |
| HK-58828 | EKONA VAGINAL SUPP 150MG | 未提供 | 未提供 |
| HK-54354 | PICOSONE CREAM | 未提供 | 未提供 |

其餘 11 張以乳膏為主（部分品名顯示為含其他成分的組合名稱，但登記資料標示為單一成分）。

## 安全性考量

- **藥物交互作用**：已查詢到 41 筆潛在交互作用，嚴重度分級皆為未知。部分例子包括 Clotrimazole、Fluconazole、Dexamethasone、Fluticasone、Clopidogrel、Heparin、Metformin、Omeprazole、Diazepam、Lorazepam。

其他安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個預測（毛外型、毛內型感染）皆無任何臨床試驗或文獻，僅有模型分數，證據等級為 L5。
- 外用劑型對毛髮內部感染的穿透性有限，標準治療通常是全身性藥物，外用 Econazole 的臨床價值不明。

**若要推進需要：**
- 檢索並確認 Econazole 對毛癬菌、小孢子菌的體外感受性與頭癬相關研究。
- 補齊作用機轉資料與香港仿單的警語及禁忌症。
- 評估外用劑型對毛囊與毛幹的穿透性，以及與全身性抗黴菌藥合併使用的可行性。
- 確認各許可證的核准適應症文字，以釐清實際已核准的使用範圍。

## 附：第二個預測（毛內型感染性疾病）

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 毛內型感染性疾病 (Endothrix Infectious Disease) |
| TxGNN 預測分數 | 0.9997 |
| 臨床試驗／文獻 | 無 |
| 證據等級 | L5 |
| 建議決策 | Hold |

評估邏輯與上述相同：機轉上有合理性，但孢子位於毛幹內，外用藥穿透受限，缺乏任何實證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

