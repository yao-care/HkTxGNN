---
layout: default
title: Ziprasidone
parent: 僅模型預測 (L5)
nav_order: 956
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
monitor_inn: "Ziprasidone"
predicted_indications: ["trichotillomania", "hydranencephaly (disease)", "congenital disorder of glycosylation with defective fucosylation", "myopia X-linked", "retinal dystrophy with or without extraocular anomalies", "Tourette syndrome", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "myopia 26, X-linked, female-limited", "syndromic myopia"]
description: "Ziprasidone：預測新適應症為拔毛癖 (trichotillomania)（證據等級 L5）。香港藥劑製品註冊：12 張（有效 12 張）"
---

# Ziprasidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Ziprasidone: 拔毛癖 (trichotillomania)
{: .text-alpha }

## 一句話總結

Ziprasidone 是一種非典型抗精神病藥。
TxGNN 模型預測它可能對**拔毛癖 (trichotillomania)** 有效，但目前**沒有臨床試驗，也沒有直接研究此疾病的文獻**，僅有模型預測分數支持。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 拔毛癖 (trichotillomania) |
| TxGNN 預測分數 | 0.9983 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 12 張／共 12 張） |
| 許可證數 | 12 張（有效 12 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Ziprasidone 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Ziprasidone 用於治療所列適應症的作用機轉，可能係經由第 2 型多巴胺（D 2 ）與第 2 型血清素（5HT 2 ）拮抗作用的組合所介導。」英文原文："The mechanism of action of ziprasidone in the treatment of the listed indications could be mediated through a combination of dopamine type 2 (D 2 ) and serotonin type 2 (5HT 2 ) antagonism."（[DailyMed: Ziprasidone Mesylate 20 Mg/Ml (ziprasidone mesylate) prescribing information, Armas Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c5c27f0f-4e45-4bca-bb9a-2d3f1c243348)，版本日期 2026-09-18；查閱日期 2026-11-19）。就藥理類別而言，ziprasidone 屬於非典型抗精神病藥，已知具有多巴胺 D2 與血清素 5-HT2A 拮抗作用。

拔毛癖屬於衝動控制與重複行為相關疾病。其他作用於多巴胺與血清素系統的抗精神病藥，曾被研究用於這類重複行為問題，因此機轉上存在一條合理的推測路徑。

不過，這個推論並沒有本次整理的資料支持。目前沒有任何試驗或文獻直接探討 ziprasidone 用於拔毛癖，因此此預測仍停留在模型層次。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無直接探討拔毛癖的相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-48922 | ZELDOX CAP 20MG | 單一成分 | VIATRIS HEALTHCARE HONG KONG LIMITED | 有效 |
| HK-48923 | ZELDOX CAP 40MG | 單一成分 | VIATRIS HEALTHCARE HONG KONG LIMITED | 有效 |
| HK-48924 | ZELDOX CAP 60MG | 單一成分 | VIATRIS HEALTHCARE HONG KONG LIMITED | 有效 |
| HK-48925 | ZELDOX CAP 80MG | 單一成分 | VIATRIS HEALTHCARE HONG KONG LIMITED | 有效 |
| HK-63940 | ZIPRASIDON STADA CAPSULES 20MG | 單一成分 | HONG KONG MEDICAL SUPPLIES LTD | 有效 |

上表列出其中 5 張（共 12 張）。

<!-- licenses:end -->

目前共有 12 張許可證皆為有效狀態，以上僅列出 5 張主要許可證。

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，其中較重要的嚴重等級包括 hydrocortisone、amphotericin B、bupropion、morphine。另有多種中等等級交互作用，例如與降血糖藥（metformin、pioglitazone、acarbose 等）、抗膽鹼藥（atropine、hyoscyamine、glycopyrronium）及 epinephrine 併用。
- **需特別留意的疾病背景**：本次整理的資料顯示，長 QT 症候群、尖端扭轉型心律不整、心臟傳導疾病、心肌梗塞、肝衰竭、腎臟疾病、癲癇、糖尿病、嗜中性白血球低下及顆粒性白血球缺乏症等，被列為不宜使用或需謹慎的情況（此為資料庫關聯，非仿單文字）。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
拔毛癖這個預測只有模型分數，沒有任何臨床試驗或直接研究，證據等級為 L5。同時，此藥有 QT 延長等心臟安全性疑慮，不宜在缺乏證據下推進。

**若要推進需要：**
- 搜尋並評估 ziprasidone 或同類藥物用於拔毛癖的直接臨床研究
- 補齊作用機轉資料，並說明與拔毛癖的機轉關聯
- 取得香港原廠仿單的警語與禁忌症
- 規劃心電圖（QTc）監測與心臟風險篩檢方案
- 若有可行的初步證據，再設計小型探索性試驗

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Ziprasidone Mesylate 20 Mg/Ml (ziprasidone mesylate) prescribing information, Armas Pharmaceuticals Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c5c27f0f-4e45-4bca-bb9a-2d3f1c243348) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

