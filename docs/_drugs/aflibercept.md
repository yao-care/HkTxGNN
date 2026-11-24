---
layout: default
title: Aflibercept
parent: 僅模型預測 (L5)
nav_order: 28
evidence_level: L5
indication_count: 1
monitor_inn: "Aflibercept"
predicted_indications: ["esotropia"]
last_modified_at: 2026-11-24
description: "Aflibercept：預測新適應症為內斜視 (esotropia)（證據等級 L5）。香港藥劑製品註冊：7 張（有效 7 張）"
---

# Aflibercept
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

## Aflibercept：VEGF 抑制劑（VEGF-A/VEGF-B/PlGF 誘捕蛋白）→ 內斜視 (esotropia)
{: .text-alpha }

## 一句話總結

Aflibercept 是一種針對血管內皮生長因子（VEGF）家族的誘捕型融合蛋白。
TxGNN 模型預測它可能對**內斜視 (esotropia)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 內斜視 (esotropia) |
| TxGNN 預測分數 | 0.9938 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 7 張／共 7 張） |
| 許可證數 | 7 張（有效 7 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Aflibercept 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「血管內皮生長因子-A（VEGF-A）及胎盤生長因子（PlGF）為 VEGF 血管新生因子家族的成員，可作為內皮細胞的促有絲分裂因子、趨化因子及血管通透性因子。VEGF 經由存在於內皮細胞表面的兩種受體酪胺酸激酶 VEGFR-1 及 VEGFR-2 發揮作用。[…] Aflibercept 產品作為一種可溶性誘餌受體，可與 VEGF - A 及 PlGF 結合，從而抑制這些同源 VEGF 受體的結合與活化。」英文原文："Vascular endothelial growth factor-A (VEGF-A) and placental growth factor (PlGF) are members of the VEGF family of angiogenic factors that can act as mitogenic, chemotactic, and vascular permeability factors for endothelial cells. VEGF acts via two receptor tyrosine kinases, VEGFR-1 and VEGFR-2, present on the surface of endothelial cells. […] Aflibercept products act as a soluble decoy receptor that binds VEGF - A and PlGF, and thereby can inhibit the binding and activation of these cognate VEGF receptors."（[DailyMed: Pavblu (aflibercept-ayyh) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c61062f3-80ec-4a20-8c28-46e468592a06)，版本日期 2026-10-29；查閱日期 2026-11-19）。根據已知資訊，Aflibercept 屬於 VEGF-A、VEGF-B 與胎盤生長因子（PlGF）的誘捕型抑制劑，主要作用是阻斷這些因子與受體結合，抑制病理性血管新生與血管通透性增加。

內斜視是眼位排列異常的疾病，成因多與神經肌肉控制或屈光因素有關，與 VEGF 驅動的血管病變並無明確的直接關聯。因此，從機轉上看，目前找不到合理的直接連結。

0.9938 的高分只代表模型的預測輸出，並沒有任何試驗或文獻佐證。這個預測應視為待驗證的假說，而非有依據的新用途。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-68960 | EYLEA SOLUTION FOR INTRAVITREAL INJECTION IN PRE-FILLED SYRINGE 114.3MG/ML | 單一成分 | BAYER HEALTHCARE LIMITED | 有效 |
| HK-61971 | EYLEA SOLUTION FOR INTRAVITREAL INJECTION 40MG/ML | 單一成分 | BAYER HEALTHCARE LIMITED | 有效 |
| HK-67381 | EYLEA SOLUTION FOR INTRAVITREAL INJECTION IN PRE-FILLED SYRINGE 40MG/ML | 單一成分 | BAYER HEALTHCARE LIMITED | 有效 |
| HK-68359 | EYLEA SOLUTION FOR INTRAVITREAL INJECTION 114.3MG/ML | 單一成分 | BAYER HEALTHCARE LIMITED | 有效 |
| HK-62551 | ZALTRAP CONCENTRATE FOR SOLUTION FOR INFUSION 100MG/4ML | 單一成分 | SANOFI HONG KONG LIMITED | 有效 |

上表列出其中 5 張（共 7 張）。

<!-- licenses:end -->

## 安全性考量

- **藥物交互作用**：本次資料共收錄 78 筆交互作用，以下為部分主要項目：
  - 重大（Major）：Deferiprone、Samarium (153Sm) lexidronam、Adalimumab、Baricitinib、Certolizumab pegol、Cladribine、Clozapine
  - 中度（Moderate）：Strontium chloride Sr-89、Roflumilast、Chloramphenicol、Zidovudine、Alemtuzumab、Anakinra、Azathioprine、Canakinumab

其他安全性資訊（警語、禁忌症）請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前只有模型預測分數，沒有任何臨床試驗或文獻直接研究 Aflibercept 用於內斜視，證據等級為 L5。
- 機轉上，VEGF 抑制與眼位異常之間缺乏合理的直接連結。

**若要推進需要：**
- 補充 Aflibercept 的作用機轉資料，並釐清其與內斜視病理的可能關聯
- 進行系統性文獻回顧，確認是否存在任何前臨床或病例層級的證據
- 取得原廠仿單的警語與禁忌症，完成基本安全性評估
- 在有前臨床或機轉研究支持之前，不建議投入臨床開發資源

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Pavblu (aflibercept-ayyh) prescribing information, Amgen, Inc](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c61062f3-80ec-4a20-8c28-46e468592a06) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

