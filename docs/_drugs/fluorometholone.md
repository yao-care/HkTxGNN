---
layout: default
title: Fluorometholone
parent: 僅模型預測 (L5)
nav_order: 389
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Fluorometholone：預測新適應症為感染後血管炎 (Postinfectious Vasculitis)（證據等級 L5）。原適應症：葡萄膜炎、虹膜疾病、過敏性結膜炎、春季角結膜炎、角膜潰瘍等"
monitor_inn: "FLUOROMETHOLONE"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "infective urethral stricture", "post-infectious syndrome"]
---

# Fluorometholone
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

# Fluorometholone：從葡萄膜炎等眼部發炎疾病到感染後血管炎

## 一句話總結

Fluorometholone 是一種外用眼科皮質類固醇，原本用於葡萄膜炎、結膜炎、角膜潰瘍等眼部發炎性疾病。
TxGNN 模型預測它可能對**感染後血管炎 (Postinfectious Vasculitis)** 有效，
但目前**沒有任何臨床試驗或文獻**支持，僅有模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 葡萄膜炎、虹膜疾病、過敏性結膜炎、春季角結膜炎、角膜潰瘍等（依知識圖譜適應症資料；香港許可證未載明適應症文字） |
| 預測新適應症 | 感染後血管炎 (Postinfectious Vasculitis) |
| TxGNN 預測分數 | 99.91% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Fluorometholone 是糖皮質素（glucocorticoid）類的外用眼科藥物，藥理資料顯示其作用標的為糖皮質素受體（NR3C1），在眼部發炎性疾病中用於抑制發炎反應。

皮質類固醇廣泛用於免疫介導的血管炎，因此在藥物類別層次上有一定合理性。不過 Fluorometholone 是眼用劑型，全身暴露量低，要用於感染後血管炎，機轉連結仍屬推測。

此外，同批預測的其他項目（感染後疾患、外耳炎、感染性尿道狹窄、感染後症候群）也都只有模型分數支持。其中外耳炎因外用類固醇本就是耳用製劑的常見成分，機轉上相對最合理，但仍需不同劑型並考量鼓膜完整性。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-34273 | FLUMETHOLON EYE DROPS 0.1%（Santen） | 眼用滴劑 | 未載明 |
| HK-34274 | FLUMETHOLON EYE DROPS 0.02%（Santen） | 眼用滴劑 | 未載明 |
| HK-54720 | TOLON EYE DROPS 0.1%（Lafarge） | 眼用滴劑 | 未載明 |
| HK-64966 | FULUSON OPHTHALMIC SOLUTION 0.1% W/V（LSB） | 眼用溶液 | 未載明 |
| HK-19538 | FML LIQUIFILM OPHTHALMIC SUSP 0.1%（Allergan） | 眼用懸液 | 未載明 |

另有 HK-45275（FLAREX OPHTHALMIC SUSP 0.1%，Novartis），共 6 張有效單方許可證。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物－疾病關聯資料，非仿單原文）：
  - 眼部感染類：疱疹性角膜炎、病毒性眼部感染、真菌性眼部感染、眼部結核、眼部感染性疾病、結膜炎
  - 眼壓相關：開放角青光眼、高眼壓
  - 代謝相關：糖尿病、糖尿病酮酸中毒、肝醣儲積症、半乳糖血症、胱胺酸尿症
  - 其他：卟啉症（含遺傳性）、G6PD 缺乏症、角膜色素沉著
- **藥物交互作用**：共查得 12 筆紀錄，其中 11 筆為藥物間交互作用，但嚴重度分級皆為未知，例如 Doxycycline、Cyclosporine、Digoxin、Brimonidine、Acyclovir、Diazepam 等；另 1 筆為藥理標的（糖皮質素受體），並非交互作用。

仿單的警語與禁忌資料尚未取得，請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 所有預測適應症皆僅有 TxGNN 模型分數（證據等級 L5），沒有臨床試驗或文獻佐證。
- 此藥為眼用劑型，全身暴露低，用於感染後血管炎的合理性有限，且感染活動期使用類固醇可能不適當。

**若要推進需要：**
- 取得 Fluorometholone 的作用機轉資料（MOA）
- 取得香港衛生署仿單的警語與禁忌資料（目前為阻斷性資料缺口）
- 進行感染後血管炎相關的文獻與試驗檢索
- 評估是否需要全身性或其他劑型，並確認給藥途徑可行性
- 若要優先探索，可先評估機轉上較合理的外耳炎（需另行開發耳用劑型並評估鼓膜安全性）
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

