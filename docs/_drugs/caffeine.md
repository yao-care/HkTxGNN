---
layout: default
title: Caffeine
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 10
---

# Caffeine
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

# 咖啡因 (Caffeine)：從原適應症未登載到鼻腔疾病

## 一句話總結

咖啡因 (Caffeine) 在香港已有多張注射劑、口服液等許可證，但本次取得的資料中沒有登載核准適應症。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，
目前**沒有臨床試驗**，只有 **3 篇文獻**，且都不是針對鼻腔疾病的直接證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5（僅有模型預測，無實際研究） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。咖啡因是腺苷受體拮抗劑與磷酸二酯酶抑制劑，這些屬於一般藥理知識，本次資料並未提供。

可能的機轉假說是：咖啡因是苦味受體 (TAS2R) 的促效劑。苦味受體並不只存在於口腔，也表現在鼻腔與呼吸道的上皮細胞，並被認為與呼吸道上皮的先天防禦有關。

這只是合理但尚未證實的假說。檢索到的文獻中，一篇是咖啡因鼻用凝膠改善睡眠剝奪後認知的製劑研究，一篇是苦味受體的綜述，還有一篇是紅茶與咖啡因抑制大鼠肺癌的動物實驗。沒有任何一篇顯示咖啡因能治療鼻腔疾病。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | 綜述苦味受體 (T2R) 的藥理與其在人類呼吸道的角色；T2R 也表現於鼻腔與肺部 |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | 製劑／前臨床 | Current Drug Delivery | 咖啡因鼻用溫敏凝膠，用於改善睡眠剝奪後的認知；探討鼻腔給藥，並非治療鼻部疾病 |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | 動物實驗 | Cancer Research | 紅茶與咖啡因抑制大鼠肺癌發生；與鼻腔疾病無關 |

## 香港上市資訊

共 20 張許可證，以下列出 5 張。資料中未登載劑型與核准適應症。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-67099 | CAFFEINE CITRATE SOLUTION FOR INJECTION 10MG/1ML | THE INTERNATIONAL MEDICAL COMPANY LIMITED |
| HK-64696 | PEYONA SOLUTION FOR INFUSION AND ORAL SOLUTION 20MG/ML | ZENFIELDS (H.K.) LIMITED |
| HK-50322 | CAFFEINE CITRATE INJ 10MG/ML | JEAN-MARIE PHARMACAL CO LTD |
| HK-01025 | HO CHAI KUNG TJI THUNG SAN | KAREN LABORATORIES O/B KAREN PHARMACEUTICAL CO LTD |
| HK-50462 | NORMET TAB | VICKMANS LABORATORIES LTD |

## 安全性考量

安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 分數很高（99.91%），但沒有任何臨床試驗，文獻也沒有直接針對鼻腔疾病的證據，屬於 L5 等級。機轉上只有苦味受體這一個未經證實的假說，因此不建議推進。

**若要推進需要：**
- 取得咖啡因的作用機轉資料（DrugBank）
- 取得香港衛生署仿單，確認警語、禁忌與核准適應症（目前為阻擋性資料缺口，無法進入安全性篩選）
- 建立咖啡因與鼻腔疾病（具體疾病亞型）之間的直接研究，例如苦味受體在鼻黏膜的體外或前臨床實驗
- 釐清給藥途徑：現有許可證以注射劑與口服劑型為主，鼻腔局部給藥的可行性尚未評估

另外，同一份資料中的「睡眠性頭痛 (Hypnic Headache)」預測（證據等級 L4）有臨床綜述支持睡前咖啡因的使用，證據比鼻腔疾病強，建議優先評估。

> 本報告結果僅供研究參考，不構成醫療建議。預測的新適應症需經臨床驗證後才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

