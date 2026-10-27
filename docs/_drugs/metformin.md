---
layout: default
title: Metformin
parent: 僅模型預測 (L5)
nav_order: 568
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Metformin：預測新適應症為典型僵人症候群 (Classic Stiff Person Syndrome)（證據等級 L5）。原適應症：第二型糖尿病 (Type 2 Diabetes Mellitus)"
monitor_inn: "Metformin"
predicted_indications: ["classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
---

# Metformin
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

## Metformin：從第二型糖尿病到僵人症候群（Classic Stiff Person Syndrome）
{: .text-alpha }

## 一句話總結

Metformin（二甲雙胍）原本用於治療第二型糖尿病。
TxGNN 模型預測它可能對**典型僵人症候群 (Classic Stiff Person Syndrome)** 有效，
但目前**沒有任何臨床試驗或文獻**支持這個方向，僅為模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 第二型糖尿病 (Type 2 Diabetes Mellitus) |
| 預測新適應症 | 典型僵人症候群 (Classic Stiff Person Syndrome) |
| TxGNN 預測分數 | 99.45% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 20 張 |
| 建議決策 | Hold |

註：原適應症取自 TxGNN 知識圖譜的適應症資料，香港許可證的核准適應症文字在本次資料中皆為空白。

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。Metformin 在第二型糖尿病的療效已被證實，一般認為其作用與改善胰島素敏感性、活化 AMPK 路徑有關，但這部分並非來自本次彙整的資料，僅供參考。

僵人症候群是一種自體免疫性神經疾病（常見抗 GAD65 抗體），常與第一型糖尿病及其他自體免疫疾病並存。因此可推測 Metformin 透過 AMPK 活化與免疫代謝調節可能有某種關聯。但 Metformin 的抗發炎作用在這類神經疾病中尚未被證實，本次資料也不支持任何直接機轉。

需要特別注意：同屬僵硬類疾病的**局限性僵肢症候群 (Focal Stiff Limb Syndrome)** 得到完全相同的分數 (99.45%)，顯示預測可能來自知識圖譜中相近疾病的鄰近關係，而非獨立證據。

### 其他預測適應症（皆為 L5，建議 Hold）

| 排名 | 預測適應症 | TxGNN 分數 | 備註 |
|------|-----------|-----------|------|
| 2 | 局限性僵肢症候群 (Focal Stiff Limb Syndrome) | 99.45% | 與排名 1 同分，推測來自相近疾病的圖譜關聯 |
| 3 | 骨發育不良症 (Opsismodysplasia) | 99.40% | INPPL1 突變影響 PI3K/AKT 訊號，與 Metformin 的胰島素/AMPK/mTOR 路徑理論上有重疊，但未經驗證 |
| 4 | 硫胺素反應性功能異常症候群 (Thiamine-responsive Dysfunction Syndrome) | 99.40% | Metformin 至多是治療合併的糖尿病，而非改善疾病本身；與有機陽離子轉運蛋白的交互作用也需留意 |
| 5 | 藥物誘發性局部脂肪營養不良 (Drug-induced Localized Lipodystrophy) | 99.06% | 改善胰島素敏感性有生物學上的合理性，但局部型病理不同，相關性不確定 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 20 張有效單方許可證（無已註銷）。以下列出 5 張主要許可證：

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-27087 | GLUCOPHAGE TAB 500MG（Merck Pharmaceutical (HK)） | 未標示 | 未標示 |
| HK-50383 | GLUCOPHAGE TAB 1000MG（Merck Pharmaceutical (HK)） | 未標示 | 未標示 |
| HK-68753 | GLUCOPHAGE XR PROLONGED-RELEASE TABLETS 500MG（Merck Pharmaceutical (HK)） | 未標示 | 未標示 |
| HK-65175 | METFORMIN SANDOZ TABLETS 500MG（Sandoz Hong Kong） | 未標示 | 未標示 |
| HK-66869 | METPHAR XR 750 EXTENDED-RELEASE TABLETS 750MG（Primal Chemical） | 未標示 | 未標示 |

---

## 安全性考量

- **禁忌症（來自知識圖譜，非仿單內容）**：圖譜標示的相關疾病包括肝衰竭、腎臟疾病、胰臟炎、肝臟疾病、膽囊疾病、充血性心衰竭、腎上腺皮質功能不全、腦下垂體功能低下及相關先天性疾病（如 Kallmann 症候群、Sheehan 症候群）等。
- **藥物交互作用**：共查得 100 筆，以下為部分範例：
  - **嚴重 (Major)**：Acetazolamide、乙醇 (Ethanol)
  - **中度 (Moderate)**：Dolutegravir、Abemaciclib、Ranitidine、Nifedipine、Ibuprofen、Ketorolac、Hydrochlorothiazide、Ethinylestradiol、Hydrocortisone、Epinephrine、Salbutamol 等
  - **輕微 (Minor)**：Acarbose、外用 Hydrocortisone

仿單的警語與禁忌症資料目前缺漏，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型分數，沒有任何臨床試驗或文獻佐證（證據等級 L5），且機轉連結屬推測。
- 排名 1 與 2 的分數完全相同，顯示預測可能是圖譜鄰近效應，而非獨立訊號。

**若要推進需要：**
- 取得 Metformin 的詳細作用機轉資料（MOA）
- 取得香港衛生署仿單的警語與禁忌症，完成安全性篩選
- 系統性檢索 Metformin 與僵人症候群、抗 GAD65 自體免疫的文獻與試驗，確認是否存在支持證據
- 若有初步證據，再評估神經疾病族群使用的安全性與合適劑型
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

