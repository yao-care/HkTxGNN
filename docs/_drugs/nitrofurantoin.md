---
layout: default
title: Nitrofurantoin
parent: 僅模型預測 (L5)
nav_order: 528
evidence_level: L5
indication_count: 5
---

# Nitrofurantoin
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

# Nitrofurantoin：從泌尿道感染到類風濕性關節炎

## 一句話總結

Nitrofurantoin 是治療泌尿道感染（含慢性菌尿症）的經典抗菌藥。
TxGNN 模型預測它可能對**類風濕性關節炎 (Rheumatoid Arthritis)** 有效，
但目前**無臨床試驗**支持，僅有 **12 篇文獻**，且文獻內容多指向安全性疑慮而非療效證據。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 泌尿道感染／菌尿症（依文獻脈絡推得，無正式核准文字資料） |
| 預測新適應症 | 類風濕性關節炎 (Rheumatoid Arthritis) |
| TxGNN 預測分數 | 99.89% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Nitrofurantoin 屬於 nitrofuran 類尿路抗菌藥，已知機轉是造成細菌核糖體蛋白與 DNA 損傷，並無已知的免疫調節或抗發炎作用可解釋其對類風濕性關節炎的潛在療效。

檢視 12 篇相關文獻後發現，內容並非支持療效的證據，而是集中在**藥物誘發肺纖維化／間質性肺病**的安全性訊號 —— 特別是 nitrofurantoin 與 methotrexate（RA 常用藥）併用時，有病例報告指出會導致不可逆肺纖維化。另有文獻單純將 RA 列為肺纖維化的其他成因之一，與 nitrofurantoin 並無直接治療關聯。

整體而言，這個預測較可能是知識圖譜中「RA 與肺纖維化」「nitrofurantoin 與肺纖維化」兩條路徑交會產生的關聯，而非真正具備生物學合理性的再利用機會。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Cohort (self-controlled case series) | Scientific Reports | 探討抗生素使用與 RA 病情發作(flare)的關聯，非 nitrofurantoin 專屬療效證據 |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Med J | 綜述藥物誘發肺纖維化，將 nitrofurantoin 與 RA 並列為肺纖維化風險因子 |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Case report | Cureus | RA 患者併用 methotrexate 與 nitrofurantoin，導致不可逆肺纖維化 |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du praticien | 藥物誘發間質性肺病綜述，列出 nitrofurantoin 等抗生素為致病藥物 |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Cohort | Chest | RA 住院患者併發間質性肺纖維化之預後不佳 |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Case report | Ann Dermatol Venereol | Phenylbutazone 誘發唾液腺炎病例，附帶提及 nitrofurantoin 可致唾液腺炎 |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | 未分類 | Acta Med Scand | 中年女性菌尿症篩檢與短期 nitrofurantoin 治療追蹤（原適應症相關） |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | 未分類 | Cureus | 自體免疫肝炎鑑別診斷病例，將 nitrofurantoin 列為需排除的藥物性肝損傷成因 |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | 未分類 | Rev Pneumol Clin | 金鹽誘發肺炎病例，比較與 methotrexate 之肺泡炎機轉 |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | 未分類 | Der Internist | 肺泡炎與肺纖維化總論 |

---

## 香港上市資訊

Nitrofurantoin 目前未在香港上市，無許可證資料。

---

## 安全性考量

- **藥物交互作用**：官方 DDI 資料庫查無資料（query_status: not_found），但文獻中有明確個案顯示 nitrofurantoin 與 methotrexate 併用可能導致不可逆肺纖維化，用於 RA 患者時需特別留意。
- **主要警語／禁忌症**：官方仿單警語與禁忌資料缺失（TFDA 仿單解析尚未完成，屬 Blocking 等級資料缺口），安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
TxGNN 分數雖高，但無任何臨床試驗支持，機轉上也缺乏生物學合理性；反而文獻證據指向安全性疑慮（併用 methotrexate 時肺纖維化風險），而非療效訊號。證據等級僅 L5，不足以支持推進。

**若要推進需要：**
- 補齊 TFDA／當地仿單警語與禁忌資料（現為 Blocking 缺口）
- 取得完整作用機轉 (MOA) 資料以評估機轉關聯性
- 若欲繼續探索此方向，需先有體外或動物實驗證據支持潛在抗發炎機轉
- 否則建議將此候選標記為知識圖譜偽陽性並排除
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

