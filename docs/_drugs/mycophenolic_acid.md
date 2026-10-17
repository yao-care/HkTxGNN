---
layout: default
title: Mycophenolic Acid
parent: 中證據等級 (L3-L4)
nav_order: 604
evidence_level: L4
indication_count: 5
last_modified_at: 2026-10-14
description: "Mycophenolic Acid：預測新適應症為血紅素病變 (Hemoglobinopathy)（證據等級 L4）。原適應症：本次整理的資料中，許可證未載明核准適應症"
monitor_inn: "MYCOPHENOLIC ACID"
predicted_indications: ["hemoglobinopathy", "migraine disorder", "migraine with brainstem aura", "partial deletion of the short arm of chromosome 16", "beta-thalassemia with other manifestations"]
---

# Mycophenolic Acid
{: .fs-9 }

證據等級: **L4** | 預測適應症: **5** 個
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

# Mycophenolic Acid：從器官移植免疫抑制到血紅素病變（Hemoglobinopathy）

## 一句話總結

Mycophenolic Acid（黴酚酸）是一種免疫抑制劑，在香港已有 12 張有效許可證。
TxGNN 模型預測它可能對**血紅素病變 (Hemoglobinopathy)** 有效，但目前僅有 **1 個間接相關的臨床試驗**和 **1 篇劑量建模文獻**，屬於初步研究線索，證據尚淺。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 本次整理的資料中，許可證未載明核准適應症 |
| 預測新適應症 | 血紅素病變 (Hemoglobinopathy) |
| TxGNN 預測分數 | 99.60% |
| 證據等級 | L4 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 12 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料（原始 MOA 欄位未提供）。依本報告所彙整的預測分析，黴酚酸抑制肌苷單磷酸脫氫酶（IMPDH），進而抑制 T 與 B 淋巴球增生。

在血紅素病變（如地中海型貧血）中，這種免疫抑制作用主要與**異體造血幹細胞移植**有關，也就是預防移植物抗宿主病（GVHD）與排斥反應，而不是直接改善珠蛋白異常這個疾病本身。

TxGNN 的高分（0.996）是模型的計算預測，本身不能證明臨床效益。這裡的合理性主要來自「移植情境下的支持性用藥」，而非對疾病本身的治療作用。

---

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT02342145](https://clinicaltrials.gov/study/NCT02342145) | Phase 4 | 完成 | 205 | 評估 basiliximab 在非親屬異體造血幹細胞移植治療重度地中海型貧血時預防急性 GVHD 的效果與安全性；並非以黴酚酸為試驗藥物，僅屬間接的移植情境證據 |

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [39891881](https://pubmed.ncbi.nlm.nih.gov/39891881/) | 2025 | 劑量建議研究（族群藥動學建模，設計尚待確認） | Eur J Drug Metab Pharmacokinet | 針對接受造血幹細胞移植的地中海型貧血兒童，建立 mycophenolate mofetil 族群藥動學模型並模擬仿單外劑量方案，以補足缺乏的給藥建議 |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-51396 | MYFORTIC GASTRO-RESISTANT TAB 180MG（Novartis） | 腸溶錠 | 資料未載明 |
| HK-51397 | MYFORTIC GASTRO-RESISTANT TAB 360MG（Novartis） | 腸溶錠 | 資料未載明 |
| HK-65062 | APO-MYCOPHENOLIC ACID ENTERIC COATED TABLETS 180MG（Hind Wing） | 腸溶錠 | 資料未載明 |
| HK-65235 | ACCORD MYCOPHENOLIC ACID GASTRO-RESISTANT TABLETS 180MG（I & C） | 腸溶錠 | 資料未載明 |
| HK-67224 | MOFECON-GR 180 GASTRO-RESISTANT TABLETS 180MG（Hovid） | 腸溶錠 | 資料未載明 |

（共 12 張有效單一成分許可證，上表僅列出 5 張。）

---

## 安全性考量

- **藥物交互作用**：資料庫共有 100 筆交互作用紀錄。主要項目如下：
  - **重大（Major）**：活性碳（Activated charcoal）
  - **中度（Moderate）**：多種抗生素（doxycycline、amoxicillin、clarithromycin、minocycline、tetracycline、levofloxacin、metronidazole、vancomycin、kanamycin、paromomycin），以及含鋁、鎂、鈣的制酸劑（如 aluminum hydroxide、magnesium oxide、calcium carbonate）
  - **輕微（Minor）**：鋅（zinc sulfate、zinc acetate）、鐵（iron）

其他警語與禁忌症請參考原廠仿單。

---

## 結論與下一步

**決策：Hold**

**理由：**
- TxGNN 分數雖高，但實際證據只有一個以其他藥物（basiliximab）為主角的 Phase 4 試驗，以及一篇劑量建模研究，皆屬移植情境的間接證據。
- 黴酚酸在此情境的角色是 GVHD 預防，而非治療血紅素病變本身，因此不宜視為真正的「新適應症」。其餘預測（偏頭痛、偏頭痛伴腦幹先兆、16 號染色體短臂部分缺失、β 型地中海型貧血伴其他表現）皆無任何臨床或文獻支持，也缺乏合理的機轉連結。

**若要推進需要：**
- 補齊作用機轉資料與香港仿單的警語、禁忌症及核准適應症。
- 蒐集黴酚酸本身（而非 basiliximab）用於地中海型貧血造血幹細胞移植 GVHD 預防的臨床研究或真實世界資料。
- 釐清此用途是否算新適應症，或僅屬移植免疫抑制的既有用法。
- 進行安全性篩檢，特別是與制酸劑、抗生素等常見併用藥物的交互作用管理。
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

