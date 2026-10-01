---
layout: default
title: Bevacizumab
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 10
---

# Bevacizumab
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Bevacizumab：從原適應症（資料缺漏）到上顎/口咽部良性腫瘤等預測新適應症

## 一句話總結

Bevacizumab 是抗 VEGF-A 的單株抗體，在香港已有多張許可證，但本資料包未提供原適應症文字。
TxGNN 預測它可能對**會厭腫瘤 (Epiglottis Neoplasm)** 有效（排名第 1），
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料包未提供（許可證的核准適應症欄位皆為空） |
| 預測新適應症 | 會厭腫瘤 (Epiglottis Neoplasm) |
| TxGNN 預測分數 | 99.90% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

> 補充：預測清單共 10 項。證據最強的是第 7 名「囊性腫瘤 (Cystic Neoplasm)」（L1，Proceed with Guardrails），但該證據實為卵巢癌等既有適應症，並非新用途訊號。詳見下方說明。

## 為什麼這個預測合理？

Bevacizumab 可中和 VEGF-A，抑制腫瘤血管新生。這是頭頸部腫瘤合理的類別層級機轉推論，因為頭頸部腫瘤常有血管新生依賴。

不過，目前缺乏詳細的作用機轉資料（DrugBank MOA 欄位缺漏）。會厭腫瘤沒有檢索到任何臨床試驗或文獻，TxGNN 分數（99.90%）是唯一支持。

## 預測新適應症一覽

| 排名 | 預測疾病 | 分數 | 證據等級 | 建議 |
|------|---------|------|---------|------|
| 1 | 會厭腫瘤 | 99.90% | L5 | Hold |
| 2 | 舌良性腫瘤 | 99.90% | L4 | Hold |
| 3 | 睪丸及副睪腫瘤 | 99.90% | L5 | Hold |
| 4 | 下咽良性腫瘤 | 99.90% | L5 | Hold |
| 5 | 口底良性腫瘤 | 99.90% | L3 | Research Question |
| 6 | 頸部神經母細胞瘤 | 99.89% | L4 | Hold |
| 7 | 囊性腫瘤 | 99.89% | L1 | Proceed with Guardrails |
| 8 | 鼻腔內翻性乳突瘤 | 99.89% | L4 | Hold |
| 9 | 間葉瘤 | 99.89% | L5 | Hold |
| 10 | 頸靜脈孔神經鞘瘤 | 99.89% | L5 | Hold |

## 臨床試驗證據

**主要預測（會厭腫瘤）：** 目前無相關臨床試驗登記。

**證據最多的預測（第 7 名，囊性腫瘤）** 中，相關性較高的試驗如下（其餘多為不同疾病，未列出）：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT00565851](https://clinicaltrials.gov/study/NCT00565851) | Phase 3 | 進行中（未招募） | 1052 | 卵巢/腹膜/輸卵管癌復發：化療加或不加 bevacizumab（已是既有適應症，對「囊性腫瘤」屬間接證據） |
| [NCT03074513](https://clinicaltrials.gov/study/NCT03074513) | Phase 2 | 進行中（未招募） | 133 | Atezolizumab + bevacizumab 用於罕見實體腫瘤（腫瘤類型未確認） |
| [NCT00381797](https://clinicaltrials.gov/study/NCT00381797) | Phase 2 | 完成 | 97 | Bevacizumab + irinotecan 用於兒童復發性腦瘤（不同族群） |
| [NCT00324987](https://clinicaltrials.gov/study/NCT00324987) | Phase 3 | 提前終止 | 12 | 腸胃道基質瘤 imatinib ± bevacizumab（僅 12 人，無法評估療效） |

**口底良性腫瘤（第 5 名）：**

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01552434](https://clinicaltrials.gov/study/NCT01552434) | Phase 1 | 進行中（未招募） | 155 | Bevacizumab、temsirolimus 單用或合併 valproic acid／cetuximab，用於晚期惡性腫瘤，僅提供安全性與劑量資訊 |

## 文獻證據

**主要預測（會厭腫瘤）：** 目前無相關文獻。

**舌良性腫瘤（第 2 名）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39927612](https://pubmed.ncbi.nlm.nih.gov/39927612/) | 2025 | Review | Expert Opin Pharmacother | 腫瘤治療的口腔黏膜毒性，含 bevacizumab 相關的地圖舌 |
| [18691881](https://pubmed.ncbi.nlm.nih.gov/18691881/) | 2008 | 前臨床 | Eur J Cancer | 頭頸癌異種移植小鼠：bevacizumab 合併 AZD2171 有加成的抗腫瘤效果 |
| [21744483](https://pubmed.ncbi.nlm.nih.gov/21744483/) | 2011 | 個案報告 | Pediatr Blood Cancer | 舌部腺泡狀軟組織肉瘤術前使用 bevacizumab + celecoxib |

**囊性腫瘤（第 7 名，取較相關者）：**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [37754507](https://pubmed.ncbi.nlm.nih.gov/37754507/) | 2023 | 系統性回顧 | Curr Oncol | Bevacizumab 用於低惡性度漿液性卵巢癌顯示部分活性 |
| [38328890](https://pubmed.ncbi.nlm.nih.gov/38328890/) | 2024 | 世代研究 | Future Oncol | 51 位復發性低惡性度漿液性卵巢癌，客觀反應率 54.1% |
| [37657955](https://pubmed.ncbi.nlm.nih.gov/37657955/) | 2023 | 臨床研究 | Clin Colorectal Cancer | Mitomycin-C + 節律性 capecitabine + bevacizumab 用於闌尾來源腹膜假黏液瘤 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67028 | MVASI 100mg/4ml 輸注濃縮液（Amgen） | 資料未提供 | 資料未提供 |
| HK-59450 | AVASTIN ROCHE 100mg/4ml 輸注濃縮液（Roche） | 資料未提供 | 資料未提供 |
| HK-67029 | MVASI 400mg/16ml 輸注濃縮液（Amgen） | 資料未提供 | 資料未提供 |
| HK-56638 | AVASTIN ROCHE 注射劑 100mg/4ml（Roche） | 資料未提供 | 資料未提供 |
| HK-56637 | AVASTIN ROCHE 注射劑 400mg/16ml（Roche） | 資料未提供 | 資料未提供 |

## 細胞毒性

Bevacizumab 為抗腫瘤標靶藥物（單株抗體），非傳統細胞毒性藥物。資料包無細胞毒性專項資料，請參考原廠仿單的警語與注意事項。

## 安全性考量

安全性資訊請參考原廠仿單。（香港衛生署仿單的警語與禁忌尚未取得；藥物交互作用查詢無結果。）

## 結論與下一步

**決策：Hold**

**理由：**
主要預測（會厭腫瘤）僅有模型分數，屬 L5，無試驗與文獻。第 7 名「囊性腫瘤」雖達 L1，但證據來自卵巢癌等既有用途，不是新的老藥新用訊號。多數預測疾病為良性腫瘤，全身性抗血管新生藥物的風險效益比有待商榷。

**若要推進需要：**
- 取得香港衛生署仿單，補齊警語、禁忌與核准適應症（目前為阻擋性缺口，無法進入安全性篩選）
- 補充 DrugBank 的作用機轉資料
- 針對會厭及頭頸部腫瘤做專門的文獻與試驗檢索
- 釐清「囊性腫瘤」等廣泛映射詞實際對應的腫瘤類型
- 評估良性腫瘤使用全身性抗血管新生藥物的風險效益

> 本報告結果僅供研究參考，不構成醫療建議；老藥新用候選需經臨床驗證才能應用。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

