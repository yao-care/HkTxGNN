---
layout: default
title: Prasterone
parent: 僅模型預測 (L5)
nav_order: 723
evidence_level: L5
indication_count: 10
monitor_inn: "PRASTERONE"
predicted_indications: ["heparin cofactor 2 deficiency", "factor 5 excess with spontaneous thrombosis", "antithrombin deficiency type 2", "thrombophilia", "severe nonproliferative diabetic retinopathy", "thrombophilia due to protein S deficiency, autosomal recessive", "scleroderma (disease)", "complement component 4a deficiency", "pseudo-von Willebrand disease", "primary release disorder of platelets"]
last_modified_at: 2026-10-28
description: "Prasterone：預測新適應症為肝素輔因子 2 缺乏症 (Heparin Cofactor 2 Deficiency)（證據等級 L5）。原適應症：香港許可證未載明核准適應症文字"
---

# Prasterone
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

## Prasterone：從知識圖譜記錄的紅斑性狼瘡與心因性性交疼痛，到肝素輔因子 2 缺乏症
{: .text-alpha }

## 一句話總結

Prasterone（DHEA，脫氫表雄固酮）在知識圖譜中記錄的相關用途包括系統性紅斑性狼瘡、兒童系統性紅斑性狼瘡與心因性性交疼痛。
TxGNN 模型預測它可能對**肝素輔因子 2 缺乏症 (Heparin Cofactor 2 Deficiency)** 有效。
目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證未載明核准適應症文字；知識圖譜記錄的關聯為系統性紅斑性狼瘡、兒童系統性紅斑性狼瘡、心因性性交疼痛（僅為知識圖譜關聯，非核准適應症） |
| 預測新適應症 | 肝素輔因子 2 缺乏症 (Heparin Cofactor 2 Deficiency) |
| TxGNN 預測分數 | 0.9999 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 1 張／共 1 張） |
| 核准許可證數 | 1 張（有效 1 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Prasterone 是 DHEA，屬雄性素與雌性素的前驅物。藥理資料顯示它與甘胺酸受體 (Glycine Receptor) 有關聯，但這與凝血機轉並無直接連結。

肝素輔因子 2 缺乏症是一種絲胺酸蛋白酶抑制劑 (serpin) 缺乏的凝血疾病。有報告指 DHEA 可能影響凝血與纖維蛋白溶解，但這屬推測，無法說明對此遺傳性缺乏症有治療作用。

這項預測來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，並非生物學證據，目前尚無機轉或臨床證據支持。

**其他預測適應症（皆為 L5，僅模型預測）：**

| 排名 | 疾病 | TxGNN 分數 | 建議 |
|------|------|-----------|------|
| 2 | 第五因子過多伴自發性血栓 | 0.9998 | Hold |
| 3 | 第 2 型抗凝血酶缺乏症 | 0.9998 | Hold |
| 4 | 血栓形成傾向 | 0.9991 | Hold |
| 5 | 重度非增殖性糖尿病視網膜病變 | 0.9925 | Hold |
| 6 | 蛋白 S 缺乏所致血栓形成傾向（體染色體隱性） | 0.9913 | Hold |
| 7 | 硬皮症 | 0.9911 | 列為研究問題 |
| 8 | 補體 C4A 缺乏症 | 0.9905 | Hold |
| 9 | 類血管性血友病 | 0.9901 | Hold |
| 10 | 血小板原發性釋放障礙 | 0.9901 | Hold |

其中硬皮症與知識圖譜中記錄的紅斑性狼瘡同屬自體免疫結締組織疾病，在生物學上相對連貫，可列為後續文獻與前臨床探索的研究問題。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66651 | INTRAROSA PESSARIES 6.5MG | 未載明 | 未載明 |

此為單一成分製劑，狀態為有效。

## 安全性考量

- **藥物交互作用／藥理交互**：藥理資料顯示，DHEA 作用於甘胺酸受體（所有亞型）。此為藥理標靶關聯，並無分級的臨床交互作用。
- **血栓風險提醒**：多項預測適應症屬凝血或血栓疾病。性類固醇對凝血的影響方向不明，可能增加血栓風險，推進前應先釐清安全性。

其餘安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究肝素輔因子 2 缺乏症，證據等級為 L5，僅有模型預測。
- 作用機轉資料缺乏，且 DHEA 對凝血的影響方向不明，存在潛在安全疑慮。

**若要推進需要：**
- 補充 DrugBank 的作用機轉資料。
- 取得香港衛生署仿單的警語與禁忌症。
- 進行系統性文獻檢索，確認 DHEA 與肝素輔因子 2 及凝血功能的關聯。
- 以前臨床研究驗證機轉，並先評估血栓安全性。
- 可優先針對硬皮症等自體免疫相關預測，另行評估探索價值。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

