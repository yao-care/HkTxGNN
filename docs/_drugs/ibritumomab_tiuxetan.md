---
layout: default
title: Ibritumomab Tiuxetan
parent: 僅模型預測 (L5)
nav_order: 451
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ibritumomab Tiuxetan：預測新適應症為急性淋巴母細胞白血病 (Acute Lymphoblastic/Lymphocytic Leukemia)（證據等級 L5）。原適應症：濾泡性淋巴瘤、成熟 B 細胞腫瘤"
monitor_inn: "IBRITUMOMAB TIUXETAN"
predicted_indications: ["acute lymphoblastic/lymphocytic leukemia", "small intestinal Burkitt lymphoma", "small intestinal mucosa-associated lymphoid tissue lymphoma", "thyroid gland mucosa-associated lymphoid tissue lymphoma", "breast mucosa-associated lymphoid tissue lymphoma"]
---

# Ibritumomab Tiuxetan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

## Ibritumomab Tiuxetan：從濾泡性淋巴瘤到急性淋巴母細胞白血病
{: .text-alpha }

## 一句話總結

Ibritumomab tiuxetan 是一種連結釔-90 (Y-90) 的抗 CD20 抗體放射免疫治療藥物，原本用於濾泡性淋巴瘤及成熟 B 細胞腫瘤。
TxGNN 模型預測它可能對**急性淋巴母細胞白血病 (Acute Lymphoblastic/Lymphocytic Leukemia)** 有效。
目前**沒有臨床試驗和文獻**支持，僅有模型預測分數，證據屬於最低等級。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 濾泡性淋巴瘤、成熟 B 細胞腫瘤（香港許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 急性淋巴母細胞白血病 (Acute Lymphoblastic/Lymphocytic Leukemia) |
| TxGNN 預測分數 | 99.78% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

其他預測適應症（同樣為 L5、建議 Hold）：

| 排名 | 預測適應症 | TxGNN 分數 |
|------|-----------|-----------|
| 2 | 小腸伯基特淋巴瘤 (Small intestinal Burkitt lymphoma) | 99.72% |
| 3 | 小腸黏膜相關淋巴組織淋巴瘤 (Small intestinal MALT lymphoma) | 99.69% |
| 4 | 甲狀腺黏膜相關淋巴組織淋巴瘤 (Thyroid MALT lymphoma) | 99.69% |
| 5 | 乳房黏膜相關淋巴組織淋巴瘤 (Breast MALT lymphoma) | 99.68% |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。依一般藥理知識（非本次彙整資料所提供），ibritumomab tiuxetan 是抗 CD20 抗體，透過 tiuxetan 螯合劑連結釔-90，將 β 射線精準送到表現 CD20 的 B 細胞。

B 細胞型急性淋巴母細胞白血病的部分病例會表現 CD20，因此在機轉上有可能適用。但這個推論尚未被驗證，且有兩項主要疑慮：
- ALL 的 CD20 表現不一致，且常常偏低。
- 放射免疫治療會造成骨髓抑制，而 ALL 本身常有骨髓侵犯，風險更為突出。

相較之下，排名第 2 至第 5 的預測（伯基特淋巴瘤與各部位 MALT 淋巴瘤）都屬於 CD20 陽性的 B 細胞腫瘤，與原適應症在生物學上更接近，機轉合理性較高。不過伯基特淋巴瘤通常使用強化化學免疫治療，放射免疫治療的角色未確立；局部 MALT 淋巴瘤則常以放射治療、手術或含 rituximab 的方案處理，額外效益不明。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-54925 | ZEVALIN FOR INFUSION 1.6MG/ML | 未載明 | 未載明 |

製造商／持證商為 Global Medical Solutions Hong Kong Limited，屬單一成分製劑，許可證狀態為有效。

---

## 細胞毒性

本藥為放射性標記的抗腫瘤藥物，用於淋巴瘤。本次彙整的資料中缺乏細胞毒性相關內容，請參考原廠仿單的警語與注意事項。

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 100 筆交互作用，以下為部分範例。
  - **Major（嚴重）**：Acetylsalicylic acid (aspirin)、Abciximab、Acalabrutinib、Ketorolac、Adalimumab、Ibuprofen、Alteplase、Anagrelide、Antithrombin III human。這些多與出血風險或免疫抑制有關。
  - **Moderate（中度）**：Fenfluramine、Dexfenfluramine、Sibutramine、Zidovudine、Alefacept、Alemtuzumab、Anakinra，以及部分疫苗（如破傷風類毒素、炭疽疫苗）。

香港仿單的警語與禁忌症資料尚未取得，其餘安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 五項預測皆僅有模型分數，沒有臨床試驗或文獻佐證（L5）。
- 首位預測 ALL 因 CD20 表現不一致及骨髓抑制風險，機轉上的疑慮較大。
- 香港仿單的安全性資料與作用機轉資料也尚未取得。

**若要推進需要：**
- 取得香港仿單，補齊警語與禁忌症，完成安全性初篩。
- 補齊 DrugBank 的作用機轉資料。
- 系統性檢索臨床試驗與文獻，優先評估與原適應症較接近的 CD20 陽性 B 細胞淋巴瘤（如 MALT 淋巴瘤）。
- 若仍考慮 ALL，需先確認 CD20 表現比例，並評估骨髓侵犯下的骨髓抑制風險。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

