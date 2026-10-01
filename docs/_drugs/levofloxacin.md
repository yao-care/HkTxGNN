---
layout: default
title: Levofloxacin
parent: 中證據等級 (L3-L4)
nav_order: 518
evidence_level: L4
indication_count: 5
---

# Levofloxacin
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Levofloxacin：從細菌感染到點狀上皮角膜結膜炎

## 一句話總結

Levofloxacin 是氟喹諾酮類抗菌藥，原本用於細菌感染。
TxGNN 模型預測它可能對**點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效，但目前**無臨床試驗**，僅有 **1 篇**間接相關的文獻（微孢子蟲角膜結膜炎群聚事件報告），證據薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌感染（依藥物類別判斷；香港許可證資料未載明適應症文字） |
| 預測新適應症 | 點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Levofloxacin 是氟喹諾酮類抗生素，透過抑制細菌 DNA gyrase 與 topoisomerase IV 發揮殺菌作用。眼用製劑在細菌性結膜炎的用途已有確立。DrugBank 目前缺乏詳細的作用機轉資料，因此以上機轉描述無法與 DrugBank 交叉比對。

從疾病關聯來看，兩者都屬眼表感染或發炎，這可能是模型給出高分的原因。但點狀上皮角膜結膜炎通常由病毒（如腺病毒）引起，本次找到的文獻則是微孢子蟲引起。抗菌活性預期對這兩種病因都無效。

因此，0.999 的高分較可能反映知識圖譜中與眼表感染節點的距離接近，而不是經過驗證的作用機轉。這個預測目前缺乏生物學上的合理支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | 群聚事件報告 | American Journal of Ophthalmology | 台灣游泳池水污染造成微孢子蟲角膜結膜炎群聚感染，並未評估 levofloxacin 的療效 |

---

## 香港上市資訊

香港共有 20 張許可證，以下列出 5 張主要許可證。資料中未載明劑型與核准適應症。

| 許可證號 | 品名 | 製造商 |
|---------|------|--------|
| HK-56369 | VICK-LEVOXA TAB 100MG | VICKMANS LABORATORIES LTD |
| HK-60925 | LEXACIN TAB 250MG | MEDILINE (HONG KONG) COMPANY LIMITED |
| HK-65005 | LEVOFLOXACIN KABI SOLUTION FOR INFUSION 500MG/100ML | FRESENIUS KABI HONG KONG LIMITED |
| HK-60112 | LEVOFLOXACINA FARMOZ SOLUTION FOR INF 5MG/ML | TRENTON-BOMA LTD |
| HK-65662 | VOCIN 500 TABLETS 500MG | HEALTH ALLIANCE INTERNATIONAL CO LTD |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗，唯一的文獻是與 levofloxacin 療效無關的群聚事件報告，且抗菌機轉無法解釋對病毒性或微孢子蟲性病因的作用。
- 同一藥物的其他 4 個預測（多株性高黏滯症候群、高澱粉酶血症、先天性無白蛋白血症、血型不合）也都缺乏機轉依據與臨床證據，同樣建議 Hold。

**若要推進需要：**
- 取得香港衛生署核准仿單，補齊警語與禁忌症資料，才能進入安全性篩選。
- 補齊 DrugBank 作用機轉資料。
- 確認點狀上皮角膜結膜炎的病因分型，並檢索 levofloxacin 眼用製劑用於該疾病的直接臨床或前臨床研究。
- 評估給藥途徑是否相容（此項目前尚無資料）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

