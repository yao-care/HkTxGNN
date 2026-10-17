---
layout: default
title: Glycocholic Acid
parent: 僅模型預測 (L5)
nav_order: 422
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Glycocholic Acid：預測新適應症為Prinzmetal 心絞痛 (Prinzmetal angina)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "Glycocholic acid"
predicted_indications: ["Prinzmetal angina", "myocardial infarction", "brain small vessel disease 1 with or without ocular anomalies", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "diabetic nephropathy", "posterolateral myocardial infarction", "posteroinferior myocardial infarction", "septal myocardial infarction", "hemoglobinopathy", "coronary thrombosis"]
---

# Glycocholic Acid
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

# Glycocholic acid：從（原適應症未載明）到 Prinzmetal 心絞痛

## 一句話總結

Glycocholic acid（甘膽酸）是一種結合型初級膽酸。香港許可證資料中未載明其核准適應症。
TxGNN 模型預測它可能對 **Prinzmetal 心絞痛 (Prinzmetal angina)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持，屬於純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | Prinzmetal 心絞痛 (Prinzmetal angina) |
| TxGNN 預測分數 | 99.98% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Glycocholic acid 是一種結合型初級膽酸，一般認為與膽汁酸代謝和脂質吸收有關，但本報告所整理的資料並未提供其原適應症或正式的作用機轉。

就 Prinzmetal 心絞痛（冠狀動脈痙攣）而言，現有資料中找不到能連結膽酸與冠狀動脈痙攣的合理機轉。這個高分預測很可能只是來自知識圖譜中的網路鄰近性，而非實際的藥理關聯。

其他排名較前的預測（心肌梗塞、糖尿病腎病變等）同樣缺乏介入性研究。相關文獻多為代謝體學或生物標記研究，只顯示膽酸代謝物與心血管或代謝疾病**可能相關**，不能證明有治療效果。Glycocholic acid 比較可能是疾病狀態的標記，而非治療藥物。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測（Prinzmetal 心絞痛）目前無相關文獻。

以下為其他預測適應症的間接文獻，均為觀察性或生物標記研究，並非治療證據：

| PMID | 年份 | 類型 | 期刊 | 對應疾病 | 主要發現 |
|------|-----|------|------|---------|---------|
| [37999255](https://pubmed.ncbi.nlm.nih.gov/37999255/) | 2023 | 生物標記/代謝體學研究 | Metabolites | 心肌梗塞 | 以高解析度代謝體學尋找動脈粥樣硬化早期診斷的代謝標記 |
| [30533038](https://pubmed.ncbi.nlm.nih.gov/30533038/) | 2018 | 生物標記/網路運算研究 | PloS one | 心肌梗塞 | 以網路方法探索心血管疾病的動態代謝生物標記 |
| [38741742](https://pubmed.ncbi.nlm.nih.gov/38741742/) | 2024 | 多體學觀察性研究 | Frontiers in microbiology | 糖尿病腎病變 | 在高血壓與糖尿病腎病變大鼠模型中分析腸道菌群與代謝物特徵 |
| [38660862](https://pubmed.ncbi.nlm.nih.gov/38660862/) | 2024 | 代謝體學描述性研究 | Zhongguo shi yan xue ye xue za zhi | 血紅素病變 | 分析輸血依賴型地中海型貧血兒童的血漿代謝特徵 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56452 | CERNEVIT FOR INJ（Baxter Healthcare Limited） | 未載明 | 未載明 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症均為 L5，僅有模型預測，沒有臨床試驗，也沒有支持治療效果的文獻。
- Prinzmetal 心絞痛與膽酸之間缺乏可信的機轉連結，其餘預測（心肌梗塞及其亞型、COL4A1 相關罕見疾病等）同樣缺乏支持。

**若要推進需要：**
- 取得香港衛生署仿單，確認原適應症、警語與禁忌症（目前為阻擋性資料缺口）。
- 補充 glycocholic acid 的作用機轉資料（例如查詢 DrugBank）。
- 進行系統性文獻回顧，確認膽酸與冠狀動脈痙攣或心血管疾病之間是否有因果或治療證據。
- 若仍有意推進，先進行前臨床機轉研究，再考慮臨床試驗設計。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

