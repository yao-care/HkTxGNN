---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 554
evidence_level: L5
indication_count: 5
---

# Paliperidone
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

# PALIPERIDONE：從抗精神病治療到視網膜營養不良（機轉關聯性存疑）

## 一句話總結

Paliperidone（DrugBank DB01267）目前原適應症資料未收錄，但依本證據包內之機轉描述，其藥理性質為 **D2/5-HT2A 受體拮抗劑**（典型抗精神病藥物機轉）。TxGNN 模型預測其可能對**視網膜營養不良合併或不合併眼外異常（Retinal Dystrophy with or without Extraocular Anomalies）**有效，目前有 **0 個臨床試驗**、**15 篇文獻**，但這些文獻皆為疾病背景資料，並非藥物療效證據，且證據包自身的機轉分析判定為「無合理機轉」。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料缺口（原始適應症與 MOA 均未收錄，見下方說明） |
| 預測新適應症 | 視網膜營養不良合併/不合併眼外異常 (Retinal Dystrophy with or without Extraocular Anomalies) |
| TxGNN 預測分數 | 99.92%（原始排名 2182） |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

Paliperidone 的完整作用機轉資料在本證據包中標記為缺口（DG002，High 等級），無法取得官方 MOA 描述。不過，證據包內各候選適應症的機轉關聯分析文字一致指出：**Paliperidone 為 D2（多巴胺）/5-HT2A（血清素）受體拮抗劑**，屬典型的抗精神病藥物藥理機轉。

視網膜營養不良合併/不合併眼外異常為先天性視網膜光感受器發育異常疾病，與已知致病基因（如 CRB1、RPE65 等）相關，屬結構性/遺傳性眼科疾病，並非神經傳導物質受體調控的病理過程。

證據包本身的機轉分析已明確結論：**「無合理機轉。Paliperidone 為 D2/5-HT2A 受體拮抗劑，未見與視網膜光感受器發育、先天性視網膜營養不良相關基因通路有藥理交互作用之文獻支持」**。換言之，這是一個 TxGNN 高分預測分數（99.92%）但機轉上難以合理解釋的候選，屬於需要謹慎對待的預測結果。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下 10 篇為 PubMed 檢索到的相關文獻。**須注意：這些文獻均為視網膜營養不良／眼眶疾病之一般臨床背景資料，內容並未提及 Paliperidone，並非藥物療效之直接證據。**

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [9416661](https://pubmed.ncbi.nlm.nih.gov/9416661/) | 1997 | Review | Semin Ultrasound CT MR | 眼眶感染回顧，鼻竇炎為最常見病因 |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review | Semin Neurol | 複視之系統性評估方法 |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmol | 水晶體先天性形狀異常之回顧 |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Review | Doc Ophthalmol | Wagner-Stickler 症候群之玻璃體視網膜退化與全身表現 |
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatr Radiol | 小兒眼眶病灶（含先天性視網膜病變）之影像鑑別診斷 |
| [22241537](https://pubmed.ncbi.nlm.nih.gov/22241537/) | 2012 | Case Report | Klin Monbl Augenheilkd | 先天性上眼瞼下垂之臨床特徵與治療 |
| [109006](https://pubmed.ncbi.nlm.nih.gov/109006/) | 1979 | Case Report | Am J Ophthalmol | 單側隱眼畸形合併眼外肌與視神經缺失之病例 |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | J Neuroophthalmol | 先天性滑車-動眼神經聯帶運動之罕見病例 |
| [19826317](https://pubmed.ncbi.nlm.nih.gov/19826317/) | 2009 | Case Report | Optom Vis Sci | 先天性眼外肌纖維化伴隨異常分向運動之病例 |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Case Report | Arch Ophthalmol | 眼眶動靜脈畸形之臨床特徵與治療結果 |

---

## 其他 TxGNN 預測候選（同批次，皆為 Hold）

本次評估同時產出以下候選，皆為模型高分預測但**無臨床試驗、無文獻、機轉分析同樣判定無合理關聯**：

| 排名 | 預測適應症 | TxGNN 分數 | 機轉關聯 |
|------|-----------|-----------|---------|
| 2 | Myopia X-linked | 99.91% | 無機轉關聯，遺傳性屈光異常與抗精神病藥理無連結 |
| 3 | Syndromic myopia | 99.91% | 無機轉關聯，屬結締組織/骨骼發育症候群伴隨表現 |
| 4 | Hydranencephaly (disease) | 99.91% | 無機轉關聯，屬結構性腦部缺失，非藥理可逆病灶 |
| 5 | Congenital disorder of glycosylation with defective fucosylation | 99.90% | 無機轉關聯，屬酵素/轉運蛋白基因缺陷疾病 |

---

## 安全性考量

安全性資訊請參考原廠仿單。目前 TFDA/香港仿單警語與禁忌症資料為 Blocking 等級缺口（DG001），無法進行安全性初評；藥物交互作用查詢亦無結果。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 5 個候選適應症皆為 L5（僅有模型預測分數，無臨床試驗、無支持性文獻），且證據包自身的機轉分析對全部候選均判定為「無合理機轉」。
- 文獻雖有 15 篇與首選候選相關，但均為疾病背景資料而非藥物療效證據。
- 存在 Blocking 等級資料缺口（DG001：仿單警語/禁忌症），無法進入安全性初評，藥物於香港亦未上市。

**若要推進需要：**
- 補齊 Paliperidone 完整 MOA 資料（DG002）
- 取得 TFDA/原廠仿單警語與禁忌症（DG001，Blocking，優先處理）
- 尋找實際「藥物＋適應症」共同出現之臨床或病例文獻，而非僅疾病背景文獻
- 若後續仍無機轉支持證據，建議將此候選組合自後續評估排除
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

