---
layout: default
title: Triamcinolone
parent: 僅模型預測 (L5)
nav_order: 903
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Triamcinolone：預測新適應症為禿髮性黏蛋白症 (Alopecia Mucinosa)（證據等級 L5）。原適應症：自體免疫疾病、克隆氏症／發炎性腸道疾病、腎上腺功能不全、先天性腎上腺增生等"
monitor_inn: "Triamcinolone"
predicted_indications: ["alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo"]
---

# Triamcinolone
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

## Triamcinolone：從自體免疫與發炎性疾病到禿髮性黏蛋白症（Alopecia Mucinosa）
{: .text-alpha }

## 一句話總結

Triamcinolone（去炎松）是一種強效糖皮質類固醇，原本用於自體免疫疾病、發炎性腸道疾病、腎上腺功能不全及相關血液腫瘤等適應症。
TxGNN 模型預測它可能對**禿髮性黏蛋白症 (Alopecia Mucinosa)** 有效，但目前**沒有臨床試驗**，僅有 **2 篇個案報告**，且其中一篇討論的是 bexarotene 凝膠而非 triamcinolone，證據相當薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 自體免疫疾病、克隆氏症／發炎性腸道疾病、腎上腺功能不全、先天性腎上腺增生等（來自知識圖譜；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 禿髮性黏蛋白症 (Alopecia Mucinosa) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L4（僅有個案報告與機轉推論，無直接臨床證據） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Triamcinolone 屬於強效糖皮質類固醇，具有抗發炎與免疫抑制作用，在多種自體免疫與發炎性疾病中的療效已被證實。

禿髮性黏蛋白症（毛囊黏蛋白症）的特徵是毛囊周圍淋巴球浸潤及黏蛋白沉積。因此，局部（病灶內注射或外用）類固醇在機轉上是合理的嘗試方向。

但需要強調：TxGNN 分數雖高，現有文獻僅為個案報告，且其中 2014 年的報告討論的是 bexarotene 凝膠，並非 triamcinolone。因此高分並未獲得針對此藥物的臨床證據支持。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [23968145](https://pubmed.ncbi.nlm.nih.gov/23968145/) | 2014 | 個案報告 | Int J Dermatol | 以 bexarotene 凝膠成功治療持續性特發性毛囊黏蛋白症，與 triamcinolone 無直接關係 |
| [14170262](https://pubmed.ncbi.nlm.nih.gov/14170262/) | 1964 | 個案報告 | Hifuka kiyo. Acta dermatologica | 禿髮性黏蛋白症（Pinkus 型）個案，無摘要可供判讀 |

---

## 香港上市資訊

香港共有 20 張有效單一成分許可證，皆為外用、口腔用或鼻用製劑。以下列出 5 張主要許可證；資料中未載明劑型與核准適應症。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-53955 | MECOL ORABASE OINTMENT 1MG/G | 資料未載明 | 資料未載明 |
| HK-63140 | KOWELL ORABASE PASTE 0.1%W/W | 資料未載明 | 資料未載明 |
| HK-64378 | EURALOG PASTE 0.1% W/W | 資料未載明 | 資料未載明 |
| HK-57710 | SUNBIN MEDICINE CREAM 0.1% | 資料未載明 | 資料未載明 |
| HK-65848 | APO-TRIAMCINOLONE AQ NASAL SPRAY 55MCG/DOSE | 資料未載明 | 資料未載明 |

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（來自知識圖譜，非仿單內容）：高血壓、癲癇、肝臟疾病、膽囊疾病、高血糖、麻疹、充血性心衰竭、單純疱疹病毒角膜炎，以及多種腦下垂體功能低下相關疾病。
- **藥物交互作用**：資料庫共記錄 100 筆，其中顯示者包括：
  - 重大 (Major)：Adalimumab
  - 中等 (Moderate)：Zidovudine、Isotretinoin、Acarbose、Acebutolol、Acetazolamide、Ketorolac、Nifedipine、Ibuprofen、Ethinylestradiol 等
  - 輕微 (Minor)：Formoterol、Salbutamol

仿單的警語與禁忌症資料尚未取得，詳細安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 雖然 TxGNN 分數很高，但沒有任何臨床試驗，文獻僅有兩篇個案報告，其中一篇還是不同藥物，無法支持 triamcinolone 對此疾病的療效。
- 此預測目前只能視為研究假說。

**若要推進需要：**
- 系統性檢索 triamcinolone（尤其是病灶內注射）用於毛囊黏蛋白症的病例系列或回顧性研究
- 取得香港仿單的警語與禁忌症，並補齊作用機轉資料
- 確認劑型可行性（香港現有製劑多為外用、口腔用及鼻用，病灶內注射劑型是否可取得需另行確認）
- 評估該病與皮膚 T 細胞淋巴瘤的關聯，並設計皮膚病理追蹤
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

