---
layout: default
title: Panitumumab
parent: 僅模型預測 (L5)
nav_order: 662
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Panitumumab：預測新適應症為藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis)（證據等級 L5）。原適應症：轉移性大腸腫瘤（Metastatic malignant neoplasm in the colon）"
monitor_inn: "PANITUMUMAB"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy"]
---

# Panitumumab
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

## Panitumumab：從轉移性大腸腫瘤到藥物誘發性骨質疏鬆
{: .text-alpha }

## 一句話總結

Panitumumab 是一種抗 EGFR 單株抗體，原本用於治療轉移性大腸腫瘤。
TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis)** 有效（預測分數 0.9913）。
目前**沒有任何臨床試驗或文獻**支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 轉移性大腸腫瘤（Metastatic malignant neoplasm in the colon） |
| 預測新適應症 | 藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 0.9913 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Panitumumab 是抗 EGFR 單株抗體，其在轉移性大腸腫瘤中的療效已被臨床應用所證實。

EGFR 訊號參與成骨細胞分化與骨重塑，因此從生物學上推論，阻斷 EGFR 可能影響骨代謝。但方向並不確定：Panitumumab 常造成低血鎂與低血鈣，可能對骨骼健康產生不利影響。因此它的作用可能是傷害而非治療。

整體而言，這個連結仍屬推測，目前提供的資料並未提供支持證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-61371 | VECTIBIX CONCENTRATE FOR SOLUTION FOR INFUSION 20MG/ML | 未提供 | 未提供 |

此為單一成分製劑，由 AMGEN HONG KONG LIMITED 持有，許可證狀態為有效。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（抗 EGFR 單株抗體） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單；另依現有資訊，可留意血鎂、血鈣等電解質 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：已查得 27 筆交互作用紀錄，以下為主要項目：
  - **重度 (Major)**：Bevacizumab、Irinotecan（含微脂體劑型）、Amiodarone、Arsenic trioxide、Dofetilide、Dronedarone、Droperidol、Aminolevulinic acid、Levacetylmethadol
  - **中度 (Moderate)**：多種氫離子幫浦抑制劑（Omeprazole、Esomeprazole、Lansoprazole、Dexlansoprazole、Pantoprazole、Rabeprazole）、Methoxsalen、Disopyramide、Idelalisib 等
- **其他已知毒性（依預測資料所述）**：常見低血鎂與低血鈣，並有眼部及皮膚毒性（如角膜炎、皮膚反應）。

警語與禁忌症的詳細內容，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有 TxGNN 模型的高預測分數，沒有臨床試驗、文獻或明確機轉支持。
- Panitumumab 可能造成電解質失衡（低血鎂、低血鈣），對骨骼的影響方向不明，甚至可能有害。

**若要推進需要：**
- 補充詳細的作用機轉資料（MOA）
- 取得香港衛生署仿單的警語與禁忌症內容
- 進行 EGFR 阻斷與骨代謝關係的前臨床或機轉研究
- 蒐集 Panitumumab 使用者的骨密度或骨折相關觀察性資料

---

### 附註：第二個預測適應症

TxGNN 另預測 **嚴重非增殖性糖尿病視網膜病變 (Severe Nonproliferative Diabetic Retinopathy)**，分數 0.9905，證據等級同為 L5，建議決策為 Hold。目前無臨床試驗與文獻支持。EGFR 訊號雖與視網膜血管及發炎病變有鬆散關聯，但 Panitumumab 是大分子全身性抗體，眼部穿透性有限，且本身有眼部與皮膚毒性。現有的標準治療（抗 VEGF、雷射）已相當完善，因此對新候選藥物的要求更高。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

