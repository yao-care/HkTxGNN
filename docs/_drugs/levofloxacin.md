---
layout: default
title: Levofloxacin
parent: 僅模型預測 (L5)
nav_order: 527
evidence_level: L5
indication_count: 10
monitor_inn: "LEVOFLOXACIN"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
last_modified_at: 2026-10-31
description: "Levofloxacin：預測新適應症為點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)（證據等級 L5）。原適應症：知識圖譜記錄的關係：細菌性肺炎、結膜炎、鼻竇炎、腎盂腎炎、炭疽等細菌感染"
---

# Levofloxacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

## Levofloxacin：從細菌感染到點狀上皮角膜結膜炎
{: .text-alpha }

## 一句話總結

Levofloxacin 是氟喹諾酮類抗菌藥物，知識圖譜中記錄的原適應症包含肺炎、鼻竇炎、結膜炎、腎盂腎炎、炭疽等細菌感染。
TxGNN 模型預測它可能對**點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇**間接相關文獻，且該文獻並不支持此預測，證據等級為 L5。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關係：細菌性肺炎、結膜炎、鼻竇炎、腎盂腎炎、炭疽等細菌感染（香港許可證資料未提供適應症文字） |
| 預測新適應症 | 點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般而言，Levofloxacin 屬於氟喹諾酮類抗菌藥，作用於細菌的 DNA 旋轉酶與拓樸異構酶 IV。香港另有 Levofloxacin 眼用製劑登記（品名含 CRAVIT OPHTHALMIC SOLUTION、LEVOCLE EYE DROPS、LEVOCIN EYE DROPS），因此對眼表面細菌感染的使用有合理基礎。

知識圖譜中記錄的原適應症包含結膜炎，TxGNN 的高分很可能來自與此疾病的相似性。不過，點狀上皮角膜結膜炎不一定由細菌引起，目前也沒有資料顯示 Levofloxacin 對此疾病有效。

唯一檢索到的文獻是微孢子蟲角膜結膜炎的群聚事件報告。微孢子蟲並非氟喹諾酮的作用對象，因此這篇文獻無法支持此預測。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | 群聚事件報告 | American Journal of Ophthalmology | 台灣游泳池水污染造成微孢子蟲角膜結膜炎群聚；與 Levofloxacin 療效無直接關聯 |

## 香港上市資訊

以下為已列出的主要許可證（總數至少 20 張，清單可能不完整；資料中未提供核准適應症與劑型文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51495 | CRAVIT TAB 250MG | 未提供 | 未提供 |
| HK-64805 | CRAVIT OPHTHALMIC SOLUTION 1.5%W/V | 眼用溶液 | 未提供 |
| HK-65005 | LEVOFLOXACIN KABI SOLUTION FOR INFUSION 500MG/100ML | 輸注液 | 未提供 |
| HK-65995 | LEVOCLE EYE DROPS 0.5% W/V | 眼藥水 | 未提供 |
| HK-58278 | LEVOCIN EYE DROPS 0.5% | 眼藥水 | 未提供 |

## 安全性考量

- **知識圖譜記錄的禁忌關係**（非仿單文字）：長 QT 症候群、尖端扭轉型心律不整、癲癇、肝臟疾病、肌腱炎、周邊神經病變、重症肌無力、糖尿病、腎功能不全、困難梭狀芽孢桿菌結腸炎、血小板減少、白血球減少、橫紋肌溶解、冠狀動脈疾病等。
- **藥物交互作用**：資料庫共記錄 100 筆，其中較重要的有：
  - 重度：Tramadol、Hydrocortisone
  - 中度：Abiraterone、Acarbose、Famotidine、Formoterol、Ketorolac、Adenosine、Ibuprofen、Metformin、Pioglitazone 等
- 此外，預測清單中的「與周邊神經病變相關的血液疾病」一項，與氟喹諾酮已知的周邊神經病變風險相衝突。

仿單警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，唯一的文獻是微孢子蟲感染事件報告，並不支持 Levofloxacin 對此疾病有效，證據等級為 L5。
- 高預測分數很可能只反映與已知結膜炎適應症的相似性。

**若要推進需要：**
- 釐清目標疾病的致病原（細菌性或非細菌性），確認抗菌藥物是否有作用對象。
- 檢索眼科領域針對 Levofloxacin 眼用製劑的臨床研究及香港眼用製劑的核准適應症。
- 取得原廠仿單的警語與禁忌症，以及作用機轉資料。

---

### 補充：其他預測適應症中值得注意的項目

- **單株免疫球蛋白病變 (Monoclonal Gammopathy)**：有 TEAMM 第 3 期隨機試驗（PMID 31668592）及多篇相關文獻，但研究對象為新診斷的有症狀骨髓瘤，而非單株免疫球蛋白病變本身，且機轉為預防感染而非治療疾病。依規則，由於沒有研究直接針對該疾病，證據等級應視為 L5，建議列為研究問題。
- **敗血性鼠疫 (Septicemic Plague)**：有非人靈長類動物研究顯示 Levofloxacin 可治癒實驗性肺鼠疫（PMID 21347450），但無人體試驗，且研究對象為肺鼠疫而非敗血性鼠疫；依規則證據等級應為 L5，僅供作為進一步研究的方向。
- 其餘預測項目（高黏稠度症候群、高澱粉酶血症、先天性無白蛋白血症等）均無證據及合理機轉，應列為 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

