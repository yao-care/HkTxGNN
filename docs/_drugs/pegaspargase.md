---
layout: default
title: Pegaspargase
parent: 僅模型預測 (L5)
nav_order: 670
evidence_level: L5
indication_count: 7
monitor_inn: "PEGASPARGASE"
predicted_indications: ["chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "follicular lymphoma", "methylcobalamin deficiency type cblE", "lymphoid neoplasm", "Hodgkins lymphoma", "blast phase chronic myelogenous leukemia, BCR-ABL1 positive"]
last_modified_at: 2026-10-29
description: "Pegaspargase：預測新適應症為Chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Pegaspargase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

## Pegaspargase: Chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation
{: .text-alpha }

## 一句話總結

Pegaspargase（聚乙二醇化天門冬醯胺酶）在知識圖譜中記錄的關聯疾病為急性淋巴母細胞白血病（ALL）。
TxGNN 模型預測它可能對**慢性淋巴球性白血病／小淋巴球淋巴瘤（伴免疫球蛋白重鏈可變區基因體細胞高突變）**有效。
目前**沒有直接研究此疾病的臨床試驗或文獻**，這個預測僅是模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation |
| TxGNN 預測分數 | 0.9995 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般而言，Pegaspargase 會分解血中的天門冬醯胺，使依賴外源性天門冬醯胺的淋巴母細胞缺乏養分，這是它用於 ALL 的基礎。

預測的新適應症同屬淋巴系惡性腫瘤，這可能是模型給出高分的原因。不過，慢性淋巴球性白血病（CLL）細胞一般不被認為強烈依賴外源性天門冬醯胺，因此天門冬醯胺耗竭在此疾病的合理性並未建立。

本次整理的資料中，這個預測有兩個限制：

- 沒有任何針對此疾病的臨床試驗或文獻。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67823 | ONCASPAR POWDER FOR SOLUTION FOR INJECTION/INFUSION 3750 UNITS（廠商：SERVIER HONG KONG LIMITED） | — | 許可證資料未載明 |

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 酵素類抗腫瘤藥物（天門冬醯胺酶），不屬傳統烷化劑或抗代謝類細胞毒性藥物 |
| 骨髓抑制風險 | 請參考原廠仿單 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 過敏反應、胰臟炎、血栓、肝毒性，以及天門冬醯胺酶活性（依相關文獻中的臨床處置經驗） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，以下為其中列出的部分，均為中度等級：
  - 降血糖藥：Acarbose、Metformin、Alogliptin、Saxagliptin、Albiglutide、Dulaglutide、Canagliflozin、Dapagliflozin、Chlorpropamide
  - 類固醇：Hydrocortisone、Dexamethasone、Betamethasone、Triamcinolone、Budesonide
  - 抗生素：Doxycycline、Tetracycline、Clarithromycin
  - 其他：Bupropion、Acetylsalicylic acid、Chenodeoxycholic acid

主要警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型分數，沒有直接針對 CLL/SLL 的臨床試驗或文獻，證據等級為 L5。
- CLL 細胞對天門冬醯胺耗竭的依賴性尚未建立，機轉合理性不足。

**若要推進需要：**
- 取得 Pegaspargase 的作用機轉資料，並評估 CLL/SLL 細胞對天門冬醯胺的依賴性（如天門冬醯胺合成酶表現）。
- 進行前臨床或細胞株研究，驗證對 CLL/SLL 的活性。
- 取得香港原廠仿單，確認核准適應症、警語與禁忌症。
- 本次整理資料中，其他預測疾病（如淋巴樣腫瘤、NK/T 細胞淋巴瘤相關訊號）的證據多與 ALL 重疊或指向不同疾病，建議另案評估，不應與本預測合併判斷。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

