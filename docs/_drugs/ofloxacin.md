---
layout: default
title: Ofloxacin
parent: 僅模型預測 (L5)
nav_order: 638
evidence_level: L5
indication_count: 10
monitor_inn: "OFLOXACIN"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-10-28
description: "Ofloxacin：預測新適應症為高澱粉酶血症 (Hyperamylasemia)（證據等級 L5）。原適應症：知識圖譜記錄的關聯包括傷寒、沙門氏菌感染、泌尿道感染、支氣管炎、細菌性肺炎等"
---

# Ofloxacin
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

## Ofloxacin：從細菌感染症到高澱粉酶血症
{: .text-alpha }

## 一句話總結

Ofloxacin 是一種氟喹諾酮類抗菌藥物，知識圖譜中記錄的相關感染症包括傷寒、泌尿道感染、支氣管炎與細菌性肺炎等。
TxGNN 模型預測它可能對**高澱粉酶血症 (Hyperamylasemia)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯包括傷寒、沙門氏菌感染、泌尿道感染、支氣管炎、細菌性肺炎等（香港許可證資料中未提供核准適應症文字） |
| 預測新適應症 | 高澱粉酶血症 (Hyperamylasemia) |
| TxGNN 預測分數 | 0.9991 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知的藥理學而言，Ofloxacin 是氟喹諾酮類抗菌藥，作用於細菌 DNA 旋轉酶與拓樸異構酶 IV。

高澱粉酶血症是血中澱粉酶升高的狀態，與胰臟或唾液腺酵素代謝有關。Ofloxacin 對澱粉酶的調控沒有已知作用，兩者之間找不到可辨識的機轉連結。這個高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

以下為資料中列出的部分許可證（共列出 20 張，總數至少 20 張，清單可能不完整），僅列前 5 張。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66156 | OFLO OPHTHALMIC SOLUTION 0.3% W/V | 眼用溶液（依品名） | 資料未提供 |
| HK-47706 | PUIRITOL TAB 100MG | 錠劑（依品名） | 資料未提供 |
| HK-49145 | OXACIN F.C. TAB 200MG | 膜衣錠（依品名） | 資料未提供 |
| HK-62027 | OCUFLO OPHTHALMIC SOLUTION 0.3%W/V | 眼用溶液（依品名） | 資料未提供 |
| HK-64416 | SINFLO TABLETS 200MG | 錠劑（依品名） | 資料未提供 |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（來自知識圖譜，並非仿單內容）：長 QT 症候群、尖端扭轉型心律不整、肝衰竭、癲癇、腎臟疾病、血小板低下、肌腱炎、糖尿病、周邊神經病變、橫紋肌溶解、重症肌無力、困難梭狀芽孢桿菌結腸炎、白血球低下等。
- **藥物交互作用**（共 100 筆，列出部分）：
  - 嚴重 (Major)：Hydrocortisone、Triamcinolone、Dexamethasone、Betamethasone、Bupropion、Chlorpropamide
  - 中度 (Moderate)：Acarbose、Famotidine、Metformin、Pioglitazone、Loperamide、Acetylsalicylic acid 等

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究 Ofloxacin 對高澱粉酶血症的作用，機轉上也無合理連結，證據等級為 L5。
- 高預測分數來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，而非生物學證據，不足以作為推進依據。

**若要推進需要：**
- 先找出任何直接研究 Ofloxacin 與血清澱粉酶之間關聯的資料。
- 補齊作用機轉與仿單的警語、禁忌資料。
- 若要在此預測以外尋找有潛力的方向，可另行評估排名第 8 的敗血性鼠疫（有動物與體外研究，但屬抗感染範疇的延伸，並非真正的藥物再利用，且缺乏人體試驗）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

