---
layout: default
title: Idarucizumab
parent: 僅模型預測 (L5)
nav_order: 456
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Idarucizumab：預測新適應症為血紅素病變 (Hemoglobinopathy)（證據等級 L5）。原適應症：許可證未載明適應症（依機轉為 dabigatran 抗凝血作用的逆轉）"
monitor_inn: "Idarucizumab"
predicted_indications: ["hemoglobinopathy", "rheumatoid arthritis", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations", "pyruvate kinase deficiency of red cells", "hemolytic anemia due to glucophosphate isomerase deficiency", "pyropoikilocytosis, hereditary", "bronchitis", "gout", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
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

<div id="pharmacist" markdown="1">

## 藥師評估報告

</div>

## Idarucizumab：從 Dabigatran 逆轉治療到血紅素病變（預測）
{: .text-alpha }

## 一句話總結

Idarucizumab 是專一結合 dabigatran 的人源化抗體片段（Fab），用來中和 dabigatran 的抗凝血作用。
TxGNN 模型預測它可能對**血紅素病變 (hemoglobinopathy)** 有效，但目前**沒有任何臨床試驗或相關文獻**支持，僅為模型運算結果，機轉上也看不出合理關聯。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證未載明適應症（依機轉為 dabigatran 抗凝血作用的逆轉） |
| 預測新適應症 | 血紅素病變 (Hemoglobinopathy) |
| TxGNN 預測分數 | 95.66% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Idarucizumab 是一種對 dabigatran 具高親和力的抗體片段，作用是中和其抗凝血活性。

血紅素病變屬於紅血球或血紅素結構與合成的遺傳性疾患。Idarucizumab 的機轉（結合並中和 dabigatran）與血紅素或紅血球代謝無明顯關聯，**找不到合理的機轉連結**。

高分預測較可能來自知識圖譜的運算假象，而非真實的藥理關聯。其他排名前十的預測（類風濕性關節炎、β-地中海型貧血、丙酮酸激酶缺乏症、支氣管炎、痛風等）同樣缺乏機轉依據與臨床證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

（備註：在排名第 9 的預測「痛風」下檢索到 1 篇病例報告，PMID 31381100，內容為急性腎損傷患者接受血液透析、新鮮冷凍血漿及兩劑 idarucizumab 以逆轉 dabigatran。該報告屬於藥物原本的核准用途，與血紅素病變及痛風治療皆無關，不構成再利用證據。）

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-64759 | PRAXBIND SOLUTION FOR INJECTION/ INFUSION 2.5G/50ML | 未載明 | 未載明 |

廠商：BOEHRINGER INGELHEIM (HK) LTD。

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有臨床試驗、文獻或機轉依據支持，證據等級為 L5。
- Idarucizumab 是針對單一抗凝血劑的專一逆轉劑，與血紅素病變沒有合理的藥理關聯。

**若要推進需要：**
- 提出具體的機轉假說，說明 dabigatran 中和作用為何可能與血紅素病變相關。
- 取得香港衛生署仿單中的核准適應症、警語與禁忌資料。
- 補齊 DrugBank 的作用機轉資料。
- 有前臨床或臨床證據後，再重新評估；在此之前不建議投入資源。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

