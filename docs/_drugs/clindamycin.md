---
layout: default
title: Clindamycin
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Clindamycin：預測新適應症為點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)（證據等級 L5）。原適應症：痤瘡、鏈球菌感染、金黃色葡萄球菌感染、厭氧菌感染、細菌性陰道病等"
---

# Clindamycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Clindamycin：從痤瘡與細菌感染到點狀上皮角膜結膜炎

## 一句話總結

Clindamycin（克林黴素）是一種林可胺類抗生素，原本用於痤瘡、鏈球菌與葡萄球菌感染、厭氧菌感染及細菌性陰道病等。
TxGNN 模型預測它可能對**點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效，但目前**沒有臨床試驗也沒有文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 痤瘡、鏈球菌感染、金黃色葡萄球菌感染、厭氧菌感染、細菌性陰道病等（香港許可證未登載適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Clindamycin 是細菌蛋白質合成抑制劑，作用於 50S 核糖體次單位，對革蘭氏陽性菌與厭氧菌有效。

點狀上皮角膜結膜炎多為病毒性或毒性/發炎性成因，抗菌機轉與其病因的關聯並不明確。因此這個預測目前較像是模型根據圖譜關聯所產生，缺乏機轉上的支持。

另外，排名第 2 的**暴露性角膜炎 (Exposure Keratitis)** 有間接合理性：此病可能繼發細菌感染，而相關文獻中的金黃色葡萄球菌、蠟樣芽孢桿菌屬於 Clindamycin 的抗菌範圍。但這些文獻談的是一般感染性角膜炎，並未評估 Clindamycin 的療效，眼部給藥與角膜穿透性也無資料。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（備註：其他較低排名的預測適應症有少量文獻，但多為感染性角膜炎的病例或流行病學研究，或獸醫研究，並未直接評估 Clindamycin 對該適應症的效果。）

---

## 香港上市資訊

下表列出 5 張主要許可證（共 20 張，均為有效的單方製劑）。資料中未登載劑型與核准適應症。

| 許可證號 | 品名 | 製造商 |
|---------|------|-------|
| HK-47355 | FUMICA GEL 1% | EUROPHARM LAB CO LTD |
| HK-62155 | EFFEXIA ACNE TOPICAL SOLUTION 1%W/V | EUROPHARM LAB CO LTD |
| HK-50033 | CLINDAMYCIN PHOS. INJ 150MG/ML (XINHUA) | JINDUN PHARMA (H.K.) LIMITED |
| HK-46045 | EDASON TOPICAL SOLUTION 1% | JULIUS CHEN & COMPANY (HK) LIMITED |
| HK-65372 | BIBI GEL 1% W/W | WILCOME PHARMACEUTICAL CO LTD |

多數產品為 1% 外用凝膠或外用溶液（痤瘡用），另有一款注射劑。

---

## 安全性考量

- **知識圖譜中的禁忌疾病**：肝衰竭、曬傷、克隆氏症、發炎性腸道疾病、克隆氏結腸炎、異位性皮膚炎、剝脫性皮膚炎、腹瀉性疾病、困難梭狀芽孢桿菌結腸炎、新生兒壞死性腸炎、皮膚炎、潰瘍性結腸炎、外陰陰道念珠菌病（此為圖譜關聯，非仿單原文）。
- **藥物交互作用**：共查得 100 筆。中度交互作用包括 Balsalazide、Clarithromycin、Picosulfuric acid、Attapulgite、Kaolin；其餘如 Amphotericin B、Acetylsalicylic acid、Amoxicillin、Vancomycin、Morphine 等的嚴重度未明。

仿單的警語與禁忌資料尚未取得，詳細安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 點狀上皮角膜結膜炎的預測僅來自模型（L5），沒有任何試驗或文獻，且該病多為病毒性或發炎性，抗菌機轉無法解釋其療效。
- 香港仿單的安全性資料尚缺，且機轉資料也有缺口。

**若要推進需要：**
- 補齊 Clindamycin 的作用機轉資料與香港仿單的警語、禁忌資料
- 確認點狀上皮角膜結膜炎中是否有細菌參與的病理機轉
- 評估眼部給藥劑型與角膜穿透性（現有香港產品多為皮膚用，並無眼用製劑）
- 若要探索眼科方向，可優先考慮證據間接較多的「暴露性角膜炎繼發細菌感染」，並先進行文獻回顧與前臨床研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

