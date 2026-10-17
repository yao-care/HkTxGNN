---
layout: default
title: Trastuzumab Deruxtecan
parent: 僅模型預測 (L5)
nav_order: 897
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Trastuzumab Deruxtecan：預測新適應症為藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "TRASTUZUMAB DERUXTECAN"
predicted_indications: ["drug-induced osteoporosis"]
---

# Trastuzumab Deruxtecan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Trastuzumab Deruxtecan：從（原適應症資料缺漏）到藥物誘發性骨質疏鬆

## 一句話總結

Trastuzumab deruxtecan 是一種以 HER2 為標靶的抗體藥物複合體（ADC），在香港以 ENHERTU 品名上市，但本報告編纂的資料中沒有記載其核准適應症。
TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis)** 有效。
目前**沒有臨床試驗與文獻**支持，僅有模型預測分數，證據薄弱。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 藥物誘發性骨質疏鬆 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 99.31% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就一般藥理知識而言，trastuzumab deruxtecan 是 HER2 標靶抗體藥物複合體，其酬載 deruxtecan 為拓樸異構酶 I 抑制劑（camptothecin 衍生物）。這段說明來自一般藥理學推論，並非本次編纂資料所提供。

HER2 標靶的細胞毒性藥物傳遞，與藥物誘發性骨質疏鬆之間，並沒有已知的生物學關聯。此預測很可能是知識圖譜結構造成的假象，例如與會造成骨質流失的腫瘤相關藥物（如芳香環轉化酶抑制劑、糖皮質素）有共同關聯，或是因為該疾病本身屬於不良反應相關節點，而非真正的治療標的。

細胞毒性化療與癌症治療相關的骨質流失之間，若有關聯，反而暗示潛在的傷害訊號，而非益處。因此，高預測分數不應被視為有效性的證據。

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
| HK-67288 | ENHERTU POWDER FOR CONCENTRATE FOR SOLUTION FOR INFUSION 100MG | 未載明 | 未載明 |

廠商為 DAIICHI SANKYO HONG KONG LIMITED，許可證狀態為有效（單一成分）。

---

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（HER2 抗體藥物複合體，酬載為拓樸異構酶 I 抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

---

## 安全性考量

- **藥物交互作用**：資料庫共查得 42 筆交互作用，以下列出部分主要項目：
  - **重大 (Major)**：Deferiprone、Samarium (153Sm) lexidronam、Adalimumab、Baricitinib、Certolizumab pegol、Cladribine、Leflunomide、Natalizumab
  - **中度 (Moderate)**：Palifermin、Strontium chloride Sr-89、Roflumilast、Chloramphenicol、Alemtuzumab、Azathioprine、Niraparib 等

主要警語與禁忌症資料缺漏，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 僅有 TxGNN 模型預測分數（99.31%），沒有任何臨床試驗或文獻，證據等級為 L5。
- 機轉上沒有合理的連結，且細胞毒性藥物可能對骨骼健康不利，預測很可能是圖譜假象。

**若要推進需要：**
- 取得香港衛生署仿單，補齊核准適應症、警語與禁忌症
- 補充 DrugBank 作用機轉資料
- 以文獻回顧確認 HER2 標靶 ADC 與骨代謝是否有任何關聯
- 在無機轉與臨床證據前，不建議投入進一步開發資源
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

