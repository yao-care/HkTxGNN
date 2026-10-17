---
layout: default
title: Amiloride
parent: 僅模型預測 (L5)
nav_order: 50
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Amiloride：預測新適應症為惡性高血壓性腎病 (Malignant Hypertensive Renal Disease)（證據等級 L5）。原適應症：高血壓、充血性心臟衰竭"
monitor_inn: "Amiloride"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "chronic pulmonary heart disease"]
---

# Amiloride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Amiloride：從高血壓到惡性高血壓性腎病

## 一句話總結

Amiloride 是一種保鉀利尿劑，原本用於高血壓與充血性心臟衰竭。
TxGNN 模型預測它可能對**惡性高血壓性腎病 (Malignant Hypertensive Renal Disease)** 有效，
但目前**沒有臨床試驗**，也**沒有直接相關文獻**，僅有模型預測支持。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 高血壓、充血性心臟衰竭（來自知識圖譜；香港許可證未載明適應症文字） |
| 預測新適應症 | 惡性高血壓性腎病 (Malignant Hypertensive Renal Disease) |
| TxGNN 預測分數 | 99.82% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 5 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知的藥理特性，Amiloride 可阻斷遠端腎elements 的上皮鈉通道 (ENaC)，減少鈉再吸收並降低血壓，同時具保鉀作用。

惡性高血壓性腎病與原本的高血壓適應症高度相關，因此這項預測較像是既有用途的延伸，而不是全新的再利用訊號。模型分數雖高，但缺乏任何試驗或文獻佐證，不能視為臨床有效的證據。

**其他排名較前的預測（皆屬探索性）：**

| 排名 | 預測適應症 | 分數 | 證據等級 | 說明 |
|------|-----------|------|---------|------|
| 2 | 惡性腎血管性高血壓 | 99.82% | L5 | 僅有 1 篇礦皮質素高血壓的一般性回顧，並非 Amiloride 療效證據 |
| 3 | 機轉不明的多因素肺高壓 | 99.81% | L5 | 無試驗與文獻 |
| 4 | 缺氧／肺病相關肺高壓 | 99.81% | L4 | 有 ENaC、ASIC1 的前臨床與生理研究，間接支持；多篇檢索結果與主題無關 |
| 5 | Braddock 症候群 | 99.75% | L5 | 無試驗與文獻，高分可能源於圖譜中共享的肺高壓節點 |
| 6 | 慢性肺心症 | 99.68% | L4 | 文獻多屬充血性心衰竭，非肺心症本身 |

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

針對首位預測（惡性高血壓性腎病），目前無相關文獻。

以下為排名第 2 位預測（惡性腎血管性高血壓）的唯一文獻，僅供參考：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12929904](https://pubmed.ncbi.nlm.nih.gov/12929904/) | 2003 | Review | Journal of Hypertension. Supplement | 礦皮質素性高血壓的診斷性回顧，非 Amiloride 治療惡性腎血管性高血壓的證據 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-25543 | AMILORIDE TAB 5MG | — | — |
| HK-25544 | AMITHIAZIDE TAB | — | — |
| HK-42186 | APO-AMILZIDE TAB 50/5MG | — | — |
| HK-50535 | POLI-URETIC TAB | — | — |
| HK-58537 | BILDURETIC TAB | — | — |

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自藥物－疾病關聯資料，並非仿單原文）：腎臟疾病、無尿症、肝臟疾病、肝性昏迷／肝性腦病變、胰臟炎、膽囊疾病、糖尿病、糖尿病酮酸中毒、糖尿病腎病變、缺鉀症、痛風、高尿酸血症、酸中毒（含後天性乳酸酸中毒）、副甲狀腺機能亢進、纖維性骨炎、全身性紅斑性狼瘡（含兒童型）、新生兒黃疸、膿輸尿管。
- **藥物交互作用**：資料庫共記錄 100 筆，以下為已列出的部分：
  - 中度：Hydrocortisone、Betamethasone、Dexamethasone、Budesonide、Metformin、Bupropion、Canagliflozin、Dapagliflozin、Empagliflozin、Ertugliflozin、Exenatide 等
  - 輕度：Doxycycline、Amoxicillin、Cimetidine
- **其他提醒**：與其他藥物併用時須留意高血鉀風險（文獻中有 trimethoprim-sulfamethoxazole 合併使用導致嚴重高血鉀的病例報告）。

完整警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 首位預測僅有模型分數支持（L5），沒有任何臨床試驗或直接文獻，且與原適應症（高血壓）重疊度高，並非明確的新用途。
- 肺高壓相關方向（排名 4）有間接的前臨床機轉證據，可列為研究問題，但距離臨床應用仍遠。

**若要推進需要：**
- 補齊香港仿單的警語、禁忌與核准適應症文字
- 補充 Amiloride 的作用機轉資料（DrugBank）
- 針對惡性高血壓性腎病進行系統性文獻回顧，尋找直接臨床證據
- 若考慮肺高壓方向，需進一步評估 ENaC／ASIC1 的機轉並設計前臨床或早期臨床研究
- 評估腎功能不全患者的高血鉀風險，建立血鉀與腎功能監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

