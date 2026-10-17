---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 876
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Ticagrelor：預測新適應症為顱內動脈硬化 (Intracranial Arteriosclerosis)（證據等級 L5）。原適應症：急性冠心症、周邊血管疾病、間歇性跛行、周邊動脈疾病"
monitor_inn: "TICAGRELOR"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "ischemic disease"]
---

# Ticagrelor
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Ticagrelor：從急性冠心症到顱內動脈硬化

## 一句話總結

Ticagrelor 是一種抗血小板藥物，原本用於急性冠心症及周邊血管疾病的治療。
TxGNN 模型預測它可能對**顱內動脈硬化 (Intracranial Arteriosclerosis)** 有效，
目前有 **2 個臨床試驗**和 **2 篇文獻**直接支持這個方向（其中 1 個為進行中的 Phase 3 試驗，尚無結果）。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 急性冠心症、周邊血管疾病、間歇性跛行、周邊動脈疾病 |
| 預測新適應症 | 顱內動脈硬化 (Intracranial Arteriosclerosis) |
| TxGNN 預測分數 | 99.97% |
| 證據等級 | L5（依判定規則嚴格適用，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 8 張 |
| 建議決策 | Hold（待 CAPTIVA 試驗結果）；若以相關缺血性疾病的證據而論，可為 Proceed with Guardrails |

> **關於證據等級：**資料中將此預測標為 L1，但針對顱內動脈硬化本身，目前僅有 1 個進行中的 Phase 3 試驗（CAPTIVA，尚無結果）與 1 個小型招募中試驗，並無已完成的 Phase 3 RCT。依本報告的判定規則，直接證據不足 L1，較接近 L3（有觀察性研究：一項小型世代研究）。L1 等級來自「缺血性疾病」這一更廣泛的預測項目（見下方補充說明）。

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（資料庫中 MOA 欄位空缺）。根據已知資訊，Ticagrelor 是可逆性的血小板 P2Y12 受體抑制劑，能減少血小板聚集與血栓形成。與 clopidogrel 不同，它不需要經 CYP2C19 代謝活化，因此對 CYP2C19 功能缺失基因型的患者可能更有利。

原適應症（急性冠心症、周邊動脈疾病）與顱內動脈硬化的共同病理基礎，都是動脈粥樣硬化斑塊上的血小板性血栓。抗血小板治療在冠狀動脈與周邊動脈已證實有效，機轉上可延伸到顱內動脈狹窄。此外，Ticagrelor 已被用於神經介入手術的雙重抗血小板療法，以及中風／TIA 的預防。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) | Phase 3 | 進行中（不再招募） | 1683 | CAPTIVA：比較 rivaroxaban、ticagrelor 或兩者合用與 clopidogrel，評估 1 年內缺血性中風、腦出血或血管性死亡率；尚無結果 |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | 不適用 | 招募中 | 100 | 症狀性顱內動脈粥樣硬化患者，基因型引導的 P2Y12 抑制劑選擇 vs 傳統 clopidogrel；尚無結果 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | 世代研究 | J Neurointerv Surg | 顱內支架置放時，ticagrelor 60 mg 每日兩次加阿斯匹靈，與標準阿斯匹靈加 clopidogrel 方案比較的經驗 |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | 試驗設計 | Int J Stroke | CAPTIVA 試驗的設計與早期進展 |

**補充（相關缺血性疾病的大型證據）：**預測清單中「缺血性疾病」項目有多項大型 RCT 支持 ticagrelor 在冠狀動脈與腦血管情境的效益，例如 THEMIS（穩定冠心病合併糖尿病，PMID 31475798）、TWILIGHT（PCI 後，PMID 31556978）、CHANCE-2（CYP2C19 功能缺失的中風／TIA，PMID 34708996）。這些結果屬於已核准或相近適應症，並非直接證明對顱內動脈硬化有效。

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-68970 | SYNLINTA FILM-COATED TABLETS 90MG | 錠劑 | 請參考原廠仿單 |
| HK-61187 | BRILINTA TAB 90MG | 錠劑 | 請參考原廠仿單 |
| HK-67990 | TICAGRELOR SANDOZ TABLETS 90MG | 錠劑 | 請參考原廠仿單 |
| HK-68747 | TRILINTA TABLETS 90MG | 錠劑 | 請參考原廠仿單 |
| HK-67899 | TICAGRELOR TABLETS 90MG | 錠劑 | 請參考原廠仿單 |

（共 8 張有效許可證，上表列出其中 5 張；另有 BRILINTA 60MG、TILANTA 90MG、TICAROGG 90 等。）

## 安全性考量

- **知識圖譜標示的相關疾病禁忌：**肝衰竭、肝病、膽囊疾病、顱內出血（來自知識圖譜，非仿單內容）。顱內出血特別值得注意，因為預測的新適應症本身就是腦血管疾病。
- **藥物交互作用：**共查得 100 筆，以下為主要項目：
  - 重大（Major）：Clarithromycin
  - 中度（Moderate）：Acetylsalicylic acid（阿斯匹靈）、Morphine、Simvastatin、Dexamethasone、Aprepitant、Miconazole 等
  - 輕度（Minor）：Naloxegol、Prucalopride

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Hold（等待 CAPTIVA 結果；缺乏仿單安全資料前不宜推進）**

**理由：**
- 對顱內動脈硬化的直接證據僅有進行中的 Phase 3 試驗與小型研究，尚無已完成的 RCT 結果。
- 仿單的警語與禁忌資料缺漏，且新適應症屬腦血管疾病，出血風險（尤其顱內出血）需審慎評估。
- 相關的冠狀動脈與中風／TIA 大型 RCT 提供強力的間接支持，若 CAPTIVA 結果正向，可升級為 Proceed with Guardrails。

**若要推進需要：**
- 追蹤 CAPTIVA（NCT05047172，預計 2027 年 1 月完成）的結果
- 取得香港衛生署仿單的警語與禁忌資料，完成安全性篩選
- 補充詳細的作用機轉資料（MOA）
- 制定出血風險監測計畫，以及 CYP2C19 基因型導向的用藥策略
- 其他預測項目（Monckeberg 動脈硬化、陰莖異常勃起、May-Thurner 症候群）僅有模型預測或極薄弱的證據，建議維持 Hold
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

