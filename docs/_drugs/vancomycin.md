---
layout: default
title: Vancomycin
parent: 僅模型預測 (L5)
nav_order: 925
evidence_level: L5
indication_count: 10
monitor_inn: "VANCOMYCIN"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
last_modified_at: 2026-10-28
description: "Vancomycin：預測新適應症為瀰漫性硬皮症 (Diffuse Scleroderma)（證據等級 L5）。原適應症：知識圖譜記錄的關聯：艱難梭菌結腸炎、葡萄球菌感染、心內膜炎等"
---

# Vancomycin
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

## Vancomycin：從艱難梭菌結腸炎與葡萄球菌感染到瀰漫性硬皮症
{: .text-alpha }

## 一句話總結

Vancomycin 是一種糖肽類抗生素，知識圖譜中記錄的用途包括艱難梭菌結腸炎、葡萄球菌感染、心內膜炎與葡萄球菌肺炎等。
TxGNN 模型預測它可能對**瀰漫性硬皮症 (Diffuse Scleroderma)** 有效，但目前**沒有臨床試驗**，僅有 1 篇不直接相關的病例報告，這個預測屬於模型推論，缺乏實質證據。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯：艱難梭菌結腸炎、葡萄球菌感染、心內膜炎等（本地許可證未載明適應症文字） |
| 預測新適應症 | 瀰漫性硬皮症 (Diffuse Scleroderma) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 7 張／共 7 張） |
| 許可證數 | 7 張（有效 7 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知的藥理學而言，Vancomycin 是糖肽類抗生素，透過抑制細菌細胞壁合成，對革蘭氏陽性菌發揮作用。

瀰漫性硬皮症是一種自體免疫性纖維化疾病，與細菌細胞壁合成沒有可辨識的機轉關聯。因此，這個高分預測來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據。

唯一檢索到的文獻是一篇關於伴隨敗血症與嗜酸性白血球增多的瀰漫性剝脫性皮疹的病例報告，並非研究 Vancomycin 治療硬皮症，不構成直接支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | 病例報告 | The American Journal of Case Reports | 一名 56 歲男性出現伴隨敗血症與嗜酸性白血球增多的瀰漫性剝脫性皮疹（紅皮症），並非硬皮症，與本預測無直接關聯 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68968 | MYCOVAN POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION AND ORAL SOLUTION 500MG | 未載明 | 未載明 |
| HK-65454 | VONDEM POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG | 未載明 | 未載明 |
| HK-33907 | VANCOMYCIN HCL FOR INJ 500MG IV | 未載明 | 未載明 |
| HK-68633 | VANCOMYCIN POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG | 未載明 | 未載明 |
| HK-64106 | VANCOMYCIN KABI POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG | 未載明 | 未載明 |

本藥共 7 張單一成分許可證，上表僅列出前 5 張。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單內容）：腎臟疾病、輸尿管膿腫、嗜中性白血球低下、顆粒球缺乏症、聽力障礙、聽覺系統疾病。
- **藥物交互作用**：共查得 100 筆，以下為部分範例。
  - 重大 (Major)：人類免疫球蛋白 G（靜脈注射）、人類肉毒桿菌神經毒素 A/B 免疫球蛋白、霍亂弧菌 CVD 103-HgR 活疫苗。
  - 中度 (Moderate)：Amphotericin B、Amikacin、Capreomycin、Carboplatin、Bacitracin、Ketorolac、Ibuprofen、Diclofenac、Celecoxib、Metformin、Cholestyramine 等；其中多為腎毒性或耳毒性疊加的組合。

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測缺乏機轉依據，Vancomycin 為抗菌藥物，而硬皮症為自體免疫纖維化疾病；分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據。
- 無臨床試驗，僅有一篇不相關病例報告，證據等級為 L5。

**若要推進需要：**
- 提出合理的生物學假說（例如抗菌以外的免疫調節作用）並進行前臨床驗證。
- 補充作用機轉資料與仿單警語、適應症文字。
- 若要探索 Vancomycin 的新用途，可優先評估機轉上較合理的革蘭氏陽性菌感染相關適應症（例如肺炎鏈球菌肺炎，但目前證據仍屬間接，且需注意既有臨床用法與耐受株問題），而非硬皮症。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

