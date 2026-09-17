---
layout: default
title: Propofol
parent: 高證據等級 (L1-L2)
nav_order: 620
evidence_level: L2
indication_count: 5
---

# Propofol
{: .fs-9 }

證據等級: **L2** | 預測適應症: **5** 個
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

# Propofol：從全身麻醉到偏頭痛（Migraine Disorder）

## 一句話總結

Propofol 是臨床廣泛使用的靜脈全身麻醉/鎮靜藥物。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
目前有 **5 個臨床試驗**和 **20 篇文獻**支持這個方向。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 全身麻醉／鎮靜（本次資料包未提供正式核准適應症文字） |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.69% |
| 證據等級 | L2 |
| 香港上市 | 未上市 |
| 許可證數 | 0 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

Propofol 目前缺乏正式登錄的作用機轉資料（原廠仿單/DrugBank MOA 為資料缺口）。但根據本資料包內證據推論，Propofol 為 **GABA-A 受體激動劑**，具中樞鎮靜、抗痛覺敏感作用，並能抑制「皮質擴散抑制 (cortical spreading depression)」——這正是偏頭痛神經血管理論中被認為與偏頭痛先兆及疼痛產生相關的關鍵現象。

低劑量（遠低於麻醉劑量）Propofol 在急診實務中已被多次作為頑固性/急性偏頭痛的 rescue therapy 使用，且在成人與兒童族群皆有臨床試驗與病例系列支持。這使得「麻醉鎮靜用藥」跨界到「偏頭痛急性期治療」在機轉上具有合理性，但仍需注意：此用途為低於麻醉劑量的短暫靜脈給藥，與原本的全身麻醉適應症在給藥情境上有本質差異。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | 已完成 | 74 | 小兒偏頭痛急診室誘導療法，低劑量 propofol 之安全性與療效評估，回溯性資料顯示可能優於標準治療 |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | NA | 已完成 | 40 | 小兒偏頭痛，低劑量 propofol 輸注作為誘導性治療，評估療效、安全劑量上限與作用持續時間 |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | NA | 已終止 | 12 | 成人重度頑固性偏頭痛之低劑量 propofol 治療，因樣本數過小而提前終止，提示招募/耐受性挑戰 |

> 另有 2 個試驗（NCT02443220 電針麻醉研究、NCT03789370 全麻藥物與術後頭痛比較）與偏頭痛治療相關性較低（Grade C），未列入上表。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | 2025 美國頭痛學會（AHS）更新急診偏頭痛靜脈藥物治療指引 |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Systematic Review | Acad Emerg Med | 系統性回顧 Propofol 用於急診急性偏頭痛之安全性與療效證據 |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | Arch Acad Emerg Med | Propofol+Granisetron 與 Propofol+Metoclopramide 比較急性偏頭痛症狀控制 |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | J Emerg Med | 低劑量 Propofol 用於小兒偏頭痛之前瞻性隨機對照試驗 |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | Arch Acad Emerg Med | Sumatriptan 併用 Propofol 對比單用 Sumatriptan 治療急性偏頭痛 |
| [32705801](https://pubmed.ncbi.nlm.nih.gov/32705801/) | 2020 | RCT (pilot) | Emerg Med Australas | 急診偏頭痛 Propofol 程序鎮靜劑量對比標準治療之先導性隨機對照試驗 |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Cohort | Expert Rev Neurother | Propofol 於次麻醉劑量下用於治療頑固性/難治性偏頭痛的完整藥物側寫 |
| [32638172](https://pubmed.ncbi.nlm.nih.gov/32638172/) | 2020 | Review | Curr Pain Headache Rep | 兒童青少年偏頭痛靜脈治療回顧，門診效果不足時的急診治療選項 |
| [32410204](https://pubmed.ncbi.nlm.nih.gov/32410204/) | 2020 | Review | Curr Neurol Neurosci Rep | 兒童青少年頭痛之急診/住院處置最新證據回顧 |
| [22309235](https://pubmed.ncbi.nlm.nih.gov/22309235/) | 2012 | Review | Headache | 急性偏頭痛急救治療系列文章：神經鬆弛劑、抗組織胺及 propofol 等其他藥物 |

---

## 香港上市資訊

Propofol 目前**未在香港上市**，本資料包中無相關許可證資料可供列出。

---

## 安全性考量

安全性資訊請參考原廠仿單。

> 註：本次資料收集中，TFDA 仿單警語/禁忌（DG001）標記為 **Blocking** 等級資料缺口，尚未取得，直接影響後續安全性初評（S1）的進行。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有多篇 RCT（含 2 篇急診情境隨機對照試驗）及 2026 年 AHS 最新指引提及 propofol 於急性偏頭痛的角色，機轉上與皮質擴散抑制假說相容，證據等級達 L2。
- 但其中一項成人試驗因樣本過小而終止，顯示招募與耐受性仍有挑戰；且藥物目前未在香港上市，無在地法規路徑與許可證基礎。
- 其餘 4 個 TxGNN 預測適應症（腦幹型偏頭痛先兆、Prinzmetal 心絞痛、腎因性抗利尿激素不當分泌症候群、妥瑞氏症）證據等級為 L3–L5，多為麻醉/鎮靜相關的間接觀察或個案報告，非治療性證據，建議狀態均為 **Hold**。

**若要推進需要：**
- 補齊 TFDA 仿單警語與禁忌資料（DG001，Blocking，需優先解決）
- 補充 DrugBank 作用機轉資料（DG002）以完善機轉關聯性分析
- 若考慮香港市場，需評估上市/特殊藥品申請路徑（目前 0 張許可證）
- 補充成人族群更大樣本的 RCT 數據，釐清 NCT02492295 提前終止之原因
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

