---
layout: default
title: Ergocalciferol
parent: 僅模型預測 (L5)
nav_order: 333
evidence_level: L5
indication_count: 6
monitor_inn: "ERGOCALCIFEROL"
predicted_indications: ["acromesomelic dysplasia, Campailla Martinelli type", "renal tubular acidosis", "craniofacial conodysplasia", "hypophosphatemia (disease)", "renal osteodystrophy", "calcium-alkali syndrome"]
last_modified_at: 2026-10-28
description: "Ergocalciferol：預測新適應症為肢中發育不良，Campailla Martinelli 型（證據等級 L5）。原適應症：香港許可證資料未提供適應症文字。知識圖譜記錄的關聯包括骨質疏鬆、佝僂病、骨軟化症、維生素 D 缺乏、副甲狀腺低下"
---

# Ergocalciferol
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

## 麥角鈣化醇（Ergocalciferol）：從維生素 D 缺乏相關疾病到 Campailla-Martinelli 型肢中段發育不良
{: .text-alpha }

## 一句話總結

麥角鈣化醇（維生素 D2）在知識圖譜中與骨質疏鬆、佝僂病、骨軟化症、維生素 D 缺乏等疾病有關聯記錄。
TxGNN 模型預測它可能對**肢中發育不良，Campailla Martinelli 型 (Acromesomelic dysplasia, Campailla Martinelli type)** 有效。
目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未提供適應症文字。知識圖譜記錄的關聯包括骨質疏鬆、佝僂病、骨軟化症、維生素 D 缺乏、副甲狀腺低下（此為知識圖譜關聯，非核准適應症） |
| 預測新適應症 | 肢中發育不良，Campailla Martinelli 型 |
| TxGNN 預測分數 | 0.9983 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 4 張／共 4 張） |
| 許可證數 | 4 張（有效 4 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般而言，麥角鈣化醇是維生素 D 補充劑，在體內轉化為活性形式後，參與鈣、磷代謝與骨骼礦化。TxGNN 模型（深度學習）給出的分數可能反映模型從相關疾病間學到的相似性，並非生物學證據。

但肢中發育不良（Campailla Martinelli 型）是罕見的遺傳性骨骼發育異常，並非維生素 D 缺乏所致。目前沒有找到可支持維生素 D2 補充有療效的機轉連結。這個高分更可能反映模型在骨骼疾病網絡中的相似性，而不是實際的治療潛力。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-36205 | VITALIPID N INFANT INJ | FRESENIUS KABI HONG KONG LIMITED |
| HK-36206 | VITALIPID N ADULT INJ | FRESENIUS KABI HONG KONG LIMITED |
| HK-01178 | POLIBABY CREAM | SATO PHARMACEUTICAL (HK) CO LTD |
| HK-52479 | AMINOLEBAN EN POWDER | OTSUKA PHARMACEUTICAL (H.K.) LIMITED |

以上 4 張許可證目前皆為有效狀態，許可證資料中沒有提供核准適應症文字。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單文字）：高血鈣、腎鈣化症、磷代謝異常、高血壓、腎臟疾病、肝臟疾病、膽囊疾病、副甲狀腺功能亢進、類肉瘤病（sarcoidosis）、糖尿病、心房顫動、原發性高草酸尿症、血色素沉著症、威爾森氏症、高血脂、攝護腺癌、乳癌等。
- **藥物交互作用**：共查得 55 筆。
  - **重大**：其他維生素 D 類藥物，包括 Cholecalciferol、Calcifediol、Calcitriol、Doxercalciferol，合併使用有高血鈣風險。
  - **中度**：thiazide 類利尿劑（Hydrochlorothiazide、Chlorothiazide、Chlorthalidone）、膽酸結合劑（Cholestyramine、Colestipol、Colesevelam）、Carbamazepine、巴比妥類、Digoxin、Rifabutin、Sevelamer、氧化鎂等。
  - **輕微**：Cimetidine。

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測疾病為罕見遺傳性骨骼發育不良，沒有任何臨床試驗或文獻，也找不到合理的機轉連結，證據等級僅為 L5。
- 高分很可能只是模型預測的結果，不足以支持推進。

**若要推進需要：**
- 補充麥角鈣化醇的作用機轉資料，並釐清與此疾病致病機轉（遺傳性骨骼生長異常）的關係。
- 取得任何針對此疾病的前臨床或臨床證據。
- 取得香港仿單的警語與禁忌資料，完成安全性篩選。

**備註：**同一份預測清單中，「腎性骨病變 (renal osteodystrophy)」有 1 個 Phase 4 試驗和多篇文獻，證據明顯較多（L3），可作為後續優先評估的方向。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

