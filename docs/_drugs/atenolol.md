---
layout: default
title: Atenolol
parent: 中證據等級 (L3-L4)
nav_order: 78
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-14
description: "Atenolol：預測新適應症為後下壁心肌梗塞 (Posteroinferior Myocardial Infarction)（證據等級 L4）。原適應症：高血壓、心肌梗塞"
monitor_inn: "ATENOLOL"
predicted_indications: ["malignant hypertensive renal disease", "chronic pulmonary heart disease"]
---

# Atenolol
{: .fs-9 }

證據等級: **L4** | 預測適應症: **9** 個
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

# Atenolol：從高血壓與心肌梗塞到後下壁心肌梗塞

## 一句話總結

Atenolol 是一種 β1 選擇性乙型阻斷劑，原本用於高血壓與心肌梗塞等心血管疾病。
TxGNN 模型預測它可能對**後下壁心肌梗塞 (Posteroinferior Myocardial Infarction)** 有效，
但目前**沒有臨床試驗**，僅有 **1 篇文獻**（1985 年的交叉試驗），且此預測本質上是已核准適應症（心肌梗塞）的解剖位置亞型，並非真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、心肌梗塞（來自知識圖譜；香港許可證未登載適應症文字） |
| 預測新適應症 | 後下壁心肌梗塞 (Posteroinferior Myocardial Infarction) |
| TxGNN 預測分數 | 99.87% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，atenolol 屬於心臟選擇性 β1 阻斷劑，其在高血壓與心肌梗塞中的療效已被廣泛使用。β1 阻斷可降低心肌耗氧量、心跳速率與心律不整風險。

後下壁心肌梗塞只是心肌梗塞依梗塞位置劃分的亞型。TxGNN 的高分很可能反映本體論中與上位疾病「心肌梗塞」的關聯，因此這**不是真正的藥物再利用候選**。任何潛在益處都是從心肌梗塞後使用 β 阻斷劑的一般原理推論而來。

其他預測項目（如後側壁心肌梗塞、間隔心肌梗塞、惡性腎血管性高血壓）多屬同類的上位疾病亞型；肺高壓相關預測則證據薄弱且互有矛盾，β 阻斷劑在肺高壓中一般不被推薦。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | 交叉單盲隨機試驗 | La Revue de médecine interne | 比較 atenolol 200 mg 與 diltiazem 240 mg 在 23 位心肌梗塞（後下壁或前壁）後 4 週患者的抗缺血活性，採運動測試評估；對此特定梗塞位置僅為間接證據 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-17873 | TENORMIN TAB 50MG | 錠劑 | 未登載 |
| HK-06812 | TENORMIN TAB 100MG | 錠劑 | 未登載 |
| HK-34859 | NOTEN TAB 50MG | 錠劑 | 未登載 |
| HK-45490 | NORMATEN TAB 50MG | 錠劑 | 未登載 |
| HK-44133 | ATENOLOL TAB 50MG | 錠劑 | 未登載 |

共 20 張有效單一成分許可證，上表僅列出 5 張主要許可證。

---

## 安全性考量

- **知識圖譜標示的相對禁忌疾病**（非仿單原文）：氣喘（含內因性、過敏性）、房室傳導阻滯、雷諾氏病、第 1 型與第 2 型糖尿病及糖尿病酮酸中毒、肝衰竭、胰臟炎、全身性紅斑狼瘡、乾癬、痛風、無尿、過敏性休克、低鉀、高鈣及磷代謝異常等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - 中度：Epinephrine、Hydrocortisone、Hyoscyamine、Bupropion、Triamcinolone、Morphine、Atropine、Betamethasone、Budesonide、多種鈣鹽
  - 輕度：Acetylsalicylic acid、Aluminum hydroxide、Attapulgite

香港仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測的適應症是已核准適應症（心肌梗塞）的位置亞型，不構成真正的再利用機會，且僅有一篇間接的 1985 年小型交叉研究，無任何臨床試驗。
- 其他預測（肺高壓等）證據薄弱或相互矛盾，且 β 阻斷劑在這些情境有潛在風險。

**若要推進需要：**
- 確認香港核准的適應症文字，釐清心肌梗塞是否已涵蓋在現有標示內（若是，則無需另行申請）
- 取得詳細的作用機轉資料
- 取得香港仿單的警語與禁忌症資料
- 如仍要探討新用途，需針對特定梗塞位置或肺部相關疾病設計直接的臨床證據
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

