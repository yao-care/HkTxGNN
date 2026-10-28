---
layout: default
title: Norfloxacin
parent: 僅模型預測 (L5)
nav_order: 630
evidence_level: L5
indication_count: 10
monitor_inn: "NORFLOXACIN"
predicted_indications: ["polyclonal hyperviscosity syndrome", "hyperamylasemia", "congenital analbuminemia", "blood group incompatibility", "punctate epithelial keratoconjunctivitis", "premalignant hematological system disease", "diffuse scleroderma", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-10-23
description: "Norfloxacin：預測新適應症為多株性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome)（證據等級 L5）。原適應症：知識圖譜中記錄的關聯：傷寒、沙門氏菌感染、泌尿道感染、支氣管炎、細菌性肺炎、痢疾等"
---

# Norfloxacin
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

## Norfloxacin：從細菌感染到多株性高黏滯症候群（預測）
{: .text-alpha }

## 一句話總結

Norfloxacin 是一種氟喹諾酮類抗菌藥，知識圖譜中記錄的原有用途包含泌尿道感染、傷寒、痢疾等細菌感染。
TxGNN 模型預測分數最高的新適應症為**多株性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome)**，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的關聯：傷寒、沙門氏菌感染、泌尿道感染、支氣管炎、細菌性肺炎、痢疾等（香港許可證未提供核准適應症文字，無法確認核准適應症） |
| 預測新適應症 | 多株性高黏滯症候群 (Polyclonal Hyperviscosity Syndrome) |
| TxGNN 預測分數 | 0.9970 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 5 張／共 5 張） |
| 許可證數 | 5 張（有效 5 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知的藥理類別而言，Norfloxacin 屬氟喹諾酮類抗菌藥，一般認為是抑制細菌 DNA 旋轉酶 (DNA gyrase) 與拓樸異構酶 IV，用於細菌感染。

多株性高黏滯症候群源於免疫球蛋白過多，並非細菌感染所致。抗菌藥物無法處理這個病理過程，因此**機轉上找不到合理的連結**。0.9970 的分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，並非生物學證據，也沒有臨床試驗或文獻佐證，應視為模型假說而非可行的再利用方向。

**其他預測的新適應症（同為模型預測，供參考）：**

| 排名 | 預測疾病 | 分數 | 證據等級 | 說明 |
|------|---------|------|---------|------|
| 2 | 高澱粉酶血症 | 0.9970 | L5 | 實驗室指標異常，無機轉依據 |
| 3 | 先天性無白蛋白血症 | 0.9967 | L5 | 基因疾病，抗菌藥無法矯正 |
| 4 | 血型不合 | 0.9955 | L5 | 免疫血液學反應，無機轉依據 |
| 5 | 點狀上皮角膜結膜炎 | 0.9954 | L5 | 僅有間接文獻，未直接研究此疾病（見下方說明） |
| 6 | 癌前血液系統疾病 | 0.9948 | L5 | 無機轉依據 |
| 7 | 瀰漫性硬皮症 | 0.9944 | L5 | 無抗纖維化或免疫調節作用 |
| 8 | 單株免疫球蛋白病變 | 0.9942 | L5 | 文獻僅談抗藥性，非療效證據 |
| 9 | 伴隨週邊神經病變的血液疾病 | 0.9938 | L5 | 氟喹諾酮本身有週邊神經病變風險，不利使用 |
| 10 | 敗血性鼠疫 | 0.9937 | L5 | 僅有間接的動物/體外研究，無直接研究此疾病的 norfloxacin 證據 |

排名第 5 與第 10 的疾病所附文獻，分別談的是微孢子蟲角膜結膜炎和霍亂弧菌/鼠疫預防的動物實驗，並未直接以 norfloxacin 研究該預測疾病本身的療效，因此依規則證據等級一律定為 L5。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對排名第一的預測適應症（多株性高黏滯症候群），目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-41225 | APT-NORFLOXACIN CAP 200MG | 未提供 | 未提供 |
| HK-41226 | APT-NORFLOXACIN CAP 100MG | 未提供 | 未提供 |
| HK-50199 | MITATONIN OPHTHALMIC SOLUTION 0.3% | 未提供 | 未提供 |
| HK-58792 | BAXICIN OPHTHALMIC SOLUTION 'S.T.' 3MG/ML | 未提供 | 未提供 |
| HK-35834 | GYRABLOCK 400 TAB 400MG | 未提供 | 未提供 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜，並非仿單內容）：長 QT 症候群、尖端扭轉型心室頻脈、癲癇、肝衰竭、腎臟疾病、肝硬化、血小板低下、精神疾病、糖尿病及酮酸中毒、週邊神經病變、肌腱炎、橫紋肌溶解症、貧血、低血鉀等。
- **藥物交互作用**：資料庫共查得 100 筆，以下為部分重點：
  - 嚴重 (Major)：Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone（皮質類固醇，須留意肌腱風險）、Bupropion、Chlorpropamide
  - 中度 (Moderate)：Metformin、Pioglitazone、Acarbose、Canagliflozin（降血糖藥，須留意血糖波動）、Famotidine、Loperamide、Acetylsalicylic acid、含鈣製劑等

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第一的預測適應症沒有任何臨床試驗或文獻，機轉上也無合理連結，證據等級僅為 L5。
- 前十名預測中，沒有任何一項有直接研究該疾病的證據，不建議投入資源。

**若要推進需要：**
- 取得完整的作用機轉資料，並重新評估預測疾病與抗菌機轉的關聯。
- 取得香港衛生署仿單的警語、禁忌與核准適應症文字。
- 若仍想探索，可優先以體外或動物模型進行初步驗證，再評估是否規劃臨床研究。
- 若目標是抗菌用途（如鼠疫），其他氟喹諾酮（如 ciprofloxacin、levofloxacin）可能是更合適的候選藥物。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

