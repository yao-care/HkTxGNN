---
layout: default
title: Sodium Acetate
parent: 僅模型預測 (L5)
nav_order: 818
evidence_level: L5
indication_count: 10
monitor_inn: "SODIUM ACETATE"
predicted_indications: ["congenital prothrombin deficiency", "epiglottitis", "urinary tract infection (disease)", "sclerosing cholangitis", "gonococcal urethritis", "Ureaplasma urethritis", "dyspepsia", "uterine inflammatory disease", "gastroparesis (disease)", "xanthogranulomatous pyelonephritis"]
last_modified_at: 2026-10-28
description: "Sodium Acetate：預測新適應症為先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)（證據等級 L5）。原適應症：資料中未載明"
---

# Sodium Acetate
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

## Sodium Acetate（醋酸鈉）：從電解質補充到先天性凝血酶原缺乏症
{: .text-alpha }

## 一句話總結

醋酸鈉是一種電解質與鹼化劑，在香港主要以靜脈輸液、腹膜透析液等複方電解質製劑的成分形式上市。
TxGNN 模型預測它可能對**先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency)** 有效，
但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅屬模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料中未載明（許可證的核准適應症欄位皆為空白） |
| 預測新適應症 | 先天性凝血酶原缺乏症 (Congenital Prothrombin Deficiency) |
| TxGNN 預測分數 | 0.9998 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 至少 20 張（清單可能不完整） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，醋酸鈉是電解質／鹼化劑與鈉的來源，在體內代謝後可產生碳酸氫鹽，用於電解質與酸鹼平衡的調節。

先天性凝血酶原缺乏症是凝血因子 II 的合成或功能缺陷。醋酸鈉與凝血因子 II 的合成或替代之間，目前找不到合理的機轉關聯。
這個高分來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據。

其他排名靠前的預測（如會厭炎、泌尿道感染、淋病性尿道炎、硬化性膽管炎等）同樣缺乏機轉與臨床證據支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

（排名較後的預測，如消化不良與胃輕癱，雖有部分文獻，但內容僅涉及以 13C 標記醋酸鹽做胃排空呼氣檢測，屬診斷用途，並非醋酸鈉的治療效果，與本預測疾病無關。）

## 香港上市資訊

資料中顯示的許可證皆為單一成分登記，但核准適應症欄位均為空白。以下列出 5 張主要許可證（總數至少 20 張，清單可能不完整）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-41852 | LACTATED RINGER'S INJ | 未載明 | 未載明 |
| HK-54146 | LACTATED RINGER'S INJ | 未載明 | 未載明 |
| HK-28245 | COMPOUND SODIUM LACTATE INJ (HARTMANN'S) | 未載明 | 未載明 |
| HK-58675 | WIDA RL RINGER LACTATE INTRAVENOUS INFUSION | 未載明 | 未載明 |
| HK-62680 | DIANEAL PD-2 PERITONEAL DIALYSIS SOLUTION WITH 1.5% DEXTROSE (ULTRA BAG) | 未載明 | 未載明 |

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（非仿單內容）：腎臟疾病、慢性腎衰竭、末期腎衰竭、無尿、高鈣血症、腎鈣質沉著症、腎結石、心臟病、心血管疾病、房室傳導阻滯、心室顫動、洋地黃中毒、高血鉀性週期性麻痺、低醛固酮症、肌強直症、苯丙酮尿症等。
- **藥物交互作用**：共查得 30 筆，以下為主要項目。
  - 中度：Doxycycline、Tetracycline、Minocycline、Acetylsalicylic acid（阿斯匹靈）、Ephedrine、Pseudoephedrine、Amphetamine、Dextroamphetamine、Methenamine
  - 輕度：Glipizide、Glyburide、Tolbutamide、Chlorpropamide、Memantine、Methotrexate

香港仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測缺乏任何機轉依據與臨床、文獻證據，且無研究直接探討該疾病，證據等級為 L5。
- 高分來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，而非生物學證據，不建議投入資源。

**若要推進需要：**
- 提出醋酸鈉與凝血酶原（因子 II）合成或功能之間的合理機轉假說，並進行前臨床驗證
- 補充 DrugBank 作用機轉資料
- 取得香港仿單的警語與禁忌資料，以進行安全性篩選
- 釐清各許可證的核准適應症與劑型
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

