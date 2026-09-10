---
layout: default
title: Potassium Iodide
parent: 中證據等級 (L3-L4)
nav_order: 606
evidence_level: L4
indication_count: 2
---

# Potassium Iodide
{: .fs-9 }

證據等級: **L4** | 預測適應症: **2** 個
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

# 碘化鉀：原適應症資料缺失，TxGNN 預測可能適用於鼻腔疾病

## 一句話總結

碘化鉀（Potassium Iodide, DB06715）目前缺乏 DrugBank 原適應症與作用機轉資料，且尚未在香港上市。
TxGNN 模型預測它可能對**鼻腔疾病 (Nasal Cavity Disease)** 有效，
目前僅有 **4 篇文獻**（多為獸醫案例報告）支持，尚無臨床試驗登記，證據等級為 L4。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺失（DrugBank 未提供原適應症，香港無許可證資料可供比對） |
| 預測新適應症 | 鼻腔疾病 (Nasal Cavity Disease) |
| TxGNN 預測分數 | 99.95%（排名 1367） |
| 證據等級 | L4 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏碘化鉀的詳細作用機轉資料（DrugBank MOA 標註為資料缺口），原適應症亦無記錄可查。

根據現有 4 篇文獻，碘化鉀的飽和溶液（SSKI, saturated solution of potassium iodide）具有已知的抗真菌／抗卵菌（oomycete）活性，歷史上曾用於孢子絲菌病等皮膚黏膜真菌感染的治療，機轉可能與碘離子破壞病原體細胞壁或誘導宿主免疫調節有關。

這 4 篇文獻均為「鼻腔黴菌性／卵菌性感染」個案報告，與 TxGNN 預測的廣義「鼻腔疾病」高分關聯相符，但實際上僅支持窄範圍的特定病原體感染適應症（如鼻孢子蟲病、麴菌性鼻炎、接合菌病），而非鼻腔疾病整體，需留意預測範圍與實際證據範圍不完全對等。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [34902797](https://pubmed.ncbi.nlm.nih.gov/34902797/) | 2022 | Case Report（獸醫，羊） | Journal de mycologie medicale | 碘化鉀成功治療綿羊鼻面部鼻孢子蟲病（pythiosis） |
| [39576399](https://pubmed.ncbi.nlm.nih.gov/39576399/) | 2024 | Case Report（獸醫，馬） | Veterinary research communications | 局部 clotrimazole 合併口服碘化鉀治療馬匹麴菌性鼻炎 |
| [10976304](https://pubmed.ncbi.nlm.nih.gov/10976304/) | 2000 | Case Report（獸醫，馬） | Journal of the American Veterinary Medical Association | Pseudallescheria boydii 鼻腔感染，以鼻內 miconazole 併靜脈碘化鈉治療（非碘化鉀） |
| [7997795](https://pubmed.ncbi.nlm.nih.gov/7997795/) | 1994 | Case Report（人類） | Revista do Instituto de Medicina Tropical de Sao Paulo | 巴西鼻面部接合菌病（zygomycosis）病例，碘化鉀治療後快速緩解 |

**注意**：4 篇文獻中 3 篇為獸醫學案例，僅 1 篇為人類病例，且均為個案報告等級，尚無人體對照試驗支持。

## 香港上市資訊

香港目前未上市，無許可證資料。

## 安全性考量

安全性資訊請參考原廠仿單。

（註：TFDA／仿單警語與禁忌症資料為阻斷性缺口 DG001，尚未取得，無法進行 S1 安全性初評。）

## 結論與下一步

**決策：Hold**

**理由：**
- 現有證據僅來自 4 篇個案報告（多數為獸醫學文獻），無任何臨床試驗或人體對照研究，證據等級 L4，不足以支持推進。
- 藥物的作用機轉、原適應症、香港上市及安全性（警語／禁忌症）資料均為缺失，其中仿單警語資料屬阻斷性缺口（DG001），已無法進入安全性初評（S1）階段。

**若要推進需要：**
- 取得 TFDA／原廠仿單警語與禁忌症資料（解除 DG001 阻斷）
- 補齊 DrugBank 作用機轉（MOA）資料（DG002）
- 尋找或推動人體臨床試驗，驗證碘化鉀對鼻腔黴菌／卵菌感染的療效
- 確認香港上市與許可證狀況

*附註：TxGNN 同時預測「急性喉咽炎 (acute laryngopharyngitis)」為候選適應症（分數 99.95%），但無任何臨床試驗或文獻支持，證據等級為 L5（純模型預測），暫不建議進一步評估。*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

