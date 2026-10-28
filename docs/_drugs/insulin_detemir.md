---
layout: default
title: Insulin Detemir
parent: 僅模型預測 (L5)
nav_order: 471
evidence_level: L5
indication_count: 9
monitor_inn: "INSULIN DETEMIR"
predicted_indications: ["autoimmune oophoritis", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "focal stiff limb syndrome", "classic stiff person syndrome", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy"]
last_modified_at: 2026-10-23
description: "Insulin Detemir：預測新適應症為自體免疫性卵巢炎（證據等級 L5）。原適應症：知識圖譜記錄的關聯：糖尿病、糖尿病酮酸中毒"
---

# Insulin Detemir
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

## Insulin Detemir：從糖尿病到自體免疫性卵巢炎
{: .text-alpha }

## 一句話總結

Insulin Detemir 是長效基礎胰島素類似物，知識圖譜中記錄的原用途為糖尿病與糖尿病酮酸中毒。
TxGNN 模型預測它可能對**自體免疫性卵巢炎 (Autoimmune Oophoritis)** 有效，但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 知識圖譜記錄的關聯：糖尿病、糖尿病酮酸中毒（香港許可證資料未載明核准適應症文字） |
| 預測新適應症 | 自體免疫性卵巢炎 |
| TxGNN 預測分數 | 0.9967 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 3 張／共 3 張） |
| 許可證數 | 3 張（有效 3 張） |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Insulin Detemir 是胰島素類似物，主要用於血糖控制。

卵巢顆粒細胞與膜細胞存在胰島素訊號，理論上可能與卵巢功能有關。但沒有任何證據顯示 Insulin Detemir 對自體免疫性卵巢損傷具有免疫調節作用。這個關聯屬於推測，高分僅代表模型的計算結果。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-65011 | LEVEMIR FLEXPEN SOLUTION FOR INJECTION IN PRE-FILLED PEN 100U/ML | 未載明 | 未載明 |
| HK-53538 | LEVEMIR FLEXPEN INJ 100U/ML | 未載明 | 未載明 |
| HK-67929 | LEVEMIR FLEXPEN SOLUTION FOR INJECTION IN PRE-FILLED PEN 100U/ML | 未載明 | 未載明 |

三張許可證皆為單一成分製劑，持有者為 NOVO NORDISK HONG KONG LIMITED。

## 安全性考量

- **藥物交互作用**：資料共收錄 100 筆交互作用，以下為部分列示。
  - 中度：Phenylephrine、Acebutolol、Acetazolamide、Formoterol、Pseudoephedrine、Doxycycline、Epinephrine、Ethinylestradiol、Hydrocortisone、Albiglutide、Salbutamol、Ethanol、Hydrochlorothiazide、Alogliptin、Metformin、Pioglitazone、Estradiol、Alpelisib
  - 輕微：外用 Hydrocortisone、外用 Alclometasone

其他警語與禁忌症請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型計算，沒有任何臨床試驗或文獻直接研究此疾病，證據等級為 L5。
- 機轉上缺乏免疫調節的依據，且尚無仿單安全性資料可供評估。

**若要推進需要：**
- 補充作用機轉資料，並評估胰島素在自體免疫性卵巢損傷中的生物學合理性
- 取得香港仿單的警語與禁忌症資料
- 進行文獻回顧或前臨床研究，確認是否有任何直接證據
- 在上述條件具備前，不建議投入臨床開發

### 其他預測項目的補充說明

其餘 8 項預測同樣只有模型分數，沒有試驗或文獻支持，建議皆為 Hold。

| 排名 | 預測疾病 | 分數 | 簡要評論 |
|------|---------|------|---------|
| 2 | 骨發育不良（Opsismodysplasia） | 0.9964 | INPPL1 (SHIP2) 突變影響胰島素訊號，但並無外源胰島素可矯正骨骼表現的證據 |
| 3 | 硫胺素反應性功能障礙症候群 | 0.9963 | 胰島素僅能處理併發的糖尿病，屬於原適應症的延伸 |
| 4 | 局部僵硬肢體症候群 | 0.9962 | 預測可能來自抗 GAD65 自體免疫與糖尿病的關聯，而非治療機轉 |
| 5 | 典型僵人症候群 | 0.9962 | 同上，胰島素只治療併發的糖尿病 |
| 6 | 胰臟發育不全 | 0.9951 | 胰島素替代在生物學上合理，但屬於原糖尿病治療範疇，且無針對此藥的證據 |
| 7 | 藥物誘發局部脂肪失養 | 0.9943 | 注射胰島素本身可能造成此問題，不支持作為治療用途 |
| 8 | 離心性脂肪失養 | 0.9941 | 缺乏胰島素相關的治療依據 |
| 9 | 壓力誘發局部脂肪萎縮 | 0.9940 | 注射胰島素是已知的誘因，預測可能只是藥物與疾病的關聯 |
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

