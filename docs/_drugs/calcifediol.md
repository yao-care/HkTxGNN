---
layout: default
title: Calcifediol
parent: 僅模型預測 (L5)
nav_order: 145
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Calcifediol：預測新適應症為維生素 D 缺乏症（本體論中已標示為過時術語）（證據等級 L5）。原適應症：高血鈣症、腎鈣質沉著症、磷代謝疾病、低磷血症、佝僂病、骨軟化症、腎性骨病變"
monitor_inn: "CALCIFEDIOL"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "hereditary hypophosphatemic rickets", "vitamin D-dependent rickets"]
---

# Calcifediol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Calcifediol：從維生素 D 代謝相關疾病到維生素 D 缺乏症

## 一句話總結

Calcifediol（25-羥基維生素 D）原本用於高血鈣、低磷血症、佝僂病、骨軟化症與腎性骨病變等礦物質與骨代謝相關疾病。
TxGNN 模型預測它可能對**維生素 D 缺乏症（obsolete vitamin D deficiency）**有效，但這個預測目前**沒有臨床試驗**支持。排名第 3、第 4 的預測各有 **1 篇文獻**，皆屬綜述或病例報告層級。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血鈣症、腎鈣質沉著症、磷代謝疾病、低磷血症、佝僂病、骨軟化症、腎性骨病變（來自知識圖譜，香港許可證未列適應症文字） |
| 預測新適應症 | 維生素 D 缺乏症（本體論中已標示為過時術語） |
| TxGNN 預測分數 | 99.99% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold |

其他預測適應症：

| 排名 | 預測適應症 | TxGNN 分數 | 證據等級 | 建議 |
|------|-----------|-----------|---------|------|
| 2 | 腎小管酸中毒 | 99.86% | L5 | Hold |
| 3 | 遺傳性低磷性佝僂病 | 99.76% | L4 | Research Question |
| 4 | 維生素 D 依賴性佝僂病 | 99.18% | L4 | Research Question |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Calcifediol 是循環中維生素 D 的主要代謝物，也是活性型態 calcitriol 的直接前驅物，同時是評估維生素 D 營養狀態的標準生物標記。因此，它用於維生素 D 缺乏在生物學上合理。

不過，需要留意兩點。第一，「維生素 D 缺乏症」這個詞條在本體論中已被標示為過時，應是現行詞條的舊版重複項目。第二，這個用途其實接近甚至屬於現有適應症範圍，嚴格來說不算真正的藥物再利用。0.9999 的高分僅代表模型預測，並不等於臨床證據。

在其他預測中，**維生素 D 依賴性佝僂病 1B 型**的機轉最具特異性。此病由 25-羥化酶（CYP2R1）缺陷造成，使維生素 D 無法轉化為 calcifediol，直接補充 calcifediol 可繞過這個阻斷點。但 1A 型（1α-羥化酶缺陷）不會對 calcifediol 有反應，需使用 calcitriol。

遺傳性低磷性佝僂病的主要缺陷是腎臟排磷，且 FGF23 過多會抑制 1α-羥化步驟，因此 calcifediol 的效益可能有限且屬間接。腎小管酸中毒則可能透過改善骨與礦物質代謝提供輔助作用，但無法矯正根本的腎小管缺陷。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

以下文獻來自排名較後的預測適應症，排名第 1 的預測目前無相關文獻。

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | 整理各型佝僂病及維生素 D 與其類似物的治療方式（對應遺傳性低磷性佝僂病） |
| [28548312](https://pubmed.ncbi.nlm.nih.gov/28548312/) | 2017 | 病例系列 | Journal of Bone and Mineral Research | 描述 2 個家族共 7 名 25-羥化酶缺陷（VDDR1B）患者，探討此罕見疾病是否被漏診（對應維生素 D 依賴性佝僂病） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68725 | RAYALDEE EXTENDED-RELEASE SOFT CAPSULES 30MCG | 未提供 | 未提供 |
| HK-67894 | HIDROFEROL CAPSULES 0.266MG | 未提供 | 未提供 |

---

## 安全性考量

- **知識圖譜中標示的禁忌疾病**（來源為知識圖譜，並非仿單內容）：腎臟疾病、膿輸尿管、類肉瘤病、高血鈣症、腎鈣質沉著症、磷代謝疾病、腎結石（含 SLC26A1 相關易感性）、急性尿酸腎病變、高磷血症、維生素過多症、閉塞性動脈硬化症。
- **藥物交互作用**：共查得 57 筆，以下為部分範例。
  - 重度（Major）：Cholecalciferol、Calcitriol、Burosumab
  - 中度（Moderate）：Fosphenytoin、Carbamazepine、巴比妥類（Amobarbital、Butalbital、Butabarbital）、噻嗪類利尿劑（Hydrochlorothiazide、Chlorothiazide、Chlorthalidone 等）、氫氧化鋁、膽酸結合劑（Cholestyramine、Colesevelam、Colestipol）、Digitoxin、局部型 Calcipotriol 與 Calcitriol

與其他維生素 D 類藥物併用有累積性高血鈣的風險。仿單的警語與禁忌資料尚待補齊，詳細內容請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 排名第 1 的預測（維生素 D 缺乏症）僅有模型分數，沒有臨床試驗或文獻，且該疾病詞條已過時，也接近既有適應症，不算真正的再利用。
- 值得優先追蹤的是**維生素 D 依賴性佝僂病 1B 型**，機轉特異性強，建議列為研究問題。但目前只有病例層級的證據。

**若要推進需要：**
- 取得香港許可證的核准適應症與仿單警語、禁忌（目前資料缺口屬阻擋級，無法進入安全性篩選）
- 補充作用機轉（MOA）資料
- 釐清過時疾病詞條與現行「維生素 D 缺乏症」的對應，並確認是否已屬核准用途
- 針對 VDDR1B 進行系統性文獻檢索，確認 calcifediol 的實際療效與劑量
- 制定高血鈣與腎功能的監測計畫，並審視與其他維生素 D 類藥物及噻嗪類利尿劑的併用風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

