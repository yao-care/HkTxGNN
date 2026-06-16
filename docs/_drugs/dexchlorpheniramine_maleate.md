---
layout: default
title: Dexchlorpheniramine Maleate
parent: 僅模型預測 (L5)
nav_order: 225
evidence_level: L5
indication_count: 1
---

# Dexchlorpheniramine Maleate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Dexchlorpheniramine Maleate：從抗過敏到急性間歇性紫質症

## 一句話總結

Dexchlorpheniramine Maleate 是第一代 H1 受體拮抗劑（Chlorpheniramine 的 R-旋光異構體），廣泛用於過敏症狀的控制。TxGNN 模型預測它可能對**急性間歇性紫質症（Acute Intermittent Porphyria, AIP）** 有效，但目前**無任何臨床試驗或文獻**支持此方向，且已知藥理機轉存在安全疑慮，建議暫緩評估。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 過敏症狀（H1 受體拮抗劑） |
| 預測新適應症 | 急性間歇性紫質症（Acute Intermittent Porphyria） |
| TxGNN 預測分數 | 99.12% |
| 證據等級 | L5 |
| 香港上市 | ✗ 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | **Hold** |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA 為 Data Gap）。根據已知資訊，Dexchlorpheniramine 是 Chlorpheniramine 的 R-旋光異構體，屬第一代 H1 受體拮抗劑。其在過敏症狀中的療效已有臨床實證，理論上 H1 拮抗作用可能透過抑制肥大細胞活化及組胺介導的神經炎症路徑，間接減緩 AIP 急性發作時的神經內臟症狀。

然而，TxGNN 的高預測分數很可能反映的是**知識圖譜中 H1 拮抗劑與廣泛神經系統疾病的共通連結**，而非 AIP 的特異性機轉。事實上，**多數第一代抗組胺藥**被 AIP 藥物安全資料庫（如 European Porphyria Network）列為「潛在危險」或「未確定」類別。

核心安全疑慮在於：第一代抗組胺藥可能誘導肝臟 **ALAS1（δ-aminolevulinate synthase 1）**的表達，導致 ALA（δ-胺基乙醯丙酸）及 PBG（卟膽原）等前驅物堆積，反而可能**觸發 AIP 急性發作**——即預測目標的對立效果。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

本藥物在香港（Department of Health）目前**無已登記之許可證**，尚未上市。

---

## 安全性考量

> 安全性資訊請參考原廠仿單。

此外，根據 AIP 特異性藥物安全性考量，使用前應特別查核：
- **AIP 藥物安全資料庫**（[www.drugs-porphyria.org](https://www.drugs-porphyria.org)）確認本藥是否列為「安全」、「潛在危險」或「未確定」類別。
- 第一代抗組胺藥誘導 **ALAS1** 的肝臟表達，是 AIP 患者用藥時最主要的安全疑慮。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 本預測目前處於 L5（僅模型輸出，無實證支持），且藥物的已知藥理機轉可能與 AIP 治療目標相悖，存在誘發急性發作的潛在風險。
- 藥物在香港無上市紀錄，監管路徑亦需從零建立。

**若要推進需要：**
1. **AIP 藥物安全性查核**：至 [European Porphyria Network 安全資料庫](https://www.drugs-porphyria.org) 確認 Dexchlorpheniramine 的分類狀態
2. **MOA 資料補充**：透過 DrugBank API 取得完整作用機轉資料（Data Gap DG002）
3. **仿單警語與禁忌**：下載香港原廠仿單 PDF 解析安全性資訊（Data Gap DG001）
4. **前臨床文獻搜索**：擴大搜尋範圍，確認是否有 H1 拮抗劑 × AIP 的體外或動物實驗資料
5. **若安全性疑慮無法排除，建議轉而評估 AIP 安全藥物清單中的其他再利用候選**
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

