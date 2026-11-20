---
layout: default
title: Dipyridamole
parent: 僅模型預測 (L5)
nav_order: 285
evidence_level: L5
indication_count: 6
monitor_inn: "DIPYRIDAMOLE"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "cavernous sinus thrombosis", "lateral sinus thrombosis"]
last_modified_at: 2026-11-03
description: "Dipyridamole：預測新適應症為Sick sinus syndrome 2, autosomal dominant（證據等級 L5）。香港藥劑製品註冊：10 張（有效 10 張）"
---

# Dipyridamole
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

## Dipyridamole: Sick sinus syndrome 2, autosomal dominant
{: .text-alpha }

## 一句話總結

Dipyridamole 是一種抗血小板與血管擴張藥物。
TxGNN 模型預測它可能對**體染色體顯性遺傳病態竇房結症候群第 2 型 (sick sinus syndrome 2, autosomal dominant)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | Sick sinus syndrome 2, autosomal dominant |
| TxGNN 預測分數 | 0.9989 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 10 張／共 10 張） |
| 許可證數 | 10 張（有效 10 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Dipyridamole 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Dipyridamole在體外及體內均可抑制血小板、內皮細胞及紅血球對腺苷的攝取；在治療濃度（0.5至1.9 mcg/mL）下，此抑制作用呈劑量依賴性。此抑制作用導致局部腺苷濃度增加，腺苷作用於血小板A 2 受體，從而刺激血小板腺苷酸環化酶，並增加血小板環-3',5'-單磷酸腺苷（cAMP）濃度。」英文原文："Dipyridamole inhibits the uptake of adenosine into platelets, endothelial cells and erythrocytes in vitro and in vivo; the inhibition occurs in a dose-dependent manner at therapeutic concentrations (0.5 to 1.9 mcg/mL). This inhibition results in an increase in local concentrations of adenosine which acts on the platelet A 2 -receptor thereby stimulating platelet adenylate cyclase and increasing platelet cyclic-3',5'-adenosine monophosphate (cAMP) levels."（[DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5)，版本日期 2026-04-29；查閱日期 2026-11-19）。就已知的藥理特性而言，Dipyridamole 會提高細胞外腺苷濃度，產生抗血小板與血管擴張作用。

然而，腺苷可減慢竇房結與房室結的傳導。因此在竇房結功能異常的情況下，這類藥物理論上可能使病情惡化，而非改善。目前資料中看不到支持其有益的機轉。

此預測僅來自模型分數，缺乏任何臨床或生物學證據支持，應視為待驗證的計算結果。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-15915 | DIPYRIDAMOLE S C TAB 25MG | KAI YUEN PHARMACEUTICAL CO |
| HK-35124 | PROCARDIN 75 TAB 75MG | STAR MEDICAL SUPPLIES LTD |
| HK-39893 | APO-DIPYRIDAMOLE FC TAB 25MG | HIND WING CO LTD |
| HK-02701 | PERSANTIN TAB (S.C.) 75MG | ZUELLIG PHARMA LIMITED |
| HK-44759 | DIPAMOL TAB 75MG | APT PHARMA LIMITED |

目前香港共有 10 張有效的單方許可證，此處僅列出 5 張。

## 安全性考量

- **藥物交互作用**：已查得 100 筆交互作用紀錄，其中列為中度者包括 Dexfenfluramine、Sibutramine、Fenfluramine；另有 Acetylsalicylic acid、Cimetidine、Metformin、Omeprazole、Morphine 等，其嚴重程度尚未分級。

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型分數，沒有任何臨床試驗或文獻支持，證據等級為 L5。
- 藥物提高腺苷的作用可能減慢竇房結傳導，機轉上有可能加重而非改善竇房結功能異常，不建議推進。

**若要推進需要：**
- 提出支持其對竇房結功能有益的機轉假說，並以前臨床研究驗證
- 取得完整的作用機轉資料與原廠仿單中的警語、禁忌症
- 評估心律傳導方面的安全風險（特別是心搏過緩與房室傳導阻滯）
- 在出現任何直接針對此疾病的研究證據前，維持暫緩狀態

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

