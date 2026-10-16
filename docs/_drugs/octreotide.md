---
layout: default
title: Octreotide
parent: 僅模型預測 (L5)
nav_order: 636
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Octreotide：預測新適應症為外陰倒置性毛囊角化症 (vulvar inverted follicular keratosis)（證據等級 L5）。原適應症：肢端肥大症、垂體機能亢進、類癌症候群"
---

# Octreotide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Octreotide：從肢端肥大症到外陰倒置性毛囊角化症

## 一句話總結

Octreotide 是體抑素（somatostatin）類似物，原本用於肢端肥大症、垂體機能亢進與類癌症候群。
TxGNN 模型預測它可能對**外陰倒置性毛囊角化症 (vulvar inverted follicular keratosis)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型推論。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 肢端肥大症、垂體機能亢進、類癌症候群 |
| 預測新適應症 | 外陰倒置性毛囊角化症 (vulvar inverted follicular keratosis) |
| TxGNN 預測分數 | 99.58% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。一般認為 Octreotide 是體抑素類似物，主要作用於體抑素受體 SSTR2 與 SSTR5，可抑制生長激素等激素分泌，這與其在肢端肥大症與類癌症候群的用途相符。

外陰倒置性毛囊角化症是良性上皮病變，目前**沒有已知機轉**將體抑素受體訊號與此疾病連結。任何假設（例如抗增生作用）都屬推測，尚未經驗證。高分可能源自知識圖譜中與皮膚病變節點的鄰近關係，而非實際的生物學依據。

另一個排名第二的預測為**脂漏性角化症 (seborrheic keratosis)**，分數 99.55%，同樣沒有任何臨床或文獻證據。兩者分數極為接近，顯示預測可能來自共同的圖譜鄰居，而非疾病特異性的生物機轉。

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

## 香港上市資訊

資料顯示 Octreotide 在香港有 20 張有效單方許可證（無複方、無已註銷）。以下列出 5 張主要許可證，核准適應症欄位於現有資料中未提供。

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-32471 | SANDOSTATIN INJ 0.1MG/ML（Novartis） | 注射劑 | 請參考原廠仿單 |
| HK-33912 | SANDOSTATIN INJ 0.5MG/ML（Novartis） | 注射劑 | 請參考原廠仿單 |
| HK-44140 | SANDOSTATIN LAR FOR INJ 20MG（Novartis） | 長效注射劑 | 請參考原廠仿單 |
| HK-62639 | DBL OCTREOTIDE INJECTION 0.5MG/ML（Pfizer） | 注射劑 | 請參考原廠仿單 |
| HK-68938 | OCTREOTIDE BENDALIS SOLUTION FOR INJECTION/INFUSION 0.1MG/1ML（Mekim） | 注射劑 | 請參考原廠仿單 |

## 安全性考量

- **知識圖譜標示的禁忌或需謹慎情形**（來自模型知識圖譜，非仿單內容）：高血糖、糖尿病、糖尿病酮酸中毒、低血糖、甲狀腺功能低下（含黏液水腫、先天性甲狀腺功能低下）、肝硬化與肝病、膽囊疾病與膽結石（膽石症、膽囊結石、膽總管結石）、腸阻塞與腸道阻塞、心臟驟停、心臟傳導疾病、腎衰竭與尿毒症、維生素 B12 缺乏。
- **藥物交互作用**：查詢共找到 100 筆，以下為資料中列出的部分中等程度（Moderate）交互作用，主要為降血糖藥物：
  - 口服及注射降血糖藥：Acarbose、Metformin、Glimepiride、Chlorpropamide、Alogliptin、Linagliptin
  - SGLT2 抑制劑：Canagliflozin、Dapagliflozin、Empagliflozin
  - GLP-1 類藥物：Albiglutide、Dulaglutide、Semaglutide
  - 各類胰島素：Insulin aspart、degludec、detemir、glargine、glulisine、human (isophane / regular / inhalation)

  Octreotide 會影響血糖調節，與上述藥物併用時需密切監測血糖。

仿單的正式警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold**

**理由：**
- 兩個預測適應症（外陰倒置性毛囊角化症、脂漏性角化症）皆僅有模型分數，沒有臨床試驗、文獻或已知機轉支持，證據等級為 L5。
- 疾病為良性皮膚病變，而 Octreotide 為需注射的藥物，且具血糖、膽道、心臟傳導等安全性顧慮，風險效益比目前無從支持推進。

**若要推進需要：**
- 取得 Octreotide 詳細的作用機轉資料，並釐清體抑素受體在角化症相關皮膚組織的表現與角色
- 進行文獻與臨床試驗的系統性檢索，確認是否存在任何病例報告或前臨床研究
- 取得香港衛生署的仿單（警語、禁忌與核准適應症），完成安全性篩選
- 評估給藥途徑的適配性（目前為注射劑，是否適合局部或皮膚病變用途尚待評估）
- 若有機轉假設，先以前臨床或探索性研究驗證，再考慮進入臨床階段
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

