---
layout: default
title: Pipemidic Acid
parent: 僅模型預測 (L5)
nav_order: 702
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Pipemidic Acid：預測新適應症為心臟疾病 (Heart Disease)（證據等級 L5）。原適應症：目前許可證資料未載明核准適應症"
monitor_inn: "PIPEMIDIC ACID"
predicted_indications: ["heart disease", "Laubry-Pezzi syndrome", "Pierre Robin syndrome associated with a chromosomal anomaly", "genetic syndromic Pierre Robin syndrome", "partial deletion of the long arm of chromosome 7"]
---

# Pipemidic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Pipemidic Acid：從泌尿道感染到心臟疾病

## 一句話總結

Pipemidic Acid（吡哌酸）是一種喹諾酮類抗菌藥物，在香港已有上市許可證。
TxGNN 模型預測它可能對**心臟疾病 (Heart Disease)** 有效，但目前**沒有臨床試驗**，僅有 **1 篇**相關性很低的 1978 年文獻，證據實質上僅來自模型預測。

---

## 快速總覽

| 項目 | 內容 |
|------|------|
| 原適應症 | 目前許可證資料未載明核准適應症 |
| 預測新適應症 | 心臟疾病 (Heart Disease) |
| TxGNN 預測分數 | 99.93% |
| 證據等級 | L5 |
| 香港上市 | ✓ 已上市 |
| 許可證數 | 1 張 |
| 建議決策 | Hold |

---

## 為什麼這個預測合理？

目前缺乏詳細的作用機轉資料。根據已知資訊，Pipemidic Acid 屬於喹諾酮類抗菌藥物，一般認為是透過抑制細菌 DNA gyrase 與拓樸異構酶 IV 發揮作用。

**這個預測在機轉上缺乏合理依據。** 該藥沒有已知的心臟保護或心臟治療作用。唯一檢索到的文獻（1978 年）談的是它在腎功能不全與血液透析病人中作為泌尿道以外的抗生素使用，屬於抗感染用途，不能支持用於心臟疾病。0.9993 的高分只是模型預測，並無臨床資料佐證。

此外，喹諾酮類藥物有心臟安全性疑慮（例如 QT 間期延長），因此用於心臟疾病需特別謹慎。

其他排名靠前的預測（Laubry-Pezzi 症候群、Pierre Robin 症候群、第 7 號染色體長臂部分缺失）皆為先天性或染色體疾病，也找不到機轉依據，很可能是知識圖譜中節點相近造成的假象。

---

## 臨床試驗證據

目前無相關臨床試驗登記。

---

## 文獻證據

| PMID | 年份 | 類型 | 期刊 | 主要發現 |
|------|-----|------|------|---------|
| [372558](https://pubmed.ncbi.nlm.nih.gov/372558/) | 1978 | 臨床報告 | Journal d'urologie et de nephrologie | 探討 Pipemidic Acid 作為腎功能不全與血液透析病人的泌尿道外抗生素；與心臟疾病無直接關聯（無摘要可供參考） |

---

## 香港上市資訊

| 許可證號 | 品名 | 劑型 | 核准適應症 |
|---------|------|------|-----------|
| HK-32130 | UROTRACTIN CAP 400MG | 未載明 | 未載明 |

---

## 安全性考量

安全性資訊請參考原廠仿單。

另外，喹諾酮類藥物一般有心臟方面的安全疑慮（如 QT 間期延長），若考慮用於心臟疾病族群需特別留意。

---

## 結論與下一步

**決策：Hold**

**理由：**
- 預測僅來自模型，沒有臨床試驗，唯一的文獻與心臟疾病無關，機轉上也找不到合理連結。
- 抗菌藥物可能帶來心臟安全風險，不宜在缺乏證據下推進。

**若要推進需要：**
- 取得完整作用機轉資料，並確認是否存在任何心臟相關的生物學連結
- 取得香港衛生署仿單，釐清核准適應症、警語與禁忌症
- 進行系統性文獻檢索，確認是否有任何支持心臟疾病用途的前臨床或臨床資料
- 評估 QT 延長等心臟安全風險
## 免責聲明

本內容僅供研究參考，不構成醫療建議。
所有老藥新用預測結果需經過臨床驗證才能應用。

---

