---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 290
evidence_level: L5
indication_count: 3
monitor_inn: "DOLUTEGRAVIR"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
last_modified_at: 2026-10-23
description: "Dolutegravir：預測新適應症為貓後天免疫缺陷症候群 (Feline Acquired Immunodeficiency Syndrome)（證據等級 L5）。原適應症：知識圖譜中記錄的關聯為 HIV 感染、AIDS"
---

# Dolutegravir
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

## Dolutegravir：從 HIV 感染到貓後天免疫缺陷症候群
{: .text-alpha }

## 一句話總結

Dolutegravir 是一種 HIV 整合酶抑制劑，知識圖譜中記錄的原適應症為 HIV 感染與 AIDS。
TxGNN 模型預測它可能對**貓後天免疫缺陷症候群 (Feline Acquired Immunodeficiency Syndrome)** 有效，
但目前**無臨床試驗**，僅有 **1 篇**動物（獸醫）研究文獻，屬於模型預測階段的證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的關聯為 HIV 感染、AIDS（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 貓後天免疫缺陷症候群 (Feline Acquired Immunodeficiency Syndrome) |
| TxGNN 預測分數 | 0.9985 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的藥物類別，dolutegravir 屬於 HIV-1 整合酶鏈轉移抑制劑（INSTI），透過阻斷病毒 DNA 嵌入宿主基因體而抑制複製。

貓免疫缺陷病毒 (FIV) 與 HIV 同屬慢病毒，其整合酶在結構上相近，因此從類別層面看，抑制整合酶在生物學上有合理性。TxGNN 的高分很可能反映它與 HIV 疾病的相似性，並非獨立的臨床證據。

需注意：這是獸醫適應症，無法直接轉換為人類藥物再利用機會。此外，僅有的一篇 2023 年研究（PMID 37112803）評估的是 dolutegravir 合併 tenofovir、emtricitabine 的複方療法在 FIV 感染貓的藥動學與臨床結果，屬於合併用藥的獸醫研究，且本次資料僅取得摘要的部分內容。

預測排名第 2 的「猴免疫缺陷病毒感染 (SIV)」雖有較多猴類動物研究，但同樣是動物模型，主要是驗證 dolutegravir 既有的抗反轉錄病毒機轉；第 3 名的神經發育障礙則完全沒有機轉關聯與證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | 獸醫/前臨床研究 | Viruses | 在 FIV 感染的家貓中評估 dolutegravir、tenofovir、emtricitabine 複方抗病毒療法的藥動學與臨床結果；設計細節尚待確認 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-63516 | TIVICAY TABLETS 50MG | 未載明 | 未載明 |
| HK-66511 | DOVATO TABLETS | 未載明 | 未載明 |
| HK-64012 | TRIUMEQ TABLETS | 未載明 | 未載明 |

以上 3 張許可證皆為有效狀態，持有者為 GLAXOSMITHKLINE LIMITED。

## 安全性考量

- **藥物交互作用**：本報告彙整的資料共記錄 62 筆交互作用，以下為部分範例：
  - **重大 (Major)**：含鋁、鈣、鎂、鐵的製劑，例如氫氧化鋁、碳酸鈣、檸檬酸鈣、葡萄糖酸鈣、碳酸鎂、檸檬酸鎂、鐵、高嶺土 (Kaolin)、Attapulgite、Magaldrate。這類多價陽離子可能影響整合酶抑制劑的吸收，用藥時間需與仿單核對。
  - **輕微 (Minor)**：Aprepitant、Cimetidine、Clarithromycin、Clotrimazole、Dexamethasone。

其他警語與禁忌資料請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 證據僅限於一篇獸醫前臨床研究，且無任何針對該疾病的臨床試驗，依規則證據等級為 L5（前述研究為合併療法，屬間接證據）。
- 預測的適應症為貓的疾病，不屬於人類藥物再利用範疇，高 TxGNN 分數主要反映與 HIV 的相似性。

**若要推進需要：**
- 確認是否有獸醫用藥的開發需求與法規途徑（人用藥品在動物的使用不在本評估範圍）。
- 取得 dolutegravir 完整的作用機轉資料及 FIV 整合酶的直接抑制數據。
- 取得香港仿單的核准適應症、警語與禁忌資料。
- 若目標為人類適應症，建議改以其他預測適應症或與 HIV 相關的新族群重新評估。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

