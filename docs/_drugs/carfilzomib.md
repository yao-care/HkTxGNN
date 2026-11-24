---
layout: default
title: Carfilzomib
parent: 僅模型預測 (L5)
nav_order: 164
evidence_level: L5
indication_count: 5
monitor_inn: "CARFILZOMIB"
predicted_indications: ["CMM7", "pediatric leptomeningeal melanoma", "epithelioid cell uveal melanoma", "vulvar melanoma (disease)", "melanoma"]
last_modified_at: 2026-11-24
description: "Carfilzomib：預測新適應症為CMM7（證據等級 L5）。香港藥劑製品註冊：2 張（有效 2 張）"
---

# Carfilzomib
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

## Carfilzomib：蛋白酶體抑制劑 → CMM7 (CMM7)
{: .text-alpha }

## 一句話總結

Carfilzomib 是一種蛋白酶體抑制劑，目前在香港有 2 張有效許可證。
TxGNN 模型預測它可能對 **CMM7 (CMM7)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個預測，僅屬模型預測階段。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | CMM7 (CMM7) |
| TxGNN 預測分數 | 0.9937 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Carfilzomib 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Carfilzomib 是一種四胜肽環氧酮類蛋白酶體抑制劑，可不可逆地結合於 20S 蛋白酶體（26S 蛋白酶體內的蛋白水解核心顆粒）含 N 端蘇胺酸的活性位點。Carfilzomib 在體外對實體腫瘤細胞及血液腫瘤細胞具有抗增生及促細胞凋亡活性。」英文原文："Carfilzomib is a tetrapeptide epoxyketone proteasome inhibitor that irreversibly binds to the N-terminal threonine-containing active sites of the 20S proteasome, the proteolytic core particle within the 26S proteasome. Carfilzomib had antiproliferative and proapoptotic activities in vitro in solid and hematologic tumor cells."（[DailyMed: Kyprolis (carfilzomib) prescribing information, Onyx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ea66eb30-e665-4693-99a1-a9d3b4bbe2d6)，版本日期 2025-06-18；查閱日期 2026-11-19）。Carfilzomib 屬於蛋白酶體抑制劑，此類藥物會干擾癌細胞的蛋白質降解與存活路徑，因此機轉上可能影響黑色素瘤相關的細胞存活路徑。

不過，這是一項推論，並沒有針對 CMM7 的任何臨床試驗、文獻或其他資料支持。「CMM7」的疾病定義與其和其他黑色素瘤類疾病的關係，也需要進一步釐清。

整體而言，這個預測目前僅來自模型分數（0.9937），尚無實際研究證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-65431 | KYPROLIS FOR INJECTION 30MG/VIAL | 單一成分 | AMGEN HONG KONG LIMITED | 有效 |
| HK-64828 | KYPROLIS FOR INJECTION 60MG/VIAL | 單一成分 | AMGEN HONG KONG LIMITED | 有效 |

<!-- licenses:end -->

## 細胞毒性

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（蛋白酶體抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 建議監測 CBC、肝腎功能；詳情請參考原廠仿單 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，以下為部分列示：
  - 嚴重（Major）：Oxandrolone、Oxymetholone、Stanozolol、Deferiprone、Samarium (153Sm) lexidronam、Aminocaproic acid、Avatrombopag
  - 中度（Moderate）：Metronidazole、Naltrexone、Rosuvastatin、Simvastatin、Tinidazole、Palifermin

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
CMM7 沒有任何臨床試驗或文獻支持，證據等級為 L5，僅有模型預測分數。作用機轉資料也有缺口，目前不適合推進。

**若要推進需要：**
- 釐清 CMM7 的疾病定義與臨床意義
- 補充 carfilzomib 的作用機轉資料
- 進行針對此疾病的前臨床研究（細胞或動物模型）
- 取得香港原廠仿單，完成警語與禁忌症的安全性評估

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Kyprolis (carfilzomib) prescribing information, Onyx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=ea66eb30-e665-4693-99a1-a9d3b4bbe2d6) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

