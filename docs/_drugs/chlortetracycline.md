---
layout: default
title: Chlortetracycline
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Chlortetracycline：預測新適應症為感染後血管炎 (Postinfectious Vasculitis)（證據等級 L5）。原適應症：砂眼、鸚鵡熱、新生兒眼炎"
monitor_inn: "Chlortetracycline"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "otitis externa", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "parasitic eyelid infestation"]
---

# Chlortetracycline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Chlortetracycline：從砂眼到感染後血管炎

## 一句話總結

Chlortetracycline（氯四環素）是四環素類抗生素，原本用於砂眼、鸚鵡熱與新生兒眼炎等感染。
TxGNN 模型預測它可能對**感染後血管炎 (postinfectious vasculitis)** 有效，
但目前**沒有任何臨床試驗或直接文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 砂眼、鸚鵡熱、新生兒眼炎（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 感染後血管炎 (Postinfectious Vasculitis) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Chlortetracycline 屬於四環素類抗生素，其在砂眼等感染中的療效已為人所知，機轉上可能適用於與感染相關的疾病。

一個尚未驗證的推測是：四環素類藥物具有抗發炎特性（如抑制基質金屬蛋白酶 MMP、降低嗜中性白血球趨化），可能作用於免疫介導的血管損傷。不過，這只是假說，現有資料無法確認機轉上的連結。

其他分數相近的預測（皆為 L5、Hold）包括：感染後症候群、細菌感染後疾患、感染性尿道狹窄、外耳炎、恰加斯心肌病變、感染相關溶血尿毒症候群，以及寄生蟲性眼瞼感染。其中**感染相關溶血尿毒症候群**需特別留意：產志賀毒素的大腸桿菌感染通常避免使用抗生素，因可能增加毒素釋放與 HUS 風險，此預測與臨床常規相抵觸。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對排名第一的預測適應症（感染後血管炎），目前無相關文獻。

補充說明：排名第八的「寄生蟲性眼瞼感染」雖檢索到 1 篇文獻（PMID [21955627](https://pubmed.ncbi.nlm.nih.gov/21955627/)，2012 年，Cornea），但該研究探討的是 5% 茶樹油軟膏治療眼部蠕形蟎蟲症的眼癢，**並未涉及 Chlortetracycline**，不構成藥物特異性證據。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-06476 | CHLORTRALIM EYE OINT 1% | 眼用軟膏（依品名推斷） | 未載明 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症皆僅有模型分數（L5），沒有臨床試驗或藥物特異性文獻，且作用機轉資料缺口使機轉連結無法確認。
- 現有安全性資料缺失，無法進入安全性篩選；部分預測（如感染相關溶血尿毒症候群）還與臨床常規相衝突。

**若要推進需要：**
- 補充 Chlortetracycline 的作用機轉資料（MOA）。
- 取得香港衛生署核准仿單，確認適應症、警語與禁忌症。
- 針對感染後血管炎進行系統性文獻回顧，確認是否有前臨床或病例報告支持。
- 評估給藥途徑相容性：香港現有製劑為眼用軟膏，是否適用於預測的全身性疾病尚待確認。
- 若轉向眼科方向（如寄生蟲性眼瞼感染、外耳炎），需先比較現行標準治療並釐清增益價值。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

