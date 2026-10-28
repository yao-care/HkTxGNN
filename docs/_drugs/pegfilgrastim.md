---
layout: default
title: Pegfilgrastim
parent: 僅模型預測 (L5)
nav_order: 671
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
description: "Pegfilgrastim：預測新適應症為嚴重非增殖性糖尿病視網膜病變 (severe nonproliferative diabetic retinopathy)（證據等級 L5）。原適應症：香港許可證資料未載明"
monitor_inn: "PEGFILGRASTIM"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "diabetic retinopathy"]
---

# Pegfilgrastim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

## Pegfilgrastim：從嗜中性白血球減少症到嚴重非增殖性糖尿病視網膜病變
{: .text-alpha }

## 一句話總結

Pegfilgrastim 是長效型 G-CSF（顆粒球群落刺激因子），香港已有 4 張有效許可證，目前的許可證資料未列出核准適應症文字。
TxGNN 模型預測它可能對**嚴重非增殖性糖尿病視網膜病變 (severe nonproliferative diabetic retinopathy)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明 |
| 預測新適應症 | 嚴重非增殖性糖尿病視網膜病變 (severe nonproliferative diabetic retinopathy) |
| TxGNN 預測分數 | 0.9989 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

另有一個相關預測為「糖尿病視網膜病變 (diabetic retinopathy)」，分數 0.9973，同為 L5。兩者高度重疊，並非獨立的證據訊號。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Pegfilgrastim 是聚乙二醇化的 G-CSF，一般認為能刺激嗜中性白血球增生，並動員造血前驅細胞。

理論上，骨髓來源前驅細胞的動員可能有助於血管修復，或調節發炎反應，這是連結到糖尿病視網膜病變的可能假說。

但方向並不確定。G-CSF 引起的嗜中性白血球活化與白血球－內皮細胞交互作用，也可能加重視網膜血管損傷，新生血管形成同樣是理論上的疑慮。此外，現行標準治療（抗 VEGF、雷射、皮質類固醇）門檻很高。這個假說尚未驗證，目前的資料也無法確認其機轉連結。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66770 | FULPHILA SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 6MG/0.6ML | 預充填注射劑 | 資料未載明 |
| HK-68176 | PELGRAZ SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 6MG/0.6ML | 預充填注射劑 | 資料未載明 |
| HK-54933 | NEULASTIM PRE-FILLED SYRINGE INJ 6MG/0.6 ML | 預充填注射劑 | 資料未載明 |
| HK-67124 | ZIEXTENZO SOLUTION FOR INJECTION IN PRE-FILLED SYRINGE 6MG/0.6ML | 預充填注射劑 | 資料未載明 |

---

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為其中列出的部分（均為中度），包括：
  - 化療與細胞毒性藥物：Paclitaxel、Mercaptopurine、Azacitidine、Arsenic trioxide、Trimetrexate、Altretamine
  - 標靶與免疫相關藥物：Abemaciclib、Acalabrutinib、Avapritinib、Alemtuzumab、Aldesleukin、Belantamab mafodotin
  - 放射性藥物與診斷劑：Ibritumomab tiuxetan、Tositumomab、Iobenguane (I-131)、Fludeoxyglucose (18F)
  - 其他：Pegvaliase、Levamisole

主要警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高，但僅來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，並非生物學證據，沒有任何臨床試驗或文獻佐證（L5）。
- 作用機轉資料缺失，且 G-CSF 對視網膜血管的影響方向不明，甚至可能有害。

**若要推進需要：**
- 取得香港仿單的警語、禁忌症與核准適應症，完成安全性篩選
- 補充作用機轉資料，並釐清 G-CSF 對視網膜血管、新生血管形成的影響
- 進行前臨床（動物模型）或文獻回顧，驗證骨髓前驅細胞動員對糖尿病視網膜病變的作用方向
- 與抗 VEGF 等標準治療比較，評估臨床價值
- 評估給藥途徑（全身性注射對比眼科局部給藥）的可行性
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

