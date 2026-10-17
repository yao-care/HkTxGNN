---
layout: default
title: Flunarizine
parent: 僅模型預測 (L5)
nav_order: 385
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
monitor_inn: "FLUNARIZINE"
predicted_indications: ["migraine disorder"]
description: "Flunarizine：預測新適應症為偏頭痛 (Migraine Disorder)（證據等級 L5）."
---

# Flunarizine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Flunarizine：從（原適應症資料未提供）到偏頭痛

## 一句話總結

Flunarizine 是一種鈣離子通道阻斷劑，香港已有多張單方許可證，但本報告所用資料未記載其核准適應症。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
目前有 **13 個臨床試驗**和 **20 篇文獻**支持這個方向。
需要說明的是，flunarizine 在許多地區本來就是偏頭痛預防用藥，因此這項預測更像是對既有用途的確認，而非真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.12% |
| 證據等級 | L1（資料庫評定；但詳見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 9 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Flunarizine 是二苯哌嗪類（diphenylpiperazine）鈣離子通道阻斷劑，同時具有組織胺 H1 拮抗與多巴胺 D2 阻斷活性。藥理資料也顯示它作用於 D2 受體及 T 型鈣離子通道（Cav3.1、Cav3.2、Cav3.3）。它能抑制神經元鈣離子過載，降低皮質擴散性抑制（cortical spreading depression）的易感性。皮質擴散性抑制被認為是偏頭痛前兆的生理基礎，也是三叉神經血管系統活化的誘因，因此這個機轉直接支持偏頭痛預防用途。

目前缺乏詳細的藥物層級作用機轉紀錄，以上機轉說明依據已知藥理學，而非本報告所用的資料記錄。

偏頭痛預防是 flunarizine 在多個國家的主要用途，多篇文獻也將它列為預防性用藥的首選之一。不過本報告資料中，香港許可證的核准適應症欄位皆為空白，無法確認本地標示的適應症。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | 完成 | 62 | Flunarizine 10 mg/日 vs topiramate 50 mg/日用於慢性偏頭痛預防 |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | N/A | 完成 | 120 | 比較枕大神經阻斷、topiramate 與 flunarizine 用於陣發性偏頭痛 |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | 尚未招募 | 460 | 基層醫療中 amitriptyline、flunarizine、topiramate、propranolol 的預防效果比較 |
| [NCT07655700](https://clinicaltrials.gov/study/NCT07655700) | Phase 4 | 尚未招募 | 177 | Propranolol、flunarizine 及兩者合併用於偏頭痛預防 |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | N/A | 招募中 | 44 | Flunarizine vs propranolol 用於兒童偏頭痛（PedMIDAS） |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | N/A | 未知 | 84 | Flunarizine vs amitriptyline 用於偏頭痛預防 |
| [NCT07751497](https://clinicaltrials.gov/study/NCT07751497) | Phase 2 | 尚未招募 | 400 | Rimegepant vs flunarizine 用於前庭性偏頭痛預防（非劣性） |
| [NCT04766762](https://clinicaltrials.gov/study/NCT04766762) | N/A | 未知 | 96 | 針灸治療無預兆偏頭痛；flunarizine 為既有治療選項 |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | 完成 | 75 | Flunarizine 與 topiramate 的藥物動力學交互作用研究（無療效資料） |
| [NCT07068815](https://clinicaltrials.gov/study/NCT07068815) | Phase 1 | 尚未招募 | 60 | 傅氏皮下針 vs flunarizine 用於無預兆偏頭痛 |

> 另有數個試驗（如 NCT04702971、NCT02747940、NCT04064814、NCT06753825、NCT02580968）與 flunarizine 療效的關聯較間接，未列入。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39365169](https://pubmed.ncbi.nlm.nih.gov/39365169/) | 2024 | 系統性回顧 | Health Technol Assess | 比較成人慢性偏頭痛各種預防藥物的臨床與成本效益 |
| [39388181](https://pubmed.ncbi.nlm.nih.gov/39388181/) | 2024 | 網絡統合分析 | JAMA Netw Open | 評估兒童偏頭痛預防藥物的療效與安全性 |
| [31413170](https://pubmed.ncbi.nlm.nih.gov/31413170/) | 2019 | 指引 | Neurology | AAN/AHS 兒童偏頭痛預防藥物治療指引更新 |
| [40553594](https://pubmed.ncbi.nlm.nih.gov/40553594/) | 2025 | 統合分析 | J Assoc Physicians India | Amitriptyline 與 propranolol、flunarizine 用於偏頭痛預防的比較 |
| [37073858](https://pubmed.ncbi.nlm.nih.gov/37073858/) | 2023 | 系統性回顧 | Cochrane Database Syst Rev | 前庭性偏頭痛預防的藥物介入 |
| [30428122](https://pubmed.ncbi.nlm.nih.gov/30428122/) | 2019 | 臨床研究 | Acta Neurol Scand | Flunarizine 合併經皮眶上神經刺激可改善偏頭痛預防效果 |
| [3878734](https://pubmed.ncbi.nlm.nih.gov/3878734/) | 1985 | 臨床研究 | Cephalalgia | 56 名患者服用 flunarizine 10 mg/日 3 個月，78.5% 頭痛改善 |
| [41572863](https://pubmed.ncbi.nlm.nih.gov/41572863/) | 2026 | Review | Dtsch Arztebl Int | 偏頭痛預防藥物綜述 |
| [28497257](https://pubmed.ncbi.nlm.nih.gov/28497257/) | 2017 | Review | Der Nervenarzt | 預防性治療可選用 β 阻斷劑、三環抗憂鬱藥、flunarizine、抗癲癇藥等 |
| [21049704](https://pubmed.ncbi.nlm.nih.gov/21049704/) | 2010 | Review | J Assoc Physicians India | 首選預防藥物包括 β 阻斷劑、flunarizine、topiramate、valproate、amitriptyline |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-49233 | FURNAZM TAB 5MG | 未提供 | 未提供 |
| HK-41240 | SUZIN CAP 10MG | 未提供 | 未提供 |
| HK-21275 | FLUZINE TAB 5MG | 未提供 | 未提供 |
| HK-61872 | VANID CAPSULES 5MG | 未提供 | 未提供 |
| HK-42370 | SIBERID-5 TAB 5MG | 未提供 | 未提供 |

> 共 9 張有效單方許可證，上表僅列 5 張。

---

## 安全性考量

- **藥物交互作用**：資料顯示 4 筆藥理作用紀錄，涉及 D2 受體及 Cav3.1、Cav3.2、Cav3.3 鈣離子通道，屬藥理靶點資訊，而非具臨床分級的藥物配對交互作用。Flunarizine 與 topiramate 的藥動交互作用曾於 NCT00752466 研究。
- **需留意的風險**：憂鬱、錐體外症狀／類帕金森氏症（尤其是年長者）、體重增加與嗜睡，以及與中樞神經抑制劑併用的風險。這些依據一般藥理知識整理，詳細警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 多項直接比較 flunarizine 與其他偏頭痛預防藥物的臨床試驗（含已完成的 Phase 4 研究），加上多篇系統性回顧與指引，支持其用於偏頭痛預防。
- 但本報告資料中未見已完成且附結果的 Phase 3 RCT，系統評定的 L1 等級宜謹慎看待。Flunarizine 本就是既有的偏頭痛預防藥，這是確認既有用途，不算真正的藥物再利用。

**若要推進需要：**
- 取得香港衛生署許可證的核准適應症與仿單警語、禁忌（目前缺漏）
- 補充詳細的藥物作用機轉資料
- 確認香港本地標示是否已涵蓋偏頭痛預防
- 制定針對憂鬱、錐體外症狀、鎮靜與體重增加的監測計畫，特別是老年族群
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

