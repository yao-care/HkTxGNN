---
layout: default
title: Ticagrelor
parent: 僅模型預測 (L5)
nav_order: 876
evidence_level: L5
indication_count: 9
monitor_inn: "TICAGRELOR"
predicted_indications: ["intracranial arteriosclerosis", "Monckeberg arteriosclerosis", "priapism", "ischemic disease", "May-Thurner syndrome", "livedo reticularis", "vascular ectasia", "angiodysplasia", "venous thromboembolism"]
last_modified_at: 2026-10-28
description: "Ticagrelor：預測新適應症為顱內動脈硬化（證據等級 L3）。原適應症：香港許可證資料未載明核准適應症文字。知識圖譜記錄的關聯包括急性冠心症、周邊血管疾病、間歇性跛行、周邊動脈疾病"
---

# Ticagrelor
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

## Ticagrelor：從急性冠心症到顱內動脈硬化
{: .text-alpha }

## 一句話總結

Ticagrelor 是一種抗血小板藥物，知識圖譜記錄它與急性冠心症、周邊動脈疾病等血管疾病有關聯。
TxGNN 模型預測它可能對**顱內動脈硬化 (intracranial arteriosclerosis)** 有效。
目前有 **2 個直接相關的臨床試驗**和 **2 篇直接相關的文獻**，其中大型 Phase 3 試驗仍在進行、尚無結果。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 香港許可證資料未載明核准適應症文字。知識圖譜記錄的關聯包括急性冠心症、周邊血管疾病、間歇性跛行、周邊動脈疾病（僅為知識圖譜關聯，非許可證核准內容） |
| 預測新適應症 | 顱內動脈硬化 |
| TxGNN 預測分數 | 0.9997 |
| 證據等級 | L5 |
| 香港上市 | 上市中（有效許可證 8 張／共 8 張） |
| 許可證數 | 8 張（有效 8 張） |
| 建議決策 | Proceed with Guardrails |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。依一般藥理知識，Ticagrelor 是可逆性的 P2Y12 受體拮抗劑，能抑制 ADP 引起的血小板活化與聚集。它不是前驅藥，不需經 CYP2C19 活化，因此不受 CYP2C19 功能缺失基因型限制，而這個限制會降低 clopidogrel 的療效。

顱內動脈粥樣硬化狹窄造成缺血事件的機轉，包括富含血小板的血栓形成與動脈到動脈的栓塞。因此在機轉上，抑制 P2Y12 有生物學上的合理性。這與知識圖譜中記錄的心血管動脈疾病關聯，屬於同一類動脈粥樣硬化血栓問題。

要注意的是，顱內出血風險必須與潛在益處一併權衡。知識圖譜也記錄了顱內出血與此藥的禁忌關聯。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05047172](https://clinicaltrials.gov/study/NCT05047172) (CAPTIVA) | Phase 3 | 進行中（不再招募） | 1683 | 比較 rivaroxaban、ticagrelor 或兩者併用是否優於 clopidogrel，主要終點為 1 年內缺血性中風、腦出血或血管性死亡。尚無結果 |
| [NCT06714526](https://clinicaltrials.gov/study/NCT06714526) | 無分期 | 招募中 | 100 | 症狀性顱內動脈粥樣硬化患者，比較基因型引導的 P2Y12 抑制劑選擇（含 ticagrelor）與標準 clopidogrel。規模小、尚無結果 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39658130](https://pubmed.ncbi.nlm.nih.gov/39658130/) | 2025 | 世代研究 | Journal of NeuroInterventional Surgery | 顱內支架置放時，ticagrelor 60 mg 每日兩次加 aspirin 81 mg，與標準 aspirin 加 clopidogrel 方案比較的使用經驗 |
| [39862061](https://pubmed.ncbi.nlm.nih.gov/39862061/) | 2025 | 試驗設計與進度 | International Journal of Stroke | CAPTIVA 試驗的設計與早期進展，目的是找出優於 clopidogrel 加 aspirin 的雙重抗栓組合 |

## 香港上市資訊

香港共有 8 張有效的單一成分許可證，以下列出 5 張主要許可證。資料中未提供劑型與核准適應症文字。

| 許可證號 | 品名 | 持證商 |
|---------|------|--------|
| HK-61187 | BRILINTA TAB 90MG | ASTRAZENECA HONG KONG LIMITED |
| HK-64706 | BRILINTA TABLETS 60MG | ASTRAZENECA HONG KONG LIMITED |
| HK-67990 | TICAGRELOR SANDOZ TABLETS 90MG | SANDOZ HONG KONG LIMITED |
| HK-68970 | SYNLINTA FILM-COATED TABLETS 90MG | SYNCO (H.K.) LIMITED |
| HK-68747 | TRILINTA TABLETS 90MG | SB PHARMA LIMITED |

## 安全性考量

- **知識圖譜記錄的禁忌關聯**（非仿單文字）：肝衰竭、肝病、膽囊疾病、顱內出血。
- **藥物交互作用**：共查得 100 筆交互作用記錄。
  - 嚴重（Major）：Clarithromycin。
  - 中度（Moderate）：Acetylsalicylic acid（aspirin）、Morphine、Simvastatin、Dexamethasone、Budesonide、Aprepitant、Saxagliptin 等。

其餘警語與禁忌請參考原廠仿單。

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 有兩個直接研究顱內動脈硬化的試驗，其中 CAPTIVA 為大型 Phase 3，另有一篇顱內支架的世代研究。但目前沒有已完成的隨機試驗結果，因此證據等級為 L3，而非更高。
- 機轉上合理，但顱內出血風險是主要顧慮，須嚴格控管。

**若要推進需要：**
- 等待 CAPTIVA 試驗結果（預計 2027 年 1 月完成），確認 ticagrelor 相對於 clopidogrel 的療效與出血風險。
- 取得香港仿單的警語、禁忌與核准適應症文字，並補齊作用機轉資料。
- 制定病人篩選標準（排除顱內出血風險高者）、抗血小板療程長度與出血監測計畫。
- 評估與 clarithromycin 等強效 CYP3A 抑制劑及 aspirin 的交互作用管理。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

