---
layout: default
title: Thyrotropin Alfa
parent: 僅模型預測 (L5)
nav_order: 875
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-24
description: "Thyrotropin Alfa：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L5）。原適應症：目前許可證資料未載明核准適應症"
monitor_inn: "Thyrotropin alfa"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "Raynaud disease", "atrophoderma vermiculata", "ulerythema ophryogenesis", "pulmonary hypertension", "kyphoscoliotic heart disease", "postural orthostatic tachycardia syndrome", "hyperthyroidism"]
---

# Thyrotropin Alfa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Thyrotropin alfa：從甲狀腺癌診斷輔助到偏頭痛（僅為模型預測）
{: .text-alpha }

## 一句話總結

Thyrotropin alfa 是重組人類促甲狀腺素（TSH），在香港以 THYROGEN 品名上市。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，屬於純模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前許可證資料未載明核准適應症 |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

根據美國 FDA 核准的 Thyrotropin Alfa 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「促甲狀腺激素（TSH）為一種腦下垂體激素，可刺激甲狀腺產生甲狀腺激素。Thyrotropin alfa 與正常甲狀腺上皮細胞或分化良好之甲狀腺癌組織上之 TSH 受體結合，可刺激碘之攝取及有機化，以及甲狀腺球蛋白（Tg）、三碘甲狀腺素（T3）及甲狀腺素（T4）之合成與分泌。」英文原文："Thyrotropin (TSH) is a pituitary hormone that stimulates the thyroid gland to produce thyroid hormone. Binding of thyrotropin alfa to TSH receptors on normal thyroid epithelial cells or on well-differentiated thyroid cancer tissue stimulates iodine uptake and organification, and synthesis and secretion of thyroglobulin (Tg), triiodothyronine (T3) and thyroxine (T4)."（[DailyMed: Thyrogen (thyrotropin alfa) prescribing information, Genzyme Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b52dfa36-f90b-4e19-9b5e-26db9d04df2b)，版本日期 2023-02-24；查閱日期 2026-11-19）。就已知資訊，Thyrotropin alfa 是重組 TSH，作用於甲狀腺組織的 TSH 受體，促進甲狀腺細胞活性與甲狀腺激素的產生。

目前沒有建立起來的機轉連結可以說明它與偏頭痛的關係。分數來自 TxGNN 模型（深度學習），可能反映模型在相關疾病之間學到的相似性，而不是生物學證據。若要把兩者連起來（例如透過甲狀腺荷爾蒙狀態影響偏頭痛），目前也只是推測。

其他排名靠前的預測（偏頭痛亞型、雷諾氏症、肺動脈高壓、姿勢性心搏過速症候群等）同樣沒有試驗或文獻支持，多半反映 TxGNN 模型（深度學習）在相關疾病之間學到的相似性，而不是生物學證據。其中**甲狀腺機能亢進**在機轉上反而是禁忌，因為 TSH 受體刺激會增加甲狀腺激素分泌，可能惡化病情。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-54932 | THYROGEN FOR INJ 1.1MG | 單一成分 | SANOFI HONG KONG LIMITED | 有效 |

<!-- licenses:end -->

---

## 安全性考量

- **藥物交互作用**：已查得 45 筆交互作用紀錄，以下列出部分（皆為中度）：
  - 降血糖藥物類：Acarbose、Metformin、Glimepiride、Glipizide、Glyburide、Chlorpropamide、Acetohexamide
  - DPP-4 抑制劑與 SGLT2 抑制劑：Alogliptin、Saxagliptin、Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin
  - GLP-1 類藥物：Albiglutide、Dulaglutide、Exenatide、Semaglutide
  - 胰島素類：Insulin human、Insulin aspart

  整體看來，併用糖尿病藥物時需留意血糖控制的變化。

- **預測適應症的安全疑慮**：對於甲狀腺機能亢進等預測項目，TSH 刺激在機轉上可能使病情惡化。姿勢性心搏過速症候群也有類似疑慮，外源性 TSH 可能增加甲狀腺激素輸出而加重心搏過速。

其餘警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都僅有模型分數，沒有臨床試驗或文獻，證據等級為 L5。
- 缺乏可辨識的機轉連結，且部分預測（如甲狀腺機能亢進）在機轉上有安全疑慮，目前不建議投入開發。

**若要推進需要：**
- 取得 Thyrotropin alfa 的詳細作用機轉資料（MOA）
- 取得香港原廠仿單，確認核准適應症、警語與禁忌症
- 以文獻回顧確認 TSH 或甲狀腺功能與偏頭痛是否有可驗證的生物學關聯
- 如找到合理假說，先進行前臨床或小規模探索性研究，再重新評估

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Thyrogen (thyrotropin alfa) prescribing information, Genzyme Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b52dfa36-f90b-4e19-9b5e-26db9d04df2b) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

