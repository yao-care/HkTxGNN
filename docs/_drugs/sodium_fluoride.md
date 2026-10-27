---
layout: default
title: Sodium Fluoride
parent: 僅模型預測 (L5)
nav_order: 821
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Sodium Fluoride：預測新適應症為會厭炎 (Epiglottitis)（證據等級 L5）。原適應症：維生素缺乏症"
monitor_inn: "SODIUM FLUORIDE"
predicted_indications: ["epiglottitis", "urinary tract infection (disease)", "Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease"]
---

# Sodium Fluoride
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

## Sodium Fluoride：從維生素缺乏症到會厭炎
{: .text-alpha }

## 一句話總結

Sodium Fluoride（氟化鈉）在資料中的原適應症為維生素缺乏症（微量元素補充相關），目前在香港以注射用微量元素濃縮液的成分上市。
TxGNN 模型預測它可能對**會厭炎 (Epiglottitis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬於模型運算的預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 維生素缺乏症（來自知識圖譜，香港許可證未列核准適應症文字） |
| 預測新適應症 | 會厭炎 (Epiglottitis) |
| TxGNN 預測分數 | 99.92% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 3 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。氟化鈉在香港是以微量元素複方輸注液的成分上市，用於營養補充；其在原適應症上的角色與抗感染無關。

會厭炎通常由 b 型流感嗜血桿菌或其他細菌引起，標準處置為呼吸道管理與全身性抗生素。氟化鈉並無已知的抗菌角色，因此機轉上無法建立合理連結。0.9992 的高分僅是圖譜特徵推算的結果，不代表生物學上的合理性。

其他排名靠前的預測（尿路感染、Ureaplasma 尿道炎、淋球菌尿道炎、子宮發炎性疾病）同樣沒有試驗或文獻支持。氟化物雖有體外抗菌作用（例如抑制烯醇酶），但沒有任何臨床證據顯示全身性或口服氟化鈉對這些感染有用。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-39024 | PEDITRACE CONC FOR PARENTERAL INFUSION（Fresenius Kabi） | 未提供 | 未提供 |
| HK-65535 | NUTRYELT CONCENTRATE FOR SOLUTION FOR INFUSION（Baxter） | 未提供 | 未提供 |
| HK-64379 | ADDAVEN CONCENTRATE FOR SOLUTION FOR INFUSION（Fresenius Kabi） | 未提供 | 未提供 |

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自圖譜關聯，非仿單內容）：腎臟疾病、腎鈣質沉著症、腎結石（含 SLC26A1 相關易感性）、急性尿酸腎病變、膿輸尿管、結節病、副甲狀腺機能亢進、纖維性骨炎、高鈣血症、磷代謝疾病、便秘、溶骨性轉移骨病灶、氟斑牙。
- **藥物交互作用**：查詢未找到相關資料。

其他警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症都只有模型分數，沒有臨床試驗、文獻或可辨識的機轉連結，證據等級為 L5。
- 會厭炎與其他感染類預測皆已有有效的標準抗生素治療，氟化鈉缺乏合理的使用理由，且知識圖譜顯示多項腎臟與代謝方面的禁忌。

**若要推進需要：**
- 補齊氟化鈉的作用機轉資料（MOA）。
- 取得香港衛生署仿單的警語與禁忌內容，完成安全性篩選。
- 進行系統性文獻回顧與前臨床研究，確認氟化物對相關病原體是否有臨床可用的活性。
- 評估給藥途徑與可達到的組織濃度是否可行。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

