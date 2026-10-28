---
layout: default
title: Loperamide
parent: 僅模型預測 (L5)
nav_order: 537
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "Loperamide"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "serous conjunctivitis except viral", "parasitic conjunctivitis", "chronic follicular conjunctivitis", "conjunctival folliculosis", "Angelucci syndrome"]
description: "Loperamide：預測新適應症為急性傳染性結膜炎 (acute contagious conjunctivitis)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Loperamide
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

## Loperamide: 急性傳染性結膜炎 (acute contagious conjunctivitis)
{: .text-alpha }

## 一句話總結

Loperamide 是periphery 型的鴉片類受體促效劑，原本用於腹瀉與痢疾的症狀控制。
TxGNN 模型預測它可能對**急性傳染性結膜炎 (Acute Contagious Conjunctivitis)** 有效，但目前**沒有任何臨床試驗，也沒有相關文獻**支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 急性傳染性結膜炎 (acute contagious conjunctivitis) |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證至少 20 張） |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就已知的藥理特性，Loperamide 是作用於腸道肌間神經叢的周邊 μ-鴉片受體促效劑，可降低腸道蠕動，用於控制腹瀉症狀。

從機轉上看，**找不到合理的關聯**。Loperamide 沒有抗菌、抗病毒或抗發炎活性，無法處理感染性結膜炎的病因。高分預測來自 TxGNN 模型（深度學習），較可能反映模型從相近疾病（各類結膜炎）之間學到的相似性，而非生物學上的依據。

### 其他預測適應症概覽

排名前 10 的預測中，絕大多數為各種結膜炎亞型（偽膜性、寄生蟲性、慢性濾泡性等）及 Angelucci 症候群，皆無試驗或文獻，也無機轉依據。以下兩項有少量文獻，但都是安全性警訊，而非療效證據：

- **阿米巴痢疾 (Amebic dysentery)**（分數 0.9995，L4）：Loperamide 沒有殺阿米巴作用，減慢腸道傳輸反而可能使侵襲性阿米巴結腸炎惡化。文獻有 1 篇報告指出使用 Loperamide 後發生猛爆性阿米巴結腸炎。
- **胃十二指腸炎 (Gastroduodenitis)**（分數 0.9977，L4）：Loperamide 只能緩解伴隨的腹瀉，無法治療發炎本身。2026 年有 1 篇病例報告指出，在化療引起的嚴重腸胃道發炎下使用 Loperamide 導致呼吸抑制。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首要預測（急性傳染性結膜炎），目前無相關文獻。

---

## 香港上市資訊

下表列出 5 張主要許可證（共 20 張，皆為有效的單一成分製劑）：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49270 | LOPERA TAB 2MG | 錠劑（2 mg） | — |
| HK-50444 | LOPAINE CAP 2MG | 膠囊（2 mg） | — |
| HK-18541 | LIDERIUM CAP 2MG | 膠囊（2 mg） | — |
| HK-47710 | KOJAR-LOPETIN CAP 2MG | 膠囊（2 mg） | — |
| HK-48842 | DIACURE SYRUP 2MG/5ML | 糖漿（2 mg/5 mL） | — |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：肝病、膽囊疾病、麻痺性腸阻塞、腸阻塞、家族性內臟肌病變、痢疾、腹瀉性疾病、感染性腹瀉、腸道感染性疾病。（來源為知識圖譜的藥物—疾病禁忌關聯，並非仿單原文。）
- **藥物交互作用**：資料庫共有 100 筆記錄，其中重大 (Major) 等級包括 Abiraterone、Ranitidine、Fosamprenavir、Gemfibrozil；中度 (Moderate) 等級包括 Codeine、Dihydrocodeine、Tramadol（其他鴉片類）、Chlorpheniramine、Cetirizine（抗組織胺）、乙醇等。
- **文獻中的安全警訊**：
  - 侵襲性腸道感染（如阿米巴結腸炎）使用後可能引發猛爆性結腸炎或毒性巨結腸。
  - 嚴重腸胃道發炎、腸黏膜屏障受損時，全身暴露量增加，曾有呼吸抑制的病例報告。

香港仿單的警語與禁忌資料尚未取得，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首要預測（急性傳染性結膜炎）僅有 TxGNN 模型（深度學習）的分數，沒有試驗、文獻與機轉依據，證據等級為 L5，分數很可能反映模型從相近疾病之間學到的相似性，而非生物學證據。
- 排名較前的其他預測中，具文獻的項目反映的是安全風險而非療效，不支持再利用。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症資料
- 補齊 Loperamide 作用機轉資料，並重新評估任何眼部作用的生物學合理性
- 若仍要探討，需先有前臨床或機轉研究，說明為何 Loperamide 可能對眼表感染或發炎有作用
- 評估給藥途徑的可行性（目前許可證皆為口服劑型，不適用於眼部給藥）
- 在無新證據前，建議不要投入資源於此預測
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

