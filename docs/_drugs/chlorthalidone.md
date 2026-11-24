---
layout: default
title: Chlorthalidone
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 9
monitor_inn: "CHLORTHALIDONE"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "acute pulmonary heart disease", "congenital hypotrichosis milia"]
last_modified_at: 2026-11-24
description: "Chlorthalidone：預測新適應症為原發性遺傳性青光眼 (primary hereditary glaucoma)（證據等級 L5）。香港藥劑製品註冊：4 張（有效 4 張）"
---

# Chlorthalidone
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

## Chlorthalidone：噻嗪類利尿劑（抑制 Na+/Cl- 共同轉運體）→ 原發性遺傳性青光眼 (primary hereditary glaucoma)
{: .text-alpha }

## 一句話總結

Chlorthalidone 是一種噻嗪類（thiazide-like）利尿劑。
TxGNN 模型預測它可能對**原發性遺傳性青光眼 (primary hereditary glaucoma)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 原發性遺傳性青光眼 (primary hereditary glaucoma) |
| TxGNN 預測分數 | 0.9992 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

根據美國 FDA 核准的 Chlorthalidone 處方資料（Prescribing Information）「Mechanism of Action」段（非官方翻譯）：「Chlorthalidone是一種具有抗高血壓活性的長效口服利尿劑。Chlorthalidone與苯并噻二嗪類（thiazide類）利尿劑的利尿作用似乎源自相似的機轉，且chlorthalidone與thiazide類利尿劑的最大效應似乎相近。」英文原文："Chlorthalidone is a long-acting oral diuretic with antihypertensive activity. The diuretic effects of chlorthalidone and the benzothiadiazine (thiazide) diuretics appear to arise from similar mechanisms and the maximal effect of chlorthalidone and the thiazides appear to be similar."（[DailyMed: Thalitone (chlorthalidone) prescribing information, Casper Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bc5a0299-115b-4e60-bb3f-c75a95c51c15)，版本日期 2026-06-25；查閱日期 2026-11-19）。根據已知資訊，Chlorthalidone 屬於噻嗪類利尿劑，一般認為其作用在於抑制腎臟遠曲小管的 Na+/Cl- 共同轉運體，促進鈉與水排出。

至於與青光眼的關聯，只能推測可能經由房水動力學改變或碳酸酐酶相關作用影響眼內壓，但這些都沒有本次資料的支持。原發性遺傳性青光眼主要由基因因素（如 MYOC、CYP1B1）造成，利尿劑不太可能處理其根本病因。

因此，0.9992 的分數應視為純計算層面的預測，不能當作療效證據。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

<!-- licenses:begin -->

| 許可證號 | 品名 | 類別 | 持證商 | 狀態 |
|------|------|------|------|------|
| HK-62250 | EDARBYCLOR TABLETS 40MG/25MG | 複方 | SYNMOSA BIOPHARMA (HONG KONG) COMPANY LIMITED | 有效 |
| HK-62249 | EDARBYCLOR TABLETS 40MG/12.5MG | 複方 | SYNMOSA BIOPHARMA (HONG KONG) COMPANY LIMITED | 有效 |
| HK-20350 | TENORET 50 TAB | 複方 | PRUDENTLINK LIMITED | 有效 |
| HK-13778 | TENORETIC TAB | 複方 | PRUDENTLINK LIMITED | 有效 |

<!-- licenses:end -->

## 安全性考量

- **藥物交互作用**：已查詢到 100 筆交互作用紀錄，其中較需注意的有：
  - 嚴重（Major）：Cisapride、Dolasetron
  - 中度（Moderate）：Acarbose、Metformin、Alogliptin、Albiglutide（降血糖藥物，可能影響血糖控制）；Hydrocortisone、Dexamethasone、Triamcinolone、Beclomethasone dipropionate（皮質類固醇）；Amphotericin B、Bupropion、Morphine、Omeprazole、Rabeprazole、Cholecalciferol 等
- 其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 目前完全沒有直接研究原發性遺傳性青光眼的臨床試驗或文獻，證據等級為 L5，僅有模型預測。
- 此疾病主要由基因因素引起，利尿劑的機轉難以對應，且全身性降血壓可能影響眼部灌流壓，療效方向不明。

**若要推進需要：**
- 前臨床或機轉研究，確認 chlorthalidone 是否影響房水生成或眼內壓
- 文獻回顧，檢視噻嗪類利尿劑與眼內壓、青光眼風險的既有觀察性資料
- 詳細的作用機轉資料（MOA）與原廠仿單的警語及禁忌症
- 若機轉上有依據，再設計小型探索性研究，並將眼內壓與眼部灌流壓列為主要觀察指標

<!-- review:begin log -->

## 查核紀錄

以下是本頁的查核紀錄。「缺乏作用機轉資料」的句子已改為所列官方仿單的節錄（附非官方翻譯）；模型預測、證據等級與結論都沒有改寫。

| 查核日期 | 項目 | 處理 | 依據 |
|------|------|------|------|
| 2026-11-19 | 「目前缺乏詳細的作用機轉資料」改為美國處方資料節錄 | 「缺乏作用機轉資料」句改為附出處的仿單節錄 | [DailyMed: Thalitone (chlorthalidone) prescribing information, Casper Pharma LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bc5a0299-115b-4e60-bb3f-c75a95c51c15) |

<!-- review:end log -->

## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

