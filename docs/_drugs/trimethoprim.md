---
layout: default
title: Trimethoprim
parent: 僅模型預測 (L5)
nav_order: 910
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Trimethoprim：預測新適應症為點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)（證據等級 L5）。原適應症：尿路感染、感染性中耳炎、肺囊蟲肺炎、志賀氏菌症、結膜炎等"
---

# Trimethoprim
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Trimethoprim：從尿路感染到點狀上皮角膜結膜炎

## 一句話總結

Trimethoprim 是一種抗菌藥物，原本用於尿路感染、中耳炎、肺囊蟲肺炎、志賀氏菌症及結膜炎等感染性疾病。
TxGNN 模型預測它可能對**點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 有效，但目前**沒有任何臨床試驗和文獻**直接支持這個預測，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 尿路感染、感染性中耳炎、肺囊蟲肺炎、志賀氏菌症、結膜炎等（香港許可證未提供適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis) |
| TxGNN 預測分數 | 99.57% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 13 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般已知 Trimethoprim 抑制細菌的二氫葉酸還原酶，阻斷葉酸合成，因而對常見細菌具抗菌活性。

模型給分很高，可能是因為它在知識圖譜中與結膜炎、瞼緣結膜炎等眼部感染適應症距離相近。但點狀上皮角膜結膜炎常由病毒（如腺病毒）或非感染性原因引起，抗菌機轉未必能處理其根本病因。因此這個高分更可能反映網絡鄰近性，而非真正的機轉關聯。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

針對預測的新適應症（點狀上皮角膜結膜炎），目前無相關文獻。

與其相鄰的「結膜炎」已是原適應症之一，該方向的文獻較多，但不能視為對新適應症的支持，因此不列於此。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-56426 | TRIMETHOPRIM SUSP 50MG/5ML | 未提供 | 未提供 |
| HK-43066 | CO-SEPTIC TAB | 未提供 | 未提供 |
| HK-21598 | TRIMETRIN CAP | 未提供 | 未提供 |
| HK-09295 | APO-SULFATRIM 400-80MG TAB | 未提供 | 未提供 |
| HK-65292 | DBL SULFAMETHOXAZOLE AND TRIMETHOPRIM CONCENTRATE FOR SOLUTION FOR INFUSION 400MG/80MG | 未提供 | 未提供 |

目前共有 13 張有效許可證（皆為單一成分登記），此處僅列出 5 張。

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自知識圖譜關聯，非仿單文字）：紫質症（含遺傳性紫質症）、腎臟疾病、肝臟疾病、膽囊疾病、血小板低下、嗜中性白血球低下、顆粒球缺乏症、困難梭狀芽孢桿菌結腸炎、新生兒壞死性腸炎、G6PD 缺乏症、肝醣儲積症、胱胺酸尿症、半乳糖血症、葉酸缺乏性貧血。
- **藥物交互作用**：資料庫查得 100 筆交互作用。其中屬於**嚴重 (Major)** 的包括：
  - 檸檬酸鉀 (Potassium citrate)
  - 碳酸氫鉀 (Potassium bicarbonate)
  - 氯化鉀 (Potassium chloride)
  - 葡萄糖酸鉀 (Potassium gluconate)

  中度 (Moderate) 的包括 Metformin、Pioglitazone、Rosiglitazone、Repaglinide、Balsalazide、Picosulfuric acid、Sapropterin 等。鉀製劑與 Trimethoprim 併用需特別留意高血鉀風險。

仿單的警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測分數雖高（99.57%），但僅來自模型推論，沒有任何臨床試驗或文獻支持。
- 抗菌機轉與非細菌性的點狀上皮角膜結膜炎之間缺乏合理連結。

**若要推進需要：**
- 取得詳細的作用機轉資料，並釐清其與該疾病病因（病毒性或非感染性）的關聯
- 文獻回顧或前臨床研究，確認是否有針對此適應症的證據
- 下載並解析香港衛生署的仿單，補齊警語、禁忌症與核准適應症
- 確認可用的眼用劑型與給藥途徑
- 若考慮眼部感染方向，另行評估「結膜炎」；該適應症已屬原適應症，並非真正的再利用
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

