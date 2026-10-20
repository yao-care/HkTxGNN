---
layout: default
title: Chlorthalidone
parent: 僅模型預測 (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Chlorthalidone：預測新適應症為原發性遺傳性青光眼 (Primary Hereditary Glaucoma)（證據等級 L5）。原適應症：高血壓、充血性心衰竭"
monitor_inn: "CHLORTHALIDONE"
predicted_indications: ["primary hereditary glaucoma", "open-angle glaucoma", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "acute pulmonary heart disease", "congenital hypotrichosis milia"]
---

# Chlorthalidone
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

# Chlorthalidone：從高血壓到原發性遺傳性青光眼

## 一句話總結

Chlorthalidone 是一種類噻嗪（thiazide-like）利尿劑，原本用於治療高血壓與充血性心衰竭。
TxGNN 模型預測它可能對**原發性遺傳性青光眼 (Primary Hereditary Glaucoma)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、充血性心衰竭（來自知識圖譜；香港許可證未提供核准適應症文字） |
| 預測新適應症 | 原發性遺傳性青光眼 (Primary Hereditary Glaucoma) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 4 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Chlorthalidone 是類噻嗪利尿劑，一般認為作用於腎臟遠端腎小管的 Na⁺/Cl⁻ 共同轉運體，促進鈉與水排出而降低血壓、減輕體液負荷。

原適應症（高血壓、心衰竭）與青光眼之間的關聯並不直接。有人推測利尿劑可能改變房水動力學而影響眼壓，但這僅是推測。原發性遺傳性青光眼主要由基因因素（如 MYOC、CYP1B1）造成，利尿劑不太可能處理其病因。此外，全身性降血壓可能降低眼灌注壓，影響方向並不明確。

因此，0.999 的高分應視為計算模型的輸出，而非有實證支持的結論。

**其他預測適應症（供參考）：** 排名前 10 的預測還包括開角型青光眼、惡性腎血管性高血壓、惡性高血壓腎病、肺高壓（兩種亞型）、Braddock 症候群、慢性肺心病、急性肺心病及先天性少毛症伴粟丘疹。其中**慢性肺心病**（分數 99.82%）是唯一有間接臨床線索者，包括一篇 1967 年以 Chlorthalidone 治療慢性肺心病所致充血性心衰竭的報告（PMID 5597001，可能為非對照研究），證據等級為 L4。若要優先探索，此方向比青光眼更有依據。

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
| HK-62250 | EDARBYCLOR TABLETS 40MG/25MG | 未提供 | 未提供 |
| HK-62249 | EDARBYCLOR TABLETS 40MG/12.5MG | 未提供 | 未提供 |
| HK-20350 | TENORET 50 TAB | 未提供 | 未提供 |
| HK-13778 | TENORETIC TAB | 未提供 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物與疾病的關聯資料，非仿單原文），部分重點如下：
  - 肝衰竭、腎臟疾病、無尿
  - 痛風、高尿酸血症、鉀缺乏、高鈣血症、腎鈣質沉著症
  - 第二型糖尿病
  - 全身性紅斑性狼瘡、氣喘、乾癬
  - 胰臟炎、消化性潰瘍
  - 心肌梗塞、冠狀動脈血栓、猝發性心臟驟停
  - 癲癇、焦慮症、神經症、輕度憂鬱症
- **藥物交互作用**：資料庫共查得 100 筆，以下為部分範例：
  - **重大 (Major)**：Cisapride、Dolasetron
  - **中度 (Moderate)**：Metformin、Acarbose、Alogliptin、Albiglutide（降血糖藥）；Hydrocortisone、Dexamethasone、Triamcinolone、Beclomethasone（皮質類固醇）；Amphotericin B、Omeprazole、Rabeprazole、Bupropion、Morphine、Cholecalciferol
  - **輕度 (Minor)**：Doxycycline、Atropine、Hyoscyamine

其餘警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 青光眼預測僅為模型輸出，無任何臨床試驗或文獻支持，機轉上也缺乏合理依據（遺傳性病因、利尿劑非青光眼標準療法）。
- 現有資料缺少作用機轉與香港仿單的警語及禁忌資訊，無法進入安全性篩選。

**若要推進需要：**
- 補齊 DrugBank 的作用機轉資料
- 下載並解析香港衛生署的仿單，取得警語、禁忌與核准適應症
- 針對利尿劑與眼壓的關係進行文獻回顧或前臨床研究
- 將探索重點轉向有間接線索的慢性肺心病，並檢視其近期文獻與對照研究
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

