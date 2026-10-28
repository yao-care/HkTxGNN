---
layout: default
title: Atazanavir
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 4
monitor_inn: "ATAZANAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "obsolete familial combined hyperlipidemia"]
last_modified_at: 2026-10-23
description: "Atazanavir：預測新適應症為貓後天免疫缺乏症候群 (feline acquired immunodeficiency syndrome)（證據等級 L5）。原適應症：HIV 感染、AIDS"
---

# Atazanavir
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Atazanavir：從 HIV 感染到貓後天免疫缺乏症候群
{: .text-alpha }

## 一句話總結

Atazanavir 是一種 HIV 蛋白酶抑制劑，原本用於 HIV 感染與 AIDS 的治療（此為知識圖譜記錄的關係）。
TxGNN 模型預測它可能對**貓後天免疫缺乏症候群 (feline acquired immunodeficiency syndrome)** 有效，但目前**沒有臨床試驗、也沒有直接研究此疾病的文獻**，僅有模型預測支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | HIV 感染、AIDS（知識圖譜記錄的關係；香港許可證未載明適應症文字） |
| 預測新適應症 | 貓後天免疫缺乏症候群 (feline acquired immunodeficiency syndrome) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，atazanavir 屬於 HIV-1 蛋白酶抑制劑類別，其在 HIV 感染中的角色已為人所知，機轉上可能與其他慢病毒的蛋白酶有關。

貓免疫缺乏病毒 (FIV) 與 HIV 同屬慢病毒，因此以蛋白酶為標的的機轉原則上可行。然而 FIV 蛋白酶在受質特異性與對抑制劑的敏感度上與 HIV-1 蛋白酶不同，不能直接假設療效可以轉移。

0.9998 的高分很可能反映的是網路上與 HIV/AIDS 適應症的鄰近性，而非獨立的證據。此外，這是一個獸醫疾病，與人用藥品的上市與審查路徑不同。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無直接研究貓後天免疫缺乏症候群的文獻。

為完整說明，排名第 2 的預測「猴免疫缺乏病毒感染」有 1 篇相關文獻，但它不屬於本報告的主要預測疾病，僅供參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [20497048](https://pubmed.ncbi.nlm.nih.gov/20497048/) | 2010 | 動物研究（非人靈長類） | The Journal of Infectious Diseases | SIV 感染獼猴接受高效能抗反轉錄病毒治療後，中樞神經系統病毒複製與發炎降低，但病毒 DNA 仍持續存在；是否含 atazanavir 尚不明 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68750 | ATAZANAVIR CAPSULES 300MG | 未提供 | 未提供 |
| HK-68749 | ATAZANAVIR CAPSULES 200MG | 未提供 | 未提供 |

兩張許可證皆為單一成分製劑，持有者為 HIND WING CO LTD，狀態有效。

## 安全性考量

- **知識圖譜記錄的禁忌關係（非仿單內容）**：肝衰竭、肝臟疾病、膽囊疾病、高血糖、糖尿病、糖尿病酮酸中毒、慢性 C 型肝炎、C 型肝炎、慢性 B 型肝炎、血友病、高膽紅素血症、遺傳性高膽紅素血症、Gilbert 症候群、腎結石、急性尿酸腎病變、房室傳導阻滯、乳酸酸中毒。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 嚴重 (Major)：Famotidine、Ranitidine、Rabeprazole、Omeprazole（胃酸抑制劑）、Loperamide、Triamcinolone、Budesonide
  - 中度 (Moderate)：Acarbose、Hydrocortisone、Metformin、Pioglitazone、Alosetron、Aprepitant、Aluminum hydroxide、Calcium carbonate 等

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型分數，沒有直接研究貓後天免疫缺乏症候群的臨床試驗或文獻，證據等級為 L5。
- 目標疾病為獸醫疾病，且 FIV 與 HIV 蛋白酶的差異使療效難以直接推論。

**若要推進需要：**
- 補齊 atazanavir 的作用機轉資料
- 以體外試驗評估 atazanavir 對 FIV 蛋白酶的抑制活性
- 確認是否有 FIV 動物模型或獸醫領域的相關研究
- 釐清此預測是否屬於人用藥品再利用範疇，並取得香港仿單的警語與禁忌資料
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

