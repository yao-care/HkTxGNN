---
layout: default
title: Tizanidine
parent: 僅模型預測 (L5)
nav_order: 884
evidence_level: L5
indication_count: 5
---

# Tizanidine
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

# Tizanidine：從痙攣性肌張力異常到偏頭痛

## 一句話總結

Tizanidine 是中樞性 α2 腎上腺素受體促效劑，在香港已有上市許可證，但本次整理的資料未載明其核准適應症文字。
TxGNN 模型預測它可能對**偏頭痛 (Migraine Disorder)** 有效，
目前有 **1 個直接相關的 Phase 3 臨床試驗**（狀態未知、尚無結果）和 **16 篇文獻**支持這個方向，其中包含 1 篇針對慢性每日頭痛的雙盲安慰劑對照試驗。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 資料未載明（香港許可證未記錄核准適應症文字） |
| 預測新適應症 | 偏頭痛 (Migraine Disorder) |
| TxGNN 預測分數 | 99.79% |
| 證據等級 | L1（暫定，見下方說明） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Proceed with Guardrails |

**證據等級說明：** 嚴格依判定規則，L1 需有 ≥2 個已完成的 Phase 3 RCT。目前唯一的偏頭痛 Phase 3 試驗（NCT05484349）狀態為「未知」且無結果，因此 L1 屬暫定判斷，實際證據強度應視為低於 L1，確認試驗結果後才能定案。

---

## 為什麼這個預測合理？

目前缺乏經核實的詳細作用機轉資料。就藥理類別而言，Tizanidine 屬中樞性 α2 腎上腺素受體促效劑。可能的機轉包括降低三叉神經痛覺傳導與中樞敏感化，並減輕頸部與頭部周圍的肌肉張力，而這些都被認為與偏頭痛及慢性每日頭痛有關。

在現有文獻中，Tizanidine 曾被評估作為慢性每日頭痛（含慢性偏頭痛）的預防性治療。一項雙盲、安慰劑對照、多中心試驗（PMID 12167135）以及一項開放標籤劑量滴定研究（PMID 11318882）針對此族群進行。不過這些族群與「發作性偏頭痛」並不完全相同，且多數文獻為回顧性綜述，直接證據有限。

TxGNN 的高分（99.79%）與上述機轉及文獻方向一致，但這是模型預測，不能取代臨床試驗結果。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT05484349](https://clinicaltrials.gov/study/NCT05484349) | Phase 3 | 未知 | 189 | 多中心、隨機、雙盲、安慰劑對照，評估口服 Tizanidine 預防成人發作性偏頭痛的療效與安全性（預計 2023-06 至 2025-12），尚無結果 |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | N/A | 完成 | 300 | 外用非類固醇消炎藥止痛效果的觀察性研究，與 Tizanidine 及偏頭痛關聯薄弱 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [12167135](https://pubmed.ncbi.nlm.nih.gov/12167135/) | 2002 | RCT | Headache | Tizanidine 作為慢性每日頭痛輔助預防治療的雙盲安慰劑對照多中心研究 |
| [11318882](https://pubmed.ncbi.nlm.nih.gov/11318882/) | 2001 | 開放標籤研究 | Headache | Tizanidine 用於慢性每日頭痛預防的劑量滴定療效與耐受性評估 |
| [20464578](https://pubmed.ncbi.nlm.nih.gov/20464578/) | 2010 | 雙盲安慰劑對照試驗回顧 | Neurol Sci | 回顧慢性偏頭痛藥物預防的雙盲安慰劑對照試驗 |
| [12696998](https://pubmed.ncbi.nlm.nih.gov/12696998/) | 2003 | Review | CNS Drugs | 探討 baclofen、tizanidine、肉毒桿菌毒素等肌張力藥物預防偏頭痛與緊張型頭痛的角色 |
| [31365643](https://pubmed.ncbi.nlm.nih.gov/31365643/) | 2019 | 共識指引 | Arq Neuropsiquiatr | 巴西頭痛學會慢性偏頭痛治療共識 |
| [15115635](https://pubmed.ncbi.nlm.nih.gov/15115635/) | 2004 | Review | Curr Pain Headache Rep | 回顧偏頭痛預防的新興治療選項，包含 tizanidine |
| [17115988](https://pubmed.ncbi.nlm.nih.gov/17115988/) | 2006 | Review | Headache | 慢性每日頭痛的預防性治療 |
| [40983294](https://pubmed.ncbi.nlm.nih.gov/40983294/) | 2025 | 前臨床／製劑研究 | J Control Release | Tizanidine 與 meloxicam 超分子自組裝共晶，增強抗偏頭痛效果 |
| [11903539](https://pubmed.ncbi.nlm.nih.gov/11903539/) | 2002 | 臨床報告 | Headache | 低劑量 Tizanidine 搭配 NSAID 用於藥物過度使用性頭痛的戒斷 |
| [20442572](https://pubmed.ncbi.nlm.nih.gov/20442572/) | 2010 | Review | Curr Opin Neurol | 慢性偏頭痛治療的新進展 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-62119 | ZITANID TABLETS 2MG | 錠劑（依品名推斷，資料未載明） | 資料未載明 |
| HK-39067 | SIRDALUD TAB 2MG | 錠劑（依品名推斷，資料未載明） | 資料未載明 |

---

## 安全性考量

- **知識圖譜標示的相關疾病禁忌（非仿單原文）**：肝衰竭、腎臟疾病、膿尿輸尿管 (pyoureter)、精神病性障礙、類精神分裂症、精神疾患、情感性分裂症、低血壓性疾患。
- **藥物交互作用**：資料庫共記錄 100 筆，以下為部分示例：
  - 重大 (Major)：Famotidine、Cimetidine、Morphine、Dolasetron、Obeticholic acid
  - 中度 (Moderate)：Clarithromycin、Levofloxacin、Metoclopramide、Atropine、Hyoscyamine、Loperamide、Naltrexone 等

仿單的警語與禁忌資料尚未取得，其他安全性資訊請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- 已有針對偏頭痛的 Phase 3 試驗登記，且有慢性每日頭痛的 RCT 作為間接支持，方向合理。但該 Phase 3 試驗狀態未知、尚無結果，證據不足以直接 Go。
- 其他預測適應症（腦幹先兆偏頭痛、偏頭痛易感性、Tourette 症候群）證據薄弱；萎縮性蠕蟲狀皮膚病（atrophoderma vermiculata）則無機轉關聯與任何研究，目前均不建議推進。

**若要推進需要：**
- 確認 NCT05484349 的現況與結果，並確認是否有 ≥2 個已完成的 Phase 3 RCT 以支持 L1
- 取得並解析香港仿單，補齊警語、禁忌與核准適應症
- 補充 DrugBank 的作用機轉資料
- 針對肝腎功能不全、精神疾患、低血壓族群及高風險藥物交互作用（如 CYP1A2 抑制劑類）制定用藥監測計畫
- 釐清發作性偏頭痛與慢性每日頭痛族群之間的證據落差
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

