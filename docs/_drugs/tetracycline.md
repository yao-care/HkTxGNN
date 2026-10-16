---
layout: default
title: Tetracycline
parent: 中證據等級 (L3-L4)
nav_order: 868
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-14
description: "Tetracycline：預測新適應症為點狀上皮角結膜炎 (Punctate Epithelial Keratoconjunctivitis)（證據等級 L4）。原適應症：泌尿道感染、支氣管炎、痤瘡、肺炎、結膜炎等"
---

# Tetracycline
{: .fs-9 }

證據等級: **L4** | 預測適應症: **4** 個
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

# Tetracycline：從細菌感染（泌尿道感染、肺炎、痤瘡等）到點狀上皮角結膜炎

## 一句話總結

Tetracycline 是廣譜四環黴素類抗生素，原本用於泌尿道感染、支氣管炎、肺炎、痤瘡、結膜炎等多種細菌感染。
TxGNN 模型預測它可能對**點狀上皮角結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇個案報告**，證據相當薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 泌尿道感染、支氣管炎、痤瘡、肺炎、結膜炎等（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 點狀上皮角結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.58% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Tetracycline 是四環黴素類抗生素，對披衣菌（Chlamydia）等病原體的抗菌活性已被證實，並已用於衣原體結膜炎（砂眼與包涵體結膜炎）。

點狀上皮角膜炎可能在衣原體感染緩解後持續或復發，因此與已核准的結膜炎適應症在疾病脈絡上相關。此外，四環黴素類藥物具有抗發炎與抑制基質金屬蛋白酶（MMP）的特性，理論上可能有助於眼表發炎。

不過要注意：TxGNN 的高分（99.58%）很可能反映的是與已知結膜炎適應症在知識圖譜中的鄰近性，而不是直接的療效證據。目前唯一的文獻只描述了「衣原體結膜炎治癒後仍出現角膜炎」，並非證明 Tetracycline 能治療該角膜炎。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | 個案報告 | Cornea | 2 例衣原體濾泡性結膜炎患者先以口服 tetracycline 或 doxycycline 治療，濾泡消退後，仍反覆出現雙側點狀上皮角膜炎 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-05419 | NEO-CYCLIN CAP 250MG | 膠囊（資料未載明） | 資料未載明 |
| HK-20019 | TETRACLIN CAP 250MG ORANGE/YELLOW | 膠囊（資料未載明） | 資料未載明 |
| HK-30208 | MEDOCYCLINE CAP 250MG | 膠囊（資料未載明） | 資料未載明 |
| HK-36081 | TETRACAP 250 CAP 250MG | 膠囊（資料未載明） | 資料未載明 |
| HK-34922 | APO-TETRA CAP 250MG | 膠囊（資料未載明） | 資料未載明 |

（共 9 張有效單方許可證，此處列出前 5 張。）

---

## 安全性考量

- **禁忌症／風險疾病（來自知識圖譜，非仿單內容）**：肝衰竭、肝病、腎病／腎衰竭、尿毒症、癲癇、糖尿病酮酸中毒、嗜中性白血球低下、顆粒球缺乏症、痛風、周邊神經病變、凝血疾病、困難梭菌結腸炎、G6PD 缺乏症、呼吸衰竭、腦部疾病等。
- **藥物交互作用**：共查得 100 筆，以下為其中的主要項目：
  - **重大 (Major)**：Isotretinoin、Acitretin、Aminolevulinic acid
  - **中度 (Moderate)**：Ethinylestradiol、Amoxicillin、Ampicillin、Aminophylline、Atovaquone、Aluminum hydroxide（含鋁制酸劑）、Bismuth subcitrate potassium 等
  - **輕微 (Minor)**：Acetazolamide、Hydrochlorothiazide、Amiloride

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測新適應症沒有任何臨床試驗，僅有 1 篇個案報告，且該報告並未證明 Tetracycline 對此疾病有療效；高 TxGNN 分數主要反映與既有結膜炎適應症的關聯。
- 同一份資料中，慢性鼻竇炎（chronic rhinosinusitis）的類別層級文獻較多，但多針對 doxycycline 而非 Tetracycline，且 doxycycline 耐受性較佳，單獨針對 Tetracycline 的研究價值有限。

**若要推進需要：**
- 取得香港衛生署仿單中的警語、禁忌症與核准適應症（目前為關鍵缺口，無法進入安全性篩選）
- 補齊作用機轉（MOA）資料
- 針對點狀上皮角結膜炎進行系統性文獻回顧，確認是否有 Tetracycline（含眼用劑型）的直接療效證據
- 釐清給藥途徑：目前路徑相容性尚未評估，口服膠囊是否適合眼表疾病需要確認
- 評估與 doxycycline 等較新藥物相比，是否具備任何優勢
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

