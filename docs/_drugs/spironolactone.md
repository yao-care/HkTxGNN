---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 832
evidence_level: L5
indication_count: 2
---

# Spironolactone
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

# Spironolactone：從高血壓與心衰竭到頭皮單純性毛髮稀少症

## 一句話總結

Spironolactone（螺旋內酯固醇）原本用於高血壓、鬱血性心衰竭及原發性醛固酮增多症等疾病。
TxGNN 模型預測它可能對**頭皮單純性毛髮稀少症 (Hypotrichosis simplex of the scalp)** 有效，但目前**沒有任何臨床試驗或文獻**支持，僅屬模型運算的預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、鬱血性心衰竭、醛固酮增多症、原發性醛固酮增多症、Bartter 症候群、Waterhouse-Friderichsen 症候群（來自知識圖譜，非仿單文字） |
| 預測新適應症 | 頭皮單純性毛髮稀少症 (Hypotrichosis simplex of the scalp) |
| TxGNN 預測分數 | 99.26% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。就一般藥理知識而言，spironolactone 是鹽皮質素受體拮抗劑，同時具有抗雄性素活性，可阻斷雄性素受體並降低雄性素合成。臨床上它常被超適應症用於雄性素性禿髮及女性型脫髮，因此與「毛髮」相關的機轉看似合理。

不過，原適應症（心血管與電解質相關疾病）與新適應症（毛髮疾病）在疾病本質上關聯不大，兩者的連結主要來自模型運算。頭皮單純性毛髮稀少症是罕見的遺傳性疾病（例如 CDSN、APCDD1 或 RPL21 變異），病理機轉並非由雄性素驅動，因此抗雄性素作用是否適用並不明確。

另一個預測的適應症是先天性毛髮稀少伴粟丘疹 (congenital hypotrichosis milia, 分數 99.04%)，同樣是罕見遺傳病，也沒有證據顯示阻斷鹽皮質素或雄性素受體能改變其病程。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

## 文獻證據

目前無相關文獻。

---

## 香港上市資訊

香港共有 9 張有效的單一成分許可證（無已註銷者）。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 廠商 |
|---------|------|------|
| HK-68285 | SMIRON TABLETS 25MG | WELLDONE PHARMACEUTICALS LIMITED |
| HK-67773 | SPIROLON 100 TABLETS 100MG | HEALTHCARE PHARMASCIENCE LIMITED |
| HK-63188 | EURO-SPIRO TABLETS 25MG | EUROPHARM LAB CO LTD |
| HK-61599 | SPIRONOLACTONE ACTAVIS TABLETS 25MG | TEVA PHARMACEUTICAL HONG KONG LIMITED |
| HK-19636 | ALDACTONE TAB 25MG | PFIZER CORPORATION HONG KONG LIMITED |

---

## 安全性考量

- **知識圖譜標示的禁忌相關疾病**（來自藥物－疾病關聯，並非仿單文字）：腎臟疾病、無尿症、缺鉀症、高血鈣症、腎鈣化症、高尿酸血症、痛風、糖尿病及糖尿病酮酸中毒、胰臟炎、全身性紅斑性狼瘡（含兒童型）、副甲狀腺機能亢進、纖維性骨炎、肝昏迷與肝性腦病變、新生兒黃疸、膿尿輸尿管、磷代謝疾病。
- **藥物交互作用**：資料共查得 100 筆，以下為其中部分：
  - 重大 (Major)：Loperamide
  - 中度 (Moderate)：Hydrocortisone、Metformin、Bupropion、Triamcinolone、Morphine、Dexamethasone、Betamethasone、Budesonide，以及多種 SGLT2 抑制劑（Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin）
  - 輕微 (Minor)：Doxycycline、Acetylsalicylic acid、Fidaxomicin

仿單的警語與禁忌資料尚未取得，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型運算（分數高但無任何臨床試驗或文獻），證據等級為 L5。
- 目標疾病是非雄性素驅動的罕見遺傳病，抗雄性素機轉不一定適用。
- 仿單安全性資料與作用機轉資料仍缺漏。

**若要推進需要：**
- 補齊作用機轉資料（如 DrugBank），並分析其與 CDSN、APCDD1、RPL21 等致病途徑的關聯。
- 取得香港衛生署仿單中的警語與禁忌，完成安全性初步篩檢。
- 進行文獻與試驗登記的系統性檢索，確認是否有病例報告或前臨床研究。
- 評估給藥途徑（口服或外用）是否適合頭皮局部治療，並考量長期使用的安全性（如高血鉀、抗雄性素副作用）。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

