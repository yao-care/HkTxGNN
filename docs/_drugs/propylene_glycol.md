---
layout: default
title: Propylene Glycol
parent: 僅模型預測 (L5)
nav_order: 741
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Propylene Glycol：預測新適應症為支氣管炎 (Bronchitis)（證據等級 L5）。原適應症：乾眼症、乾眼病（xerophthalmia）"
monitor_inn: "PROPYLENE GLYCOL"
predicted_indications: ["bronchitis", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "cortical cataract", "nuclear senile cataract"]
---

# Propylene Glycol
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

# Propylene Glycol：從乾眼症到支氣管炎

## 一句話總結

Propylene Glycol（丙二醇）是眼用潤滑劑與藥劑賦形劑的常見成分，原本用於乾眼症與乾眼病（xerophthalmia）。
TxGNN 模型預測它可能對**支氣管炎 (Bronchitis)** 有效，但目前**沒有任何臨床試驗**，且檢索到的 3 篇文獻並不支持治療用途，整體僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 乾眼症、乾眼病（xerophthalmia）（香港許可證未載明核准適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 支氣管炎 (Bronchitis) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，丙二醇是眼用潤滑滴眼液的成分之一，主要作用為保濕與潤滑眼表，在乾眼症中的用途已為人熟知。但這種潤滑作用與支氣管炎的病理機轉並無明確關聯。

**這個預測缺乏機轉與臨床支持。** 檢索到的文獻主要討論丙二醇作為電子菸載體成分，可能是呼吸道刺激物，並與氣道疾病風險有關，方向與治療效果相反。另一篇 quercetin 的小鼠研究與丙二醇無關。TxGNN 的高分（99.90%）僅是模型輸出，應視為待驗證的假說，而非有效性的證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [26408554](https://pubmed.ncbi.nlm.nih.gov/26408554/) | 2015 | Review | Am J Physiol Lung Cell Mol Physiol | 討論長期使用電子菸是否導致肺部疾病，涉及慢性支氣管炎與 COPD 風險；屬風險討論，非治療證據 |
| [28983782](https://pubmed.ncbi.nlm.nih.gov/28983782/) | 2017 | Review | Curr Allergy Asthma Rep | 電子菸液及氣霧含氣道刺激物，可能與氣喘等肺部疾病的發生與惡化有關 |
| [20920189](https://pubmed.ncbi.nlm.nih.gov/20920189/) | 2010 | 前臨床（動物研究） | Respir Res | Quercetin 在小鼠 COPD 模型中減輕肺部發炎；與丙二醇無關 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-59636 | SYSTANE ULTRA LUBRICANT EYE DROPS | 未載明 | 未載明 |
| HK-61280 | SYSTANE ULTRA LUBRICANT EYE DROPS PRESERVATIVE FREE | 未載明 | 未載明 |
| HK-67320 | SYSTANE ULTRA LUBRICANT EYE DROPS | 未載明 | 未載明 |

三張許可證皆為單方、有效，持有者為 ALCON HONG KONG LTD。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 支氣管炎的預測只有模型分數支持，沒有臨床試驗，現有文獻甚至指出丙二醇（以吸入方式暴露時）可能刺激呼吸道，與治療方向相反。
- 丙二醇在香港的現有用途是眼用潤滑，與支氣管炎的給藥途徑和病理機轉皆不相符。

**若要推進需要：**
- 取得丙二醇的作用機轉資料，評估與支氣管炎之間是否有合理的生物學連結
- 取得香港仿單的警語與禁忌資料，完成安全性篩選
- 以吸入方式暴露的呼吸道安全性資料（現有文獻顯示可能有刺激性風險）
- 至少有前臨床或小型臨床研究，直接檢驗丙二醇對支氣管炎的效果

---

### 附註：其他預測適應症

資料中另有四個預測適應症，證據同樣薄弱，皆建議 Hold：

| 預測適應症 | TxGNN 分數 | 證據等級 | 說明 |
|-----------|-----------|---------|------|
| 重度非增殖性糖尿病視網膜病變 | 99.82% | L5 | 無試驗與文獻；丙二醇無已知抗血管新生或微血管相關機轉 |
| 糖尿病視網膜病變 | 99.68% | L4 | 僅有間接證據：一項 Phase 4 試驗（NCT07090044）比較注射後止痛滴眼液，探討的是程序性疼痛而非疾病；PMID 39006273 研究的是不同化合物（丙二醇甘露糖酯硫酸鹽）；其餘兩篇為其他藥物的製劑研究 |
| 皮質性白內障 | 99.56% | L5 | 無試驗與文獻，無合理機轉 |
| 核性老年性白內障 | 99.56% | L5 | 無試驗與文獻，無合理機轉 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

