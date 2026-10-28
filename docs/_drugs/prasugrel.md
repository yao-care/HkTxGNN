---
layout: default
title: Prasugrel
parent: 僅模型預測 (L5)
nav_order: 724
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-28
monitor_inn: "Prasugrel"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "leprosy"]
description: "Prasugrel：預測新適應症為肺高壓 (Pulmonary Hypertension)（證據等級 L5）。原適應症：本地許可證資料未記載適應症"
---

# Prasugrel
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

## Prasugrel: 肺高壓 (Pulmonary Hypertension)；證據較多的替代方向：偏頭痛 (pulmonary hypertension)
{: .text-alpha }

## 一句話總結

Prasugrel 是 P2Y12 血小板抑制劑，原本用於急性冠心症 (acute coronary syndrome) 的治療。
TxGNN 模型預測分數最高的新適應症是**肺高壓 (pulmonary hypertension)**，但該項目缺乏直接證據。
實際證據較多的方向是**偏頭痛 (migraine disorder)**，目前有 **2 個臨床試驗**和 **2 篇相關文獻**，但都屬間接證據，且沒有任何一項是 prasugrel 的隨機對照試驗。

> 說明：本報告以預測分數最高者（肺高壓）作為主要預測新適應症，並另列證據較多的偏頭痛作為次要方向。標題採用後者，因為它是目前最有研究依據的方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本地許可證資料未記載適應症 |
| 預測新適應症 | 肺高壓 (Pulmonary Hypertension)；證據較多的替代方向：偏頭痛 (pulmonary hypertension) |
| TxGNN 預測分數 | 0.9988 |
| 證據等級 | 肺高壓 L5；偏頭痛 L3 |
| 香港上市 | 上市中（有效許可證 2 張／共 2 張） |
| 許可證數 | 2 張（有效 2 張） |
| 建議決策 | 肺高壓：Hold；偏頭痛：Hold（列為研究問題，需先補足證據） |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（MOA）。根據已知資訊，Prasugrel 是 P2Y12 拮抗劑，可抑制血小板聚集，在急性冠心症的療效已被證實。

**肺高壓：** 血小板活化與原位血栓形成可能參與肺血管重塑，因此機轉上有合理性。但本次整理的資料中沒有任何直接的臨床或前臨床證據，檢索到的兩篇文獻分別談 clopidogrel 在急性冠心症的用藥遵從性，以及 COVID-19 前的背景用藥，都與肺高壓無關。高分只是模型預測。

**偏頭痛：** 偏頭痛（尤其合併卵圓孔未閉 PFO 者）可能與矛盾性微栓子，或繞過肺部過濾的血小板衍生/血管活性介質有關。Thienopyridine 類藥物（如 prasugrel、clopidogrel）抑制血小板 P2Y12，理論上可減少這些作用。回溯性研究與 ticagrelor 的開放標籤先導試驗提供了「產生假說」的訊號，但並非 prasugrel 的隨機試驗。

---

## 臨床試驗證據

肺高壓目前無相關臨床試驗登記。以下為偏頭痛方向的試驗：

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT07629635](https://clinicaltrials.gov/study/NCT07629635) | Phase 3 | 招募中 | 32 | 以 PFO 為導向的治療（可能包含 prasugrel 等抗血小板藥）用於偏頭痛緩解；是否使用 prasugrel 尚未確認，僅間接支持 |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | 不適用 (NA) | 已終止 | 7 | GORE CARDIOFORM septal occluder（器材）經導管關閉 PFO 治療偏頭痛；僅收 7 人即終止，未評估 prasugrel |

---

## 文獻證據

肺高壓方向（兩篇皆與肺高壓無直接關聯，未列入下表）；以下為偏頭痛方向：

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [30478066](https://pubmed.ncbi.nlm.nih.gov/30478066/) | 2018 | 回溯性世代研究 | Neurology | 回顧合併 PFO 的偏頭痛患者使用 thienopyridine（仿單外使用）的臨床經驗 |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | 開放標籤先導試驗 | Neurology | Ticagrelor 用於難治型偏頭痛/PFO；起因是 clopidogrel 與 prasugrel 曾在部分 PFO 患者減輕偏頭痛症狀 |
| [42722054](https://pubmed.ncbi.nlm.nih.gov/42722054/) | 2026 | 前臨床動物研究 | Eur J Pharmacol | 小鼠 PTZ 點燃模型顯示 prasugrel 具神經保護作用；研究對象為癲癇而非偏頭痛，僅提示可能的神經效應 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66424 | PRASUGREL TABLETS 5MG | 未載明 | 未載明 |
| HK-66423 | PRASUGREL TABLETS 10MG | 未載明 | 未載明 |

兩張許可證皆為單方、有效狀態，持有人為 Camber Pharmaceuticals Hong Kong Limited。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**（來自模型知識圖譜，非仿單內容）：肝衰竭、低血壓、凝血疾病、中風、腦血管疾病、腦梗塞、外傷、血栓性血小板減少性紫斑症、顱內出血、短暫性腦缺血發作、椎基底動脈循環不全。
- **藥物交互作用**（共查得 100 筆，以下為部分重點）：
  - 重大 (Major)：Deferasirox、Ibritumomab tiuxetan
  - 中度 (Moderate)：Acetylsalicylic acid（阿斯匹靈）、Morphine、Opium、Fenfluramine、Dexfenfluramine、Sibutramine
  - 輕微 (Minor)：多種質子幫浦抑制劑（如 omeprazole、pantoprazole）與 H2 阻斷劑（如 famotidine、ranitidine）、Bupropion 等

出血風險是抗血小板藥物的核心考量，尤其本藥在知識圖譜中與顱內出血、中風史相關；用於偏頭痛這類非危及生命的適應症時，風險效益比需特別審慎。其餘安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Hold（肺高壓）／Hold，列為研究問題（偏頭痛）**

**理由：**
- 肺高壓僅有模型預測（L5），沒有任何直接證據支持。
- 偏頭痛有回溯性研究與相關藥物的先導試驗（L3），但缺乏 prasugrel 的隨機對照試驗；進行中的 Phase 3 試驗為 PFO 導向治療，且僅 32 人。Prasugrel 的出血風險也讓在此族群的效益評估更為重要。

**若要推進需要：**
- 取得完整作用機轉（MOA）資料與香港仿單的警語、禁忌資料（目前皆缺）
- 偏頭痛：針對 prasugrel 設計的隨機對照試驗，並明確鎖定合併 PFO 的族群
- 釐清 NCT07629635 是否實際使用 prasugrel
- 評估出血風險與雙重抗血小板治療的交互作用，訂定安全監測計畫
- 肺高壓：先進行前臨床或機轉研究，再考慮臨床試驗
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

