---
layout: default
title: Serine
parent: 僅模型預測 (L5)
nav_order: 808
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Serine：預測新適應症為家族性內臟肌病 (Familial Visceral Myopathy)（證據等級 L5）。原適應症：開角型青光眼、肺結核"
monitor_inn: "SERINE"
predicted_indications: ["familial visceral myopathy", "intestinal obstruction", "unclassified intestinal pseudoobstruction", "myopathic intestinal pseudoobstruction", "neuronal intestinal dysplasia, type B"]
---

# Serine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Serine：從青光眼與肺結核到家族性內臟肌病

## 一句話總結

Serine（絲胺酸）是一種胺基酸，在知識圖譜中的原適應症為開角型青光眼與肺結核，同時也是多種香港上市靜脈營養輸液的成分。
TxGNN 模型預測它可能對**家族性內臟肌病 (Familial Visceral Myopathy)** 有效，但目前**沒有任何臨床試驗與相關文獻**支持，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 開角型青光眼、肺結核（來自知識圖譜；香港許可證未載明核准適應症文字） |
| 預測新適應症 | 家族性內臟肌病 (Familial Visceral Myopathy) |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Serine 是一種胺基酸，在香港主要作為複方胺基酸輸液與全靜脈營養製劑的成分上市。現有資料無法說明它如何影響內臟平滑肌的病理。

家族性內臟肌病通常與 ACTG2 等基因有關，目前沒有證據顯示補充或調節 serine 能改善這類病變。TxGNN 的高分反映的是知識圖譜中的網路鄰近性，並非已證實的療效，任何機轉連結都只是推測。

其他排名較前的預測也屬同一類型：腸阻塞 (Intestinal Obstruction)、未分類腸假性阻塞、肌病性腸假性阻塞、神經元腸道發育不良 B 型。這些預測同樣缺乏試驗與文獻支持，且都集中在腸道動力異常的疾病群。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首要預測（家族性內臟肌病）目前無相關文獻。

附帶說明：排名第 2 的預測「腸阻塞」檢索到 17 篇文獻，但內容多為關鍵字誤配，例如 Peutz-Jeghers 症候群、與 serine 蛋白酶或 serine/threonine 激酶有關的研究、腎臟纖維化與結腸炎的動物實驗等。這些都不是以 serine 胺基酸治療腸阻塞的證據，因此不納入本報告的證據評估。

---

## 香港上市資訊

香港共有 20 張有效單一成分許可證，以下列出 5 張主要許可證（資料未提供劑型與核准適應症文字）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-58387 | AMINOLEBAN 8% AMINO ACID INJ（Otsuka） | 注射劑 | 未提供 |
| HK-46283 | AMINOLEBAN INJ（Otsuka） | 注射劑 | 未提供 |
| HK-67075 | AMINOVEN INFANT SOLUTION FOR INFUSION 10% W/V（Fresenius Kabi） | 輸注液 | 未提供 |
| HK-36470 | VAMINOLACT I.V. SOLUTION（Fresenius Kabi） | 靜脈輸注液 | 未提供 |
| HK-32746 | AMINOPLASMAL HEPA-10% INJ（B. Braun） | 注射劑 | 未提供 |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病（非仿單內容）**：包括癲癇、焦慮與精神疾病、腎臟疾病（含慢性腎衰竭、腎結石）、糖尿病與糖尿病酮酸中毒、高鈣血症、心臟與心血管疾病、維生素 B12 缺乏、巨母細胞性貧血等。這些來自圖譜的藥物－疾病關聯，需對照實際仿單確認。

仿單的警語、禁忌症與藥物交互作用資料目前缺漏，安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測只來自模型分數，沒有臨床試驗，也沒有支持性文獻，證據等級為 L5。
- 作用機轉與仿單安全性資料皆缺漏，無法建立 serine 與內臟肌病的機轉連結。

**若要推進需要：**
- 補齊 serine 的作用機轉資料（如 DrugBank）。
- 取得香港衛生署仿單中的警語與禁忌症，完成安全性篩選。
- 進行系統性文獻檢索，確認是否有 serine 代謝與內臟平滑肌或腸道動力障礙相關的前臨床證據。
- 評估給藥途徑的可行性（目前香港產品皆為輸注類製劑）。
- 釐清原適應症（青光眼、肺結核）與現有營養輸液用途之間的差異。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

