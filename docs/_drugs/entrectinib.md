---
layout: default
title: Entrectinib
parent: 僅模型預測 (L5)
nav_order: 324
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Entrectinib：預測新適應症為多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)（證據等級 L5）。原適應症：目前資料未載明"
---

# Entrectinib
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Entrectinib：從 NTRK／ROS1 陽性實體腫瘤到多發性內分泌腫瘤

> 說明：本報告以預測排名第 1 的適應症（多發性內分泌腫瘤）為主軸。另有排名第 8 的「女性乳癌」證據明顯較強，已在各章節一併說明，供決策參考。

## 一句話總結

Entrectinib 是 TRK／ROS1／ALK 激酶抑制劑，在香港已有上市許可證。
TxGNN 模型預測它可能對**多發性內分泌腫瘤 (Multiple Endocrine Neoplasia)** 有效，但目前僅有 **1 個臨床試驗**（Phase 1，提前終止，僅收 2 人）和 **1 篇間接文獻**，實質證據非常薄弱。

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前資料未載明（香港許可證未列出核准適應症文字） |
| 預測新適應症 | 多發性內分泌腫瘤 (Multiple Endocrine Neoplasia) |
| TxGNN 預測分數 | 98.58% |
| 證據等級 | L3（僅有間接的機轉／抗藥性研究；無有效的臨床療效資料） |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 2 張 |
| 建議決策 | Hold（列為研究問題） |

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。已知 Entrectinib 可抑制 TRK、ROS1 與 ALK，並在部分情境下對 RET 有活性。

多發性內分泌腫瘤第 2 型 (MEN2) 由 RET 基因的活化型生殖系突變所驅動，因此在激酶訊號傳導上有合理的連結。

不過，Entrectinib 並非選擇性 RET 抑制劑。目前臨床上針對 RET 驅動腫瘤的標準選擇是 selpercatinib、pralsetinib 等選擇性藥物。唯一的文獻是 2024 年關於選擇性 RET 抑制劑抗藥性機制的研究，對 Entrectinib 僅屬間接證據。高預測分數主要是計算模型的結果，尚缺乏實際療效佐證。

## 臨床試驗證據

| 試驗編號 | 階段 | 狀態 | 人數 | 主要發現 |
|---------|------|------|------|---------|
| [NCT03878524](https://clinicaltrials.gov/study/NCT03878524) | Phase 1 | 已終止 | 2 | SMMART PRIME 個人化用藥組合平台試驗；非 MEN 專屬，也非針對 Entrectinib 療效，無可解讀的結果 |

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [38438731](https://pubmed.ncbi.nlm.nih.gov/38438731/) | 2024 | 前臨床／機轉研究 | NPJ Precision Oncology | 探討 RET 驅動癌症對選擇性 RET 抑制劑的抗藥機制；對 Entrectinib 屬間接證據 |

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-66639 | ROZLYTREK CAPSULES 100MG（Roche Hong Kong） | 未載明 | 未載明 |
| HK-66640 | ROZLYTREK CAPSULES 200MG（Roche Hong Kong） | 未載明 | 未載明 |

## 細胞毒性

Entrectinib 為抗腫瘤藥物，屬**標靶藥物**（TRK／ROS1／ALK 激酶抑制劑），非傳統細胞毒性化療藥物。

| 項目 | 內容 |
|------|------|
| 細胞毒性分類 | 標靶藥物（酪胺酸激酶抑制劑） |
| 骨髓抑制風險 | 請參考原廠仿單的警語與注意事項 |
| 致吐性分級 | 請參考原廠仿單的警語與注意事項 |
| 監測項目 | 請參考原廠仿單的警語與注意事項 |
| 處置防護 | 請參考原廠仿單的警語與注意事項 |

## 安全性考量

- **藥物交互作用**：本次共查得 100 筆交互作用紀錄，其中列出者含多項 **Major（嚴重）** 等級：
  - Aprepitant
  - Dexamethasone
  - Clarithromycin
  - Dolasetron

  另有多項 Moderate 等級，例如 Famotidine、Loperamide、Cimetidine、Levofloxacin、Naltrexone 等；Minor 等級包括 Naloxegol、Metronidazole。
- **其他提醒**：文獻中有一例 NTRK 融合陽性大腸癌患者在 Entrectinib 治療期間，雖腫瘤明顯縮小，卻出現肺腫瘤血栓性微血管病變 (PTTM)，提示需留意肺部相關併發症。

警語與禁忌症資料請參考原廠仿單。

## 結論與下一步

**決策：Hold（列為研究問題）**

**理由：**
- 針對多發性內分泌腫瘤，唯一的臨床試驗是提前終止的 Phase 1（2 人），沒有可用的療效資料，Entrectinib 也不是選擇性 RET 抑制劑，高 TxGNN 分數目前只是計算預測。
- 補充：在其他預測適應症中，**女性乳癌**證據較強（Phase 2 basket 試驗 STARTRK-2，n=534，以及 NTRK3 融合分泌型乳癌個案與前臨床研究），可考慮以生物標記（NTRK／ROS1／ALK 融合）篩選的族群為優先方向，建議決策為 Proceed with Guardrails。血小板低下與肺高壓等預測則較像不良事件關聯，而非治療機會。

**若要推進需要：**
- 補齊作用機轉（MOA）資料，並釐清 Entrectinib 對 RET 的實際抑制活性
- 取得香港仿單的警語、禁忌症與核准適應症，以進行安全性篩選
- 針對 RET 突變的 MEN2 或甲狀腺髓樣癌，與選擇性 RET 抑制劑做比較的前臨床或早期臨床研究
- 若轉向乳癌：設計以融合基因陽性為條件的族群與監測計畫
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

