---
layout: default
title: Ravulizumab
parent: 僅模型預測 (L5)
nav_order: 761
evidence_level: L5
indication_count: 10
monitor_inn: "RAVULIZUMAB"
predicted_indications: ["autosomal recessive severe congenital neutropenia due to G6PC3 deficiency", "cyclic hematopoiesis", "primary hyperoxaluria", "severe congenital neutropenia", "autosomal recessive severe congenital neutropenia due to CXCR2 deficiency", "primary immunodeficiency syndrome due to p14 deficiency", "pseudo-von Willebrand disease", "X-linked severe congenital neutropenia", "primary release disorder of platelets", "megaloblastic anemia (disease)"]
last_modified_at: 2026-10-28
description: "Ravulizumab：預測新適應症為 G6PC3 缺陷所致體染色體隱性嚴重先天性嗜中性白血球減少症（證據等級 L5）。原適應症：陣發性夜間血紅素尿症"
---

# Ravulizumab
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

## Ravulizumab：從陣發性夜間血紅素尿症到 G6PC3 缺陷所致體染色體隱性嚴重先天性嗜中性白血球減少症
{: .text-alpha }

## 一句話總結

Ravulizumab 是一種補體 C5 抑制劑，知識圖譜中記錄其與陣發性夜間血紅素尿症 (paroxysmal nocturnal hemoglobinuria) 有關。
TxGNN 模型預測它可能對**伴 G6PC3 缺乏的常染色體隱性嚴重先天性嗜中性球低下症**有效，但目前**沒有任何臨床試驗或文獻**支持這個預測，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 陣發性夜間血紅素尿症（知識圖譜中記錄的關聯；香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 伴 G6PC3 缺乏的常染色體隱性嚴重先天性嗜中性球低下症 |
| TxGNN 預測分數 | 0.9996 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，ravulizumab 是補體 C5 抑制劑，在陣發性夜間血紅素尿症（補體介導的血管內溶血）相關的關聯已記錄於知識圖譜中。

然而，G6PC3 缺乏所致的嗜中性球低下症，成因是嗜中性球葡萄糖代謝受損及細胞凋亡增加，並非補體驅動的疾病。目前沒有已知的機轉，說明阻斷 C5 能改善這個疾病。

因此，0.9996 的高分來自 TxGNN 模型（深度學習），可能反映模型學到的相關疾病之間的相似性，並非生物學證據，也沒有臨床資料佐證。其他排名靠前的預測（如週期性造血異常、原發性高草酸尿症、其他先天性嗜中性白血球減少症等）同樣沒有試驗或文獻支持。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-67383 | ULTOMIRIS CONCENTRATE FOR SOLUTION FOR INFUSION 300MG/3ML | 未載明 | 未載明 |
| HK-67382 | ULTOMIRIS CONCENTRATE FOR SOLUTION FOR INFUSION 1100MG/11ML | 未載明 | 未載明 |

兩張許可證皆為單一成分製劑，持有者為 AstraZeneca Hong Kong Limited，狀態有效。

## 安全性考量

- **知識圖譜記錄的禁忌關聯**：脑膜炎球菌感染 (meningococcal infection)。此為知識圖譜的關聯，並非仿單文字。補體 C5 抑制劑已知會增加奈瑟氏菌感染風險，使用前需特別留意。
- **藥物交互作用**：共查詢到 4 項，皆為輕微 (Minor) 等級，涉及人類免疫球蛋白 G（靜脈注射、皮下注射、肌肉注射、靜脈加皮下注射）。

其他警語與禁忌資料請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 此預測僅來自模型分數，沒有臨床試驗或文獻，且疾病機轉（嗜中性球代謝與凋亡缺陷）與補體 C5 抑制無明確關聯，證據等級為 L5。
- 此外，補體抑制可能增加嚴重感染風險，而嗜中性球低下症患者本身就易感染，風險效益比不利。

**若要推進需要：**
- 補充 ravulizumab 的作用機轉資料
- 取得香港仿單的警語、禁忌與核准適應症文字
- 建立 C5 補體活化與 G6PC3 缺乏嗜中性球低下症之間的前臨床或機轉證據
- 若有機轉支持，再評估感染風險（特別是腦膜炎球菌）及疫苗接種與預防策略
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

