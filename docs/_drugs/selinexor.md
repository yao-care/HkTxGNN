---
layout: default
title: Selinexor
parent: 僅模型預測 (L5)
nav_order: 804
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Selinexor：預測新適應症為藥物誘發性骨質疏鬆症 (Drug-induced Osteoporosis)（證據等級 L5）。原適應症：資料未載明"
monitor_inn: "SELINEXOR"
predicted_indications: ["drug-induced osteoporosis"]
---

# Selinexor
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

## Selinexor：從（原適應症未載明）到藥物誘發性骨質疏鬆症
{: .text-alpha }

## 一句話總結

Selinexor 是一種 XPO1（exportin-1）核輸出抑制劑，屬於抗腫瘤藥物，在香港已有上市許可證，但本次整理的資料中未載明其核准適應症。
TxGNN 模型預測它可能對**藥物誘發性骨質疏鬆症 (Drug-induced Osteoporosis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明 |
| 預測新適應症 | 藥物誘發性骨質疏鬆症 (Drug-induced Osteoporosis) |
| TxGNN 預測分數 | 0.9922 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Selinexor 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「在非臨床研究中，selinexor可透過阻斷輸出蛋白1（XPO1），可逆性地抑制腫瘤抑制蛋白（TSP）、生長調節因子及致癌蛋白mRNA的核輸出。Selinexor抑制XPO1會導致TSP於細胞核內累積、數種致癌蛋白（如c-myc及cyclin D1）減少、細胞週期停滯，以及癌細胞凋亡。」英文原文："In nonclinical studies, selinexor reversibly inhibits nuclear export of tumor suppressor proteins (TSPs), growth regulators, and mRNAs of oncogenic proteins by blocking exportin 1 (XPO1). XPO1 inhibition by selinexor leads to accumulation of TSPs in the nucleus and reductions in several oncoproteins, such as c-myc and cyclin D1, cell cycle arrest, and apoptosis of cancer cells."（[DailyMed: Xpovio (selinexor) prescribing information, Karyopharm Therapeutics Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6dd2682-75a6-4863-90a8-a3197f6f78a8)，版本日期 2026-05-12；查閱日期 2026-11-19）。作用機轉已連同出處引用於上文（[DailyMed](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6dd2682-75a6-4863-90a8-a3197f6f78a8)）。

一個可能但**尚未驗證**的假說是：XPO1 抑制可能影響與骨重塑相關的訊號路徑（例如破骨細胞與造骨細胞的調控）。不過，現有資料中沒有任何證據支持此假說，0.9922 的預測分數只代表計算模型的推論，並非臨床驗證。

另外要注意，selinexor 是腫瘤用藥，已知可能出現噁心、疲倦、血球低下、低血鈉等不良反應。要把它用在長期、非腫瘤的骨質保護情境，其安全性尚未建立。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-67895 | XPOVIO TABLETS 20MG | 單一成分 | ANTENGENE THERAPEUTICS LIMITED | 有效 |

<!-- licenses:end -->

持證商：ANTENGENE THERAPEUTICS LIMITED（單一成分，狀態：有效）。

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（XPO1 核輸出抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項（一般建議包含 CBC、電解質如血鈉、肝腎功能） |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：資料庫共記錄 81 筆交互作用。其中較重要的 Major 等級包括：
  - Deferiprone
  - Samarium (153Sm) lexidronam
  - Adalimumab
  - Baricitinib
  - Certolizumab pegol
  - Cladribine
  - Clozapine

  Moderate 等級包括 Strontium chloride Sr-89、Roflumilast、Chloramphenicol、Zidovudine、Azathioprine、Anakinra 及多種疫苗等。這些多與血球抑制或免疫抑制疊加有關。對於已在使用糖皮質素等會誘發骨質疏鬆藥物的病人，用藥組合會更複雜。

其餘警語與禁忌症資料，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前僅有模型預測分數，沒有臨床試驗、文獻或已確認的作用機轉支持。
- 香港許可證的核准適應症與仿單警語也尚未取得，無法進行安全性評估。

**若要推進需要：**
- 取得香港衛生署的仿單，補齊核准適應症、警語與禁忌症。
- 補充 selinexor 的作用機轉資料（如自 DrugBank 取得）。
- 檢索 XPO1 抑制與骨代謝（破骨／造骨細胞）相關的前臨床研究，驗證機轉假說。
- 評估在非腫瘤、長期使用情境下的獲益與風險，包括血球低下、低血鈉等不良反應及多重藥物交互作用。

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Xpovio (selinexor) prescribing information, Karyopharm Therapeutics Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6dd2682-75a6-4863-90a8-a3197f6f78a8) |
| 2026-11-20 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄（2026-11-20 修訂，前版保留於紀錄） | [DailyMed: Xpovio (selinexor) prescribing information, Karyopharm Therapeutics Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=f6dd2682-75a6-4863-90a8-a3197f6f78a8) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

