---
layout: default
title: Fluorometholone
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 9
monitor_inn: "FLUOROMETHOLONE"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome", "punctate epithelial keratoconjunctivitis", "infection-related hemolytic uremic syndrome", "Chagas cardiomyopathy", "glaucomatocyclitic crisis"]
last_modified_at: 2026-10-28
description: "Fluorometholone：預測新適應症為感染後血管炎 (Postinfectious Vasculitis)（證據等級 L5）。原適應症：知識圖譜中記錄的關聯：葡萄膜炎、虹彩炎、睫狀體疾病、全葡萄膜炎、異位性／乳突性／春季結膜炎、角膜潰瘍等"
---

# Fluorometholone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

## Fluorometholone：從眼部發炎性疾病到感染後血管炎（預測新適應症）
{: .text-alpha }

## 一句話總結

Fluorometholone 是局部眼用皮質類固醇，知識圖譜中記錄的使用範圍為葡萄膜炎、虹彩炎、過敏性結膜炎等眼部發炎性疾病。
TxGNN 模型預測它可能對**感染後血管炎 (Postinfectious Vasculitis)** 有效，但目前**沒有任何臨床試驗或文獻**直接支持這個方向，僅有模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜中記錄的關聯：葡萄膜炎、虹彩炎、睫狀體疾病、全葡萄膜炎、異位性／乳突性／春季結膜炎、角膜潰瘍等（香港許可證未附適應症文字，無法確認核准範圍） |
| 預測新適應症 | 感染後血管炎 (Postinfectious Vasculitis) |
| TxGNN 預測分數 | 0.9991 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 6 張／共 6 張） |
| 許可證數 | 6 張（有效 6 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Fluorometholone 是局部眼用皮質類固醇，藥理資料顯示其作用於糖皮質素受體（NR3C1），具抗發炎與免疫抑制效果。

從機轉上看，糖皮質素理論上可以抑制免疫媒介的血管炎。但本藥僅以眼用滴劑形式上市，全身暴露量極低，要在全身性血管炎中發揮作用的可能性很小。因此這個關聯性偏弱，預測分數來自 TxGNN 模型（深度學習），可能反映模型從相關疾病之間學到的相似性，並非生物學證據，也無臨床研究佐證。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-34273 | FLUMETHOLON EYE DROPS 0.1% | 未提供 | 未提供 |
| HK-34274 | FLUMETHOLON EYE DROPS 0.02% | 未提供 | 未提供 |
| HK-54720 | TOLON EYE DROPS 0.1% | 未提供 | 未提供 |
| HK-64966 | FULUSON OPHTHALMIC SOLUTION 0.1% W/V | 未提供 | 未提供 |
| HK-19538 | FML LIQUIFILM OPHTHALMIC SUSP 0.1% | 未提供 | 未提供 |

另有 HK-45275（FLAREX OPHTHALMIC SUSP 0.1%）。6 張許可證皆為單一成分、有效狀態。

## 安全性考量

- **知識圖譜中記錄的禁忌關聯**（非仿單內容）：單純疱疹病毒角膜炎、開角型青光眼、高眼壓、眼部感染性疾病（含黴菌、病毒、眼結核）、結膜炎、糖尿病與糖尿病酮酸中毒、紫質症、G6PD 缺乏症等。
- **藥物交互作用**：共查得 12 筆，包括 Doxycycline、Salbutamol、Cyclosporine、Acetaminophen、Digoxin、Brimonidine、Cephalexin、Alendronic acid、Acyclovir、Diazepam、Fenofibrate，嚴重度分級皆為未知。另有糖皮質素受體的藥理標靶紀錄。

仿單的警語與禁忌資料未取得，詳細安全性資訊請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 沒有任何臨床試驗或文獻直接研究此疾病，證據等級為 L5。
- 局部眼用劑型全身暴露極低，用於全身性血管炎在機轉上缺乏說服力。

**若要推進需要：**
- 取得香港仿單的警語、禁忌與核准適應症文字
- 補充作用機轉資料
- 評估是否有適合的給藥途徑（目前僅有眼用劑型）
- 找到直接針對感染後血管炎的研究證據

**附註：** 在同批預測中，**點狀上皮角膜結膜炎 (Punctate Epithelial Keratoconjunctivitis)** 在生物學上較為合理（與本藥眼表發炎的既有用途相近）。但現有 2 篇文獻僅間接討論相關疾病，並未直接測試 fluorometholone，且感染性病因使用類固醇需謹慎。可列為後續研究問題，而非目前推進對象。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

