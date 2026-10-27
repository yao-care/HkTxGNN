---
layout: default
title: Lurbinectedin
parent: 僅模型預測 (L5)
nav_order: 546
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lurbinectedin：預測新適應症為多發性內分泌腫瘤 (multiple endocrine neoplasia)（證據等級 L5）。原適應症：許可證資料未載明"
monitor_inn: "Lurbinectedin"
predicted_indications: ["multiple endocrine neoplasia", "HIV infectious disease", "rheumatoid arthritis", "amyotrophic lateral sclerosis", "cytomegalovirus infection", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "infectious bovine rhinotracheitis", "malignant catarrh", "Mills syndrome"]
---

# Lurbinectedin
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

## Lurbinectedin：從原適應症（許可證未載明）到多發性內分泌腫瘤
{: .text-alpha }

## 一句話總結

Lurbinectedin 是一種細胞毒性抗腫瘤藥物，目前在香港已有一張有效許可證，但資料中未記載核准適應症。
TxGNN 模型預測它可能對**多發性內分泌腫瘤 (multiple endocrine neoplasia)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅屬模型預測階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 許可證資料未載明 |
| 預測新適應症 | 多發性內分泌腫瘤 (multiple endocrine neoplasia) |
| TxGNN 預測分數 | 99.44% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據一般藥理知識，Lurbinectedin 是一種烷化類藥物，會結合 DNA 小溝並抑制致癌基因的轉錄。此推論並非來自本報告所整理的資料，需另行查證。

此機轉對神經內分泌腫瘤可能有相關性，例如該藥在小細胞肺癌（屬神經內分泌癌）已有應用。多發性內分泌腫瘤同樣涉及內分泌／神經內分泌組織，因此有一定的推論空間。

但此連結目前純屬推測：沒有任何針對多發性內分泌腫瘤的試驗或文獻，TxGNN 分數也只是計算預測。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68069 | ZEPZELCA POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 4MG | 未載明（輸注用濃縮液粉末） | 未載明 |

持證商為 LUYE PHARMA HONG KONG LIMITED，屬單一成分製劑，狀態有效。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 傳統細胞毒性藥物（DNA 結合／轉錄抑制類） |
| 骨髓抑制風險 | 預測資料指出有骨髓抑制疑慮，詳細分級請參考原廠仿單 |
| 致吐性分級 | 請參考原廠仿單 |
| 監測項目 | 建議監測 CBC（含分類）、肝腎功能 |
| 處置防護 | 請依細胞毒性藥物處置規範操作 |

請參考原廠仿單的警語與注意事項。

## 安全性考量

- **藥物交互作用**：共查得 100 筆交互作用，以下為部分主要項目：
  - **重大 (Major)**：Aprepitant、Dexamethasone、Clarithromycin、Cobicistat、Deferiprone、Lumacaftor、Samarium (153Sm) lexidronam
  - **中度 (Moderate)**：Cimetidine、Naltrexone、Clotrimazole、Ticagrelor、Ivacaftor、Mercaptopurine 等
  - **輕微 (Minor)**：Levofloxacin

其中 Aprepitant 與 Dexamethasone 常用於化療止吐，臨床併用時需特別留意。

其餘警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有模型預測（L5），沒有臨床試驗或文獻佐證，且作用機轉與許可證適應症資料皆缺漏。
- 這是細胞毒性藥物，安全性風險較高，現階段無法支持推進。

**若要推進需要：**
- 取得香港衛生署仿單，補齊核准適應症、警語與禁忌症
- 補充 DrugBank 的作用機轉資料，釐清與多發性內分泌腫瘤的機轉連結
- 搜尋並評估神經內分泌腫瘤相關的臨床前或臨床研究
- 評估骨髓抑制與藥物交互作用的風險管理計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

