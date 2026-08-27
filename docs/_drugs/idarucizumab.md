---
layout: default
title: Idarucizumab
parent: 僅模型預測 (L5)
nav_order: 387
evidence_level: L5
indication_count: 10
---

# Idarucizumab
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

Using the drug-repurposing report prompt (v5) directly on the supplied Evidence Pack — no additional tool calls are needed since all source data is already in the JSON.

# Idarucizumab：從 Dabigatran 抗凝血逆轉到血紅素病變 (Hemoglobinopathy)

## 一句話總結

Idarucizumab 是一種人源化單株抗體片段，原本用於逆轉 dabigatran（一種口服抗凝血劑）的抗凝血作用，供緊急手術或危及生命出血時使用。TxGNN 模型預測其可能對**血紅素病變 (Hemoglobinopathy)** 有效，但目前**無臨床試驗**、**無支持性文獻**，機轉分析也顯示此預測缺乏生物學合理性。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料庫未收錄正式許可證文字；已知全球核准用途為逆轉 dabigatran 之抗凝血作用 |
| 預測新適應症 | 血紅素病變 (Hemoglobinopathy) |
| TxGNN 預測分數 | 95.66% |
| 證據等級 | L5 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏正式登錄的 MOA 資料（DrugBank 查詢未取得完整機轉描述，列為 High 等級資料缺口）。根據現有證據脈絡描述，idarucizumab 是專一結合 dabigatran 分子的人源化單株抗體片段（Fab fragment），其作用機轉為直接中和 dabigatran、逆轉其抗凝血效果，臨床用途限於使用 dabigatran 患者發生危及生命出血或需緊急手術時的解毒劑。

原適應症（dabigatran 逆轉）與本次 TxGNN 預測的血紅素病變（涵蓋地中海貧血、蠶豆症樣酵素缺陷、遺傳性球狀紅血球增多症等紅血球相關疾病）在機轉上並無關聯。Idarucizumab 的藥理活性僅限於結合並中和特定小分子抗凝血藥物，不具備任何影響紅血球生成、血紅素合成、代謝酵素或膜骨架蛋白的生物活性。

根據評估報告中附帶的機轉分析（repurposing_rationale），此高分預測很可能源自知識圖譜中「血液科」相關節點的間接鄰近性連結，而非真實藥理機轉關聯，應視為模型的預測假訊號。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

目前無香港上市許可證資料（本藥物於香港未上市，`total_licenses` = 0）。

---

## 本次評估的其他候選適應症（補充說明）

本輪 TxGNN 針對 idarucizumab 共產生 10 個預測候選，**全數判定為 Hold**，機轉分析一致指出與原始適應症（dabigatran 結合/中和）無生物學關聯：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 備註 |
|------|-----------|-----------|---------|------|
| 1 | 血紅素病變 | 95.66% | L5 | 無證據，疑為知識圖譜鄰近性假陽性 |
| 2 | 類風濕性關節炎 | 95.52% | L5 | 無免疫調節機轉證據 |
| 3 | 16 號染色體短臂部分缺失 | 94.99% | L5 | 基因層級病因，非抗體可介入機轉 |
| 4 | β-地中海貧血（合併其他表現） | 94.98% | L5 | 珠蛋白基因突變所致，無交集 |
| 5 | 紅血球丙酮酸激酶缺乏症 | 94.82% | L5 | 代謝酵素缺陷，無關聯 |
| 6 | 葡萄糖磷酸異構酶缺乏溶血性貧血 | 94.56% | L5 | 糖解酵素缺陷，無關聯 |
| 7 | 遺傳性熱敏感異型紅血球增多症 | 94.26% | L5 | 膜骨架蛋白缺陷，無關聯 |
| 8 | 支氣管炎 | 94.09% | L5 | 呼吸道發炎/感染，無關聯 |
| 9 | 痛風 | 93.75% | **L4** | 唯一文獻 (PMID 31381100) 實為個案報告描述 idarucizumab **原始適應症**（逆轉 dabigatran 合併血液透析），並非用於治療痛風——屬文字/情境共現造成的假陽性配對 |
| 10 | 眼缺損—肢體近端短小症候群 | 93.62% | L5 | 先天性發育畸形，結構性病因，無關聯 |

**規則性觀察**：多數候選為罕見血液/遺傳疾病，且集中出現在知識圖譜的「血液科」鄰近節點，顯示這批預測可能反映知識圖譜結構偏誤，而非真實藥理訊號。

---

## 安全性考量

安全性資訊請參考原廠仿單。（本評估之 TFDA/香港仿單警語與禁忌症資料為 **Blocking 等級資料缺口**，尚未取得。）

---

## 結論與下一步

**決策：Hold**

**理由：**
- 本輪全部 10 個 TxGNN 預測候選，機轉分析均顯示與原始適應症（dabigatran 中和）無生物學關聯性，證據等級以 L5 為主。
- 唯一具文獻紀錄的候選（痛風，rank 9，L4）經查證後，該文獻描述的仍是 idarucizumab 的原始核准用途（逆轉 dabigatran），並非用於治療痛風本身，判定為假陽性配對，不構成再利用證據。
- 安全性初評所需的仿單警語/禁忌症資料為 Blocking 等級缺口，目前無法進入 S1 安全性初評。

**若要推進需要：**
- 補齊正式 MOA 資料（DrugBank API 查詢，High 等級缺口）
- 補齊 TFDA／香港衛生署仿單警語與禁忌症資料（Blocking 等級缺口，PDF 解析）
- 若未來模型更新產生新的高分候選，須重新檢視是否具備獨立於知識圖譜鄰近效應的真實機轉證據，再決定是否投入臨床前驗證資源
- 現階段不建議針對本輪任何候選投入後續驗證資源
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

