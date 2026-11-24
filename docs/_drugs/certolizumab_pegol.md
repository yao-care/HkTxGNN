---
layout: default
title: Certolizumab Pegol
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 3
monitor_inn: "CERTOLIZUMAB PEGOL"
predicted_indications: ["hypermobility of coccyx", "Kummell disease", "vertebral disease"]
last_modified_at: 2026-11-24
description: "Certolizumab Pegol：預測新適應症為尾骨過度活動 (hypermobility of coccyx)（證據等級 L5）。香港藥劑製品註冊：2 張（有效 2 張）"
---

# Certolizumab Pegol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

## Certolizumab Pegol：腫瘤壞死因子抑制劑 → 尾骨過度活動 (hypermobility of coccyx)
{: .text-alpha }

## 一句話總結

Certolizumab Pegol 是一種聚乙二醇化的抗 TNF-α 抗體片段，屬於生物製劑。
TxGNN 模型預測它可能對**尾骨過度活動 (hypermobility of coccyx)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬於模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 尾骨過度活動 (hypermobility of coccyx) |
| TxGNN 預測分數 | 0.9975 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Certolizumab Pegol 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Certolizumab pegol 與人類 TNFα 結合，其 KD 為 90pM。TNFα 是一種關鍵的促發炎細胞激素，在發炎過程中扮演核心角色。Certolizumab pegol 選擇性中和 TNFα（在體外 L929 小鼠纖維肉瘤細胞毒性試驗中，抑制人類 TNFα 的 IC 90 為 4 ng/mL），但不中和淋巴毒素 α（TNFβ）。」英文原文："Certolizumab pegol binds to human TNFα with a KD of 90pM. TNFα is a key pro-inflammatory cytokine with a central role in inflammatory processes. Certolizumab pegol selectively neutralizes TNFα (IC 90 of 4 ng/mL for inhibition of human TNFα in the in vitro L929 murine fibrosarcoma cytotoxicity assay) but does not neutralize lymphotoxin α (TNFβ)."（[DailyMed: Cimzia (certolizumab pegol) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b4c2c9dc-a0bb-4d64-a667-a67ebe88392d)，版本日期 2026-10-29；查閱日期 2026-11-19）。根據已知資訊，Certolizumab Pegol 是一種抗 TNF-α 的聚乙二醇化抗體片段，其抑制 TNF 的作用常用於發炎性關節與脊椎疾病，機轉上的適用範圍主要在 TNF 驅動的發炎性疾病。

然而，尾骨過度活動主要是機械性或創傷性的問題，沒有明確的 TNF 驅動發炎機制可以支持這個連結。因此，雖然模型分數很高，但這只是計算層面的預測，目前無法以機轉合理解釋。

與原藥物用途的相似性分析尚未完成，也沒有路徑相容性的評估資料。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-61805 | CIMZIA SOLUTION FOR INJ 200MG | 單一成分 | UCB PHARMA (HONG KONG) LIMITED | 有效 |
| HK-67262 | CIMZIA SOLUTION FOR INJECTION IN PRE-FILLED PENS 200MG/1ML | 單一成分 | UCB PHARMA (HONG KONG) LIMITED | 有效 |

<!-- licenses:end -->

## 安全性考量

- **藥物交互作用**：共查得 100 筆交互作用紀錄，以下為主要項目：
  - **重度**：Hydrocortisone、Triamcinolone、Dexamethasone、Betamethasone、Budesonide、Prednisolone、Prednisone（皆為皮質類固醇）；Deferiprone；Ibritumomab tiuxetan；Iobenguane (I-131)；Tositumomab (I-131)
  - **中度**：Metronidazole、Pegvaliase、Rosuvastatin、Simvastatin、Tinidazole
  - **輕度**：Zinc acetate、Zinc gluconate、Zinc sulfate

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前沒有任何臨床試驗或文獻研究此疾病，僅有模型的高分預測（0.9975），且尾骨過度活動屬機械性問題，缺乏 TNF 相關的機轉依據。

**若要推進需要：**
- 取得 Certolizumab Pegol 的作用機轉資料，並釐清其與尾骨過度活動之間是否有合理的生物學連結
- 取得香港仿單的警語與禁忌症資料，以進行安全性篩選
- 有直接針對尾骨過度活動的臨床前或臨床研究，才能考慮提升證據等級

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Cimzia (certolizumab pegol) prescribing information, UCB, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b4c2c9dc-a0bb-4d64-a667-a67ebe88392d) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

