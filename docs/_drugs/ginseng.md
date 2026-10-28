---
layout: default
title: Ginseng
parent: 僅模型預測 (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
monitor_inn: "GINSENG"
predicted_indications: ["drug-induced osteoporosis", "acne (disease)", "severe nonproliferative diabetic retinopathy", "hemorrhagic disease of newborn", "nuclear senile cataract", "cortical cataract", "diabetic retinopathy", "amenorrhea (disease)", "craniostenosis cataract", "mature cataract"]
last_modified_at: 2026-10-23
description: "Ginseng：預測新適應症為藥物誘發性骨質疏鬆 (drug-induced osteoporosis)（證據等級 L5）。原適應症：本報告所整理的資料中未記載核准適應症"
---

# Ginseng
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

## 人參（Ginseng）：從〔無登記適應症資料〕到藥物誘發性骨質疏鬆
{: .text-alpha }

## 一句話總結

人參（Ginseng，DrugBank：DB01404）在香港有 2 張單一成分許可證，但本報告所整理的資料中沒有記載核准適應症。
TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆 (drug-induced osteoporosis)** 有效，不過目前**沒有任何臨床試驗或文獻**支持這個方向，僅屬模型預測（L5）。
在其他預測方向中，**糖尿病視網膜病變**的文獻最多（20 篇，多為動物與細胞研究），較值得優先追蹤。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本報告所整理的資料中未記載核准適應症 |
| 預測新適應症 | 藥物誘發性骨質疏鬆 (drug-induced osteoporosis) |
| TxGNN 預測分數 | 0.9995 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。人參含有多種人參皂苷（ginsenosides），一般認為可能影響骨重塑，但本報告所整理的資料並未提供人參與藥物（如糖皮質激素）誘發性骨質疏鬆之間的直接關聯。

由於原適應症資料缺漏，也無法分析原適應症與新適應症之間的關聯。此預測目前只能視為模型提出的假說，尚無臨床試驗與文獻佐證。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 其他預測方向（供參考）

本藥另有數個預測適應症，證據強度不同：

| 預測適應症 | TxGNN 分數 | 證據等級 | 摘要 |
|-----------|-----------|---------|------|
| 糖尿病視網膜病變 | 0.9955 | L4 | 20 篇文獻，多為動物與細胞實驗（Rg1、Rg3、Rd、Rk1 等皂苷），另有綜述與網絡藥理學研究；尚無登記的臨床試驗 |
| 嚴重非增殖性糖尿病視網膜病變 | 0.9971 | L5 | 一項 2026 年韓國紅蔘隨機雙盲試驗（[PMID 42395017](https://pubmed.ncbi.nlm.nih.gov/42395017/)），以深層微血管叢影像為替代指標，族群為一般糖尿病視網膜病變，設計與規模待確認 |
| 痤瘡 | 0.9987 | L4 | 一篇 2019 年紅蔘疏水性萃取物抗痤瘡的前臨床研究（[PMID 30506753](https://pubmed.ncbi.nlm.nih.gov/30506753/)） |
| 新生兒出血症 | 0.9970 | L5 | 唯一連結的試驗（[NCT00719563](https://clinicaltrials.gov/study/NCT00719563)）是美國人參用於癌因性疲憊，與此適應症無關，應為對應上的誤差 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-45214 | HIYA KIOGAN SILVER PILLS | 未記載 | 未記載 |
| HK-45213 | HIYA KIOGAN GOLD PILLS | 未記載 | 未記載 |

兩張許可證皆為有效的單一成分許可證，持證商為 MAN HING MEDICINE TRADERS。

---

## 安全性考量

- **藥物交互作用**：資料中共有 83 筆交互作用紀錄，以下列出的皆為中度等級，以降血糖藥物為主：
  - 口服降血糖藥：Acarbose、Metformin、Pioglitazone、Glimepiride、Chlorpropamide
  - SGLT2 抑制劑：Canagliflozin、Dapagliflozin、Empagliflozin
  - DPP-4 抑制劑：Alogliptin、Linagliptin
  - GLP-1 類藥物：Albiglutide、Dulaglutide、Semaglutide、Lixisenatide
  - 胰島素類：Insulin aspart、degludec、detemir、glargine、glulisine
  - 其他：Acetylsalicylic acid（阿斯匹靈）

  上述組合在併用時需留意血糖變化，尤其若未來朝糖尿病相關適應症發展，更需要審慎評估。

其餘警語與禁忌症資料不足，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 針對首位預測（藥物誘發性骨質疏鬆），沒有任何試驗或文獻，僅有模型分數，證據等級為 L5。
- 原適應症、作用機轉與仿單安全資料皆缺漏，目前不足以支持推進。

**若要推進需要：**
- 取得香港衛生署的仿單與核准適應症，補齊警語與禁忌症。
- 補充 DrugBank 的作用機轉資料。
- 若要優先評估，建議改以糖尿病視網膜病變為研究問題：先確認 PMID 42395017 的試驗設計、樣本數與結果，再考慮設計對照的 Phase 2 試驗。
- 針對藥物誘發性骨質疏鬆，先做系統性文獻檢索與骨代謝的前臨床驗證。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

