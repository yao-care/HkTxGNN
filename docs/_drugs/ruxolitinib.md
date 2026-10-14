---
layout: default
title: Ruxolitinib
parent: 僅模型預測 (L5)
nav_order: 793
evidence_level: L5
indication_count: 5
---

# Ruxolitinib
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

# Ruxolitinib：從骨髓增生性腫瘤到子宮血管周上皮樣細胞腫瘤（PEComa）

## 一句話總結

Ruxolitinib 原本用於骨髓增生性腫瘤，包括原發性骨髓纖維化與真性紅血球增多症。
TxGNN 模型預測它可能對**子宮體血管周上皮樣細胞腫瘤 (uterine corpus perivascular epithelioid cell tumor)** 有效。
目前**沒有臨床試驗與文獻**支持這項預測，僅為模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 真性紅血球增多症、骨髓增生性腫瘤、原發性骨髓纖維化等（依知識圖譜適應症資料；香港許可證未載明適應症文字） |
| 預測新適應症 | 子宮體血管周上皮樣細胞腫瘤 (uterine corpus perivascular epithelioid cell tumor) |
| TxGNN 預測分數 | 99.73% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

其他排名較高的預測包括良性 PEComa（99.73%）、淋巴管肌瘤（99.72%）、淋巴管平滑肌瘤病（99.64%）與脂肪肉瘤（99.52%）。前四者同屬 PEComa／mTOR 相關疾病，彼此高度相關，不應視為獨立的證據。脂肪肉瘤有少量前臨床文獻（見下文）。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。依一般背景知識，ruxolitinib 是 JAK1/JAK2 抑制劑，可抑制 JAK-STAT 訊號傳導，這也是它用於骨髓增生性腫瘤的基礎。

PEComa 與相關疾病（淋巴管平滑肌瘤病、淋巴管肌瘤）主要由 TSC1/TSC2 失去功能、mTORC1 過度活化所驅動，既有標準治療是 sirolimus 等 mTOR 抑制劑。JAK-STAT 與 mTOR 通路之間或許存在交互作用，但提供的資料中沒有任何證據顯示這一點。TxGNN 的高分更可能反映知識圖譜中相近疾病的共同鄰域，而非獨立的機轉證據。

在預測清單中，脂肪肉瘤是唯一有機轉文獻的項目。兩篇前臨床研究指出，JAK-STAT 訊號與黏液樣脂肪肉瘤的癌幹細胞特性及化療抗藥性有關，為 JAK 抑制提供了合理的研究方向。但證據僅限於黏液樣亞型的體外研究。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

以下文獻針對排名第 5 的預測「脂肪肉瘤」。首要預測（子宮體 PEComa）目前無相關文獻。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [35186752](https://pubmed.ncbi.nlm.nih.gov/35186752/) | 2022 | 前臨床／基礎研究 | Frontiers in Oncology | FUS-DDIT3 融合致癌蛋白表達會提高 STAT3 及磷酸化 STAT3 水平，影響黏液樣脂肪肉瘤的 JAK-STAT 訊號 |
| [30650179](https://pubmed.ncbi.nlm.nih.gov/30650179/) | 2019 | 前臨床／基礎研究 | International Journal of Cancer | JAK-STAT 訊號控制黏液樣脂肪肉瘤的癌幹細胞特性，包括對 doxorubicin 的化療抗藥性 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68437 | LUMIRIX CREAM 15MG/G | 未載明 | 未載明 |
| HK-61973 | JAKAVI TAB 5MG | 未載明 | 未載明 |
| HK-61972 | JAKAVI TAB 20MG | 未載明 | 未載明 |
| HK-61974 | JAKAVI TAB 15MG | 未載明 | 未載明 |
| HK-66148 | JAKAVI TABLETS 10MG | 未載明 | 未載明 |

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為部分重點：
  - **Major（嚴重）**：Clarithromycin、Cobicistat、Deferasirox、Deferiprone、Ibritumomab tiuxetan、Tositumomab、Tositumomab (I-131)、Samarium (153Sm) lexidronam
  - **Moderate（中度）**：Dexamethasone、Rosuvastatin、Dexfenfluramine、Fenfluramine、Sibutramine、Troglitazone、Palifermin、Strontium chloride Sr-89
  - **Minor（輕微）**：Aprepitant、Cimetidine、Miconazole、Clotrimazole

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（子宮體 PEComa）及同家族的三項預測僅有模型分數，沒有臨床試驗、文獻或明確機轉支持，證據等級為 L5。
- 脂肪肉瘤雖有前臨床機轉線索（L4），但僅限黏液樣亞型的體外研究，無人體資料，適合列為研究問題，而非推進開發。

**若要推進需要：**
- 補齊 ruxolitinib 的作用機轉資料，並釐清 JAK-STAT 與 mTOR 通路在 PEComa／淋巴管平滑肌瘤病的關聯。
- 進行 PEComa 相關的前臨床驗證（細胞株或動物模型），並系統性搜尋文獻與試驗登記。
- 針對脂肪肉瘤，驗證前臨床發現是否可延伸到其他亞型，並取得人體安全性與療效資料。
- 取得香港衛生署的仿單，確認核准適應症、警語與禁忌症，以完成安全性篩選。
- 與既有標準治療（如 mTOR 抑制劑）比較其潛在價值。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

