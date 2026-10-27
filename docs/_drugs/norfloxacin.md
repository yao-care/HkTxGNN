---
layout: default
title: Norfloxacin
parent: 僅模型預測 (L5)
nav_order: 630
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Norfloxacin：預測新適應症為多發性克隆高黏滯症候群 (Polyclonal Hyperviscosity Syndrome)（證據等級 L5）。原適應症：細菌感染"
monitor_inn: "NORFLOXACIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "punctate epithelial keratoconjunctivitis"]
---

# Norfloxacin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Norfloxacin：從細菌感染到多發性克隆高黏滯症候群
{: .text-alpha }

## 一句話總結

Norfloxacin 是一種氟喹諾酮類抗菌藥物，原本用於泌尿道感染、傷寒、痢疾、細菌性肺炎等多種細菌感染。
TxGNN 模型預測它可能對**多發性克隆高黏滯症候群 (Polyclonal Hyperviscosity Syndrome)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個預測，僅屬模型推論。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 細菌感染（泌尿道感染、傷寒、痢疾、細菌性肺炎等；香港許可證未載明適應症文字） |
| 預測新適應症 | 多發性克隆高黏滯症候群 (Polyclonal Hyperviscosity Syndrome) |
| TxGNN 預測分數 | 99.70% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知的藥理學而言，Norfloxacin 是氟喹諾酮類抗菌藥物，主要抑制細菌的 DNA 旋轉酶 (DNA gyrase) 與拓撲異構酶 IV (topoisomerase IV)。

多發性克隆高黏滯症候群是因血清免疫球蛋白或其他蛋白質升高所致，不涉及細菌，Norfloxacin 沒有對應的作用標的。**目前找不到合理的機轉關聯**。

0.997 的 TxGNN 分數僅是知識圖譜的計算結果，沒有試驗或文獻佐證，不宜視為有效性的證據。

### 其他預測適應症（供參考）

| 排名 | 預測疾病 | TxGNN 分數 | 證據等級 | 評估 |
|------|---------|-----------|---------|------|
| 2 | 高澱粉酶血症 (Hyperamylasemia) | 99.70% | L5 | 為實驗室指標異常，Norfloxacin 無降澱粉酶機轉，無證據 |
| 3 | 先天性無白蛋白血症 (Congenital analbuminemia) | 99.67% | L5 | 為 ALB 基因突變疾病，抗菌藥不可能矯正，無證據 |
| 4 | 血型不合 (Blood group incompatibility) | 99.55% | L5 | 為免疫介導反應，Norfloxacin 無相關免疫調節作用，無證據 |
| 5 | 點狀上皮性角結膜炎 (Punctate epithelial keratoconjunctivitis) | 99.54% | L4 | 僅有 2 篇病例系列，機轉關聯間接且薄弱，僅適合作為研究問題 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測（多發性克隆高黏滯症候群），目前無相關文獻。

僅排名第 5 的「點狀上皮性角結膜炎」有 2 篇文獻，均為病例層級證據：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12867402](https://pubmed.ncbi.nlm.nih.gov/12867402/) | 2003 | 病例系列 | Ophthalmology | 6 例健康非免疫缺陷者的微孢子蟲角結膜炎病例報告 |
| [22959880](https://pubmed.ncbi.nlm.nih.gov/22959880/) | 2012 | 病例系列 | Am J Ophthalmol | 以反覆角膜拭擦治療微孢子蟲角結膜炎；療效較可能來自機械清創，而非藥物 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-41225 | APT-NORFLOXACIN CAP 200MG | 未載明 | 未載明 |
| HK-41226 | APT-NORFLOXACIN CAP 100MG | 未載明 | 未載明 |
| HK-50199 | MITATONIN OPHTHALMIC SOLUTION 0.3% | 未載明 | 未載明 |
| HK-58792 | BAXICIN OPHTHALMIC SOLUTION 'S.T.' 3MG/ML | 未載明 | 未載明 |
| HK-35834 | GYRABLOCK 400 TAB 400MG | 未載明 | 未載明 |

---

## 安全性考量

- **禁忌症（來自知識圖譜關聯，非仿單內容）**：包含長 QT 症候群、尖端扭轉型心律不整、肝衰竭、肝病、肝硬化、腎臟疾病、癲癇、精神疾病（焦慮症、精神病性疾患、思覺失調情感性疾患等）、血小板低下、貧血、低血鉀、肌腱炎、糖尿病與糖尿病酮酸中毒、周邊神經病變、橫紋肌溶解症等。
- **藥物交互作用**：共查詢到 100 筆，以下為部分範例：
  - **嚴重 (Major)**：Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone（皮質類固醇，與肌腱風險相關）、Bupropion、Chlorpropamide
  - **中度 (Moderate)**：Metformin、Pioglitazone、Acarbose、Alogliptin、Canagliflozin（降血糖藥，可能影響血糖）、Famotidine、Loperamide、Acetylsalicylic acid、Bisacodyl、含鈣製劑等

完整警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測疾病沒有任何臨床試驗或文獻，也找不到合理的機轉關聯，證據等級為 L5，僅是模型預測。
- 安全性方面，Norfloxacin 有多項知識圖譜標示的禁忌與大量交互作用，在缺乏療效證據下不值得承擔這些風險。

**若要推進需要：**
- 提出具體的機轉假說（目前無法由 Norfloxacin 的抗菌機轉解釋）
- 取得香港衛生署仿單的警語與禁忌症資料
- 補充作用機轉（MOA）資料
- 若有興趣，可將排名第 5 的點狀上皮性角結膜炎作為研究問題，先進行體外微孢子蟲敏感性試驗，再考慮臨床研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

