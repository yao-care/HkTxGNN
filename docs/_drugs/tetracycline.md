---
layout: default
title: Tetracycline
parent: 僅模型預測 (L5)
nav_order: 868
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "TETRACYCLINE"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "chronic ethmoidal sinusitis", "chronic rhinosinusitis", "paranasal sinus neoplasm (disease)"]
description: "Tetracycline：預測新適應症為點狀上皮角結膜炎 (punctate epithelial keratoconjunctivitis)（證據等級 L5）。香港藥劑製品註冊：9 張（有效 8 張）"
---

# Tetracycline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

## Tetracycline: 點狀上皮角結膜炎 (punctate epithelial keratoconjunctivitis)
{: .text-alpha }

## 一句話總結

Tetracycline 是廣譜四環黴素類抗生素，原本用於泌尿道感染、支氣管炎、肺炎、痤瘡、結膜炎等多種細菌感染。
TxGNN 模型預測它可能對**點狀上皮角結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇個案報告**，證據相當薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 點狀上皮角結膜炎 (punctate epithelial keratoconjunctivitis) |
| TxGNN 預測分數 | 0.9958 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 8 張／共 9 張） |
| 許可證數 | 9 張（有效 8 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

ChEMBL（EMBL-EBI）收錄的 Tetracycline 作用機轉（非官方翻譯）：「細菌 70S 核糖體抑制劑」。英文原文："Bacterial 70S ribosome inhibitor"（[ChEMBL CHEMBL1440 (tetracycline): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1440)，CC BY-SA 3.0；查閱日期 2026-11-19）。根據已知資訊，Tetracycline 是四環黴素類抗生素，對披衣菌（Chlamydia）等病原體的抗菌活性已被證實，並已用於衣原體結膜炎（砂眼與包涵體結膜炎）。

點狀上皮角膜炎可能在衣原體感染緩解後持續或復發，因此與已核准的結膜炎適應症在疾病脈絡上相關。此外，四環黴素類藥物具有抗發炎與抑制基質金屬蛋白酶（MMP）的特性，理論上可能有助於眼表發炎。

不過要注意：TxGNN 的高分（0.9958）來自 TxGNN 模型（深度學習），可能反映的是模型學到的相關疾病之間的相似性，而不是生物學證據或直接的療效證據。目前唯一的文獻只描述了「衣原體結膜炎治癒後仍出現角膜炎」，並非證明 Tetracycline 能治療該角膜炎。

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

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-05419 | NEO-CYCLIN CAP 250MG | 單一成分 | NEOCHEM PHARMACEUTICAL LABORATORIES LTD. | 有效 |
| HK-20019 | TETRACLIN CAP 250MG ORANGE/YELLOW | 單一成分 | UNICORN LABORATORIES O/B AMERICAN UNICORN LABORATORIES LIMITED | 有效 |
| HK-30208 | MEDOCYCLINE CAP 250MG | 單一成分 | STAR MEDICAL SUPPLIES LTD | 有效 |
| HK-36081 | TETRACAP 250 CAP 250MG | 單一成分 | HOVID LIMITED | 有效 |
| HK-34922 | APO-TETRA CAP 250MG | 單一成分 | HIND WING CO LTD | 已註銷 |

上表列出其中 5 張（共 9 張）。

<!-- licenses:end -->

（共 9 張單方許可證，8 張有效、HK-34922 已註銷；此處列出前 5 張。）

<!-- review:begin hk-lic-20261117-tetracycline-1 -->

> **查核更正（2026-11-17）**：原文為「（共 9 張有效單方許可證，」。已更正：HK-34922 已不列於衞生署藥物辦公室的註冊藥劑製品名單，網上藥物資料庫也查不到，已不是現行註冊（2026-11-17 核對）。依據：[衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html)。

<!-- review:end hk-lic-20261117-tetracycline-1 -->

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

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄：內容已對照衞生署藥物辦公室的藥劑製品註冊資料。更正只限基本事實，模型預測、證據等級與結論未有改寫。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-17 | 「（共 9 張有效單方許可證，」→「（共 9 張單方許可證，8 張有效、HK-34922 已註銷；」 | 更正 | [衞生署藥物辦公室 註冊藥劑製品名單 DrugList.xml（lastUpdate 2026-11-13）](https://www.drugoffice.gov.hk/eps/psi/DrugList.xml)；[data.gov.hk 歷史存檔：DrugList.xml 每週版本（2025-08-04～2026-11-16）](https://api.data.gov.hk/v1/historical-archive/list-file-versions?url=http%3A%2F%2Fwww.drugoffice.gov.hk%2Feps%2Fpsi%2FDrugList.xml&start=20250801&end=20261116)；[衞生署藥物辦公室 搜尋藥物資料庫（依註冊號查詢）](https://www.drugoffice.gov.hk/eps/do/en/consumer/search_drug_database.html) |
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄（2026-11-20 修訂，前版保留於紀錄） | [ChEMBL CHEMBL1440 (tetracycline): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1440) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

