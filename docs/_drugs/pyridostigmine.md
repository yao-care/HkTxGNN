---
layout: default
title: Pyridostigmine
parent: 中證據等級 (L3-L4)
nav_order: 748
evidence_level: L3
indication_count: 7
last_modified_at: 2026-10-14
description: "Pyridostigmine：預測新適應症為重症肌無力合併胸腺增生 (myasthenia gravis with thymus hyperplasia)（證據等級 L3）。原適應症：重症肌無力、成人型重症肌無力、神經肌肉接合部疾病"
monitor_inn: "Pyridostigmine"
predicted_indications: ["autoimmune disease of peripheral nervous system", "disease of receptor activity", "hypersplenism (disease)", "atypical hemolytic-uremic syndrome with B factor anomaly"]
---

# Pyridostigmine
{: .fs-9 }

證據等級: **L3** | 預測適應症: **7** 個
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

# Pyridostigmine：從重症肌無力到重症肌無力合併胸腺增生

## 一句話總結

Pyridostigmine 是可逆性乙醯膽鹼酯酶抑制劑，原本用於重症肌無力及神經肌肉接合部疾病。
TxGNN 模型預測它可能對**重症肌無力合併胸腺增生 (myasthenia gravis with thymus hyperplasia)** 有效。
目前**無臨床試驗登記**，僅有 **3 篇文獻**（1 篇回顧、1 篇個案報告、1 篇世代研究）。此預測本質上屬於原適應症的亞型，並非真正的新適應症。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 重症肌無力、成人型重症肌無力、神經肌肉接合部疾病（許可證未載明適應症文字，此為知識圖譜資料） |
| 預測新適應症 | 重症肌無力合併胸腺增生 (myasthenia gravis with thymus hyperplasia) |
| TxGNN 預測分數 | 99.76% |
| 證據等級 | L3 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 6 張 |
| 建議決策 | Proceed with Guardrails |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。不過 Pyridostigmine 屬於可逆性乙醯膽鹼酯酶抑制劑，可增加神經肌肉接合部突觸間的乙醯膽鹼，是乙醯膽鹼受體 (AChR) 抗體陽性重症肌無力的標準症狀治療。

胸腺增生是 AChR 抗體陽性重症肌無力的常見表現型，因此這項預測屬於原適應症的亞型，並非真正的藥物再利用。

需特別注意：在 MuSK 抗體陽性的患者，膽鹼酯酶抑制劑常耐受性不佳或效果有限。文獻中「MuSK 陽性合併胸腺增生」的個案報告，不能視為療效證據。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [25683765](https://pubmed.ncbi.nlm.nih.gov/25683765/) | 2015 | Cohort | Journal of Neurology | 回顧 39 例非胸腺瘤晚發型重症肌無力患者，分析胸腺切除後 2 年預後 |
| [34225443](https://pubmed.ncbi.nlm.nih.gov/34225443/) | 2021 | Review | Molecular Medicine Reports | 重症肌無力的基因體、表現型與表觀遺傳回顧，涵蓋自體抗體機轉 |
| [18053719](https://pubmed.ncbi.nlm.nih.gov/18053719/) | 2008 | Case report | Neuromuscular Disorders | MuSK 陽性重症肌無力合併胸腺增生，以垂頭症候群為主要表現（不支持 Pyridostigmine 療效） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-03376 | MESTINON TAB 60MG | 未提供 | 未提供 |
| HK-03386 | MESTINON TAB 10MG | 未提供 | 未提供 |
| HK-56949 | JM-PYRIDOSTIGMINE TAB 10MG | 未提供 | 未提供 |
| HK-67155 | PYRINON TABLETS 60MG | 未提供 | 未提供 |
| HK-56950 | JM-PYRIDOSTIGMINE TAB 60MG | 未提供 | 未提供 |

此外尚有 HK-58081（MESTINON TAB 60MG），共 6 張有效單方許可證。

---

## 安全性考量

- **知識圖譜標示的禁忌疾病**：腎臟疾病、輸尿管積膿、氣喘（含內因性及過敏性氣喘）、泌尿道阻塞。此資料來自知識圖譜，並非仿單內容。
- **藥物交互作用**：共查得 78 筆，以下為部分中度交互作用：
  - 皮質類固醇：氫化可體松、潑尼松、潑尼松龍、地塞米松、倍他米松、曲安奈德、布地奈德
  - 抗膽鹼藥物：阿托品、東莨菪鹼、hyoscyamine、glycopyrronium、dicyclomine、propantheline、trospium 等
  - 胺基糖苷類抗生素：新黴素、卡那黴素、巴龍黴素

其餘仿單警語與禁忌請參考原廠仿單。

---

## 結論與下一步

**決策：Proceed with Guardrails**

**理由：**
- Pyridostigmine 是 AChR 抗體陽性重症肌無力的標準症狀治療，胸腺增生為其常見亞型，機轉上合理且已在香港上市。
- 但針對此亞型的直接證據有限（無臨床試驗，文獻僅 3 篇且無對照研究），且 MuSK 陽性患者可能反應不佳。

**若要推進需要：**
- 確認患者抗體型別（AChR 或 MuSK），MuSK 陽性者不宜預期療效
- 取得香港衛生署核准適應症文字與仿單的警語、禁忌資料
- 針對氣喘、腎病、泌尿道阻塞患者及併用類固醇或抗膽鹼藥物者，建立安全性監測計畫
- 補充詳細的作用機轉資料
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

