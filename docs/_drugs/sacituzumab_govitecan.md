---
layout: default
title: Sacituzumab Govitecan
parent: 僅模型預測 (L5)
nav_order: 794
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Sacituzumab Govitecan：預測新適應症為藥物引起的骨質疏鬆症 (Drug-induced Osteoporosis)（證據等級 L5）。原適應症：香港許可證未載明核准適應症"
---

# Sacituzumab Govitecan
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

# Sacituzumab govitecan：從（原適應症資料未提供）到藥物引起的骨質疏鬆症

## 一句話總結

Sacituzumab govitecan 是一種以 Trop-2 為標靶的抗體藥物複合體（ADC），搭載拓樸異構酶 I 抑制劑 SN-38，屬於細胞毒性抗腫瘤藥物。
TxGNN 模型預測它可能對**藥物引起的骨質疏鬆症 (Drug-induced Osteoporosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症 |
| 預測新適應症 | 藥物引起的骨質疏鬆症 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Sacituzumab govitecan 是 Trop-2 導向的 ADC，其 SN-38 酬載透過抑制拓樸異構酶 I 發揮細胞毒性。

**坦白說，這個預測在機轉上並不合理。** 此藥的骨髓抑制與腸胃道毒性特性，無法解釋對骨質流失有益。TxGNN 的高分（0.998）僅來自知識圖譜的推論，並無生物學或臨床證據佐證。

其他排名靠前的預測（糖尿病視網膜病變、各類白內障等）同樣沒有試驗或文獻支持，部分白內障亞型的分數完全相同，顯示可能是圖譜鄰近關係造成的假象，而非藥物特異性的訊號。對慢性、非致命性疾病而言，全身性細胞毒性藥物的風險也很可能大於任何推測的效益。

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
| HK-67599 | TRODELVY POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 180MG | 未載明 | 未載明 |

製造商：Gilead Sciences Hong Kong Limited（單方，有效）。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 抗體藥物複合體（ADC），酬載為拓樸異構酶 I 抑制劑 SN-38，屬細胞毒性藥物 |
| 骨髓抑制風險 | 高（預測資料指出具骨髓抑制毒性；詳細數據請參考原廠仿單） |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 建議監測 CBC（含分類）、肝腎功能；詳細項目請參考原廠仿單 |
| 處置防護 | 應依細胞毒性藥物處置規範操作 |

---

## 安全性考量

- **藥物交互作用**：已查得 40 筆交互作用，以下列出部分主要項目：
  - **Major（嚴重）**：Irinotecan、Deferiprone、Fostamatinib、Adalimumab、Apalutamide、Certolizumab pegol、Cladribine、Dacomitinib、Leflunomide、Natalizumab、Nilotinib、Ozanimod
  - **Moderate（中度）**：Alefacept、Alemtuzumab、Anakinra、Canakinumab、Dimethyl fumarate、Lorlatinib、Ocrelizumab、Omacetaxine mepesuccinate

  多數為免疫抑制劑或其他骨髓抑制藥物，合併使用時需特別留意感染與血球低下風險。

其餘警語與禁忌症資料，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 證據僅有模型預測（L5），無任何臨床試驗或文獻，且機轉上找不到合理連結。
- 這是一個有顯著全身毒性的細胞毒性藥物，用於非致命的慢性骨質疏鬆症，風險效益比不利。

**若要推進需要：**
- 取得 Sacituzumab govitecan 的作用機轉資料，並釐清其與骨代謝的任何可能關聯
- 取得香港仿單的警語、禁忌症與核准適應症
- 有前臨床或機轉研究顯示對骨質流失有益，再考慮後續評估
- 建議把資源轉向機轉上更合理、且有證據的候選藥物或適應症
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

