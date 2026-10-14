---
layout: default
title: Vancomycin
parent: 僅模型預測 (L5)
nav_order: 925
evidence_level: L5
indication_count: 5
---

# Vancomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Vancomycin：從困難梭狀芽孢桿菌結腸炎到瀰漫性硬皮症

## 一句話總結

Vancomycin 是一種糖肽類抗生素，原本用於困難梭狀芽孢桿菌結腸炎、金黃色葡萄球菌感染、心內膜炎等革蘭氏陽性菌感染。
TxGNN 模型預測它可能對**瀰漫性硬皮症 (Diffuse Scleroderma)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇**相關性很低的病例報告，證據非常薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 困難梭狀芽孢桿菌結腸炎、金黃色葡萄球菌感染、心內膜炎、細菌性關節炎、葡萄球菌肺炎等（香港許可證未載明適應症文字，此處依知識圖譜資料） |
| 預測新適應症 | 瀰漫性硬皮症 (Diffuse Scleroderma) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 7 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Vancomycin 是糖肽類抗生素，透過抑制細菌細胞壁合成來殺菌，主要作用於革蘭氏陽性菌。

瀰漫性硬皮症是一種自體免疫性、纖維化的疾病，與細菌感染的病理機轉並無直接關聯。目前**找不到合理的機轉連結**，0.999 的高分較可能來自知識圖譜中的關聯性推論，缺乏生物學上的支持。

唯一檢索到的文獻是一篇伴隨敗血症與嗜酸性球增多的紅皮症病例報告，並未討論硬皮症的治療，因此不能視為支持證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case report | The American Journal of Case Reports | 一名 56 歲男性出現泛發性脫屑性皮疹，合併敗血症與嗜酸性球增多，討論是否為紅皮症；與硬皮症治療無關 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68968 | MYCOVAN POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION AND ORAL SOLUTION 500MG | 未提供 | 未提供 |
| HK-65454 | VONDEM POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG | 未提供 | 未提供 |
| HK-33907 | VANCOMYCIN HCL FOR INJ 500MG IV | 未提供 | 未提供 |
| HK-68633 | VANCOMYCIN POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG | 未提供 | 未提供 |
| HK-64106 | VANCOMYCIN KABI POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 500MG | 未提供 | 未提供 |

（另有 2 張有效許可證，共 7 張，皆為單方製劑。）

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（非仿單內容）：腎臟疾病、輸尿管積膿、嗜中性白血球低下、顆粒球缺乏症、聽力障礙、聽覺系統疾病。
- **藥物交互作用**：共查得 100 筆，以下列出部分：
  - **重大 (Major)**：人類免疫球蛋白 G（靜脈注射）、人類肉毒桿菌神經毒素 A/B 免疫球蛋白、霍亂弧菌 CVD 103-HgR 活疫苗
  - **中度 (Moderate)**：Amphotericin B、Amikacin、Capreomycin、Carboplatin、Bacitracin（常涉及腎毒性或耳毒性疊加）；Ketorolac、Ibuprofen、Diclofenac、Celecoxib 等 NSAID；Metformin、Cholestyramine、Mesalazine 等

其餘警語與仿單禁忌資料請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有臨床試驗，唯一文獻為不相關的病例報告，且無合理的機轉連結，高 TxGNN 分數僅屬計算預測。
- Vancomycin 具腎毒性與耳毒性風險，用於慢性自體免疫疾病的風險效益並不明確。

**若要推進需要：**
- 補充作用機轉資料，並說明其與纖維化或自體免疫機轉的可能關聯
- 進行系統性文獻檢索，確認是否有硬皮症相關的前臨床或臨床證據
- 取得香港仿單的警語、禁忌與核准適應症
- 若有前臨床證據支持，再評估給藥途徑與長期用藥的安全性

---

**補充觀察：**本次預測清單中，副傷寒與沙門氏菌病（排名 2、3）因革蘭氏陰性菌的外膜屏障，vancomycin 並無有效抗菌活性；先天性無白蛋白血症與高澱粉酶血症（排名 4、5）亦無機轉依據，也沒有任何研究，皆建議 Hold。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

